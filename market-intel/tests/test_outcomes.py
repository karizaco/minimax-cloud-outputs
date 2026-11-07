import copy
import json

import pytest

from sip.outcomes import OutcomeError, ingest


def session(day, close="16:00", tz="America/New_York"):
    offset = "-04:00" if day < "2024-11-03" else "-05:00"
    return {
        "session_id": day,
        "date": day,
        "open": f"{day}T09:30:00{offset}",
        "close": f"{day}T{close}{offset}",
    }


def payload(flag=True, observations=True):
    days = [
        session("2024-11-04"),
        session("2024-11-05"),
        session("2024-11-06"),
    ]
    data = {
        "calendars": [
            {
                "calendar_id": "NYSE",
                "market": "US",
                "venue": "NYSE",
                "timezone": "America/New_York",
                "sessions": days,
            }
        ],
        "flags": [],
        "observations": [],
    }
    if flag:
        data["flags"] = [
            {
                "market": "US",
                "venue": "NYSE",
                "ticker": "AAA",
                "tier": "A",
                "catalyst": "x",
                "calendar_id": "NYSE",
                "session_id": "2024-11-04",
                "flag_timestamp": "2024-11-04T10:00:00-05:00",
                "flag_price": 100,
                "quote_timestamp": "2024-11-04T10:00:00-05:00",
                "quote_provenance": "fixture",
                "currency": "USD",
                "price_basis": "raw",
                "adjustment_id": "none",
            }
        ]
    if observations:
        for index, day in enumerate(days):
            data["observations"].append(
                {
                    "market": "US",
                    "venue": "NYSE",
                    "calendar_id": "NYSE",
                    "ticker": "AAA",
                    "session_id": day["session_id"],
                    "date": day["date"],
                    "timestamp": day["close"],
                    "open": 101,
                    "prior_close": 100,
                    "close": 102 + index,
                    "final": True,
                    "currency": "USD",
                    "price_basis": "raw",
                    "adjustment_id": "none",
                    "provenance": "fixture",
                }
            )
    return data


def test_quote_age_nulls_move_and_pending_fill(tmp_path):
    data = payload()
    result = ingest(data, tmp_path, 0.5, 60)
    assert result["derived"][0]["same_close_vs_flag_pct"] == pytest.approx(2)
    stale = copy.deepcopy(data)
    stale["flags"][0]["quote_timestamp"] = "2024-11-04T09:58:00-05:00"
    result = ingest(stale, tmp_path / "stale", 0.5, 60)
    assert result["derived"][0]["same_close_vs_flag_pct"] is None
    assert (
        "quote_stale_or_ahead_of_flag"
        in result["derived"][0]["pending_reasons"]
    )


def test_next_move_independent_of_missing_flag_price(tmp_path):
    data = payload()
    data["flags"][0].update(
        flag_price=None,
        quote_timestamp=None,
        quote_provenance=None,
    )
    result = ingest(data, tmp_path, 0.5)
    assert result["derived"][0]["same_close_vs_flag_pct"] is None
    assert result["derived"][0]["next_close_vs_same_close_pct"] == pytest.approx(
        (103 / 102 - 1) * 100
    )
    assert result["derived"][0]["same_session_close"] == 102
    assert result["derived"][0]["next_session_close"] == 103


def test_numeric_retention_states_and_basis_mismatch(tmp_path):
    data = payload()
    data["observations"][0]["close"] = 100.5
    result = ingest(data, tmp_path, 0.5)
    assert result["derived"][0]["gap_retention_ratio"] == pytest.approx(0.5)
    assert result["derived"][0]["gap_classification"] == "up_held"
    data = payload()
    data["observations"][0]["close"] = 100.4
    result = ingest(data, tmp_path / "faded", 0.5)
    assert result["derived"][0]["gap_classification"] == "up_faded"
    mismatch = payload()
    mismatch["observations"][0]["adjustment_id"] = "split"
    result = ingest(mismatch, tmp_path / "split", 0.5)
    assert result["derived"][0]["same_close_vs_flag_pct"] is None


def test_down_gap_uses_same_signed_ratio(tmp_path):
    data = payload()
    data["observations"][0].update(open=99, prior_close=100, close=99.5)
    result = ingest(data, tmp_path, 0.5)
    assert result["derived"][0]["gap_retention_ratio"] == pytest.approx(0.5)
    assert result["derived"][0]["gap_classification"] == "down_held"


def test_immutable_conflict_corrupt_duplicate_and_pending_rerun(tmp_path):
    ingest(payload(), tmp_path, 0.5)
    changed = payload()
    changed["flags"][0]["catalyst"] = "changed"
    with pytest.raises(OutcomeError, match="immutable flag conflict"):
        ingest(changed, tmp_path, 0.5)
    corrupt = tmp_path / "corrupt"
    corrupt.mkdir()
    (corrupt / "outcomes-state.json").write_text("bad")
    with pytest.raises(OutcomeError, match="corrupt"):
        ingest(payload(), corrupt, 0.5)
    duplicate = payload()
    duplicate["observations"].append(copy.deepcopy(duplicate["observations"][0]))
    duplicate["observations"][-1]["close"] = 999
    with pytest.raises(OutcomeError):
        ingest(duplicate, tmp_path / "duplicate", 0.5)
    pending = payload(observations=False)
    ingest(pending, tmp_path / "pending", 0.5)
    fill = payload(flag=False)
    result = ingest(fill, tmp_path / "pending", 0.5)
    assert result["derived"][0]["status"] == "complete"


def test_equivalent_timestamp_spelling_is_not_a_conflict(tmp_path):
    first = payload()
    ingest(first, tmp_path, 0.5)
    second = payload()
    second["flags"][0]["flag_timestamp"] = "2024-11-04T15:00:00Z"
    result = ingest(second, tmp_path, 0.5)
    assert len(result["flags"]) == 1


def test_existing_state_is_deeply_validated_before_overwrite(tmp_path):
    ingest(payload(), tmp_path, 0.5)
    state_path = tmp_path / "outcomes-state.json"
    state = json.loads(state_path.read_text())
    state["observations"][0]["close"] = -1
    state_path.write_text(json.dumps(state))
    with pytest.raises(OutcomeError):
        ingest(payload(flag=False), tmp_path, 0.5)
    assert json.loads(state_path.read_text())["observations"][0]["close"] == -1


def test_calendar_dst_holiday_halfday_and_tuple_lookup(tmp_path):
    days = [
        session("2024-11-01"),
        session("2024-11-04", close="13:00"),
        session("2024-11-05"),
    ]
    data = payload(flag=False, observations=False)
    data["calendars"][0]["sessions"] = days
    result = ingest(data, tmp_path, 0.5)
    assert len(result["calendars"]) == 1


def test_rejects_live_path_and_symlink(tmp_path):
    with pytest.raises(OutcomeError):
        ingest(payload(), "/home/box/live", 0.5)
    link = tmp_path / "link"
    link.symlink_to(tmp_path)
    with pytest.raises(OutcomeError, match="symlink"):
        ingest(payload(), link, 0.5)
