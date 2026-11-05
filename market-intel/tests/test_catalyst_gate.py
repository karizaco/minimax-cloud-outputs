from __future__ import annotations

from sip.catalyst_gate import is_boilerplate_mops, materiality_score
from sip.markets.taiwan.adapter import _attach_mops_catalysts
from sip.schema import CandidateRow
from sip.tier import run_pipeline


def test_boilerplate_denied() -> None:
    assert is_boilerplate_mops("公告本公司取得有價證券")
    assert is_boilerplate_mops("公告本公司取得機器設備")
    assert materiality_score("公告本公司取得有價證券") == 0 or is_boilerplate_mops(
        "公告本公司取得有價證券"
    )


def test_q3_financials_material() -> None:
    assert materiality_score("公告本公司董事會通過115年第3季合併財務報告") >= 1
    assert not is_boilerplate_mops("公告本公司董事會通過115年第3季合併財務報告")


def test_attach_skips_boilerplate() -> None:
    movers = {
        "2330": {
            "ticker": "2330",
            "catalyst": None,
            "raw": {},
        }
    }
    rows = [
        {
            "ticker": "2330",
            "catalyst": "公告本公司取得有價證券",
            "time": "09:00",
        }
    ]
    _attach_mops_catalysts(movers, rows)
    assert not movers["2330"].get("catalyst")


def test_attach_keeps_material() -> None:
    movers = {"2330": {"ticker": "2330", "catalyst": None, "raw": {}}}
    rows = [
        {
            "ticker": "2330",
            "catalyst": "公告本公司董事會通過115年第3季合併財務報告",
            "time": "09:00",
        }
    ]
    _attach_mops_catalysts(movers, rows)
    assert movers["2330"].get("catalyst")
    assert movers["2330"]["raw"].get("mops_materiality", 0) >= 1


def _cfg() -> dict:
    return {
        "open": {"floors": {"price_min": 0, "turnover_min": 0, "mcap_min": 0}},
        "soft_a_requires_catalyst": True,
        "day_move_hard": 5.0,
        "day_move_soft": 4.0,
        "gap_soft": 3.0,
        "elevated_rvol_min": 1.5,
        "tech_watch_rvol_min": 1.0,
        "tech_watch_rvol_max": 2.0,
    }


def _row(**kwargs) -> CandidateRow:
    base = dict(
        ticker="1001",
        venue="TWSE",
        instrument_type="common",
        last=100.0,
        chg_pct=-6.0,
        dollar_vol=80_000_000.0,
        rvol=0.5,
        catalyst=None,
        catalyst_time=None,
        flags=[],
        source="test",
        asof="2026-11-05T09:30:00+08:00",
        tier=None,
        mops_materiality=None,
    )
    base.update(kwargs)
    return CandidateRow(**base)


def test_soft_a_requires_material_catalyst() -> None:
    # tape alone → not Soft-A
    result = run_pipeline([_row(catalyst=None, rvol=0.5, chg_pct=-6.0)], _cfg(), "open")
    assert result[0].tier != "Soft-A"
    # material + hard move + soft rvol → Soft-A
    result = run_pipeline(
        [
            _row(
                catalyst="Q3 EPS NT$3.00 record",
                mops_materiality=2,
                rvol=0.5,
                chg_pct=-6.0,
            )
        ],
        _cfg(),
        "open",
    )
    assert result[0].tier == "Soft-A"


def test_limit_down_with_material_is_soft_a_never_a() -> None:
    result = run_pipeline(
        [
            _row(
                catalyst="Q3 financials",
                mops_materiality=2,
                flags=["LIMIT_DOWN"],
                rvol=2.0,
                chg_pct=-9.9,
            )
        ],
        _cfg(),
        "open",
    )
    assert result[0].tier == "Soft-A"


def test_tech_watch_rvol_band() -> None:
    cfg = _cfg()
    # soft rvol no catalyst → TECH_WATCH
    tw = run_pipeline([_row(catalyst=None, rvol=1.2, chg_pct=-5.0)], cfg, "open")
    assert tw[0].tier == "TECH_WATCH"
    soft = run_pipeline([_row(catalyst=None, rvol=0.5, chg_pct=-8.0)], cfg, "open")
    assert soft[0].tier == "TECH_WATCH"
    # strong rvol no catalyst → B
    b = run_pipeline([_row(catalyst=None, rvol=2.5, chg_pct=-5.0)], cfg, "open")
    assert b[0].tier == "B"
