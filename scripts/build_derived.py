#!/usr/bin/env python3
"""Run every derived-view builder, then write the manifests the contract requires.

`derived/` holds views that are JOINED from cron artifacts rather than produced by
a cron. Running them is one command so the tree is never half-regenerated, and
`refs/artifact-contract.md` Rule 3 - a dated directory carries a `_manifest.json`
- applies here exactly as it does to `daily-screens/<date>/`.

Order matters only in that the manifests are written last, because they describe
whatever the builders produced.

  python3 scripts/build_derived.py            # build everything, write manifests
  python3 scripts/build_derived.py --check    # report, write nothing
  python3 scripts/build_derived.py --manifest # manifests only, skip the builders
"""
import importlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

OUT_ROOT = "derived"

BUILDERS = (
    ("build_persistence", "persistence across the dated boards"),
    ("build_gap_reconciliation", "pre-market gap vs the settled close"),
    ("build_sector_flow", "the board by sector, against the ETF tape"),
    ("build_ledger", "one row per name per session"),
    ("build_setups", "the setup card and the next-session journal"),
    ("build_client_safe", "the client-safe twin of every narrative artifact"),
    ("build_confirmation", "how many routines saw each name"),
    ("build_thesis_score", "did yesterday's published thesis hold?"),
    ("build_run_ledger", "which routine published what, and when"),
    ("build_charts", "the renders of what is already computed"),
)

ROLES = {
    "gap-reconciliation.md": "brief - every PRE_GAP name and the path its gap took",
    "gap-reconciliation.csv": "machine - the same rows with the full catalyst text",
    "sector-flow.md": "brief - the board's sector mix against the ETF tape",
    "sector-flow.csv": "machine - the same rows",
    "ledger.md": "brief - coverage, and the names several routines saw",
    "ledger.jsonl": "machine - one record per name, `_meta` on the first line",
    "setup-card.md": "brief - published Stalk and Tier-A, session-stamped, with unchecked gaps",
    "setup-card.csv": "machine - the same rows, including tags that could not be recomputed",
    "confirmation.md": "brief - how many routines saw each name, and where they agree",
    "confirmation.csv": "machine - the same rows",
    "thesis-score.md": "brief - the published thesis verdicts, by contract, with coverage",
    "thesis-score.csv": "machine - the same verdicts",
    "run-ledger.md": "brief - which routine published what, and which are missing",
    "run-ledger.csv": "machine - the same rows",
    "client-safe/": "the same artifacts rendered for a client that shows bold, italics and lists only",
    "_manifest.json": "this file",
}

SOURCES = {
    "gap-reconciliation": ["earnings/<date>-reactions.md", "us-eod/<date>.csv"],
    "sector-flow": ["daily-screens/<date>/master.csv", "us-stocks-in-play/<date>.md"],
    "ledger": ["daily-screens/<date>/{master,focus,tier-a}.csv",
               "earnings/<date>-reactions.md", "us-eod/<date>.csv",
               "us-stocks-in-play/<date>-candidates.csv", "options-flow/<date>.md"],
    "setup-card": ["daily-screens/<date>/{stalk,tier-a}.csv",
                   "earnings/<date>-reactions.md", "us-eod/<date>.csv"],
    "client-safe": ["daily-screens/<date>/daily-sweep.md", "daily-briefs/<date>.md",
                    "us-stocks-in-play/<date>.md", "ntrt/<date>.md",
                    "earnings/<date>.md", "weekly/<date>.md", "cross-asset/<date>.md",
                    "options-flow/<date>.md", "international-eod/<date>/summary.md"],
    "confirmation": ["daily-screens/<date>/{tier-a,focus}.csv", "ntrt/<date>.md",
                     "options-flow/<date>.md", "earnings/<date>-{reminders,reactions}.md"],
    "thesis-score": ["daily-briefs/<date>-pre-market.md", "us-stocks-in-play/<date>.md"],
    "run-ledger": ["every published artifact, against the roster's schedule"],
}


def run_builders(check_only):
    results = []
    for name, _desc in BUILDERS:
        mod = importlib.import_module(name)
        argv = [name] + (["--check"] if check_only else [])
        print("--- %s" % name)
        try:
            code = mod.main(argv)
        except Exception as exc:  # a builder failing must not hide the others
            print("  FAILED: %s: %s" % (type(exc).__name__, exc))
            results.append((name, "failed"))
            continue
        results.append((name, "ok" if code == 0 else "exit %d" % code))
    return results


def build_manifest(date_dir, date):
    names = sorted(n for n in os.listdir(date_dir)
                   if os.path.isfile(os.path.join(date_dir, n)))
    files, views = [], {}
    for n in names:
        if n == "_manifest.json":
            continue
        stem = n.rsplit(".", 1)[0]
        files.append({
            "name": n,
            "bytes": os.path.getsize(os.path.join(date_dir, n)),
            "role": ROLES.get(n, "unclassified"),
        })
        if stem in SOURCES:
            views.setdefault(stem, {"files": [], "joined_from": SOURCES[stem]})
            views[stem]["files"].append(n)

    notes = [
        "Every file here is DERIVED. No cron writes into this directory, and nothing "
        "in it is a new measurement - each value is copied from the artifacts named "
        "in `joined_from`.",
        "A view absent from this manifest was not built for this date, which means a "
        "source it needs does not exist. The view's own brief states which one.",
    ]
    missing = [k for k in SOURCES if k not in views]
    if missing:
        notes.append("Not built for this date: %s." % ", ".join(sorted(missing)))

    return {
        "_schema": "derived-manifest-v1",
        "date": date,
        "generated_by": "scripts/build_derived.py",
        "views": views,
        "files": files,
        "notes": notes,
    }


def write_manifests(check_only):
    root = os.path.join(J.REPO, OUT_ROOT)
    if not os.path.isdir(root):
        print("no %s/ directory - nothing to describe" % OUT_ROOT)
        return 0
    n = 0
    for date in sorted(os.listdir(root)):
        date_dir = os.path.join(root, date)
        if not (J.DATE_RE.match(date) and os.path.isdir(date_dir)):
            continue
        manifest = build_manifest(date_dir, date)
        if check_only:
            print("%s: %d file(s), views %s" % (
                date, len(manifest["files"]), ",".join(sorted(manifest["views"])) or "none"))
        else:
            J.write_json(os.path.join(date_dir, "_manifest.json"), manifest)
        n += 1
    print("%d dated derived directory/ies %s" % (n, "checked" if check_only else "described"))
    return 0


def main(argv):
    check_only = "--check" in argv
    manifest_only = "--manifest" in argv
    if not manifest_only:
        results = run_builders(check_only)
        print()
        print("builders: %s" % ", ".join("%s=%s" % r for r in results))
        failed = [n for n, s in results if s != "ok"]
        if failed:
            print("FAILED: %s" % ", ".join(failed))
    print()
    rc = write_manifests(check_only)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
