#!/usr/bin/env python3
"""One row per name per session, joining what five routines each know separately.

Why: on a single day a name like FROG is touched by the earnings scanner (a
catalyst, a pre-market gap, a move measured against its own average), the daily
sweep (Tier-A membership, a stylist count), the in-play digest (whether the gap
held), the options-flow screen (whether unusual positioning showed up - and FROG
does NOT appear in the 2026-11-06 flow leaders, which is itself a fact), and the
settled EOD snapshot (the close). Each of those is a column. None of them is a
row. There is no artifact in this repo that answers "what do we know about X
today" in one place.

This is that row. It is also the artifact that exposes the coverage holes the
others leave invisible: the earnings scanner's own table says "no catalyst lookup
(outside the per-run budget)" for several of the largest gaps of the morning, and
a reader of the sweep cannot tell that absence from a genuine finding.

THE CONSTRAINT, which is the same one the decisions contract states: **it joins,
it does not restate.** Every field is copied from an artifact that already exists.
A field that cannot be filled is left null and counted, so the ledger's own
coverage rate is visible in the ledger. A ledger that silently filled gaps with
guesses would be the most dangerous artifact in this repo, because it would look
like the authoritative one.

Sources joined, per session:
  daily-screens/<date>/{tier-a,focus,master}.csv   tier, stylists, sector
  earnings/<date>-reactions.md                     pre-market gap, catalyst, tag
  us-eod/<date>.csv                                settled close, change, sector
  us-stocks-in-play/<date>-candidates.csv          tier, RVol, gap verdict
  options-flow/<date>.md                           whether unusual flow appeared

  python3 scripts/build_ledger.py            # write the ledgers
  python3 scripts/build_ledger.py --check    # report coverage only, write nothing
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402
import build_gap_reconciliation as G  # noqa: E402

SCREENS = "daily-screens"
EARNINGS = "earnings"
INPLAY = "us-stocks-in-play"
FLOW = "options-flow"
OUT_ROOT = "derived"

# Which routine contributed anything at all to a row.
ROUTINES = ("screen", "earnings", "eod", "in_play", "options_flow")


def read_screen(date):
    """Tier membership and stylist counts from the dated screen boards."""
    out = {}
    for board in ("master", "focus", "tier-a"):
        rows = J.read_csv_rows(os.path.join(J.REPO, SCREENS, date, board + ".csv"))
        tcol, _n = J.ticker_column(rows)
        if not tcol:
            continue
        scol, _tax = J.sector_column(rows)
        for row in rows:
            t = J.strip_md(row.get(tcol)).upper()
            if not t:
                continue
            entry = out.setdefault(t, {"boards": [], "n_stylists": None,
                                       "stylists": None, "sector": None})
            if board not in entry["boards"]:
                entry["boards"].append(board)
            n = J.lead_float(row.get("n_stylists") or row.get("_n_stylists"))
            if n is not None:
                entry["n_stylists"] = int(n)
            sty = J.strip_md(row.get("stylists") or row.get("_stylists"))
            if sty:
                entry["stylists"] = sty
            if scol:
                sec = J.strip_md(row.get(scol))
                if sec:
                    entry["sector"] = sec
    return out


def read_earnings(date):
    path = os.path.join(J.REPO, EARNINGS, date + "-reactions.md")
    if not os.path.exists(path):
        return {}
    morning, _header = G.parse_reactions(path)
    out = {}
    for m in morning:
        catalyst = m["catalyst"] or ""
        out[m["ticker"]] = {
            "pre_mkt_pct": m["pre_mkt_pct"],
            "tag": m["tag"] or None,
            "catalyst": catalyst or None,
            "catalyst_status": (
                "not_looked_up" if "no catalyst lookup" in catalyst.lower()
                else ("sourced" if catalyst else "absent")),
            "move_vs_avg": m["move_vs_avg"] or None,
            "us_tradeable": m["us_tradeable"] or None,
        }
    return out


def read_inplay(date):
    for name in ("%s-candidates.csv" % date, "%s-close-candidates.csv" % date):
        rows = J.read_csv_rows(os.path.join(J.REPO, INPLAY, name))
        if not rows:
            continue
        out = {}
        for row in rows:
            t = J.strip_md(row.get("ticker")).upper()
            if not t:
                continue
            out[t] = {
                "tier": J.strip_md(row.get("tier")) or None,
                "rvol": J.lead_float(row.get("rvol")),
                "gap_verdict": J.strip_md(row.get("gap_verdict")) or None,
                "session_dollar_vol": J.lead_float(row.get("session_dollar_vol")),
                "catalyst_materiality": J.strip_md(row.get("catalyst_materiality")) or None,
                "source_file": "%s/%s" % (INPLAY, name),
            }
        return out
    return {}


def read_flow(date):
    """Which names the options-flow screen surfaced, and their own-history ratio.

    Absence here is a fact worth recording: a name the screen did not surface had
    no unusual relative option volume that session, which is different from the
    screen not having run. `flow_screen_ran` carries that distinction.
    """
    path = os.path.join(J.REPO, FLOW, date + ".md")
    if not os.path.exists(path):
        return {}, False
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    out = {}
    for _start, header, rows in J.md_tables(text):
        if "Ticker" not in header:
            continue
        for row in rows:
            t = J.strip_md(row.get("Ticker")).upper()
            if not t or len(t) > 6 or not t.replace(".", "").replace("-", "").isalnum():
                continue
            entry = out.setdefault(t, {"own_history_ratio": None, "peak_v_oi": None})
            oh = J.lead_float(row.get("Own-hist") or row.get("Own-history ratio"))
            if oh is not None:
                entry["own_history_ratio"] = max(entry["own_history_ratio"] or 0.0, oh)
            voi = J.lead_float(row.get("V/OI"))
            if voi is not None:
                entry["peak_v_oi"] = max(entry["peak_v_oi"] or 0.0, voi)
    return out, True


def build_one(date):
    screen = read_screen(date)
    earnings = read_earnings(date)
    inplay = read_inplay(date)
    flow, flow_ran = read_flow(date)
    eod_rows, eod_index, _dupes = J.load_eod(date)
    eod_present = bool(eod_rows)

    tickers = set(screen) | set(earnings) | set(inplay) | set(flow)
    rows = []
    for t in sorted(tickers):
        s = screen.get(t)
        e = earnings.get(t)
        p = inplay.get(t)
        f = flow.get(t)
        erow, matched = J.eod_match(eod_index, t) if eod_index else (None, None)

        seen = []
        if s:
            seen.append("screen")
        if e:
            seen.append("earnings")
        if erow:
            seen.append("eod")
        if p:
            seen.append("in_play")
        if f:
            seen.append("options_flow")

        settled_change = J.to_float(erow.get("change_pct")) if erow else None
        rows.append({
            "date": date,
            "ticker": t,
            "seen_by": seen,
            "n_routines": len(seen),
            # screen
            "screen_boards": s["boards"] if s else None,
            "screen_n_stylists": s["n_stylists"] if s else None,
            "screen_stylists": s["stylists"] if s else None,
            # earnings
            "pre_mkt_pct": e["pre_mkt_pct"] if e else None,
            "earnings_tag": e["tag"] if e else None,
            "catalyst": e["catalyst"] if e else None,
            "catalyst_status": e["catalyst_status"] if e else None,
            "move_vs_avg": e["move_vs_avg"] if e else None,
            # eod
            "settled_close": J.to_float(erow.get("close")) if erow else None,
            "settled_change_pct": settled_change,
            "open_gap_pct": J.to_float(erow.get("gap_pct")) if erow else None,
            "sector": (J.strip_md(erow.get("sector")) if erow else None)
                      or (s["sector"] if s else None),
            "eod_match": matched,
            # in-play
            "in_play_tier": p["tier"] if p else None,
            "rvol": p["rvol"] if p else None,
            "gap_verdict": p["gap_verdict"] if p else None,
            "in_play_catalyst": p["catalyst_materiality"] if p else None,
            # options flow
            "unusual_options_flow": bool(f) if flow_ran else None,
            "options_own_history_ratio": f["own_history_ratio"] if f else None,
            # the path, where both ends exist
            "gap_outcome": (G.outcome(e["pre_mkt_pct"], settled_change)
                            if e else None),
        })

    # Coverage is a property of the ledger and belongs inside it.
    def filled(field):
        return sum(1 for r in rows if r.get(field) is not None)

    coverage = {
        "rows": len(rows),
        "by_routine": {k: sum(1 for r in rows if k in r["seen_by"]) for k in ROUTINES},
        "fields": {
            f: {"filled": filled(f), "null": len(rows) - filled(f)}
            for f in ("pre_mkt_pct", "settled_change_pct", "catalyst", "sector",
                      "rvol", "gap_verdict", "options_own_history_ratio", "gap_outcome")
        },
        "catalyst_status": {},
        "multi_routine": sum(1 for r in rows if r["n_routines"] >= 2),
    }
    for r in rows:
        k = r["catalyst_status"] or "no_earnings_row"
        coverage["catalyst_status"][k] = coverage["catalyst_status"].get(k, 0) + 1

    notes = []
    if not eod_present:
        notes.append("No settled EOD file for %s (`us-eod/<date>.csv`), so no settled "
                     "close, change or sector is available for any row." % date)
    if not flow_ran:
        notes.append("No options-flow artifact for %s (`options-flow/<date>.md`), so "
                     "`unusual_options_flow` is null rather than false — the screen's "
                     "silence cannot be distinguished from it not having run." % date)
    if not earnings:
        notes.append("No reactions artifact for %s (`earnings/<date>-reactions.md`), so "
                     "no pre-market gap or catalyst is available for any row." % date)
    if not inplay:
        notes.append("No in-play candidate file for this date, so no RVol or gap "
                     "verdict is available.")
    if not screen:
        notes.append("No readable screen board for this date, so no tier or stylist "
                     "count is available.")
    nlu = coverage["catalyst_status"].get("not_looked_up", 0)
    if nlu:
        notes.append(
            "%d row(s) carry `catalyst_status: not_looked_up` — the earnings scanner "
            "states \"no catalyst lookup (outside the per-run budget)\" for them. That "
            "is a budget decision, not a finding of no catalyst." % nlu)

    return {
        "_schema": "ledger-v1",
        "date": date,
        "rule": "joins, does not restate - every field is copied from a named artifact "
                "and an unfillable field is left null and counted",
        "sources": {
            "screen": "%s/%s/{master,focus,tier-a}.csv" % (SCREENS, date) if screen else None,
            "earnings": "%s/%s-reactions.md" % (EARNINGS, date) if earnings else None,
            "eod": "us-eod/%s.csv" % date if eod_present else None,
            "in_play": (list(inplay.values())[0]["source_file"] if inplay else None),
            "options_flow": "%s/%s.md" % (FLOW, date) if flow_ran else None,
        },
        "coverage": coverage,
        "notes": notes,
        "rows": rows,
    }


def render_jsonl(data):
    out = [json.dumps({"_meta": {k: data[k] for k in
                                 ("_schema", "date", "rule", "sources", "coverage", "notes")}},
                      sort_keys=False)]
    for r in data["rows"]:
        out.append(json.dumps(r, sort_keys=False))
    return "\n".join(out) + "\n"


def render_md(data):
    c = data["coverage"]
    rows = data["rows"]
    lines = []
    lines.append("# Ledger — what every routine saw on %s" % data["date"])
    lines.append("")
    srcs = [v for v in data["sources"].values() if v]
    lines.append(J.provenance(
        "derived join over %d artifact(s): %s" % (len(srcs), ", ".join("`%s`" % s for s in srcs)),
        "%d name(s) any routine mentioned; %d seen by two or more"
        % (c["rows"], c["multi_routine"]),
        "read-only",
    ))
    lines.append("")
    lines.append("> **Read this before the table.**")
    lines.append("> ")
    lines.append("> 1. **This artifact joins; it does not restate.** Every field is copied from")
    lines.append(">    one of the sources above. Nothing is computed from scratch, nothing is")
    lines.append(">    scored, and no name is recommended.")
    lines.append("> 2. **A blank is a blank, and it is counted.** Where a routine did not see a")
    lines.append(">    name, the field is null and appears in the coverage table below. A ledger")
    lines.append(">    that filled gaps with guesses would look like the authoritative artifact in")
    lines.append(">    this repo while being the least trustworthy one.")
    lines.append("> 3. **`unusual_options_flow: null` is not `false`.** Null means the flow screen")
    lines.append(">    did not run for this date; false means it ran and did not surface the name.")
    if data["notes"]:
        lines.append("> 4. **Deviations and degraded paths.**")
        for n in data["notes"]:
            lines.append(">    - %s" % n)
    lines.append("")

    lines.append("## Coverage — what this ledger actually knows")
    lines.append("")
    lines.append("| Routine | Rows it contributed to | Share |")
    lines.append("|---|---|---|")
    for k in ROUTINES:
        n = c["by_routine"][k]
        lines.append("| `%s` | %d | %.0f%% |" % (
            k, n, (100.0 * n / c["rows"]) if c["rows"] else 0))
    lines.append("")
    lines.append("| Field | Filled | Null |")
    lines.append("|---|---|---|")
    for f, v in c["fields"].items():
        lines.append("| `%s` | %d | %d |" % (f, v["filled"], v["null"]))
    lines.append("")
    lines.append("**What the coverage table means.** A low fill rate is not a fault in the")
    lines.append("ledger — it is the actual overlap between routines that screen different")
    lines.append("universes for different reasons. The daily sweep publishes 200 names, the")
    lines.append("in-play digest over a thousand, the earnings scanner only names that reacted to")
    lines.append("a print. A name in one and not the others is the normal case, and the point of")
    lines.append("this table is that the gap is now measurable instead of being invisible.")
    lines.append("")

    lines.append("### Catalyst coverage")
    lines.append("")
    lines.append("| Status | Rows | Meaning |")
    lines.append("|---|---|---|")
    meaning = {
        "sourced": "the scanner published a catalyst with a source",
        "not_looked_up": "the scanner states the lookup was outside its per-run budget",
        "absent": "the scanner had a row for the name but no catalyst text",
        "no_earnings_row": "the earnings scanner did not cover this name at all",
    }
    for k, v in sorted(c["catalyst_status"].items(), key=lambda kv: -kv[1]):
        lines.append("| `%s` | %d | %s |" % (k, v, meaning.get(k, "—")))
    lines.append("")
    lines.append("`not_looked_up` is the row that matters. **It is a budget decision, not a")
    lines.append("finding** — the scanner did not check, so the absence of a catalyst says")
    lines.append("nothing about whether one exists. No other artifact in this repo distinguishes")
    lines.append("those two cases, and a reader of a brief would reasonably assume the second.")
    lines.append("")

    multi = sorted((r for r in rows if r["n_routines"] >= 3),
                   key=lambda r: (-r["n_routines"],
                                  -(abs(r["settled_change_pct"]) if r["settled_change_pct"] is not None else -1)))
    lines.append("## Names three or more routines saw")
    lines.append("")
    if multi:
        lines.append("The rows where this artifact earns its place: a name several independent")
        lines.append("routines touched on the same session, with each routine's column beside the")
        lines.append("others.")
        lines.append("")
        lines.append("| Ticker | Seen by | Pre-mkt % | Settled chg % | Path | Tier | RVol | Flow | Catalyst |")
        lines.append("|---|---|---|---|---|---|---|---|---|")
        for r in multi[:40]:
            lines.append("| %s | %d | %s | %s | %s | %s | %s | %s | %s |" % (
                r["ticker"], r["n_routines"],
                "—" if r["pre_mkt_pct"] is None else "%+.2f" % r["pre_mkt_pct"],
                "—" if r["settled_change_pct"] is None else "%+.2f" % r["settled_change_pct"],
                ("`%s`" % r["gap_outcome"]) if r["gap_outcome"] else "—",
                r["in_play_tier"] or (",".join(r["screen_boards"]) if r["screen_boards"] else "—"),
                "—" if r["rvol"] is None else "%.2f" % r["rvol"],
                ("yes" if r["unusual_options_flow"] else "no")
                if r["unusual_options_flow"] is not None else "—",
                (r["catalyst_status"] or "—")))
        if len(multi) > 40:
            lines.append("")
            lines.append("*%d further row(s) in `ledger.jsonl`.*" % (len(multi) - 40))
    else:
        lines.append("No name on this date was seen by three or more routines.")
    lines.append("")

    lines.append("## How to read `ledger.jsonl`")
    lines.append("")
    lines.append("The first line is a `_meta` record carrying the sources, the coverage counts")
    lines.append("and the deviations. Every line after it is one name.")
    lines.append("")
    lines.append("```python")
    lines.append("import json")
    lines.append("with open('derived/%s/ledger.jsonl', encoding='utf-8') as fh:" % data["date"])
    lines.append("    meta = json.loads(fh.readline())['_meta']")
    lines.append("    rows = [json.loads(line) for line in fh]")
    lines.append("")
    lines.append("# names the flow screen surfaced AND the earnings scanner had a catalyst for")
    lines.append("both = [r for r in rows")
    lines.append("        if r['unusual_options_flow'] and r['catalyst_status'] == 'sourced']")
    lines.append("")
    lines.append("# where the ledger does not know, rather than knows 'no'")
    lines.append("print(meta['coverage']['fields']['catalyst'])")
    lines.append("```")
    lines.append("")
    return "\n".join(lines) + "\n"


def candidate_dates():
    dates = set(J.dated_dirs(SCREENS))
    root = os.path.join(J.REPO, EARNINGS)
    if os.path.isdir(root):
        for n in os.listdir(root):
            if n.endswith("-reactions.md") and J.DATE_RE.match(n[:10]):
                dates.add(n[:10])
    return sorted(d for d in dates if d >= "2026-10-22")


def main(argv):
    check_only = "--check" in argv
    for date in candidate_dates():
        data = build_one(date)
        if not data["rows"]:
            print("%s: no rows from any routine" % date)
            continue
        c = data["coverage"]
        if check_only:
            print("%s: %d rows, %d multi-routine, by_routine %s" % (
                date, c["rows"], c["multi_routine"], c["by_routine"]))
            continue
        target = os.path.join(J.REPO, OUT_ROOT, date)
        a = J.write_if_changed(os.path.join(target, "ledger.jsonl"), render_jsonl(data))
        b = J.write_if_changed(os.path.join(target, "ledger.md"), render_md(data))
        print("%s: jsonl %s · md %s (%d rows)" % (date, a, b, c["rows"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
