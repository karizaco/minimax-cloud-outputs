#!/usr/bin/env python3
"""Aggregate the screen board by sector, and compare it to the ETF tape.

Why: every `daily-sweep.md` describes a rotation in prose and never tabulates it.
On 2026-11-06 the brief says "a duration rally inside a rising-rate tape" and
supports it with SMH +3.62%, SOXX +3.51%, XLK +1.45% and the defensive ETFs all
red. The sector column exists in every `master.csv` and the day's change sits
beside it. What does not exist is the aggregation: which sectors gained
representation on the board today versus the last session, and whether the board's
sector mix agrees with the tape.

That disagreement is the point. A board that is 40% Health Technology on a day
when healthcare ETFs are flat is a stock-picking tape; a board that is 40%
Electronic Technology on a day when SMH is +3.6% is a sector tape and the
individual names are the beta. The sweep's own prose makes exactly this
distinction - "the names that moved hardest today are the ones with a story of
their own" versus "NVDA, MU, AMD are the beta, not a story" - but it makes it per
name, by hand, for the dozen names it has room to discuss. This makes it for the
whole 200-row board, every day.

Two taxonomies, never blended. `master.csv` labels sectors with a FactSet-style
vocabulary on most dates (`Electronic Technology`, `Health Technology`) and a GICS
one on two (`Information Technology`, `Health Care`). The ETF tape in the in-play
digest is a third thing again - a list of tickers, not a taxonomy. So the ETF
column is attached by an explicit, published mapping and the artifact names which
vocabulary it read; no row is silently re-bucketed.

  python3 scripts/build_sector_flow.py            # write per-date artifacts
  python3 scripts/build_sector_flow.py --check    # report only, write nothing
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

SCREENS = "daily-screens"
INPLAY = "us-stocks-in-play"
OUT_ROOT = "derived"

# Which ETF is the tape's read on a sector. This mapping is a judgement and is
# printed in every artifact, so a reader can disagree with a row of it without
# reading the code. A sector with no obvious single-ETF proxy is left unmapped
# rather than attached to a loose one.
SECTOR_ETF = {
    # FactSet-style vocabulary (the majority of dates)
    "Electronic Technology": ["SMH", "XLK"],
    "Technology Services": ["IGV", "XLK"],
    "Health Technology": ["XBI", "XLV"],
    "Health Services": ["XLV"],
    "Finance": ["XLF"],
    "Energy Minerals": ["XLE"],
    "Non-Energy Minerals": ["XLB"],
    "Process Industries": ["XLB"],
    "Producer Manufacturing": ["XLI"],
    "Industrial Services": ["XLI"],
    "Transportation": ["XLI"],
    "Consumer Durables": ["XLY"],
    "Consumer Services": ["XLY"],
    "Consumer Non-Durables": ["XLP"],
    "Retail Trade": ["XLY"],
    "Distribution Services": ["XLY"],
    "Utilities": ["XLU"],
    "Communications": ["XLC"],
    "Commercial Services": ["XLI"],
    "Miscellaneous": [],
    # GICS vocabulary (2026-10-29, 2026-10-30)
    "Information Technology": ["XLK"],
    "Health Care": ["XLV"],
    "Financials": ["XLF"],
    "Industrials": ["XLI"],
    "Consumer Discretionary": ["XLY"],
    "Consumer Staples": ["XLP"],
    "Materials": ["XLB"],
    "Communication Services": ["XLC"],
    "Real Estate": ["XLRE"],
}

# How far the board's sector mix has to move before it is worth a word.
SHIFT_PP = 3.0
# How far the board and the tape have to disagree in direction before the
# artifact calls it a disagreement.
DISAGREE_PP = 2.0


def read_board(date, board="master"):
    """One dated board, with the columns it actually used.

    Three dates (2026-10-28, 2026-11-02, 2026-11-03) publish a board with no
    sector column at all. For those the sector is recovered by joining the
    board's tickers to `us-eod/<date>.csv`, which carries a GICS sector for the
    whole universe. That is a different source and a different vocabulary, so it
    is recorded as such in `sector_source` and stated in the artifact - never
    presented as if the board had published it.
    """
    path = os.path.join(J.REPO, SCREENS, date, board + ".csv")
    rows = J.read_csv_rows(path)
    if not rows:
        return None
    tcol, _tnote = J.ticker_column(rows)
    scol, taxonomy = J.sector_column(rows)
    ccol, crule = J.change_column(rows, date)
    sector_source = ("%s/%s/%s.csv" % (SCREENS, date, board)) if scol else None
    joined = {}
    if not scol and tcol:
        _erows, eindex, _d = J.load_eod(date)
        if eindex:
            labels = set()
            for row in rows:
                t = J.strip_md(row.get(tcol)).upper()
                if not t:
                    continue
                erow, _how = J.eod_match(eindex, t)
                sec = J.strip_md(erow.get("sector")) if erow else ""
                if sec:
                    joined[t] = sec
                    labels.add(sec)
            if joined:
                sector_source = "us-eod/%s.csv (joined on ticker)" % date
                taxonomy = J.sector_taxonomy(labels)
    return {
        "date": date,
        "rows": rows,
        "ticker_column": tcol,
        "sector_column": scol,
        "sector_joined": joined,
        "sector_source": sector_source,
        "taxonomy": taxonomy,
        "change_column": ccol,
        "change_rule": crule,
        "path": "%s/%s/%s.csv" % (SCREENS, date, board),
    }


def sector_of(board, row, ticker):
    if board["sector_column"]:
        return J.strip_md(row.get(board["sector_column"]))
    return board["sector_joined"].get(ticker, "")


def sector_mix(board):
    """Per-sector count, share of the board, and median session change."""
    if not board or not (board["sector_column"] or board["sector_joined"]):
        return {}, 0
    out = {}
    counted = 0
    for row in board["rows"]:
        ticker0 = J.strip_md(row.get(board["ticker_column"])).upper() if board["ticker_column"] else ""
        sec = sector_of(board, row, ticker0)
        if not sec:
            sec = "(unlabelled)"
        entry = out.setdefault(sec, {"names": [], "changes": []})
        ticker = J.strip_md(row.get(board["ticker_column"])).upper() if board["ticker_column"] else ""
        if ticker:
            entry["names"].append(ticker)
        if board["change_column"]:
            v = J.to_float(row.get(board["change_column"]))
            if v is not None:
                entry["changes"].append(v)
        counted += 1
    for sec, entry in out.items():
        entry["count"] = len(entry["names"])
        entry["share_pct"] = round(100.0 * entry["count"] / counted, 2) if counted else None
        entry["median_change_pct"] = median(entry["changes"])
        entry["n_with_change"] = len(entry["changes"])
    return out, counted


def median(values):
    if not values:
        return None
    s = sorted(values)
    mid = len(s) // 2
    if len(s) % 2:
        return round(s[mid], 2)
    return round((s[mid - 1] + s[mid]) / 2.0, 2)


# The in-play digest's tape table has had four header shapes. Each is
# (label column, change column); the table is found by both being present.
TAPE_SHAPES = (
    ("ETF", "Change"),          # 2026-11-04 onward
    ("Instrument", "Change"),   # 2026-11-04 onward, the index strip
    ("Instrument", "Chg"),      # 2026-10-29 through 2026-11-03
    ("Index / ETF", "1d"),      # 2026-10-26 through 2026-10-29-pre-open
)


def read_etf_tape(date):
    """The ETF tape from the in-play digest, across every header shape it has had.

    Some digests publish the tape as two instrument/change pairs per row
    (`Instrument | Close | Chg | | Instrument | Close | Chg`). `md_tables`
    de-duplicates repeated header names, so the second pair is read by position
    rather than by name.
    """
    for name in ("%s.md" % date, "%s-midday.md" % date, "%s-open.md" % date):
        path = os.path.join(J.REPO, INPLAY, name)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        tape = {}
        for _start, header, rows in J.md_tables(text):
            for label_col, chg_col in TAPE_SHAPES:
                if label_col not in header or chg_col not in header:
                    continue
                pairs = [(i, j) for i, h in enumerate(header) if h == label_col
                         for j, h2 in enumerate(header) if h2 == chg_col and j > i]
                # Keep the nearest change column to each label column.
                used = {}
                for i, j in pairs:
                    if i not in used or j < used[i]:
                        used[i] = j
                for row in rows:
                    cells = list(row.values())
                    for i, j in used.items():
                        if i >= len(cells) or j >= len(cells):
                            continue
                        sym = J.strip_md(cells[i]).upper()
                        chg = J.to_float(cells[j])
                        if sym and chg is not None and sym not in tape:
                            tape[sym] = chg
        if tape:
            return tape, "%s/%s" % (INPLAY, name)
    return {}, None


def etf_read(sector, tape):
    """The tape's read on one sector: the mapped ETFs that the digest published."""
    etfs = SECTOR_ETF.get(sector)
    if etfs is None:
        return None, None, "sector not in the published mapping"
    present = [(e, tape[e]) for e in etfs if e in tape]
    if not present:
        if not etfs:
            return None, None, "no single-ETF proxy for this sector"
        return None, None, "mapped ETF(s) %s not in the digest's tape" % ", ".join(etfs)
    value = median([v for _e, v in present])
    return value, ", ".join("%s %+.2f%%" % (e, v) for e, v in present), None


def build_one(date, prev_date):
    board = read_board(date)
    if not board:
        return None
    mix, counted = sector_mix(board)
    prev_board = read_board(prev_date) if prev_date else None
    prev_mix, prev_counted = sector_mix(prev_board) if prev_board else ({}, 0)
    tape, tape_source = read_etf_tape(date)

    taxonomy_match = (
        prev_board is not None
        and prev_board.get("taxonomy") == board.get("taxonomy")
        and board.get("taxonomy") is not None
    )

    sectors = []
    for sec in sorted(mix, key=lambda s: (-mix[s]["count"], s)):
        entry = mix[sec]
        prev_entry = prev_mix.get(sec) if taxonomy_match else None
        delta = None
        if prev_entry and entry["share_pct"] is not None and prev_entry["share_pct"] is not None:
            delta = round(entry["share_pct"] - prev_entry["share_pct"], 2)
        tape_value, tape_detail, tape_note = etf_read(sec, tape)
        disagreement = None
        if tape_value is not None and entry["median_change_pct"] is not None:
            gap = entry["median_change_pct"] - tape_value
            if abs(gap) >= DISAGREE_PP:
                disagreement = round(gap, 2)
        sectors.append({
            "sector": sec,
            "count": entry["count"],
            "share_pct": entry["share_pct"],
            "prev_count": prev_entry["count"] if prev_entry else None,
            "prev_share_pct": prev_entry["share_pct"] if prev_entry else None,
            "share_delta_pp": delta,
            "median_change_pct": entry["median_change_pct"],
            "n_with_change": entry["n_with_change"],
            "tape_median_pct": tape_value,
            "tape_detail": tape_detail,
            "tape_note": tape_note,
            "board_vs_tape_pp": disagreement,
            "names": entry["names"][:12],
        })

    notes = []
    if not board["sector_column"] and board["sector_joined"]:
        notes.append(
            "**The sector on this date is not the board's own.** `%s` publishes no sector "
            "column, so each sector was recovered by joining the board's tickers to "
            "`%s` — a different source with a GICS vocabulary, where the board's own "
            "dates mostly use a FactSet-style one. %d of %d rows matched."
            % (board["path"], board["sector_source"], len(board["sector_joined"]), counted))
    elif not board["sector_column"]:
        notes.append(
            "`%s` publishes no sector column on this date and no sector could be "
            "recovered by joining to `us-eod/`, so no mix can be computed." % board["path"])
    if not board["change_column"]:
        notes.append(
            "`%s` publishes no column identifiable as this session's change, so the "
            "median-change column is empty." % board["path"])
    elif board["change_rule"] != "current schema":
        notes.append(
            "The session-change column on this date is `%s`, chosen because it is %s. "
            "The column name is not stable across dates." % (board["change_column"], board["change_rule"]))
    if prev_board and not taxonomy_match:
        notes.append(
            "No day-over-day delta: the previous board (`%s`) labels sectors with the "
            "**%s** vocabulary and this one uses **%s**. Two taxonomies are not "
            "comparable, so the delta column is left empty rather than mapped across."
            % (prev_board["path"], prev_board.get("taxonomy") or "none",
               board.get("taxonomy") or "none"))
    elif not prev_board:
        notes.append("No previous board found, so there is no day-over-day delta.")
    elif bool(prev_board["sector_column"]) != bool(board["sector_column"]):
        notes.append(
            "The day-over-day delta spans two **kinds** of sector source — `%s` for the "
            "previous board and `%s` for this one. Both use the %s vocabulary, so the "
            "labels are comparable, but the delta carries a source change as well as a "
            "real one."
            % (prev_board["sector_source"], board["sector_source"], board.get("taxonomy")))
    if not tape:
        notes.append(
            "No ETF tape found for this date in `%s/`, so the board-versus-tape "
            "comparison is empty." % INPLAY)
    unmapped = [s["sector"] for s in sectors if s["tape_note"]]
    if unmapped:
        notes.append(
            "%d sector(s) carry no tape read: %s. Each is left blank rather than "
            "attached to a loose proxy." % (len(unmapped), ", ".join(unmapped[:6])))

    return {
        "_schema": "sector-flow-v1",
        "date": date,
        "previous_date": prev_date if taxonomy_match else None,
        "source_board": board["path"],
        "source_sector": board["sector_source"],
        "sector_from_board": bool(board["sector_column"]),
        "source_tape": tape_source,
        "taxonomy": board.get("taxonomy"),
        "columns_used": {
            "ticker": board["ticker_column"],
            "sector": board["sector_column"],
            "change": board["change_column"],
            "change_rule": board["change_rule"],
        },
        "board_rows": counted,
        "rules": {
            "shift_pp": SHIFT_PP,
            "disagree_pp": DISAGREE_PP,
            "sector_etf_map": {k: v for k, v in SECTOR_ETF.items() if k in mix},
            "disclaimer": "shares and medians are counts over the published board - "
                          "no name is weighted, scored or recommended",
        },
        "sectors": sectors,
        "notes": notes,
    }


CSV_COLS = ["sector", "count", "share_pct", "prev_count", "prev_share_pct", "share_delta_pp",
            "median_change_pct", "n_with_change", "tape_median_pct", "board_vs_tape_pp"]


def render_csv(data):
    out = [",".join(CSV_COLS)]
    for s in data["sectors"]:
        out.append(",".join("" if s.get(c) is None else str(s.get(c)) for c in CSV_COLS))
    return "\n".join(out) + "\n"


def _pp(v, fmt="%+.2f"):
    return "—" if v is None else fmt % v


def render_md(data):
    s_all = data["sectors"]
    lines = []
    lines.append("# Sector flow — the %s board by sector" % data["date"])
    lines.append("")
    lines.append(J.provenance(
        "derived aggregation over `%s`%s (neither source is modified)"
        % (data["source_board"],
           (" and `%s`" % data["source_tape"]) if data["source_tape"] else ""),
        "%d board rows across %d sector(s), %s vocabulary"
        % (data["board_rows"], len(s_all), data["taxonomy"] or "no"),
        "read-only",
    ))
    lines.append("")
    lines.append("> **Read this before the table.**")
    lines.append("> ")
    lines.append("> 1. **This counts the board, it does not weight the market.** A sector's share")
    lines.append(">    is its share of the names the screen published, not of any index. A sector")
    lines.append(">    with 40% of the board is where the screen found candidates — that is a")
    lines.append(">    statement about the screen's output, not about market capitalisation.")
    lines.append("> 2. **The vocabulary on this date is `%s`.** The boards use a FactSet-style"
                 % (data["taxonomy"] or "none"))
    lines.append(">    taxonomy on most dates, and GICS wherever the board carries a `gics_sector`")
    lines.append(">    column or the sector had to be recovered from `us-eod/`. The two are never")
    lines.append(">    blended and a delta across them is never computed.")
    lines.append("> 3. **The ETF column is a mapping, not a fact.** Which ETF reads a sector is a")
    lines.append(">    judgement, published in full under *The sector-to-ETF mapping* below.")
    if data["notes"]:
        lines.append("> 4. **Deviations and degraded paths.**")
        for n in data["notes"]:
            lines.append(">    - %s" % n)
    lines.append("")

    lines.append("## The board's sector mix")
    lines.append("")
    lines.append("| Sector | Names | Share | Prev share | Δ share | Median chg | Tape | Board − tape |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for s in s_all:
        lines.append("| %s | %d | %s | %s | %s | %s | %s | %s |" % (
            s["sector"], s["count"],
            _pp(s["share_pct"], "%.1f%%"),
            _pp(s["prev_share_pct"], "%.1f%%"),
            _pp(s["share_delta_pp"]),
            _pp(s["median_change_pct"]),
            _pp(s["tape_median_pct"]),
            _pp(s["board_vs_tape_pp"])))
    lines.append("")
    lines.append("**What this table means.** `Share` is the sector's percentage of the published")
    lines.append("board. `Median chg` is the median session change of that sector's names on the")
    lines.append("board — a median, not a mean, so one 70% mover does not carry a sector. `Tape` is")
    lines.append("the median change of the mapped ETFs as the in-play digest published them.")
    lines.append("")
    lines.append("**What it does not mean.** It is not a performance attribution and not a return.")
    lines.append("The board is a screen output, so a sector's median change describes *names that")
    lines.append("passed a momentum screen in that sector*, which is a biased sample of the sector")
    lines.append("by construction. A reader should not infer sector performance from it — that is")
    lines.append("what the `Tape` column is for, and the two measure different things on purpose.")
    lines.append("")

    shifts = [s for s in s_all if s["share_delta_pp"] is not None and abs(s["share_delta_pp"]) >= SHIFT_PP]
    if shifts:
        lines.append("### Where the board moved, versus `%s`" % data["previous_date"])
        lines.append("")
        lines.append("Sectors whose share of the board moved at least %.0f pp." % SHIFT_PP)
        lines.append("")
        lines.append("| Sector | Prev share | Share | Δ |")
        lines.append("|---|---|---|---|")
        for s in sorted(shifts, key=lambda s: -abs(s["share_delta_pp"])):
            lines.append("| %s | %s | %s | %s |" % (
                s["sector"], _pp(s["prev_share_pct"], "%.1f%%"),
                _pp(s["share_pct"], "%.1f%%"), _pp(s["share_delta_pp"])))
        lines.append("")
        lines.append("A share can move because a sector gained names or because another sector lost")
        lines.append("them — the board is capped, so the shares are not independent. Read a Δ as")
        lines.append("\"more of the board looked like this today\", never as an inflow.")
        lines.append("")

    disagree = [s for s in s_all if s["board_vs_tape_pp"] is not None]
    lines.append("### Board versus tape")
    lines.append("")
    if disagree:
        lines.append("Sectors where the board's median name and the mapped ETF disagree by at least")
        lines.append("%.0f pp. This is the column that distinguishes a sector tape from a" % DISAGREE_PP)
        lines.append("stock-picking one.")
        lines.append("")
        lines.append("| Sector | Board median | Tape | Gap | Tape detail |")
        lines.append("|---|---|---|---|---|")
        for s in sorted(disagree, key=lambda s: -abs(s["board_vs_tape_pp"])):
            lines.append("| %s | %s | %s | %s | %s |" % (
                s["sector"], _pp(s["median_change_pct"]), _pp(s["tape_median_pct"]),
                _pp(s["board_vs_tape_pp"]), s["tape_detail"] or "—"))
        lines.append("")
        lines.append("A **positive gap** means the board's names outran their sector ETF: the screen")
        lines.append("found movers the sector as a whole did not have, which is a stock-picking")
        lines.append("read. A **negative gap** means the ETF outran the board's names, so the")
        lines.append("sector moved without the screen's candidates leading it. Neither is good or")
        lines.append("bad; the gap is a description of where the move lived.")
    else:
        lines.append("No sector's board median and mapped ETF disagree by %.0f pp or more on this" % DISAGREE_PP)
        lines.append("date, or no tape was available to compare against.")
    lines.append("")

    lines.append("## The sector-to-ETF mapping")
    lines.append("")
    lines.append("Published in full because it is a judgement this artifact makes, not a fact it")
    lines.append("reads. A sector mapped to two ETFs takes their median.")
    lines.append("")
    lines.append("| Sector | ETF(s) |")
    lines.append("|---|---|")
    for sec in sorted(data["rules"]["sector_etf_map"]):
        etfs = data["rules"]["sector_etf_map"][sec]
        lines.append("| %s | %s |" % (sec, ", ".join(etfs) if etfs else "— *(no single proxy)*"))
    lines.append("")
    lines.append("## Method and caveats")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append("| Board | `%s` |" % data["source_board"])
    lines.append("| Tape | `%s` |" % (data["source_tape"] or "— none for this date"))
    lines.append("| Sector source | `%s`%s |" % (
        data["source_sector"] or "— none",
        "" if data["sector_from_board"] else " — **joined, not the board's own column**"))
    lines.append("| Sector column | `%s` (%s vocabulary) |" % (
        data["columns_used"]["sector"] or "—", data["taxonomy"] or "no"))
    lines.append("| Session-change column | `%s` (%s) |" % (
        data["columns_used"]["change"] or "—", data["columns_used"]["change_rule"] or "—"))
    lines.append("| Board rows counted | %d |" % data["board_rows"])
    lines.append("| Share-shift threshold | %.1f pp |" % SHIFT_PP)
    lines.append("| Board-versus-tape threshold | %.1f pp |" % DISAGREE_PP)
    lines.append("")
    lines.append("The column names above are not stable across dates — that is why they are")
    lines.append("printed. `sector-flow.csv` beside this file carries the same rows.")
    lines.append("")
    return "\n".join(lines) + "\n"


def main(argv):
    check_only = "--check" in argv
    dates = J.dated_dirs(SCREENS)
    dates = [d for d in dates if os.path.exists(os.path.join(J.REPO, SCREENS, d, "master.csv"))]
    if not dates:
        print("no daily-screens/*/master.csv found", file=sys.stderr)
        return 2
    for i, date in enumerate(dates):
        prev_date = dates[i - 1] if i else None
        data = build_one(date, prev_date)
        if not data:
            print("%s: no readable board" % date)
            continue
        if check_only:
            shifts = sum(1 for s in data["sectors"]
                         if s["share_delta_pp"] is not None and abs(s["share_delta_pp"]) >= SHIFT_PP)
            dis = sum(1 for s in data["sectors"] if s["board_vs_tape_pp"] is not None)
            print("%s: %d sectors (%s), %d rows, %d shift(s), %d disagreement(s), tape %s" % (
                date, len(data["sectors"]), data["taxonomy"], data["board_rows"],
                shifts, dis, "yes" if data["source_tape"] else "no"))
            continue
        target = os.path.join(J.REPO, OUT_ROOT, date)
        a = J.write_if_changed(os.path.join(target, "sector-flow.md"), render_md(data))
        b = J.write_if_changed(os.path.join(target, "sector-flow.csv"), render_csv(data))
        print("%s: md %s · csv %s" % (date, a, b))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
