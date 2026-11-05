from __future__ import annotations

import json
from datetime import date as date_cls
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping
from zoneinfo import ZoneInfo

from sip.config import load_market
from sip.format_taiwan import render_chat, render_digest
from sip.markets.taiwan.adapter import build_candidates
from sip.midday import delta_label, load_open_tickers
from sip.overnight import parse_overnight_carry, promote_if_clears
from sip.paths import assert_safe_out_path
from sip.schema import CandidateRow, validate_row
from sip.tier import run_pipeline


TAIPEI = ZoneInfo("Asia/Taipei")
HOLIDAYS_PATH = Path(
    "/home/box/agent-data/shared-research/run-coverage/holidays.json"
)


def _as_float(value: Any, default: float = 0.0) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return default
    return result


def _venue(value: Any) -> str:
    venue = str(value or "").strip().upper()
    if venue in {"TPEX", "TPE", "OTC", "上櫃"}:
        return "TPEx"
    return "TWSE" if venue in {"", "TWSE", "TSE", "上市"} else venue


def _candidate_to_row(
    candidate: Mapping[str, Any],
    asof: Any = None,
    fx: Any = None,
) -> CandidateRow:
    price = candidate.get("last", candidate.get("price"))
    change = candidate.get("chg_pct", candidate.get("change_percent"))
    turnover = candidate.get("dollar_vol", candidate.get("turnover"))
    dollar_vol = _as_float(turnover)

    flags = candidate.get("flags") or []
    if not isinstance(flags, list):
        flags = list(flags)
    flags = [str(flag) for flag in flags]

    if candidate.get("limit_up") and "LIMIT_UP" not in flags:
        flags.append("LIMIT_UP")
    if candidate.get("limit_down") and "LIMIT_DOWN" not in flags:
        flags.append("LIMIT_DOWN")

    usd_turnover = (
        dollar_vol / float(fx)
        if fx is not None and float(fx) > 0
        else None
    )

    return CandidateRow(
        ticker=str(candidate.get("ticker") or candidate.get("symbol") or ""),
        venue=_venue(candidate.get("venue", candidate.get("board"))),
        instrument_type=str(candidate.get("instrument_type") or "common"),
        last=_as_float(price),
        chg_pct=_as_float(change),
        dollar_vol=dollar_vol,
        rvol=(
            _as_float(candidate.get("rvol"))
            if candidate.get("rvol") is not None
            else None
        ),
        catalyst=candidate.get("catalyst"),
        catalyst_time=candidate.get("catalyst_time"),
        flags=flags,
        source=str(candidate.get("source") or ""),
        asof=str(candidate.get("asof") or asof or ""),
        tier=candidate.get("tier"),
        company_en=candidate.get("company_en", candidate.get("english_name")),
        company_zh=candidate.get("company_zh", candidate.get("name")),
        board=candidate.get("board"),
        mcap_twd=(
            _as_float(candidate.get("mcap_twd"))
            if candidate.get("mcap_twd") is not None
            else None
        ),
        usd_turnover=usd_turnover,
        display_ticker=candidate.get("display_ticker", candidate.get("symbol")),
        why=candidate.get("why"),
    )


def _pipeline_rows(result: Any) -> list[CandidateRow]:
    if isinstance(result, Mapping):
        raw_rows = result.get("candidates", [])
    elif isinstance(result, list):
        raw_rows = result
    else:
        raw_rows = []

    rows: list[CandidateRow] = []
    for row in raw_rows:
        if isinstance(row, CandidateRow):
            rows.append(row)
        elif isinstance(row, Mapping):
            rows.append(_candidate_to_row(row))
    return rows


def _valid_rows(
    candidates: list[Mapping[str, Any]],
    date: str,
    fx: Any = None,
) -> tuple[list[CandidateRow], int]:
    rows: list[CandidateRow] = []
    invalid = 0
    for candidate in candidates:
        try:
            row = _candidate_to_row(candidate, date, fx=fx)
            validation_result = validate_row(row)
            if validation_result is False:
                invalid += 1
                continue
        except Exception:
            invalid += 1
            continue
        rows.append(row)
    return rows, invalid


def _rows_by_tier(rows: list[CandidateRow]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        tier = row.tier or "C"
        grouped.setdefault(tier, []).append(row.asdict())
    return grouped


def _source_health(value: Any) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    if isinstance(value, Mapping):
        for source, detail in value.items():
            if isinstance(detail, Mapping):
                item = dict(detail)
                item.setdefault("source", source)
            else:
                item = {
                    "source": source,
                    "status": (
                        "ok"
                        if detail in (True, "ok", "healthy")
                        else str(detail)
                    ),
                }
            result.append(item)
    elif isinstance(value, list):
        for detail in value:
            if isinstance(detail, Mapping):
                result.append(dict(detail))
            else:
                result.append({"source": "unknown", "status": str(detail)})
    return result


def _parse_date(value: str) -> date_cls:
    return datetime.strptime(value, "%Y-%m-%d").date()


def _is_holiday(value: str) -> bool:
    try:
        parsed = _parse_date(value)
    except ValueError:
        return False

    if parsed.weekday() >= 5:
        return True

    try:
        holidays = json.loads(HOLIDAYS_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        return False

    xtai = holidays.get("XTAI", []) if isinstance(holidays, Mapping) else []
    if isinstance(xtai, Mapping):
        xtai = xtai.get("dates", xtai.get("holidays", []))
    if not isinstance(xtai, list):
        return False

    normalized = {str(item)[:10] for item in xtai}
    return value in normalized


def _holiday_stub(
    root: Path,
    date: str,
    slot: str,
    market: str,
) -> dict[str, Path]:
    json_path = root / f"{date}-{slot}.json"
    md_path = root / f"{date}-{slot}.md"
    chat_path = root / f"{date}-{slot}.chat.md"

    payload = {
        "date": date,
        "slot": slot,
        "market": market,
        "fx": None,
        "source_health": [
            {
                "source": "calendar",
                "status": "ok",
                "detail": "Taiwan market holiday; no session data",
            }
        ],
        "candidates": [],
        "meta": {"holiday": True},
    }
    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    md_path.write_text(
        f"# SIP Market Digest\n\nDate: {date} | Slot: {slot}\n\n"
        "Taiwan market holiday; no digest generated.\n",
        encoding="utf-8",
    )
    chat_path.write_text(
        f"Taiwan market holiday ({date}, {slot}); no SIP chat generated.\n",
        encoding="utf-8",
    )
    return {"json": json_path, "md": md_path, "chat": chat_path}


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _candidate_dicts(rows: list[CandidateRow], fx: Any) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for row in rows:
        candidate = row.asdict()
        candidate["fx"] = fx
        candidate["usd_turnover"] = (
            row.dollar_vol / float(fx)
            if fx is not None and float(fx) > 0
            else None
        )
        result.append(candidate)
    return result


def _apply_open_carry(
    rows: list[CandidateRow],
    root: Path,
    date: str,
    cfg: dict[str, Any],
) -> list[CandidateRow]:
    previous = root / f"{date}-open.json"
    if not previous.exists():
        previous = root / f"{date}-open.md"
    if not previous.exists():
        return rows

    payload = _read_json(previous) if previous.suffix == ".json" else {}
    if not payload:
        return rows

    candidates = payload.get("candidates", payload.get("rows", []))
    if not isinstance(candidates, list):
        candidates = []
    carry = parse_overnight_carry(candidates)
    max_age = int(cfg.get("overnight_carry_max_age_sessions", 1))
    carry = [
        item
        for item in carry
        if int(item.get("age_sessions", 0)) <= max_age
    ]
    if not carry:
        return rows

    floors = cfg.get("open", {}).get("floors", {})
    by_ticker = {row.ticker.upper(): row for row in rows}
    for item in carry:
        ticker = str(item.get("ticker", "")).upper()
        row = by_ticker.get(ticker)
        if row is not None:
            row.flags.append("OVERNIGHT_CARRY")
            row.why = item.get("why") or row.why

    promoted = promote_if_clears(carry, rows, floors)
    promoted_tickers = {row.ticker.upper() for row in promoted}
    return rows


def _apply_midday_delta(
    rows: list[CandidateRow],
    root: Path,
    date: str,
) -> list[CandidateRow]:
    open_path = root / f"{date}-open.json"
    if not open_path.exists():
        open_path = root / f"{date}-open.md"
    if not open_path.exists():
        return rows

    open_rows: list[dict[str, Any]] = []
    if open_path.suffix == ".json":
        payload = _read_json(open_path)
        candidates = payload.get("candidates", payload.get("rows", []))
        if isinstance(candidates, list):
            open_rows = [
                item for item in candidates if isinstance(item, Mapping)
            ]

    if not open_rows:
        return rows

    open_by_ticker = {
        str(item.get("ticker", "")).upper(): dict(item)
        for item in open_rows
        if item.get("ticker")
    }
    open_tickers = set(open_by_ticker)
    current_tickers = {row.ticker.upper() for row in rows}

    for row in rows:
        old = open_by_ticker.get(row.ticker.upper())
        if old is None:
            row.flags.append("NEW_MIDDAY")
            continue
        label = delta_label(old, row.asdict())
        row.flags.append(f"MIDDAY_{label.upper()}")

    for ticker in sorted(open_tickers & current_tickers):
        pass

    return rows


def run_shadow(
    market: str,
    slot: str,
    date: str,
    fixtures_dir: str | Path,
    out_root: str | Path = "/home/box/taiwan-in-play/shadow",
    tv_dump: str | Path | None = None,
    require_mmx_chat: bool = False,
) -> tuple[dict[str, Path], int]:
    root = assert_safe_out_path(out_root, label="shadow output root")
    root.mkdir(parents=True, exist_ok=True)

    market_name = str(market).strip().lower()
    if market_name in {"taiwan", "tw"}:
        market_name = "taiwan"

    if _is_holiday(date):
        return _holiday_stub(root, date, slot, market_name), 0

    built = build_candidates(
        fixtures_dir=Path(fixtures_dir),
        tv_dump_path=Path(tv_dump) if tv_dump else None,
        slot=slot,
        asof=date,
    )
    cfg = load_market(market_name)
    fx = built.get("fx")
    rows, invalid_count = _valid_rows(built.get("candidates", []), date, fx=fx)

    if slot == "open":
        rows = _apply_open_carry(rows, root, date, cfg)
    elif slot == "midday":
        rows = _apply_midday_delta(rows, root, date)

    pipeline = run_pipeline(rows, cfg, slot)
    output_rows = _pipeline_rows(pipeline)
    candidate_dicts = _candidate_dicts(output_rows, fx)

    source_health = _source_health(built.get("source_health", []))
    source_health.append(
        {
            "source": "schema",
            "status": "ok" if invalid_count == 0 else "skipped",
            "detail": f"{invalid_count} invalid rows dropped",
            "count": invalid_count,
        }
    )
    meta = dict(built.get("meta") or {})
    meta.update({"date": date, "slot": slot, "market": market_name, "fx": fx})

    payload: dict[str, Any] = {
        "date": date,
        "slot": slot,
        "market": market_name,
        "fx": fx,
        "source_health": source_health,
        "candidates": candidate_dicts,
        "meta": meta,
    }

    run_dict: dict[str, Any] = {
        "candidates": candidate_dicts,
        "source_health": source_health,
        "fx": fx,
        "date": date,
        "slot": slot,
        "metadata": meta,
    }

    json_path = root / f"{date}-{slot}.json"
    md_path = root / f"{date}-{slot}.md"
    chat_path = root / f"{date}-{slot}.chat.md"

    assert_safe_out_path(json_path, label="shadow JSON")
    assert_safe_out_path(md_path, label="shadow digest")
    assert_safe_out_path(chat_path, label="shadow chat")

    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    md_path.write_text(render_digest(run_dict), encoding="utf-8")

    chat_top_n = cfg.get("chat_top_n", {})
    chat_path.write_text(
        render_chat(
            _rows_by_tier(output_rows),
            fx=fx,
            top_n=chat_top_n,
            midday_turnover_floor=cfg.get("midday", {})
            .get("floors", {})
            .get("turnover_min", 100_000_000),
        ),
        encoding="utf-8",
    )

    paths = {"json": json_path, "md": md_path, "chat": chat_path}

    if require_mmx_chat:
        from sip.draft_mmx import draft_chat

        code = draft_chat(json_path, chat_path)
        if code != 0:
            return paths, int(code)

    return paths, 0


__all__ = ["run_shadow"]
