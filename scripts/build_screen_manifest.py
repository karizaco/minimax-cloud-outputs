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
import datetime
import json
import os
import re
import sys

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


def build(date_dir, date):
    names = [n for n in os.listdir(date_dir) if os.path.isfile(os.path.join(date_dir, n))]
    screens, components, artifacts = classify(names)
    described = describe_screens(screens)

    data_as_of = None
    results_path = os.path.join(date_dir, "_results.json")
    if os.path.exists(results_path):
        try:
            with open(results_path, encoding="utf-8") as fh:
                data_as_of = json.load(fh).get("data_as_of")
        except (OSError, ValueError):
            data_as_of = None

    lag = None
    if data_as_of:
        try:
            lag = (datetime.date.fromisoformat(date)
                   - datetime.date.fromisoformat(data_as_of)).days
        except ValueError:
            lag = None

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
        notes.append(
            "screen metrics describe the %s session (%d day(s) before this directory's date); "
            "the 'today' columns are the %s settled close" % (data_as_of, lag, date)
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
