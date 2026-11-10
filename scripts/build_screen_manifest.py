#!/usr/bin/env python3
"""Generate a `_manifest.json` for every dated directory under daily-screens/.

Why: a dated screen directory does not carry a fixed file set. 2026-10-19 ran with
every screen empty, 2026-10-22 split stockbee into three components with no aggregate,
2026-10-26 and 2026-10-27 carried an aggregate *plus* components, and 2026-10-28 onward
carried the aggregate alone. A consumer that globs `daily-screens/*/stockbee.csv`
therefore misses 2026-10-22 entirely and can double-count 2026-10-26/27.

The manifest states, per directory: which file is the brief, which are machine artifacts,
which screens are present, whether each screen has a matching .csv, and which screens are
split into components. `international-eod/<date>/_manifest.json` already works this way.

Everything here is read from files that exist. Nothing is inferred about content.

  python3 scripts/build_screen_manifest.py            # write the manifests
  python3 scripts/build_screen_manifest.py --check    # report drift, write nothing
"""
import csv
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENS_ROOT = os.path.join(REPO, "daily-screens")

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Screen stems the routine publishes. Anything else in a dated directory is a
# machine artifact, a brief, or a component of one of these.
SCREEN_STEMS = {
    "focus": "convergence tier - >=2 stylists",
    "master": "deduped union of all branches, capped",
    "stalk": "master intersect near 20/50-DMA",
    "tier-a": "convergence tier - >=3 stylists",
    "stockbee": "Bonde stylist screen",
    "qullamaggie": "Qullamaggie stylist screen",
    "jeff-sun": "Sun CANSLIM screen",
    "peoplewish": "peoplewish ADR/velocity screen",
    "ariel-hernandez": "Hernandez theme funnel",
    "short-candidates": "parabolic short candidates",
    "long-reversal-candidates": "parabolic long candidates",
    "pre-market-gapper": "pre-market gapper (cron #08)",
    "focus-rvol-snapshot": "intraday RVOL re-rank (cron #07)",
    "volume-breakout": "KSE volume-breakout cross-check",
    "breadth": "breadth + regime detail (cron #09)",
    "breadth-snapshot": "intraday breadth snapshot (cron #10)",
    "catalysts": "sourced catalyst attribution",
    "high-short-float": "weekly high-short-float refresh",
    "ipo": "weekly IPO refresh",
    "weekly-ipo": "weekly IPO refresh (pattern-study cron)",
    "reversal-bullish-3_55": "Bonde reversal-bullish scan (cron #04)",
}

# Files that are never screens, whatever they are called.
RESERVED = {
    "daily-sweep.md": "the narrative brief",
    "_summary.md": "machine digest of the brief",
    "_results.json": "full candidate pool + screen coverage",
    "_regime.json": "regime flags and their inputs",
    "_regime-screener.json": "regime flags, screener source",
    "_regime-intraday.json": "regime flags, intraday source",
    "_cache.json": "upstream cache",
    "_premarket-pull.json": "raw pre-market pull",
    "_breadth_raw.json": "raw breadth input",
    "_source-health.json": "substitutions and unavailable fields",
    "_manifest.json": "this file",
}

BRIEF_EXTRA = {"reversal-bullish-3_55-CORRECTION"}


def classify(names):
    """Split a directory's filenames into screens, components and machine artifacts."""
    screens = {}
    components = {}
    artifacts = {}

    for n in sorted(names):
        if n in RESERVED:
            artifacts[n] = RESERVED[n]
            continue
        stem, ext = os.path.splitext(n)
        if stem in BRIEF_EXTRA:
            artifacts[n] = "correction to a sibling artifact"
            continue
        if stem in SCREEN_STEMS:
            screens.setdefault(stem, {"files": [], "components": []})["files"].append(n)
            continue
        # A component is "<screen>_<qualifier>" where <screen> is a known stem.
        base = None
        for s in SCREEN_STEMS:
            if stem.startswith(s + "_"):
                base = s
                break
        if base:
            components.setdefault(base, []).append(n)
            continue
        artifacts[n] = "unclassified"

    for base, files in components.items():
        entry = screens.setdefault(base, {"files": [], "components": []})
        entry["components"] = sorted(files)
        if not entry["files"]:
            entry["files"] = []
    return screens, components, artifacts


def describe_screens(screens):
    out = {}
    for stem, entry in sorted(screens.items()):
        files = sorted(entry["files"])
        comps = sorted(entry.get("components", []))
        has_md = any(f.endswith(".md") for f in files)
        has_csv = any(f.endswith(".csv") for f in files)
        note = []
        if has_md and not has_csv:
            note.append("no .csv for this screen")
        if not has_md and has_csv:
            note.append("no .md for this screen")
        if comps:
            note.append("split into %d component file(s)" % len(comps))
        out[stem] = {
            "role": SCREEN_STEMS.get(stem, "component"),
            "files": files,
            "components": comps,
            "paired": has_md and has_csv,
            "note": "; ".join(note) if note else None,
        }
    return out


ISO_DATE_RE = re.compile(r"(20\d{2})-(\d{2})-(\d{2})")
SHORT_DATE_RE = re.compile(r"_(\d{2})_?(\d{2})(?![0-9])")


def dated_columns(path):
    """The dates named in a CSV's column headers, oldest first.

    The board schemas carry the session in the column name, in three spellings
    across the archive: `close_2026-10-30`, `close_1027` and `close_10_28`.
    All three name the SCREEN session FIRST and the observation session second,
    so the earliest is the screen session.
    """
    rows = []
    try:
        with open(path, encoding="utf-8-sig", newline="") as fh:
            header = next(csv.reader(fh))
    except (OSError, StopIteration, csv.Error):
        return rows
    for col in header:
        m = ISO_DATE_RE.search(col)
        if m:
            rows.append(m.group(0))
            continue
        m = SHORT_DATE_RE.search(col)
        if m:
            rows.append("%s-%s" % (m.group(1), m.group(2)))
    return rows


def last_settled_session(date):
    """The most recent session `us-eod/` published before `date`.

    The repo's own record of which days the US market was open. A screen run on
    session S describes S's settled tape, so the screen session for a directory
    dated D is the last session before D.

    This is the weakest of the four sources - it infers the session rather than
    reading it - so it is recorded as such and the manifest names it.
    """
    sessions = []
    for name in os.listdir(os.path.join(REPO, "us-eod")):
        if not name.endswith(".csv"):
            continue
        stem = name[:-4]
        if re.match(r"^\d{4}-\d{2}-\d{2}$", stem) and stem < date:
            sessions.append(stem)
    return max(sessions) if sessions else None


def derive_screen_session(date_dir, date, screens):
    """Which session this directory's screen metrics describe, and how we know.

    Three sources, in order of authority:
      1. `_results.json` / `_decisions.json` - the routine states it outright.
      2. a `data_date` column in the board CSVs - the current schema's own
         record of the session the metrics resolve to.
      3. the oldest date-stamped column in the board CSVs - the screen session
         is named before the observation session, so the earliest is the one.

    Returns (session_date, source). A session of None means this directory's
    own files do not say, and the manifest says so rather than guessing.
    """
    for name in ("_results.json", "_decisions.json"):
        path = os.path.join(date_dir, name)
        if not os.path.exists(path):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                value = json.load(fh).get("data_as_of")
        except (OSError, ValueError):
            value = None
        if value:
            return value, "%s.data_as_of" % name

    board_paths = []
    for stem, entry in sorted(screens.items()):
        for fname in entry.get("files", []):
            if fname.endswith(".csv"):
                board_paths.append(os.path.join(date_dir, fname))
    for path in board_paths:
        rows = J.read_csv_rows(path)
        if not rows:
            continue
        for col in rows[0].keys():
            if col.strip().lower() in ("data_date", "screen_date", "session_date"):
                value = J.strip_md(rows[0].get(col))
                if re.match(r"^\d{4}-\d{2}-\d{2}$", value):
                    return value, "%s.%s" % (os.path.basename(path), col)

    dates_seen = []
    for path in board_paths:
        dates_seen.extend(dated_columns(path))
    if dates_seen:
        resolved = []
        for value in dates_seen:
            if re.match(r"^20\d{2}-\d{2}-\d{2}$", value):
                resolved.append(value)
            else:
                mm, dd = value.split("-")
                for year in (date[:4], str(int(date[:4]) - 1)):
                    cand = "%s-%s-%s" % (year, mm, dd)
                    try:
                        datetime.date.fromisoformat(cand)
                    except ValueError:
                        continue
                    resolved.append(cand)
                    break
        if resolved:
            return min(resolved), "the oldest date-stamped column in the board CSVs"

    fallback = last_settled_session(date)
    if fallback:
        return fallback, ("the last settled session in us-eod/ before this date "
                          "(inferred, not read)")

    return None, None


def build(date_dir, date):
    names = [n for n in os.listdir(date_dir) if os.path.isfile(os.path.join(date_dir, n))]
    screens, components, artifacts = classify(names)
    described = describe_screens(screens)

    data_as_of, lag_source = derive_screen_session(date_dir, date, described)

    lag = None
    if data_as_of:
        try:
            lag = (datetime.date.fromisoformat(date)
                   - datetime.date.fromisoformat(data_as_of)).days
        except ValueError:
            lag = None

    # The same lag counted in SESSIONS rather than calendar days. A Monday's
    # screen is three calendar days behind but ONE session behind, and reading
    # "3" as three sessions would be wrong by a factor of three.
    sessions = None
    if data_as_of:
        published = sorted(
            n[:-4] for n in os.listdir(os.path.join(REPO, "us-eod"))
            if n.endswith(".csv") and re.match(r"^\d{4}-\d{2}-\d{2}$", n[:-4])
        )
        between = [s for s in published if data_as_of < s <= date]
        if between:
            sessions = len(between)

    files = []
    for n in sorted(names):
        if n == "_manifest.json":
            continue
        stem = os.path.splitext(n)[0]
        role = None
        if stem in described:
            role = described[stem]["role"]
        else:
            # A component file belongs to its parent screen.
            for base, entry in described.items():
                if n in entry["components"]:
                    role = "%s component" % entry["role"]
                    break
        files.append({
            "name": n,
            "bytes": os.path.getsize(os.path.join(date_dir, n)),
            "role": role or artifacts.get(n),
        })

    notes = []
    if lag is not None and lag != 0:
        extra = ""
        if sessions is not None and sessions != lag:
            extra = (" (%d trading session(s) - the calendar gap includes a weekend)"
                     % sessions)
        notes.append(
            "screen metrics describe the %s session (%d day(s)%s before this directory's "
            "date); the 'today' columns are the %s settled close"
            % (data_as_of, lag, extra, date)
        )
    elif data_as_of is None and any(n.endswith(".csv") for n in names):
        notes.append(
            "the session these screen metrics describe is NOT derivable from this "
            "directory: no _results.json, no data_date column, no date-stamped "
            "column, and no us-eod/ session published before this date to infer it "
            "from. The 'today' columns are the %s settled close." % date
        )
    for stem, entry in described.items():
        if entry["components"]:
            notes.append(
                "%s is published as %d component file(s) with no aggregate - a consumer "
                "globbing %s.csv will not see it" % (stem, len(entry["components"]), stem)
            )
        if not entry["paired"] and entry["files"]:
            notes.append("%s has no matching .csv in this directory" % stem)
    if "_source-health.json" not in names:
        notes.append(
            "no _source-health.json - source health for this run exists only in the "
            "prose table in daily-sweep.md"
        )

    return {
        "_schema": "daily-screens-manifest-v1",
        "date": date,
        "data_as_of": data_as_of,
        "session_lag_days": lag,
        "session_lag_sessions": sessions,
        "session_lag_source": lag_source,
        "canonical": {
            "brief": "daily-sweep.md" if "daily-sweep.md" in names else None,
            "summary": "_summary.md" if "_summary.md" in names else None,
            "machine": [n for n in ("_results.json", "_regime.json", "_regime-screener.json",
                                    "_regime-intraday.json", "_source-health.json") if n in names],
            "raw": [n for n in ("_cache.json", "_premarket-pull.json", "_breadth_raw.json")
                    if n in names],
        },
        "screens": described,
        "files": files,
        "notes": notes,
    }


def main(argv):
    if not os.path.isdir(SCREENS_ROOT):
        print("daily-screens/ not found", file=sys.stderr)
        return 2

    check_only = "--check" in argv
    dates = sorted(
        d for d in os.listdir(SCREENS_ROOT)
        if DATE_RE.match(d) and os.path.isdir(os.path.join(SCREENS_ROOT, d))
    )

    written = 0
    drift = []
    for date in dates:
        manifest = build(os.path.join(SCREENS_ROOT, date), date)
        for note in manifest["notes"]:
            if "split into" in note or "no matching" in note or "no _source-health" in note:
                drift.append("%s: %s" % (date, note))
        if not check_only:
            out = os.path.join(SCREENS_ROOT, date, "_manifest.json")
            with open(out, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(manifest, fh, indent=1, sort_keys=False)
                fh.write("\n")
            written += 1

    print("%d dated directories %s" % (len(dates), "checked" if check_only else "written"))
    if drift:
        print()
        print("shape differences (not failures - they are real, and now visible):")
        for d in drift:
            print("  %s" % d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
