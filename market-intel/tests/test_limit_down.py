from __future__ import annotations

from sip.schema import CandidateRow
from sip.tier import run_pipeline


def test_limit_down_always_tier_c() -> None:
    row = CandidateRow(
        ticker="9999",
        venue="TWSE",
        instrument_type="common",
        last=100.0,
        chg_pct=-9.9,
        dollar_vol=80_000_000.0,
        rvol=5.0,
        catalyst="panic selling note",
        catalyst_time="09:30",
        flags=["LIMIT_DOWN"],
        source="test",
        asof="2026-11-05T09:30:00+08:00",
        tier=None,
    )
    cfg = {
        "open": {"floors": {"price_min": 0, "turnover_min": 0, "mcap_min": 0}},
        "day_move_hard": 5.0,
        "day_move_soft": 4.0,
        "gap_soft": 3.0,
        "elevated_rvol_min": 1.5,
    }
    result = run_pipeline([row], cfg, "open")
    assert len(result) == 1
    assert result[0].tier == "C"
