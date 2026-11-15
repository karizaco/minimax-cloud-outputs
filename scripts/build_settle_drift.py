#!/usr/bin/env python3
"""How far did the 08:00 ET EU/UK move travel by the close? A running record.

Why: cron #15 publishes the EU/UK session MID-FLIGHT at 08:00 ET (the session
closes 11:30 ET in winter), so every EU move in the morning artifact is a
snapshot. Since 2026-11-11 the 12:15 ET settlement pass (#15b) republishes the
same rows with their settled move and prints a one-line `scan_to_settle`
summary. But each summary lives in its own day's file: nobody can see whether
the drift is systematic, which markets drift most, or whether reactions tend
to extend or fade between the two prints. This view pools them.

What it reads:
  earnings/<date>-reactions-settled.md   the settled table: Ticker, Market,
                                         Chg % (settled), Move @08:00, Δ vs scan
  earnings/<date>-reactions.md           the morning EU/UK table - read only to
                                         COUNT the morning rows the settle
                                         table does not republish

THE SELECTION TRAP this view states rather than hides. The settle pass
re-selects its rows by the SETTLED move, so a morning row whose reaction faded
below the cut is simply not in the settled table - its drift is never measured
- while a name that grew into the table appears with no morning move. The
matched set is therefore biased toward reactions that stayed large, and the
measured drift UNDERSTATES fading. The coverage table counts both kinds of
unmatched row per session, and the brief says so above the first table.

Paths (descriptive labels for the path between two prints, nothing more):
  held      |settled - scan| <= 1pp (the same 1pp line the scanner uses)
  extended  moved more than 1pp further in the morning move's direction
  faded     moved more than 1pp back toward zero, without changing sign
  reversed  moved more than 1pp and changed sign

  python3 scripts/build_settle_drift.py
  python3 scripts/build_settle_drift.py --check
"""
import csv
import io
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

OUT_ROOT = "derived"
FAMILY = "earnings"
SETTLED_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-reactions-settled\.md$")

# The scanner's own line: its settle summary counts rows "more than 1pp apart".
# Using the same line keeps this view's counts comparable with the artifact's.
DRIFT_LINE_PP = 1.0
# Below this many matched rows a per-market figure is printed but marked as
# too few to read: one large mover would set the median on its own.
MIN_ROWS_TO_READ = 5

PUBLISHED_SUMMARY_RE = re.compile(
    r"scan_to_settle:\s*(\d+) rows compared with the 08:00 ET scan"
    r"(?:, median drift ([\d.]+)pp, max ([\d.]+)pp, (\d+) rows more than 1pp apart)?")
VERSION_RE = re.compile(r"^- pipeline_version:\s*(\S+)", re.M)


def path_of(scan, settled):
    """held / extended / faded / reversed for one row (see the module doc)."""
    delta = settled - scan
    if abs(delta) <= DRIFT_LINE_PP:
        return "held"
    if scan != 0 and settled != 0 and (scan > 0) != (settled > 0):
        return "reversed"
    # A zero morning move has no direction; any move away from it is growth.
    if abs(settled) > abs(scan):
        return "extended"
    return "faded"


def _read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return None


def morning_tickers(date):
    """The morning EU/UK table's tickers, or None when there is no morning file."""
    text = _read(os.path.join(J.REPO, FAMILY, "%s-reactions.md" % date))
    if text is None:
        return None
    _start, _header, rows = J.table_after(text, "EU/UK — Headline", "Ticker", "Chg %")
    return [J.strip_md(r.get("Ticker")) for r in rows if J.strip_md(r.get("Ticker"))]


def read_session(date, name):
    """One settled artifact -> its compared rows, coverage and published summary."""
    text = _read(os.path.join(J.REPO, FAMILY, name)) or ""
    _start, header, rows = J.table_after(text, "EU/UK — Settled", "Ticker", "Market",
                                         "Chg %", "Move @08:00")
    delta_col = next((h for h in header if h.lower().endswith("vs scan")), None)
    compared, new_at_settle, settled_tickers, bad_delta = [], [], [], 0
    for r in rows:
        ticker = J.strip_md(r.get("Ticker"))
        if not ticker:                      # the "| — | — |" empty-table placeholder
            continue
        settled_tickers.append(ticker)
        settled = J.to_float(r.get("Chg %"))
        scan = J.to_float(r.get("Move @08:00"))
        if settled is None:
            continue
        if scan is None:
            # Grew into the settled table: there is no morning move to compare.
            new_at_settle.append(ticker)
            continue
        delta = settled - scan
        published = J.to_float(r.get(delta_col)) if delta_col else None
        # The artifact prints Δ to 2 decimals; anything beyond rounding means
        # the artifact's own columns disagree, which this view must say.
        if published is not None and abs(published - delta) > 0.011:
            bad_delta += 1
        compared.append({
            "date": date, "ticker": ticker,
            "market": J.strip_md(r.get("Market")) or "?",
            "venue": J.strip_md(r.get("Venue")),
            "scan_move_pct": scan, "settled_move_pct": settled,
            "delta_pp": round(delta, 2), "abs_drift_pp": round(abs(delta), 2),
            "path": path_of(scan, settled),
        })

    morning = morning_tickers(date)
    published = PUBLISHED_SUMMARY_RE.search(text)
    version = VERSION_RE.search(text)
    return {
        "date": date, "file": "%s/%s" % (FAMILY, name),
        "pipeline_version": version.group(1) if version else None,
        "rows": compared,
        "settled_rows": len(settled_tickers),
        "new_at_settle": new_at_settle,
        "morning_found": morning is not None,
        "morning_rows": len(morning) if morning is not None else None,
        "morning_absent": (sorted(set(morning) - set(settled_tickers))
                           if morning is not None else None),
        "bad_delta": bad_delta,
        "table_found": bool(header),
        "published": {
            "matched": int(published.group(1)) if published else None,
            "median": float(published.group(2)) if published and published.group(2) else None,
            "max": float(published.group(3)) if published and published.group(3) else None,
            "over_1pp": int(published.group(4)) if published and published.group(4) else None,
        },
    }


def summarise(rows):
    """Aggregate a list of compared rows. Empty input -> counts of zero, no stats."""
    drifts = [r["abs_drift_pp"] for r in rows]
    paths = {p: sum(1 for r in rows if r["path"] == p)
             for p in ("held", "extended", "faded", "reversed")}
    over = sum(1 for d in drifts if d > DRIFT_LINE_PP)
    return {
        "n": len(rows),
        # The TRUE median (the mean of the two middle values for an even count).
        # The artifact's own summary takes the upper-middle value instead, so
        # the two can differ slightly on an even count; both are printed.
        "median": round(statistics.median(drifts), 2) if drifts else None,
        "max": round(max(drifts), 2) if drifts else None,
        "over": over,
        "over_share": round(100.0 * over / len(drifts), 1) if drifts else None,
        "paths": paths,
    }


def build():
    root = os.path.join(J.REPO, FAMILY)
    names = sorted(n for n in os.listdir(root) if SETTLED_RE.match(n)) \
        if os.path.isdir(root) else []
    sessions = [read_session(SETTLED_RE.match(n).group(1), n) for n in names]
    rows = [r for s in sessions for r in s["rows"]]
    markets = {}
    for r in rows:
        markets.setdefault(r["market"], []).append(r)
    return {
        "sessions": sessions,
        "rows": rows,
        "pooled": summarise(rows),
        "by_session": [(s, summarise(s["rows"])) for s in sessions],
        "by_market": sorted(((m, summarise(rs)) for m, rs in markets.items()),
                            key=lambda kv: (-kv[1]["n"], kv[0])),
    }


# ---------------------------------------------------------------- rendering

def _f(v, fmt="%.2f"):
    return "—" if v is None else fmt % v


def _paths(p):
    return "%d / %d / %d / %d" % (p["held"], p["extended"], p["faded"], p["reversed"])


def render(data):
    sessions, pooled = data["sessions"], data["pooled"]
    dates = [s["date"] for s in sessions]
    morning_known = [s for s in sessions if s["morning_found"]]
    absent = sum(len(s["morning_absent"]) for s in morning_known)
    morning_total = sum(s["morning_rows"] for s in morning_known)
    new_total = sum(len(s["new_at_settle"]) for s in sessions)
    missing_morning = [s["date"] for s in sessions if not s["morning_found"]]
    bad = sum(s["bad_delta"] for s in sessions)

    L = []
    A = L.append
    A("# Settle drift — how far the 08:00 ET EU/UK move travelled by the close")
    A("")
    A(J.provenance(
        "derived read of `earnings/<date>-reactions-settled.md` (the 12:15 ET settlement "
        "pass) and the morning `earnings/<date>-reactions.md`; no source file is modified",
        ("%d settle session(s), %s → %s; %d compared row(s)"
         % (len(sessions), dates[0], dates[-1], pooled["n"])) if sessions
        else "no settle session found",
        "read-only"))
    A("")
    A("> **Read this before the tables.**")
    A(">")
    A("> 1. **The comparison only covers rows that are in BOTH tables, and that set is")
    A(">    biased.** The settle pass re-selects its rows by the SETTLED move, so a morning")
    A(">    row whose reaction faded below the cut is not republished and its drift is never")
    if morning_known:
        A(">    measured: **%d of %d morning EU/UK row(s) (%s) were not in the settled table.**"
          % (absent, morning_total,
             _f(100.0 * absent / morning_total, "%.0f%%") if morning_total else "—"))
    else:
        A(">    measured (no morning artifact was readable, so that count is unavailable).")
    A(">    The measured drift therefore UNDERSTATES fading. %d settled row(s) grew into the"
      % new_total)
    A(">    table with no morning move and are not compared either.")
    A("> 2. **Small sample.** %d session(s). A per-market figure with fewer than %d rows"
      % (len(sessions), MIN_ROWS_TO_READ))
    A(">    is printed but marked *too few to read* - one large mover sets its median.")
    A("> 3. **Descriptive only.** `held`, `extended`, `faded` and `reversed` describe the")
    A(">    path between two prints. Nothing here is a direction, a size or a recommendation.")
    # Conditional notes are numbered as they are emitted, so the list never
    # skips a number when an earlier conditional note does not apply.
    n = 3
    if missing_morning:
        n += 1
        A("> %d. **Morning artifact missing for %s** - those sessions' coverage counts are"
          % (n, ", ".join(missing_morning)))
        A(">    unavailable; their compared rows still come from the settled table's own")
        A(">    `Move @08:00` column.")
    if bad:
        n += 1
        A("> %d. **%d row(s) whose published `Δ vs scan` disagrees with `Chg %% - Move @08:00`**"
          % (n, bad))
        A(">    beyond rounding. This view recomputes Δ from the two moves.")
    A("")

    A("## Summary — every session pooled")
    A("")
    A("| Sessions | Compared rows | Median abs drift (pp) | Max (pp) | Rows > %gpp | "
      "Held / extended / faded / reversed |" % DRIFT_LINE_PP)
    A("|---|---|---|---|---|---|")
    A("| %d | %d | %s | %s | %d (%s) | %s |" % (
        len(sessions), pooled["n"], _f(pooled["median"]), _f(pooled["max"]),
        pooled["over"], _f(pooled["over_share"], "%.1f%%"), _paths(pooled["paths"])))
    A("")
    if pooled["n"]:
        p = pooled["paths"]
        A("**What this shows.** Of the %d EU/UK rows that appear in both the 08:00 ET scan "
          "and the 12:15 ET settle pass, %d (%s) ended more than %gpp away from the move the "
          "morning artifact printed. Of those, %d extended, %d faded and %d reversed. The "
          "morning EU/UK move is a snapshot, and this is how far the snapshot was from the "
          "session's result."
          % (pooled["n"], pooled["over"], _f(pooled["over_share"], "%.1f%%"), DRIFT_LINE_PP,
             p["extended"], p["faded"], p["reversed"]))
        A("")
        A("**What it does not show.** It is not the drift of *every* morning row - see note 1 "
          "above: the rows that faded out of the settle table are missing, so fading is "
          "under-counted. **The extended-versus-faded split is the number that selection "
          "distorts most**: a table re-selected by the settled move keeps the reactions that "
          "grew and loses the ones that shrank, so a lopsided split here is what the method "
          "would produce even if reactions faded as often as they extended. Do not read it as "
          "a tendency. It also says nothing about the US rows, which the settle pass does not "
          "republish (the US session is open at 12:15 ET).")
    else:
        A("No compared rows yet.")
    A("")

    A("## By session")
    A("")
    A("| Session | Compared | Median abs drift (pp) | Artifact's median | Max (pp) | "
      "Rows > %gpp | Held / ext / faded / rev | Pipeline |" % DRIFT_LINE_PP)
    A("|---|---|---|---|---|---|---|---|")
    for s, agg in data["by_session"]:
        A("| %s | %d | %s | %s | %s | %d (%s) | %s | %s |" % (
            s["date"], agg["n"], _f(agg["median"]), _f(s["published"]["median"]),
            _f(agg["max"]), agg["over"], _f(agg["over_share"], "%.0f%%"),
            _paths(agg["paths"]), s["pipeline_version"] or "—"))
    A("")
    A("**How to read it.** The *Artifact's median* is the figure the settle pass printed in "
      "its own `scan_to_settle` line. It takes the upper-middle value on an even count, while "
      "this view takes the true median, so the two can differ by a few hundredths on an even "
      "count; a larger gap would mean the two read different rows. A session-to-session swing "
      "in the median is not, on its own, a trend: each session has 15-25 compared rows.")
    A("")

    A("## By market — every session pooled")
    A("")
    A("| Market | Compared | Median abs drift (pp) | Max (pp) | Rows > %gpp | "
      "Held / ext / faded / rev | Readable? |" % DRIFT_LINE_PP)
    A("|---|---|---|---|---|---|---|")
    for m, agg in data["by_market"]:
        A("| %s | %d | %s | %s | %d (%s) | %s | %s |" % (
            m, agg["n"], _f(agg["median"]), _f(agg["max"]), agg["over"],
            _f(agg["over_share"], "%.0f%%"), _paths(agg["paths"]),
            "yes" if agg["n"] >= MIN_ROWS_TO_READ else "too few to read"))
    A("")
    A("**How to read it.** A market's drift mixes two things this table cannot separate: how "
      "much of the session was still to run at 08:00 ET (close times differ by venue - most "
      "close at 11:30 ET in winter, a few earlier) and which names the per-market cap let "
      "into the table. A high figure on a thin row count is one name, not a market property.")
    A("")

    A("## Coverage — morning table vs settled table")
    A("")
    A("| Session | Morning EU/UK rows | Settled rows | Compared | New at settle | "
      "Morning rows not republished |")
    A("|---|---|---|---|---|---|")
    for s in sessions:
        A("| %s | %s | %d | %d | %d | %s |" % (
            s["date"], "—" if s["morning_rows"] is None else s["morning_rows"],
            s["settled_rows"], len(s["rows"]), len(s["new_at_settle"]),
            "— (no morning file)" if s["morning_absent"] is None
            else "%d%s" % (len(s["morning_absent"]),
                           (" (" + ", ".join(s["morning_absent"][:8])
                            + (", ..." if len(s["morning_absent"]) > 8 else "") + ")")
                           if s["morning_absent"] else "")))
    A("")
    A("**What the last column means.** These morning rows had a printed 08:00 ET move and "
      "no settled move in this view. Most fell below the settle pass's selection cut, and some "
      "may have been dropped by its reference-close gate. Their drift is unknown here, not zero.")
    A("")

    A("## Every compared row")
    A("")
    A("| Session | Ticker | Market | Move @08:00 | Settled | Δ (pp) | Path |")
    A("|---|---|---|---|---|---|---|")
    for r in sorted(data["rows"], key=lambda r: (r["date"], -r["abs_drift_pp"], r["ticker"])):
        A("| %s | %s | %s | %+.2f | %+.2f | %+.2f | %s |" % (
            r["date"], r["ticker"], r["market"], r["scan_move_pct"],
            r["settled_move_pct"], r["delta_pp"], r["path"]))
    A("")

    A("## Method & caveats")
    A("")
    A("| Field | Value |")
    A("|---|---|")
    A("| Drift | `Chg %` (settled) minus `Move @08:00`, recomputed from the two moves |")
    A("| Drift line | %gpp - the line the scanner's own settle summary uses |" % DRIFT_LINE_PP)
    A("| Paths | held ≤ %gpp; otherwise reversed (sign change), extended (further from zero), "
      "faded (back toward zero) |" % DRIFT_LINE_PP)
    A("| Median | the true median; the artifact prints the upper-middle value |")
    A("| Readable market | at least %d compared rows |" % MIN_ROWS_TO_READ)
    A("| Not covered | the US rows (open at 12:15 ET), and the ASX and APAC/Gulf rows (already settled at 08:00 ET) |")
    A("")

    A("## Source health")
    A("")
    A("| Session | Settled file | Settled table | Morning file | Δ disagreements |")
    A("|---|---|---|---|---|")
    for s in sessions:
        A("| %s | `%s` | %s | %s | %d |" % (
            s["date"], s["file"], "found" if s["table_found"] else "**NOT FOUND**",
            "found" if s["morning_found"] else "**missing**", s["bad_delta"]))
    if not sessions:
        A("| — | no `earnings/<date>-reactions-settled.md` found | — | — | — |")
    A("")
    return "\n".join(L) + "\n"


CSV_COLS = ["date", "ticker", "market", "venue", "scan_move_pct", "settled_move_pct",
            "delta_pp", "abs_drift_pp", "path"]


def render_csv(data):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(CSV_COLS)
    for r in sorted(data["rows"], key=lambda r: (r["date"], r["ticker"])):
        w.writerow([r[c] for c in CSV_COLS])
    return buf.getvalue()


def main(argv):
    check_only = "--check" in argv
    data = build()
    p = data["pooled"]
    if check_only:
        print("settle sessions: %d | compared rows: %d | median %s pp | > %gpp: %d"
              % (len(data["sessions"]), p["n"], _f(p["median"]), DRIFT_LINE_PP, p["over"]))
        return 0
    a = J.write_if_changed(os.path.join(J.REPO, OUT_ROOT, "settle-drift.md"), render(data))
    b = J.write_if_changed(os.path.join(J.REPO, OUT_ROOT, "settle-drift.csv"), render_csv(data))
    print("settle-drift.md %s · settle-drift.csv %s (%d sessions, %d compared rows)"
          % (a, b, len(data["sessions"]), p["n"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
