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
    )


def test_live_names_are_assigned_tier_b() -> None:
    rows = [
        _row("2468", rvol=1.6, chg_pct=0.5),
        _row("2610", rvol=1.0, chg_pct=3.5),
        _row("6538.TPEX", rvol=1.0, chg_pct=3.5),
    ]
    cfg = {
        "AM": {
            "floors": {
                "price_min": 0,
                "turnover_min": 0,
                "mcap_min": 0,
            }
        },
        "day_move_hard": 5.0,
        "day_move_soft": 4.0,
        "gap_soft": 3.0,
        "elevated_rvol_min": 1.5,
    }

    result = run_pipeline(rows, cfg, "AM")

    assert [(row.ticker, row.tier) for row in result] == [
        ("2468", "B"),
        ("2610", "B"),
        ("6538.TPEX", "B"),
    ]
