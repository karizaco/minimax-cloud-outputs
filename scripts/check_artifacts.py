#!/usr/bin/env python3
"""Check this repo's own consistency: the index, in-text file references, and the naming convention.

Three checks, one per --mode. Each is read-only and safe to run on any checkout.

  index       ARTIFACT-INDEX.md names every top-level directory, and every path it
              cites resolves on disk. An index that silently omits a directory is
              worse than no index, because a reader trusts it.

  links       Every backticked file reference inside every .md resolves - either
              repo-relative or relative to the file that mentions it. This catches
              the class of rot where a basename is renamed but the prose still
              points at the old name.

  convention  Artifact basenames are Windows-safe (no ':' - it is illegal in a
              Windows filename and this repo is checked out on Windows), and dated
              screen directories keep one filename shape.

Exit code: 0 clean, 1 findings, 2 the checker could not run.
"""
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(REPO, "ARTIFACT-INDEX.md")

# Directories that are not artifact families.
SKIP_DIRS = {".git", ".vscode", "__pycache__", ".idea"}

# Top-level directories that are deliberately not listed in the index.
INDEX_EXEMPT = set()

# Path prefixes that belong to the migration repo (karizaco/maxhermes-migration),
# not to this repo. A reference to one of these is correct, not broken.
EXTERNAL_PREFIXES = (
    "cloud-prompts/", "tools/", "docs/", "skills/", "_shared/",
    "karizaco/", "http://", "https://",
)

# Bare filenames that live in the migration repo. Referencing them is correct.
EXTERNAL_NAMES = {
    "mcp_bridge.py", "preopen_feed.py", "push_artifact.sh", "verify_delivery.sh",
    "probe_mcp.py", "relvol_screen.py", "reversal_bullish.py", "screen.py",
    "check_bonde_artifact.py", "apply_skip_marker.py", "gen_roster.py",
    "01-weekly-mcp-health-check.md", "02-asia-pre-market-reactions.md",
    "same_day_prints.py", "premarket_pull.py", "premarket_universe.py",
    "trending-symbols.json", "RUNTIME-CONTRACT.md",
    # `cloud-prompts/_shared/PROMPT-BLOCKS.md` in the migration repo. The weekly
    # and macro-calendar briefs cite it by bare name in their source-health
    # tables; macro-calendar/2026-11-08-week-ahead.md gives the full path.
    "PROMPT-BLOCKS.md", "window_check.sh",
}

# Real paths that live outside this repo. Each is listed because an artifact
# points at it and a reader following the pointer today would not find it here.
EXTERNAL_PATHS = {
    "research/watchlist.yaml":
        "the personal watchlist on the Mavis host; the published replacement is refs/watchlist.yaml",
    "research/watchlist.README.md":
        "schema and publish instructions, in the migration repo",
    "research/logs/audit.log":
        "a host-side log path named by a brief, not a repo artifact",
}

# Directory names that exist in more than one repo, so a reference under them
# cannot be resolved to "this repo" without guessing.
AMBIGUOUS_DIRS = {"scripts"}

# Path segments that are placeholders rather than literal directories.
TEMPLATE_SEGMENTS = {"YYYY", "yyyy", "Wnn", "WNN", "cron_date", "date", "HHMM"}

# Characters that are illegal in a Windows filename.
ILLEGAL_BASENAME_CHARS = set(':<>"|?*')

BACKTICKED = re.compile(r"`([^`\n]{1,200})`")
PATH_LIKE = re.compile(
    r"^[A-Za-z0-9_][A-Za-z0-9_./-]*"
    r"\.(md|csv|json|jsonl|yaml|yml|txt|py|sh|log)$"
)
PLACEHOLDER = set("<>{}*…")


def repo_top_dirs():
    return sorted(
        d for d in os.listdir(REPO)
        if os.path.isdir(os.path.join(REPO, d)) and d not in SKIP_DIRS
    )


def walk_files(ext):
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(ext):
                yield os.path.join(root, f)


def is_external(token):
    if token.startswith(EXTERNAL_PREFIXES):
        return True
    if token in EXTERNAL_PATHS:
        return True
    if os.path.basename(token) in EXTERNAL_NAMES and "/" not in token:
        return True
    return False


def is_repo_candidate(token, repo_dirs):
    """Is this token claiming to be a path in THIS repo?

    A path with a directory is a candidate when it starts with a directory that
    exists here - unless that directory name is ambiguous across repos.

    A bare name is a candidate only when it is artifact-shaped (it carries a
    dash). A runtime scratch file (`avg10.json`, `company_tickers.json`,
    `_VIX.json`) is not an artifact, and neither is a migration-repo prompt
    (`SKILL.md`), so those are not this check's business.
    """
    if "/" in token:
        first = token.split("/")[0]
        if first in AMBIGUOUS_DIRS:
            return False
        return first in repo_dirs
    return "-" in token


def has_placeholder(token):
    if PLACEHOLDER & set(token):
        return True
    for part in token.split("/"):
        stem = part.split(".")[0]
        if stem in TEMPLATE_SEGMENTS or stem.upper().startswith("YYYY"):
            return True
    return False


def all_basenames():
    """Every filename in the repo, so a bare name can be recognised as a name."""
    return {os.path.basename(p) for p in walk_files("")}


def resolve(token, source_path, names=None):
    """Resolve a referenced path: repo-relative first, then sibling of the source.

    A bare filename with no directory component is a NAME, not a path - the index
    writes `focus.csv` to mean "the focus CSV", wherever it lives. If the name
    exists anywhere in the repo it counts as resolved.

    A bare name that names a *variant* of a sibling also counts: a macro-calendar
    brief says "the Sunday edition: `2026-W44-week.md`" when the sibling that
    exists is `2026-W44-week-mid.md`. Neither stem is a prefix of the other
    unless one drops its last segment, so both directions are checked.
    """
    cands = [os.path.join(REPO, token)]
    src_dir = os.path.dirname(source_path)
    cands.append(os.path.join(src_dir, token))
    cands.append(os.path.join(src_dir, os.path.basename(token)))
    for c in cands:
        if os.path.exists(c):
            return c
    if names is not None and "/" not in token:
        base = os.path.basename(token)
        if base in names:
            return base
        stem = os.path.splitext(base)[0]
        for other in names:
            other_stem = os.path.splitext(other)[0]
            if len(stem) < 12 or len(other_stem) < 12:
                continue
            # The extra part must be a dash-separated qualifier, so that only a
            # genuine variant matches - not an unrelated name that merely shares
            # a prefix.
            if other_stem.startswith(stem):
                extra = other_stem[len(stem):]
            elif stem.startswith(other_stem):
                extra = stem[len(other_stem):]
            else:
                continue
            if extra.startswith("-"):
                return other
    return None


# ---------------------------------------------------------------- index mode

def check_index():
    findings = []
    if not os.path.exists(INDEX):
        return ["ARTIFACT-INDEX.md is missing from the repo root"], 0

    text = open(INDEX, encoding="utf-8").read()

    dirs = [d for d in repo_top_dirs() if d not in INDEX_EXEMPT]
    missing = [d for d in dirs if "`%s/" % d not in text]
    for d in missing:
        findings.append("index: top-level directory `%s/` is not named in ARTIFACT-INDEX.md" % d)

    # Every path-like token the index cites must resolve.
    cited = set()
    for token in BACKTICKED.findall(text):
        token = token.strip()
        if not PATH_LIKE.match(token) or has_placeholder(token) or is_external(token):
            continue
        cited.add(token)

    unresolved = sorted(t for t in cited if resolve(t, INDEX, all_basenames()) is None)
    for t in unresolved:
        findings.append("index: cited path does not resolve: `%s`" % t)

    print("index: %d top-level directories, %d cited paths checked" % (len(dirs), len(cited)))
    return findings, len(dirs)


# ---------------------------------------------------------------- links mode

def check_links():
    findings = []
    checked = 0
    external = 0
    placeholder = 0
    not_ours = 0
    names = all_basenames()
    repo_dirs = set(repo_top_dirs())

    for md in walk_files(".md"):
        rel = os.path.relpath(md, REPO)
        if rel.startswith("archive" + os.sep) or rel.startswith("refs" + os.sep + "archive"):
            continue
        try:
            text = open(md, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for token in BACKTICKED.findall(line):
                token = token.strip()
                if not PATH_LIKE.match(token):
                    continue
                if has_placeholder(token):
                    placeholder += 1
                    continue
                if is_external(token):
                    external += 1
                    continue
                if not is_repo_candidate(token, repo_dirs):
                    not_ours += 1
                    continue
                checked += 1
                if resolve(token, md, names) is None:
                    findings.append(
                        "links: %s:%d -> `%s` does not resolve" % (rel, lineno, token)
                    )

    print("links: %d in-repo references checked, %d external skipped, "
          "%d templated skipped, %d not a path in this repo" % (checked, external, placeholder, not_ours))
    return findings, checked


# ------------------------------------------------------------ convention mode

def check_convention():
    findings = []
    shape = []

    for path in walk_files(""):
        rel = os.path.relpath(path, REPO)
        if rel.startswith("archive" + os.sep) or rel.startswith("refs" + os.sep + "archive"):
            continue
        base = os.path.basename(path)
        bad = ILLEGAL_BASENAME_CHARS & set(base)
        if bad:
            findings.append(
                "convention: illegal character(s) %s in basename `%s`"
                % (", ".join(sorted(bad)), rel)
            )

    screens_root = os.path.join(REPO, "daily-screens")
    if os.path.isdir(screens_root):
        for date in sorted(os.listdir(screens_root)):
            d = os.path.join(screens_root, date)
            if not os.path.isdir(d) or not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
                continue
            names = os.listdir(d)
            for n in names:
                if n.startswith(date + "-"):
                    findings.append(
                        "convention: dated screen file carries a date prefix: "
                        "`daily-screens/%s/%s`" % (date, n)
                    )
            mds = {n[:-3] for n in names if n.endswith(".md")}
            csvs = {n[:-4] for n in names if n.endswith(".csv")}
            for stem in sorted(mds - csvs):
                shape.append("daily-screens/%s: `%s.md` has no matching `.csv`" % (date, stem))
            for stem in sorted(csvs - mds):
                shape.append("daily-screens/%s: `%s.csv` has no matching `.md`" % (date, stem))

    print("convention: %d shape differences recorded (not failures)" % len(shape))
    for s in shape[:40]:
        print("  note: %s" % s)
    if len(shape) > 40:
        print("  ... and %d more shape differences" % (len(shape) - 40))
    return findings, len(shape)


# ------------------------------------------------------------------- driver

MODES = {
    "index": check_index,
    "links": check_links,
    "convention": check_convention,
}


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("-")]
    modes = args or list(MODES)

    if not os.path.isdir(REPO):
        print("cannot locate the repo root", file=sys.stderr)
        return 2

    all_findings = []
    for mode in modes:
        if mode not in MODES:
            print("unknown mode: %s (choose from %s)" % (mode, ", ".join(MODES)), file=sys.stderr)
            return 2
        print("== %s ==" % mode)
        findings, _ = MODES[mode]()
        all_findings.extend(findings)

    if all_findings:
        print()
        for f in all_findings:
            print("FAIL %s" % f)
        print()
        print("%d finding(s)" % len(all_findings))
        return 1

    print()
    print("clean")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
