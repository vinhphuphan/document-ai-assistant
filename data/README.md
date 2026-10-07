# Data

Local data artifacts used for development.

- Raw Vietnamese financial reports are organized directly under `<ticker>/<year>/{BCTN,BCTC}/`.
- The demo corpus covers FPT, VCB, MWG, and VIC for 2021–2025: annual reports (BCTN) and consolidated annual financial statements (BCTC).
- Downloaded files are gitignored because the corpus can become large.
- Fetch the sample corpus with `uv run data/download.py`.