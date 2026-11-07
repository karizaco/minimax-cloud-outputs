"""Offline change-only comparison of open and midday SIP snapshots."""
from __future__ import annotations

import copy
import hashlib
import json
import math
from datetime import datetime
from zoneinfo import ZoneInfo

TIERS = ("A", "Soft-A", "TECH_WATCH", "B", "C")
DISPLAY_RANK = {name: index for index, name in enumerate(TIERS)}
QUALITY_RANK = DISPLAY_RANK.copy()
MARKET_ALIASES = {
    "US": "US",
    "us": "US",
    "EU": "EU",
    "europe": "EU",
    "ASX": "ASX",
    "asx": "ASX",
    "JP": "JP",
    "tokyo": "JP",
    "TW": "TW",
    "taiwan": "TW",
}


class ChatError(ValueError):
    pass


def _required(obj, *names):
    missing = [name for name in names if name not in obj]
    if missing:
        raise ChatError("missing required field: " + ", ".join(missing))


def _aware(value, field):
    if not isinstance(value, str):
        raise ChatError(f"{field} must be an ISO timestamp")
    try:
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ChatError(f"{field} is invalid") from exc
    if stamp.tzinfo is None or stamp.utcoffset() is None:
        raise ChatError(f"{field} must be timezone-aware")
    return stamp


def _number(value, field, nullable=False, positive=False):
    if value is None and nullable:
        return None
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
        or (positive and value <= 0)
    ):
        qualifier = "positive and finite" if positive else "finite"
        raise ChatError(f"{field} must be {qualifier}")
    return float(value)


def _text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ChatError(f"{field} must be a non-empty string")
    return value


def _market(value):
    if not isinstance(value, str) or not value.strip():
        raise ChatError("market must be a non-empty string")
    market = MARKET_ALIASES.get(value)
    if market is None:
        raise ChatError(f"unknown market {value}")
    return market


def _basis_valid(row):
    return all(
        isinstance(row.get(name), str) and bool(row[name].strip())
        for name in ("currency", "price_basis", "adjustment_id")
    )


def _validate_snapshot(snapshot, slot):
    if not isinstance(snapshot, dict):
        raise ChatError("snapshot must be an object")
    _required(
        snapshot,
        "market",
        "session_id",
        "calendar_id",
        "timezone",
        "session_date",
        "asof",
        "slot",
        "rows",
    )
    snapshot["market"] = _market(snapshot["market"])
    if snapshot["slot"] != slot:
        raise ChatError(f"snapshot slot must be {slot}")
    try:
        zone = ZoneInfo(snapshot["timezone"])
    except Exception as exc:
        raise ChatError("timezone must be a valid IANA timezone") from exc
    stamp = _aware(snapshot["asof"], "asof")
    if stamp.astimezone(zone).date().isoformat() != snapshot["session_date"]:
        raise ChatError("asof local date does not match session_date")
    if not isinstance(snapshot["rows"], list):
        raise ChatError("rows must be a list")
    seen = set()
    for row in snapshot["rows"]:
        if not isinstance(row, dict):
            raise ChatError("row must be an object")
        _required(
            row,
            "ticker",
            "tier",
            "session_open",
            "prior_close",
            "price",
        )
        _text(row["ticker"], "ticker")
        if row["ticker"] in seen:
            raise ChatError(f"duplicate ticker {row['ticker']}")
        seen.add(row["ticker"])
        if row["tier"] not in TIERS:
            raise ChatError(f"unknown tier {row['tier']}")
        for name in ("session_open", "prior_close", "price"):
            _number(row[name], name, nullable=True, positive=True)
        if "usd_turnover" in row and row["usd_turnover"] is not None:
            _number(row["usd_turnover"], "usd_turnover")
            if row["usd_turnover"] < 0:
                raise ChatError("usd_turnover must be non-negative")
        if "local_turnover" in row and row["local_turnover"] is not None:
            _number(row["local_turnover"], "local_turnover")


def _hash(value):
    return hashlib.sha256(
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode()
    ).hexdigest()


def _gap_state(row, threshold):
    opening = row.get("session_open")
    prior = row.get("prior_close")
    price = row.get("price")
    if opening is None or prior is None or price is None:
        return "unknown"
    if opening == prior:
        return "flat"
    ratio = (price - prior) / (opening - prior)
    if ratio <= 0:
        return "reversed"
    if ratio < threshold:
        return "faded"
    return "held"


def _sort_key(row):
    turnover = row.get("usd_turnover")
    return (
        DISPLAY_RANK[row["tier"]],
        -(float(turnover) if turnover is not None else float("-inf")),
        row["ticker"],
    )


def _baseline_problem(opening, midday, max_age):
    if opening is None:
        return "BASELINE_UNAVAILABLE: open snapshot was not supplied"
    for field in (
        "market",
        "session_id",
        "calendar_id",
        "timezone",
        "session_date",
    ):
        if opening[field] != midday[field]:
            return "BASELINE_UNAVAILABLE: open and midday " + field + " differ"
    old_time = _aware(opening["asof"], "open.asof")
    new_time = _aware(midday["asof"], "midday.asof")
    age = (new_time - old_time).total_seconds() / 3600
    if age <= 0:
        return "BASELINE_UNAVAILABLE: open snapshot must precede midday"
    if age > max_age:
        return (
            "BASELINE_UNAVAILABLE: open snapshot is stale "
            f"({age:.2f}h > {max_age:.2f}h)"
        )
    return None


def _warning_rows(rows, threshold, old_rows=None):
    warnings = []
    old_rows = old_rows or {}
    for row in rows:
        ticker = row["ticker"]
        state = _gap_state(row, threshold)
        if not _basis_valid(row):
            warnings.append(
                f"UNKNOWN BASIS: {ticker} has missing or invalid "
                "currency, price basis, or adjustment"
            )
        if state == "unknown":
            warnings.append(
                f"UNKNOWN GAP: {ticker} has unavailable price or gap basis"
            )
            continue
        old = old_rows.get(ticker)
        if old is None:
            continue
        if not _basis_valid(old):
            warnings.append(
                f"UNKNOWN BASIS: {ticker} open snapshot has missing or invalid "
                "currency, price basis, or adjustment"
            )
        elif any(
            old.get(name) != row.get(name)
            for name in ("currency", "price_basis", "adjustment_id")
        ):
            warnings.append(
                f"UNKNOWN GAP: basis or currency changed for {ticker}"
            )
        elif (
            old.get("session_open") != row.get("session_open")
            or old.get("prior_close") != row.get("prior_close")
        ):
            warnings.append(
                "UNKNOWN GAP: actual session open/prior close "
                f"changed for {ticker}"
            )
        else:
            old_state = _gap_state(old, threshold)
            if old_state == "unknown":
                warnings.append(
                    f"UNKNOWN GAP: {ticker} open snapshot has unavailable "
                    "price or gap basis"
                )
            elif old_state != state:
                warnings.append(
                    f"GAP CHANGED: {ticker} {old_state} -> {state}"
                )
    return warnings


def _display_ticker(row, market):
    if row.get("display_ticker"):
        return str(row["display_ticker"])
    ticker = str(row["ticker"])
    if market == "TW":
        venue = " ".join(
            str(row.get(name, "")) for name in ("venue", "board")
        ).upper()
        if "TPEX" in venue:
            if ticker.endswith(".TW"):
                return ticker[:-3] + ".TPEX"
            if ticker.endswith(".TPE"):
                return ticker
            return ticker + ".TPEX"
        if "TWSE" in venue:
            return ticker[:-3] if ticker.endswith(".TW") else ticker
        return ticker[:-3] if ticker.endswith(".TW") else ticker
    return ticker


def _row_text(row, market):
    ticker = _display_ticker(row, market)
    if market == "JP":
        name = row.get("company_en")
        if not isinstance(name, str) or not name.strip():
            name = "English name unavailable"
    else:
        name = row.get("company_en")
    identity = f"{ticker} {name}" if name else ticker
    bits = [f"- {identity} [{row['tier']}]"]
    if row.get("price") is not None:
        currency = row.get("currency")
        currency = currency if isinstance(currency, str) and currency.strip() else "unavailable"
        bits.append(f"price {row['price']} {currency}")
    else:
        bits.append("price unavailable")
    if row.get("local_turnover") is not None:
        currency = row.get("local_turnover_currency")
        currency = currency if isinstance(currency, str) and currency.strip() else "unavailable"
        bits.append(f"local turnover {row['local_turnover']} {currency}")
    if row.get("usd_turnover") is not None:
        bits.append(f"USD turnover {row['usd_turnover']}")
    return " ".join(bits)


def _direction(old_tier, new_tier):
    return (
        "upgrade"
        if QUALITY_RANK[new_tier] < QUALITY_RANK[old_tier]
        else "downgrade"
    )


def format_chat(result, market):
    lines = [
        f"SIP {market} MIDDAY",
        f"Status: {'COMPLETE' if result['complete'] else 'BASELINE_UNAVAILABLE'}",
    ]
    lines.extend(f"WARNING: {warning}" for warning in result["warnings"])
    if result["changes"]:
        lines.append("Changes:")
        for change in result["changes"]:
            row = change.get("row") or change["old"]
            reasons = change["reasons"]
            lines.append(
                f"{_row_text(row, market)}: " + "; ".join(reasons)
            )
    elif not result["warnings"]:
        lines.append("No material changes.")
    if result.get("show_rows"):
        lines.append("Current rows:")
        lines.extend(_row_text(row, market) for row in result["rows"])
    return "\n".join(lines)


def compare_snapshots(
    open_snapshot,
    midday,
    retention,
    max_open_age_hours=6.0,
):
    midday = copy.deepcopy(midday)
    open_snapshot = (
        copy.deepcopy(open_snapshot) if open_snapshot is not None else None
    )
    if (
        isinstance(retention, bool)
        or not isinstance(retention, (int, float))
        or not math.isfinite(retention)
        or not 0 < retention <= 1
    ):
        raise ChatError("retention must satisfy 0 < retention <= 1")
    if (
        isinstance(max_open_age_hours, bool)
        or not isinstance(max_open_age_hours, (int, float))
        or not math.isfinite(max_open_age_hours)
        or max_open_age_hours < 0
    ):
        raise ChatError(
            "max_open_age_hours must be finite and non-negative"
        )
    _validate_snapshot(midday, "midday")
    if open_snapshot is not None:
        _validate_snapshot(open_snapshot, "open")
    problem = _baseline_problem(open_snapshot, midday, max_open_age_hours)
    if problem:
        warnings = [problem]
        warnings.extend(_warning_rows(midday["rows"], retention))
        result = {
            "complete": False,
            "warnings": warnings,
            "changes": [],
            "rows": sorted(midday["rows"], key=_sort_key),
            "show_rows": True,
            "digest": _hash(midday),
        }
        return format_chat(result, midday["market"])
    before = {row["ticker"]: row for row in open_snapshot["rows"]}
    after = {row["ticker"]: row for row in midday["rows"]}
    grouped = {}
    for ticker in sorted(set(before) | set(after)):
        old = before.get(ticker)
        new = after.get(ticker)
        reasons = []
        if old is None:
            reasons.append("new name")
            row = new
        elif new is None:
            reasons.append("removed (no longer listed, not a gap failure)")
            row = old
        else:
            row = new
            if old["tier"] != new["tier"]:
                reasons.append(
                    f"{_direction(old['tier'], new['tier'])} "
                    f"{old['tier']} -> {new['tier']}"
                )
        grouped[ticker] = {"ticker": ticker, "row": row, "reasons": reasons}
    warnings = _warning_rows(midday["rows"], retention, before)
    for ticker in set(before) & set(after):
        old = before[ticker]
        new = after[ticker]
        comparable = (
            _basis_valid(old)
            and _basis_valid(new)
            and all(
                old.get(name) == new.get(name)
                for name in (
                    "currency",
                    "price_basis",
                    "adjustment_id",
                    "session_open",
                    "prior_close",
                )
            )
        )
        if comparable:
            old_state = _gap_state(old, retention)
            new_state = _gap_state(new, retention)
            if (
                old_state != new_state
                and old_state != "unknown"
                and new_state != "unknown"
            ):
                grouped[ticker]["reasons"].append(
                    f"gap {old_state} -> {new_state}"
                )
    changes = [
        change for change in grouped.values() if change["reasons"]
    ]
    change_rank = {
        "tier_change": 0,
        "gap_change": 1,
        "new_name": 2,
        "removed_name": 3,
    }
    changes.sort(key=lambda change: (_sort_key(change["row"]), change["ticker"]))
    complete = not any(
        warning.startswith("BASELINE_UNAVAILABLE")
        or warning.startswith("UNKNOWN")
        for warning in warnings
    )
    result = {
        "complete": complete,
        "warnings": warnings,
        "changes": changes,
        "rows": sorted(midday["rows"], key=_sort_key),
        "show_rows": False,
        "digest": _hash(midday),
    }
    return format_chat(result, midday["market"])
