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


def test_buyback_is_material_but_boilerplate_is_not() -> None:
    assert materiality_score("公告本公司董事會決議買回庫藏股") >= 1
    assert materiality_score("本公司董事會通過買回公司股份") >= 1
    assert materiality_score("COMPANY BOARD APPROVED BUYBACK") >= 1
    assert materiality_score("SHARE REPURCHASE ANNOUNCEMENT") >= 1
    assert materiality_score("TREASURY SHARE REPURCHASE") >= 1
    assert is_boilerplate_mops("公告本公司取得有價證券")
    assert not is_boilerplate_mops("公告本公司董事會決議買回庫藏股")


def test_q3_financials_material() -> None:
    assert materiality_score("公告本公司董事會通過115年第3季合併財務報告") >= 1
    assert not is_boilerplate_mops("公告本公司董事會通過115年第3季合併財務報告")


def test_monthly_performance_uses_explanation_sales_figures() -> None:
    headline = "發布本公司115年10月份業績資料"
    explanation = "本公司115年10月份合併營業額為新台幣1,000,000,000元"
    assert materiality_score(headline, explanation) >= 1


def test_attach_uses_explanation_and_preserves_source() -> None:
    movers = {"2308": {"ticker": "2308", "catalyst": None, "raw": {}}}
    rows = [
        {
            "ticker": "2308",
            "catalyst": "發布本公司115年10月份業績資料",
            "explanation": "115年10月份合併營業額為新台幣1,000,000,000元",
            "time": "16:32",
        }
    ]

    _attach_mops_catalysts(movers, rows)

    assert movers["2308"]["catalyst"]
    assert "合併營業額" in movers["2308"]["catalyst"]
    assert movers["2308"]["raw"]["mops_explanation"] == (
        "115年10月份合併營業額為新台幣1,000,000,000元"
    )
    assert movers["2308"]["raw"]["mops_materiality"] >= 1


def test_acquisition_outranks_ordinary_consolidated_monthly_sales() -> None:
    movers = {"6271": {"ticker": "6271", "catalyst": None, "raw": {}}}
    rows = [
        {
            "ticker": "6271",
            "catalyst": "公告本公司115年10月份合併營收淨額",
            "explanation": "115年10月份合併營收淨額為新台幣500,000,000元",
            "time": "09:00",
        },
        {
            "ticker": "6271",
            "catalyst": "公告本公司與Global Testing股份有限公司進行協議安排及收購案",
            "explanation": "本公司擬以股份及現金進行收購",
            "time": "10:00",
        },
    ]

    _attach_mops_catalysts(movers, rows)

    assert "收購" in movers["6271"]["catalyst"]
    assert "Global Testing" in movers["6271"]["catalyst"]


def test_media_clarification_with_quoted_revenue_is_not_attached() -> None:
    movers = {"9999": {"ticker": "9999", "catalyst": None, "raw": {}}}
    rows = [
        {
            "ticker": "9999",
            "catalyst": "說明媒體報導",
            "explanation": (
                "報導內容：「預期2027年營收可望達新台幣500億元，展望明年獲利成長」。"
                "本則重大訊息同時符合證券交易法施行細則第45條至第46條規定。"
            ),
        }
    ]

    _attach_mops_catalysts(movers, rows)

    assert not movers["9999"].get("catalyst")
    assert not movers["9999"]["raw"].get("mops_materiality")


def test_own_monthly_revenue_earnings_is_attached() -> None:
    movers = {"9998": {"ticker": "9998", "catalyst": None, "raw": {}}}
    explanation = "本公司115年10月份合併營業額為新台幣1,250,000,000元"
    rows = [
        {
            "ticker": "9998",
            "catalyst": "發布本公司115年10月份業績資料",
            "explanation": explanation,
        }
    ]

    _attach_mops_catalysts(movers, rows)

    assert movers["9998"]["catalyst"]
    assert "合併營業額" in movers["9998"]["catalyst"]
    assert movers["9998"]["raw"]["mops_explanation"] == explanation
    assert len(movers["9998"]["catalyst"]) < len(explanation) + 100


def test_legal_footer_template_material_message_is_not_enough() -> None:
    explanation = (
        "重大訊息\n"
        "發佈重大訊息澄清\n"
        "本則重大訊息同時符合證券交易法施行細則第45條至第46條規定。"
    )
    movers = {"9997": {"ticker": "9997", "catalyst": None, "raw": {}}}

    _attach_mops_catalysts(
        movers,
        [
            {
                "ticker": "9997",
                "catalyst": "澄清媒體報導",
                "explanation": explanation,
            }
        ],
    )

    assert not movers["9997"].get("catalyst")
    assert not movers["9997"]["raw"].get("mops_materiality")


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
        "day_move_hard": 4.0,
        "day_move_soft": 4.0,
        "gap_soft": 3.0,
        "elevated_rvol_min": 1.5,
        "tech_watch_rvol_min": 0.3,
        "tech_watch_rvol_max": 2.0,
        "tech_watch_liquid_turnover_min": 2_500_000_000,
        "tech_watch_move_min": 2.0,
        "c_limit_usd_min": 50_000_000,
    }


def _row(**kwargs) -> CandidateRow:
    base = dict(
        ticker="1001",
        venue="TWSE",
        instrument_type="common",
        last=100.0,
        chg_pct=-6.0,
        dollar_vol=80_000_000.0,
        usd_turnover=50_000_000.0,
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
    result = run_pipeline([_row(catalyst=None, rvol=0.5, chg_pct=-6.0)], _cfg(), "open")
    assert all(r.tier != "Soft-A" for r in result)
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


def test_soft_a_hard_move_floor_is_four_percent() -> None:
    catalyst = "Q3 EPS NT$3.00 record"
    below = run_pipeline(
        [_row(catalyst=catalyst, mops_materiality=2, rvol=0.5, chg_pct=3.9)],
        _cfg(),
        "open",
    )
    assert all(r.tier != "Soft-A" for r in below)

    at_floor = run_pipeline(
        [_row(catalyst=catalyst, mops_materiality=2, rvol=0.5, chg_pct=4.0)],
        _cfg(),
        "open",
    )
    assert at_floor[0].tier == "Soft-A"


def test_limit_up_buyback_is_soft_a() -> None:
    result = run_pipeline(
        [
            _row(
                catalyst="公告本公司董事會決議買回庫藏股",
                mops_materiality=1,
                flags=["LIMIT_UP"],
                rvol=0.5,
                chg_pct=9.5,
            )
        ],
        _cfg(),
        "open",
    )
    assert result[0].tier == "Soft-A"


def test_limit_down_with_material_is_c() -> None:
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
    assert result[0].tier == "C"


def test_tech_watch_rvol_band() -> None:
    cfg = _cfg()
    tw = run_pipeline([_row(catalyst=None, rvol=1.2, chg_pct=-5.0)], cfg, "open")
    assert tw[0].tier == "TECH_WATCH"
    below = run_pipeline([_row(catalyst=None, rvol=0.2, chg_pct=-8.0)], cfg, "open")
    assert all(r.tier != "TECH_WATCH" for r in below)
    missing = run_pipeline([_row(catalyst=None, rvol=None, chg_pct=-8.0)], cfg, "open")
    assert all(r.tier != "TECH_WATCH" for r in missing)
    b = run_pipeline([_row(catalyst=None, rvol=2.5, chg_pct=-5.0)], cfg, "open")
    assert b[0].tier == "B"


def test_liquid_name_tech_watch_uses_two_percent_move_floor() -> None:
    cfg = _cfg()
    liquid = run_pipeline(
        [
            _row(
                catalyst=None,
                rvol=0.3,
                chg_pct=3.5,
                dollar_vol=2_500_000_000,
            )
        ],
        cfg,
        "open",
    )
    assert liquid[0].tier == "TECH_WATCH"

    thin = run_pipeline(
        [
            _row(
                catalyst=None,
                rvol=0.3,
                chg_pct=2.4,
                dollar_vol=2_499_999_999,
            )
        ],
        cfg,
        "open",
    )
    assert all(r.tier != "TECH_WATCH" for r in thin)


def test_catalyst_min_score_from_cfg() -> None:
    cfg = _cfg()
    row = _row(
        catalyst="Q3 EPS NT$3.00 record",
        mops_materiality=1,
        rvol=0.5,
        chg_pct=-6.0,
    )
    assert run_pipeline([row], cfg, "open")[0].tier == "Soft-A"
    cfg = {**cfg, "catalyst_min_score": 3}
    result = run_pipeline([row], cfg, "open")
    assert all(r.tier != "Soft-A" for r in result)
    assert all(r.tier != "A" for r in result)
