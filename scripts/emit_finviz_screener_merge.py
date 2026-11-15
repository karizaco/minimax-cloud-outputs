#!/usr/bin/env python3
"""Publish the weekly Finviz screener merge.

Inputs are a dated Grok Box merge Markdown file, screener bookmark Markdown,
optional older merge Markdown files, and refs/watchlist.yaml. Outputs are the
finviz-screener-merge family: canonical JSON/CSV/Markdown, dated run files,
history, and an index. This script never fetches anything from the network.
"""

import argparse
import csv
import io
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

FAMILY = "finviz-screener-merge"
SCHEMA = "finviz-screener-merge-v1"
PRODUCER = "grok-bot/finviz-screener-merge"
SKILL = "finviz-screener-merge"
BANGKOK = timezone(timedelta(hours=7))
EXCHANGES = {"NYSE", "NASDAQ", "AMEX", "CBOE", "OTC"}


def fail(message):
    raise ValueError(message)


def read_text(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"cannot read {path}: {exc}")


def parse_date(value):
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        fail(f"invalid date {value!r}; expected YYYY-MM-DD")
    if parsed.isoformat() != value:
        fail(f"invalid date {value!r}; expected YYYY-MM-DD")
    return parsed


def generated_at(value):
    if value:
        try:
            parsed = datetime.fromisoformat(value)
        except ValueError:
            fail(f"invalid --generated-at {value!r}")
        if parsed.tzinfo is None:
            fail("--generated-at must include a UTC offset")
        return parsed.astimezone(BANGKOK).isoformat(timespec="seconds")
    return datetime.now(BANGKOK).isoformat(timespec="seconds")


def section(text, title):
    match = re.search(
        r"^##\s+" + re.escape(title) + r"[^\n]*$\n(.*?)(?=^##\s+|\Z)",
        text,
        re.MULTILINE | re.IGNORECASE | re.DOTALL,
    )
    return match.group(1).strip() if match else None


def strip_markdown(value):
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"\1", value)
    value = re.sub(r"\*([^*]+)\*", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"^[-*+]\s+", "", value)
    return value.strip()


def bullet_items(body):
    if not body:
        return []
    return [strip_markdown(line) for line in body.splitlines() if re.match(r"^\s*[-*+]\s+", line)]


def parse_coverage(body):
    if not body:
        return []
    notes = []
    for line in body.splitlines():
        match = re.match(r"^\s*[-*+]\s+(.*)$", line)
        if match:
            notes.append(strip_markdown(match.group(1)))
    return notes


def parse_urls(text):
    urls = {}
    current = None
    for line in text.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            current = match.group(1).strip()
            continue
        if current and re.match(r"^https?://\S+$", line.strip()):
            urls[current] = line.strip()
            current = None
    return urls


def parse_union(body):
    if not body:
        return []

    match = re.search(
        r"^\*\*(\d+)\*\*\s+symbols?",
        body,
        re.MULTILINE | re.IGNORECASE,
    )
    text = body[match.end():] if match else body

    if match:
        intro_line, separator, remainder = text.partition("\n")
        if ":" in intro_line:
            text = remainder if separator else intro_line.split(":", 1)[1]

    items = []
    for item in re.split(r"[,\n]", text):
        item = item.strip().rstrip(".").strip()
        if item:
            items.append(item)

    return items


def parse_named_bullets(body, label_pattern):
    result = []
    if not body:
        return result
    pattern = re.compile(label_pattern, re.IGNORECASE)
    for line in body.splitlines():
        match = pattern.match(line.strip())
        if match:
            result.append((match.group(1).strip(), match.group(2).strip()))
    return result


def parse_overlap(body):
    if not body:
        return []
    if re.search(r"_\s*None\s*_", body, re.IGNORECASE):
        return []
    text = re.sub(r"^\s*[-*+]\s+", "", body, flags=re.MULTILINE)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    return [item.strip() for item in text.split(",") if item.strip()]


def parse_sizes(body):
    rows = []
    if not body:
        return rows
    for line in body.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4 or cells[0] in {"Screener", "---"} or set(cells[0]) <= {"-", ":"}:
            continue
        def number(value):
            match = re.search(r"-?\d+", value.replace(",", ""))
            return int(match.group(0)) if match else None
        rows.append({
            "name": strip_markdown(cells[0]),
            "tickers_page1": number(cells[1]),
            "finviz_total": number(cells[2]),
            "notes": strip_markdown(cells[3]),
        })
    return rows


def parse_screener_membership(body):
    result = []
    if not body:
        return result
    pattern = re.compile(r"^-\s+\*\*(.+?)\*\*\s*\((\d+)\)\s*:\s*(.*)$")
    for line in body.splitlines():
        match = pattern.match(line.strip())
        if not match:
            continue
        raw = match.group(3).strip()
        if re.match(r"^_none_\b", raw, re.IGNORECASE):
            tickers = []
        else:
            tickers = [item.strip() for item in raw.split(",") if item.strip()]
        result.append({"name": match.group(1).strip(), "tickers": tickers})
    return result


def parse_data_as_of(text):
    match = re.search(r"Data reflects\s+(.+?)(?:\.|$)", text, re.IGNORECASE)
    return match.group(1).strip() if match else None


def parse_watchlist(path):
    """Read watchlist symbol values without imposing a YAML structure.

    The watchlist has changed between schema versions, so this deliberately
    scans for the symbol keys rather than parsing or validating the complete
    YAML document.
    """
    if not path:
        return {"values": [], "has_tv_symbol": False}

    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError:
        return {"values": [], "has_tv_symbol": False}

    values = []
    has_tv_symbol = False
    key_pattern = re.compile(r"^\s*(?:-\s*)?(tv_symbol|us_symbol)\s*:\s*(.*?)\s*$", re.IGNORECASE)

    for raw_line in text.splitlines():
        match = key_pattern.match(raw_line)
        if not match:
            continue
        key = match.group(1).lower()
        raw_value = match.group(2).strip()
        if key == "tv_symbol":
            has_tv_symbol = True

        # Remove an unquoted YAML comment, while preserving # characters
        # inside quoted values.
        if raw_value.startswith(('"', "'")):
            quote = raw_value[0]
            end = raw_value.find(quote, 1)
            if end != -1:
                raw_value = raw_value[1:end]
        else:
            raw_value = re.split(r"\s+#", raw_value, maxsplit=1)[0].strip()

        if raw_value.startswith("[") and raw_value.endswith("]"):
            raw_values = raw_value[1:-1].split(",")
        else:
            raw_values = [raw_value]

        for item in raw_values:
            item = item.strip()
            if len(item) >= 2 and item[0] == item[-1] and item[0] in {'"', "'"}:
                item = item[1:-1].strip()
            if item:
                values.append(item)

    return {"values": values, "has_tv_symbol": has_tv_symbol}


def watchlist_symbols(watchlist):
    if not watchlist or not watchlist.get("has_tv_symbol"):
        return None

    symbols = set()
    for item in watchlist.get("values", []):
        parts = item.split(":", 1)
        if len(parts) < 2:
            continue
        exchange = parts[0].strip().upper()
        symbol = parts[1].strip()
        if exchange in EXCHANGES and symbol:
            symbols.add(symbol)
    return symbols


def source_date(text):
    match = re.search(r"(20\d{2}-\d{2}-\d{2})", text)
    return match.group(1) if match else None


def seed_records(paths, notes):
    records = []
    for path in paths:
        try:
            text = read_text(path)
        except ValueError as exc:
            notes.append(f"seed {Path(path).name}: {exc}")
            continue
        found = source_date(text)
        if not found:
            notes.append(f"seed {Path(path).name}: no date found")
            continue
        try:
            membership = parse_screener_membership(section(text, "Tickers by screener (page 1)"))
            if not membership:
                fail("no ticker membership found")
            parse_date(found)
        except (ValueError, KeyError) as exc:
            notes.append(f"seed {Path(path).name}: {exc}")
            continue
        records.append({"date": found, "path": path, "membership": membership})
    return records


def history_entries(screeners):
    entries = []
    for screener in screeners:
        if not screener["unique"]:
            continue
        for ticker in screener["tickers"]:
            entries.append((ticker, screener["name"]))
    grouped = {}
    for ticker, name in entries:
        grouped.setdefault(ticker, []).append(name)
    return grouped


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def json_text(value):
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def csv_text(columns, rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)


def build(args, now_text):
    session_date = parse_date(args.date)
    merge_text = read_text(args.merge_md)
    screeners_text = read_text(args.screeners_md)
    notes = []
    seed_data = seed_records(args.seed_md or [], notes)
    coverage = parse_coverage(section(merge_text, "Coverage"))
    full_overlap = parse_overlap(section(merge_text, "Full overlap (all 11 unique screeners)"))
    if not full_overlap:
        for match in re.finditer(r"^##\s+Full overlap[^\n]*\n(.*?)(?=^##\s+|\Z)", merge_text, re.MULTILINE | re.IGNORECASE | re.DOTALL):
            full_overlap = parse_overlap(match.group(1))
            break
    union = parse_union(section(merge_text, "All tickers (unique union)"))
    multi3 = parse_named_bullets(section(merge_text, "≥3 multi-hits"), r"^-\s+\*\*(.+?)\*\*\s*\((\d+)")
    multi2 = parse_named_bullets(section(merge_text, "≥2 multi-hits"), r"^-\s+\*\*(.+?)\*\*\s*\((\d+)")
    sizes = parse_sizes(section(merge_text, "Per-screener sizes (first page)"))
    membership = parse_screener_membership(section(merge_text, "Tickers by screener (page 1)"))
    stocktwits = section(merge_text, "StockTwits") or ""
    urls = parse_urls(screeners_text)
    size_map = {row["name"]: row for row in sizes}
    member_map = {row["name"]: row["tickers"] for row in membership}
    names = list(member_map)
    if not names:
        fail("merge Markdown has no 'Tickers by screener (page 1)' entries")
    unique_names = []
    seen_urls = {}
    screeners = []
    for name in names:
        url = urls.get(name)
        duplicate_of = None
        unique = True
        if url and url in seen_urls:
            unique = False
            duplicate_of = seen_urls[url]
        elif url:
            seen_urls[url] = name
        if unique:
            unique_names.append(name)
        size = size_map.get(name, {})
        screener_notes = size.get("notes", "")
        screeners.append({
            "name": name,
            "url": url,
            "unique": unique,
            "duplicate_of": duplicate_of,
            "tickers_page1": size.get("tickers_page1"),
            "finviz_total": size.get("finviz_total"),
            "notes": screener_notes,
            "tickers": member_map[name],
        })
    grouped = history_entries(screeners)
    parsed_union = set(grouped)
    if union and parsed_union != set(union):
        notes.append("Declared union differs from parsed unique-screener ticker membership; parsed membership was used.")
    failed_notes = [s["name"] for s in screeners if re.search(r"\b(fail(?:ed|ure)?|error|non[- ]?ok)\b", s["notes"], re.IGNORECASE)]
    status = "degraded" if failed_notes or not parsed_union else "ok"
    if failed_notes:
        notes.append("Screener notes reported failure or non-OK status: " + ", ".join(failed_notes) + ".")
    watch_records = parse_watchlist(args.watchlist) if args.watchlist else {"values": [], "has_tv_symbol": False}
    watched = watchlist_symbols(watch_records)
    if watched is None:
        notes.append("watchlist has no tv_symbol keys; on_watchlist not computed")
    previous_seeds = [seed for seed in seed_data if seed["date"] < args.date]
    previous = max(previous_seeds, key=lambda item: item["date"]) if previous_seeds else None
    previous_symbols = set()
    if previous:
        for item in previous["membership"]:
            previous_symbols.update(item["tickers"])
    all_dates = sorted({seed["date"] for seed in seed_data} | {args.date})
    first_seen = {}
    history_rows = []
    for found_at in all_dates:
        if found_at == args.date:
            members = grouped
        else:
            seed = next(item for item in seed_data if item["date"] == found_at)
            members = {}
            for item in seed["membership"]:
                for ticker in item["tickers"]:
                    members.setdefault(ticker, []).append(item["name"])
        for ticker, member_names in sorted(members.items()):
            first_seen.setdefault(ticker, found_at)
            history_rows.append({
                "found_at": found_at,
                "ticker": ticker,
                "hits": len(member_names),
                "screeners": member_names,
            })
    ticker_rows = []
    for ticker, member_names in grouped.items():
        hits = len(member_names)
        ticker_rows.append({
            "ticker": ticker,
            "hits": hits,
            "screeners": member_names,
            "first_seen": first_seen.get(ticker),
            "new_this_week": None if previous is None else ticker not in previous_symbols,
            "on_watchlist": None if watched is None else ticker in watched,
        })
    ticker_rows.sort(key=lambda row: (-row["hits"], row["ticker"]))
    counts = {
        "screeners": len(screeners),
        "unique_screeners": len(unique_names),
        "union": len(grouped),
        "full_overlap": len(full_overlap),
        "multi_hit_3plus": len(multi3),
        "multi_hit_2plus": len(multi2),
        "new_this_week": sum(1 for row in ticker_rows if row["new_this_week"] is True),
        "on_watchlist": sum(1 for row in ticker_rows if row["on_watchlist"] is True),
    }
    run_id = args.date + "Tweekly"
    machine = {
        "_schema": SCHEMA,
        "found_at": args.date,
        "timezone": "Asia/Bangkok",
        "producer": PRODUCER,
        "run_id": run_id,
        "status": status,
        "data_as_of": parse_data_as_of(merge_text),
        "screeners": [{key: value for key, value in item.items() if key != "tickers"} for item in screeners],
        "counts": counts,
        "full_overlap": full_overlap,
        "tickers": ticker_rows,
        "stocktwits_note": stocktwits.strip(),
        "coverage_notes": coverage,
    }
    for item in machine["screeners"]:
        item["tickers"] = next(s["tickers"] for s in screeners if s["name"] == item["name"])
    history_rows.sort(key=lambda row: (row["found_at"], row["ticker"]))
    history_text = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in history_rows)
    csv_rows = [{
        "ticker": row["ticker"],
        "hits": row["hits"],
        "screeners": "; ".join(row["screeners"]),
        "first_seen": row["first_seen"] or "",
        "new_this_week": "" if row["new_this_week"] is None else str(row["new_this_week"]).lower(),
        "on_watchlist": "" if row["on_watchlist"] is None else str(row["on_watchlist"]).lower(),
    } for row in ticker_rows]
    ticker_csv = csv_text(
        ["ticker", "hits", "screeners", "first_seen", "new_this_week", "on_watchlist"],
        csv_rows,
    )
    brief = build_brief(args, now_text, status, coverage, notes, screeners, ticker_rows, counts, merge_text)
    manifest = {
        "_schema": FAMILY + "-manifest-v1",
        "date": args.date,
        "producer": PRODUCER + "/" + SKILL,
        "run_id": run_id,
        "generated_at": now_text,
        "provenance": f"Grok Bot box merge Markdown and standing screener bookmarks; built {now_text}; covered the weekly session dated {args.date}.",
        "canonical": {"brief": "brief.md", "machine": ["merge.json", "tickers.csv"]},
        "files": [
            {"name": "_manifest.json", "role": "provenance"},
            {"name": "brief.md", "role": "brief"},
            {"name": "merge.json", "role": "machine"},
            {"name": "tickers.csv", "role": "tickers"},
        ],
        "counts": counts,
        "notes": notes,
    }
    index_entry = {
        "date": args.date,
        "run_id": run_id,
        "status": status,
        "counts": {
            "union": counts["union"],
            "multi_hit_2plus": counts["multi_hit_2plus"],
            "new_this_week": counts["new_this_week"],
        },
        "path": args.date + "/",
    }
    return {
        "machine": json_text(machine),
        "csv": ticker_csv,
        "brief": brief,
        "history": history_text,
        "manifest": json_text(manifest),
        "index_entry": index_entry,
        "counts": counts,
    }


def build_brief(args, now_text, status, coverage, notes, screeners, tickers, counts, merge_text):
    deviation_lines = [f"- {note}" for note in notes] if notes else ["- none"]
    screener_rows = [
        [s["name"], "yes" if s["unique"] else "no", s["duplicate_of"] or "", s["tickers_page1"] if s["tickers_page1"] is not None else "", s["finviz_total"] if s["finviz_total"] is not None else "", s["notes"]]
        for s in screeners
    ]
    ticker_rows = [
        [row["ticker"], row["hits"], "; ".join(row["screeners"]), row["first_seen"] or "", "" if row["new_this_week"] is None else str(row["new_this_week"]).lower(), "" if row["on_watchlist"] is None else str(row["on_watchlist"]).lower()]
        for row in tickers
    ]
    provenance = f"Source: Grok Bot box archive ({args.merge_md} and {args.screeners_md}); built {now_text}; weekly Sunday session dated {args.date}."
    parts = [
        "---",
        f"date: {args.date}",
        f"producer: {PRODUCER}",
        f"contract: {FAMILY}-v1",
        f"source: \"Grok Bot box archive ({args.merge_md} and {args.screeners_md})\"",
        f"generated_at: {now_text}",
        f"status: {status}",
        "---",
        "",
        provenance,
        "",
        "## Deviations / degraded paths",
        *deviation_lines,
        "",
        "## Coverage notes",
        *(["- " + note for note in coverage] if coverage else ["- none"]),
        "",
        table(["Screener", "Unique", "Duplicate of", "Page-1 tickers", "Finviz total", "Notes"], screener_rows),
        "",
        f"The run contains {counts['screeners']} named screeners, {counts['unique_screeners']} unique URL sets, and {counts['union']} unique tickers from unique screeners. Duplicate URL sets are retained in the screener ledger but excluded from intersection and hit counts.",
        "",
        "## Tickers",
        "",
        table(["Ticker", "Hits", "Screeners", "First seen", "New this week", "On watchlist"], ticker_rows),
        "",
        f"The table contains {len(tickers)} tickers sorted by descending hits and then ticker. An empty new-this-week value means no immediately previous seeded run was available; an empty watchlist value means the watchlist contained no tv_symbol keys.",
        "",
        "## Source Markdown",
        "",
        merge_text.rstrip(),
        "",
    ]
    return "\n".join(parts)


def publish(args, built):
    root = Path(args.out_dir)
    dated = root / args.date
    files = {
        dated / "_manifest.json": built["manifest"],
        dated / "brief.md": built["brief"],
        dated / "merge.json": built["machine"],
        dated / "tickers.csv": built["csv"],
        root / "latest.json": built["machine"],
        root / "latest.md": built["brief"],
        root / "latest.csv": built["csv"],
        root / "history.jsonl": built["history"],
    }
    index_path = root / "_index.json"
    index = {"_schema": FAMILY + "-index-v1", "updated": args.date, "runs": []}
    if index_path.exists():
        try:
            existing = json.loads(index_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"cannot read existing index {index_path}: {exc}")
        if isinstance(existing, dict) and isinstance(existing.get("runs"), list):
            index = existing
    runs = [run for run in index.get("runs", []) if run.get("date") != args.date]
    runs.append(built["index_entry"])
    runs.sort(key=lambda run: run.get("date", ""))
    index["_schema"] = FAMILY + "-index-v1"
    index["updated"] = max([run.get("date", "") for run in runs] + [args.date])
    index["runs"] = runs
    files[index_path] = json_text(index)
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True)
    parser.add_argument("--merge-md", required=True)
    parser.add_argument("--screeners-md", required=True)
    parser.add_argument("--seed-md", action="append", default=[])
    parser.add_argument("--watchlist", default="refs/watchlist.yaml")
    parser.add_argument("--out-dir", default=FAMILY)
    parser.add_argument("--generated-at")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        now_text = generated_at(args.generated_at)
        built = build(args, now_text)
        files = publish(args, built)
        if args.dry_run:
            for path in sorted(files, key=lambda item: str(item)):
                print(path)
            print(json.dumps(built["counts"], sort_keys=True))
        else:
            for path, content in files.items():
                write_text(path, content)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
