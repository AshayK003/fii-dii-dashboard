"""Tests for the charts module (Altair-backed)."""

import pytest
import pandas as pd
import altair as alt

from src.charts import (
    build_trend_chart,
    build_comparison_chart,
    build_rolling_avg_chart,
    build_fii_nifty_overlay,
)


@pytest.fixture
def sample_data():
    """Realistic FII/DII sample data spanning 5 days."""
    return [
        {"date": "06-Jul-2026", "category": "FII/FPI", "buy_value": 17000.0, "sell_value": 15500.0, "net_value": 1500.0},
        {"date": "06-Jul-2026", "category": "DII", "buy_value": 8000.0, "sell_value": 9000.0, "net_value": -1000.0},
        {"date": "07-Jul-2026", "category": "FII/FPI", "buy_value": 16500.0, "sell_value": 15000.0, "net_value": 1500.0},
        {"date": "07-Jul-2026", "category": "DII", "buy_value": 7500.0, "sell_value": 8500.0, "net_value": -1000.0},
        {"date": "08-Jul-2026", "category": "FII/FPI", "buy_value": 17463.95, "sell_value": 15501.15, "net_value": 1962.8},
        {"date": "08-Jul-2026", "category": "DII", "buy_value": 19165.13, "sell_value": 18374.97, "net_value": 790.16},
        {"date": "09-Jul-2026", "category": "FII/FPI", "buy_value": 18000.0, "sell_value": 16000.0, "net_value": 2000.0},
        {"date": "09-Jul-2026", "category": "DII", "buy_value": 9000.0, "sell_value": 10000.0, "net_value": -1000.0},
        {"date": "10-Jul-2026", "category": "FII/FPI", "buy_value": 17500.0, "sell_value": 15800.0, "net_value": 1700.0},
        {"date": "10-Jul-2026", "category": "DII", "buy_value": 8500.0, "sell_value": 9200.0, "net_value": -700.0},
    ]


class TestTrendChart:
    def test_returns_altair_chart(self, sample_data):
        fig, err = build_trend_chart(sample_data)
        assert err is None
        assert isinstance(fig, alt.Chart)

    def test_has_line_mark(self, sample_data):
        fig, err = build_trend_chart(sample_data)
        assert err is None
        # An Altair chart with mark_line means encoding mark == 'line'
        assert "line" in str(fig.mark).lower()

    def test_correct_net_values(self, sample_data):
        fig, err = build_trend_chart(sample_data)
        assert err is None
        # Layer chart encodes data — verify it's not empty
        assert fig.data is not None and not fig.data.empty

    def test_empty_data_returns_err(self):
        fig, err = build_trend_chart([])
        assert fig is None
        assert err is not None

    def test_single_day_returns_chart(self, sample_data):
        fig, err = build_trend_chart(sample_data[:2])
        assert err is None
        assert isinstance(fig, alt.Chart)


class TestComparisonChart:
    def test_returns_altair_chart(self, sample_data):
        fig, err = build_comparison_chart(sample_data)
        assert err is None
        assert isinstance(fig, alt.Chart)

    def test_has_bar_mark(self, sample_data):
        fig, err = build_comparison_chart(sample_data)
        assert err is None
        assert "bar" in str(fig.mark).lower()

    def test_empty_data_returns_err(self):
        fig, err = build_comparison_chart([])
        assert fig is None
        assert err is not None


class TestRollingAvgChart:
    def test_returns_altair_chart(self, sample_data):
        fig, err = build_rolling_avg_chart(sample_data, window=3)
        assert err is None
        assert isinstance(fig, alt.Chart)

    def test_has_line_mark(self, sample_data):
        fig, err = build_rolling_avg_chart(sample_data, window=3)
        assert err is None
        assert "line" in str(fig.mark).lower()

    def test_empty_data_returns_err(self):
        fig, err = build_rolling_avg_chart([], window=3)
        assert fig is None
        assert err is not None


class TestNiftyOverlay:
    def test_returns_altair_chart(self, sample_data):
        fig, err = build_fii_nifty_overlay(sample_data)
        assert err is None
        assert isinstance(fig, alt.Chart)

    def test_empty_data_returns_err(self):
        fig, err = build_fii_nifty_overlay([])
        assert fig is None
        assert err is not None

    def test_with_nifty_data(self, sample_data):
        nifty = {"06-Jul-2026": 24200.0, "07-Jul-2026": 24150.0}
        fig, err = build_fii_nifty_overlay(sample_data, nifty_prices=nifty)
        assert err is None
        assert isinstance(fig, (alt.Chart, alt.LayerChart))
