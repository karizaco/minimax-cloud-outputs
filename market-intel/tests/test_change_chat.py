import copy

import pytest

from sip.change_chat import ChatError, compare_snapshots


def row(
    ticker="AAA",
    tier="A",
    price=102,
    opening=101,
    prior=100,
    usd=10,
    **extra,
):
    value = {
        "ticker": ticker,
        "tier": tier,
        "session_open": opening,
        "prior_close": prior,
        "price": price,
        "currency": "USD",
        "price_basis": "raw",
        "adjustment_id": "none",
        "usd_turnover": usd,
    }
    value.update(extra)
    return value


def snapshot(slot="open", rows=None):
    return {
        "market": "US",
        "session_id": "2024-11-04",
        "calendar_id": "NYSE",
        "timezone": "America/New_York",
        "session_date": "2024-11-04",
        "asof": (
            "2024-11-04T09:30:00-05:00"
            if slot == "open"
            else "2024-11-04T12:00:00-05:00"
        ),
        "slot": slot,
        "rows": rows if rows is not None else [row()],
    }


def test_change_only_and_numeric_reversal():
    same = compare_snapshots(snapshot(), snapshot("midday"), 0.5)
    assert "No material changes" in same
    assert "Current rows:" not in same
    assert "- AAA [A]" not in same
    before = snapshot("open", [row(price=102)])
    after = snapshot("midday", [row(price=100)])
    output = compare_snapshots(before, after, 0.5)
    assert "gap held -> reversed" in output
    assert "held -> reversed" in output
    assert "Current rows:" not in same


def test_new_removed_tier_up_down_and_preserved_removed_row():
    before = snapshot(
        "open",
        [row(ticker="OLD", tier="A"), row(ticker="B", tier="B")],
    )
    after = snapshot(
        "midday",
        [
            row(ticker="NEW", tier="Soft-A"),
            row(ticker="B", tier="TECH_WATCH"),
        ],
    )
    output = compare_snapshots(before, after, 0.5)
    assert "new name" in output
    assert "removed" in output
    assert "not a gap failure" in output
    assert "upgrade B -> TECH_WATCH" in output
    assert "OLD [A]" in output

    downgrade = compare_snapshots(
        snapshot("open", [row(ticker="A", tier="A")]),
        snapshot("midday", [row(ticker="A", tier="Soft-A")]),
        0.5,
    )
    assert "downgrade A -> Soft-A" in downgrade


def test_soft_a_to_a_is_upgrade():
    output = compare_snapshots(
        snapshot("open", [row(tier="Soft-A")]),
        snapshot("midday", [row(tier="A")]),
        0.5,
    )
    assert "upgrade Soft-A -> A" in output


def test_missing_stale_same_time_date_and_null_warnings():
    assert "BASELINE_UNAVAILABLE" in compare_snapshots(
        None, snapshot("midday"), 0.5
    )
    old = snapshot()
    old["asof"] = "2024-11-04T01:00:00-05:00"
    assert "BASELINE_UNAVAILABLE" in compare_snapshots(
        old, snapshot("midday"), 0.5
    )
    same_time = snapshot()
    same_time["asof"] = snapshot("midday")["asof"]
    assert "BASELINE_UNAVAILABLE" in compare_snapshots(
        same_time, snapshot("midday"), 0.5
    )
    wrong_date = snapshot("midday")
    wrong_date["session_date"] = "2024-11-05"
    with pytest.raises(ChatError, match="session_date"):
        compare_snapshots(snapshot(), wrong_date, 0.5)
    null = snapshot("midday", [row(price=None)])
    assert "UNKNOWN GAP" in compare_snapshots(snapshot(), null, 0.5)


def test_basis_and_actual_open_changes_prevent_gap_claim():
    before = snapshot("open")
    after = snapshot("midday")
    after["rows"][0]["currency"] = "TWD"
    output = compare_snapshots(before, after, 0.5)
    assert "UNKNOWN GAP" in output
    assert "gap held ->" not in output
    before = snapshot("open")
    after = snapshot("midday")
    after["rows"][0]["session_open"] = 100
    output = compare_snapshots(before, after, 0.5)
    assert "actual session open/prior close changed" in output
    assert "gap held ->" not in output


def test_missing_or_empty_basis_warns_without_raising():
    before = snapshot("open")
    before["rows"][0].pop("price_basis")
    after = snapshot("midday")
    after["rows"][0]["adjustment_id"] = ""
    output = compare_snapshots(before, after, 0.5)
    assert "UNKNOWN BASIS" in output
    assert "gap held ->" not in output


def test_all_markets_formatting_and_nonmutation():
    before = snapshot()
    original = copy.deepcopy(before)
    compare_snapshots(before, snapshot("midday"), 0.5)
    assert before == original
    for market in ("US", "TW", "JP", "ASX", "EU"):
        midday = snapshot("midday")
        midday["market"] = market
        current = row(
            ticker="1234.TW" if market == "TW" else "7203.T",
            company_en="Toyota Motor Corp",
        )
        midday["rows"] = [current]
        output = compare_snapshots(None, midday, 0.5)
        assert market in output
        assert "USD turnover" in output
        if market == "JP":
            assert "Toyota Motor Corp" in output


def test_market_aliases_and_taiwan_conventions():
    for alias, canonical in (
        ("asx", "ASX"),
        ("tokyo", "JP"),
        ("taiwan", "TW"),
        ("europe", "EU"),
        ("us", "US"),
    ):
        midday = snapshot("midday")
        midday["market"] = alias
        original = copy.deepcopy(midday)
        output = compare_snapshots(None, midday, 0.5)
        assert f"SIP {canonical} MIDDAY" in output
        assert midday == original

    tpex = snapshot("midday", [row(ticker="1234.TW", venue="TPEx")])
    tpex.update(
        market="TW",
        calendar_id="TPEx",
        timezone="Asia/Taipei",
        asof="2024-11-04T12:00:00+08:00",
    )
    assert "1234.TPEX" in compare_snapshots(None, tpex, 0.5)
    twse = snapshot("midday", [row(ticker="1234.TW", venue="TWSE")])
    twse.update(
        market="TW",
        calendar_id="TWSE",
        timezone="Asia/Taipei",
        asof="2024-11-04T12:00:00+08:00",
    )
    assert "1234 [A]" in compare_snapshots(None, twse, 0.5)
    plain = snapshot("midday", [row(ticker="1234.TW")])
    assert ".TPEX" not in compare_snapshots(None, plain, 0.5)
    supplied = snapshot(
        "midday", [row(ticker="1234.TW", display_ticker="CUSTOM")]
    )
    assert "CUSTOM" in compare_snapshots(None, supplied, 0.5)


def test_unknown_old_gap_warns_and_is_not_a_change():
    before = snapshot("open", [row(price=None)])
    after = snapshot("midday", [row(price=103)])
    output = compare_snapshots(before, after, 0.5)
    assert "UNKNOWN GAP" in output
    assert "open snapshot has unavailable price or gap basis" in output
    assert "- AAA [A]" not in output


def test_changed_ticker_has_details_and_merged_reasons():
    before = snapshot("open", [row(ticker="A", tier="B")])
    after = snapshot("midday", [row(ticker="A", tier="TECH_WATCH", price=100)])
    output = compare_snapshots(before, after, 0.5)
    assert output.count("- A [TECH_WATCH]") == 1
    assert "price 100 USD" in output
    assert "USD turnover 10" in output
    assert "upgrade B -> TECH_WATCH" in output
    assert "gap held -> reversed" in output


def test_tech_watch_one_per_line_and_sorting():
    rows = [
        row(ticker="Z", tier="TECH_WATCH", usd=2),
        row(ticker="A", tier="TECH_WATCH", usd=3),
        row(ticker="C", tier="A", usd=1),
    ]
    output = compare_snapshots(None, snapshot("midday", rows), 0.5)
    assert output.count("- A [TECH_WATCH]") == 1
    assert output.count("- Z [TECH_WATCH]") == 1
    assert output.index("C [A]") < output.index("A [TECH_WATCH]")
    assert output.index("A [TECH_WATCH]") < output.index("Z [TECH_WATCH]")


def test_invalid_numeric_turnover_and_session():
    after = snapshot("midday")
    after["rows"][0]["usd_turnover"] = -1
    with pytest.raises(ChatError, match="usd_turnover"):
        compare_snapshots(snapshot(), after, 0.5)
    after = snapshot("midday")
    after["session_id"] = "other"
    output = compare_snapshots(snapshot(), after, 0.5)
    assert "BASELINE_UNAVAILABLE" in output
    assert "session_id" in output
    after = snapshot("midday")
    after["slot"] = "open"
    with pytest.raises(ChatError, match="slot"):
        compare_snapshots(snapshot(), after, 0.5)
