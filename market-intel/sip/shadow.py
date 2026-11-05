from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from sip.config import load_market
from sip.format_taiwan import render_chat, render_digest
from sip.markets.taiwan.adapter import build_candidates
from sip.schema import CandidateRow, validate_row
from sip.tier import run_pipeline


def _as_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _venue(value: Any) -> str:
    venue = str(value or "").strip().upper()
    if venue in {"TPEX", "TPE", "OTC", "上櫃"}:
        return "TPEx"
    return "TWSE" if venue in {"", "TWSE", "TSE", "上市"} else venue


def _candidate_to_row(candidate: Mapping[str, Any], asof: Any = None) -> CandidateRow:
    price = candidate.get("last", candidate.get("price"))
    change = candidate.get("chg_pct", candidate.get("change_percent"))
    turnover = candidate.get("dollar_vol", candidate.get("turnover"))
    flags = candidate.get("flags") or []
    if not isinstance(flags, list):
        flags = list(flags)

    return CandidateRow(
        ticker=str(candidate.get("ticker") or candidate.get("symbol") or ""),
        venue=_venue(candidate.get("venue", candidate.get("board"))),
        instrument_type=str(candidate.get("instrument_type") or "common"),
        last=_as_float(price),
        chg_pct=_as_float(change),
        dollar_vol=_as_float(turnover),
        rvol=(
            _as_float(candidate.get("rvol"))
            if candidate.get("rvol") is not None
            else None
        ),
        catalyst=candidate.get("catalyst"),
        catalyst_time=candidate.get("catalyst_time"),
        flags=list(flags),
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
        usd_turnover=(
            _as_float(candidate.get("usd_turnover"))
            if candidate.get("usd_turnover") is not None
            else None
        ),
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
) -> list[CandidateRow]:
    rows: list[CandidateRow] = []
    for candidate in candidates:
        try:
            row = _candidate_to_row(candidate, date)
            validation_result = validate_row(row)
            if validation_result is False:
                continue
        except Exception:
            continue
        rows.append(row)
    return rows


def _rows_by_tier(rows: list[CandidateRow]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        tier = row.tier or "C"
        grouped.setdefault(tier, []).append(row.asdict())
    return grouped


def run_shadow(
    market: str,
    slot: str,
    date: str,
    fixtures_dir: str | Path,
    out_root: str | Path = "/home/box/taiwan-in-play/shadow",
    tv_dump: str | Path | None = None,
    require_mmx_chat: bool = False,
) -> dict[str, Path]:
    root = Path(out_root).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    market_name = str(market).strip().lower()
    if market_name in {"taiwan", "tw"}:
        market_name = "taiwan"

    built = build_candidates(
        fixtures_dir=Path(fixtures_dir),
        tv_dump_path=Path(tv_dump) if tv_dump else None,
        slot=slot,
        asof=date,
    )
    cfg = load_market(market_name)
    rows = _valid_rows(built.get("candidates", []), date)
    pipeline = run_pipeline(rows, cfg, slot)
    output_rows = _pipeline_rows(pipeline)
    candidate_dicts = [row.asdict() for row in output_rows]

    source_health = built.get("source_health", [])
    fx = built.get("fx")
    meta = dict(built.get("meta") or {})
    meta.update({"date": date, "slot": slot, "market": market_name})

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
    }

    json_path = root / f"{date}-{slot}.json"
    md_path = root / f"{date}-{slot}.md"
    chat_path = root / f"{date}-{slot}.chat.md"

    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    md_path.write_text(render_digest(run_dict), encoding="utf-8")
    chat_path.write_text(
        render_chat(_rows_by_tier(output_rows)),
        encoding="utf-8",
    )

    if require_mmx_chat:
        try:
            from sip.draft_mmx import draft_mmx
        except ImportError as exc:
            raise RuntimeError("MMX draft support is unavailable") from exc
        draft_path = root / f"{date}-{slot}.mmx.md"
        draft_path.write_text(draft_mmx(run_dict), encoding="utf-8")

    return {
        "json": json_path,
        "md": md_path,
        "chat": chat_path,
    }
