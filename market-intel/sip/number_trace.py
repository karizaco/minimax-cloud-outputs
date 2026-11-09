"""Trace numeric claims in generated chat text against a SIP run.

Percentage claims use PERCENT_TOLERANCE = 0.05 percentage points while
retaining the requirement that positive and negative changes do not match.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any, Iterable


PERCENT_TOLERANCE = 0.05

_NUMBER_RE = re.compile(
    r"(?<![A-Za-z0-9])"
    r"(?P<sign>[+-])?"
    r"(?P<currency>US\$|\$)?"
    r"(?P<number>\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)"
    r"(?P<suffix>%|x|m|bn)?"
    r"(?![A-Za-z0-9])",
    re.IGNORECASE,
)

_ALLOWED_FIELDS = {
    "last",
    "chg_pct",
    "rvol",
    "dollar_vol",
    "usd_turnover",
    "turnover_usd",
}

_TICKER_FIELDS = {"ticker", "symbol", "display_ticker"}

_MM_TO_USD = 1_000_000.0
_BN_TO_USD = 1_000_000_000.0


def _as_float(value: Any) -> float | None:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def _display_forms(value: float, kind: str) -> set[float]:
    forms = {value}
    if kind in {"percent", "number", "currency"}:
        forms.update(
            {
                round(value),
                round(value, 1),
                round(value, 2),
                math.floor(value),
                math.ceil(value),
            }
        )
    return {float(item) for item in forms if math.isfinite(float(item))}


def extract_numbers(text: str) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    for match in _NUMBER_RE.finditer(text or ""):
        raw = match.group(0)
        number = _as_float(match.group("number").replace(",", ""))
        if number is None:
            continue
        if match.group("sign") == "-":
            number = -number
        suffix = (match.group("suffix") or "").lower()
        currency = match.group("currency")
        if suffix == "%":
            kind = "percent"
        elif suffix == "x":
            kind = "multiple"
        elif currency:
            kind = "currency"
        elif suffix in {"m", "bn"}:
            kind = "currency"
        else:
            kind = "number"
        normalized = number
        if suffix == "m":
            normalized *= _MM_TO_USD
        elif suffix == "bn":
            normalized *= _BN_TO_USD
        found.append(
            {
                "raw": raw,
                "value": normalized,
                "kind": kind,
                "span": [match.start(), match.end()],
            }
        )
    return found


def _walk(run: dict | list) -> Iterable[tuple[str | None, Any]]:
    if isinstance(run, dict):
        for key, value in run.items():
            yield str(key).lower(), value
            yield from _walk(value)
    elif isinstance(run, list):
        for value in run:
            yield from _walk(value)


def _currency_candidates(value: float) -> set[float]:
    candidates = set(_display_forms(value, "currency"))
    candidates.update(
        {
            value / _MM_TO_USD,
            value / _BN_TO_USD,
            round(value / _MM_TO_USD, 1),
            round(value / _BN_TO_USD, 1),
            round(value / _MM_TO_USD),
            round(value / _BN_TO_USD),
        }
    )
    return {float(item) for item in candidates if math.isfinite(float(item))}


def collect_allowed_numbers(run: dict | list) -> set[float]:
    allowed: set[float] = set()
    for field, value in _walk(run):
        if field not in _ALLOWED_FIELDS:
            continue
        if isinstance(value, dict):
            for nested in value.values():
                number = _as_float(nested)
                if number is not None:
                    allowed.update(_display_forms(number, "number"))
            continue
        if isinstance(value, (list, tuple, set)):
            for nested in value:
                number = _as_float(nested)
                if number is not None:
                    allowed.update(_display_forms(number, "number"))
            continue
        number = _as_float(value)
        if number is None:
            continue
        if field in {"dollar_vol", "usd_turnover", "turnover_usd"}:
            allowed.update(_currency_candidates(number))
        elif field == "chg_pct":
            allowed.update(_display_forms(number, "percent"))
        elif field == "rvol":
            allowed.update(_display_forms(number, "multiple"))
        else:
            allowed.update(_display_forms(number, "number"))
    return allowed


def collect_ticker_codes(run: dict | list) -> set[float]:
    """Collect numeric ticker codes from ticker/symbol/display_ticker fields."""
    codes: set[float] = set()
    for field, value in _walk(run):
        if field not in _TICKER_FIELDS:
            continue
        if isinstance(value, dict):
            values = value.values()
        elif isinstance(value, (list, tuple, set)):
            values = value
        else:
            values = (value,)
        for ticker in values:
            if isinstance(ticker, str):
                ticker = ticker.strip()
                if re.fullmatch(r"\d+(?:\.\d+)?", ticker):
                    number = _as_float(ticker)
                    if number is not None:
                        codes.add(number)
            else:
                number = _as_float(ticker)
                if number is not None and float(number).is_integer():
                    codes.add(number)
    return codes


def _context_for(text: str, span: list[int], radius: int = 36) -> str:
    start, end = span
    left = max(0, start - radius)
    right = min(len(text), end + radius)
    return " ".join(text[left:right].split())


def _matches(
    number: dict[str, Any],
    allowed: set[float],
    ticker_codes: set[float] | None = None,
) -> bool:
    value = float(number["value"])
    if (
        number["kind"] == "number"
        and ticker_codes
        and any(
            math.isclose(value, code, rel_tol=1e-9, abs_tol=1e-9)
            for code in ticker_codes
        )
    ):
        return True

    tolerance = max(1e-9, abs(value) * 1e-9)
    for candidate in allowed:
        if number["kind"] == "percent":
            if value > 0 and candidate <= 0:
                continue
            if value < 0 and candidate >= 0:
                continue
            if value == 0 and candidate != 0:
                continue
            if abs(value - candidate) > PERCENT_TOLERANCE:
                continue
        elif not math.isclose(
            value, candidate, rel_tol=1e-9, abs_tol=tolerance
        ):
            continue
        return True
    return False


def check_chat(
    run_json: dict | list,
    chat_md: str,
    *,
    fx_rate: float | None = None,
) -> dict[str, Any]:
    allowed = collect_allowed_numbers(run_json)
    ticker_codes = collect_ticker_codes(run_json)
    if fx_rate is not None:
        fx = _as_float(fx_rate)
        if fx is not None and fx > 0:
            allowed.update({fx, round(fx, 1), round(fx, 2), round(fx)})

    offenders: list[dict[str, Any]] = []
    for number in extract_numbers(chat_md):
        if _matches(number, allowed, ticker_codes):
            continue
        reason = {
            "percent": "percentage is not represented by the run",
            "multiple": "multiple is not represented by the run",
            "currency": "currency amount is not represented by the run",
        }.get(number["kind"], "number is not represented by the run")
        offenders.append(
            {
                "raw": number["raw"],
                "context": _context_for(chat_md, number["span"]),
                "reason": reason,
            }
        )
    return {"ok": not offenders, "offenders": offenders}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check SIP chat numbers against a run")
    parser.add_argument("--run", required=True)
    parser.add_argument("--chat", required=True)
    parser.add_argument("--fx", type=float, default=None)
    args = parser.parse_args(argv)
    try:
        run = json.loads(Path(args.run).read_text(encoding="utf-8"))
        chat = Path(args.chat).read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as exc:
        print(f"number_trace: {exc}", file=sys.stderr)
        return 2
    result = check_chat(run, chat, fx_rate=args.fx)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 5


if __name__ == "__main__":
    raise SystemExit(main())
