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
from datetime import date as date_cls
from pathlib import Path
from typing import Any, Iterable, Mapping


PERCENT_TOLERANCE = 0.05

_NUMBER_RE = re.compile(
    r"(?<![A-Za-z0-9])"
    r"(?P<sign>[+-])?"
    r"(?P<currency>US\$|\$)?"
    r"(?P<number>\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)"
    r"(?P<suffix>%|x|m|bn)?"
    r"\s*"
    r"(?P<yi>億美元|億美金|億元|億台幣|億)?"
    r"(?![A-Za-z0-9])",
    re.IGNORECASE,
)

_ALLOWED_FIELDS = {
    "last", "chg_pct", "rvol", "dollar_vol", "usd_turnover", "turnover_usd",
}
_TICKER_FIELDS = {"ticker", "symbol", "display_ticker"}
_MM_TO_USD = 1_000_000.0
_BN_TO_USD = 1_000_000_000.0
_YI = 100_000_000.0


def _as_float(value: Any) -> float | None:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def _display_forms(value: float, kind: str) -> set[float]:
    forms = {value}
    if kind in {"percent", "number", "currency", "multiple"}:
        forms.update({round(value), round(value, 1), round(value, 2),
                      math.floor(value), math.ceil(value)})
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
        yi = match.group("yi") or ""
        if yi:
            kind = "usd_yi" if yi in {"億美元", "億美金"} else "twd_yi"
        elif suffix == "%":
            kind = "percent"
        elif suffix == "x":
            kind = "multiple"
        elif currency:
            kind = "usd_amount"
        elif suffix in {"m", "bn"}:
            kind = "twd_amount"
        else:
            kind = "number"
        normalized = number
        if suffix == "m":
            normalized *= _MM_TO_USD
        elif suffix == "bn":
            normalized *= _BN_TO_USD
        elif yi:
            normalized *= _YI
        found.append({"raw": raw, "value": normalized, "kind": kind,
                      "span": [match.start(), match.end()]})
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
    millions = value / _MM_TO_USD
    billions = value / _BN_TO_USD
    candidates.update({millions, billions, round(millions, 1), round(millions, 2),
                       round(millions), round(billions, 1), round(billions, 2),
                       round(billions), round(millions, 1) * _MM_TO_USD,
                       round(millions, 2) * _MM_TO_USD, round(millions) * _MM_TO_USD,
                       round(billions, 1) * _BN_TO_USD, round(billions, 2) * _BN_TO_USD,
                       round(billions) * _BN_TO_USD})
    return {float(item) for item in candidates if math.isfinite(float(item))}


def _yi_candidates(value: float, decimals: tuple[int, ...] = (1, 2, 4)) -> set[float]:
    yi_value = value / _YI
    candidates: set[float] = {yi_value, yi_value * _YI}
    for decimal_places in decimals:
        rounded = round(yi_value, decimal_places)
        candidates.add(rounded)
        candidates.add(rounded * _YI)
    return {float(item) for item in candidates if math.isfinite(float(item))}


def _metadata_mappings(run: dict | list) -> list[Mapping[str, Any]]:
    if not isinstance(run, dict):
        return []
    mappings: list[Mapping[str, Any]] = [run]
    for key in ("meta", "metadata"):
        value = run.get(key)
        if isinstance(value, Mapping):
            mappings.append(value)
    return mappings


def _metadata_values(run: dict | list) -> dict[str, set[float]]:
    metadata = {"date_parts": set(), "candidate_count": set(), "fx": set(),
                "roc_years": set()}
    for mapping in _metadata_mappings(run):
        for field, value in mapping.items():
            key = str(field).lower()
            if key in {"date", "run_date"}:
                if isinstance(value, str):
                    try:
                        parsed = date_cls.fromisoformat(value[:10])
                    except ValueError:
                        continue
                    metadata["date_parts"].update(
                        {float(parsed.year), float(parsed.month), float(parsed.day)})
                    metadata["roc_years"].add(float(parsed.year - 1911))
            elif key == "candidate_count":
                number = _as_float(value)
                if number is not None and number >= 0 and number.is_integer():
                    metadata["candidate_count"].add(number)
            elif key in {"fx", "fx_rate"}:
                number = _as_float(value)
                if number is not None and number > 0:
                    metadata["fx"].add(number)
    return metadata


def _source_health_counts(run: dict | list) -> set[float]:
    if not isinstance(run, dict):
        return set()
    lists: list[Any] = []
    if isinstance(run.get("source_health"), list):
        lists.append(run["source_health"])
    meta = run.get("meta")
    if isinstance(meta, Mapping) and isinstance(meta.get("source_health"), list):
        lists.append(meta["source_health"])
    counts: set[float] = set()
    for entries in lists:
        if not isinstance(entries, list):
            continue
        for entry in entries:
            if not isinstance(entry, Mapping):
                continue
            number = _as_float(entry.get("count"))
            if number is not None and number >= 0 and number.is_integer():
                counts.add(number)
    return counts


def _candidate_source_texts(run: dict | list) -> tuple[list[str], list[str]]:
    """Return visible catalyst text and raw MOPS explanations separately.

    Raw explanations commonly contain AP04 field numbers and dummy reporting
    dates.  They must not become a general-purpose numeric allowlist.
    """
    if not isinstance(run, dict):
        return [], []
    candidates = run.get("candidates")
    if not isinstance(candidates, list):
        return [], []
    catalysts: list[str] = []
    explanations: list[str] = []
    for candidate in candidates:
        if not isinstance(candidate, Mapping):
            continue
        catalyst = candidate.get("catalyst")
        if isinstance(catalyst, str) and catalyst:
            catalysts.append(catalyst)
        raw = candidate.get("raw")
        if isinstance(raw, Mapping):
            explanation = raw.get("mops_explanation")
            if isinstance(explanation, str) and explanation:
                explanations.append(explanation)
    return catalysts, explanations


def _sourced_catalyst_values(run: dict | list) -> dict[str, set[float]]:
    values: dict[str, set[float]] = {
        "number": set(), "percent": set(), "twd_yi": set(), "usd_yi": set(),
    }
    catalysts, explanations = _candidate_source_texts(run)
    roc_year_re = re.compile(r"(?<!\d)(1[01]\d)\s*(?:年|年度)")
    quarter_re = re.compile(r"第\s*(\d+)\s*季")
    yi_re = re.compile(
        r"(?<![A-Za-z0-9])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)\s*"
        r"(億美元|億美金|億元|億台幣|億)(?![A-Za-z0-9])", re.IGNORECASE)
    percent_re = re.compile(
        r"(?<![A-Za-z0-9])([+-]?\d+(?:\.\d+)?)\s*%(?![A-Za-z0-9])")

    # A filing amount is valid only when its monetary unit is explicit.  This
    # covers both "608,886,833 仟元" and forms such as
    # "營業收入(仟元):608,886,833" / "每股盈餘(元):14.17".
    filing_amount_re = re.compile(
        r"(?<![A-Za-z0-9])"
        r"(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)\s*"
        r"(仟元|元)(?![A-Za-z0-9])")
    unit_before_amount_re = re.compile(
        r"(?:[^\n:：]{0,40}[(（]\s*(仟元|元)\s*[)）]\s*[:：]?\s*"
        r"|(?:仟元|元)\s*[:：]\s*)"
        r"(?<![A-Za-z0-9])"
        r"(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)(?![A-Za-z0-9])")

    def add_number(amount: float) -> None:
        values["number"].update(_display_forms(amount, "number"))

    def add_text(text: str, *, allow_plain_visible: bool) -> None:
        for match in roc_year_re.finditer(text):
            add_number(float(match.group(1)))
        for match in quarter_re.finditer(text):
            add_number(float(match.group(1)))
        for match in yi_re.finditer(text):
            amount = _as_float(match.group(1).replace(",", ""))
            if amount is None:
                continue
            kind = "usd_yi" if match.group(2) in {"億美元", "億美金"} else "twd_yi"
            values[kind].update(_yi_candidates(amount * _YI))
        for match in percent_re.finditer(text):
            amount = _as_float(match.group(1))
            if amount is not None:
                values["percent"].update(_display_forms(amount, "percent"))
        for match in filing_amount_re.finditer(text):
            amount = _as_float(match.group(1).replace(",", ""))
            if amount is not None:
                add_number(amount)
        for match in unit_before_amount_re.finditer(text):
            amount = _as_float(match.group(2).replace(",", ""))
            if amount is not None:
                add_number(amount)

        # Only numbers visible in the catalyst itself may be admitted as
        # unrestricted bare values.  The same rule is deliberately not
        # applied to the full raw explanation.
        if allow_plain_visible:
            for match in re.finditer(
                    r"(?<![A-Za-z0-9])"
                    r"(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)"
                    r"(?![A-Za-z0-9])", text):
                amount = _as_float(match.group(1).replace(",", ""))
                if amount is not None:
                    add_number(amount)

    for catalyst in catalysts:
        add_text(catalyst, allow_plain_visible=True)
    for explanation in explanations:
        add_text(explanation, allow_plain_visible=False)
    return values


def _candidate_aggregate(run: dict | list) -> float | None:
    if not isinstance(run, dict):
        return None
    candidates = run.get("candidates")
    if not isinstance(candidates, list):
        return None
    total = 0.0
    found = False
    for candidate in candidates:
        if not isinstance(candidate, Mapping):
            continue
        value = _as_float(candidate.get("dollar_vol"))
        if value is not None:
            total += value
            found = True
    return total if found else None


def _collect_typed_values(run: dict | list) -> dict[str, set[float]]:
    values: dict[str, set[float]] = {
        "number": set(), "percent": set(), "multiple": set(),
        "usd_amount": set(), "twd_amount": set(), "twd_yi": set(), "usd_yi": set(),
    }
    metadata = _metadata_values(run)
    dollar_volumes: set[float] = set()
    for field, value in _walk(run):
        if field not in _ALLOWED_FIELDS:
            continue
        if isinstance(value, dict):
            nested_values = value.values()
        elif isinstance(value, (list, tuple, set)):
            nested_values = value
        else:
            nested_values = (value,)
        for nested in nested_values:
            number = _as_float(nested)
            if number is None:
                continue
            if field == "dollar_vol":
                dollar_volumes.add(number)
                values["twd_amount"].update(_currency_candidates(number))
                values["twd_yi"].update(_yi_candidates(number))
            elif field in {"usd_turnover", "turnover_usd"}:
                values["usd_amount"].update(_currency_candidates(number))
                values["usd_yi"].update(_yi_candidates(number))
            elif field == "chg_pct":
                values["percent"].update(_display_forms(number, "percent"))
            elif field == "rvol":
                values["multiple"].update(_display_forms(number, "multiple"))
            else:
                values["number"].update(_display_forms(number, "number"))
    for fx in metadata["fx"]:
        for dollar_volume in dollar_volumes:
            values["usd_amount"].update(_currency_candidates(dollar_volume / fx))
            values["usd_yi"].update(_yi_candidates(dollar_volume / fx))
    values["number"].update(metadata["date_parts"])
    values["number"].update(metadata["candidate_count"])
    values["number"].update(metadata["fx"])
    values["number"].update(metadata["roc_years"])
    values["number"].update(_source_health_counts(run))
    for kind, sourced_values in _sourced_catalyst_values(run).items():
        values[kind].update(sourced_values)
    aggregate = _candidate_aggregate(run)
    if aggregate is not None:
        values["twd_amount"].update(_currency_candidates(aggregate))
        values["twd_yi"].update(_yi_candidates(aggregate))
        for fx in metadata["fx"]:
            values["usd_amount"].update(_currency_candidates(aggregate / fx))
            values["usd_yi"].update(_yi_candidates(aggregate / fx))
    return values


def collect_allowed_numbers(run: dict | list) -> set[float]:
    result: set[float] = set()
    for values in _collect_typed_values(run).values():
        result.update(values)
    return result


def collect_ticker_codes(run: dict | list) -> set[float]:
    codes: set[float] = set()
    for field, value in _walk(run):
        if field not in _TICKER_FIELDS:
            continue
        nested_values = value.values() if isinstance(value, dict) else value
        if not isinstance(nested_values, (list, tuple, set)):
            nested_values = (nested_values,)
        for ticker in nested_values:
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


def _matches(number: dict[str, Any], allowed: dict[str, set[float]],
             ticker_codes: set[float] | None = None) -> bool:
    value = float(number["value"])
    kind = str(number["kind"])
    if kind == "number" and ticker_codes and any(
        math.isclose(value, code, rel_tol=1e-9, abs_tol=1e-9)
        for code in ticker_codes
    ):
        return True
    for candidate in allowed.get(kind, set()):
        if kind == "percent":
            if value > 0 and candidate <= 0:
                continue
            if value < 0 and candidate >= 0:
                continue
            if value == 0 and candidate != 0:
                continue
            if abs(value - candidate) > PERCENT_TOLERANCE:
                continue
        elif kind in {"usd_yi", "twd_yi"}:
            if not math.isclose(value, candidate, rel_tol=5e-4, abs_tol=100_000.0):
                continue
        elif not math.isclose(value, candidate, rel_tol=1e-9,
                              abs_tol=max(1e-9, abs(value) * 1e-9)):
            continue
        return True
    return False


def check_chat(run_json: dict | list, chat_md: str, *, fx_rate: float | None = None,
              date: str | None = None, candidate_count: int | None = None) -> dict[str, Any]:
    allowed = _collect_typed_values(run_json)
    if fx_rate is not None:
        fx = _as_float(fx_rate)
        if fx is not None and fx > 0:
            allowed["number"].update({fx, round(fx, 1), round(fx, 2), round(fx)})
            dollar_volumes = {
                value for field, value in _walk(run_json)
                if field == "dollar_vol"
                for value in ([value] if not isinstance(value, (list, tuple, set, dict))
                              else (value.values() if isinstance(value, dict) else value))
                if (parsed := _as_float(value)) is not None
            }
            aggregate = _candidate_aggregate(run_json)
            if aggregate is not None:
                dollar_volumes.add(aggregate)
            for dollar_volume in dollar_volumes:
                allowed["usd_amount"].update(_currency_candidates(dollar_volume / fx))
                allowed["usd_yi"].update(_yi_candidates(dollar_volume / fx))
    if date is not None:
        try:
            parsed = date_cls.fromisoformat(str(date)[:10])
        except ValueError:
            pass
        else:
            allowed["number"].update({float(parsed.year), float(parsed.month),
                                      float(parsed.day), float(parsed.year - 1911)})
    if candidate_count is not None:
        count = _as_float(candidate_count)
        if count is not None and count >= 0 and count.is_integer():
            allowed["number"].add(count)
    ticker_codes = collect_ticker_codes(run_json)
    offenders: list[dict[str, Any]] = []
    for number in extract_numbers(chat_md):
        if _matches(number, allowed, ticker_codes):
            continue
        kind = str(number["kind"])
        reason = {
            "percent": "percentage is not represented by the run",
            "multiple": "multiple is not represented by the run",
            "usd_amount": "USD amount is not represented by the run",
            "twd_amount": "TWD amount is not represented by the run",
            "twd_yi": "TWD yi amount is not represented by the run",
            "usd_yi": "USD yi amount is not represented by the run",
        }.get(kind, "number is not represented by the run")
        offenders.append({"raw": number["raw"],
                          "context": _context_for(chat_md, number["span"]),
                          "reason": reason})
    return {"ok": not offenders, "offenders": offenders}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check SIP chat numbers against a run")
    parser.add_argument("--run", required=True)
    parser.add_argument("--chat", required=True)
    parser.add_argument("--fx", type=float, default=None)
    parser.add_argument("--date")
    parser.add_argument("--candidate-count", type=int)
    args = parser.parse_args(argv)
    try:
        run = json.loads(Path(args.run).read_text(encoding="utf-8"))
        chat = Path(args.chat).read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as exc:
        print(f"number_trace: {exc}", file=sys.stderr)
        return 2
    result = check_chat(run, chat, fx_rate=args.fx, date=args.date,
                        candidate_count=args.candidate_count)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 5


if __name__ == "__main__":
    raise SystemExit(main())
