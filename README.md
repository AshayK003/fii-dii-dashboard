# NSE FII/DII Data Dashboard

Track daily Foreign Institutional Investor (FII) and Domestic Institutional Investor (DII) flows from NSE India with historical trends, interactive charts, and Nifty correlation.

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.35%2B-red)
![License](https://img.shields.io/badge/license-AGPL%20v3-green)
![UI](https://img.shields.io/badge/ui-premium-22C55E)

## Features

- **Live FII/DII data** — Auto-fetches daily from NSE India
- **Premium UI** — Lucide SVG icons, design-token CSS, clean metric cards
- **Historical persistence** — Every day's data saved to SQLite for trend analysis
- **4 interactive charts** — Net flow trend, FII vs DII comparison, rolling averages, Nifty overlay
- **Date range filtering** — Zoom into any period
- **CSV export** — Download raw data for your own analysis
- **Zero maintenance** — Lazy-fill pattern, no cron jobs, no API keys

## How It Works

1. Open the app → checks SQLite for today's FII/DII snapshot
2. If missing → fetches from NSE India via `nsepython` (~8.5s)
3. Data stored locally in SQLite → accumulates over time
4. Interactive Altair charts render from stored history

![Screenshot](https://via.placeholder.com/800x400?text=FII/DII+Dashboard)

## Quick Start

```bash
git clone https://github.com/AshayK003/fii-dii-dashboard
cd fii-dii-dashboard
pip install -r requirements.txt
streamlit run app.py
```

## Deploy

[![Deploy to Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

Connect your GitHub repo to Streamlit Cloud — no config needed.

## Tech Stack

| Component | Choice | Why |
|-----------|--------|-----|
| Dashboard | Streamlit | Free hosting, Python-native |
| Storage | SQLite | Zero infra, stdlib, file-based |
| Charts | Altair | Zero extra deps - ships with Streamlit |
| Data source | nsepython | Only working NSE FII/DII API |
| Nifty prices | yfinance | Reliable, free, no API key |

## License

AGPL v3 — free to use, modify, and share. Cannot be closed-sourced or monetized without open-sourcing your changes.
