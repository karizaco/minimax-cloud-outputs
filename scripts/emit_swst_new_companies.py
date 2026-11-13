#!/usr/bin/env python3
"""Publish a Grok Bot Simply Wall St weekly archive as SWST artifacts."""

import argparse
import csv
import json
import re
import shutil
import sys
from pathlib import Path


SCHEMA = "swst-new-companies-v1"
PRODUCER = "grok-bot/simply-wall-st-new-companies"
TIMEZONE = "Asia/Bangkok"
REGION_IDS = {
    "US": "S-20%earnings-sub10B-over$1-US",
    "EU": "S-20%earnings-sub10B-over$1-EU",
    "JP/TW": "S-20%earnings-sub10B-over$1-JP/TW",
}
DEFAULT_NOTES = [
    "SWS badge counts 123 (US64/EU16/JP·TW43) vs 121 distinct rows collected",
    "SWS card-expiry popup appeared; billing not touched",
]
EXPECTED_REPEATS = {
    "BJRI", "KN", "MEI", "SIMO", "VIR", "LZM", "VSAT", "6239", "5234", "7744"
}
EXPECTED_WATCHLIST = {"VIAV", "AF"}


def die(message):
    raise ValueError(message)


def read_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def copy_bytes(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.resolve() != destination.resolve():
        shutil.copyfile(source, destination)


def normalized_key(value):
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def get_value(row, *names):
    normalized = {normalized_key(key): value for key, value in row.items() if key is not None}
    for name in names:
        value = normalized.get(normalized_key(name))
        if value is not None and str(value).strip() != "":
            return str(value).strip()
    return None


def bare_ticker(symbol):
    value = (symbol or "").strip()
    return value.rsplit(":", 1)[-1].strip()


def ticker_pattern(ticker):
    escaped = re.escape(ticker)
    return re.compile(r"(?<![A-Za-z0-9])" + escaped + r"(?![A-Za-z0-9])", re.IGNORECASE)


def parse_archive(archive_text):
    screeners = []
    heading_re = re.compile(
        r"^##\s+(\S+)\s+.*?\b(\d+)\s+new\s*\(\s*(\d+)\s+found\s*\)\s*$",
        re.IGNORECASE | re.MULTILINE,
    )
    for match in heading_re.finditer(archive_text):
        screener_id, new_count, found_count = match.groups()
        region = region_for_screener(screener_id)
        if region is None:
            die(f"Cannot infer region for screener {screener_id!r}")
        screeners.append({
            "id": screener_id,
            "region": region,
            "found": int(found_count),
            "new": int(new_count),
            "url": None,
        })

    if not screeners:
        die("No screener headers with new/found counts were found in the archive")

    totals_match = re.search(
        r"Totals:\s*(\d+)\s+found,\s*(\d+)\s+new\b.*?"
        r"Repeats skipped:\s*(\d+)\s*\(([^)]*)\)",
        archive_text,
        re.IGNORECASE | re.DOTALL,
    )
    if not totals_match:
        die("Could not parse the archive totals and repeats-skipped line")
    found, new, repeat_count, repeat_text = totals_match.groups()
    repeats = parse_symbol_list(repeat_text)
    if len(repeats) != int(repeat_count):
        die("Repeats-skipped count does not match the listed tickers")
    if set(repeats) != EXPECTED_REPEATS:
        die(f"Archive repeats {repeats!r} do not match the required 2026-11-09 facts")

    watch_match = re.search(
        r"Watchlist matches:\s*([^.\n]*)",
        archive_text,
        re.IGNORECASE,
    )
    watchlist = parse_symbol_list(watch_match.group(1)) if watch_match else []
    if set(watchlist) != EXPECTED_WATCHLIST:
        die(f"Archive watchlist {watchlist!r} does not match the required 2026-11-09 facts")

    section_occurrences = {}
    section_by_line = {}
    current = None
    for line_number, line in enumerate(archive_text.splitlines(), 1):
        heading = re.match(r"^##\s+(\S+)", line)
        if heading:
            current = heading.group(1)
        section_by_line[line_number] = current

    archive_lines = archive_text.splitlines()
    all_candidates = set(repeats) | set(watchlist)
    for line_number, line in enumerate(archive_lines, 1):
        section = section_by_line.get(line_number)
        region = region_for_screener(section) if section else None
        for ticker in all_candidates:
            if ticker_pattern(ticker).search(line):
                if region:
                    section_occurrences.setdefault(ticker, []).append(region)

    return {
        "screeners": screeners,
        "found": int(found),
        "new": int(new),
        "repeats": repeats,
        "watchlist": watchlist,
        "section_occurrences": section_occurrences,
    }


def parse_symbol_list(text):
    if not text.strip():
        return []
    return [
        token.strip()
        for token in re.split(r"[,;]", text)
        if token.strip()
    ]


def region_for_screener(screener_id):
    for region, canonical_id in REGION_IDS.items():
        if screener_id == canonical_id or screener_id.endswith("-" + region):
            return region
    return None


def parse_history(history_path):
    rows = []
    if not history_path.exists():
        die(f"History file does not exist: {history_path}")
    with history_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                die(f"Invalid JSON in history on line {line_number}: {exc}")
            rows.append(row)
    return rows


def history_ticker(row):
    for key in ("ticker", "tv_symbol", "symbol"):
        value = row.get(key)
        if isinstance(value, str) and value.strip():
            return bare_ticker(value)
    company = row.get("company")
    if isinstance(company, dict):
        for key in ("ticker", "tv_symbol", "symbol"):
            value = company.get(key)
            if isinstance(value, str) and value.strip():
                return bare_ticker(value)
    return None


def history_region(row):
    screener = row.get("screener")
    if isinstance(screener, dict):
        screener = screener.get("id")
    region = row.get("region")
    if isinstance(region, str) and region in REGION_IDS:
        return region
    if isinstance(screener, str):
        inferred = region_for_screener(screener)
        if inferred:
            return inferred
    company = row.get("company")
    if isinstance(company, dict):
        return history_region(company)
    return None


def history_url(row):
    url = row.get("url") or row.get("screener_url")
    if isinstance(url, str) and url.strip():
        return url.strip()
    company = row.get("company")
    if isinstance(company, dict):
        return history_url(company)
    return None


def history_date(row):
    for key in ("found_at", "date"):
        value = row.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()[:10]
    return None


def build_history_indexes(rows):
    by_ticker = {}
    for row in rows:
        ticker = history_ticker(row)
        if ticker:
            by_ticker.setdefault(ticker.upper(), []).append(row)
    return by_ticker


def parse_csv_rows(csv_path):
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            die("Fundamentals CSV has no header")
        rows = list(reader)
    if not rows:
        die("Fundamentals CSV has no data rows")
    for row in rows:
        if not get_value(row, "Ticker", "TV Symbol", "Symbol"):
            die("Every fundamentals row must have a Ticker value")
    return rows


def csv_screener_region(row):
    screener = get_value(row, "Screener", "Screener ID")
    if screener:
        region = region_for_screener(screener)
        if region:
            return region
        if screener in REGION_IDS:
            return screener
    region = get_value(row, "Region")
    if region in REGION_IDS:
        return region
    if region:
        normalized = region.upper().replace("·", "/")
        if normalized in REGION_IDS:
            return normalized
    return None


def parse_float(value):
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    match = re.search(r"[-+]?\d+(?:\.\d+)?", text)
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None


def parse_valuation(row):
    pe = get_value(row, "P/E", "PE", "Price Earnings")
    ps = get_value(row, "P/S", "PS", "Price Sales")
    if pe:
        if pe.lower() == "n/m":
            return "n/m", None
        value = parse_float(pe)
        return ("P/E", value) if value is not None else ("P/E", None)
    if ps:
        if ps.lower() == "n/m":
            return "n/m", None
        value = parse_float(ps)
        return ("P/S", value) if value is not None else ("P/S", None)

    combined = get_value(row, "Valuation", "P/E or P/S", "PE or PS")
    if combined:
        if combined.lower() == "n/m":
            return "n/m", None
        match = re.search(r"P\s*/\s*([ES])\s*([-+]?\d+(?:\.\d+)?)", combined, re.I)
        if match:
            return "P/" + match.group(1).upper(), float(match.group(2))
    return None, None


def parse_market_cap(display):
    if display is None:
        return None, None
    text = display.strip()
    currency = None
    if re.search(r"\bUSD\b", text, re.I):
        currency = "USD"
    elif re.search(r"\bEUR\b", text, re.I):
        currency = "EUR"
    elif re.search(r"\bJPY\b", text, re.I):
        currency = "JPY"
    elif re.search(r"\bTWD\b", text, re.I):
        currency = "TWD"
    elif re.search(r"\bGBP\b", text, re.I):
        currency = "GBP"
    elif "NT$" in text:
        currency = "TWD"
    elif "$" in text:
        currency = "USD"
    elif "€" in text:
        currency = "EUR"
    elif "£" in text:
        currency = "GBP"
    elif "¥" in text:
        currency = "JPY"

    number_match = re.search(r"([-+]?\d+(?:\.\d+)?)\s*(k|m|bn|b)?\b", text, re.I)
    if not number_match:
        return None, currency
    number = float(number_match.group(1))
    unit = (number_match.group(2) or "").lower()
    multiplier = {"": 1, "k": 1_000, "m": 1_000_000, "bn": 1_000_000_000, "b": 1_000_000_000}[unit]
    value = number * multiplier
    return (value if currency == "USD" else None), currency


def parse_net_margin(row):
    flags = get_value(row, "Flags", "Flag") or ""
    match = re.search(r"net\s+margin\s+([-+]?\d+(?:\.\d+)?)\s*%", flags, re.I)
    return float(match.group(1)) if match else None


def load_notes(notes_path):
    notes = list(DEFAULT_NOTES)
    if notes_path is None:
        return notes
    value = read_json(notes_path)
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        die("--notes-json must contain an array of strings")
    notes.extend(value)
    return notes


def validate_archive_counts(parsed):
    found = parsed["found"]
    new = parsed["new"]
    repeats = len(parsed["repeats"])
    if found != new + repeats:
        die(f"Archive totals are inconsistent: found={found}, new={new}, repeats={repeats}")
    if sum(item["found"] for item in parsed["screeners"]) != found:
        die("Screener found counts do not sum to the archive total")
    if sum(item["new"] for item in parsed["screeners"]) != new:
        die("Screener new counts do not sum to the archive total")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True)
    parser.add_argument("--archive-md", required=True, type=Path)
    parser.add_argument("--fundamentals-csv", required=True, type=Path)
    parser.add_argument("--history-jsonl", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--notes-json", type=Path)
    args = parser.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        die("--date must use YYYY-MM-DD format")
    run_id = args.run_id or f"{args.date}Tweekly"
    archive_text = args.archive_md.read_text(encoding="utf-8")
    parsed = parse_archive(archive_text)
    validate_archive_counts(parsed)

    history_rows = parse_history(args.history_jsonl)
    history_by_ticker = build_history_indexes(history_rows)
    csv_rows = parse_csv_rows(args.fundamentals_csv)
    notes = load_notes(args.notes_json)

    rows_by_ticker = {}
    for row in csv_rows:
        tv_symbol = get_value(row, "Ticker", "TV Symbol", "Symbol")
        ticker = bare_ticker(tv_symbol)
        key = ticker.upper()
        if key in rows_by_ticker:
            die(f"Duplicate fundamentals ticker: {ticker}")
        rows_by_ticker[key] = (row, tv_symbol, ticker)

    repeat_set = {ticker.upper() for ticker in parsed["repeats"]}
    company_rows = []
    for key, (row, tv_symbol, ticker) in rows_by_ticker.items():
        if key not in repeat_set:
            company_rows.append((row, tv_symbol, ticker))
    company_rows.sort(key=lambda item: item[0].get("Ticker", item[2]).lower())

    if len(company_rows) != parsed["new"]:
        die(
            f"Fundamentals rows after excluding repeats={len(company_rows)}, "
            f"but archive new={parsed['new']}"
        )

    archive_lines = archive_text.splitlines()
    watchlist = set(parsed["watchlist"])
    companies = []
    for row, tv_symbol, ticker in company_rows:
        region = csv_screener_region(row)
        occurrences = parsed["section_occurrences"].get(ticker, [])
        if region is None and len(set(occurrences)) == 1:
            region = occurrences[0]
        if region is None:
            historical = history_by_ticker.get(ticker.upper(), [])
            historical_regions = {
                history_region(item) for item in historical if history_region(item)
            }
            if len(historical_regions) == 1:
                region = next(iter(historical_regions))
        if region not in REGION_IDS:
            die(f"Could not determine region for company ticker {ticker}")

        on_watchlist = False
        for line in archive_lines:
            if "**on watchlist**" in line and ticker_pattern(ticker).search(line):
                on_watchlist = True
                break

        valuation_kind, valuation_value = parse_valuation(row)
        mkt_cap_display = get_value(row, "Mkt cap", "Market Cap", "Market Capitalization") or ""
        mkt_cap_usd, currency = parse_market_cap(mkt_cap_display)
        flags_value = get_value(row, "Flags", "Flag")
        flags = flags_value.split("; ") if flags_value else []
        rev_growth = parse_float(
            get_value(row, "Rev growth", "Revenue Growth", "Revenue Growth YoY", "Rev Growth YoY %")
        )

        screener_url = None
        for historical in history_by_ticker.get(ticker.upper(), []):
            if history_date(historical) == args.date:
                screener_url = history_url(historical)
                if screener_url:
                    break

        companies.append({
            "region": region,
            "ticker": ticker,
            "tv_symbol": tv_symbol,
            "company": get_value(row, "Company", "Company Name", "Name") or "",
            "screener": REGION_IDS[region],
            "screener_url": screener_url,
            "on_watchlist": on_watchlist,
            "what_they_do": get_value(row, "What they do", "Business", "Description") or "",
            "mkt_cap_display": mkt_cap_display,
            "mkt_cap_usd": mkt_cap_usd,
            "valuation_kind": valuation_kind,
            "valuation_value": valuation_value,
            "rev_growth_yoy_pct": rev_growth,
            "net_margin_ttm": parse_net_margin(row),
            "flags": flags,
            "currency": currency,
        })

    found_watchlist = {item["ticker"] for item in companies if item["on_watchlist"]}
    if found_watchlist != watchlist:
        die(
            f"Watchlist markers for company rows {sorted(found_watchlist)!r} "
            f"do not match archive watchlist {sorted(watchlist)!r}"
        )

    repeats_skipped = []
    for ticker in parsed["repeats"]:
        historical = history_by_ticker.get(ticker.upper(), [])
        dates = [history_date(item) for item in historical if history_date(item)]
        prior_found_at = max(dates) if dates else None
        regions = {
            history_region(item) for item in historical if history_region(item)
        }
        region = next(iter(regions)) if len(regions) == 1 else None
        if region is None:
            occurrences = set(parsed["section_occurrences"].get(ticker, []))
            if len(occurrences) == 1:
                region = next(iter(occurrences))
        if region not in REGION_IDS:
            die(f"Could not determine region for repeated ticker {ticker}")
        repeats_skipped.append({
            "ticker": ticker,
            "region": region,
            "prior_found_at": prior_found_at,
        })

    by_region = {
        region: sum(1 for item in companies if item["region"] == region)
        for region in REGION_IDS
    }
    counts = {
        "found": parsed["found"],
        "new": parsed["new"],
        "repeats_skipped": len(repeats_skipped),
        "on_watchlist": sum(1 for item in companies if item["on_watchlist"]),
        "by_region": by_region,
    }

    if counts["new"] != len(companies):
        die("counts.new does not equal len(companies)")
    if counts["found"] != counts["new"] + counts["repeats_skipped"]:
        die("counts.found does not equal new plus repeats_skipped")

    for screener in parsed["screeners"]:
        matching = [
            item for item in companies if item["region"] == screener["region"]
        ]
        urls = [item["screener_url"] for item in matching if item["screener_url"]]
        if urls:
            screener["url"] = urls[0]

    document = {
        "_schema": SCHEMA,
        "found_at": args.date,
        "timezone": TIMEZONE,
        "producer": PRODUCER,
        "run_id": run_id,
        "status": "ok",
        "screeners": parsed["screeners"],
        "counts": counts,
        "repeats_skipped": repeats_skipped,
        "notes": notes,
        "companies": companies,
    }

    manifest = {
        "_schema": "swst-new-companies-manifest-v1",
        "date": args.date,
        "producer": PRODUCER,
        "run_id": run_id,
        "canonical": {
            "brief": "brief.md",
            "machine": ["companies.json", "fundamentals.csv"],
        },
        "files": [
            {"name": "brief.md", "role": "narrative brief"},
            {"name": "companies.json", "role": f"machine snapshot {SCHEMA}"},
            {"name": "fundamentals.csv", "role": "fundamentals table"},
            {"name": "_manifest.json", "role": "provenance"},
        ],
        "counts": {
            "found": counts["found"],
            "new": counts["new"],
            "repeats_skipped": counts["repeats_skipped"],
            "on_watchlist": counts["on_watchlist"],
        },
        "notes": notes,
    }

    index = {
        "_schema": "swst-new-companies-index-v1",
        "updated": args.date,
        "runs": [{
            "date": args.date,
            "run_id": run_id,
            "status": "ok",
            "found": counts["found"],
            "new": counts["new"],
            "path": f"{args.date}/",
        }],
    }

    dated_dir = args.out_dir / args.date
    dated_dir.mkdir(parents=True, exist_ok=True)
    copy_bytes(args.archive_md, dated_dir / "brief.md")
    copy_bytes(args.fundamentals_csv, dated_dir / "fundamentals.csv")
    copy_bytes(args.history_jsonl, args.out_dir / "history.jsonl")
    write_json(dated_dir / "companies.json", document)
    write_json(dated_dir / "_manifest.json", manifest)
    write_json(args.out_dir / "_index.json", index)
    write_json(args.out_dir / "latest.json", document)
    copy_bytes(dated_dir / "brief.md", args.out_dir / "latest.md")
    copy_bytes(dated_dir / "fundamentals.csv", args.out_dir / "latest.csv")

    print(
        f"date={args.date} found={counts['found']} new={counts['new']} "
        f"on_watchlist={counts['on_watchlist']}"
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, csv.Error) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(2)
