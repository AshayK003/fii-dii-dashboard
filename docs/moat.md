# NSE FII/DII Data Dashboard — Competitive Moat

## Defensibility Strategy

This is a **data moat** project. The code is trivial (fetch → store → plot). The defensibility comes from:

### 1. Historical Data Accumulation
Every day the app runs, it collects another snapshot. After 6+ months, the SQLite database itself becomes the moat — no one starting fresh can show a year of FII/DII trends without waiting.

### 2. Zero-Maintenance Architecture
- Streamlit Cloud = free hosting, zero ops
- SQLite = no database server, file-based
- nsepython = zero API keys
- Lazy-fill pattern = no cron needed

### 3. AGPL v3 License
Anyone can use, modify, fork — but can't close-source and monetize without open-sourcing their changes.

## Non-Goals
- Not building a SaaS or charging for this
- Not competing with institutional terminals (Bloomberg, Reuters)
- Not adding trading signals/alerts (pure research tool)
