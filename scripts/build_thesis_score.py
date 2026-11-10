#!/usr/bin/env python3
"""Score every brief's published thesis, and show which briefs score at all.

Why: the pre-market brief is the only routine that closes the loop - it scores
yesterday's own published thesis against the invalidation level it published.
On 2026-11-06 it scored 112 names: 67 HELD, 41 BROKE, 2 PARTIAL, 2 UNJUDGED.

But it did so on ONE run. Across the 32 briefs in `daily-briefs/`, only two carry
a thesis-verdict table at all, and they carry DIFFERENT ones: the 2026-11-06
brief tests the invalidation LEVEL the previous brief published, while the
2026-11-05 brief tests whether the pre-market GAP survived the session. Those
are two different tests, and pooling their hits into one rate would be
meaningless - a gap that survives is not a thesis that holds.

So this scores each contract separately, and reports the coverage: which briefs
published a scoreable table and which published none. That coverage is itself
the finding - a reader of a brief with no score has no way to know whether the
thesis held or whether nobody checked.

A trap this avoids: the source-health table uses the word PARTIAL to mean the
DATA SOURCE was partial. Scoring that as a thesis verdict would invent
partial holds. The extractor therefore requires a column literally headed
"Thesis held?" (or an explicit verdict column in a table that is not a source
table).

  python3 scripts/build_thesis_score.py
  python3 scripts/build_thesis_score.py --check
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

FAMILIES = ("daily-briefs", "us-stocks-in-play", "weekly")
OUT_ROOT = "derived"

VERDICTS = ("HELD", "BROKE", "PARTIAL", "UNJUDGED")
VERDICT_RE = re.compile(r"^\s*\**\s*(HELD|BROKE|PARTIAL|UNJUDGED)\b", re.I)

# A column that means "this row is a source-health row", not a thesis row.
SOURCE_HINT = re.compile(r"^(source|endpoint|tool|availability|status|reliability|notes?)$", re.I)
TICKER_HINT = re.compile(r"^(ticker|symbol|name)$", re.I)
MOVE_HINT = re.compile(r"(move|%|change|session|pre-market|premarket)", re.I)


def contract_of(header):
    """Which test this table applies, or None if it is not a thesis table.

    The two contracts in the archive are:
      invalidation - the level the previous brief published, tested against the
                     session's close.
      gap          - whether the pre-market gap survived the session.
    """
    cols = [h.strip() for h in header]
    if any(re.search(r"thesis\s*held", c, re.I) for c in cols):
        if any("pre-market" in c.lower() or "premarket" in c.lower() for c in cols):
            return "gap"
        return "invalidation"
    return None


def extract(text):
    """Every thesis verdict table in a document."""
    out = []
    for _start, header, rows in J.md_tables(text):
        contract = contract_of(header)
        if not contract:
            continue
        if any(SOURCE_HINT.match(h.strip()) for h in header):
            # A source-health table. PARTIAL here means the source was partial.
            continue
        tcol = next((h for h in header if TICKER_HINT.match(h.strip())), None)
        vcol = next((h for h in header if re.search(r"thesis\s*held|verdict", h, re.I)), None)
        if not tcol or not vcol:
            continue
        mcol = next((h for h in header if h != tcol and h != vcol and MOVE_HINT.search(h)), None)
        entries = []
        for row in rows:
            ticker = J.strip_md(row.get(tcol)).upper()
            if not ticker:
                continue
            m = VERDICT_RE.match(J.strip_md(row.get(vcol)))
            if not m:
                continue
            entries.append({
                "ticker": ticker,
                "verdict": m.group(1).upper(),
                "reason": J.strip_md(row.get(vcol)),
                "move": J.to_float(row.get(mcol)) if mcol else None,
                "move_column": mcol,
                "setup": J.strip_md(row.get(header[1])) if len(header) > 1 else None,
            })
        if entries:
            out.append({"contract": contract, "columns": header, "entries": entries})
    return out


def scan():
    """Every brief in the archive, and what it published."""
    briefs = []
    for family in FAMILIES:
        root = os.path.join(J.REPO, family)
        if not os.path.isdir(root):
            continue
        for name in sorted(os.listdir(root)):
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            try:
                text = open(path, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            tables = extract(text)
            briefs.append({
                "family": family,
                "file": "%s/%s" % (family, name),
                "date": re.search(r"(\d{4}-\d{2}-\d{2})", name).group(1)
                        if re.search(r"(\d{4}-\d{2}-\d{2})", name) else None,
                "tables": tables,
                "n_scored": sum(len(t["entries"]) for t in tables),
            })
    return briefs


def build():
    briefs = scan()
    scored = [b for b in briefs if b["n_scored"]]
    unscored = [b for b in briefs if not b["n_scored"]]

    rows = []
    for b in scored:
        for t in b["tables"]:
            for e in t["entries"]:
                rows.append({
                    "brief": b["file"],
                    "brief_date": b["date"],
                    "contract": t["contract"],
                    "ticker": e["ticker"],
                    "verdict": e["verdict"],
                    "move": e["move"],
                    "reason": e["reason"],
                })

    by_contract = {}
    for contract in sorted({r["contract"] for r in rows}):
        subset = [r for r in rows if r["contract"] == contract]
        counts = {v: sum(1 for r in subset if r["verdict"] == v) for v in VERDICTS}
        judged = sum(counts[v] for v in ("HELD", "BROKE", "PARTIAL"))
        by_contract[contract] = {
            "rows": len(subset),
            "counts": counts,
            "judged": judged,
            "held_rate": round(100.0 * counts["HELD"] / judged, 1) if judged else None,
            "briefs": sorted({r["brief"] for r in subset}),
        }

    # Which names broke, and how often they were judged.
    per_name = {}
    for r in rows:
        n = per_name.setdefault(r["ticker"], {"held": 0, "broke": 0, "partial": 0,
                                              "unjudged": 0, "briefs": []})
        n[r["verdict"].lower()] = n.get(r["verdict"].lower(), 0) + 1
        n["briefs"].append("%s:%s" % (r["brief_date"] or r["brief"], r["contract"]))

    notes = []
    if len(scored) <= 1:
        notes.append(
            "Only %d brief(s) in the archive publish a thesis-verdict table, so the "
            "scorecard below is a description of that run rather than a track record. "
            "The other %d briefs published no score, and a reader cannot tell from a "
            "brief with no score whether the thesis held or whether nobody checked."
            % (len(scored), len(unscored)))
    if len(by_contract) > 1:
        notes.append(
            "**The two contracts are not pooled.** The archive contains %d different "
            "tests - %s - and a gap that survives a session is not a thesis that holds. "
            "Each is counted separately below."
            % (len(by_contract), ", ".join(sorted(by_contract))))
    return {
        "briefs": briefs,
        "scored": scored,
        "unscored": unscored,
        "rows": rows,
        "by_contract": by_contract,
        "per_name": per_name,
        "notes": notes,
    }


def render(data):
    lines = []
    lines.append("# Thesis scorecard — did yesterday's published thesis hold?")
    lines.append("")
    lines.append(J.provenance(
        "derived read of the thesis-verdict tables in the published briefs "
        "(no source file is modified)",
        "%d brief(s) scored, %d name-verdict row(s); %d brief(s) published no score"
        % (len(data["scored"]), len(data["rows"]), len(data["unscored"])),
        "read-only",
    ))
    lines.append("")
    lines.append("> **Read this before the table.**")
    lines.append(">")
    lines.append("> 1. **A brief with no score is not a brief whose thesis broke.** It is a")
    lines.append(">    brief that did not check. The coverage table below separates them, because")
    lines.append(">    the artifact itself does not.")
    lines.append("> 2. **Different tests are never pooled.** The archive contains two contracts")
    lines.append(">    and they are counted separately.")
    lines.append("> 3. **This counts verdicts. It does not judge them.** A high HELD rate is not")
    lines.append(">    a quality score, and a name's verdict says nothing about whether it")
    lines.append(">    should be traded.")
    for n in data["notes"]:
        lines.append("> 4. **%s**" % n)
    lines.append("")

    lines.append("## Coverage — which briefs score")
    lines.append("")
    lines.append("| Brief | Date | Contract | Names scored |")
    lines.append("|---|---|---|---|")
    for b in data["scored"]:
        contracts = ", ".join(sorted({t["contract"] for t in b["tables"]}))
        lines.append("| `%s` | %s | %s | %d |" % (b["file"], b["date"] or "—", contracts, b["n_scored"]))
    lines.append("")
    lines.append("%d brief(s) published no thesis score:" % len(data["unscored"]))
    lines.append("")
    lines.append("| Brief | Date |")
    lines.append("|---|---|")
    for b in data["unscored"]:
        lines.append("| `%s` | %s |" % (b["file"], b["date"] or "—"))
    lines.append("")

    lines.append("## By contract")
    lines.append("")
    lines.append("| Contract | Briefs | Rows | HELD | BROKE | PARTIAL | UNJUDGED | HELD rate |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for contract, agg in sorted(data["by_contract"].items()):
        c = agg["counts"]
        lines.append("| %s | %d | %d | %d | %d | %d | %d | %s |" % (
            contract, len(agg["briefs"]), agg["rows"], c["HELD"], c["BROKE"],
            c["PARTIAL"], c["UNJUDGED"],
            "%.1f%%" % agg["held_rate"] if agg["held_rate"] is not None else "—"))
    lines.append("")
    lines.append("**What the HELD rate is.** The share of JUDGED names whose thesis held, where")
    lines.append("judged means HELD, BROKE or PARTIAL - an UNJUDGED row has no level and no")
    lines.append("price, so it is excluded rather than counted as a failure. The rate is not")
    lines.append("comparable across contracts and is not a measure of the routine's quality.")
    lines.append("")

    lines.append("## Every verdict")
    lines.append("")
    lines.append("| Brief | Contract | Ticker | Verdict | Move |")
    lines.append("|---|---|---|---|---|")
    for r in sorted(data["rows"], key=lambda r: (r["brief_date"] or "", r["ticker"])):
        lines.append("| %s | %s | %s | **%s** | %s |" % (
            r["brief_date"] or r["brief"], r["contract"], r["ticker"], r["verdict"],
            "—" if r["move"] is None else "%+.2f%%" % r["move"]))
    lines.append("")

    lines.append("## Names by verdict")
    lines.append("")
    lines.append("| Ticker | HELD | BROKE | PARTIAL | UNJUDGED | Judged in |")
    lines.append("|---|---|---|---|---|---|")
    for t in sorted(data["per_name"]):
        n = data["per_name"][t]
        judged = n["held"] + n["broke"] + n["partial"]
        lines.append("| %s | %d | %d | %d | %d | %s |" % (
            t, n["held"], n["broke"], n["partial"], n["unjudged"], ", ".join(n["briefs"])))
    lines.append("")
    lines.append("## Method and caveats")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append("| Families scanned | %s |" % ", ".join(FAMILIES))
    lines.append("| Table key | a column headed `Thesis held?` |")
    lines.append("| Verdict | the leading HELD / BROKE / PARTIAL / UNJUDGED |")
    lines.append("| Source-health tables | excluded - PARTIAL there means the SOURCE was partial |")
    lines.append("")
    return "\n".join(lines) + "\n"


CSV_COLS = ["brief", "brief_date", "contract", "ticker", "verdict", "move", "reason"]


def render_csv(data):
    out = [",".join(CSV_COLS)]
    for r in sorted(data["rows"], key=lambda r: (r["brief_date"] or "", r["ticker"])):
        vals = []
        for c in CSV_COLS:
            v = r.get(c)
            if v is None:
                v = ""
            s = str(v)
            if "," in s or '"' in s:
                s = '"%s"' % s.replace('"', '""')
            vals.append(s)
        out.append(",".join(vals))
    return "\n".join(out) + "\n"


def main(argv):
    check_only = "--check" in argv
    data = build()
    if check_only:
        print("briefs scanned: %d | scored: %d | unscored: %d | rows: %d" % (
            len(data["briefs"]), len(data["scored"]), len(data["unscored"]), len(data["rows"])))
        for contract, agg in sorted(data["by_contract"].items()):
            print("  %-14s %s" % (contract, agg["counts"]))
        return 0
    a = J.write_if_changed(os.path.join(J.REPO, OUT_ROOT, "thesis-score.md"), render(data))
    b = J.write_if_changed(os.path.join(J.REPO, OUT_ROOT, "thesis-score.csv"), render_csv(data))
    print("thesis-score.md %s · thesis-score.csv %s (%d briefs scanned, %d scored)"
          % (a, b, len(data["briefs"]), len(data["scored"])))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
