#!/usr/bin/env python3
"""Publish Hypnotoad's standing TradingView watchlist.

Inputs are a TradingView Positions JSON export, a core-symbol text file, and
an earnings next-dates cache. The output is refs/watchlist.yaml and an
optional extended-list CSV. This script never fetches anything from the network.
"""

import argparse
import csv
import io
import json
import re
import sys
from pathlib import Path

HEADER = """# The user's watchlist — PUBLISHED FILE, fetched at run time.
#
# This is the single source of truth for every routine's "watchlist" section:
#   #16 unusual-options-flow-daily  -> Pass A leg (the watchlist's option chains, legacy method)
#   #19 earnings-reminder-daily     -> \"Your watchlist\" section
#   #23 agentic-post-market-brief    -> \"Watchlist EOD review\" section
#   #26 agentic-pre-market-brief     -> the brief's watchlist section
#
# Published at: refs/watchlist.yaml on branch main of karizaco/minimax-cloud-outputs
# Schema + publish instructions: research/watchlist.README.md (maxhermes-migration)
#
# HOW TO EDIT: change this file, commit it to the outputs repo at refs/watchlist.yaml, and the
# next fire of every routine above picks it up. Nothing else has to change.
#
# RULES
#   - ticker is the plain US symbol (\"AAPL\", not \"NASDAQ:AAPL\").
#   - earnings_flag: true marks a name the earnings reminder always highlights.
#   - note is free text carried into the brief.
#   - unknown keys are ignored, so the file can grow without a routine change.
#   - never publish a file with no real tickers: that turns an honest \"no watchlist today\"
#     into an empty section that reads as a bug.
#
# SEED ({date}) — REPLACED BY THE STANDING LIST
#   The original eight-name seed was replaced on {date} by scripts/emit_watchlist.py.
#   Source: {source}
"""


def fail(message, code=2):
    print("ERROR: " + message, file=sys.stderr)
    raise SystemExit(code)


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, ValueError) as exc:
        fail("cannot read JSON input %s: %s" % (path, exc))
    if not isinstance(value, dict):
        fail("JSON input %s must contain an object" % path)
    return value


def read_core(path):
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        fail("cannot read core file %s: %s" % (path, exc))
    result = []
    for line in lines:
        line = line.split("#", 1)[0].strip()
        if line and line not in result:
            result.append(line)
    return result


def valid_symbol(value):
    return isinstance(value, str) and bool(re.match(r"^[^:]+:[^:]+$", value))


def map_primary(symbol, merged, cache):
    """Follow merged-listings chains, using cache primary metadata when present."""
    current = symbol
    visited = set()
    for _ in range(5):
        if current in visited:
            return current
        visited.add(current)
        entry = merged.get(current)
        if not isinstance(entry, dict):
            break
        primary = entry.get("primary")
        if not valid_symbol(primary):
            break
        current = primary
    cache_entry = cache.get(current)
    if isinstance(cache_entry, dict):
        primary = cache_entry.get("primary")
        if valid_symbol(primary) and primary not in visited:
            current = primary
    return current


def exchange_region(exchange):
    regions = {
        "NYSE": "us", "NASDAQ": "us", "AMEX": "us", "CBOE": "us",
        "OTC": "us", "NYSEARCA": "us", "BATS": "us",
        "TSX": "ca", "TSXV": "ca", "CSE": "ca", "NEO": "ca",
        "ASX": "au", "TSE": "jp", "TSE_DLY": "jp", "TWSE": "tw",
        "TPEX": "tw", "SGX": "sg", "HKEX": "hk", "JSE": "za",
        "LSE": "uk", "AIM": "uk", "XETR": "eu", "FWB": "eu",
        "EURONEXT": "eu", "MIL": "eu", "BME": "eu", "GPW": "eu",
        "NEWCONNECT": "eu", "OMXSTO": "eu", "OMXHEX": "eu",
        "OMXCOP": "eu", "OSL": "eu", "SIX": "eu", "VIE": "eu",
        "PSECZ": "eu", "BET": "eu", "ATHEX": "eu",
    }
    return regions.get(exchange, "other")


def yaml_string(value):
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    text = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return '"' + text + '"'


def yaml_inline_list(values):
    return "[" + ", ".join(yaml_string(value) for value in values) + "]"


def write_yaml_line(out, key, value):
    if isinstance(value, int) and not isinstance(value, bool):
        out.append(key + ": " + str(value))
    else:
        out.append(key + ": " + yaml_string(value))


def emit_yaml(date, source, positions, core, cache, merged, symbol_cache):
    symbols = positions.get("symbols")
    if not isinstance(symbols, list) or not all(valid_symbol(item) for item in symbols):
        fail("positions JSON must contain a symbols list of EXCHANGE:SYMBOL values")
    if len(symbols) < 20:
        fail("Positions has fewer than 20 symbols; refusing to publish")

    positions_raw = len(symbols)
    core_symbols = read_core(core)
    input_symbols = list(dict.fromkeys(symbols + core_symbols))

    core_primary = {map_primary(item, merged, symbol_cache) for item in core_symbols}
    for symbol, entry in symbol_cache.items():
        if isinstance(entry, dict) and entry.get("core") is True and valid_symbol(symbol):
            core_primary.add(symbol)
            core_primary.add(map_primary(symbol, merged, symbol_cache))
    for entry in merged.values():
        if isinstance(entry, dict) and entry.get("carry_core") is True:
            primary = entry.get("primary")
            if valid_symbol(primary):
                core_primary.add(map_primary(primary, merged, symbol_cache))

    position_primary = {map_primary(item, merged, symbol_cache) for item in symbols}
    all_primary = position_primary | core_primary

    resolved = {
        symbol: map_primary(symbol, merged, symbol_cache)
        for symbol in input_symbols
    }
    listings = {primary: set() for primary in all_primary}
    for primary in all_primary:
        entry = symbol_cache.get(primary)
        if isinstance(entry, dict):
            for listing in entry.get("also_listed") or []:
                if valid_symbol(listing) and listing != primary:
                    listings[primary].add(listing)

    for listing, entry in merged.items():
        if not isinstance(entry, dict) or not valid_symbol(listing):
            continue
        primary = map_primary(listing, merged, symbol_cache)
        if primary in listings and listing != primary:
            listings[primary].add(listing)

    collapsed_secondaries = sum(
        1 for symbol in input_symbols if resolved[symbol] != symbol
    )

    us_exchanges = {"NYSE", "NASDAQ", "AMEX", "CBOE", "NYSEARCA", "BATS"}
    watchlist = []
    watchlist_intl = []
    watchlist_keys = set()

    for primary in sorted(all_primary):
        if primary not in core_primary:
            continue
        exchange, ticker = primary.split(":", 1)
        region = exchange_region(exchange)
        if region == "other":
            print("WARNING: unknown exchange prefix %s" % exchange, file=sys.stderr)

        other_listings = sorted(
            listing for listing in listings.get(primary, set())
            if listing != primary
        )
        us_listings = sorted(
            listing for listing in other_listings
            if listing.split(":", 1)[0] in us_exchanges
        )
        us_symbol = primary if exchange in us_exchanges else (
            us_listings[0] if us_listings else None
        )

        if us_symbol is not None:
            us_exchange, us_ticker = us_symbol.split(":", 1)
            note = "core; primary listing %s" % primary
            if us_symbol != primary:
                note += " (US line %s)" % us_symbol
            entry = {
                "ticker": us_ticker,
                "note": note,
                "earnings_flag": True,
                "tv_symbol": primary,
                "us_symbol": us_symbol,
                "region": region,
                "tags": ["core"],
            }
            watchlist.append(entry)
            watchlist_keys.add(primary)
        else:
            note = "core; primary listing %s" % primary
            entry = {
                "ticker": ticker,
                "note": note,
                "tv_symbol": primary,
                "region": region,
                "tags": ["core"],
            }
            if other_listings:
                entry["also_listed"] = other_listings
            watchlist_intl.append(entry)

    watchlist.sort(key=lambda item: item["ticker"])
    watchlist_intl.sort(key=lambda item: item["ticker"])

    extended = []
    for primary in sorted(all_primary):
        exchange, ticker = primary.split(":", 1)
        region = exchange_region(exchange)
        if region == "other":
            print("WARNING: unknown exchange prefix %s" % exchange, file=sys.stderr)

        cache_entry = symbol_cache.get(primary)
        instrument_type = None
        if isinstance(cache_entry, dict):
            instrument_type = cache_entry.get("type")
            if instrument_type is None:
                instrument_type = cache_entry.get("instrument_type")

        other_listings = sorted(
            listing for listing in listings.get(primary, set())
            if listing != primary
        )

        merge_note = None
        for listing in other_listings:
            merge_entry = merged.get(listing)
            if isinstance(merge_entry, dict) and merge_entry.get("note"):
                merge_note = merge_entry["note"]
                break

        note = merge_note or ""
        if primary not in position_primary:
            if note:
                note += "; "
            note += "core list only (not in Positions)"

        row = {
            "tv_symbol": primary,
            "ticker": ticker,
            "exchange": exchange,
            "region": region,
            "core": primary in core_primary,
            "in_watchlist_key": primary in watchlist_keys,
            "instrument_type": instrument_type,
            "also_listed": other_listings,
        }
        if note:
            row["note"] = note
        extended.append(row)

    if not watchlist:
        fail("watchlist would be empty; refusing to publish")

    out = [HEADER.format(date=date, source=source)]
    write_yaml_line(out, "version", 2)
    write_yaml_line(out, "updated", date)
    write_yaml_line(out, "source", source)
    write_yaml_line(out, "generated_by", "scripts/emit_watchlist.py")
    out.append("counts:")
    out.append("  watchlist: %d" % len(watchlist))
    out.append("  watchlist_intl: %d" % len(watchlist_intl))
    out.append("  extended: %d" % len(extended))
    out.append("  positions_raw: %d" % positions_raw)
    out.append("  collapsed_secondaries: %d" % collapsed_secondaries)

    for key, rows in (
        ("watchlist", watchlist),
        ("watchlist_intl", watchlist_intl),
        ("extended", extended),
    ):
        out.append(key + ":")
        for row in rows:
            first = True
            for key_name, value in row.items():
                prefix = "  - " if first else "    "
                if isinstance(value, list):
                    out.append(prefix + key_name + ": " + yaml_inline_list(value))
                else:
                    out.append(prefix + key_name + ": " + yaml_string(value))
                first = False

    return (
        "\n".join(out) + "\n",
        watchlist,
        watchlist_intl,
        extended,
        positions_raw,
        collapsed_secondaries,
    )


def emit_csv(extended):
    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow([
        "tv_symbol", "ticker", "exchange", "region", "core",
        "in_watchlist_key", "instrument_type", "also_listed", "note",
    ])
    for row in extended:
        writer.writerow([
            row["tv_symbol"],
            row["ticker"],
            row["exchange"],
            row["region"],
            str(row["core"]).lower(),
            str(row["in_watchlist_key"]).lower(),
            row["instrument_type"] if row["instrument_type"] is not None else "",
            ";".join(row["also_listed"]),
            row.get("note", ""),
        ])
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--positions-json", required=True)
    parser.add_argument("--core-txt", required=True)
    parser.add_argument("--cache-json", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--csv-out")
    args = parser.parse_args()

    positions = load_json(args.positions_json)
    cache = load_json(args.cache_json)

    merged = cache.get("merged_listings", {})
    if not isinstance(merged, dict):
        fail("cache merged_listings must be an object")

    symbol_cache = cache.get("symbols", {})
    if not isinstance(symbol_cache, dict):
        fail("cache symbols must be an object")

    source = (
        "TradingView watchlist 'Positions' (id %s) fetched %s + core list + "
        "earnings next-dates cache merged_listings"
    ) % (
        positions.get("id", "unknown"),
        positions.get("fetched_at", "unknown"),
    )

    (
        text,
        watchlist,
        watchlist_intl,
        extended,
        positions_raw,
        collapsed_secondaries,
    ) = emit_yaml(
        args.date,
        source,
        positions,
        args.core_txt,
        cache,
        merged,
        symbol_cache,
    )

    csv_text = emit_csv(extended) if args.csv_out else None

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")

    if args.csv_out:
        csv_path = Path(args.csv_out)
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        csv_path.write_text(csv_text, encoding="utf-8")

    print(json.dumps({
        "watchlist": len(watchlist),
        "watchlist_intl": len(watchlist_intl),
        "extended": len(extended),
        "positions_raw": positions_raw,
        "collapsed_secondaries": collapsed_secondaries,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
