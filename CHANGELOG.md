# Changelog

## v0.2.0 (2026-07-09)

- Premium UI refresh — Lucide SVG icons for FII/DII metrics, section headers, sidebar
- Design token CSS — cleaner cards, consistent spacing, improved readability
- Empty states for no-data sections (charts, MTD, today's snapshot)
- Collapsed chart mode bars for cleaner look
- Streamlined layout — regular headers, proper dividers, compact footer
- Fixed missing `httpx` dependency in requirements.txt — resolves Streamlit Cloud import error

## v0.1.0 (2026-07-09)

- Initial release
- FII/DII data fetching from NSE India via nsepython
- SQLite storage with daily snapshots
- Interactive Plotly charts: trend, comparison, rolling averages, Nifty overlay
- Date range filtering and CSV export
- Lazy-fill pattern — no cron needed on Streamlit Cloud
