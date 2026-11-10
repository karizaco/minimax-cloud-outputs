from __future__ import annotations

from sip.number_trace import check_chat


def _run(*, last: float = 100.0, chg_pct: float = 5.0) -> dict:
    return {
        "date": "2026-11-05",
        "slot": "open",
        "candidates": [
            {
                "ticker": "2330",
                "venue": "TWSE",
                "instrument_type": "common",
                "last": last,
                "chg_pct": chg_pct,
                "dollar_vol": 50_000_000.0,
                "rvol": 1.2,
                "catalyst": None,
                "flags": [],
                "source": "test",
                "asof": "2026-11-05T09:30:00+08:00",
                "tier": "B",
            }
        ],
    }


def _metadata_run() -> dict:
    run = _run()
    run.update(
        {
            "date": "2026-11-10",
            "candidate_count": 565,
            "fx": 32.780875,
        }
    )
    return run


def test_signed_change_is_accepted() -> None:
    result = check_chat(_run(chg_pct=2.5), "# Picks\n\n- 2330: +2.5%\n")
    assert result["ok"] is True
    assert result["offenders"] == []


def test_negative_percent_does_not_match_positive() -> None:
    result = check_chat(_run(chg_pct=5.0), "# Picks\n\n- 2330: -5%\n")
    assert result["ok"] is False
    assert result["offenders"]


def test_garbage_number_is_rejected() -> None:
    chat = "99.9% on US$777m, 12.3x, 1,234.5"
    result = check_chat(_run(last=100.0, chg_pct=1.0), chat)
    assert result["ok"] is False
    assert len(result["offenders"]) >= 3


def test_percent_tolerance_accepts_rounded_value() -> None:
    result = check_chat(_run(chg_pct=6.06), "Change: 6.1%")
    assert result["ok"] is True
    assert result["offenders"] == []


def test_percent_tolerance_accepts_unrounded_value() -> None:
    result = check_chat(_run(chg_pct=6.1), "Change: 6.06%")
    assert result["ok"] is True
    assert result["offenders"] == []


def test_percent_true_mismatch_is_rejected() -> None:
    result = check_chat(_run(chg_pct=6.1), "Change: 5.0%")
    assert result["ok"] is False
    assert result["offenders"]


def test_percent_tolerance_still_rejects_wrong_sign() -> None:
    result = check_chat(_run(chg_pct=6.1), "Change: -6.06%")
    assert result["ok"] is False
    assert result["offenders"]


def test_typed_run_metadata_is_accepted() -> None:
    chat = "2026-11-10, 565 檔, 匯率 32.780875"
    result = check_chat(_metadata_run(), chat)
    assert result["ok"] is True
    assert result["offenders"] == []


def test_untyped_metadata_numbers_are_rejected() -> None:
    chat = "2026-11-10, 565 檔, 匯率 32.780875"
    result = check_chat(_run(), chat)
    assert result["ok"] is False
    assert result["offenders"]


def test_nested_candidate_metadata_is_rejected() -> None:
    run = _run()
    run["candidates"][0]["raw"] = {
        "date": "2026-11-10",
        "fx": 32.780875,
        "fx_rate": 32.780875,
        "candidate_count": 565,
    }
    chat = "2026-11-10, 565 檔, 匯率 32.780875"
    result = check_chat(run, chat)
    assert result["ok"] is False
    assert result["offenders"]


def test_meta_metadata_is_accepted() -> None:
    run = _run()
    run["meta"] = {
        "date": "2026-11-10",
        "fx": 32.780875,
        "candidate_count": 565,
    }
    chat = "2026-11-10, 565 檔, 匯率 32.780875"
    result = check_chat(run, chat)
    assert result["ok"] is True
    assert result["offenders"] == []


def test_metadata_alias_metadata_is_accepted() -> None:
    run = _run()
    run["metadata"] = {
        "run_date": "2026-11-10",
        "fx_rate": 32.780875,
        "candidate_count": 565,
    }
    chat = "2026-11-10, 565 檔, 匯率 32.780875"
    result = check_chat(run, chat)
    assert result["ok"] is True
    assert result["offenders"] == []


def test_explicit_fx_rate_is_accepted() -> None:
    result = check_chat(_run(), "匯率 32.780875", fx_rate=32.780875)
    assert result["ok"] is True
    assert result["offenders"] == []


def test_explicit_date_and_candidate_count_are_accepted() -> None:
    result = check_chat(
        _run(),
        "2026-11-10, 565 檔",
        date="2026-11-10",
        candidate_count=565,
    )
    assert result["ok"] is True
    assert result["offenders"] == []


def _turnover_run() -> dict:
    run = _run()
    run["fx"] = 32.780875
    run["candidates"][0]["dollar_vol"] = 29_374_530_000.0
    run["candidates"][0]["usd_turnover"] = 29_374_530_000.0 / 32.780875
    return run


def test_raw_twd_dollar_volume_is_rejected_as_usd_compact() -> None:
    result = check_chat(_turnover_run(), "US$29374.53m")
    assert result["ok"] is False
    assert result["offenders"]


def test_twd_yi_mislabelled_as_usd_yi_is_rejected() -> None:
    result = check_chat(_turnover_run(), "293.7453 億美元")
    assert result["ok"] is False
    assert result["offenders"]


def test_correct_usd_turnover_display_is_accepted() -> None:
    result = check_chat(_turnover_run(), "US$896.1m")
    assert result["ok"] is True
    assert result["offenders"] == []


def test_correct_usd_yi_display_is_accepted() -> None:
    result = check_chat(_turnover_run(), "8.96 億美元")
    assert result["ok"] is True
    assert result["offenders"] == []


def test_correct_twd_yi_display_is_accepted() -> None:
    result = check_chat(_turnover_run(), "293.7453 億元")
    assert result["ok"] is True
    assert result["offenders"] == []


def test_unlabelled_twd_compact_turnover_is_accepted() -> None:
    result = check_chat(_turnover_run(), "TWD 29.4bn")
    assert result["ok"] is True
    assert result["offenders"] == []


def test_unlabelled_compact_turnover_is_accepted() -> None:
    result = check_chat(_turnover_run(), "29.4bn")
    assert result["ok"] is True
    assert result["offenders"] == []


def test_plain_twd_price_is_accepted() -> None:
    run = _turnover_run()
    run["candidates"][0]["last"] = 1275.00
    result = check_chat(run, "TWD 1275.00")
    assert result["ok"] is True
    assert result["offenders"] == []
