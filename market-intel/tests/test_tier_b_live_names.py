from __future__ import annotations

from sip.schema import CandidateRow
from sip.tier import run_pipeline


def _row(ticker: str, *, rvol: float = 1.0, chg_pct: float = 3.5) -> CandidateRow:
    return CandidateRow(
        ticker=ticker,
        venue="TWSE",
        instrument_type="common",
        last=100.0,
        chg_pct=chg_pct,
        dollar_vol=50_000_000.0,
        rvol=rvol,
        catalyst=None,
        catalyst_time=None,
        flags=[],
        source="test",
        asof="2026-11-05T09:30:00+08:00",
        tier=None,
        display_ticker=None,
        mcap_twd=None,
        mops_materiality=None,
    )


def test_live_names_follow_tech_watch_rvol_band() -> None:
    """No-catalyst: rvol in [1.0, 2.0) + soft move → TECH_WATCH; rvol >= 2 → B."""
    rows = [
        _row("2468", rvol=1.6, chg_pct=3.5),
        _row("2610", rvol=1.0, chg_pct=3.5),
        _row("6538.TPEX", rvol=2.5, chg_pct=3.5),
    ]
    cfg = {
        "open": {"floors": {"price_min": 0, "turnover_min": 0, "mcap_min": 0}},
        "day_move_hard": 5.0,
        "day_move_soft": 4.0,
        "gap_soft": 3.0,
        "elevated_rvol_min": 1.5,
        "tech_watch_rvol_min": 1.0,
        "tech_watch_rvol_max": 2.0,
        "soft_a_requires_catalyst": True,
    }
    result = {row.ticker: row.tier for row in run_pipeline(rows, cfg, "open")}
    assert result["2468"] == "TECH_WATCH"
    assert result["2610"] == "TECH_WATCH"
    assert result["6538.TPEX"] == "B"
