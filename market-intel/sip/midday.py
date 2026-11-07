from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _read_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def _ticker_from_markdown_row(line: str) -> str | None:
    stripped = line.strip()
    if not stripped or "|" not in stripped:
        return None

    cells = [cell.strip() for cell in stripped.split("|") if cell.strip()]
    if not cells:
        return None

    first = cells[0]
    if first.lower() in {"ticker", "symbol", "code"}:
        return None
    if all(
        cell and set(cell) <= {"-", ":"}
        for cell in cells
    ):
        return None

    return first.upper()


def load_open_tickers(open_json_or_md_path: str | Path) -> set[str]:
    path = Path(open_json_or_md_path)
    text = _read_text(path)

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        tickers: set[str] = set()
        for line in text.splitlines():
            ticker = _ticker_from_markdown_row(line)
            if ticker:
                tickers.add(ticker)
            elif line.strip().startswith("-"):
                tokens = line.strip().lstrip("- ").split()
                if tokens:
                    tickers.add(tokens[0].upper())
        return tickers

    if isinstance(data, list):
        return {
            str(item.get("ticker", "")).upper()
            for item in data
            if isinstance(item, dict) and item.get("ticker")
        }

    if isinstance(data, dict):
        rows = data.get("rows", data.get("tickers", data.get("candidates", [])))
        if isinstance(rows, list):
            return {
                str(item.get("ticker", item)).upper()
                for item in rows
                if item and str(item.get("ticker", item)).strip()
            }

    return set()


def delta_label(open_row: dict[str, Any], mid_row: dict[str, Any]) -> str:
    try:
        old = float(open_row.get("chg_pct", 0.0))
    except (TypeError, ValueError):
        old = 0.0
    try:
        new = float(mid_row.get("chg_pct", 0.0))
    except (TypeError, ValueError):
        new = 0.0

    if old > 0 and new <= 0:
        return "reversed"
    if old > 0 and abs(new) < abs(old) * 0.5:
        return "faded"
    if old <= 0 and new > 0:
        return "new_catalyst"
    return "holding"
