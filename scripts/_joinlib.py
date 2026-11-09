#!/usr/bin/env python3
"""Shared readers for the derived-view builders in this directory.

Why this exists: five builders (persistence, gap reconciliation, sector flow,
the charts, the ledger) all have to open the same dated CSVs, and the columns in
those CSVs have drifted three times in the last month. The ticker is `symbol`,
`ticker` or `name` depending on the date. The session change is `change_pct`,
`change`, `today_change` or a date-stamped column. The sector is `sector`,
`gics_sector` or absent altogether, and when it is present it is either a
FactSet-style vocabulary or a GICS one.

None of that drift is an error in the artifacts. It is what the routines
published. So the shared layer here resolves a column by rule, records which
column it actually used, and never silently drops a date that looks different.

Nothing in this module infers a value or rewrites a source file.
"""
import csv
import json
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TICKER_RE = re.compile(r"^[A-Z0-9][A-Z0-9.\-]{0,9}$")

TICKER_COLUMNS = ("symbol", "ticker", "name")


def dated_dirs(root_rel):
    """Every `<YYYY-MM-DD>` directory under a family root, oldest first."""
    root = os.path.join(REPO, root_rel)
    if not os.path.isdir(root):
        return []
    return [
        d for d in sorted(os.listdir(root))
        if DATE_RE.match(d) and os.path.isdir(os.path.join(root, d))
    ]


def read_csv_rows(path):
    try:
        with open(path, encoding="utf-8-sig", newline="") as fh:
            return [dict(r) for r in csv.DictReader(fh)]
    except (OSError, UnicodeDecodeError, csv.Error):
        return []


def strip_md(cell):
    """A markdown cell without its bold/inline-code chrome."""
    out = (cell or "").strip()
    out = out.replace("**", "").replace("`", "").strip()
    if out in {"—", "–", "-", "n/a", "N/A", "None", ""}:
        return ""
    return out


def to_float(cell):
    """A percentage or price cell as a float, or None."""
    txt = strip_md(cell).replace("%", "").replace("+", "").replace(",", "")
    if not txt or txt.lower() in {"none", "null", "n/a", "-"}:
        return None
    try:
        return float(txt)
    except ValueError:
        return None


LEAD_NUM = re.compile(r"^([+-]?\d+(?:\.\d+)?)")


def lead_float(cell):
    """The leading signed number in a cell, ignoring anything after it.

    The correlation matrix publishes `+0.92 🟥` - a number plus a colour-band
    emoji. Plain float() refuses it, so the number is taken from the front and
    the band glyph is discarded rather than the cell being read as missing.
    """
    txt = strip_md(cell).replace(",", "")
    m = LEAD_NUM.match(txt)
    if not m:
        return None
    try:
        return float(m.group(1))
    except ValueError:
        return None


def ticker_column(rows):
    """Which column carries the ticker, and why.

    `symbol` and `ticker` are tickers by name. `name` is a ticker only on the
    dates where the routine put the symbol in that column (2026-10-26 and
    2026-10-27); on 2026-10-23 the same column holds company names. The rule is
    therefore: accept `name` only when every non-empty value looks like a ticker.
    """
    if not rows:
        return None, None
    cols = rows[0].keys()
    for col in ("symbol", "ticker"):
        if col in cols:
            return col, col
    if "name" in cols:
        values = [strip_md(r.get("name")) for r in rows]
        values = [v for v in values if v]
        if values:
            good = sum(1 for v in values if TICKER_RE.match(v))
            # A majority rule, not all-or-nothing: on 2026-10-26 a single
            # preferred-share line (`HPE/PC`) failed a strict test and discarded
            # a whole 200-row board. The exception count is returned so a caller
            # can report it rather than absorb it.
            if good >= 0.9 * len(values):
                odd = len(values) - good
                note = "name holds tickers on this date"
                if odd:
                    note += " (%d value(s) not ticker-shaped, kept as-is)" % odd
                return "name", note
    return None, None


def tickers_from(rows):
    """The board's tickers, uppercased and de-duplicated, in file order."""
    col, _note = ticker_column(rows)
    if not col:
        return []
    seen, out = set(), []
    for row in rows:
        t = strip_md(row.get(col)).upper()
        if not t or t in seen:
            continue
        seen.add(t)
        out.append(t)
    return out


def ticker_variants(t):
    """Join-key candidates for one ticker, most likely spelling first."""
    out = [t]
    if "-" in t:
        out.append(t.replace("-", "."))
        out.append(t.replace("-", ""))
    if "." in t:
        out.append(t.replace(".", "-"))
    return [v for i, v in enumerate(out) if v and v not in out[:i]]


def change_column(rows, date):
    """The column holding THIS session's change, and the rule that picked it.

    Preference order:
      1. `today_change` - the current schema's own name for it
      2. a column stamped with the directory date (`chg_1030_pct`,
         `chg_pct_2026-11-06`, `close_2026-11-06` is not a change column)
      3. `change_pct`, then `change` - the early schema, which was already the
         session change rather than a multi-period performance figure
    """
    if not rows:
        return None, None
    cols = list(rows[0].keys())
    if "today_change" in cols:
        return "today_change", "current schema"
    mmdd = date[5:7] + date[8:10]
    candidates = [
        c for c in cols
        if ("chg" in c.lower() or "change" in c.lower())
        and (mmdd in c or date in c)
    ]
    if candidates:
        return candidates[0], "stamped with the directory date"
    for c in ("change_pct", "change"):
        if c in cols:
            return c, "early schema"
    return None, None


# Sector names that belong to exactly one of the two vocabularies in this repo.
# Terms the two SHARE - "Utilities", "Energy", "Industrials" - cannot discriminate
# and are deliberately absent: keying on a shared term labelled every FactSet
# board "gics" because almost every board carries a utility.
GICS_ONLY = {
    "Information Technology", "Health Care", "Financials", "Consumer Discretionary",
    "Consumer Staples", "Materials", "Real Estate", "Communication Services",
}
FACTSET_ONLY = {
    "Electronic Technology", "Technology Services", "Health Technology",
    "Health Services", "Finance", "Energy Minerals", "Non-Energy Minerals",
    "Producer Manufacturing", "Distribution Services", "Retail Trade",
    "Consumer Non-Durables", "Consumer Durables", "Commercial Services",
    "Industrial Services", "Process Industries", "Consumer Services",
    "Communications", "Transportation", "Miscellaneous",
}


def sector_taxonomy(values):
    """Which of the two vocabularies a set of sector labels belongs to.

    Decided by which vocabulary's EXCLUSIVE terms appear more often, so a label
    both share cannot cast a vote.
    """
    values = {v for v in values if v}
    if not values:
        return None
    g, f = len(values & GICS_ONLY), len(values & FACTSET_ONLY)
    if g > f:
        return "gics"
    if f > g:
        return "factset-like"
    return "indeterminate" if values else None


def sector_column(rows):
    """The sector column and which taxonomy its vocabulary looks like."""
    if not rows:
        return None, None
    cols = rows[0].keys()
    col = "sector" if "sector" in cols else ("gics_sector" if "gics_sector" in cols else None)
    if not col:
        return None, None
    values = {strip_md(r.get(col)) for r in rows if strip_md(r.get(col))}
    return col, sector_taxonomy(values)


# ------------------------------------------------------------------ markdown

def md_tables(text):
    """Every markdown table in a document: (start_line, headers, rows).

    Headers are normalised - bold and inline code stripped. A row shorter than
    the header is padded so callers can index by column name.
    """
    out = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.startswith("|") or i + 1 >= len(lines):
            i += 1
            continue
        header = [strip_md(c) for c in line.strip().strip("|").split("|")]
        sep = lines[i + 1]
        if not sep.startswith("|") or set(sep.replace("|", "").replace("-", "").replace(":", "").strip()):
            i += 1
            continue
        rows = []
        j = i + 2
        while j < len(lines) and lines[j].startswith("|"):
            cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
            if len(cells) < len(header):
                cells = cells + [""] * (len(header) - len(cells))
            rows.append(dict(zip(header, cells[:len(header)])))
            j += 1
        out.append((i, header, rows))
        i = j
    return out


def table_with(text, *wanted):
    """The first table whose header contains every wanted column."""
    for start, header, rows in md_tables(text):
        if all(w in header for w in wanted):
            return start, header, rows
    return None, [], []


def table_after(text, heading_substring, *wanted):
    """The first table after a heading that mentions `heading_substring`."""
    lines = text.splitlines()
    begin = 0
    for i, line in enumerate(lines):
        if line.startswith("#") and heading_substring in line:
            begin = i
            break
    tail = "\n".join(lines[begin:])
    offset, header, rows = table_with(tail, *wanted)
    return (begin + offset if offset is not None else None), header, rows


# ---------------------------------------------------------------- provenance

def eod_dates():
    """Every settled session us-eod/ publishes, oldest first."""
    root = os.path.join(REPO, "us-eod")
    if not os.path.isdir(root):
        return []
    out = []
    for name in sorted(os.listdir(root)):
        if name.endswith(".csv") and DATE_RE.match(name[:-4]):
            out.append(name[:-4])
    return out


def load_eod(date):
    """One settled session, indexed by bare ticker.

    Schema drift this absorbs: the files dated 2026-10-20 through 2026-10-27 key
    the ticker as `NASDAQ:NVDA`, exchange-qualified; 2026-10-28 onward use the
    bare symbol. Both are indexed under the bare symbol, and the qualified
    spelling is kept as an alias so either join key works.

    Returns (rows, index, dupes).
    """
    rows = read_csv_rows(os.path.join(REPO, "us-eod", date + ".csv"))
    index, dupes = {}, 0
    for row in rows:
        raw = (row.get("ticker") or "").strip().upper()
        if not raw:
            continue
        bare = raw.split(":")[-1]
        keys = [bare]
        if raw != bare:
            keys.append(raw)
        for v in list(keys):
            keys.extend(ticker_variants(v))
        for key in keys:
            if key in index:
                if index[key] is not row:
                    dupes += 1
                continue
            index[key] = row
    return rows, index, dupes


def eod_match(index, ticker):
    """The settled row for a ticker, and which spelling matched."""
    t = (ticker or "").strip().upper()
    for key in ticker_variants(t):
        if key in index:
            return index[key], ("exact" if key == t else "variant %s" % key)
    return None, None


def build_stamp():
    """The build date, to the day.

    Deliberately not to the minute: these builders are re-run often and this repo
    is shared across crons, so a clock time would rewrite every derived file on
    every run and bury real changes in timestamp churn. A same-day rebuild that
    changed nothing should produce no diff.
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")


def provenance(source, covers, extra=None):
    """One provenance line, in the shape AGENTS.md asks every artifact to carry."""
    parts = [
        "**Source:** %s" % source,
        "**Built:** %s" % build_stamp(),
        "**Covers:** %s" % covers,
    ]
    if extra:
        parts.append(extra)
    return " · ".join(parts)


def write_if_changed(path, text):
    """Write text to path; return 'written', 'unchanged' or 'error'."""
    try:
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                if fh.read() == text:
                    return "unchanged"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        return "written"
    except OSError as exc:
        return "error: %s" % exc


def write_json(path, obj):
    text = json.dumps(obj, indent=1, sort_keys=False) + "\n"
    return write_if_changed(path, text)
