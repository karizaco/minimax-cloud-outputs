"""Taiwan market candidate adapter."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Mapping

from sip.catalyst_gate import (
    is_boilerplate_mops,
    materiality_class,
    materiality_score,
    visible_excerpt,
)

from .fetch import SourceHealth, fetch_yahoo_ranks
from .names import display_ticker, english_name
from .parse import (
    ParseError,
    parse_cmoney_change_up_html,
    parse_fx_json,
    parse_mops_browser_text,
    parse_mops_html,
    parse_mops_items,
    parse_tpex_roster,
    parse_tv_dump,
    parse_twse_ap04,
    parse_twse_roster,
    parse_yahoo_rank_html,
)


class AdapterError(RuntimeError):
    pass


def _read_fixture(directory: Path, names: tuple[str, ...]) -> tuple[Any, Path | None]:
    for name in names:
        path = directory / name
        if not path.is_file():
            continue
        try:
            return json.loads(path.read_text(encoding="utf-8")), path
        except (OSError, ValueError):
            try:
                return path.read_text(encoding="utf-8"), path
            except OSError:
                continue
    return None, None


def _venue(symbol: str, board: str | None = None) -> str:
    board_value = str(board or "").strip().upper()
    if board_value in {"TPEX", "TPE", "OTC", "上櫃"}:
        return "TPEx"
    if board_value in {"TWSE", "TSE", "TAI", "上市"}:
        return "TWSE"

    upper = str(symbol or "").strip().upper()
    if upper.endswith((".TWO", ".TPEX")) or upper.startswith(("TPEX:", "TPE:")):
        return "TPEx"
    if upper.endswith(".TW") or upper.startswith("TWSE:"):
        return "TWSE"
    return "TWSE"


def _ticker(symbol: str) -> str:
    value = str(symbol or "").strip().upper()
    for prefix in ("TWSE:", "TPEX:", "TPE:"):
        if value.startswith(prefix):
            value = value[len(prefix):]
    return value.split(".")[0]


def _number(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _turnover(row: Mapping[str, Any]) -> float | None:
    value = _number(row.get("turnoverK", row.get("turn")))
    if value is None:
        value = _number(row.get("turnover", row.get("dollar_vol")))
    return value if abs(value) >= 100_000 else value * 1_000


def _instrument_type(row: Mapping[str, Any], code: str) -> str:
    name = str(row.get("name") or "")
    if re.match(r"^00\d{2,}", code) or "正2" in name or "反1" in name:
        return "etf"
    return str(row.get("instrument_type") or "common")


def _candidate(
    row: Mapping[str, Any],
    *,
    source: str,
    roster: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    roster = roster or {}
    symbol = str(
        row.get("sym")
        or row.get("symbol")
        or row.get("ticker")
        or row.get("code")
        or ""
    )
    code = _ticker(symbol)
    board = row.get("board") or row.get("market")
    venue = _venue(symbol, str(board) if board is not None else None)
    display = display_ticker(code, venue)

    roster_item = roster.get(code, {})
    english = str(
        row.get("en")
        or row.get("english_name")
        or (
            roster_item.get("english_name", "")
            if isinstance(roster_item, Mapping)
            else ""
        )
    ).strip()
    if not english:
        english = english_name(code, venue)

    price = _number(row.get("price"))
    previous = _number(row.get("previousClose", row.get("pc")))
    change_percent = _number(row.get("changePercent"))
    if change_percent is None:
        change_percent = _number(row.get("chg"))
    if change_percent is None and price is not None and previous not in (None, 0):
        change_percent = (price / previous - 1.0) * 100.0

    turnover = _turnover(row)
    rvol = _number(row.get("rv", row.get("rvol")))
    mcap = _number(row.get("mcap", row.get("mcap_twd")))

    flags = [str(flag) for flag in (row.get("flags") or [])]
    limit_up = bool(row.get("limitUp", row.get("lu", False)))
    limit_down = bool(row.get("limitDown", row.get("ld", False)))
    if limit_up and "LIMIT_UP" not in flags:
        flags.append("LIMIT_UP")
    if limit_down and "LIMIT_DOWN" not in flags:
        flags.append("LIMIT_DOWN")

    catalyst = row.get("catalyst") or row.get("headline") or row.get("subj")
    result: dict[str, Any] = {
        "symbol": display,
        "display_ticker": display,
        "ticker": code,
        "venue": venue,
        "board": venue,
        "instrument_type": _instrument_type(row, code),
        "tier": str(row.get("tier") or row.get("grade") or "C"),
        "name": str(row.get("name") or "").strip(),
        "english_name": english,
        "company_en": english or None,
        "company_zh": str(row.get("name") or "").strip() or None,
        "price": price,
        "last": price if price is not None else 0.0,
        "change_percent": change_percent,
        "chg_pct": change_percent if change_percent is not None else 0.0,
        "turnover": turnover,
        "dollar_vol": turnover if turnover is not None else 0.0,
        "rvol": rvol,
        "volume": _number(row.get("volume", row.get("vol"))),
        "limit_up": limit_up,
        "limit_down": limit_down,
        "previous_close": previous,
        "day_high": _number(row.get("dayHigh", row.get("hi"))),
        "day_low": _number(row.get("dayLow", row.get("lo"))),
        "mcap_twd": mcap,
        "day_move_hard": _number(row.get("day_move_hard")),
        "source": source,
        "catalyst": catalyst,
        "catalyst_time": row.get("catalyst_time") or row.get("time"),
        "flags": flags,
        "raw": dict(row),
    }
    result["why"] = row.get("why")
    return result


def _load_json_or_text(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    try:
        return json.loads(text)
    except ValueError:
        return text


def _rows(payload: Any, key: str = "candidates") -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, Mapping)]
    if isinstance(payload, Mapping):
        rows = payload.get(key, [])
        if isinstance(rows, list):
            return [row for row in rows if isinstance(row, Mapping)]
    return []


def _add_mover(
    movers: dict[str, dict[str, Any]],
    row: Mapping[str, Any],
    *,
    source: str,
) -> None:
    item = _candidate(row, source=source)
    ticker = str(item.get("ticker") or "").strip()
    if ticker:
        movers.setdefault(ticker, item)


def _materiality_score(headline: str, explanation: str = "") -> int:
    return materiality_score(headline, explanation)


def _materiality_class(headline: str, explanation: str = "") -> int:
    return materiality_class(headline, explanation)


def _is_boilerplate_mops(headline: str, explanation: str = "") -> bool:
    return is_boilerplate_mops(headline, explanation)


def _explanation(row: Mapping[str, Any]) -> str:
    sources: list[Mapping[str, Any]] = [row]
    raw = row.get("raw")
    if isinstance(raw, Mapping):
        sources.append(raw)

    for source in sources:
        for key, value in source.items():
            normalized = re.sub(r"\s+", "", str(key)).casefold()
            if normalized in {"explanation", "說明", "description"}:
                if value is not None:
                    return str(value).strip()
    return ""


def _attach_mops_catalysts(
    movers: dict[str, dict[str, Any]],
    rows: list[Mapping[str, Any]],
    min_score: int = 1,
) -> None:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        ticker = _ticker(
            str(
                row.get("sym")
                or row.get("symbol")
                or row.get("ticker")
                or row.get("code")
                or ""
            )
        )
        headline = str(
            row.get("catalyst")
            or row.get("headline")
            or row.get("subj")
            or ""
        ).strip()
        explanation = _explanation(row)
        catalyst_time = row.get("catalyst_time") or row.get("time")
        raw = row.get("raw")
        if not ticker or not headline:
            continue
        grouped.setdefault(ticker, []).append(
            {
                "ticker": ticker,
                "catalyst": headline,
                "explanation": explanation,
                "catalyst_time": catalyst_time,
                "raw": dict(raw) if isinstance(raw, Mapping) else dict(row),
            }
        )

    for ticker, items in grouped.items():
        target = movers.get(ticker)
        if target is None:
            continue

        eligible = [
            item
            for item in items
            if _materiality_score(
                str(item.get("catalyst") or ""),
                str(item.get("explanation") or ""),
            ) >= min_score
            and not _is_boilerplate_mops(
                str(item.get("catalyst") or ""),
                str(item.get("explanation") or ""),
            )
        ]
        if not eligible:
            continue

        selected = max(
            eligible,
            key=lambda item: (
                _materiality_class(
                    str(item.get("catalyst") or ""),
                    str(item.get("explanation") or ""),
                ),
                _materiality_score(
                    str(item.get("catalyst") or ""),
                    str(item.get("explanation") or ""),
                ),
                str(item.get("catalyst_time") or ""),
            ),
        )
        catalyst = str(selected.get("catalyst") or "").strip()
        explanation = str(selected.get("explanation") or "").strip()
        excerpt = visible_excerpt(catalyst, explanation)
        score = _materiality_score(catalyst, explanation)
        catalyst_class = _materiality_class(catalyst, explanation)
        target["catalyst"] = (
            f"{catalyst} — {excerpt}" if excerpt else catalyst
        )
        target["catalyst_time"] = selected.get("catalyst_time")
        target.setdefault("raw", {})["mops"] = dict(selected.get("raw") or {})
        target["raw"]["mops_explanation"] = explanation
        target["raw"]["mops_materiality"] = score
        target["raw"]["mops_materiality_class"] = catalyst_class


def _load_mops_rows(path: Path) -> list[dict[str, Any]]:
    if path.name == "mops1.html":
        return parse_mops_html(path.read_text(encoding="utf-8"))
    if path.name == "twse-ap04.json":
        return parse_twse_ap04(_load_json_or_text(path))

    payload = _load_json_or_text(path)
    if isinstance(payload, str):
        rows = parse_mops_browser_text(payload)
        if rows:
            return rows
    parsed = parse_mops_items(payload)
    if isinstance(parsed, list):
        return [row for row in parsed if isinstance(row, Mapping)]
    return [row for row in parsed.values() if isinstance(row, Mapping)]


def build_candidates(
    fixtures_dir: str | Path | None = None,
    tv_dump_path: str | Path | None = None,
    slot: str = "open",
    asof: Any = None,
) -> dict[str, Any]:
    health: list[SourceHealth] = []
    movers: dict[str, dict[str, Any]] = {}
    mops_rows: list[Mapping[str, Any]] = []
    primary_ok = False
    directory = Path(fixtures_dir) if fixtures_dir else None

    if directory:
        cands_path = directory / "cands.json"
        if cands_path.is_file():
            try:
                rows = _rows(_load_json_or_text(cands_path))
                for row in rows:
                    _add_mover(movers, row, source="cmoney")
                primary_ok = bool(rows)
                health.append(SourceHealth("cmoney", "ok" if rows else "empty", len(rows)))
            except (OSError, ParseError, ValueError) as exc:
                health.append(SourceHealth("cmoney", "blocked", detail=str(exc)))
        else:
            health.append(SourceHealth("cmoney", "skipped", detail="fixture not found"))

        mops_names = (
            "mops_items.json",
            "mops-browser.txt",
            "mops_browser.txt",
            "mops-browser.md",
            "mops1.html",
            "twse-ap04.json",
        )
        mops_paths = [
            directory / name for name in mops_names if (directory / name).is_file()
        ]
        if mops_paths:
            errors: list[str] = []
            for mops_path in mops_paths:
                try:
                    mops_rows.extend(_load_mops_rows(mops_path))
                except (OSError, ParseError, ValueError) as exc:
                    errors.append(f"{mops_path.name}: {exc}")
            if mops_rows:
                health.append(SourceHealth("mops", "ok", len(mops_rows)))
            elif errors:
                health.append(
                    SourceHealth(
                        "mops",
                        "coverage_failed",
                        detail="; ".join(errors),
                    )
                )
            else:
                health.append(
                    SourceHealth(
                        "mops",
                        "coverage_failed",
                        detail=(
                            "MOPS fixture contained no filing rows; required one of: "
                            + ", ".join(mops_names)
                        ),
                    )
                )
        else:
            health.append(
                SourceHealth(
                    "mops",
                    "coverage_failed",
                    detail=(
                        "MOPS fixture missing; required one of: "
                        + ", ".join(mops_names)
                    ),
                )
            )

        yahoo_names = (
            "yahoo_rank.html",
            "yahoo-tai-turnover.html",
            "yahoo-tai-change-up.html",
            "yahoo-two-turnover.html",
            "yahoo-two-change-up.html",
        )
        yahoo_path = next(
            (directory / name for name in yahoo_names if (directory / name).is_file()),
            None,
        )
        if yahoo_path is not None:
            try:
                rows = parse_yahoo_rank_html(yahoo_path.read_text(encoding="utf-8"))
                for row in rows:
                    _add_mover(movers, row, source="yahoo")
                primary_ok = primary_ok or bool(rows)
                health.append(SourceHealth("yahoo", "ok" if rows else "empty", len(rows)))
            except (OSError, ParseError, ValueError) as exc:
                health.append(SourceHealth("yahoo", "blocked", detail=str(exc)))
        else:
            health.append(SourceHealth("yahoo", "skipped", detail="fixture not found"))

        cmoney_path = directory / "cmoney_change_up.html"
        if cmoney_path.is_file():
            try:
                rows = parse_cmoney_change_up_html(cmoney_path.read_text(encoding="utf-8"))
                for row in rows:
                    _add_mover(movers, row, source="cmoney")
                primary_ok = primary_ok or bool(rows)
                health.append(SourceHealth("cmoney_change_up", "ok" if rows else "empty", len(rows)))
            except (OSError, ParseError, ValueError) as exc:
                health.append(SourceHealth("cmoney_change_up", "blocked", detail=str(exc)))
        else:
            health.append(SourceHealth("cmoney_change_up", "skipped", detail="fixture not found"))

        fx_payload, _ = _read_fixture(directory, ("fx.json",))
        fx: float | None = None
        if fx_payload is not None:
            try:
                parsed = parse_fx_json(fx_payload)
                if isinstance(parsed, Mapping):
                    rate = parsed.get("rate", parsed.get("TWD"))
                    fx = _number(rate)
                else:
                    fx = _number(parsed)
                health.append(
                    SourceHealth(
                        "fx",
                        "ok" if fx is not None else "empty",
                        detail=str(fx) if fx is not None else None,
                    )
                )
            except (OSError, ParseError, ValueError, TypeError) as exc:
                health.append(SourceHealth("fx", "blocked", detail=str(exc)))
        else:
            health.append(SourceHealth("fx", "skipped", detail="fixture not found"))
    else:
        fx = None
        health.append(SourceHealth("fx", "skipped", detail="fixtures not configured"))

    dump_path = Path(tv_dump_path) if tv_dump_path else None
    if dump_path is None and directory:
        candidate = directory / "tv-dump.json"
        if candidate.is_file():
            dump_path = candidate
    if dump_path and dump_path.is_file():
        try:
            rows = parse_tv_dump(dump_path.read_text(encoding="utf-8"))
            for row in rows:
                _add_mover(movers, row, source="tradingview")
            primary_ok = primary_ok or bool(rows)
            health.append(
                SourceHealth("tradingview", "ok" if rows else "empty", len(rows))
            )
        except (OSError, ParseError, ValueError) as exc:
            health.append(SourceHealth("tradingview", "blocked", detail=str(exc)))
    else:
        health.append(SourceHealth("tradingview", "skipped", detail="dump not found"))

    _attach_mops_catalysts(movers, mops_rows)

    if not primary_ok and not any(
        item["source"] in {"yahoo", "cmoney", "tradingview"}
        for item in movers.values()
    ):
        raise AdapterError("all primary Taiwan movers sources failed")

    candidates = sorted(
        movers.values(),
        key=lambda item: abs(float(item.get("change_percent") or 0)),
        reverse=True,
    )
    return {
        "candidates": candidates,
        "source_health": [item.to_dict() for item in health],
        "fx": fx,
        "meta": {
            "market": "TW",
            "slot": slot,
            "asof": asof,
            "count": len(candidates),
        },
    }
