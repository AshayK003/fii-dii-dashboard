"""Altair chart builders for the FII/DII dashboard.

Zero extra deps — Altair ships with Streamlit. No pip install needed.
"""

from __future__ import annotations

import logging
from typing import Optional

log = logging.getLogger(__name__)

_ERR_MSG = "No data available for charting"


def _prepare_df(records: list[dict]):
    """Convert DB records to a sorted DataFrame. Returns None if no data."""
    try:
        import pandas as pd
    except ImportError:
        return None
    if not records:
        return None
    df = pd.DataFrame(records)
    df["date_parsed"] = pd.to_datetime(df["date"], format="%d-%b-%Y")
    return df.sort_values("date_parsed")


def _import_altair():
    """Lazy import altair — returns (alt|None, error_msg)."""
    try:
        import altair as alt
        return alt, None
    except Exception as e:
        log.warning("altair import failed: %s", e)
        return None, str(e)


_COLOR_SCALE = {
    "domain": ["FII/FPI", "DII"],
    "range": ["#22C55E", "#EF4444"],
}

_HEIGHT = 400


def _base_chart(df, alt):
    """Shared encoding for date + color + tooltip."""
    return alt.Chart(df).encode(
        x=alt.X("date_parsed:T", title="Date"),
        color=alt.Color("category:N", title=None, scale=alt.Scale(**_COLOR_SCALE)),
        tooltip=[
            alt.Tooltip("date_parsed:T", title="Date", format="%d-%b-%Y"),
            alt.Tooltip("category:N", title="Type"),
        ],
    )


def build_trend_chart(records: list[dict]):
    """Line chart: FII vs DII net flow over time.

    Returns (altair.Chart|None, error_msg).
    """
    alt, err = _import_altair()
    if err:
        return None, err

    df = _prepare_df(records)
    if df is None or df.empty:
        return None, _ERR_MSG

    chart = (
        _base_chart(df, alt)
        .mark_line(point=True, strokeWidth=2)
        .encode(
            y=alt.Y("net_value:Q", title="Net Value (₹ Cr)"),
            tooltip=[
                alt.Tooltip("date_parsed:T", title="Date", format="%d-%b-%Y"),
                alt.Tooltip("category:N", title="Type"),
                alt.Tooltip("net_value:Q", title="Net (₹ Cr)", format=",.2f"),
            ],
        )
        .properties(title="FII/DII Net Flow (₹ Crores)", height=_HEIGHT)
        .interactive()
    )
    return chart, None


def build_comparison_chart(records: list[dict]):
    """Bar chart: FII vs DII side-by-side daily comparison.

    Returns (altair.Chart|None, error_msg).
    """
    alt, err = _import_altair()
    if err:
        return None, err

    df = _prepare_df(records)
    if df is None or df.empty:
        return None, _ERR_MSG

    chart = (
        _base_chart(df, alt)
        .mark_bar()
        .encode(
            x=alt.X("date_parsed:T", title="Date"),
            y=alt.Y("net_value:Q", title="Net Value (₹ Cr)"),
            column=alt.Column(
                "category:N",
                title=None,
                header=alt.Header(labelFontSize=12, labelPadding=8),
            ),
        )
        .properties(title="FII vs DII Daily Net Comparison", height=_HEIGHT)
        .interactive()
    )
    return chart, None


def build_rolling_avg_chart(records: list[dict], window: int = 7):
    """Line chart: rolling average of FII/DII net flow.

    Returns (altair.Chart|None, error_msg).
    """
    alt, err = _import_altair()
    if err:
        return None, err

    df = _prepare_df(records)
    if df is None or df.empty:
        return None, _ERR_MSG

    df = df.copy()
    df["rolling_avg"] = (
        df.groupby("category")["net_value"]
        .transform(lambda x: x.rolling(window=window, min_periods=1).mean())
    )

    chart = (
        _base_chart(df, alt)
        .mark_line(strokeWidth=2, strokeDash=[5, 3])
        .encode(
            y=alt.Y("rolling_avg:Q", title=f"{window}D Rolling Avg (₹ Cr)"),
            tooltip=[
                alt.Tooltip("date_parsed:T", title="Date", format="%d-%b-%Y"),
                alt.Tooltip("category:N", title="Type"),
                alt.Tooltip("rolling_avg:Q", title=f"{window}D Avg (₹ Cr)", format=",.2f"),
            ],
        )
        .properties(
            title=f"{window}-Day Rolling Average Net Flow (₹ Crores)", height=_HEIGHT
        )
        .interactive()
    )
    return chart, None


def build_fii_nifty_overlay(
    records: list[dict],
    nifty_prices: Optional[dict[str, float]] = None,
):
    """Dual-axis chart: FII net flow + Nifty closing price.

    Returns (altair.Chart|None, error_msg).
    """
    alt, err = _import_altair()
    if err:
        return None, err

    df = _prepare_df(records)
    if df is None or df.empty:
        return None, _ERR_MSG

    fii_df = df[df["category"] == "FII/FPI"]
    if fii_df.empty:
        return None, "No FII data available"

    fii_layer = (
        alt.Chart(fii_df)
        .mark_line(point=True, strokeWidth=2, color="#22C55E")
        .encode(
            x=alt.X("date_parsed:T", title="Date"),
            y=alt.Y(
                "net_value:Q",
                title="FII Net (₹ Cr)",
                axis=alt.Axis(titleColor="#22C55E", labelColor="#22C55E"),
            ),
            tooltip=[
                alt.Tooltip("date_parsed:T", title="Date", format="%d-%b-%Y"),
                alt.Tooltip("net_value:Q", title="FII Net (₹ Cr)", format=",.2f"),
            ],
        )
    )

    if nifty_prices:
        try:
            import pandas as pd
        except ImportError:
            pass
        else:
            nifty_df = pd.DataFrame(
                [
                    {
                        "date_parsed": pd.to_datetime(d, format="%d-%b-%Y"),
                        "nifty_close": p,
                    }
                    for d, p in (nifty_prices or {}).items()
                ]
            )
            if not nifty_df.empty:
                nifty_layer = (
                    alt.Chart(nifty_df)
                    .mark_line(strokeWidth=2, color="#636363", strokeDash=[3, 3])
                    .encode(
                        x=alt.X("date_parsed:T"),
                        y=alt.Y(
                            "nifty_close:Q",
                            title="Nifty 50",
                            axis=alt.Axis(titleColor="#636363", labelColor="#636363"),
                        ),
                        tooltip=[
                            alt.Tooltip("date_parsed:T", title="Date", format="%d-%b-%Y"),
                            alt.Tooltip("nifty_close:Q", title="Nifty 50", format=",.2f"),
                        ],
                    )
                )

                combined = (
                    alt.layer(fii_layer, nifty_layer)
                    .resolve_scale(y="independent")
                    .properties(title="FII Net Flow vs Nifty 50", height=_HEIGHT)
                    .interactive()
                )
                return combined, None

    chart = fii_layer.properties(
        title="FII Net Flow vs Nifty 50 (Nifty data unavailable)",
        height=_HEIGHT,
    ).interactive()
    return chart, None
