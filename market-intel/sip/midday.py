from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _read_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def load_open_tickers(open_json_or_md_path: str | Path) -> set[str]:
    path = Path(open_json_or_md_path)
    text = _read_text(path)
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        tickers = set()
        for line in text.splitlines():
            if "|" in line:
                parts = [part.strip() for part in line.split("|")]
                if parts:
                    tickers.add(parts[0].upper())
            elif line.strip().startswith("-"):
                tokens = line.strip().lstrip("- ").split()
                if tokens:
                    tickers.add(tokens[0].upper())
        return tickers
    if isinstance(data, list):
        return {str(item.get("ticker", "")).upper() for item in data if isinstance(item, dict) and item.get("ticker")}
    if isinstance(data, dict):
        rows = data.get("rows", data.get("tickers", []))
        if isinstance(rows, list):
            return {str(item.get("ticker", item)).upper() for item in rows if item}
    return set()


def delta_label(open_row: dict[str, Any], mid_row: dict[str, Any]) -> str:
    old = float(open_row.get("chg_pct", 0.0))
    new = float(mid_row.get("chg_pct", 0.0))
    if old > 0 and new <= 0:
        return "reversed"
    if old > 0 and abs(new) < abs(old) * 0.5:
        return "faded"
    if old <= 0 and new > 0:
        return "new_catalyst"
    return "holding"
