#!/usr/bin/env python3
"""Join the morning's pre-market gaps to the same session's settled close.

Why: on 2026-11-06 three routines each saw part of the same story and none saw the
whole thing. The 08:23 ET earnings scanner listed FROG at +22.96% pre-market, NET
at +18.86% and IREN at +16.03%, each tagged PRE_GAP with a sourced catalyst. The
18:30 ET daily sweep reported FROG +35.33% and IREN +20.02% and NET nowhere,
because by then NET's gap had faded and it no longer ranked. The 15:50 ET in-play
digest is the only one that states the relationship - "the gaps that held into the
bell were overwhelmingly the earnings gaps" - and it names the reversals. A reader
who wants to know whether the morning's gaps held has to open three files and do
the subtraction by hand.

This closes that. One artifact per fire date: every name the scanner tagged
PRE_GAP, its morning gap, its settled session change, and a label for the path.

WHICH SESSION THE MORNING NUMBER BELONGS TO. This is the whole correctness
question, and it is resolved from the data rather than assumed. In a reactions
file, `Close` and `Chg %` describe the session that had just settled when the
scanner fired, and `Pre-mkt %` is the extended-hours move measured against that
same close - so the morning number is already on the same base as the FIRE DATE's
`change_pct` in `us-eod/`, and the two are directly comparable with no rebasing.

That was verified before this script was written, not assumed: matching the
reactions `Close` column against every settled session's closes identifies the
prior session at 90-99% for every file from 2026-10-29 on, and matching `Chg %`
against `change_pct` agrees. The `Ref close` / `Ref asof` columns are the base of
the `Chg %` column, NOT of the pre-market column - using them to pick the session
dates the join two sessions early and turns held gaps into false reversals.

For the two oldest files (2026-10-24, 2026-10-26) neither column matches any
settled session above 9%. Their base cannot be verified, so their artifacts are
labelled `unverified` in the body rather than published as if they were sound.

What it does NOT do: state a direction, a size or a trade. `held`, `faded`,
`reversed`, `extended` and `flat` describe the session path only. The thresholds
are constants at the top of this file and are printed inside the artifact, so a
reader can disagree with them without reading the code.

  python3 scripts/build_gap_reconciliation.py            # write per-date artifacts
  python3 scripts/build_gap_reconciliation.py --check    # report only, write nothing
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

EARNINGS = "earnings"
OUT_ROOT = "derived"

# ------------------------------------------------------------------ the rules
# These constants are the whole judgement this artifact makes. They are printed
# in the artifact body next to the table, not left buried here.
MATERIAL_GAP_PP = 1.0      # below this the morning move is not a gap worth a label
EXTEND_FLOOR_PP = 0.5      # a `reversed` label needs a settled move this large
EXTEND_MARGIN_PP = 0.25    # `extended` must beat the gap by this much
FLAT_PP = 0.25             # under this the settled session went nowhere
HOLD_FRACTION = 0.5        # `held` keeps at least this share of the gap magnitude
VERIFY_FLOOR = 0.5         # below this match rate the session base is unverified

PATH_LABELS = ("extended", "held", "faded", "reversed", "flat", "no_close", "unclassified")

LABEL_MEANING = {
    "extended": "same sign, settled move larger than the morning gap",
    "held": "same sign, settled move kept at least %.0f%% of the gap's magnitude" % (HOLD_FRACTION * 100),
    "faded": "same sign but under that share, or an opposite sign under %.1fpp" % EXTEND_FLOOR_PP,
    "reversed": "opposite sign, settled move at least %.1fpp" % EXTEND_FLOOR_PP,
    "flat": "settled move under %.2fpp" % FLAT_PP,
    "no_close": "no settled row for this name in the session file",
    "unclassified": "morning gap under %.1fpp - too small to label" % MATERIAL_GAP_PP,
}


def outcome(gap, change):
    """Label the path from the morning gap to the settled change.

    `gap` is the morning pre-market move in percentage points against the prior
    close; `change` is the settled session change against the same close, or
    None when the session has no settled row for the name.
    """
    if change is None:
        return "no_close"
    if gap is None or abs(gap) < MATERIAL_GAP_PP:
        return "unclassified"
    if gap * change < 0:
        return "reversed" if abs(change) >= EXTEND_FLOOR_PP else "faded"
    if abs(change) < FLAT_PP:
        return "flat"
    if abs(change) >= abs(gap) + EXTEND_MARGIN_PP:
        return "extended"
    if abs(change) >= abs(gap) * HOLD_FRACTION:
        return "held"
    return "faded"


def parse_reactions(path):
    """The US headline table of one reactions file: morning gaps and their tags."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    _start, header, rows = J.table_after(text, "US", "Ticker", "Pre-mkt %", "Tag")
    if not rows:
        _start, header, rows = J.table_after(text, "US", "Ticker", "Pre-mkt %")
    out = []
    for row in rows:
        ticker = J.strip_md(row.get("Ticker")).upper()
        if not ticker:
            continue
        out.append({
            "ticker": ticker,
            "venue": J.strip_md(row.get("Venue")),
            "pre_mkt_pct": J.to_float(row.get("Pre-mkt %")),
            "post_mkt_pct": J.to_float(row.get("Post-mkt %")),
            "tag": J.strip_md(row.get("Tag")).upper(),
            "prior_close": J.to_float(row.get("Close")),
            "prior_change_pct": J.to_float(row.get("Chg %")),
            "ref_close": J.to_float(row.get("Ref close")),
            "ref_asof": J.strip_md(row.get("Ref asof")),
            "us_tradeable": J.strip_md(row.get("US tradeable")),
            "catalyst": J.strip_md(row.get("Catalyst")),
            "move_vs_avg": J.strip_md(row.get("Move vs avg daily")),
        })
    return out, header


def verify_prior(morning, date):
    """How well a candidate session's closes match the morning file's `Close` column.

    This is the check that pins the join down. Returns (rate, hits, compared).
    """
    _rows, index, _dupes = J.load_eod(date)
    if not index:
        return 0.0, 0, 0
    hits = compared = 0
    for m in morning:
        if m["prior_close"] is None:
            continue
        row, _how = J.eod_match(index, m["ticker"])
        if not row:
            continue
        close = J.to_float(row.get("close"))
        if close is None:
            continue
        compared += 1
        tolerance = max(0.02, abs(m["prior_close"]) * 0.001)
        if abs(close - m["prior_close"]) <= tolerance:
            hits += 1
    rate = (hits / compared) if compared else 0.0
    return rate, hits, compared


def resolve_sessions(fire_date, morning):
    """Which session settled before the fire, and which one the gaps resolve into.

    The settled session is the fire date when `us-eod/` has a file for it. The
    prior session is identified by matching the morning file's `Close` column,
    and the match rate is carried out so the artifact can say how well the join
    is pinned down rather than asserting it.
    """
    available = J.eod_dates()
    settled = fire_date if fire_date in available else None
    earlier = [d for d in available if d < fire_date]
    best = (0.0, 0, 0, None)
    for d in reversed(earlier[-4:]):
        rate, hits, compared = verify_prior(morning, d)
        if rate > best[0]:
            best = (rate, hits, compared, d)
    rate, hits, compared, prior = best
    notes = []
    if settled is None:
        notes.append(
            "No settled EOD file for %s (`us-eod/<date>.csv`) - the fire landed on a day "
            "with no settled US session, so no name can be given a settled close and "
            "every row is `no_close`." % fire_date)
    if rate < VERIFY_FLOOR:
        notes.append(
            "**Session base unverified.** The morning file's `Close` column matches no "
            "settled session's closes above %.0f%% (best: %s at %.0f%%, %d of %d names "
            "compared). The labels in this artifact rest on an unverified base and should "
            "not be read as firm." % (VERIFY_FLOOR * 100, prior or "none", rate * 100, hits, compared))
    return {
        "settled": settled,
        "prior": prior,
        "prior_match_rate": round(rate, 4),
        "prior_match_hits": hits,
        "prior_match_compared": compared,
        "verified": rate >= VERIFY_FLOOR,
        "notes": notes,
    }


def build_one(fire_date):
    path = os.path.join(J.REPO, EARNINGS, fire_date + "-reactions.md")
    morning, header = parse_reactions(path)
    sessions = resolve_sessions(fire_date, morning)
    settled_date = sessions["settled"]

    eod_rows, eod_index, dupes = ([], {}, 0)
    if settled_date:
        eod_rows, eod_index, dupes = J.load_eod(settled_date)

    rows_out = []
    for m in morning:
        if m["tag"] and "PRE_GAP" not in m["tag"]:
            continue
        row, matched = J.eod_match(eod_index, m["ticker"]) if eod_index else (None, None)
        change = J.to_float(row.get("change_pct")) if row else None
        open_gap = J.to_float(row.get("gap_pct")) if row else None
        close = J.to_float(row.get("close")) if row else None
        catalyst = m["catalyst"] or ""
        rows_out.append({
            "ticker": m["ticker"],
            "pre_mkt_pct": m["pre_mkt_pct"],
            "open_gap_pct": open_gap,
            "settled_change_pct": change,
            "settled_close": close,
            "outcome": outcome(m["pre_mkt_pct"], change),
            "tag": m["tag"] or None,
            "prior_close": m["prior_close"],
            "prior_change_pct": m["prior_change_pct"],
            "move_vs_avg": m["move_vs_avg"] or None,
            "catalyst": catalyst or None,
            "catalyst_status": (
                "not_looked_up" if "no catalyst lookup" in catalyst.lower()
                else ("sourced" if catalyst else "absent")
            ),
            "us_tradeable": m["us_tradeable"] or None,
            "venue": m["venue"] or None,
            "matched": matched,
        })

    counts = {}
    for r in rows_out:
        counts[r["outcome"]] = counts.get(r["outcome"], 0) + 1

    notes = list(sessions["notes"])
    if dupes:
        notes.append("%d duplicate ticker key(s) on the settled side; the first row wins." % dupes)
    missing = counts.get("no_close", 0)
    if missing and settled_date:
        notes.append(
            "%d of %d PRE_GAP name(s) have no settled row in the %s session file and are "
            "labelled `no_close` rather than dropped." % (missing, len(rows_out), settled_date))
    if eod_rows:
        with_open = sum(1 for r in eod_rows if J.to_float(r.get("open")) is not None)
        if with_open < len(eod_rows):
            notes.append(
                "The settled file publishes an `open` for %d of %d rows, so `Open gap %%` is "
                "blank wherever the session file has no open." % (with_open, len(eod_rows)))
    if not any("gap_pct" in (r or {}) for r in eod_rows[:1]):
        notes.append(
            "The %s session file carries no `gap_pct` column (only the newest one does), "
            "so the `Open gap %%` column is empty for this date." % settled_date
            if settled_date else "No settled file, so no open-gap column.")
    if "Catalyst" not in header:
        notes.append(
            "This reactions file predates the `Catalyst` column, so catalyst coverage "
            "cannot be reported for it.")

    return {
        "_schema": "gap-reconciliation-v1",
        "fire_date": fire_date,
        "settled_session": settled_date,
        "prior_session": sessions["prior"],
        "session_resolution": {
            "rule": "the morning Pre-mkt % is measured against the prior close, so it is "
                    "directly comparable to the fire date's change_pct - no rebasing",
            "prior_identified_by": "matching the reactions `Close` column against settled closes",
            "prior_match_rate": sessions["prior_match_rate"],
            "prior_match_hits": sessions["prior_match_hits"],
            "prior_match_compared": sessions["prior_match_compared"],
            "verified": sessions["verified"],
        },
        "source_morning": "%s/%s-reactions.md" % (EARNINGS, fire_date),
        "source_settled": ("us-eod/%s.csv" % settled_date) if settled_date else None,
        "rules": {
            "material_gap_pp": MATERIAL_GAP_PP,
            "extend_floor_pp": EXTEND_FLOOR_PP,
            "extend_margin_pp": EXTEND_MARGIN_PP,
            "flat_pp": FLAT_PP,
            "hold_fraction": HOLD_FRACTION,
            "labels": {k: LABEL_MEANING[k] for k in PATH_LABELS},
            "disclaimer": "labels describe the session path only - no direction, no size, no trade",
        },
        "counts": counts,
        "rows": rows_out,
        "notes": notes,
    }


CSV_COLS = ["ticker", "pre_mkt_pct", "open_gap_pct", "settled_change_pct", "settled_close",
            "outcome", "tag", "prior_close", "prior_change_pct", "move_vs_avg",
            "catalyst_status", "us_tradeable", "venue", "matched", "catalyst"]


def _csv_cell(v):
    if v is None:
        return ""
    s = str(v)
    if any(c in s for c in ',"\n'):
        return '"%s"' % s.replace('"', '""')
    return s


def sort_rows(rows):
    return sorted(
        rows,
        key=lambda r: (-(abs(r["pre_mkt_pct"]) if r["pre_mkt_pct"] is not None else -1), r["ticker"]),
    )


def render_csv(data):
    out = [",".join(CSV_COLS)]
    for r in sort_rows(data["rows"]):
        out.append(",".join(_csv_cell(r.get(c)) for c in CSV_COLS))
    return "\n".join(out) + "\n"


def _fmt(v):
    return "—" if v is None else "%+.2f" % v


def render_md(data):
    rows = sort_rows(data["rows"])
    counts = data["counts"]
    res = data["session_resolution"]
    lines = []
    lines.append("# Gap reconciliation — %s pre-market vs the settled close" % data["fire_date"])
    lines.append("")
    lines.append(J.provenance(
        "derived join over `%s` and `%s` (neither source is modified)"
        % (data["source_morning"], data["source_settled"] or "no settled file"),
        "%d PRE_GAP name(s) tagged at the %s pre-market fire" % (len(rows), data["fire_date"]),
        "read-only",
    ))
    lines.append("")
    lines.append("> **Read this before the table.**")
    lines.append("> ")
    lines.append("> 1. **These labels describe the session path, not a trade.** `held`, `faded`,")
    lines.append(">    `reversed`, `extended` and `flat` say what the price did between the morning")
    lines.append(">    quote and the settled close. This artifact states no direction and no size.")
    lines.append("> 2. **The two sides share one base.** `Pre-mkt %` is the extended-hours move")
    lines.append(">    against the prior session's close; `Settled chg %` is the 16:00 ET close")
    lines.append(">    against that same close. They are directly comparable — the subtraction a")
    lines.append(">    reader would otherwise do across three files is done here.")
    if not res["verified"]:
        lines.append("> 3. **This date's base is UNVERIFIED — treat every label as provisional.**")
        lines.append(">    See *Session resolution* below for the match rate that failed.")
    else:
        lines.append("> 3. **Session resolution is verified** at %.0f%% (%d of %d names): the morning"
                     % (res["prior_match_rate"] * 100, res["prior_match_hits"], res["prior_match_compared"]))
        lines.append(">    file's `Close` column matches the `%s` settled closes, so the morning gap"
                     % (data["prior_session"] or "—"))
        lines.append(">    resolves into the `%s` session." % (data["settled_session"] or "—"))
    if data["notes"]:
        lines.append("> 4. **Deviations and degraded paths.**")
        for n in data["notes"]:
            lines.append(">    - %s" % n)
    lines.append("")

    lines.append("## Outcome counts")
    lines.append("")
    lines.append("| Outcome | Names | What the label means |")
    lines.append("|---|---|---|")
    for label in PATH_LABELS:
        if label in counts:
            lines.append("| `%s` | %d | %s |" % (label, counts[label], LABEL_MEANING[label]))
    lines.append("| **total** | **%d** | |" % len(rows))
    lines.append("")
    lines.append("The counts are a distribution of session paths, not a scorecard. A high `faded`")
    lines.append("count means opening moves were given back that day; it does not mean the morning")
    lines.append("scan was wrong, and a `reversed` row is not a failure of the routine that found")
    lines.append("it. What a reader should **not** conclude from this table is anything about")
    lines.append("tradeability: the artifact knows the open and the close, and nothing about the")
    lines.append("path between them or whether either price was reachable.")
    lines.append("")

    lines.append("## Session resolution")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append("| Fire date | `%s` |" % data["fire_date"])
    lines.append("| Prior session (the `Close` column) | `%s` |" % (data["prior_session"] or "—"))
    lines.append("| Settled session joined to | `%s` |" % (data["settled_session"] or "—"))
    lines.append("| Prior-session match rate | %.0f%% (%d of %d) |" % (
        res["prior_match_rate"] * 100, res["prior_match_hits"], res["prior_match_compared"]))
    lines.append("| Verified | %s |" % ("yes" if res["verified"] else "**no**"))
    lines.append("")
    lines.append("The reactions file's `Ref close` / `Ref asof` columns are the base of its `Chg %`")
    lines.append("column — the prior session's own change — and are **not** the base of the")
    lines.append("pre-market column. Using them to pick the session dates the join two sessions")
    lines.append("early and turns held gaps into false reversals; that error was found and fixed")
    lines.append("before this artifact was first published.")
    lines.append("")

    lines.append("## Every PRE_GAP name")
    lines.append("")
    lines.append("Sorted by the magnitude of the morning gap. Every row the scanner tagged")
    lines.append("`PRE_GAP` is here, including the ones it did not look up a catalyst for.")
    lines.append("")
    lines.append("| Ticker | Pre-mkt % | Open gap % | Settled chg % | Outcome | Catalyst | US access |")
    lines.append("|---|---|---|---|---|---|---|")
    for row in rows:
        lines.append("| %s | %s | %s | %s | `%s` | %s | %s |" % (
            row["ticker"], _fmt(row["pre_mkt_pct"]), _fmt(row["open_gap_pct"]),
            _fmt(row["settled_change_pct"]), row["outcome"],
            row["catalyst_status"], row["us_tradeable"] or "—"))
    lines.append("")
    lines.append("`Open gap %` is the official 09:30 open against the prior close, taken from the")
    lines.append("settled file's own `gap_pct` where it publishes one. It sits between the two")
    lines.append("other columns in time, and where it differs sharply from `Pre-mkt %` the move")
    lines.append("happened between the morning quote and the opening auction.")
    lines.append("")

    no_cat = [r["ticker"] for r in rows if r["catalyst_status"] == "not_looked_up"]
    if no_cat:
        lines.append("### Catalyst coverage")
        lines.append("")
        lines.append("%d of %d name(s) carry `not_looked_up`: the morning scanner's own table says"
                     % (len(no_cat), len(rows)))
        lines.append("\"no catalyst lookup (outside the per-run budget)\" for them. **The absence of a")
        lines.append("catalyst for those names is a budget decision, not a finding** — and a reader of")
        lines.append("the sweep has no way to tell those two apart. This column makes the difference")
        lines.append("visible instead of leaving an empty cell that reads as \"nothing happened\".")
        lines.append("")

    lines.append("## Method and caveats")
    lines.append("")
    lines.append("| Rule | Value |")
    lines.append("|---|---|")
    lines.append("| Morning gap counts as a gap at | %.1f pp |" % MATERIAL_GAP_PP)
    lines.append("| `held` keeps at least | %.0f%% of the gap's magnitude |" % (HOLD_FRACTION * 100))
    lines.append("| `extended` requires | settled move ≥ gap + %.2f pp |" % EXTEND_MARGIN_PP)
    lines.append("| `reversed` requires | opposite sign and settled move ≥ %.1f pp |" % EXTEND_FLOOR_PP)
    lines.append("| `flat` is | settled move < %.2f pp |" % FLAT_PP)
    lines.append("")
    lines.append("These constants live at the top of `scripts/build_gap_reconciliation.py`. Change")
    lines.append("them there and the labels change here — this table is never adjusted by hand.")
    lines.append("")
    lines.append("The join is a copy: every value in it comes from one of the two sources in the")
    lines.append("provenance line. Nothing is interpolated, no missing price is filled in, and a")
    lines.append("name with no settled row is labelled rather than dropped. `gap-reconciliation.csv`")
    lines.append("beside this file carries the same rows with the prior close, the move-vs-average")
    lines.append("figure and the catalyst text in full.")
    lines.append("")
    return "\n".join(lines) + "\n"


def fire_dates():
    root = os.path.join(J.REPO, EARNINGS)
    if not os.path.isdir(root):
        return []
    return [n[:10] for n in sorted(os.listdir(root))
            if n.endswith("-reactions.md") and J.DATE_RE.match(n[:10])]


def main(argv):
    check_only = "--check" in argv
    dates = fire_dates()
    if not dates:
        print("no %s/*-reactions.md found" % EARNINGS, file=sys.stderr)
        return 2
    for date in dates:
        data = build_one(date)
        if check_only:
            print("%s -> settled %s (prior %s, match %.0f%%%s): %d rows %s" % (
                date, data["settled_session"], data["prior_session"],
                data["session_resolution"]["prior_match_rate"] * 100,
                "" if data["session_resolution"]["verified"] else " UNVERIFIED",
                len(data["rows"]), data["counts"]))
            continue
        target = os.path.join(J.REPO, OUT_ROOT, date)
        a = J.write_if_changed(os.path.join(target, "gap-reconciliation.md"), render_md(data))
        b = J.write_if_changed(os.path.join(target, "gap-reconciliation.csv"), render_csv(data))
        print("%s: md %s · csv %s" % (date, a, b))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
