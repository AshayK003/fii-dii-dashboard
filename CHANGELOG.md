# Changelog

## v0.2.0 (2026-07-09)

- Premium UI refresh — Lucide SVG icons for FII/DII metrics, section headers, sidebar
- Design token CSS — cleaner cards, consistent spacing, improved readability
- Empty states for no-data sections (charts, MTD, today's snapshot)
- Collapsed chart mode bars for cleaner look
- Streamlined layout — regular headers, proper dividers, compact footer
- **[FIX]** Lazy-import all optional deps (nsepython, yfinance, httpx, plotly, pandas in charts)
  — prevents crash on startup when any dep fails to install on Streamlit Cloud
- **[FIX]** Each lazy import wrapped in try/except with graceful fallback (returns None/[])
- **[FIX]** Chart rendering guarded: if plotly unavailable, shows empty-state message
- **[FIX]** NaT.date() crash when all dates fail to parse — dropna() guard before .date()
- **[FIX]** get_monthly_rollup strptime crash on bad date strings — try/except skip
- **[FIX]** SVG HTML in st.button/st.download_button labels rendered as raw text
  — moved SVGs to st.markdown above buttons; labels are plain text
- **[FIX]** Removed nsepython, yfinance, httpx, pytest from requirements.txt
  — only install what's needed at module-load time (streamlit, pandas, plotly)

## v0.1.0 (2026-07-09)

- Initial release
- FII/DII data fetching from NSE India via nsepython
- SQLite storage with daily snapshots
- Interactive Plotly charts: trend, comparison, rolling averages, Nifty overlay
- Date range filtering and CSV export
- Lazy-fill pattern — no cron needed on Streamlit Cloud
