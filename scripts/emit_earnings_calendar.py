#!/usr/bin/env python3
"""Emit the weekly earnings-calendar family and shared next-dates cache.

Inputs are a Grok Bot markdown calendar, its CSV, and the shared cache JSON.
Outputs are the earnings-calendar family and refs/earnings-next-dates.json.
This script never fetches anything from the network.
"""

import argparse
import csv
import io
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

PRODUCER = "grok-bot/weekly-earnings-calendar"
SCHEMA = "earnings-calendar-v1"
BANGKOK = timezone(timedelta(hours=7))
SOURCE = (
    "Grok Bot weekly-earnings-calendar archive "
    "(TradingView MCP calendar + symbol-data; StockAnalysis confirmation)"
)
REQUIRED = [
    "date", "ticker", "exchange", "symbol", "timing", "eps_est",
    "eps_growth_est_pct", "rev_est", "rev_growth_est_pct", "source", "core",
    "notes", "sa_confirmed", "tv_date", "confirmed", "eps_forecast_raw",
    "eps_last_raw", "rev_forecast_raw", "rev_last_raw", "currency",
]


def load_json(path):
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, ValueError) as exc:
        raise ValueError("cannot read JSON input %s: %s" % (path, exc))


def number(value):
    if value is None or str(value).strip() == "":
        return None
    try:
        return float(str(value).strip())
    except ValueError:
        return None


def boolean(value):
    text = str(value).strip().lower()
    if text == "true":
        return True
    if text == "false":
        return False
    raise ValueError("invalid boolean value: %r" % value)


def md_field(text, name):
    match = re.search(r"^\*\*%s:\*\*\s*(.*?)\s*$" % re.escape(name), text, re.M)
    return match.group(1).strip() if match else None


def strip_md(text):
    text = text or ""
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    return text.strip()


def sanitize_box_paths(text, repo_root):
    """Remove backticks from path-like tokens not known to exist in this repo."""
    def replace(match):
        token = match.group(1)
        if "/" in token and re.search(r"\.(?:md|csv|json|jsonl|yaml|py)$", token):
            candidate = repo_root / token
            if not candidate.exists():
                return token
        return match.group(0)
    return re.sub(r"`([^`\n]+)`", replace, text)


def parse_window(text, rows):
    line = md_field(text, "Window") or ""
    match = re.search(
        r"(\d{4}-\d{2}-\d{2})\s+through\s+(\d{4}-\d{2}-\d{2})", line
    )
    if match:
        return {"from": match.group(1), "to": match.group(2)}
    dates = [row["date"] for row in rows if row["date"]]
    return {"from": min(dates) if dates else None, "to": max(dates) if dates else None}


def parse_rows(csv_text):
    reader = csv.DictReader(io.StringIO(csv_text))
    if not reader.fieldnames or any(name not in reader.fieldnames for name in REQUIRED):
        raise ValueError("calendar CSV is missing required columns")
    rows = []
    for source in reader:
        ticker = (source.get("ticker") or "").strip()
        symbol = (source.get("symbol") or "").strip()
        if not ticker and not symbol:
            continue
        eps_growth = source.get("eps_growth_est_pct", "")
        rev_growth = source.get("rev_growth_est_pct", "")
        eps_flag = "n/m tiny base" if "tiny base" in eps_growth.lower() else None
        rev_flag = "n/m tiny base" if "tiny base" in rev_growth.lower() else None
        rows.append({
            "date": (source.get("date") or "").strip() or None,
            "ticker": ticker,
            "exchange": (source.get("exchange") or "").strip() or None,
            "symbol": symbol,
            "timing": (source.get("timing") or "").strip() or None,
            "core": (source.get("core") or "").strip().upper() == "Y",
            "confirmed": boolean(source.get("confirmed") or "False"),
            "sa_confirmed": (source.get("sa_confirmed") or "").strip() or None,
            "tv_date": (source.get("tv_date") or "").strip() or None,
            "eps_est": number(source.get("eps_est")),
            "eps_growth_est_pct": None if eps_flag else number(eps_growth),
            "eps_growth_flag": eps_flag,
            "rev_est_display": (source.get("rev_est") or "").strip(),
            "rev_growth_est_pct": None if rev_flag else number(rev_growth),
            "rev_growth_flag": rev_flag,
            "eps_forecast_raw": number(source.get("eps_forecast_raw")),
            "eps_last_raw": number(source.get("eps_last_raw")),
            "rev_forecast_raw": number(source.get("rev_forecast_raw")),
            "rev_last_raw": number(source.get("rev_last_raw")),
            "currency": (source.get("currency") or "").strip() or None,
            "source": (source.get("source") or "").strip() or None,
            "notes": (source.get("notes") or "").strip() or None,
        })
    rows.sort(key=lambda row: (row["date"] or "", row["ticker"], row["symbol"]))
    return rows


def normalize_generated_at(value):
    if value:
        try:
            parsed = datetime.fromisoformat(value)
        except ValueError:
            raise ValueError("--generated-at must be ISO8601")
        if parsed.tzinfo is None:
            raise ValueError("--generated-at must include a timezone")
        parsed = parsed.astimezone(BANGKOK)
    else:
        parsed = datetime.now(BANGKOK)
    return parsed.replace(microsecond=0).isoformat(timespec="seconds")


def front_matter(date, generated_at, status):
    return (
        "---\n"
        "date: %s\n"
        "producer: %s\n"
        "contract: earnings-calendar-v1\n"
        "source: \"%s\"\n"
        "generated_at: %s\n"
        "status: %s\n"
        "---\n\n"
    ) % (
        date,
        PRODUCER,
        SOURCE.replace("\\", "\\\\").replace('"', '\\"'),
        generated_at,
        status,
    )


def json_bytes(value):
    return json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="")


def make_manifest(date, run_id, generated_at, window, counts, notes):
    return {
        "_schema": "earnings-calendar-manifest-v1",
        "date": date,
        "producer": PRODUCER,
        "run_id": run_id,
        "generated_at": generated_at,
        "provenance": (
            "Grok Bot box run %s, covering the %s through %s session window; "
            "built %s by scripts/emit_earnings_calendar.py."
        ) % (date, window.get("from"), window.get("to"), generated_at),
        "canonical": {
            "brief": "brief.md",
            "machine": ["calendar.json", "calendar.csv"],
        },
        "files": [
            {"name": "_manifest.json", "role": "provenance"},
            {"name": "brief.md", "role": "brief"},
            {"name": "calendar.json", "role": "machine-json"},
            {"name": "calendar.csv", "role": "machine-csv"},
        ],
        "counts": counts,
        "notes": notes,
    }


def update_history(path, date, rows):
    existing = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except ValueError:
                raise ValueError("garbled history file: %s" % path)
            if item.get("run_date") != date:
                existing.append(item)
    seen = set()
    for row in rows:
        key = (date, row["symbol"] or row["ticker"])
        if key in seen:
            continue
        seen.add(key)
        existing.append({
            "run_date": date,
            "symbol": row["symbol"],
            "date": row["date"],
            "timing": row["timing"],
            "confirmed": row["confirmed"],
            "core": row["core"],
        })
    existing.sort(key=lambda item: (
        item.get("run_date", ""),
        item.get("symbol") or "",
        item.get("date") or "",
    ))
    return "".join(
        json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n"
        for item in existing
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True)
    parser.add_argument("--calendar-md", required=True, type=Path)
    parser.add_argument("--calendar-csv", required=True, type=Path)
    parser.add_argument("--cache-json", required=True, type=Path)
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--run-id")
    parser.add_argument("--generated-at")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    date = args.date
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        raise ValueError("--date must be YYYY-MM-DD")
    generated_at = normalize_generated_at(args.generated_at)
    run_id = args.run_id or (date + "Tweekly")

    try:
        md = args.calendar_md.read_text(encoding="utf-8")
        csv_text = args.calendar_csv.read_text(encoding="utf-8")
        cache = load_json(args.cache_json)
    except (OSError, UnicodeError, ValueError) as exc:
        raise ValueError(str(exc))

    if not isinstance(cache, dict):
        raise ValueError("cache JSON must contain an object")

    csv_text = csv_text.replace("\r\n", "\n").replace("\r", "\n")
    rows = parse_rows(csv_text)
    window = parse_window(md, rows)

    by_date = {}
    by_timing = {"BMO": 0, "AMC": 0, "unknown": 0}
    for row in rows:
        by_date[row["date"]] = by_date.get(row["date"], 0) + 1
        timing = row["timing"] if row["timing"] in by_timing else "unknown"
        by_timing[timing] += 1

    sa_confirmed = sum(row["sa_confirmed"] is not None for row in rows)
    counts = {
        "rows": len(rows),
        "sa_confirmed": sa_confirmed,
        "soft_filtered": len(rows) - sa_confirmed,
        "core_rows": sum(row["core"] for row in rows),
        "by_date": by_date,
        "by_timing": by_timing,
    }
    needs_attention = md_field(md, "Needs attention")
    universe = md_field(md, "Universe")
    status = "ok" if rows and window.get("from") and window.get("to") else "degraded"

    deviations = []
    if status == "degraded":
        deviations.append("calendar rows or window metadata were unavailable")
    notes = [
        "line endings normalised to LF",
        "window %s through %s" % (window.get("from"), window.get("to")),
        "cache published at refs/earnings-next-dates.json (cache run %s)" %
        cache.get("run"),
    ]
    if deviations:
        notes.extend(deviations)

    machine = {
        "_schema": SCHEMA,
        "run_date": date,
        "timezone": "Asia/Bangkok",
        "producer": PRODUCER,
        "run_id": run_id,
        "status": status,
        "window": window,
        "universe_note": strip_md(universe),
        "counts": counts,
        "needs_attention": needs_attention,
        "rows": rows,
    }

    box_body = sanitize_box_paths(md, args.repo_root)
    provenance = (
        "**Provenance:** box run %s (Asia/Bangkok) · window %s → %s · "
        "built %s by scripts/emit_earnings_calendar.py · "
        "cache refs/earnings-next-dates.json (run %s)"
    ) % (
        date,
        window.get("from"),
        window.get("to"),
        generated_at,
        cache.get("run"),
    )
    deviation_text = "; ".join(deviations) if deviations else "none"
    brief = (
        front_matter(date, generated_at, status)
        + provenance
        + "\n**Deviations:** "
        + deviation_text
        + "\n\n"
        + box_body
    )

    root = args.repo_root / "earnings-calendar"
    dated = root / date
    index_path = root / "_index.json"
    index = (
        load_json(index_path)
        if index_path.exists()
        else {
            "_schema": "earnings-calendar-index-v1",
            "updated": date,
            "runs": [],
        }
    )
    if not isinstance(index.get("runs"), list):
        raise ValueError("garbled earnings calendar index")

    runs = [run for run in index["runs"] if run.get("date") != date]
    runs.append({
        "date": date,
        "run_id": run_id,
        "status": status,
        "counts": {
            "rows": len(rows),
            "sa_confirmed": sa_confirmed,
            "core_rows": counts["core_rows"],
        },
        "window": window,
        "path": date + "/",
    })
    runs.sort(key=lambda run: run.get("date", ""))
    index = {
        "_schema": "earnings-calendar-index-v1",
        "updated": date,
        "runs": runs,
    }

    published = {
        "_schema": "earnings-next-dates-v2",
        "_published_at": generated_at,
        "_producer": PRODUCER,
        "_source": "Grok Bot box: shared-research/earnings-calendar/next-dates-cache.json",
    }
    published.update(cache)
    cache_text = json.dumps(
        published, indent=2, ensure_ascii=False, sort_keys=False
    ) + "\n"

    manifest = make_manifest(date, run_id, generated_at, window, counts, notes)
    history = update_history(root / "history.jsonl", date, rows)

    files = [
        dated / "_manifest.json",
        dated / "brief.md",
        dated / "calendar.json",
        dated / "calendar.csv",
        root / "history.jsonl",
        root / "_index.json",
        root / "latest.json",
        root / "latest.md",
        root / "latest.csv",
        args.repo_root / "refs/earnings-next-dates.json",
    ]

    if args.dry_run:
        print("planned files:")
        for path in files:
            print(path)
        print("counts: " + json.dumps(counts, sort_keys=True))
        return

    dated.mkdir(parents=True, exist_ok=True)
    write_text(dated / "_manifest.json", json_bytes(manifest))
    write_text(dated / "brief.md", brief)
    write_text(dated / "calendar.json", json_bytes(machine))
    write_text(dated / "calendar.csv", csv_text)
    write_text(root / "history.jsonl", history)
    write_text(root / "_index.json", json_bytes(index))
    write_text(args.repo_root / "refs/earnings-next-dates.json", cache_text)

    newest = max((run.get("date", "") for run in index["runs"]), default=date)
    if date >= newest:
        write_text(root / "latest.json", json_bytes(machine))
        write_text(root / "latest.md", brief)
        write_text(root / "latest.csv", csv_text)

    if cache.get("run") != date:
        print(
            "warning: cache run %r differs from run date %s" %
            (cache.get("run"), date),
            file=sys.stderr,
        )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("error: %s" % exc, file=sys.stderr)
        sys.exit(1)
