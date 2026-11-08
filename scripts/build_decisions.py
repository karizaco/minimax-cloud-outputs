#!/usr/bin/env python3
"""Generate a `_decisions.json` for every dated directory under daily-screens/.

Why: this repo stores outputs, not reasoning transcripts - there is no model
transcript anywhere in the tree. The closest thing to a reasoning trail is prose:
the "Flags" and "Caveats" sections of each brief, and the exclusion funnel each
brief publishes in words. Those paragraphs carry real decisions - which 729 names
failed on volume, which 10 had no confirmed driver - but a consumer has to parse
English to get them.

`_results.json` already holds most of the decision content in machine form: the
thresholds that produced each tier, the cap that truncated it, the names the cap
dropped, and the rows_passing / rows_kept assertion for every branch. This script
promotes that subset into a small, documented, self-describing record, and adds
the two facts a consumer cannot derive from the brief alone:

  * which names were DROPPED by a cap, and why the list is shorter than the pool
  * the session lag - screen metrics describe the previous session while the
    "today" columns are this session's settled close

Every value is copied from `_results.json` or from a file's presence on disk.
Nothing is inferred about content, and no value is invented.

  python3 scripts/build_decisions.py            # write the records
  python3 scripts/build_decisions.py --check    # report only, write nothing
"""
import datetime
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENS_ROOT = os.path.join(REPO, "daily-screens")

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def as_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def find_value(obj, key):
    """Find a scalar under `key`, at the top level or one level down.

    The _results.json layout has changed between runs: `candidates` is a list of
    candidate records in some and an object in others, and the tier lists sit
    beside it rather than inside it. Rather than hard-coding one shape, look in
    the top level first and then one level down.
    """
    if key in obj and not isinstance(obj[key], (list, dict)):
        return obj[key]
    for val in obj.values():
        if isinstance(val, dict) and key in val and not isinstance(val[key], (list, dict)):
            return val[key]
    return None


def find_dict(obj, key):
    """Find a mapping under `key`, at the top level or one level down."""
    v = obj.get(key)
    if isinstance(v, dict):
        return v
    for val in obj.values():
        if isinstance(val, dict):
            inner = val.get(key)
            if isinstance(inner, dict):
                return inner
    return {}


def find_list(obj, key):
    """Find a list of ticker strings under `key`, at the top level or one level down."""
    v = obj.get(key)
    if isinstance(v, list):
        return v
    for val in obj.values():
        if isinstance(val, dict):
            inner = val.get(key)
            if isinstance(inner, list):
                return inner
    return []


def build(date_dir, date):
    results_path = os.path.join(date_dir, "_results.json")
    if not os.path.exists(results_path):
        return None
    try:
        with open(results_path, encoding="utf-8") as fh:
            res = json.load(fh)
    except (OSError, ValueError):
        return None

    thresholds = find_dict(res, "thresholds")
    stylists = res.get("stylist_buckets")
    if not isinstance(stylists, list):
        stylists = []
    counts = find_dict(res, "counts")
    coverage = find_dict(res, "screen_coverage")
    regime = find_dict(res, "regime")

    rules = {
        "stylists": stylists,
        "focus": {
            "min_stylists": thresholds.get("focus_stylists"),
            "max_names": thresholds.get("focus_max"),
        },
        "tier_a": {
            "min_stylists": thresholds.get("tier_a_stylists"),
            "max_names": thresholds.get("tier_a_max"),
        },
    }

    # The truncation decision: a pool of names met the rule, the cap cut it.
    published = find_list(res, "tier_a")
    pool_members = find_list(res, "tier_a_pool_members")
    pool_size = find_value(res, "tier_a_pool")
    if pool_size is None:
        pool_size = counts.get("tier_a_pool")
    truncated = bool(find_value(res, "tier_a_truncated"))
    dropped_names = [n for n in pool_members if n not in published]

    coverage_out = {}
    for branch, stats in sorted(coverage.items()):
        passing = as_int(stats.get("rows_passing"))
        kept = as_int(stats.get("rows_kept"))
        coverage_out[branch] = {
            "rows_passing": passing,
            "rows_kept": kept,
            "complete": (passing is not None and kept is not None and passing == kept),
        }
    incomplete = [b for b, s in coverage_out.items() if not s["complete"]]

    data_as_of = res.get("data_as_of")
    lag = None
    if data_as_of:
        try:
            lag = (datetime.date.fromisoformat(date)
                   - datetime.date.fromisoformat(data_as_of)).days
        except ValueError:
            lag = None

    machine_source_health = os.path.exists(os.path.join(date_dir, "_source-health.json"))

    notes = []
    if truncated:
        notes.append(
            "Tier-A was truncated by its cap: %s names met the >=%s-stylist rule, %d were "
            "published, %d were dropped. The dropped names are listed under dropped.tier_a."
            % (pool_size, rules["tier_a"]["min_stylists"], len(published), len(dropped_names))
        )
    if lag:
        notes.append(
            "session lag %d day(s): the screen metrics describe the %s session, the 'today' "
            "columns are the %s settled close" % (lag, data_as_of, date)
        )
    if incomplete:
        notes.append(
            "branch coverage is not complete for: %s" % ", ".join(incomplete)
        )
    if not machine_source_health:
        notes.append(
            "source health for this run exists only in the prose table in daily-sweep.md; "
            "there is no _source-health.json"
        )

    return {
        "_schema": "daily-screens-decisions-v1",
        "date": date,
        "data_as_of": data_as_of,
        "session_lag_days": lag,
        "derived_from": "daily-screens/%s/_results.json" % date,
        "rules": rules,
        "counts": counts,
        "dropped": {
            "tier_a_truncated": truncated,
            "tier_a_pool_size": pool_size,
            "tier_a_published": len(published),
            "tier_a": dropped_names,
        },
        "screen_coverage": coverage_out,
        "regime": {
            "size_cut_pct": regime.get("size_cut_pct"),
            "uncertainty": regime.get("uncertainty"),
            "late_cycle": regime.get("late_cycle"),
            "breadth_pct_spx": regime.get("breadth_pct_spx"),
        },
        "source_health": {
            "machine_file": "_source-health.json" if machine_source_health else None,
            "prose_only": not machine_source_health,
        },
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
    skipped = []
    truncated = 0
    for date in dates:
        record = build(os.path.join(SCREENS_ROOT, date), date)
        if record is None:
            skipped.append(date)
            continue
        if record["dropped"]["tier_a_truncated"]:
            truncated += 1
        if not check_only:
            out = os.path.join(SCREENS_ROOT, date, "_decisions.json")
            with open(out, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(record, fh, indent=1, sort_keys=False)
                fh.write("\n")
            written += 1

    print("%d dated directories %s" % (len(dates), "checked" if check_only else "written"))
    print("%d carried a tier-A truncation decision" % truncated)
    if skipped:
        print("no _results.json, skipped: %s" % ", ".join(skipped))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
