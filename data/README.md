# Data

Local data artifacts for development live here

- `downloads/` hold the raw source files fetches from SEC EDGAR, grouped by year.
- Downloaded payloads are gitignored because the corpus can be large.
- Fetch a sample corpus with `uv run data/download.py`