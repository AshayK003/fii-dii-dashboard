# NSE FII/DII Dashboard — Product Management Spec

## Executive Summary
A free, open-source Streamlit dashboard that scrapes daily FII/DII data from NSE India, stores historical snapshots in SQLite, and provides interactive trend charts with Nifty overlay and rolling averages. Pure research tool — no trading signals, no notifications.

## Target Persona
**Indian retail equity investor** who checks FII/DII data daily but has no tool to track historical trends. Currently checking NSE website (current day only) or Moneycontrol (limited history).

## Jobs To Be Done
1. "Check today's FII/DII net flows at a glance"
2. "See how FII/DII activity has trended over the past week/month"
3. "Compare FII vs DII activity side by side"
4. "Correlate FII flows with Nifty price movement"
5. "Export data for my own analysis"

## Feature Evaluation

| Feature | Customer Value | Eng Cost (higher=cheaper) | Build? |
|---------|---------------|--------------------------|--------|
| Current day FII/DII display | 10/10 | 9/10 — 2 lines from nsepython | ✅ Build |
| Historical SQLite storage | 9/10 | 8/10 — stdlib sqlite3 | ✅ Build |
| Net flow trend chart | 9/10 | 8/10 — Plotly line chart | ✅ Build |
| Nifty price overlay | 7/10 | 7/10 — yfinance + dual axis | ✅ Build |
| 7d/30d rolling averages | 8/10 | 8/10 — pandas rolling | ✅ Build |
| CSV export | 5/10 | 9/10 — st.download_button | ✅ Build |
| FII vs DII comparison | 8/10 | 8/10 — dual line or stacked | ✅ Build |
| Category breakdown (equity/debt) | 6/10 | 3/10 — nse_fiidii doesn't provide this | ❌ Not possible at source |

## Acceptance Criteria (P0)
- [x] User can see current day FII and DII buy/sell/net values
- [ ] User can view an interactive line chart of net FII/DII over selectable date range
- [ ] Data persists across sessions (SQLite)
- [ ] Missing today's data auto-fetches on app open
- [ ] Dashboard works on Streamlit Cloud free tier

## Acceptance Criteria (P1)
- [ ] Nifty closing price overlaid on FII/DII trend
- [ ] 7-day and 30-day rolling averages of net flow
- [ ] CSV download button
- [ ] Date range filter

## Success Metrics
- Cold start < 15s
- Warm load < 2s
- Zero manual maintenance
- Data accuracy matches NSE source exactly

## Non-Goals
- No trading signals, no alerts, no notifications
- No user accounts or authentication
- No real-time intraday data
