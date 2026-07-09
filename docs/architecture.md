# NSE FII/DII Data Dashboard — Architecture

## System Design

```
┌──────────────────────┐
│   Web Browser        │
│   (streamlit.app)    │
└─────────┬────────────┘
          │ HTTPS
┌─────────▼────────────────────────┐
│  Streamlit App (app.py)          │
│                                  │
│  ┌───────────┐  ┌─────────────┐  │
│  │ Fetcher   │  │ Charts      │  │
│  │ Module    │  │ Module      │  │
│  │ (fetch)   │  │ (charts)    │  │
│  └─────┬─────┘  └─────────────┘  │
│        │                          │
│  ┌─────▼──────────────────────┐  │
│  │  Database Module (db)      │  │
│  │  - SQLite                  │  │
│  │  - Session: fii_dii_data   │  │
│  └─────┬──────────────────────┘  │
└────────┼──────────────────────────┘
         │
┌────────▼──────────────────────────┐
│  External Sources                 │
│  - nsepython.nse_fiidii() (NSE)   │
│  - yfinance ^NSEI (Nifty price)   │
└───────────────────────────────────┘
```

## Data Flow

1. **App Load:** Check SQLite for today's snapshot
2. **If missing:** Call nse_fiidii() → parse → store in SQLite
3. **If exists:** Use cached data (session state)
4. **Render:** Fetch all history from SQLite → plot charts

## Database Schema

```sql
CREATE TABLE IF NOT EXISTS fii_dii_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,                -- DD-Mon-YYYY (e.g., 08-Jul-2026)
    category TEXT NOT NULL,            -- 'FII/FPI' or 'DII'
    buy_value REAL NOT NULL,           -- ₹ Crores
    sell_value REAL NOT NULL,
    net_value REAL NOT NULL,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(date, category)
);

-- Index for fast date-range queries
CREATE INDEX IF NOT EXISTS idx_fii_dii_date ON fii_dii_data(date);
```

## Module Structure

```
src/
├── app.py              # Streamlit entry point — layout, sidebar, pages
├── db.py               # SQLite init, insert, query helpers
├── fetch.py            # nse_fiidii() wrapper + parsing + Nifty fetch
├── charts.py           # Plotly chart builders (trend, overlay, rolling)
├── config.py           # Constants, settings, categories
└── __init__.py

tests/
├── test_db.py
├── test_fetch.py
├── test_charts.py
└── __init__.py
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Lazy-fill instead of cron** | Streamlit Cloud has no scheduler — fetch on app open if today's data missing |
| **Session state cache** | Avoid re-fetch on every rerun (8.5s is slow) |
| **Normalize all values to float** | nse_fiidii() returns strings — parse immediately on insert |
| **Nifty overlay via yfinance** | Separate fetch, synced to same date axis |
| **Rolling averages computed in SQL/query** | 7-day and 30-day avg as SQL window functions or pandas rolling |
| **One-file-per-module** | Keeps it simple — no over-engineering for a 5-module app |

## Non-Functional Requirements

- **Cold start:** ≤15s (includes 8.5s for nse_fiidii if today missing)
- **Warm load:** ≤2s (cached in session state)
- **DB size:** ~5KB/year (365 days × 2 categories × ~50 bytes)
- **Zero deps beyond:** streamlit, pandas, plotly, nsepython, yfinance, sqlite3 (stdlib)
