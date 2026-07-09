"""Constants and configuration for the FII/DII dashboard."""

from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "fiidii.db"
NIFTY_TICKER = "^NSEI"
CATEGORIES = ["FII/FPI", "DII"]
ROLLING_WINDOWS = {"7D": 7, "30D": 30}

# nse_fiidii() column mapping
COLUMN_MAP = {
    "buyValue": "buy_value",
    "sellValue": "sell_value",
    "netValue": "net_value",
}
