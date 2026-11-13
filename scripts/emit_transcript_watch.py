#!/usr/bin/env python3
"""Publish the public weekly transcript-watch digest and short briefs."""

import argparse
import csv
import io
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

PRODUCER = "grok-bot/weekly-transcript-watch"
CONTRACT = "transcript-watch-v1"
BANGKOK = timezone(timedelta(hours=7))
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SUMMARY_LINK_RE = re.compile(
    r"\[([^\]]*)\]\((/home/box/[^)\s]*?/summaries/(\d{4}-\d{2}-\d{2}-[^)\s]+)\.md)\)"
)
CODE_FILE_RE = re.compile(r"`([^`\n]+\.(?:md|csv|json|jsonl|yaml|py))`", re.IGNORECASE)


def fail(message, code=2):
    raise SystemExit(message if code == 2 else f"error: {message}")


def read_text(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"cannot read {path}: {exc}")


def read_json(path):
    text = read_text(path)
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        fail(f"garbled JSON in {path}: {exc}")
    if not isinstance(value, dict):
        fail(f"expected a JSON object in {path}")
    return value


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def yaml_string(value):
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def front_matter(fields):
    lines = ["---"]
    for key, value in fields:
        lines.append(f"{key}: null" if value is None else f"{key}: {yaml_string(value)}")
    lines.append("---")
    return "\n".join(lines)


def parse_date(value):
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        fail(f"invalid date {value!r}; expected YYYY-MM-DD")
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        fail(f"invalid date {value!r}: {exc}")
    return value


def parse_generated_at(value):
    if value is None:
        return datetime.now(BANGKOK).replace(microsecond=0).isoformat()
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as exc:
        fail(f"invalid --generated-at value {value!r}: {exc}")
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=BANGKOK)
    return parsed.astimezone(BANGKOK).replace(microsecond=0).isoformat()


def parse_inline_list(value):
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        fail(f"unsupported watchlist list value: {value}")
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [part.strip().strip('"').strip("'") for part in inner.split(",") if part.strip()]


def _unquote_watchlist_value(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        value = value[1:-1]
    return value.strip()


def _read_watchlist_data(path):
    """Read watchlist data without assuming a particular YAML structure.

    The returned tuple contains the canonical symbol set and the subset of
    legacy v1 ticker values found under the top-level ``watchlist`` key.
    """
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError:
        return set(), set()

    symbols = set()
    v1_tickers = set()
    in_top_level_watchlist = False

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        # A top-level key ends the scope of the top-level watchlist section.
        if line and not line[0].isspace():
            stripped = line.strip()
            key = stripped.split(":", 1)[0].strip() if ":" in stripped else ""
            in_top_level_watchlist = key == "watchlist"
            if ":" not in stripped:
                continue
            value = stripped.split(":", 1)[1].strip()
            if key in ("tv_symbol", "us_symbol"):
                value = _unquote_watchlist_value(value)
                if value:
                    symbols.add(value.upper())
            continue

        # Ignore malformed or unsupported structures rather than failing the
        # entire run. Key/value pairs are intentionally permissive.
        match = re.search(r"(?:^|-\s+)([A-Za-z_][\w-]*)\s*:\s*(.*?)\s*$", line)
        if not match:
            continue
        key = match.group(1).strip().lower()
        value = _unquote_watchlist_value(match.group(2))
        if key in ("tv_symbol", "us_symbol"):
            if value:
                symbols.add(value.upper())
        elif key == "ticker" and in_top_level_watchlist and value:
            symbols.add(value.upper())
            v1_tickers.add(value.upper())

    return symbols, v1_tickers


def parse_watchlist(path):
    """Return all known watchlist symbols.

    This reader is deliberately tolerant of unknown YAML structures. Missing
    or unreadable files simply produce an empty set.
    """
    symbols, _ = _read_watchlist_data(path)
    return symbols


def parse_v1_tickers(path):
    """Return ticker values found under the top-level watchlist key."""
    _, tickers = _read_watchlist_data(path)
    return tickers


def windows_slug(value):
    slug = re.sub(r"[-_. ]+", "-", re.sub(r"[^a-z0-9._-]+", "-", value.lower())).strip("-. ")
    if not slug:
        fail("summary slug is empty after sanitization")
    return slug


def summary_slug(path_value):
    match = re.fullmatch(
        r"\d{4}-\d{2}-\d{2}-(.+)\.md", Path(path_value).name, re.IGNORECASE
    )
    if not match:
        fail(f"box summary filename does not match the dated-slug shape: {Path(path_value).name}")
    return windows_slug(match.group(1))


def find_summary_file(summaries_dir, item, digest):
    summary_path = item.get("summary")
    if not isinstance(summary_path, str) or not summary_path:
        return None
    name = Path(summary_path).name
    candidate = Path(summaries_dir) / name
    if candidate.is_file():
        return candidate
    for path in sorted(Path(summaries_dir).glob("*.md")):
        if path.name == name:
            return path
    if any(Path(match.group(2)).name == name for match in SUMMARY_LINK_RE.finditer(digest)):
        fail(f"summary file for {name} was not found in {summaries_dir}")
    return None


def meta_model(summary_file):
    for candidate in (
        summary_file.with_name(summary_file.name + ".meta.json"),
        summary_file.with_name(summary_file.stem + ".meta.json"),
    ):
        if candidate.is_file():
            meta = read_json(candidate)
            model = meta.get("model")
            return str(model) if model is not None else ""
    return ""


def extract_summary(text, source_url):
    lines = text.replace("\r\n", "\n").splitlines()
    if lines and lines[0].strip() == "SUMMARY":
        lines = lines[1:]
    h1 = ""
    tl_heading = ""
    bullets = []
    section = None
    for line in lines:
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            section = heading.group(1).strip()
            if re.match(r"^TL;DR\b", section, re.IGNORECASE):
                tl_heading = line
            continue
        if re.match(r"^#\s+", line) and not h1:
            h1 = line
            continue
        if section and re.match(r"^TL;DR\b", section, re.IGNORECASE):
            if re.match(r"^-\s+", line):
                bullets.append(re.sub(r"^-\s+", "", line).rstrip())
    if not h1:
        fail(f"box summary has no H1 heading: {source_url}")
    if not tl_heading:
        return h1, "", [], True
    return h1, "\n".join([tl_heading] + [f"- {bullet}" for bullet in bullets]), bullets, False


def rewrite_digest(digest, emitted, repo_root):
    def replace_summary_link(match):
        slug = emitted.get(Path(match.group(2)).name)
        return f"[{match.group(1)}]({slug})" if slug else match.group(1)

    rewritten = SUMMARY_LINK_RE.sub(replace_summary_link, digest)

    def unbacktick(match):
        token = match.group(1)
        relative = token.replace("\\", "/")
        candidates = [repo_root / relative]
        if relative.startswith(str(repo_root) + "/"):
            candidates.append(Path(relative))
        return match.group(0) if any(candidate.exists() for candidate in candidates) else token

    return CODE_FILE_RE.sub(unbacktick, rewritten)


def csv_bytes(headers, rows):
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(headers)
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def transcript_sort_key(item, auto_position):
    briefed = bool(item.get("briefed"))
    if briefed:
        return (
            0,
            auto_position.get(item["ticker"], len(auto_position)),
            item["date"],
            item["ticker"],
            item["title"],
        )
    return (1, item["date"], item["ticker"], item["title"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True)
    parser.add_argument("--digest-md", required=True)
    parser.add_argument("--last-run-json", required=True)
    parser.add_argument("--summaries-dir", required=True)
    parser.add_argument("--watchlist", default="refs/watchlist.yaml")
    parser.add_argument("--out-dir", default="transcript-watch")
    parser.add_argument("--generated-at")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_date = parse_date(args.date)
    generated_at = parse_generated_at(args.generated_at)
    last_run = read_json(args.last_run_json)
    if last_run.get("run_date_bkk") != run_date:
        fail(
            f"last-run.json run_date_bkk is {last_run.get('run_date_bkk')!r}, "
            f"but --date is {run_date!r}"
        )
    digest = read_text(args.digest_md).replace("\r\n", "\n")
    if not digest.lstrip().startswith("# "):
        fail(f"digest does not begin with an H1 heading: {args.digest_md}")
    lookback = last_run.get("lookback")
    if not isinstance(lookback, list) or len(lookback) != 2:
        fail("last-run.json lookback must be a two-element list")
    items = last_run.get("new_transcripts")
    if not isinstance(items, list):
        fail("last-run.json new_transcripts must be a list")
    auto_briefed = last_run.get("auto_briefed")
    if not isinstance(auto_briefed, list):
        fail("last-run.json auto_briefed must be a list")
    for item in items:
        if not isinstance(item, dict):
            fail("last-run.json new_transcripts contains a non-object item")
        for field in ("ticker", "date", "title", "url"):
            if not isinstance(item.get(field), str) or not item[field]:
                fail(f"transcript item is missing {field}")
        parse_date(item["date"])

    watchlist = set(parse_watchlist(args.watchlist))
    v1_tickers = set(parse_v1_tickers(args.watchlist))
    watchlist_unavailable = not watchlist
    auto_position = {ticker: index for index, ticker in enumerate(auto_briefed)}
    ordered = sorted(items, key=lambda item: transcript_sort_key(item, auto_position))

    summaries_dir = Path(args.summaries_dir)
    if not summaries_dir.is_dir():
        fail(f"summaries directory does not exist: {summaries_dir}")

    emitted = {}
    brief_contents = {}
    tldrs = {}
    missing_tldr = []
    degraded_notes = []
    used_slugs = {}
    item_briefs = {}

    for item in ordered:
        if not item.get("briefed"):
            item_briefs[id(item)] = (None, [], False)
            continue
        summary_file = find_summary_file(summaries_dir, item, digest)
        if summary_file is None:
            item_briefs[id(item)] = (None, [], False)
            summary_name = item.get("summary") or "unknown summary"
            degraded_notes.append(
                f"{item['ticker']} ({item['title']}) was marked briefed but its summary file is missing: {summary_name}."
            )
            continue
        slug = summary_slug(summary_file.name)
        if slug in used_slugs and used_slugs[slug] != summary_file.name:
            fail(f"summary slug collision for {slug}")
        used_slugs[slug] = summary_file.name
        text = read_text(summary_file)
        h1, tl_body, bullets, no_tldr = extract_summary(text, item["url"])
        model = meta_model(summary_file)
        fields = [
            ("date", run_date), ("producer", PRODUCER), ("contract", CONTRACT),
            ("ticker", item["ticker"]), ("title", item["title"]),
            ("transcript_date", item["date"]), ("source_url", item["url"]),
            ("model", model), ("status", "ok"),
        ]
        parts = [front_matter(fields), "", h1, ""]
        if tl_body:
            parts.extend([tl_body, ""])
        parts.append(
            f"Source transcript: {item['url']} (StockAnalysis). "
            "Full summary kept on the Grok box; not published here."
        )
        brief_contents[slug] = "\n".join(parts).rstrip() + "\n"
        emitted[summary_file.name] = slug
        tldrs[id(item)] = bullets
        item_briefs[id(item)] = (f"summary-{slug}.md", bullets, no_tldr)
        if no_tldr:
            missing_tldr.append(summary_file.name)

    repo_root = Path(__file__).resolve().parent.parent
    rewritten_digest = rewrite_digest(digest, emitted, repo_root).strip()
    provenance = (
        f"Source: Grok Bot box archive {args.digest_md} "
        f"(StockAnalysis transcript pages and shared earnings cache); "
        f"built {generated_at}; covered session {lookback[0]} through {lookback[1]}."
    )
    deviations = []
    if missing_tldr:
        deviations.extend(
            f"{name} has no TL;DR section; only its H1 and source line were published."
            for name in missing_tldr
        )
    deviations.extend(degraded_notes)
    if not deviations:
        deviations = ["none"]

    brief_md = "\n".join([
        front_matter([
            ("date", run_date), ("producer", PRODUCER), ("contract", CONTRACT),
            ("source", f"Grok Bot box archive {args.digest_md} (StockAnalysis)"),
            ("generated_at", generated_at),
            ("status", "degraded" if missing_tldr or degraded_notes else "ok"),
        ]),
        "", provenance, "", "## Deviations / degraded paths", "",
        *[f"- {line}" for line in deviations], "", rewritten_digest, "",
    ])

    by_tag = {}
    transcript_rows = []
    core_items = 0
    on_watchlist_count = 0
    for rank, item in enumerate(ordered, 1):
        ticker = item["ticker"]
        tag = item.get("tag") or ""
        core = bool(item.get("core"))
        brief_file, bullets, _ = item_briefs[id(item)]
        if watchlist_unavailable:
            watchlisted = None
        else:
            symbol = ticker.split(":", 1)[-1]
            watchlisted = ticker.upper() in watchlist or symbol.upper() in v1_tickers
        by_tag[tag] = by_tag.get(tag, 0) + 1
        core_items += int(core)
        if watchlisted is not None:
            on_watchlist_count += int(watchlisted)
        transcript_rows.append({
            "rank": rank, "ticker": ticker, "symbol": ticker.split(":", 1)[-1],
            "date": item["date"], "title": item["title"], "tag": tag,
            "url": item["url"], "core": core, "briefed": bool(item.get("briefed")),
            "brief_file": brief_file, "tldr": bullets, "on_watchlist": watchlisted,
        })

    counts = {
        "new_transcripts": len(transcript_rows),
        "auto_briefed": sum(1 for row in transcript_rows if row["briefed"]),
        "core_items": core_items, "by_tag": dict(sorted(by_tag.items())),
        "on_watchlist": None if watchlist_unavailable else on_watchlist_count,
    }
    status = "degraded" if missing_tldr or degraded_notes else "ok"
    machine = {
        "_schema": CONTRACT, "run_date": run_date, "timezone": "Asia/Bangkok",
        "producer": PRODUCER, "run_id": f"{run_date}Tweekly", "status": status,
        "lookback": lookback, "sweep": last_run.get("sweep"),
        "tv_calls": last_run.get("tv_calls"), "counts": counts,
        "transcripts": transcript_rows, "core_status": last_run.get("core_status"),
        "notes": last_run.get("notes"),
    }
    csv_rows = [
        [row["rank"], row["ticker"], row["date"], row["title"], row["tag"],
         str(row["core"]).lower(), str(row["briefed"]).lower(), row["brief_file"] or "",
         row["url"], "" if row["on_watchlist"] is None else str(row["on_watchlist"]).lower()]
        for row in transcript_rows
    ]
    transcripts_csv = csv_bytes(
        ["rank", "ticker", "date", "title", "tag", "core", "briefed", "brief_file", "url", "on_watchlist"],
        csv_rows,
    )

    out_root = Path(args.out_dir)
    dated = out_root / run_date
    files = {
        "brief.md": brief_md.encode("utf-8"),
        "transcripts.json": json_bytes(machine),
        "transcripts.csv": transcripts_csv,
    }
    for slug, content in brief_contents.items():
        files[f"summary-{slug}.md"] = content.encode("utf-8")

    manifest = {
        "_schema": "transcript-watch-manifest-v1", "date": run_date,
        "producer": PRODUCER, "run_id": f"{run_date}Tweekly",
        "generated_at": generated_at, "provenance": provenance,
        "canonical": {"brief": "brief.md", "machine": ["transcripts.json"]},
        "files": [], "counts": counts, "notes": deviations,
    }
    if watchlist_unavailable:
        manifest["notes"].append("watchlist unavailable")
    roles = {
        "brief.md": "public weekly digest",
        "transcripts.json": "canonical machine data",
        "transcripts.csv": "tabular transcript index",
    }
    for slug in brief_contents:
        roles[f"summary-{slug}.md"] = "short public brief"
    for name in sorted(files):
        manifest["files"].append({"name": name, "role": roles[name]})
    manifest["files"].append({"name": "_manifest.json", "role": "provenance"})
    manifest["files"].sort(key=lambda item: item["name"])
    files["_manifest.json"] = json_bytes(manifest)

    history_entries = []
    history_path = out_root / "history.jsonl"
    if history_path.exists():
        for number, line in enumerate(read_text(history_path).splitlines(), 1):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as exc:
                fail(f"garbled history.jsonl at line {number}: {exc}")
            if entry.get("run_date") != run_date:
                history_entries.append(entry)
    for row in transcript_rows:
        history_entries.append({
            "run_date": run_date, "ticker": row["ticker"], "date": row["date"],
            "title": row["title"], "tag": row["tag"], "core": row["core"],
            "briefed": row["briefed"], "url": row["url"],
        })
    history_entries.sort(key=lambda entry: (str(entry.get("run_date") or ""), str(entry.get("url") or "")))
    history_text = "".join(
        json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n" for entry in history_entries
    )

    index_path = out_root / "_index.json"
    runs = []
    if index_path.exists():
        old_runs = read_json(index_path).get("runs", [])
        if not isinstance(old_runs, list):
            fail("existing _index.json runs must be a list")
        runs = [entry for entry in old_runs if entry.get("date") != run_date]
    runs.append({
        "date": run_date, "run_id": f"{run_date}Tweekly", "status": status,
        "counts": counts, "path": f"{run_date}/",
    })
    runs.sort(key=lambda entry: entry.get("date", ""))
    index_data = {"_schema": "transcript-watch-index-v1", "updated": run_date, "runs": runs}

    planned = [str(dated / name) for name in sorted(files)]
    planned.extend([
        str(out_root / "latest.json"), str(out_root / "latest.md"),
        str(out_root / "latest.csv"), str(history_path), str(index_path),
    ])
    if args.dry_run:
        print(json.dumps({
            "run_date": run_date, "status": status, "counts": counts, "files": planned,
        }, indent=2, ensure_ascii=False))
        return

    dated.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (dated / name).write_bytes(content)
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "latest.json").write_bytes(files["transcripts.json"])
    (out_root / "latest.md").write_bytes(files["brief.md"])
    (out_root / "latest.csv").write_bytes(files["transcripts.csv"])
    history_path.write_text(history_text, encoding="utf-8", newline="")
    index_path.write_bytes(json_bytes(index_data))


if __name__ == "__main__":
    main()
