# /// script
# requires-python = ">=3.12"
# ///

from __future__ import annotations

import json
import time
from pathlib import Path
from urllib import request
from urllib.error import HTTPError, URLError

TICKERS = ["FPT", "VCB", "MWG", "VIC"]
TARGET_YEARS = range(2021, 2026)
EXCHANGE = "HOSE"
LANGUAGE = "VN"
USER_AGENT = "Vietnam Equity Research Assistant  phanvinhphu1@gmail.com"
BASE_URL = "https://static2.vietstock.vn/data"
OUTPUT_DIR = Path(__file__).resolve().parent
MANIFEST_PATH = OUTPUT_DIR / "manifest.json"
REQUEST_PAUSE_SECONDS = 0.5

DOCUMENT_TYPES = {
    "BCTN": {
        "folder": "BCTN",
        "period": None,
        "stem": "{ticker}_Baocaothuongnien_{year}",
    },
    "BCTC_HOPNHAT": {
        "folder": "BCTC",
        "period": "NAM",
        "stem": "{ticker}_Baocaotaichinh_{year}_Kiemtoan_Hopnhat",
    },
}


def download_file(url: str) -> bytes:
    req = request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/pdf"},
    )
    with request.urlopen(req, timeout=60) as response:
        content = response.read()
    if not content.startswith(b"%PDF-"):
        raise RuntimeError(f"Not a PDF: {url}")
    return content


def download_report(ticker: str, year: str, doc_key: str, doc: dict) -> dict:
    stem = doc["stem"].format(ticker=ticker, year=year)
    dest = OUTPUT_DIR / ticker / year / doc["folder"] / f"{stem}.pdf"
    relative_path = dest.relative_to(OUTPUT_DIR).as_posix()

    if dest.exists():
        print("skip (exists):", dest)
        return {
            "run": "skipped",
            "status": "downloaded",
            "path": relative_path,
            "size_bytes": dest.stat().st_size,
        }

    parts = [BASE_URL, EXCHANGE, year, doc["folder"], LANGUAGE]
    if doc["period"]:
        parts.append(doc["period"])
    prefix = "/".join(parts) + f"/{stem}"
    urls = [f"{prefix}.pdf", f"{prefix}/{stem}.pdf"]

    for url in urls:
        print("GET", url)
        try:
            content = download_file(url)
        except (HTTPError, URLError, TimeoutError, RuntimeError) as exc:
            print("failed:", exc)
            time.sleep(REQUEST_PAUSE_SECONDS)
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(content)
        print("saved:", dest, dest.stat().st_size, "bytes")
        time.sleep(REQUEST_PAUSE_SECONDS)
        return {
            "run": "downloaded",
            "status": "downloaded",
            "path": relative_path,
            "size_bytes": dest.stat().st_size,
        }

    print(f"FAILED: {ticker} {year} {doc_key}")
    return {
        "run": "failed",
        "status": "failed",
        "path": relative_path,
        "size_bytes": 0,
    }


def write_manifest(manifest: dict) -> None:
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    skipped = 0
    downloaded = 0
    failed: list[str] = []
    manifest: dict = {}

    for ticker in TICKERS:
        for year in TARGET_YEARS:
            year_key = str(year)
            for doc_key, doc in DOCUMENT_TYPES.items():
                record = download_report(ticker, year_key, doc_key, doc)
                manifest.setdefault(ticker, {}).setdefault(year_key, {})[doc_key] = {
                    "path": record["path"],
                    "status": record["status"],
                    "size_bytes": record["size_bytes"],
                }
                match record["run"]:
                    case "skipped":
                        skipped += 1
                    case "downloaded":
                        downloaded += 1
                    case "failed":
                        failed.append(f"{ticker} {year_key} {doc_key}")
                    case other:
                        raise RuntimeError(f"unknown result: {other}")

    write_manifest(manifest)

    total = skipped + downloaded + len(failed)
    dataset_bytes = sum(
        entry["size_bytes"]
        for years in manifest.values()
        for docs in years.values()
        for entry in docs.values()
    )

    print()
    print("Download complete")
    print()
    print(f"Total:       {total}")
    print(f"Skipped:     {skipped}")
    print(f"Downloaded:  {downloaded}")
    print(f"Failed:      {len(failed)}")
    print(f"Dataset:     {dataset_bytes / (1024 * 1024):.1f} MB")
    print(f"Manifest:    {MANIFEST_PATH}")
    if failed:
        print()
        print("Failed documents:")
        for item in failed:
            print(f"- {item}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
