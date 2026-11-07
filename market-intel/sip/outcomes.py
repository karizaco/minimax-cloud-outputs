"""Deterministic offline SIP outcome ingestion."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import tempfile
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ALLOWED_ROOTS = ("/workspace/stage", "/tmp")
MAX_QUOTE_AGE_SECONDS = 60.0
CANONICAL_TIERS = {"A", "Soft-A", "TECH_WATCH", "B", "C"}


class OutcomeError(ValueError):
    pass


def _obj(value, field):
    if not isinstance(value, dict):
        raise OutcomeError(f"{field} must be an object")
    return value


def _required(obj, *names):
    missing = [name for name in names if name not in obj]
    if missing:
        raise OutcomeError("missing required input: " + ", ".join(missing))


def _aware(value, field):
    if not isinstance(value, str):
        raise OutcomeError(f"{field} must be an ISO timestamp")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise OutcomeError(f"{field} is not a valid ISO timestamp") from exc
    if result.tzinfo is None or result.utcoffset() is None:
        raise OutcomeError(f"{field} must be timezone-aware")
    return result.astimezone(ZoneInfo("UTC"))


def _number(value, field, positive=False, nullable=False):
    if value is None and nullable:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise OutcomeError(f"{field} must be numeric")
    value = float(value)
    if not math.isfinite(value) or (positive and value <= 0):
        raise OutcomeError(
            f"{field} must be finite" + (" and positive" if positive else "")
        )
    return value


def _text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise OutcomeError(f"{field} must be a non-empty string")
    return value


def _calendar_key(calendar):
    return (
        calendar["market"],
        calendar["venue"],
        calendar["calendar_id"],
    )


def _session_key(session):
    return session["session_id"]


def _observation_key(observation):
    return (
        observation["market"],
        observation["venue"],
        observation["calendar_id"],
        observation["ticker"],
        observation["session_id"],
    )


def validate_calendars(calendars):
    if not isinstance(calendars, list) or not calendars:
        raise OutcomeError("calendars must be a non-empty list")
    result = {}
    for raw in calendars:
        calendar = _obj(raw, "calendar")
        _required(
            calendar,
            "calendar_id",
            "market",
            "venue",
            "timezone",
            "sessions",
        )
        for name in ("calendar_id", "market", "venue"):
            _text(calendar[name], f"calendar.{name}")
        key = _calendar_key(calendar)
        if key in result:
            raise OutcomeError(f"duplicate calendar {key}")
        try:
            zone = ZoneInfo(calendar["timezone"])
        except Exception as exc:
            raise OutcomeError(
                "calendar.timezone must be a valid IANA timezone"
            ) from exc
        sessions = calendar["sessions"]
        if not isinstance(sessions, list) or not sessions:
            raise OutcomeError("calendar.sessions must be a non-empty list")
        ids = set()
        dates = set()
        normalized = []
        previous_close = None
        for raw_session in sessions:
            session = _obj(raw_session, "session")
            _required(session, "session_id", "date", "open", "close")
            session_id = _text(
                session["session_id"], "session.session_id"
            )
            if session_id in ids:
                raise OutcomeError(f"duplicate session_id {session_id}")
            ids.add(session_id)
            date = _text(session["date"], "session.date")
            if date in dates:
                raise OutcomeError(f"duplicate session date {date}")
            dates.add(date)
            opened = _aware(session["open"], "session.open")
            closed = _aware(session["close"], "session.close")
            if opened >= closed:
                raise OutcomeError("session.open must precede session.close")
            if (
                opened.astimezone(zone).date().isoformat() != date
                or closed.astimezone(zone).date().isoformat() != date
            ):
                raise OutcomeError(
                    "session local date does not match calendar timezone/date"
                )
            if previous_close is not None and opened < previous_close:
                raise OutcomeError(
                    "calendar sessions must be ordered and nonoverlapping"
                )
            previous_close = closed
            normalized.append(
                {
                    "session_id": session_id,
                    "date": date,
                    "open": opened.isoformat(),
                    "close": closed.isoformat(),
                }
            )
        result[key] = {**calendar, "sessions": normalized}
    return result


def _find_session(calendars, item):
    key = (item["market"], item["venue"], item["calendar_id"])
    calendar = calendars.get(key)
    if calendar is None:
        raise OutcomeError(
            "item references an unknown market/venue/calendar"
        )
    for index, session in enumerate(calendar["sessions"]):
        if session["session_id"] == item["session_id"]:
            return calendar, session, index
    raise OutcomeError("item references an unknown session")


def _validate_flag(flag, calendars):
    _obj(flag, "flag")
    _required(
        flag,
        "market",
        "venue",
        "ticker",
        "tier",
        "catalyst",
        "calendar_id",
        "session_id",
        "flag_timestamp",
        "flag_price",
        "quote_timestamp",
        "quote_provenance",
        "currency",
        "price_basis",
        "adjustment_id",
    )
    for name in (
        "ticker",
        "tier",
        "currency",
        "price_basis",
        "adjustment_id",
    ):
        _text(flag[name], f"flag.{name}")
    if flag["tier"] not in CANONICAL_TIERS:
        raise OutcomeError(f"unknown flag tier {flag['tier']}")
    if flag["catalyst"] is None:
        if flag["tier"] != "TECH_WATCH":
            raise OutcomeError("catalyst may be null only for TECH_WATCH flags")
    else:
        _text(flag["catalyst"], "flag.catalyst")
    _, session, _ = _find_session(calendars, flag)
    stamp = _aware(flag["flag_timestamp"], "flag_timestamp")
    opened = _aware(session["open"], "session.open")
    closed = _aware(session["close"], "session.close")
    if not opened <= stamp < closed:
        raise OutcomeError("flag_timestamp must be inside its declared session")
    price = _number(
        flag["flag_price"], "flag_price", positive=True, nullable=True
    )
    if price is None:
        if (
            flag["quote_timestamp"] is not None
            or flag["quote_provenance"] is not None
        ):
            raise OutcomeError(
                "null flag_price requires null quote_timestamp "
                "and quote_provenance"
            )
    else:
        quote_stamp = _aware(flag["quote_timestamp"], "quote_timestamp")
        if quote_stamp > stamp:
            raise OutcomeError("quote_timestamp cannot be after flag_timestamp")
        _text(flag["quote_provenance"], "quote_provenance")
    if "flag_change_pct" in flag:
        _number(flag["flag_change_pct"], "flag_change_pct")


def _validate_observation(observation, calendars):
    _obj(observation, "observation")
    _required(
        observation,
        "market",
        "venue",
        "calendar_id",
        "ticker",
        "session_id",
        "date",
        "timestamp",
        "open",
        "prior_close",
        "close",
        "final",
        "currency",
        "price_basis",
        "adjustment_id",
        "provenance",
    )
    key = (
        observation["market"],
        observation["venue"],
        observation["calendar_id"],
    )
    calendar = calendars.get(key)
    if calendar is None:
        raise OutcomeError(
            "observation references an unknown market/venue/calendar"
        )
    session = next(
        (
            item
            for item in calendar["sessions"]
            if item["session_id"] == observation["session_id"]
        ),
        None,
    )
    if session is None:
        raise OutcomeError("observation references an unknown session")
    stamp = _aware(observation["timestamp"], "observation.timestamp")
    if stamp != _aware(session["close"], "session.close"):
        raise OutcomeError(
            "observation timestamp must equal session close"
        )
    if observation["date"] != session["date"]:
        raise OutcomeError("observation date does not match session")
    if observation["final"] is not True:
        raise OutcomeError("only final=true observations are accepted")
    for name in ("open", "prior_close"):
        _number(
            observation[name],
            f"observation.{name}",
            positive=True,
            nullable=True,
        )
    _number(observation["close"], "observation.close", positive=True)
    for name in (
        "currency",
        "price_basis",
        "adjustment_id",
        "provenance",
    ):
        _text(observation[name], f"observation.{name}")


def _stable_id(flag):
    stamp = _aware(flag["flag_timestamp"], "flag_timestamp").isoformat()
    raw = "|".join(
        (flag["market"], flag["venue"], flag["ticker"], stamp)
    )
    return hashlib.sha256(raw.encode()).hexdigest()[:24]


def _pct(end, start):
    if end is None or start is None or start == 0:
        return None
    return (end / start - 1.0) * 100.0


def _gap(observation, retention):
    if observation is None:
        return "unknown", None, None
    opening = observation["open"]
    prior = observation["prior_close"]
    closing = observation["close"]
    if opening is None or prior is None:
        return "unknown", None, "gap_basis_unavailable"
    if opening == prior:
        return "flat", 0.0, None
    ratio = (closing - prior) / (opening - prior)
    if ratio <= 0:
        state = "reversed"
    elif ratio < retention:
        state = "faded"
    else:
        state = "held"
    cohort = "up" if opening > prior else "down"
    return f"{cohort}_{state}", ratio, None


def _derived(flag, calendars, observations, retention, max_age):
    _, session, index = _find_session(calendars, flag)
    own = observations.get(
        (
            flag["market"],
            flag["venue"],
            flag["calendar_id"],
            flag["ticker"],
            session["session_id"],
        )
    )
    next_session = (
        calendars[
            (
                flag["market"],
                flag["venue"],
                flag["calendar_id"],
            )
        ]["sessions"][index + 1]
        if index + 1
        < len(
            calendars[
                (
                    flag["market"],
                    flag["venue"],
                    flag["calendar_id"],
                )
            ]["sessions"]
        )
        else None
    )
    following = (
        observations.get(
            (
                flag["market"],
                flag["venue"],
                flag["calendar_id"],
                flag["ticker"],
                next_session["session_id"],
            )
        )
        if next_session
        else None
    )
    reasons = []
    same = None
    next_move = None
    if flag["flag_price"] is None:
        reasons.append("historical_flag_price_unavailable")
    if own is None:
        reasons.append("flag_session_observation_pending")
    elif (
        own["currency"],
        own["price_basis"],
        own["adjustment_id"],
    ) != (
        flag["currency"],
        flag["price_basis"],
        flag["adjustment_id"],
    ):
        reasons.append("split_or_adjustment_basis_mismatch")
    else:
        same = _pct(own["close"], flag["flag_price"])
    if next_session is None:
        reasons.append("calendar_end_next_session_pending")
    elif following is None:
        reasons.append("next_session_observation_pending")
    elif own is None:
        reasons.append("same_session_close_unavailable")
    elif (
        following["currency"],
        following["price_basis"],
        following["adjustment_id"],
    ) != (
        own["currency"],
        own["price_basis"],
        own["adjustment_id"],
    ):
        reasons.append("split_or_adjustment_basis_mismatch")
    else:
        next_move = _pct(following["close"], own["close"])
    gap, ratio, gap_reason = _gap(own, retention)
    if gap_reason:
        reasons.append(gap_reason)
    if flag["flag_price"] is not None:
        age = (
            _aware(flag["flag_timestamp"], "flag_timestamp")
            - _aware(flag["quote_timestamp"], "quote_timestamp")
        ).total_seconds()
        if age < 0 or age > max_age:
            same = None
            reasons.append("quote_stale_or_ahead_of_flag")
    flag_change = flag.get("flag_change_pct")
    if flag_change is None:
        flag_cohort = "unknown"
    elif flag_change > 0:
        flag_cohort = "up"
    elif flag_change < 0:
        flag_cohort = "down"
    else:
        flag_cohort = "flat"
    if ratio is None:
        cohort = "flat_or_unknown"
    elif own is None:
        cohort = "flat_or_unknown"
    elif own["open"] == own["prior_close"]:
        cohort = "flat"
    else:
        cohort = "up" if own["open"] > own["prior_close"] else "down"
    return {
        **flag,
        "id": _stable_id(flag),
        "same_close_vs_flag_pct": same,
        "next_close_vs_same_close_pct": next_move,
        "same_session_close": own["close"] if own else None,
        "next_session_close": following["close"] if following else None,
        "gap_classification": gap,
        "gap_retention_ratio": ratio,
        "gap_cohort": cohort,
        "flag_cohort": flag_cohort,
        "status": (
            "complete"
            if same is not None and next_move is not None
            else "pending"
        ),
        "pending_reasons": sorted(set(reasons)),
    }


def _safe_directory(path):
    original = Path(path).expanduser()
    if original.is_symlink():
        raise OutcomeError("state directory cannot be a symlink")
    resolved = original.resolve()
    if not any(
        resolved == Path(root).resolve()
        or Path(root).resolve() in resolved.parents
        for root in ALLOWED_ROOTS
    ):
        raise OutcomeError(
            "state directory must be under /workspace/stage or /tmp"
        )
    return resolved


def _atomic(path, writer):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        raise OutcomeError(
            f"output target cannot be a symlink: {path.name}"
        )
    fd, temp_name = tempfile.mkstemp(
        prefix=path.name + ".", dir=path.parent
    )
    try:
        with os.fdopen(
            fd, "w", encoding="utf-8", newline=""
        ) as handle:
            writer(handle)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def _normalize_flag(flag):
    result = dict(flag)
    result["flag_timestamp"] = _aware(
        result["flag_timestamp"], "flag_timestamp"
    ).isoformat()
    if result["quote_timestamp"] is not None:
        result["quote_timestamp"] = _aware(
            result["quote_timestamp"], "quote_timestamp"
        ).isoformat()
    result["id"] = _stable_id(result)
    return result


def _normalize_observation(observation):
    result = dict(observation)
    result["timestamp"] = _aware(
        result["timestamp"], "observation.timestamp"
    ).isoformat()
    return result


def ingest(
    payload,
    state_dir,
    retention,
    max_quote_age_seconds=MAX_QUOTE_AGE_SECONDS,
):
    if (
        isinstance(retention, bool)
        or not isinstance(retention, (int, float))
        or not math.isfinite(retention)
        or not 0 < retention <= 1
    ):
        raise OutcomeError("retention must satisfy 0 < retention <= 1")
    if (
        isinstance(max_quote_age_seconds, bool)
        or not isinstance(max_quote_age_seconds, (int, float))
        or not math.isfinite(max_quote_age_seconds)
        or max_quote_age_seconds < 0
    ):
        raise OutcomeError(
            "max_quote_age_seconds must be finite and non-negative"
        )
    directory = _safe_directory(state_dir)
    state_path = directory / "outcomes-state.json"
    csv_path = directory / "outcomes.csv"
    if state_path.exists():
        if state_path.is_symlink():
            raise OutcomeError("state file cannot be a symlink")
        try:
            state = json.loads(
                state_path.read_text(encoding="utf-8")
            )
        except (OSError, json.JSONDecodeError) as exc:
            raise OutcomeError(
                "existing state is corrupt; refusing to overwrite"
            ) from exc
        if (
            not isinstance(state, dict)
            or state.get("schema_version") != 2
            or not isinstance(state.get("flags"), list)
            or not isinstance(state.get("observations"), list)
            or not isinstance(state.get("calendars"), list)
        ):
            raise OutcomeError(
                "existing state has an invalid schema; refusing to overwrite"
            )
    else:
        state = {
            "schema_version": 2,
            "calendars": [],
            "flags": [],
            "observations": [],
        }
    incoming = _obj(payload, "payload")
    for name in ("calendars", "flags", "observations"):
        if name not in incoming or not isinstance(incoming[name], list):
            raise OutcomeError(f"payload.{name} must be a list")
    incoming_calendars = validate_calendars(incoming["calendars"])
    persisted_calendars = (
        validate_calendars(state["calendars"])
        if state["calendars"]
        else {}
    )
    flags_by_id = {}
    for raw in state["flags"]:
        flag = _normalize_flag(raw)
        _validate_flag(flag, persisted_calendars)
        identifier = flag["id"]
        if identifier in flags_by_id:
            raise OutcomeError(
                "existing state contains duplicate flag identities"
            )
        flags_by_id[identifier] = flag
    observations_by_key = {}
    for raw in state["observations"]:
        observation = _normalize_observation(raw)
        _validate_observation(observation, persisted_calendars)
        key = _observation_key(observation)
        if key in observations_by_key:
            raise OutcomeError(
                "existing state contains duplicate observation identities"
            )
        observations_by_key[key] = observation
    combined = dict(persisted_calendars)
    for key, calendar in incoming_calendars.items():
        if key not in combined:
            combined[key] = calendar
            continue
        old = combined[key]
        new = calendar
        if old["timezone"] != new["timezone"]:
            raise OutcomeError(f"immutable calendar conflict for {key}")
        old_sessions = old["sessions"]
        if (
            len(new["sessions"]) < len(old_sessions)
            or new["sessions"][: len(old_sessions)] != old_sessions
        ):
            raise OutcomeError(
                f"immutable calendar session conflict for {key}"
            )
        combined[key] = new
    for raw in incoming["flags"]:
        flag = _normalize_flag(raw)
        _validate_flag(flag, combined)
        identifier = flag["id"]
        if identifier in flags_by_id:
            if flags_by_id[identifier] != flag:
                raise OutcomeError(
                    f"immutable flag conflict for {identifier}"
                )
        else:
            flags_by_id[identifier] = flag
    for raw in incoming["observations"]:
        observation = _normalize_observation(raw)
        _validate_observation(observation, combined)
        key = _observation_key(observation)
        if key in observations_by_key:
            if observations_by_key[key] != observation:
                raise OutcomeError(
                    f"immutable observation conflict for {key}"
                )
        else:
            observations_by_key[key] = observation
    flags = sorted(flags_by_id.values(), key=lambda item: item["id"])
    observations = sorted(
        observations_by_key.values(),
        key=_observation_key,
    )
    derived = [
        _derived(
            flag,
            combined,
            observations_by_key,
            retention,
            max_quote_age_seconds,
        )
        for flag in flags
    ]
    new_state = {
        "schema_version": 2,
        "calendars": list(combined.values()),
        "flags": flags,
        "observations": observations,
        "derived": derived,
        "params": {
            "retention": retention,
            "max_quote_age_seconds": max_quote_age_seconds,
        },
    }

    def write_state(handle):
        json.dump(
            new_state,
            handle,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        handle.write("\n")

    _atomic(state_path, write_state)
    columns = [
        "id",
        "market",
        "venue",
        "calendar_id",
        "ticker",
        "tier",
        "catalyst",
        "flag_timestamp",
        "flag_price",
        "quote_timestamp",
        "quote_provenance",
        "currency",
        "price_basis",
        "adjustment_id",
        "same_session_close",
        "next_session_close",
        "same_close_vs_flag_pct",
        "next_close_vs_same_close_pct",
        "gap_classification",
        "gap_retention_ratio",
        "gap_cohort",
        "flag_cohort",
        "status",
        "pending_reasons",
    ]

    def write_csv(handle):
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for item in derived:
            row = {name: item.get(name) for name in columns}
            row["pending_reasons"] = ";".join(
                item["pending_reasons"]
            )
            writer.writerow(row)

    _atomic(csv_path, write_csv)
    return new_state
