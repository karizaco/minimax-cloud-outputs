#!/usr/bin/env python3
"""Build the persistence layer for the daily screens: how long a name stays on the board.

Why: every dated screen is a snapshot that does not know what yesterday's snapshot
said. A reader opening today's Tier-A list cannot tell a name that has been
converging for a week from one that appeared this morning and will be gone
tomorrow - and that distinction is the whole point of a convergence screen.

Measured before building this: across the 12 dates of `tier-a.csv` (2026-10-22
through 2026-11-06) the most persistent name appeared 4 times and the majority
appeared exactly once. The screen is finding recurring names and the artifact
hides it.

What this writes:
  derived/persistence.json   machine record, one entry per name
  derived/persistence.md     the same join, read as prose + tables

It writes into `derived/` rather than into `daily-screens/`, because every file
under `daily-screens/<date>/` is a cron product and this is not one. Keeping the
derived views in their own tree means a routine's own file-set logic never has to
account for a file no routine wrote.

It does NOT edit `daily-sweep.md`. That file is a cron product; a builder
writing into it would mean two writers on one artifact. The streak column lives
here instead, and the sweep can take it when the routine itself asks for it.

Drift it has to tolerate: the ticker column is `symbol`, `ticker` or `name`
depending on the date, and 2026-10-19 published `tier-a.md` with zero rows
because the run was degraded. A date with no readable CSV is reported in
`boards.skipped`, not silently dropped.

  python3 scripts/build_persistence.py            # write both files
  python3 scripts/build_persistence.py --check    # report only, write nothing
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

SCREENS = "daily-screens"
OUT_ROOT = "derived"
BOARDS = ("tier-a", "focus")


def read_board(date):
    """One dated board: its tickers and the column that held them."""
    path = os.path.join(J.REPO, SCREENS, date, "tier-a.csv")
    out = {}
    for board in BOARDS:
        p = os.path.join(J.REPO, SCREENS, date, board + ".csv")
        rows = J.read_csv_rows(p)
        col, note = J.ticker_column(rows)
        out[board] = {
            "tickers": J.tickers_from(rows),
            "rows": len(rows),
            "ticker_column": col,
            "ticker_column_note": note,
            "present": os.path.exists(p),
        }
    return out


def streaks(dates, appearances):
    """Run lengths over the list of board dates on which the name appeared.

    A streak is consecutive *board dates*, not calendar days: a weekend is not a
    gap, because no board was published for it. A date that published a board
    without the name does break the run.
    """
    index = {d: i for i, d in enumerate(dates)}
    positions = sorted(index[d] for d in appearances if d in index)
    if not positions:
        return {"current": 0, "longest": 0, "at_exit": 0}
    longest = run = 1
    for a, b in zip(positions, positions[1:]):
        if b == a + 1:
            run += 1
            longest = max(longest, run)
        else:
            run = 1
    last_is_latest = positions[-1] == len(dates) - 1
    current = run if last_is_latest else 0
    return {"current": current, "longest": longest, "at_exit": run}


def build():
    dirs = J.dated_dirs(SCREENS)
    boards, skipped, counted = {}, [], []
    for date in dirs:
        info = read_board(date)
        boards[date] = info
        if info["tier-a"]["present"] and info["tier-a"]["ticker_column"]:
            counted.append(date)
        else:
            reason = "no tier-a.csv" if not info["tier-a"]["present"] else "no readable ticker column"
            if os.path.exists(os.path.join(J.REPO, SCREENS, date, "tier-a.md")):
                reason += " (tier-a.md exists - the run published no rows)"
            skipped.append({"date": date, "reason": reason})

    names = {}
    for board in BOARDS:
        per_name = {}
        for date in counted:
            for t in boards[date][board]["tickers"]:
                per_name.setdefault(t, []).append(date)
        for t, dates in per_name.items():
            entry = names.setdefault(t, {"ticker": t})
            s = streaks(counted, dates)
            entry[board] = {
                "days": len(dates),
                "first": dates[0],
                "last": dates[-1],
                "dates": dates,
                "streak_current": s["current"],
                "streak_longest": s["longest"],
                "streak_at_exit": s["at_exit"],
            }

    latest = counted[-1] if counted else None
    previous = counted[-2] if len(counted) > 1 else None
    arrivals, departures = [], []
    if latest and previous:
        for board in BOARDS:
            now = set(boards[latest][board]["tickers"])
            was = set(boards[previous][board]["tickers"])
            for t in sorted(now - was):
                arrivals.append({"ticker": t, "board": board, "date": latest})
            for t in sorted(was - now):
                entry = names.get(t, {}).get(board, {})
                departures.append({
                    "ticker": t, "board": board, "date": latest,
                    "last_seen": entry.get("last"),
                    "streak_at_exit": entry.get("streak_at_exit"),
                    "days": entry.get("days"),
                })

    coverage = {"tier-a": 0, "focus": 0}
    for board in BOARDS:
        coverage[board] = sum(1 for d in counted if boards[d][board]["present"])

    record = {
        "_schema": "daily-screens-persistence-v1",
        "derived_from": "daily-screens/<date>/{tier-a,focus}.csv",
        "join": "one row per ticker per board; no value is inferred, only counted",
        "boards": {
            "counted": counted,
            "skipped": skipped,
            "latest": latest,
            "previous": previous,
            "per_board_file_count": coverage,
        },
        "names": {t: names[t] for t in sorted(names)},
        "arrivals": arrivals,
        "departures": departures,
        "notes": [
            "A streak is consecutive board dates, not calendar days. A weekend is not a "
            "gap; a date that published a board without the name is.",
            "streak_current is 0 for a name that is not on the latest board. "
            "streak_at_exit holds the run it was on when it left.",
            "2026-10-19 published tier-a.md with zero rows because the run was degraded "
            "and every MCP was unregistered; it is in boards.skipped, not counted as a "
            "board, so a streak that spans it is not broken by a run that never saw data.",
        ],
    }
    return record, boards


def render(record, boards):
    counted = record["boards"]["counted"]
    latest = record["boards"]["latest"]
    names = record["names"]
    lines = []
    lines.append("# Persistence — how long a name stays on the board")
    lines.append("")
    lines.append(J.provenance(
        "derived join over daily-screens/<date>/{tier-a,focus}.csv (no source file is modified)",
        "boards dated %s → %s (%d dates)" % (
            counted[0] if counted else "—", counted[-1] if counted else "—", len(counted)),
        "read-only",
    ))
    lines.append("")
    lines.append("> **Deviations, stated up front.**")
    lines.append("> ")
    lines.append("> 1. **This file is not written by a cron.** It is derived from artifacts that are.")
    lines.append(">    It is as current as the newest dated directory when it was built, and it will not")
    lines.append(">    update itself when the next screen lands. Regenerate with")
    lines.append(">    `python3 scripts/build_persistence.py`.")
    lines.append("> 2. **It does not modify `daily-sweep.md`.** The streak column a reader wants in the")
    lines.append(">    sweep lives here instead, because that file is a cron product and this builder")
    lines.append(">    must not become a second writer on it.")
    lines.append("> 3. **%s date(s) published no readable Tier-A board** and are not counted" % len(record["boards"]["skipped"]))
    lines.append(">    as boards — see *Coverage* below. A streak spanning one of them is not broken")
    lines.append(">    by a run that produced nothing.")
    lines.append("")
    lines.append("## What this says")
    lines.append("")
    top = sorted(
        (v for v in names.values() if v.get("tier-a")),
        key=lambda v: (-v["tier-a"]["days"], -v["tier-a"]["streak_longest"], v["ticker"]),
    )[:10]
    if top:
        lines.append("Across %d Tier-A boards the names that recur are:" % len(counted))
        lines.append("")
        lines.append("| Ticker | Days on Tier-A | First seen | Last seen | Current streak | Longest streak |")
        lines.append("|---|---|---|---|---|---|")
        for v in top:
            ta = v["tier-a"]
            lines.append("| %s | %d | %s | %s | %d | %d |" % (
                v["ticker"], ta["days"], ta["first"], ta["last"],
                ta["streak_current"], ta["streak_longest"]))
        lines.append("")
        lines.append("The table above is a **count of appearances**, not a judgement about the names.")
        lines.append("A name on a long streak has been converging across several screens; a name with")
        lines.append("`days 1` appeared once and may not be back. The two are different signals and a")
        lines.append("single-day sweep cannot tell them apart.")
        lines.append("")

    if latest and record["arrivals"]:
        lines.append("### New to the %s board" % latest)
        lines.append("")
        lines.append("| Ticker | Board |")
        lines.append("|---|---|")
        for a in record["arrivals"]:
            lines.append("| %s | %s |" % (a["ticker"], a["board"]))
        lines.append("")
    if latest and record["departures"]:
        lines.append("### Off the board as of %s" % latest)
        lines.append("")
        lines.append("The mirror of the arrivals table: what left, and after how long.")
        lines.append("")
        lines.append("| Ticker | Board | Last seen | Streak at exit | Days on board |")
        lines.append("|---|---|---|---|---|")
        for d in record["departures"]:
            lines.append("| %s | %s | %s | %s | %s |" % (
                d["ticker"], d["board"], d["last_seen"],
                d["streak_at_exit"] if d["streak_at_exit"] is not None else "—",
                d["days"] if d["days"] is not None else "—"))
        lines.append("")

    lines.append("## The latest board, with streaks")
    lines.append("")
    if latest:
        rows = boards[latest]["tier-a"]["tickers"]
        lines.append("Tier-A on %s, with the persistence column a sweep table does not carry." % latest)
        lines.append("")
        lines.append("| Ticker | Days on Tier-A | Current streak | Longest streak | Focus days |")
        lines.append("|---|---|---|---|---|")
        for t in rows:
            v = names.get(t, {})
            ta = v.get("tier-a", {})
            fo = v.get("focus", {})
            lines.append("| %s | %s | %s | %s | %s |" % (
                t,
                ta.get("days", "—"),
                ta.get("streak_current", "—"),
                ta.get("streak_longest", "—"),
                fo.get("days", "—")))
        lines.append("")
    else:
        lines.append("No readable Tier-A board was found.")
        lines.append("")

    lines.append("## Coverage")
    lines.append("")
    lines.append("| Board | Dated directories | Readable boards |")
    lines.append("|---|---|---|")
    total = len(record["boards"]["counted"]) + len(record["boards"]["skipped"])
    for board in BOARDS:
        lines.append("| %s | %d | %d |" % (board, total, record["boards"]["per_board_file_count"][board]))
    lines.append("")
    if record["boards"]["skipped"]:
        lines.append("Dates that published no readable Tier-A board:")
        lines.append("")
        lines.append("| Date | Why it is not counted |")
        lines.append("|---|---|")
        for s in record["boards"]["skipped"]:
            lines.append("| %s | %s |" % (s["date"], s["reason"]))
        lines.append("")
    lines.append("## How to read it")
    lines.append("")
    lines.append("`persistence.json` beside this file carries the same join with every date a")
    lines.append("name appeared.")
    lines.append("The rule for this artifact is the one the decision-record contract states:")
    lines.append("**it joins, it does not restate.** Every value here is a count or a date copied")
    lines.append("from a dated CSV. No name is scored, ranked or interpreted.")
    lines.append("")
    lines.append("Column drift the builder tolerates, and reports rather than hides: the ticker is")
    lines.append("`symbol` on 2026-10-22/23 and 2026-11-04 onward, `ticker` on 2026-10-28 through")
    lines.append("2026-11-03, and `name` on 2026-10-26/27 where that column holds symbols.")
    lines.append("")
    return "\n".join(lines) + "\n"


def main(argv):
    check_only = "--check" in argv
    record, boards = build()
    md = render(record, boards)
    if check_only:
        print("boards counted: %d" % len(record["boards"]["counted"]))
        print("boards skipped: %d" % len(record["boards"]["skipped"]))
        print("names tracked:  %d" % len(record["names"]))
        print("arrivals %d, departures %d" % (len(record["arrivals"]), len(record["departures"])))
        return 0
    a = J.write_json(os.path.join(J.REPO, OUT_ROOT, "persistence.json"), record)
    b = J.write_if_changed(os.path.join(J.REPO, OUT_ROOT, "persistence.md"), md)
    print("persistence.json %s · persistence.md %s" % (a, b))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
