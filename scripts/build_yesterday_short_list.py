#!/usr/bin/env python3
"""Did yesterday's short list show up in this morning's pre-market feed?

Why: the evening sweep's Tier-A list and the morning gap brief are different
jobs. Hoping they overlap is the wrong question. The useful question is the
follow-up: for each name the sweep led with last session, did this morning's
feed have it, and was it gapping, under the 3% line, or absent?

This is that follow-up, reconstructed from the artifacts. The 09:00 routine is
told to publish the same check itself; this builder is the historical copy, so
a morning that fired before the instruction changed still has an answer.

It reads EVERY morning feed, not one of them. Each feed quotes a different
slice of the tape - the brief's own screen, the gap brief's 3% band, the
pre-open tape - so a name can be in one and not another, and reading only the
band made every quiet name look like nobody quoted it. The order is by clock,
newest print first, because "was it gapping?" is answered by the most recent
print, and every row names the feed its print came from.

  python3 scripts/build_yesterday_short_list.py
  python3 scripts/build_yesterday_short_list.py --check
"""
import csv
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

NTRT = "ntrt"
SCREENS = "daily-screens"
BRIEFS = "daily-briefs"
PREOPEN = "preopen-feed"
OUT_ROOT = "derived"

# The morning brief's own gate. Under this, a print is in the feed but is not
# a gap the brief would lead with.
GAP_LINE = 3.0


def screen_dates():
    out = []
    for date in J.dated_dirs(SCREENS):
        if os.path.exists(os.path.join(J.REPO, SCREENS, date, "tier-a.csv")):
            out.append(date)
    return out


def morning_dates():
    out = []
    root = os.path.join(J.REPO, NTRT)
    if not os.path.isdir(root):
        return out
    for name in sorted(os.listdir(root)):
        if name.endswith(".csv") and J.DATE_RE.match(name[:10]):
            out.append(name[:10])
    return out


def prior_short_list(morning):
    """The last Tier-A board published before this morning.

    That is the list the 09:00 brief can actually see: the previous evening's
    sweep, not a screen that has not been written yet.
    """
    earlier = [d for d in screen_dates() if d < morning]
    if not earlier:
        return None, [], None
    date = earlier[-1]
    rows = J.read_csv_rows(os.path.join(J.REPO, SCREENS, date, "tier-a.csv"))
    col, note = J.ticker_column(rows)
    names = []
    if col:
        for row in rows:
            t = J.strip_md(row.get(col)).upper()
            if t:
                names.append({
                    "ticker": t,
                    "stylists": J.strip_md(row.get("stylists") or row.get("origins")),
                    "yesterday_change": J.to_float(
                        row.get("today_change") or row.get("chg_pct_resolved")),
                })
    return date, names, note


def brief_quotes(date):
    """The morning brief's own screen: every name it quoted, with its print.

    This is the fullest morning feed the repo holds - the CSV behind every
    table the brief publishes. Its percent column is spelled two ways across
    the archive (`premarket_change_pct` and `gap_pct`), so both are tried.
    The prior session's own change columns are NOT the pre-market print and
    are deliberately not read.
    """
    path = os.path.join(J.REPO, BRIEFS, date + "-pre-market.csv")
    if not os.path.exists(path):
        return {}
    rows = J.read_csv_rows(path)
    col, _note = J.ticker_column(rows)
    if not col:
        return {}
    out = {}
    for row in rows:
        t = J.strip_md(row.get(col)).upper()
        if not t:
            continue
        pct = J.to_float(row.get("premarket_change_pct"))
        if pct is None:
            pct = J.to_float(row.get("gap_pct"))
        if pct is not None:
            out[t] = pct
    return out


def ntrt_quotes(date):
    path = os.path.join(J.REPO, NTRT, date + ".csv")
    out = {}
    if not os.path.exists(path):
        return out
    for row in J.read_csv_rows(path):
        t = J.strip_md(row.get("ticker")).upper()
        if t:
            out[t] = J.to_float(row.get("premarket_change_pct"))
    return out


def preopen_quotes(date):
    """The pre-open tape for that morning, one pct per ticker.

    Every checkpoint is read, and a later checkpoint wins over an earlier one
    for the same ticker. The `pct` field is already a number, so it is not
    run through the string parser.
    """
    paths = sorted(glob.glob(os.path.join(J.REPO, PREOPEN, date + "-*.jsonl")))
    out = {}
    used = []
    for path in paths:
        used.append(os.path.basename(path))
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except ValueError:
                    continue
                t = (row.get("ticker") or "").upper()
                pct = row.get("pct")
                if t and isinstance(pct, (int, float)):
                    out[t] = float(pct)
    return out, used


def morning_feeds(date):
    """Every morning feed that morning, newest print first.

    Each feed quotes a different slice of the tape, so a name can be in one
    and not another. A name that is in the gap brief's band but not in the
    brief's own screen is a real answer, not an absence.

    The order is by clock, newest first: the pre-open tape's last checkpoint
    (09:50), the gap brief's band (the 09:00 routine), and the pre-market
    brief's own screen (the 08:30 routine). "Was it gapping?" is answered by
    the most recent print, not by the first feed that happens to quote it -
    a name that was +1.96% at 08:30 and +3.45% at 09:00 was gapping.
    """
    feeds = []
    tape, used = preopen_quotes(date)
    if tape:
        if len(used) > 1:
            label = "the pre-open tape (`%s/%s` and %d earlier checkpoint(s))" % (
                PREOPEN, used[-1], len(used) - 1)
        else:
            label = "the pre-open tape (`%s/%s`)" % (PREOPEN, used[0] if used else "")
        feeds.append((label, tape))
    gap = ntrt_quotes(date)
    if gap:
        feeds.append((
            "the gap brief's 3%% band (`%s/%s.csv`)" % (NTRT, date),
            gap))
    brief = brief_quotes(date)
    if brief:
        feeds.append((
            "the brief's own screen (`%s/%s-pre-market.csv`)" % (BRIEFS, date),
            brief))
    return feeds


def status_of(pct):
    if pct is None:
        return "not in the feed"
    if abs(pct) >= GAP_LINE:
        return "gapping"
    return "under the line"


def build(morning):
    prior_date, names, note = prior_short_list(morning)
    feeds = morning_feeds(morning)
    rows = []
    for name in names:
        ticker = name["ticker"]
        pct = None
        source = "no feed quoted it"
        for label, quotes in feeds:
            if ticker in quotes:
                pct = quotes[ticker]
                source = label
                break
        rows.append({
            "ticker": ticker,
            "stylists": name["stylists"],
            "yesterday_change": name["yesterday_change"],
            "morning_pct": pct,
            "status": status_of(pct),
            "source": source,
        })
    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    return {
        "morning": morning,
        "prior_date": prior_date,
        "ticker_note": note,
        "feeds": [label for label, _quotes in feeds],
        "rows": rows,
        "counts": counts,
    }


def _fmt(v):
    if v is None:
        return "—"
    return "%+.2f%%" % v


def render(data):
    lines = []
    lines.append("# Yesterday's short list — did it show up this morning?")
    lines.append("")
    lines.append(J.provenance(
        "derived join of daily-screens/<prior>/tier-a.csv to the morning feed "
        "(no source file is modified)",
        "%s morning, prior board %s, %d name(s)" % (
            data["morning"], data["prior_date"] or "none", len(data["rows"])),
        "read-only",
    ))
    lines.append("")
    lines.append("> **Read this before the table.**")
    lines.append(">")
    lines.append("> This is a follow-up, not a demand that the two lists match. The evening")
    lines.append("> list and the morning feed are different jobs. The question is whether")
    lines.append("> yesterday's lead names were in this morning's feed at all, and whether")
    lines.append("> any that were there were past the 3% line the morning brief treats as a gap.")
    lines.append(">")
    lines.append("> `gapping` means the morning print was at least 3% either way. `under the line`")
    lines.append("> means the name was in a feed but the print was smaller than that.")
    lines.append("> `not in the feed` means none of the morning feeds quoted the name. It does")
    lines.append("> not mean the name was flat. It means nobody quoted it.")
    lines.append("")
    if not data["prior_date"]:
        lines.append("No Tier-A board was published before %s, so there is no short list to check."
                     % data["morning"])
        lines.append("")
        return "\n".join(lines) + "\n"
    lines.append("Prior board: `%s`." % data["prior_date"])
    if data["ticker_note"]:
        lines.append("Ticker column: %s." % data["ticker_note"])
    if data["feeds"]:
        lines.append("Feeds consulted: %s." % "; ".join(data["feeds"]))
    else:
        lines.append("No morning feed published for %s, so no name could be checked."
                     % data["morning"])
    lines.append("")
    lines.append("| Status | Names |")
    lines.append("|---|---|")
    for key in ("gapping", "under the line", "not in the feed"):
        lines.append("| %s | %d |" % (key, data["counts"].get(key, 0)))
    lines.append("")
    lines.append("| Ticker | Yesterday's move | This morning | Status | Feed |")
    lines.append("|---|---|---|---|---|")
    order = {"gapping": 0, "under the line": 1, "not in the feed": 2}
    for row in sorted(data["rows"], key=lambda r: (order[r["status"]], r["ticker"])):
        lines.append("| %s | %s | %s | %s | %s |" % (
            row["ticker"], _fmt(row["yesterday_change"]), _fmt(row["morning_pct"]),
            row["status"], row["source"]))
    lines.append("")
    lines.append("A blank yesterday move means that board did not publish one. A blank morning")
    lines.append("print means the name was not in the feed, which is the status, not a zero.")
    lines.append("The feed column names where each print came from; a name quoted by more than")
    lines.append("one feed is shown from the LATEST feed that quoted it, because \"was it")
    lines.append("gapping?\" is answered by the most recent print.")
    lines.append("")
    return "\n".join(lines) + "\n"


def render_csv(data):
    cols = ["ticker", "stylists", "yesterday_change", "morning_pct", "status", "source"]
    out = [",".join(cols)]
    for row in data["rows"]:
        vals = []
        for c in cols:
            v = row.get(c)
            s = "" if v is None else str(v)
            if "," in s or '"' in s:
                s = '"%s"' % s.replace('"', '""')
            vals.append(s)
        out.append(",".join(vals))
    return "\n".join(out) + "\n"


def main(argv):
    check_only = "--check" in argv
    for date in morning_dates():
        data = build(date)
        if check_only:
            print("%s prior=%s %s" % (date, data["prior_date"], data["counts"]))
            continue
        target = os.path.join(J.REPO, OUT_ROOT, date)
        a = J.write_if_changed(os.path.join(target, "yesterday-short-list.md"), render(data))
        b = J.write_if_changed(os.path.join(target, "yesterday-short-list.csv"), render_csv(data))
        print("%s: md %s · csv %s" % (date, a, b))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
