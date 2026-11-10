#!/usr/bin/env python3
"""Show what each routine saw, and where they agree.

Why: five routines publish a pre-market universe and each one sees a different
slice of the day. The 18:30 sweep publishes the convergence tier, the 09:00 gap
brief publishes the pre-market gaps, the 16:35 flow screen publishes the unusual
option positioning, the 06:00 reminder publishes the watchlist, and the 08:00
scanner publishes the earnings reactions. Every one of them is a column in
`ledger.md`, and none of them is a row.

The consequence is measurable. On 2026-11-06 the sweep's Tier-A list of eight
names had **zero** overlap with the gap brief's 58 names, **zero** with the flow
screen's 46, and one with the 06:00 reminders - while the 200-name master board
shared twelve names with the gap brief. Nothing else in the repo confirms the
names the sweep leads with, and a name seen by one routine looks exactly like a
name seen by five.

This makes that structure visible per session: for every name, how many
independent routines saw it, which ones, and what each of them said about it.

The families are NOT the same universe, and the artifact says so. The sweep
describes the PREVIOUS session's tape (its metrics are T+1), the gap brief
describes THIS morning's pre-market, and the flow screen describes the close.
A name can only appear in more than one if it persisted across that boundary,
which is the interesting case and the reason the count matters.

  python3 scripts/build_confirmation.py
  python3 scripts/build_confirmation.py --check
"""
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

SCREENS = "daily-screens"
EARNINGS = "earnings"
NTRT = "ntrt"
FLOW = "options-flow"
INPLAY = "us-stocks-in-play"
OUT_ROOT = "derived"

# The five families, and what each one contributes to the count.
FAMILIES = (
    ("screen", "the 18:30 sweep - Tier-A and Focus"),
    ("gap_brief", "the 09:00 pre-open gap brief (ntrt)"),
    ("options_flow", "the 16:35 unusual-options-flow screen"),
    ("reminders", "the 06:00 earnings-reminder watchlist"),
    ("reactions", "the 08:00 earnings-reaction scanner"),
)

# Words that are not tickers, so a table cell is not mistaken for one.
NOT_TICKER = {
    "TICKER", "SYMBOL", "NAME", "SIDE", "STRIKE", "EXPIRY", "DTE", "VOLUME",
    "OPEN", "INT", "V/OI", "CLOSE", "CHANGE", "GAP", "PRICE", "SHARE", "THEO",
    "LEVEL", "VOL", "OI", "CORR", "BAND", "PAIR", "MOVE", "OPT", "IV", "DATE",
    "TIME", "SESSION", "AD", "NET", "SLOPE", "ADL", "TICK", "CAT", "SRC", "WHY",
    "CONF", "REF", "PCT", "RANK", "SCORE", "MARKET", "CAP", "TYPE", "NOTES",
    "REASON", "STATUS", "SEC", "EST", "ACT", "SURPRISE", "WATCHLIST", "TOTAL",
}


def is_ticker(token):
    t = token.strip().strip("*").strip("`").strip()
    if not t or t.upper() in NOT_TICKER:
        return False
    if not re.fullmatch(r"[A-Z][A-Z.\-]{0,6}", t):
        return False
    # A cell that is a single capital letter is a column marker, not a ticker.
    return len(t) > 1


def md_tickers(path):
    """Every ticker-looking cell in a markdown table of a file."""
    out = set()
    if not os.path.exists(path):
        return out
    try:
        text = open(path, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError):
        return out
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        # Split on unescaped pipes only, so a cell carrying `\|corr\|` does
        # not shift the columns after it.
        for cell in J.split_row(s.strip("|")):
            c = cell.strip()
            if is_ticker(c):
                out.add(c)
                break
    return out


def csv_tickers(path):
    out = set()
    rows = J.read_csv_rows(path)
    if not rows:
        return out
    col, _note = J.ticker_column(rows)
    if not col:
        return out
    for row in rows:
        t = J.strip_md(row.get(col)).upper()
        if t:
            out.add(t)
    return out


def screen_names(date):
    """The sweep's published tiers, and the broader board behind them."""
    tiers = {}
    for board in ("tier-a", "focus"):
        tiers[board] = csv_tickers(os.path.join(J.REPO, SCREENS, date, board + ".csv"))
    tiers["master"] = csv_tickers(os.path.join(J.REPO, SCREENS, date, "master.csv"))
    return tiers


def build(date):
    tiers = screen_names(date)
    gap = md_tickers(os.path.join(J.REPO, NTRT, date + ".md"))
    flow = md_tickers(os.path.join(J.REPO, FLOW, date + ".md"))
    rem = md_tickers(os.path.join(J.REPO, EARNINGS, date + "-reminders.md"))
    react = md_tickers(os.path.join(J.REPO, EARNINGS, date + "-reactions.md"))

    sets = {
        "screen": tiers["tier-a"] | tiers["focus"],
        "gap_brief": gap,
        "options_flow": flow,
        "reminders": rem,
        "reactions": react,
    }
    master = tiers["master"]

    names = set()
    for v in sets.values():
        names |= v

    rows = []
    for t in sorted(names):
        seen = [k for k, v in sets.items() if t in v]
        on_master = t in master
        on_tier_a = t in tiers["tier-a"]
        on_focus = t in tiers["focus"]
        rows.append({
            "ticker": t,
            "families": seen,
            "n_families": len(seen),
            "on_master_board": on_master,
            "on_tier_a": on_tier_a,
            "on_focus": on_focus,
        })

    # The overlap structure, which is the point.
    pair_overlap = {}
    keys = list(sets)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            pair_overlap["%s & %s" % (a, b)] = sorted(sets[a] & sets[b])

    counts = {k: len(v) for k, v in sets.items()}
    hist = {}
    for r in rows:
        hist[r["n_families"]] = hist.get(r["n_families"], 0) + 1

    return {
        "date": date,
        "sets": sets,
        "counts": counts,
        "master_size": len(master),
        "rows": rows,
        "pair_overlap": pair_overlap,
        "histogram": hist,
        "union": len(names),
    }


def render(data):
    date = data["date"]
    counts = data["counts"]
    rows = data["rows"]
    lines = []
    lines.append("# Confirmation — how many routines saw each name")
    lines.append("")
    lines.append(J.provenance(
        "derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, "
        "options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md "
        "(no source file is modified)",
        "%d distinct name(s) across %d routines; %d on the 200-name master board"
        % (data["union"], len(FAMILIES), data["master_size"]),
        "read-only",
    ))
    lines.append("")
    lines.append("> **Read this before the table.**")
    lines.append(">")
    lines.append("> 1. **The five routines are not looking at the same thing, and that is the")
    lines.append(">    finding.** The sweep describes the PREVIOUS session's tape (its metrics")
    lines.append(">    are T+1), the gap brief describes THIS morning's pre-market, and the")
    lines.append(">    flow screen describes the close. A name can appear in more than one")
    lines.append(">    only if it persisted across that boundary.")
    lines.append("> 2. **A count of one is not a weak signal; it is an unconfirmed one.** It means")
    lines.append(">    no other routine saw the name, which is a fact worth having and not the")
    lines.append(">    same thing as the routine being wrong.")
    lines.append("> 3. **This artifact counts. It does not score.** No name is ranked, sized or")
    lines.append(">    recommended, and no name is called a setup.")
    lines.append("")

    lines.append("## What each routine published")
    lines.append("")
    lines.append("| Routine | What it is | Names |")
    lines.append("|---|---|---|")
    for key, desc in FAMILIES:
        lines.append("| `%s` | %s | %d |" % (key, desc, counts[key]))
    lines.append("| `master board` | the 200-name screen output the tiers are cut from | %d |" % data["master_size"])
    lines.append("")
    lines.append("The master board is not one of the five - it is the population the sweep's")
    lines.append("tiers are cut from, and it is the baseline for how much overlap a")
    lines.append("similarly-sized list would show by chance.")
    lines.append("")

    lines.append("## Where the routines agree")
    lines.append("")
    lines.append("| Pair | Shared names |")
    lines.append("|---|---|")
    for pair, names in sorted(data["pair_overlap"].items(), key=lambda kv: -len(kv[1])):
        lines.append("| %s | %d%s |" % (
            pair, len(names), (" — " + ", ".join(names[:10])) if names else ""))
    lines.append("")
    lines.append("## How many routines saw each name")
    lines.append("")
    lines.append("| Routines that saw the name | Names |")
    lines.append("|---|---|")
    for n in sorted(data["histogram"], reverse=True):
        lines.append("| %d | %d |" % (n, data["histogram"][n]))
    lines.append("")
    confirmed = data["histogram"].get(2, 0) + data["histogram"].get(3, 0) \
        + sum(v for k, v in data["histogram"].items() if k >= 4)
    lines.append("**%d of %d name(s) were seen by two or more routines.** The rest were seen" % (
        confirmed, data["union"]))
    lines.append("by exactly one, and which one is in the table below.")
    lines.append("")

    lines.append("## Names seen by more than one routine")
    lines.append("")
    multi = [r for r in rows if r["n_families"] >= 2]
    if not multi:
        lines.append("None on this date.")
    else:
        lines.append("| Ticker | Routines | On master board | Tier-A | Focus |")
        lines.append("|---|---|---|---|---|")
        for r in sorted(multi, key=lambda r: (-r["n_families"], r["ticker"])):
            lines.append("| %s | %s | %s | %s | %s |" % (
                r["ticker"], ", ".join(r["families"]),
                "yes" if r["on_master_board"] else "no",
                "yes" if r["on_tier_a"] else "no",
                "yes" if r["on_focus"] else "no"))
    lines.append("")

    lines.append("## Names seen by exactly one routine")
    lines.append("")
    lines.append("| Ticker | Routine | On master board | Tier-A | Focus |")
    lines.append("|---|---|---|---|---|")
    for r in sorted((r for r in rows if r["n_families"] == 1),
                    key=lambda r: (r["families"][0], r["ticker"])):
        lines.append("| %s | %s | %s | %s | %s |" % (
            r["ticker"], r["families"][0],
            "yes" if r["on_master_board"] else "no",
            "yes" if r["on_tier_a"] else "no",
            "yes" if r["on_focus"] else "no"))
    lines.append("")
    lines.append("## Method and caveats")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append("| Sources | 5 families, listed above |")
    lines.append("| Ticker extraction | the first ticker-shaped cell of every markdown table row, "
                 "and the ticker column of every CSV |")
    lines.append("| Counts | per family, per name; a name can be in a family's set even if "
                 "that family listed it in a table the reader would skip |")
    lines.append("")
    lines.append("**What this does not say.** It does not say the routines are wrong, and it")
    lines.append("does not say a name seen once is a better or worse setup. It says the repo")
    lines.append("currently contains no artifact that would tell you either.")
    lines.append("")
    return "\n".join(lines) + "\n"


CSV_COLS = ["ticker", "n_families", "families", "on_master_board", "on_tier_a", "on_focus"]


def render_csv(data):
    out = [",".join(CSV_COLS)]
    for r in sorted(data["rows"], key=lambda r: (-r["n_families"], r["ticker"])):
        out.append(",".join([
            r["ticker"], str(r["n_families"]), "|".join(r["families"]),
            "yes" if r["on_master_board"] else "no",
            "yes" if r["on_tier_a"] else "no",
            "yes" if r["on_focus"] else "no",
        ]))
    return "\n".join(out) + "\n"


def dates():
    out = []
    for date in J.dated_dirs(SCREENS):
        if os.path.exists(os.path.join(J.REPO, SCREENS, date, "tier-a.csv")):
            out.append(date)
    return out


def main(argv):
    check_only = "--check" in argv
    for date in dates():
        data = build(date)
        if check_only:
            print("%s: %d names, %d seen by 2+, counts %s" % (
                date, data["union"],
                sum(1 for r in data["rows"] if r["n_families"] >= 2),
                data["counts"]))
            continue
        target = os.path.join(J.REPO, OUT_ROOT, date)
        a = J.write_if_changed(os.path.join(target, "confirmation.md"), render(data))
        b = J.write_if_changed(os.path.join(target, "confirmation.csv"), render_csv(data))
        print("%s: md %s · csv %s" % (date, a, b))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
