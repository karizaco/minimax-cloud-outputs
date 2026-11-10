from __future__ import annotations

from sip.catalyst_gate import visible_excerpt
from sip.number_trace import check_chat


def _run(*, last: float = 100.0, chg_pct: float = 5.0) -> dict:
    return {"date": "2026-11-05", "slot": "open", "candidates": [{
        "ticker": "2330", "venue": "TWSE", "instrument_type": "common", "last": last,
        "chg_pct": chg_pct, "dollar_vol": 50_000_000.0, "rvol": 1.2,
        "catalyst": None, "flags": [], "source": "test",
        "asof": "2026-11-05T09:30:00+08:00", "tier": "B"}]}


def _metadata_run() -> dict:
    run = _run()
    run.update({"date": "2026-11-10", "candidate_count": 565, "fx": 32.780875})
    return run


def test_signed_change_is_accepted() -> None:
    assert check_chat(_run(chg_pct=2.5), "# Picks\n\n- 2330: +2.5%\n")["ok"] is True


def test_negative_percent_does_not_match_positive() -> None:
    assert check_chat(_run(chg_pct=5.0), "# Picks\n\n- 2330: -5%\n")["ok"] is False


def test_garbage_number_is_rejected() -> None:
    assert check_chat(_run(last=100.0, chg_pct=1.0),
                      "99.9% on US$777m, 12.3x, 1,234.5")["ok"] is False


def test_percent_tolerance_accepts_rounded_value() -> None:
    assert check_chat(_run(chg_pct=6.06), "Change: 6.1%")["ok"] is True


def test_percent_tolerance_accepts_unrounded_value() -> None:
    assert check_chat(_run(chg_pct=6.1), "Change: 6.06%")["ok"] is True


def test_percent_true_mismatch_is_rejected() -> None:
    assert check_chat(_run(chg_pct=6.1), "Change: 5.0%")["ok"] is False


def test_percent_tolerance_still_rejects_wrong_sign() -> None:
    assert check_chat(_run(chg_pct=6.1), "Change: -6.06%")["ok"] is False


def test_typed_run_metadata_is_accepted() -> None:
    assert check_chat(_metadata_run(), "2026-11-10, 565 檔, 匯率 32.780875")["ok"] is True


def test_untyped_metadata_numbers_are_rejected() -> None:
    assert check_chat(_run(), "2026-11-10, 565 檔, 匯率 32.780875")["ok"] is False


def test_nested_candidate_metadata_is_rejected() -> None:
    run = _run()
    run["candidates"][0]["raw"] = {"date": "2026-11-10", "fx": 32.780875,
                                    "fx_rate": 32.780875, "candidate_count": 565}
    assert check_chat(run, "2026-11-10, 565 檔, 匯率 32.780875")["ok"] is False


def test_meta_metadata_is_accepted() -> None:
    run = _run()
    run["meta"] = {"date": "2026-11-10", "fx": 32.780875, "candidate_count": 565}
    assert check_chat(run, "2026-11-10, 565 檔, 匯率 32.780875")["ok"] is True


def test_metadata_alias_metadata_is_accepted() -> None:
    run = _run()
    run["metadata"] = {"run_date": "2026-11-10", "fx_rate": 32.780875,
                       "candidate_count": 565}
    assert check_chat(run, "2026-11-10, 565 檔, 匯率 32.780875")["ok"] is True


def test_explicit_fx_rate_is_accepted() -> None:
    assert check_chat(_run(), "匯率 32.780875", fx_rate=32.780875)["ok"] is True


def test_explicit_date_and_candidate_count_are_accepted() -> None:
    assert check_chat(_run(), "2026-11-10, 565 檔", date="2026-11-10",
                      candidate_count=565)["ok"] is True


def _turnover_run() -> dict:
    run = _run()
    run["fx"] = 32.780875
    run["candidates"][0]["dollar_vol"] = 29_374_530_000.0
    run["candidates"][0]["usd_turnover"] = 29_374_530_000.0 / 32.780875
    return run


def test_raw_twd_dollar_volume_is_rejected_as_usd_compact() -> None:
    assert check_chat(_turnover_run(), "US$29374.53m")["ok"] is False


def test_twd_yi_mislabelled_as_usd_yi_is_rejected() -> None:
    assert check_chat(_turnover_run(), "293.7453 億美元")["ok"] is False


def test_correct_usd_turnover_display_is_accepted() -> None:
    assert check_chat(_turnover_run(), "US$896.1m")["ok"] is True


def test_correct_usd_yi_display_is_accepted() -> None:
    assert check_chat(_turnover_run(), "8.96 億美元")["ok"] is True


def test_correct_twd_yi_display_is_accepted() -> None:
    assert check_chat(_turnover_run(), "293.7453 億元")["ok"] is True


def test_unlabelled_twd_compact_turnover_is_accepted() -> None:
    assert check_chat(_turnover_run(), "TWD 29.4bn")["ok"] is True


def test_unlabelled_compact_turnover_is_accepted() -> None:
    assert check_chat(_turnover_run(), "29.4bn")["ok"] is True


def test_unlabelled_twd_price_is_accepted() -> None:
    run = _turnover_run()
    run["candidates"][0]["last"] = 1275.00
    assert check_chat(run, "TWD 1275.00")["ok"] is True


def test_rvol_display_rounding_is_accepted() -> None:
    run = _run()
    run["candidates"][0]["rvol"] = 0.44321753753315096
    assert check_chat(run, "RelVol 0.4x")["ok"] is True


def test_sourced_catalyst_year_quarter_and_amount_are_accepted() -> None:
    run = _run()
    run["candidates"][0]["catalyst"] = "公司於115年第3季公告，資本支出2,701億元"
    run["candidates"][0]["raw"] = {"mops_explanation": "115年第3季財務報告說明"}
    assert check_chat(run, "115年 第3季 2,701億元")["ok"] is True


def test_sourced_percent_is_accepted_only_when_present() -> None:
    run = _run()
    run["candidates"][0]["raw"] = {"mops_explanation": "營業額成長30.1%，較上月成長14.2%"}
    assert check_chat(run, "營收成長 30.1%")["ok"] is True
    assert check_chat(run, "營收成長 99.9%")["ok"] is False


def test_sourced_percent_wrong_sign_is_rejected() -> None:
    run = _run()
    run["candidates"][0]["raw"] = {"mops_explanation": "營業額成長30.1%"}
    assert check_chat(run, "營收變化 -30.1%")["ok"] is False


def test_bare_rvol_is_rejected_but_unit_qualified_is_accepted() -> None:
    run = _run()
    run["candidates"][0]["rvol"] = 5.009524452716406
    assert check_chat(run, "RelVol 5.0x")["ok"] is True
    assert check_chat(run, "RelVol 5.01x")["ok"] is True
    assert check_chat(run, "5.01")["ok"] is False


def test_source_health_counts_are_accepted() -> None:
    run = _run()
    run["source_health"] = [{"source": "mops", "count": 371},
                            {"source": "cmoney", "count": 565},
                            {"source": "yahoo", "count": 100},
                            {"source": "schema", "count": 0}]
    assert check_chat(run, "mops 371, cmoney 565, yahoo 100, schema 0")["ok"] is True


def test_nested_source_health_count_is_rejected() -> None:
    run = _run()
    run["raw"] = {"source_health": [{"source": "mops", "count": 371}]}
    assert check_chat(run, "mops 371")["ok"] is False


def _aggregate_run() -> dict:
    run = _run()
    run.update({"date": "2026-11-09", "fx": 32.851408})
    run["candidates"] = [{"ticker": "2330", "dollar_vol": 200_000_000_000.0},
                         {"ticker": "2454", "dollar_vol": 9_070_100_000.0}]
    return run


def test_proven_candidate_aggregate_is_accepted() -> None:
    assert check_chat(_aggregate_run(), "TWD 2,090.7 億元, US$6.36bn")["ok"] is True


def test_raw_twd_aggregate_is_rejected_as_usd() -> None:
    assert check_chat(_aggregate_run(), "US$2090.7bn")["ok"] is False


def test_visible_catalyst_numbers_trace_to_unsanitized_explanation() -> None:
    run = _run()
    explanation = ("本公司115年10月份合併營業額為新台幣746.66億元，"
                   "較去年同期573.84億元成長30.1%，較上月654.00億元成長14.2%；"
                   "115年1~10個月累積合併營業額為新台幣6,143.34億元。")
    catalyst = ("發布本公司115年10月份業績資料 — 本公司115年10月份合併營業額"
                "為新台幣746.66億元，較去年同期573.84億元成長30.1%，"
                "較上月654.00億元成長14.2%；115年1~10個月累積合併營業額為新台幣6,143.34億元。")
    run["candidates"][0]["catalyst"] = catalyst
    run["candidates"][0]["raw"] = {"mops_explanation": explanation}
    assert check_chat(run, catalyst)["ok"] is True


def test_visible_catalyst_numbers_trace_for_two_unsanitized_mops_explanations() -> None:
    headline_2308 = "發布本公司115年10月份業績資料"
    explanation_2308 = """1.事實發生日:115/11/09
2.公司名稱:台達電子工業股份有限公司
3.與公司關係(請輸入本公司或子公司):本公司
4.相互持股比例:不適用
5.發生緣由:發布本公司115年10月份業績資料
6.因應措施:不適用
7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事件):
本公司115年10月份合併營業額為新台幣746.66億元，較去年同期合併營業額新台幣573.84億元成長30.1%，較上月份合併營業額新台幣654.00億元成長14.2%；115年1~10月份累積合併營業額為新台幣6,143.34億元。"""

    headline_3711 = "公告本公司115年第3季合併財務報告經董事會決議通過"
    explanation_3711 = """1.提報董事會或經董事會決議日期:115/11/09
2.審計委員會通過日期:115/11/09
3.財務報告或年度自結財務資訊報導期間
起訖日期(XXX/XX/XX~XXX/XX/XX):115/01/01~115/09/30
4.1月1日累計至本期止營業收入(仟元):608,886,833
10.1月1日累計至本期止基本每股盈餘(損失) (元):14.17"""

    excerpt_2308 = visible_excerpt(headline_2308, explanation_2308)
    excerpt_3711 = visible_excerpt(headline_3711, explanation_3711)
    catalyst_2308 = f"{headline_2308} — {excerpt_2308}"
    catalyst_3711 = f"{headline_3711} — {excerpt_3711}"

    assert "746.66億" in excerpt_2308
    assert "營業收入" in excerpt_3711
    assert "608,886,833" in excerpt_3711
    assert "115/01/01" not in excerpt_3711

    run = _run()
    run["candidates"] = [
        {
            **run["candidates"][0],
            "ticker": "2308",
            "catalyst": catalyst_2308,
            "raw": {"mops_explanation": explanation_2308},
        },
        {
            **run["candidates"][0],
            "ticker": "3711",
            "catalyst": catalyst_3711,
            "raw": {"mops_explanation": explanation_3711},
        },
    ]

    chat = f"{catalyst_2308}\n{catalyst_3711}"
    assert check_chat(run, chat)["ok"] is True
    assert check_chat(run, "4")["ok"] is False
    assert check_chat(run, "115/01/01")["ok"] is False
