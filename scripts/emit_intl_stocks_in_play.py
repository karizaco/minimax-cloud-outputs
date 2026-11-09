#!/usr/bin/env python3
"""Publish Fundamental regional stocks-in-play digests.

Inputs are a Grok Bot box digest, a market name, date, slot, and optionally the
repository watchlist. Outputs are dated digest, candidate JSON/CSV, family
history, index, and manifest files. This script never fetches anything from the
network.
"""

import argparse
import csv
import io
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


MARKETS = ("asx", "europe", "tokyo", "taiwan")
SLOTS = ("open", "midday", "preclose", "close")
SCHEMA = "intl-stocks-in-play-v1"
GENERATED_AT_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+07:00$")
CSV_COLUMNS = (
    "rank", "tier", "ticker", "tv_symbol", "company", "venue", "segment",
    "price_raw", "chg_pct", "gap_pct", "rvol", "turnover_raw", "mcap_raw",
    "catalyst", "flags", "on_watchlist", "parse", "section",
)
TIER_ORDER = {"A": 0, "SOFT_A": 1, "TECH_WATCH": 2, "B": 3, "C": 4}
SKIP_HEADINGS = (
    "near-miss", "annex", "overnight", "skipped", "source health", "fx",
    "market index", "other ps", "poland", "what changed", "recheck", "excluded",
)
PATH_TOKEN_RE = re.compile(
    r"`([^`\n]*\.(?:md|csv|json|jsonl|yaml|py|txt|log))`",
    re.IGNORECASE,
)


def fail(message):
    raise ValueError(message)


def generated_now():
    return datetime.now(timezone(timedelta(hours=7))).replace(microsecond=0).isoformat()


def json_bytes(value):
    return json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def csv_bytes(rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=CSV_COLUMNS, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({key: "" if row.get(key) is None else row.get(key) for key in CSV_COLUMNS})
    return stream.getvalue().encode("utf-8")


def section_tier(heading):
    lowered = heading.casefold()
    if any(term in lowered for term in SKIP_HEADINGS):
        return None
    if "tier a" in lowered:
        return "A"
    if "soft-a" in lowered or "soft_a" in lowered:
        return "SOFT_A"
    if "tech_watch" in lowered or "tech-watch" in lowered:
        return "TECH_WATCH"
    if "tier b / c" in lowered or "tier b/c" in lowered:
        return "MIXED"
    if "tier b" in lowered:
        return "B"
    if "tier c" in lowered:
        return "C"
    return None


def split_table_row(line):
    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]
    return [cell.strip() for cell in text.split("|")]


def is_separator_row(cells):
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def normalize_header(cell):
    value = cell.strip().casefold()
    if value.startswith("catalyst"):
        return "catalyst"
    if value.startswith("turnover") or value == "€vt":
        return "turnover_raw"
    if value.startswith("price") or value == "last":
        return "price_raw"
    if value in ("chg", "chg%", "move"):
        return "chg_raw"
    if value in ("gap", "gap%"):
        return "gap_raw"
    if value in ("rvol", "relvol"):
        return "rvol_raw"
    if value in ("why", "note"):
        return "catalyst"
    if value in ("ticker", "code", "symbol"):
        return "ticker"
    if value == "company":
        return "company"
    if value == "venue":
        return "venue"
    if value == "seg":
        return "segment"
    if value == "mcap":
        return "mcap_raw"
    return None


def is_header_row(cells):
    mapped = [normalize_header(cell) for cell in cells]
    return "ticker" in mapped and any(value is not None for value in mapped)


def signed_number(sign, digits):
    number = float(digits.replace(",", "."))
    return -number if sign in ("-", "−") else number


def first_number(text):
    match = re.search(r"([+\-−]?)\s*(\d+(?:[,.]\d+)?)", text or "")
    if not match:
        return None
    try:
        return signed_number(match.group(1), match.group(2))
    except ValueError:
        return None


def parse_plain_number(text):
    if not text:
        return None
    value = text.replace("**", "")
    match = re.search(r"([+\-−]?)\s*(\d+(?:[,.]\d+)?)", value)
    if not match:
        return None
    try:
        return signed_number(match.group(1), match.group(2))
    except ValueError:
        return None


def parse_chg(text):
    if not text:
        return None
    match = re.search(r"([+\-−]?)\s*(\d+(?:[,.]\d+)?)\s*%", text.replace("**", ""))
    if not match:
        return None
    try:
        return signed_number(match.group(1), match.group(2))
    except ValueError:
        return None


def parse_list_chg(text):
    if not text:
        return None
    match = re.search(r"([+\-−])\s*(\d+(?:[,.]\d+)?)\s*%", text.replace("**", ""))
    if not match:
        return None
    try:
        return signed_number(match.group(1), match.group(2))
    except ValueError:
        return None


def parse_gap(text, chg_text):
    if text:
        match = re.search(r"([+\-−]?)\s*(\d+(?:[,.]\d+)?)\s*%", text.replace("**", ""))
        if match:
            try:
                return signed_number(match.group(1), match.group(2))
            except ValueError:
                return None
    if chg_text:
        match = re.search(
            r"\(gap\s*([+\-−]?)\s*(\d+(?:[,.]\d+)?)\s*%\)",
            chg_text.replace("**", ""),
            re.IGNORECASE,
        )
        if match:
            try:
                return signed_number(match.group(1), match.group(2))
            except ValueError:
                return None
    return None


def parse_rvol(text):
    if not text:
        return None
    match = re.search(r"([+\-−]?)\s*(\d+(?:[,.]\d+)?)\s*[×x]", text.replace("**", ""), re.IGNORECASE)
    if not match:
        return None
    try:
        return signed_number(match.group(1), match.group(2))
    except ValueError:
        return None


def ticker_pattern(market):
    if market == "asx":
        return re.compile(r"^[A-Z][A-Z0-9]{1,4}$")
    if market == "tokyo":
        return re.compile(r"^\d{3}[0-9A-Z]$")
    if market == "taiwan":
        return re.compile(r"^\d{4,6}[A-Z]?(?:\.TPEX)?$")
    return re.compile(r"^[A-Z0-9][A-Z0-9.\-]{1,9}$")


def valid_ticker(market, ticker):
    return bool(ticker and ticker_pattern(market).fullmatch(ticker.strip("*")))


def venue_symbol(venue):
    value = (venue or "").casefold()
    mapping = (
        (("borsa italiana",), "MIL"),
        (("xetra",), "XETR"),
        (("lse (aim)", "lse"), "LSE"),
        (("euronext paris", "euronext amsterdam", "euronext brussels",
          "euronext lisbon", "euronext dublin"), "EURONEXT"),
        (("six",), "SIX"),
        (("oslo",), "OSL"),
        (("helsinki",), "OMXHEX"),
        (("stockholm", "nasdaq stockholm"), "OMXSTO"),
        (("copenhagen",), "OMXCOP"),
        (("warsaw", "gpw"), "GPW"),
        (("madrid", "bme"), "BME"),
        (("vienna",), "VIE"),
    )
    for names, symbol in mapping:
        if any(name in value for name in names):
            return symbol
    return None


def tv_symbol_for(market, ticker, venue):
    if market == "asx":
        return "ASX:" + ticker
    if market == "tokyo":
        return "TSE:" + ticker
    if market == "taiwan":
        return ("TPEX:" if ticker.endswith(".TPEX") else "TWSE:") + ticker.replace(".TPEX", "")
    prefix = venue_symbol(venue)
    return prefix + ":" + ticker if prefix else None


def extract_first_ticker(market, text):
    value = (text or "").strip()
    value = re.sub(r"^\*\*", "", value)
    value = re.sub(r"\*\*", "", value)
    value = re.sub(r"^(?:B|C):\s*", "", value)
    token = value.split(None, 1)[0].rstrip(":") if value.split() else ""
    token = token.strip("*")
    if not valid_ticker(market, token):
        return None
    return token


def clean_limit_text(market, text):
    value = text or ""
    flags = []
    if market == "taiwan":
        if re.search(r"\bLIMIT_UP\b", value, re.IGNORECASE):
            flags.append("LIMIT_UP")
            value = re.sub(r"\bLIMIT_UP\b", "", value, flags=re.IGNORECASE)
        if re.search(r"\bLIMIT_DOWN\b", value, re.IGNORECASE):
            flags.append("LIMIT_DOWN")
            value = re.sub(r"\bLIMIT_DOWN\b", "", value, flags=re.IGNORECASE)
    elif market == "tokyo":
        if re.search(r"\bSTOP[\s_-]*HIGH\b", value, re.IGNORECASE):
            flags.append("LIMIT_UP")
            value = re.sub(r"\bSTOP[\s_-]*HIGH\b", "", value, flags=re.IGNORECASE)
    return re.sub(r"\s{2,}", " ", value).strip(), flags


def parse_watchlist(path):
    if not path.exists():
        fail("watchlist not found: " + str(path))
    symbols = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        fail("cannot read watchlist: " + str(exc))
    for line in lines:
        match = re.match(r'^\s*(?:-\s*)?tv_symbol\s*:\s*"([^"]*)"\s*$', line)
        if match:
            symbols.append(match.group(1))
    return set(symbols)


def split_tickers(value):
    return [part.strip() for part in value.split(",") if part.strip()]


def table_candidate(market, heading, cells, tier):
    mapped = {}
    original = {}
    column_keys = {}
    for header, value in zip(cells[0], cells[1]):
        key = normalize_header(header)
        original[header.strip()] = value.strip()
        if key:
            mapped[key] = value.strip()
            column_keys[key] = header.strip()
    ticker_values = split_tickers(mapped.get("ticker", ""))
    if not ticker_values:
        return [], False
    venue = mapped.get("venue")
    company, flags = clean_limit_text(market, mapped.get("company"))

    chg_text = mapped.get("chg_raw")
    chg_pct = parse_chg(chg_text)
    if chg_pct is None and "chg_raw" in column_keys:
        chg_pct = parse_plain_number(chg_text)

    gap_text = mapped.get("gap_raw")
    gap_pct = parse_gap(gap_text, chg_text)
    if gap_pct is None and "gap_raw" in column_keys:
        gap_pct = parse_plain_number(gap_text)

    rvol_text = mapped.get("rvol_raw")
    rvol = parse_rvol(rvol_text)
    if rvol is None and "rvol_raw" in column_keys:
        rvol = parse_plain_number(rvol_text)

    results = []
    for ticker in ticker_values:
        ticker = ticker.strip("*")
        if not valid_ticker(market, ticker):
            continue
        results.append({
            "tier": tier,
            "ticker": ticker,
            "tv_symbol": tv_symbol_for(market, ticker, venue),
            "company": company,
            "venue": venue,
            "segment": mapped.get("segment"),
            "price_raw": mapped.get("price_raw"),
            "chg_pct": chg_pct,
            "gap_pct": gap_pct,
            "rvol": rvol,
            "turnover_raw": mapped.get("turnover_raw"),
            "mcap_raw": mapped.get("mcap_raw"),
            "catalyst": mapped.get("catalyst"),
            "flags": list(flags),
            "parse": "table",
            "section": heading,
            "raw": None,
            "cells": original,
        })
    return results, bool(results)


def list_candidate(market, heading, item, tier):
    cleaned, flags = clean_limit_text(market, item.strip())
    company = None
    venue = None
    if market == "europe":
        first_paren = re.search(r"\(([^()]*)\)", cleaned)
        if first_paren:
            venue = first_paren.group(1).strip()
        bold = re.match(r"^\*\*([^*]+)\*\*", cleaned)
        if bold:
            ticker = bold.group(1).strip().rstrip(":")
        else:
            ticker = extract_first_ticker(market, cleaned)
    else:
        ticker = extract_first_ticker(market, cleaned)
    if not valid_ticker(market, ticker):
        return None, False
    return {
        "tier": tier,
        "ticker": ticker,
        "tv_symbol": tv_symbol_for(market, ticker, venue),
        "company": company,
        "venue": venue,
        "segment": None,
        "price_raw": None,
        "chg_pct": parse_list_chg(cleaned),
        "gap_pct": parse_gap(None, cleaned),
        "rvol": parse_rvol(cleaned),
        "turnover_raw": None,
        "mcap_raw": None,
        "catalyst": None,
        "flags": flags,
        "parse": "list",
        "section": heading,
        "raw": item.strip(),
        "cells": {},
    }, True


def parse_digest(market, text):
    lines = text.splitlines()
    candidates = []
    unparsed = 0
    index = 0
    while index < len(lines):
        match = re.match(r"^##\s+(.+?)\s*$", lines[index])
        if not match:
            index += 1
            continue
        heading = match.group(1).strip()
        tier = section_tier(heading)
        index += 1
        while index < len(lines) and not lines[index].startswith("## "):
            line = lines[index].strip()
            if tier and line.startswith("|"):
                cells = split_table_row(line)
                if is_header_row(cells):
                    index += 1
                    while index < len(lines):
                        row_line = lines[index].strip()
                        if not row_line.startswith("|"):
                            break
                        row = split_table_row(row_line)
                        if is_separator_row(row):
                            index += 1
                            continue
                        if is_header_row(row):
                            index += 1
                            continue
                        if len(row) < len(cells):
                            row += [""] * (len(cells) - len(row))
                        parsed_candidates, parsed = table_candidate(
                            market, heading, [cells, row[:len(cells)]], tier
                        )
                        if parsed:
                            candidates.extend(parsed_candidates)
                        else:
                            unparsed += 1
                        index += 1
                    continue
                index += 1
                continue
            if tier and line.startswith("- "):
                item = line[2:].strip()
                item_tier = tier
                if tier == "MIXED":
                    prefix = re.match(r"^([BC]):\s*(.*)$", item)
                    if not prefix:
                        index += 1
                        continue
                    item_tier = prefix.group(1)
                    item = prefix.group(2)
                if market == "tokyo" and tier == "MIXED":
                    parts = [part.strip() for part in item.split("; ") if part.strip()]
                else:
                    parts = [item]
                for part in parts:
                    candidate, parsed = list_candidate(market, heading, part, item_tier)
                    if parsed:
                        candidates.append(candidate)
                    else:
                        unparsed += 1
                index += 1
                continue
            if tier and line and " | " in line:
                for item in line.split(" | "):
                    item = item.strip()
                    if not item:
                        continue
                    candidate, parsed = list_candidate(market, heading, item, tier)
                    if parsed:
                        candidates.append(candidate)
                    else:
                        unparsed += 1
                index += 1
                continue
            index += 1
    return candidates, unparsed


def resolve_tv_symbol_fallbacks(market, date, slot, candidates, repo_root):
    symbol_by_ticker = {}
    for candidate in candidates:
        ticker = candidate.get("ticker")
        symbol = candidate.get("tv_symbol")
        if ticker and symbol and ticker not in symbol_by_ticker:
            symbol_by_ticker[ticker] = symbol

    dated_dir = repo_root / (market + "-stocks-in-play") / date
    for other_slot in SLOTS:
        if other_slot == slot:
            continue
        path = dated_dir / (other_slot + "-candidates.json")
        if not path.is_file():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for candidate in data.get("candidates", []):
            ticker = candidate.get("ticker")
            symbol = candidate.get("tv_symbol")
            if ticker and symbol and ticker not in symbol_by_ticker:
                symbol_by_ticker[ticker] = symbol

    for candidate in candidates:
        if not candidate.get("tv_symbol"):
            symbol = symbol_by_ticker.get(candidate.get("ticker"))
            if symbol:
                candidate["tv_symbol"] = symbol


def strip_markdown(text):
    text = re.sub(r"[*_`]", "", text or "")
    return re.sub(r"\s+", " ", text).strip()


def skipped_section_note(text):
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("## ") and "skipped" in line.casefold():
            content = []
            for following in lines[index + 1:]:
                if following.startswith("## "):
                    break
                if following.strip():
                    content.append(following.strip())
            joined = strip_markdown(" ".join(content))
            if joined.casefold().startswith("none"):
                return None
            if joined:
                return joined[:200]
            return "Skipped section is empty."
    return None


def rank_candidates(candidates):
    ordered = sorted(
        enumerate(candidates),
        key=lambda pair: (TIER_ORDER.get(pair[1]["tier"], 99), pair[0]),
    )
    result = []
    for rank, (_, candidate) in enumerate(ordered, 1):
        row = dict(candidate)
        row["rank"] = rank
        result.append(row)
    return result


def path_exists_in_repo(repo_root, token):
    token = token.strip()
    if not token:
        return False
    candidate = Path(token)
    if candidate.is_absolute():
        try:
            candidate.relative_to(repo_root.resolve())
        except ValueError:
            return False
    return candidate.exists()


def sanitize_markdown(text, repo_root):
    count = 0

    def replace(match):
        nonlocal count
        token = match.group(1)
        if path_exists_in_repo(repo_root, token):
            return match.group(0)
        count += 1
        return token

    return PATH_TOKEN_RE.sub(replace, text), count


def candidate_rows(candidates):
    rows = []
    for candidate in candidates:
        row = {key: candidate.get(key) for key in CSV_COLUMNS if key != "flags"}
        row["flags"] = ";".join(candidate.get("flags") or [])
        row["on_watchlist"] = (
            "" if candidate.get("on_watchlist") is None
            else str(candidate["on_watchlist"]).lower()
        )
        rows.append(row)
    return rows


def source_title(text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def front_matter(date, market, slot, generated_at, status, source):
    return (
        "---\n"
        f"date: {date}\n"
        f"market: {market}\n"
        f"slot: {slot}\n"
        f"producer: grok-bot/{market}-stocks-in-play\n"
        f"contract: {SCHEMA}\n"
        f"source: {source}\n"
        f"generated_at: {generated_at}\n"
        f"status: {status}\n"
        "---\n\n"
    )


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        fail("cannot read JSON " + str(path) + ": " + str(exc))


def write_text(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="")


def write_bytes(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def load_history(path):
    if not path.exists():
        return []
    rows = []
    try:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except ValueError as exc:
                fail("garbled history line " + str(number) + " in " + str(path) + ": " + str(exc))
    except OSError as exc:
        fail("cannot read history: " + str(exc))
    return rows


def slot_sort(slot):
    return SLOTS.index(slot)


def build_index(family_root):
    runs = []
    if not family_root.exists():
        return {"_schema": "intl-stocks-in-play-index-v1", "updated": "", "runs": []}
    for directory in family_root.iterdir():
        if not directory.is_dir() or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", directory.name):
            continue
        slots = []
        for slot in SLOTS:
            path = directory / (slot + "-candidates.json")
            if path.exists():
                data = read_json(path)
                slots.append({
                    "slot": slot,
                    "status": data.get("status"),
                    "counts": data.get("counts", {}),
                })
        if slots:
            newest_slot = slots[-1]["slot"]
            runs.append({
                "date": directory.name,
                "path": directory.name + "/",
                "run_id": directory.name + "T" + newest_slot,
                "slots": slots,
            })
    runs.sort(key=lambda run: run["date"])
    return {
        "_schema": "intl-stocks-in-play-index-v1",
        "updated": runs[-1]["date"] if runs else "",
        "runs": runs,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--market", required=True, choices=MARKETS)
    parser.add_argument("--date", required=True)
    parser.add_argument("--slot", required=True, choices=SLOTS)
    parser.add_argument("--digest-md", required=True)
    parser.add_argument("--watchlist", default="refs/watchlist.yaml")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--generated-at")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        fail("invalid date: " + args.date)

    repo_root = Path(args.repo_root).resolve()
    family_root = repo_root / (args.market + "-stocks-in-play")
    dated_dir = family_root / args.date
    existing_machine_path = dated_dir / (args.slot + "-candidates.json")

    if args.generated_at:
        generated_at = args.generated_at
    elif existing_machine_path.is_file():
        existing_machine = read_json(existing_machine_path)
        generated_at = existing_machine.get("generated_at", "")
        if not generated_at:
            fail("existing run has no generated_at: " + str(existing_machine_path))
    else:
        generated_at = generated_now()
    if not GENERATED_AT_RE.fullmatch(generated_at):
        fail("generated-at must be ISO8601 with +07:00, for example 2026-11-09T14:00:00+07:00")

    digest_path = Path(args.digest_md).expanduser().resolve()
    watchlist_path = Path(args.watchlist)
    if not watchlist_path.is_absolute():
        watchlist_path = repo_root / watchlist_path
    if not digest_path.is_file():
        fail("digest not found: " + str(digest_path))
    try:
        digest = digest_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        fail("cannot read digest: " + str(exc))
    if not digest.strip():
        fail("digest is empty: " + str(digest_path))

    watch_symbols = parse_watchlist(watchlist_path)
    watchlist_missing_keys = not watch_symbols
    candidates, unparsed = parse_digest(args.market, digest)
    resolve_tv_symbol_fallbacks(
        args.market, args.date, args.slot, candidates, repo_root
    )
    for candidate in candidates:
        if watchlist_missing_keys:
            candidate["on_watchlist"] = None
        else:
            candidate["on_watchlist"] = candidate["tv_symbol"] in watch_symbols
    candidates = rank_candidates(candidates)

    skipped_note = skipped_section_note(digest)
    degraded_reasons = []
    if not candidates:
        degraded_reasons.append("no candidates parsed")
    if skipped_note:
        degraded_reasons.append(skipped_note)
    status = "degraded" if degraded_reasons else "ok"
    by_tier = {tier: sum(candidate["tier"] == tier for candidate in candidates)
               for tier in ("A", "SOFT_A", "TECH_WATCH", "B", "C")}
    on_watchlist = sum(candidate["on_watchlist"] is True for candidate in candidates)
    counts = {
        "candidates": len(candidates),
        "by_tier": by_tier,
        "on_watchlist": on_watchlist,
        "unparsed_items": unparsed,
    }
    source = "Grok Bot box digest (Fundamental " + args.market + " stocks-in-play routine)"
    safe_digest, path_count = sanitize_markdown(digest, repo_root)
    deviations = []
    if not candidates:
        deviations.append("no candidates parsed")
    if skipped_note:
        deviations.append("digest reports a skipped section")
    if watchlist_missing_keys:
        deviations.append("watchlist has no tv_symbol keys; on_watchlist is null")
    if path_count:
        deviations.append(str(path_count) + " box-local path references un-backticked")
    deviation_line = "**Deviations:** " + ("; ".join(deviations) if deviations else "none")

    brief = (
        front_matter(args.date, args.market, args.slot, generated_at, status, source)
        + "Provenance: Fundamental digest at " + str(digest_path)
        + "; built at " + generated_at + "; covered session " + args.slot + ".\n\n"
        + deviation_line + "\n\n"
        + safe_digest.rstrip() + "\n"
    )
    machine = {
        "_schema": SCHEMA,
        "market": args.market,
        "date": args.date,
        "slot": args.slot,
        "timezone": "Asia/Bangkok",
        "producer": "grok-bot/" + args.market + "-stocks-in-play",
        "run_id": args.date + "T" + args.slot,
        "status": status,
        "degraded_reasons": degraded_reasons,
        "source_digest": str(digest_path),
        "digest_title": source_title(digest),
        "counts": counts,
        "candidates": candidates,
    }
    files = {
        args.slot + ".md": brief.encode("utf-8"),
        args.slot + "-candidates.json": json_bytes(machine).encode("utf-8"),
        args.slot + "-candidates.csv": csv_bytes(candidate_rows(candidates)),
    }
    existing = []
    if dated_dir.exists():
        if not dated_dir.is_dir():
            fail("dated output path is not a directory: " + str(dated_dir))
        for path in sorted(dated_dir.iterdir()):
            if path.is_file() and path.name != "_manifest.json":
                existing.append((path.name, path.read_bytes()))
    all_dated_files = dict(existing)
    all_dated_files.update(files)

    prior_notes_by_slot = {slot: [] for slot in SLOTS}
    prior_manifest_path = dated_dir / "_manifest.json"
    if prior_manifest_path.is_file():
        prior_manifest = read_json(prior_manifest_path)
        for note in prior_manifest.get("notes", []):
            for slot in SLOTS:
                prefix = slot + ": "
                if note.startswith(prefix):
                    prior_notes_by_slot[slot].append(note[len(prefix):])
                    break

    current_notes = list(deviations)
    if skipped_note:
        current_notes.append(skipped_note)
    if path_count:
        current_notes.append(str(path_count) + " box-local path references un-backticked")

    manifest_notes = []
    for slot in SLOTS:
        notes = current_notes if slot == args.slot else prior_notes_by_slot[slot]
        for note in notes:
            prefixed = slot + ": " + note
            if prefixed not in manifest_notes:
                manifest_notes.append(prefixed)

    manifest = {
        "_schema": "intl-stocks-in-play-manifest-v1",
        "date": args.date,
        "producer": "grok-bot/" + args.market + "-stocks-in-play",
        "run_id": args.date + "T" + args.slot,
        "generated_at": generated_at,
        "provenance": "Fundamental " + args.market + " box digest built at "
                      + generated_at + " covering the " + args.slot + " session.",
        "canonical": {
            "brief": [name for name in sorted(all_dated_files) if name.endswith(".md")],
            "machine": [
                name for name in sorted(all_dated_files)
                if name.endswith(".json") or name.endswith(".csv")
            ],
        },
        "files": [
            {"name": name, "role": "brief" if name.endswith(".md") else "machine"}
            for name in sorted(all_dated_files)
        ] + [{"name": "_manifest.json", "role": "provenance"}],
        "counts": {
            slot: machine["counts"] if slot == args.slot else read_json(
                dated_dir / (slot + "-candidates.json")
            )["counts"]
            for slot in SLOTS if (slot + "-candidates.json") in all_dated_files
        },
        "notes": manifest_notes,
    }
    all_dated_files["_manifest.json"] = json_bytes(manifest).encode("utf-8")

    history = load_history(family_root / "history.jsonl")
    history = [row for row in history if not (
        row.get("date") == args.date and row.get("slot") == args.slot
    )]
    for candidate in candidates:
        history.append({
            "date": args.date,
            "slot": args.slot,
            "tier": candidate["tier"],
            "ticker": candidate["ticker"],
            "tv_symbol": candidate["tv_symbol"],
            "chg_pct": candidate["chg_pct"],
        })
    history.sort(key=lambda row: (
        row.get("date", ""), slot_sort(row.get("slot", "")), TIER_ORDER.get(row.get("tier"), 99),
        row.get("ticker", ""),
    ))
    history_text = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in history
    )

    index = build_index(family_root)
    if not any(run["date"] == args.date for run in index["runs"]):
        index["runs"].append({
            "date": args.date,
            "path": args.date + "/",
            "run_id": args.date + "T" + args.slot,
            "slots": [],
        })
        index["runs"].sort(key=lambda run: run["date"])
    run = next(run for run in index["runs"] if run["date"] == args.date)
    run["slots"] = [slot for slot in run["slots"] if slot["slot"] != args.slot]
    run["slots"].append({"slot": args.slot, "status": status, "counts": counts})
    run["slots"].sort(key=lambda slot: slot_sort(slot["slot"]))
    run["path"] = args.date + "/"
    run["run_id"] = args.date + "T" + run["slots"][-1]["slot"]
    index["updated"] = max(
        [run["date"] for run in index["runs"]] + [args.date]
    )

    indexed_runs = []
    for indexed_run in index["runs"]:
        for indexed_slot in indexed_run["slots"]:
            indexed_runs.append((
                indexed_run["date"],
                slot_sort(indexed_slot["slot"]),
                indexed_run["date"],
                indexed_slot["slot"],
            ))
    newest = max(indexed_runs, key=lambda item: (item[0], item[1]))
    current_key = (args.date, slot_sort(args.slot))
    latest_files = {}
    if (newest[0], newest[1]) == current_key:
        latest_files = {
            "latest.json": files[args.slot + "-candidates.json"],
            "latest.md": files[args.slot + ".md"],
            "latest.csv": files[args.slot + "-candidates.csv"],
        }
    else:
        newest_dir = family_root / newest[2]
        latest_files = {
            "latest.json": (newest_dir / (newest[3] + "-candidates.json")).read_bytes(),
            "latest.md": (newest_dir / (newest[3] + ".md")).read_bytes(),
            "latest.csv": (newest_dir / (newest[3] + "-candidates.csv")).read_bytes(),
        }

    planned = [
        str(dated_dir / name) for name in sorted(all_dated_files)
    ] + [
        str(family_root / "history.jsonl"),
        str(family_root / "_index.json"),
    ] + [str(family_root / name) for name in sorted(latest_files)]
    if args.dry_run:
        print("planned files:")
        for path in planned:
            print(path)
        print("counts: " + json.dumps(counts, sort_keys=True))
        return 0

    family_root.mkdir(parents=True, exist_ok=True)
    dated_dir.mkdir(parents=True, exist_ok=True)
    for name, content in sorted(all_dated_files.items()):
        write_bytes(dated_dir / name, content)
    write_text(family_root / "history.jsonl", history_text)
    write_text(family_root / "_index.json", json_bytes(index))
    for name, content in latest_files.items():
        write_bytes(family_root / name, content)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as exc:
        print("emit_intl_stocks_in_play.py: " + str(exc), file=sys.stderr)
        sys.exit(2)
