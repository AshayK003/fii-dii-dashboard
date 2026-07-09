# NSE FII/DII Data Dashboard — Build Plan

## Milestones

| Phase | Tasks | Est. Time |
|-------|-------|-----------|
| **P0** | Core data pipeline (fetch → store → display) | 1 session |
| **P0.1** | Trend chart with date range filter | Same session |
| **P1** | Nifty overlay + rolling averages | Same session |
| **P1.1** | CSV export + polish | Same session |
| **Ship** | Git init + Streamlit Cloud deploy | 15 min |

## Build Order (Phase 4 — TDD)

### Step 1: Project scaffolding
- pyproject.toml / requirements.txt
- `src/__init__.py`, `tests/__init__.py`
- DB schema + init in `db.py`

### Step 2: Database layer (test first)
- `test_db.py` — init, insert, query_all, query_range
- `db.py` — SQLite CRUD

### Step 3: Fetch layer (test first)
- `test_fetch.py` — parse_fiidii(), fetch_nifty()
- `fetch.py` — nse_fiidii() wrapper with string→float parsing + yfinance nifty

### Step 4: Chart module (test first)
- `test_charts.py` — trend chart, overlay chart, rolling avg
- `charts.py` — Plotly chart builders

### Step 5: App shell
- `app.py` — Streamlit layout, wire everything

### Step 6: Polish & ship
- CSV export button
- README, CHANGELOG, LICENSE
- Deploy to Streamlit Cloud
