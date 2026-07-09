# NSE FII/DII Data Dashboard — Strategic Intelligence

## Problem
FII/DII data is a key market sentiment indicator for Indian equities. Retail investors check it daily but have no dedicated tool to track historical trends — NSE's website only shows current day, and most portfolio tools skip institutional flow data.

## Users
- **Indian retail equity investors** — primary audience
- **Swing traders** — track FII/DII conviction shifts
- **Open-source community** — use the data layer for their own analysis

## Requirements (P0/P1)

| Priority | Requirement | Source |
|----------|-------------|--------|
| P0 | Fetch current-day FII/DII data from NSE | nsepython.nse_fiidii() |
| P0 | Store daily snapshots in SQLite | Historical trends |
| P0 | Display current day figures (buy/sell/net per category) | Dashboard |
| P0 | Historical trend charts (net value over time) | Dashboard |
| P1 | Nifty 50 overlay on trends | Correlation analysis |
| P1 | 7-day/30-day rolling averages of net flow | Smoothing |
| P1 | Category breakdown (FII vs DII comparison) | Side-by-side view |
| P1 | Data export (CSV download) | Utility |

## Data Sources

| Source | What | Reliability | Speed |
|--------|------|-------------|-------|
| nsepython.nse_fiidii() | FII/DII daily buy/sell/net (₹ Cr) | ✅ Working (Jun 2026) | ~8.5s |
| yfinance | Nifty 50 price (^NSEI) | ✅ Very reliable | ~0.5s |
| Fallback: Upstox API | Same FII/DII data + more | ✅ With account | ~1s |

## Competitor Landscape

| Tool | FII/DII tracking | Historical trends | Free |
|------|------------------|-------------------|------|
| NSE India website | ✅ Current day only | ❌ | ✅ |
| Moneycontrol | ✅ Limited | ❌ | ✅ |
| TradingView | ✅ With paid plan | ✅ | ❌ |
| Upstox/Trading apps | ✅ Basic | ❌ | ✅ |
| **FII/DII Dashboard** | **✅ Full** | **✅ Yes** | **✅ OSS** |
