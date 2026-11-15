#!/usr/bin/env python3
"""Publish Grok Bot StockTwits crowd-sentiment scans.

Inputs are local core/general run JSON files, summary markdown files, and an
optional refs/watchlist.yaml. Outputs are the dated stocktwits-sentiment
family layout, including canonical JSON/CSV, brief, manifest, index, and
history. This script never fetches anything from the network.
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

SCHEMA = "stocktwits-sentiment-v1"
PRODUCER = "grok-bot/stocktwits-sentiment-scan"
TZ = dt.timezone(dt.timedelta(hours=7))
LABELS = ["EXTREMELY_BEARISH", "BEARISH", "NEUTRAL", "BULLISH", "EXTREMELY_BULLISH"]
VOL_LABELS = ["EXTREMELY_LOW", "LOW", "NORMAL", "HIGH", "EXTREMELY_HIGH"]
CSV_COLUMNS = [
    "list", "in_deep_set", "ticker", "tv_symbol", "sent_label", "sent_score",
    "bull_pct", "bear_pct", "vol_label", "vol_score", "vol_change_1d",
    "trending_rank", "watchers", "price", "prior_sent_label", "prior_sent_score",
    "notable", "material", "on_watchlist", "themes", "claims",
]


def fail(message, code=2):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(code)


def read_json(path):
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, ValueError) as exc:
        fail("cannot read JSON %s: %s" % (path, exc))
    if not isinstance(value, dict):
        fail("JSON root must be an object: %s" % path)
    return value


def parse_watchlist(path):
    if not path or not Path(path).exists():
        return set()
    values = set()
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        fail("cannot read watchlist %s: %s" % (path, exc))
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("tv_symbol:"):
            value = line.split(":", 1)[1].strip()
            if value.startswith("[") and value.endswith("]"):
                value = value[1:-1]
                values.update(x.strip().strip('"') for x in value.split(",") if x.strip())
            else:
                values.add(value.strip('"'))
        elif re.match(r"^-\s+tv_symbol\s*:", line):
            value = line.split(":", 1)[1].strip().strip('"')
            if value:
                values.add(value)
    return values


def clean_summary(text):
    removals = 0
    # Remove the exact account-bearing segment used by the source summaries.
    pattern = re.compile(r"(?:\*\*whoami:\*\*.*?)(?:\s+·\s+|$)", re.I)
    text, count = pattern.subn("", text)
    removals += count
    # Also remove plain whoami phrases, without touching unrelated prose.
    pattern = re.compile(r"\bwhoami\s+OK\s*\([^)]*\)", re.I)
    text, count = pattern.subn("", text)
    removals += count
    text = re.sub(r"^\s*·\s*", "", text, flags=re.M)
    return text.strip(), removals


def normalize_summary_headings(text):
    """Remove the copied summary's first H1 and demote its H2 headings."""
    lines = text.splitlines()
    first_h1_removed = False
    normalized = []
    for line in lines:
        if not first_h1_removed and re.match(r"^#\s+", line):
            first_h1_removed = True
            continue
        if re.match(r"^##\s+", line):
            line = "#" + line
        normalized.append(line)
    return "\n".join(normalized).strip()


def parse_general_prior(text):
    if not isinstance(text, str):
        return None, None, None, None
    sent = re.search(r"sent\s+(\S+)\s+(-?\d+(?:\.\d+)?)\s*->\s*(\S+)\s+(-?\d+(?:\.\d+)?)", text)
    vol = re.search(r"vol\s+(-?\d+(?:\.\d+)?)\s+(\S+)\s*->\s*(-?\d+(?:\.\d+)?)\s+(\S+)", text)
    return (
        sent.group(3) if sent else None,
        float(sent.group(4)) if sent else None,
        vol.group(4) if vol else None,
        float(vol.group(3)) if vol else None,
    )


def selected_symbol(selected, ticker):
    for item in selected or []:
        if isinstance(item, str) and item.split(":", 1)[-1] == ticker:
            return item
    return None


def in_selected_deep_set(selected, ticker):
    """Return whether ticker or its EXCHANGE:SYMBOL form occurs in selected."""
    ticker = str(ticker)
    bare = ticker.split(":", 1)[-1]
    for item in selected or []:
        if not isinstance(item, str):
            continue
        if item == ticker or item.split(":", 1)[-1] == bare:
            return True
    return False


def build_rows(name, data, watchlist):
    per = data.get("per_ticker")
    if not isinstance(per, dict):
        fail("%s JSON has no object per_ticker" % name)
    selected = data.get("selected") or []
    notable = data.get("notable_tickers") or []
    notable_why = data.get("notable_why")
    rows = []
    for ticker in sorted(per):
        item = per[ticker]
        if not isinstance(item, dict):
            continue
        if name == "core":
            tv = selected_symbol(selected, ticker)
            score = item.get("sent_score")
            prior = item.get("prior") if isinstance(item.get("prior"), dict) else {}
            row = {
                "list": "core", "in_deep_set": True, "ticker": ticker, "tv_symbol": tv,
                "sent_label": item.get("sent_label"), "sent_score": score,
                "bull_pct": item.get("bull_pct"), "bear_pct": item.get("bear_pct"),
                "vol_label": item.get("vol_label"), "vol_score": item.get("vol_score"),
                "vol_change_1d": item.get("vol_change_1d"),
                "vol_1d_label": item.get("vol_1d_label"), "vol_1d_score": item.get("vol_1d_score"),
                "trending_rank": item.get("trending_rank"), "watchers": item.get("watchers"),
                "price": item.get("price"), "price_change_pct": item.get("price_change_pct"),
                "price_time": item.get("price_time"),
                "prior_sent_label": prior.get("sent_label"), "prior_sent_score": prior.get("sent_score"),
                "prior_vol_label": prior.get("prior_vol_label"), "prior_vol_score": prior.get("prior_vol_score"),
                "vs_prior_text": None, "notable": ticker in notable,
                "notable_why": notable_why.get(ticker) if isinstance(notable_why, dict) else None,
                "material": None, "material_reason": None, "themes": [], "claims": [],
            }
        else:
            tv = item.get("full")
            prior_label, prior_score, prior_vol_label, prior_vol_score = parse_general_prior(item.get("vs_prior"))
            row = {
                "list": "general", "in_deep_set": in_selected_deep_set(selected, ticker),
                "ticker": ticker, "tv_symbol": tv,
                "sent_label": item.get("sent_label"), "sent_score": item.get("score"),
                "bull_pct": item.get("bull_pct"), "bear_pct": item.get("bear_pct"),
                "vol_label": item.get("vol_label"), "vol_score": item.get("vol_score"),
                "vol_change_1d": item.get("vol_change_1d"), "vol_1d_label": None,
                "vol_1d_score": None, "trending_rank": item.get("trending_rank"),
                "watchers": item.get("watchers"), "price": item.get("price"),
                "price_change_pct": None, "price_time": item.get("price_time"),
                "prior_sent_label": prior_label, "prior_sent_score": prior_score,
                "prior_vol_label": prior_vol_label, "prior_vol_score": prior_vol_score,
                "vs_prior_text": item.get("vs_prior"), "notable": item.get("notable"),
                "notable_why": None, "material": item.get("material"),
                "material_reason": item.get("material_reason"),
                "themes": item.get("themes") if isinstance(item.get("themes"), list) else [],
                "claims": item.get("claims") if isinstance(item.get("claims"), list) else [],
            }
        row["on_watchlist"] = bool(tv and tv in watchlist)
        rows.append(row)
    rows.sort(key=lambda row: (row["list"], -(row["sent_score"] if row["sent_score"] is not None else -1), row["ticker"]))
    return rows


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")


def csv_bytes(rows):
    import io
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=CSV_COLUMNS, lineterminator="\n", extrasaction="ignore")
    writer.writeheader()
    for row in rows:
        out = dict(row)
        out["themes"] = " | ".join(str(x) for x in (row.get("themes") or []))
        out["claims"] = " | ".join(str(x) for x in (row.get("claims") or []))
        for key in CSV_COLUMNS:
            if out.get(key) is None:
                out[key] = ""
            elif isinstance(out[key], bool):
                out[key] = "true" if out[key] else "false"
        writer.writerow(out)
    return output.getvalue().encode("utf-8")


def count_labels(rows):
    counts = {label: 0 for label in LABELS}
    for row in rows:
        if row.get("sent_label") in counts:
            counts[row["sent_label"]] += 1
    return counts


def make_lists(name, data):
    if name == "core":
        return {
            "ts_bkk": data.get("ts_bkk"), "path": data.get("path_used"), "quiet_ok": data.get("quiet_ok"),
            "selected_count": len(data.get("selected") or []),
            "trending_intersect": data.get("trending_intersect_core") or {},
            "notable_count": len(data.get("notable_tickers") or []),
        }
    return {
        "ts_bkk": data.get("ts_bkk"), "path": data.get("path"), "mode": data.get("mode"),
        "deep_n": data.get("deep_n"), "trending_intersect": data.get("trending_intersect") or [],
        "trending_board_top50": data.get("trending_board_top50") or [],
        "promoted_from_vol": data.get("promoted_from_vol") or [],
        "dropped_from_prior_deep": data.get("dropped_from_prior_deep") or [],
        "notable_count": data.get("notable_count", len(data.get("notable_tickers") or [])),
        "material_tickers": data.get("material_tickers") or [],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--core-json")
    parser.add_argument("--core-summary-md")
    parser.add_argument("--general-json")
    parser.add_argument("--general-summary-md")
    parser.add_argument("--watchlist", default="refs/watchlist.yaml")
    parser.add_argument("--out-dir", default="stocktwits-sentiment")
    parser.add_argument("--generated-at")
    parser.add_argument("--allow-stale", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        run_date = dt.date.fromisoformat(args.date)
    except ValueError:
        fail("--date must be YYYY-MM-DD")
    if not ((args.core_json and args.core_summary_md) or (args.general_json and args.general_summary_md)):
        fail("each supplied list requires its JSON and summary markdown pair")
    if args.core_json and not args.core_summary_md:
        fail("core JSON supplied without core summary markdown")
    if args.general_json and not args.general_summary_md:
        fail("general JSON supplied without general summary markdown")
    generated_at = args.generated_at or dt.datetime.now(TZ).isoformat(timespec="seconds")
    watchlist = parse_watchlist(args.watchlist)
    deviations = []
    inputs = {}
    summaries = {}
    removals = 0
    for name in ("core", "general"):
        json_path = getattr(args, name + "_json")
        md_path = getattr(args, name + "_summary_md")
        if not json_path:
            deviations.append("%s list was not supplied." % name.capitalize())
            continue
        data = read_json(json_path)
        ts = data.get("ts_bkk")
        if not isinstance(ts, str) or not ts[:10] == args.date:
            if not args.allow_stale:
                fail("%s input ts_bkk date does not equal --date" % name)
            deviations.append("%s input ts_bkk date is stale for %s." % (name.capitalize(), args.date))
        try:
            summary = Path(md_path).read_text(encoding="utf-8")
        except OSError as exc:
            fail("cannot read summary %s: %s" % (md_path, exc))
        summary, count = clean_summary(summary)
        summary = normalize_summary_headings(summary)
        removals += count
        inputs[name] = data
        summaries[name] = summary
    rows = []
    for name in ("core", "general"):
        if name in inputs:
            rows.extend(build_rows(name, inputs[name], watchlist))
    rows.sort(key=lambda row: (row["list"], -(row["sent_score"] if row["sent_score"] is not None else -1), row["ticker"]))
    status = "degraded" if deviations else "ok"
    lists = {name: make_lists(name, inputs[name]) for name in ("core", "general") if name in inputs}
    counts = {
        "rows": len(rows), "by_list": {name: sum(1 for row in rows if row["list"] == name) for name in ("core", "general")},
        "notable": sum(1 for row in rows if row.get("notable") is True),
        "material": sum(1 for row in rows if row.get("material") is True),
        "on_watchlist": sum(1 for row in rows if row.get("on_watchlist") is True),
        "by_label": count_labels(rows),
        "general_deep_set": sum(1 for row in rows if row["list"] == "general" and row.get("in_deep_set") is True),
    }
    payload = {"_schema": SCHEMA, "date": args.date, "timezone": "Asia/Bangkok", "producer": PRODUCER,
               "run_id": args.date + "Tdaily", "status": status, "lists": lists, "counts": counts, "rows": rows}
    out = Path(args.out_dir)
    dated = out / args.date
    planned = ["_manifest.json", "brief.md", "sentiment.json", "sentiment.csv"]
    if args.dry_run:
        print("\n".join(planned))
        print(json.dumps(counts, sort_keys=True))
        return
    out.mkdir(parents=True, exist_ok=True)
    dated.mkdir(parents=True, exist_ok=True)
    (dated / "sentiment.json").write_bytes(json_bytes(payload))
    (dated / "sentiment.csv").write_bytes(csv_bytes(rows))
    core_ts = inputs.get("core", {}).get("ts_bkk", "n/a")
    general_ts = inputs.get("general", {}).get("ts_bkk", "n/a")
    provenance = (
        "**Provenance:** StockTwits MCP via Grok Bot (core run %s, general run %s) · built %s "
        "by scripts/emit_stocktwits_sentiment.py · covers %s (Asia/Bangkok)"
        % (core_ts, general_ts, generated_at, args.date)
    )
    manifest_provenance = provenance[2:]
    brief = [
        "---",
        "date: " + args.date,
        "producer: " + PRODUCER,
        "contract: " + SCHEMA,
        'source: "Grok Bot box: StockTwits MCP scans by the Portfolio analyst agent (core + general lists)"',
        "generated_at: " + generated_at,
        "status: " + status,
        "---",
        "",
        "# StockTwits sentiment — %s (Asia/Bangkok)" % args.date,
        "",
        provenance,
        "",
        "## Deviations / degraded paths",
        "",
    ]
    brief += ["- " + item for item in deviations] if deviations else ["- none"]
    for name in ("core", "general"):
        brief += ["", "## " + ("Core list" if name == "core" else "General list"), ""]
        if name in summaries:
            brief.append(summaries[name])
        else:
            brief.append("Not supplied.")
    brief += [
        "",
        "## Coverage",
        "",
        "The published rows contain %d normalized ticker rows: %d core and %d general."
        % (len(rows), counts["by_list"]["core"], counts["by_list"]["general"]),
        "Crowd sentiment and claims describe StockTwits posts and are not independently verified facts.",
    ]
    (dated / "brief.md").write_text("\n".join(brief).rstrip() + "\n", encoding="utf-8")
    manifest = {
        "_schema": "stocktwits-sentiment-manifest-v1",
        "date": args.date,
        "producer": PRODUCER,
        "run_id": args.date + "Tdaily",
        "generated_at": generated_at,
        "provenance": manifest_provenance,
        "canonical": {"brief": "brief.md", "machine": ["sentiment.json", "sentiment.csv"]},
        "files": [
            {"name": "brief.md", "role": "brief"},
            {"name": "sentiment.json", "role": "machine"},
            {"name": "sentiment.csv", "role": "table"},
            {"name": "_manifest.json", "role": "provenance"},
        ],
        "counts": counts,
        "notes": ["StockTwits account identity and MCP notes were removed."]
        + (["Removed %d account identity segment(s) from supplied summaries." % removals] if removals else [])
        + deviations,
    }
    (dated / "_manifest.json").write_bytes(json_bytes(manifest))
    # Replace the dated directory's history contribution while retaining prior dates.
    history = out / "history.jsonl"
    existing = []
    if history.exists():
        for line in history.read_text(encoding="utf-8").splitlines():
            try:
                obj = json.loads(line)
            except ValueError:
                fail("garbled history.jsonl")
            if obj.get("date") != args.date:
                existing.append(obj)
    for row in rows:
        existing.append({
            "date": args.date,
            "list": row["list"],
            "ticker": row["ticker"],
            "sent_label": row["sent_label"],
            "sent_score": row["sent_score"],
            "vol_label": row["vol_label"],
            "vol_score": row["vol_score"],
            "trending_rank": row["trending_rank"],
            "notable": row.get("notable"),
        })
    existing.sort(key=lambda obj: (obj.get("date", ""), obj.get("list", ""), obj.get("ticker", "")))
    history.write_text(
        "".join(json.dumps(obj, ensure_ascii=False, sort_keys=True) + "\n" for obj in existing),
        encoding="utf-8",
    )
    index_path = out / "_index.json"
    index = {"_schema": "stocktwits-sentiment-index-v1", "updated": args.date, "runs": []}
    if index_path.exists():
        try:
            old = json.loads(index_path.read_text(encoding="utf-8"))
            index["runs"] = [r for r in old.get("runs", []) if r.get("date") != args.date]
        except (OSError, ValueError) as exc:
            fail("cannot read _index.json: %s" % exc)
    index["runs"].append({
        "date": args.date,
        "run_id": args.date + "Tdaily",
        "status": status,
        "counts": {
            "rows": len(rows),
            "notable": counts["notable"],
            "material": counts["material"],
        },
        "path": args.date + "/",
    })
    index["runs"].sort(key=lambda r: r.get("date", ""))
    index_path.write_bytes(json_bytes(index))
    for source, target in (("sentiment.json", "latest.json"), ("brief.md", "latest.md"), ("sentiment.csv", "latest.csv")):
        (out / target).write_bytes((dated / source).read_bytes())


if __name__ == "__main__":
    main()
