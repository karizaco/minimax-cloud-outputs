#!/usr/bin/env python3
"""Assemble the setup the routines each see a piece of, and score it next session.

The screener skill defines the actionable object as Stalk: on the master list,
near a short moving average, and carrying a confirming tag. What the briefs lead
with is Tier-A, a convergence cap. The skill also says a name's stylist origins
go into a setup-journal when a trade is opened. That journal does not exist.

This builder does not change any routine. It does not write into daily-screens/,
earnings/, or us-eod/. Those directories are what the MiniMax agent publishes.
Everything here is a join, written under derived/.

Two artifacts:

  derived/<date>/setup-card.md
      The evening's published Stalk and Tier-A, each number stamped with the
      session it belongs to, the gap path and the catalyst status copied from
      the morning scanner, and the price tags that can be recomputed from
      us-eod/. A second table ranks the morning gaps the scanner did not look
      up a catalyst for, where the gap later held or extended.

  derived/setup-journal.md
      Every published Stalk or Tier-A name scored against the NEXT settled
      session: the open gap and the close, both versus the close the sweep
      was published against. A name whose next session has not settled yet
      is listed as unscored, not dropped.

The price tags follow the skill's own formulas in
karizaco/maxhermes-migration cloud-prompts/skills/stock-screener-suite/references/tiering.md.
Where this archive cannot supply the history the formula needs (a 50-session
compression window, a MACD series), the tag is `not_recomputable` and the
reason is printed. A blank is never treated as "the tag did not fire".

  python3 scripts/build_setups.py
  python3 scripts/build_setups.py --check
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402
import build_gap_reconciliation as G  # noqa: E402

SCREENS = "daily-screens"
OUT_ROOT = "derived"

# Skill thresholds, copied so a reader can see them without opening the other repo.
GAP_UP_PCT = 4.0
GAP_UP_RVOL = 2.0
NEAR_MA_PCT = 2.0
HIGHER_LOW_RANGE = 0.08
COMPRESSION_RATIO = 0.6
MIN_VOL_BARS = 5

# Next-session path. Same idea as the gap reconciliation, applied to the open
# gap versus the close of the entry session. Describes the path only.
HOLD_FRACTION = 0.5
FLAT_PP = 0.25


def screen_dates():
    out = []
    for date in J.dated_dirs(SCREENS):
        d = os.path.join(J.REPO, SCREENS, date)
        if os.path.exists(os.path.join(d, "tier-a.csv")) or os.path.exists(os.path.join(d, "stalk.csv")):
            out.append(date)
    return out


def read_board(date, stem):
    path = os.path.join(J.REPO, SCREENS, date, stem + ".csv")
    rows = J.read_csv_rows(path)
    col, note = J.ticker_column(rows)
    by_ticker = {}
    if not col:
        return by_ticker, note, os.path.exists(path)
    for row in rows:
        t = J.strip_md(row.get(col)).upper()
        if t:
            by_ticker[t] = row
    return by_ticker, note, True


def read_json(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def screen_session(date):
    results = read_json(os.path.join(J.REPO, SCREENS, date, "_results.json"))
    if results.get("data_as_of"):
        return results["data_as_of"], "_results.json"
    decisions = read_json(os.path.join(J.REPO, SCREENS, date, "_decisions.json"))
    if decisions.get("data_as_of"):
        return decisions["data_as_of"], "_decisions.json"
    return None, None


def load_bars():
    """Every settled bar, keyed by bare ticker, oldest first."""
    bars = {}
    for date in J.eod_dates():
        rows, _index, _dupes = J.load_eod(date)
        for row in rows:
            raw = (row.get("ticker") or "").strip().upper()
            if not raw:
                continue
            t = raw.split(":")[-1]
            bars.setdefault(t, []).append({
                "date": date,
                "open": J.to_float(row.get("open")),
                "high": J.to_float(row.get("high")),
                "low": J.to_float(row.get("low")),
                "close": J.to_float(row.get("close")),
                "volume": J.to_float(row.get("volume")),
                "sma_20": J.to_float(row.get("sma_20")),
                "gap_pct": J.to_float(row.get("gap_pct")),
                "rel_volume": J.to_float(row.get("rel_volume")),
            })
    for t in bars:
        bars[t].sort(key=lambda b: b["date"])
    return bars


def bars_through(series, date):
    return [b for b in series if b["date"] <= date]


def recompute_tags(series, date):
    """Price tags the archive can actually recompute, plus the ones it cannot.

    A tag that fires is a copy of the skill's formula on the bars this repo
    holds. A tag that cannot be run is named, with the reason. Neither is a
    judgement on the routine that published the name.
    """
    hist = bars_through(series, date)
    fired, blocked = [], []
    if not hist or hist[-1]["date"] != date:
        return {
            "fired": [],
            "blocked": ["no settled bar for the observation session"],
            "detail": {},
        }
    bar = hist[-1]
    detail = {}

    # gap-up ready: open vs prior close, and volume vs its own recent average.
    if len(hist) >= 2 and bar["open"] is not None and hist[-2]["close"]:
        gap = (bar["open"] / hist[-2]["close"] - 1.0) * 100.0
        detail["open_vs_prior_close_pct"] = round(gap, 2)
        vols = [b["volume"] for b in hist[:-1] if b["volume"]]
        if len(vols) >= MIN_VOL_BARS and bar["volume"]:
            avg = sum(vols) / len(vols)
            rvol = bar["volume"] / avg if avg else None
            detail["rvol_vs_prior_bars"] = round(rvol, 2) if rvol is not None else None
            detail["rvol_window_sessions"] = len(vols)
            if gap > GAP_UP_PCT and rvol is not None and rvol > GAP_UP_RVOL:
                fired.append("gap-up ready")
        else:
            blocked.append(
                "gap-up ready volume leg: %d prior volume bar(s), need %d "
                "(the open-gap leg is in detail, and is not the full tag)"
                % (len(vols), MIN_VOL_BARS))
    else:
        blocked.append("gap-up ready: no prior settled close to measure the open against")

    # higher-low base: low above the low five sessions ago, and a tight 5-session range.
    if len(hist) >= 6 and bar["low"] is not None and bar["close"]:
        window = hist[-6:]
        lows = [b["low"] for b in window if b["low"] is not None]
        highs = [b["high"] for b in window if b["high"] is not None]
        if len(lows) == 6 and len(highs) == 6:
            rng = (max(highs) - min(lows)) / bar["close"]
            detail["higher_low"] = bar["low"] > window[0]["low"]
            detail["range_5_over_close"] = round(rng, 3)
            if bar["low"] > window[0]["low"] and rng < HIGHER_LOW_RANGE:
                fired.append("higher-low base")
        else:
            blocked.append("higher-low base: a bar in the 6-session window has no high or low")
    else:
        blocked.append("higher-low base: fewer than 6 settled sessions in us-eod/")

    # near the 20-day average. The skill also uses a 10-day average; this archive
    # does not carry one, so only the 20-day leg is attempted.
    sma = bar["sma_20"]
    sma_note = "vendor sma_20"
    if sma is None and len(hist) >= 20:
        closes = [b["close"] for b in hist[-20:] if b["close"] is not None]
        if len(closes) == 20:
            sma = sum(closes) / 20.0
            sma_note = "mean of the last 20 settled closes in us-eod/"
    if sma and bar["close"]:
        dist = abs(bar["close"] / sma - 1.0) * 100.0
        detail["dist_sma20_pct"] = round(dist, 2)
        detail["sma20_source"] = sma_note
        if dist <= NEAR_MA_PCT:
            fired.append("within 2% of sma20")
    else:
        blocked.append(
            "within 2% of sma20: no sma_20 on the bar and fewer than 20 settled "
            "closes in us-eod/ (the 10-day average the skill also uses is not in this archive)")

    blocked.append(
        "compression: the skill's formula needs 50 sessions of (high-low)/close; "
        "us-eod/ holds %d session(s) for this name. Not recomputed." % len(hist))
    blocked.append(
        "MACD cross-up: us-eod/ has no MACD series. Not recomputed.")
    return {"fired": fired, "blocked": blocked, "detail": detail}


def next_session(date, eod_dates):
    later = [d for d in eod_dates if d > date]
    return later[0] if later else None


def prior_session(date, eod_dates):
    earlier = [d for d in eod_dates if d < date]
    return earlier[-1] if earlier else None


def entry_path(open_gap, close_change):
    """Path from the entry open to the entry close. Not a recommendation."""
    if close_change is None:
        return "no_close"
    if open_gap is None:
        if abs(close_change) < FLAT_PP:
            return "flat"
        return "up" if close_change > 0 else "down"
    if open_gap * close_change < 0:
        return "reversed" if abs(close_change) >= FLAT_PP else "faded"
    if abs(close_change) < FLAT_PP:
        return "flat"
    if abs(open_gap) < FLAT_PP:
        return "up" if close_change > 0 else "down"
    if abs(close_change) >= abs(open_gap) * HOLD_FRACTION:
        return "held"
    return "faded"


def field(row, *names):
    if not row:
        return None
    for name in names:
        if name in row and J.strip_md(row.get(name)):
            return J.to_float(row.get(name)) if name != "stylists" else J.strip_md(row.get(name))
    return None


def text_field(row, *names):
    if not row:
        return None
    for name in names:
        if name in row:
            v = J.strip_md(row.get(name))
            if v:
                return v
    return None


ORIGIN_TO_STYLIST = (
    ("stockbee", "stockbee"),
    ("bonde", "stockbee"),
    ("qullamaggie", "qullamaggie"),
    ("qull", "qullamaggie"),
    ("peoplewish", "peoplewish"),
    ("hernandez", "hernandez"),
    ("ariel", "hernandez"),
    ("jeff_sun", "jeff_sun"),
    ("jeff sun", "jeff_sun"),
    ("canslim", "jeff_sun"),
    ("rs leader", "qullamaggie"),
    ("adr", "peoplewish"),
    ("volume_breakout", "jeff_sun"),
)


def clean_token(value):
    return value.strip().strip("[]").strip().strip("'").strip('"').strip()


def stylist_label(row):
    """The combination, never the count.

    On 2026-11-02 and 2026-11-03 the column named `stylists` holds the count
    (`3`) and the names are in `origins`. Treating the count as a combination
    would make the journal group every name that hit three stylists together.
    """
    if not row:
        return None
    for col in ("stylists", "_stylists", "stylist_flags"):
        raw = text_field(row, col)
        if not raw or raw.isdigit():
            continue
        parts = [clean_token(p) for p in raw.replace(";", "|").replace(",", "|").split("|")]
        parts = [p for p in parts if p and not p.isdigit()]
        if parts:
            return "|".join(parts)
    origins = text_field(row, "origins")
    if not origins:
        return None
    found = []
    for part in origins.replace(";", "|").split("|"):
        low = part.lower()
        for needle, name in ORIGIN_TO_STYLIST:
            if needle in low and name not in found:
                found.append(name)
                break
    return "|".join(found) if found else None


def published_tags(row):
    raw = text_field(row, "setup_tags")
    if not raw:
        return []
    return [clean_token(p) for p in raw.replace(";", "|").split("|") if clean_token(p)]
    if not row:
        return None
    for name in names:
        v = J.strip_md(row.get(name)) if name in row else ""
        if v:
            return v
    return None


def build_cards(bars):
    eod_dates = J.eod_dates()
    cards = []
    journal_rows = []
    for date in screen_dates():
        tier, _tn, tier_present = read_board(date, "tier-a")
        stalk, _sn, stalk_present = read_board(date, "stalk")
        if not tier and not stalk:
            continue
        sess, sess_src = screen_session(date)
        regime = read_json(os.path.join(J.REPO, SCREENS, date, "_regime.json"))
        entry = next_session(date, eod_dates)
        gaps = {}
        gap_notes = []
        reactions = os.path.join(J.REPO, "earnings", date + "-reactions.md")
        if os.path.exists(reactions):
            data = G.build_one(date)
            for row in data["rows"]:
                gaps[row["ticker"]] = row
            if not data["session_resolution"]["verified"]:
                gap_notes.append(
                    "Morning-gap join for this date is unverified "
                    "(prior-close match %.0f%%). Gap paths below are provisional."
                    % (data["session_resolution"]["prior_match_rate"] * 100))
        else:
            gap_notes.append(
                "No reactions artifact for this fire (`earnings/<date>-reactions.md`), "
                "so no catalyst status and no morning-gap path.")

        names = []
        for t in sorted(set(tier) | set(stalk)):
            row = tier.get(t) or stalk.get(t)
            boards = []
            if t in stalk:
                boards.append("stalk")
            if t in tier:
                boards.append("tier-a")
            gap = gaps.get(t)
            tags = recompute_tags(bars.get(t, []), date)
            published = published_tags(row)
            label = stylist_label(row)
            obs_change = field(row, "today_change")
            if obs_change is None and row:
                ccol, _rule = J.change_column([row], date)
                if ccol and ccol != "today_change":
                    obs_change = field(row, ccol)
            names.append({
                "ticker": t,
                "boards": boards,
                "stylists": label,
                "n_stylists": text_field(row, "n_stylists", "_n_stylists"),
                "screen_close": field(row, "screen_close_resolved", "close"),
                "screen_change": field(row, "chg_pct_resolved", "change_pct", "change"),
                "observation_close": field(row, "today_close", "close"),
                "observation_change": obs_change,
                "catalyst_status": gap["catalyst_status"] if gap else None,
                "pre_mkt_pct": gap["pre_mkt_pct"] if gap else None,
                "gap_outcome": gap["outcome"] if gap else None,
                "tags_published": published,
                "tags_fired": tags["fired"],
                "tags_blocked": tags["blocked"],
                "tag_detail": tags["detail"],
            })
            if entry:
                series = bars.get(t, [])
                obs = next((b for b in series if b["date"] == date), None)
                ent = next((b for b in series if b["date"] == entry), None)
                prior_close = obs["close"] if obs else None
                open_gap = None
                close_change = None
                if prior_close and ent and ent["open"] is not None:
                    open_gap = round((ent["open"] / prior_close - 1.0) * 100.0, 2)
                if prior_close and ent and ent["close"] is not None:
                    close_change = round((ent["close"] / prior_close - 1.0) * 100.0, 2)
                journal_rows.append({
                    "published_on": date,
                    "screen_session": sess,
                    "entry_session": entry,
                    "ticker": t,
                    "boards": boards,
                    "stylists": label,
                    "prior_close": prior_close,
                    "entry_open_gap_pct": open_gap,
                    "entry_close_change_pct": close_change,
                    "path": entry_path(open_gap, close_change) if ent else "no_bar",
                })
            else:
                journal_rows.append({
                    "published_on": date,
                    "screen_session": sess,
                    "entry_session": None,
                    "ticker": t,
                    "boards": boards,
                    "stylists": label,
                    "prior_close": None,
                    "entry_open_gap_pct": None,
                    "entry_close_change_pct": None,
                    "path": "unscored",
                })

        unchecked = [
            r for r in gaps.values()
            if r["catalyst_status"] == "not_looked_up" and r["outcome"] in ("held", "extended")
        ]
        unchecked.sort(key=lambda r: -(abs(r["pre_mkt_pct"]) if r["pre_mkt_pct"] is not None else -1))

        cards.append({
            "date": date,
            "screen_session": sess,
            "screen_session_source": sess_src,
            "entry_session": entry,
            "tier_present": tier_present,
            "stalk_present": stalk_present,
            "n_stalk": len(stalk),
            "n_tier_a": len(tier),
            "regime": {
                "size_cut_pct": regime.get("size_cut_pct"),
                "uncertainty": regime.get("uncertainty"),
                "late_cycle": regime.get("late_cycle"),
                "breadth_pct_spx": regime.get("breadth_pct_spx"),
                "present": bool(regime),
            },
            "gap_notes": gap_notes,
            "names": names,
            "unchecked": [
                {
                    "ticker": r["ticker"],
                    "pre_mkt_pct": r["pre_mkt_pct"],
                    "settled_change_pct": r["settled_change_pct"],
                    "outcome": r["outcome"],
                    "on_board": r["ticker"] in tier or r["ticker"] in stalk,
                }
                for r in unchecked
            ],
        })
    return cards, journal_rows


def _fmt(v, signed=True):
    if v is None or v == "":
        return "—"
    try:
        n = float(v)
    except (TypeError, ValueError):
        return str(v)
    return ("%+.2f" % n) if signed else ("%.2f" % n)


def render_card(card):
    regime = card["regime"]
    lines = []
    lines.append("# Setup card — published %s" % card["date"])
    lines.append("")
    lines.append(J.provenance(
        "derived join over `daily-screens/<date>/{stalk,tier-a}.csv`, "
        "`earnings/<date>-reactions.md` and `us-eod/<date>.csv` "
        "(no routine artifact is modified)",
        "%d stalk name(s), %d Tier-A name(s); entry session %s"
        % (card["n_stalk"], card["n_tier_a"], card["entry_session"] or "not yet settled"),
        "read-only",
    ))
    lines.append("")
    lines.append("> **Read this before the table.**")
    lines.append(">")
    lines.append("> 1. **This is not a routine output.** The MiniMax agent keeps writing")
    lines.append(">    `daily-screens/`, `earnings/` and `us-eod/`. This card only joins them.")
    lines.append("> 2. **No direction and no size.** `held`, `faded` and `reversed` describe")
    lines.append(">    a session path. They are not an instruction.")
    lines.append("> 3. **The tradeable moment is the next open after this card's date,**")
    lines.append(">    not the close the screen describes. See the session clock.")
    if card["gap_notes"]:
        lines.append("> 4. **Degraded paths.**")
        for note in card["gap_notes"]:
            lines.append(">    - %s" % note)
    lines.append("")
    lines.append("## Session clock")
    lines.append("")
    lines.append("| Clock | Session | What the numbers on that clock describe |")
    lines.append("|---|---|---|")
    lines.append("| Screen | `%s` | the metrics the 18:30 sweep computed (`%s`) |" % (
        card["screen_session"] or "—", card["screen_session_source"] or "not recorded"))
    lines.append("| Observation | `%s` | the settled close on the day the card was published |" % card["date"])
    lines.append("| Entry | `%s` | the next settled session. A setup cannot be entered on the observation close. |" % (
        card["entry_session"] or "not yet settled"))
    lines.append("")
    lines.append("A figure in the table below is stamped with the clock it belongs to.")
    lines.append("Do not read an observation-session change as an entry.")
    lines.append("")
    lines.append("## Regime the sweep recorded")
    lines.append("")
    if not regime["present"]:
        lines.append("No `_regime.json` for this date, so no size-cut or uncertainty flag is copied.")
    else:
        lines.append("| Flag | Value |")
        lines.append("|---|---|")
        lines.append("| `size_cut_pct` | %s |" % (
            "—" if regime["size_cut_pct"] is None else regime["size_cut_pct"]))
        lines.append("| `uncertainty` | %s |" % regime["uncertainty"])
        lines.append("| `late_cycle` | %s |" % regime["late_cycle"])
        lines.append("| breadth %% (screen input) | %s |" % _fmt(regime["breadth_pct_spx"], signed=False))
        lines.append("")
        lines.append("Copied from the sweep's own regime file. A true `uncertainty` flag is a")
        lines.append("header on this card because the skill treats it as a condition on every")
        lines.append("name below, not as a footnote.")
    lines.append("")
    lines.append("## Published setups")
    lines.append("")
    lines.append("Stalk first — that is the skill's setup tier — then Tier-A names that")
    lines.append("were not also on Stalk. On this date Stalk has %d name(s) and Tier-A has %d." % (
        card["n_stalk"], card["n_tier_a"]))
    lines.append("")
    lines.append("| Ticker | Boards | Stylists | Screen close | Observation close | Observation chg | Morning gap | Gap path | Catalyst | Tags published | Tags recomputed |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|")
    ordered = sorted(card["names"], key=lambda n: (
        0 if "stalk" in n["boards"] else 1, n["ticker"]))
    for n in ordered:
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            n["ticker"],
            ", ".join(n["boards"]),
            n["stylists"] or "—",
            _fmt(n["screen_close"], signed=False),
            _fmt(n["observation_close"], signed=False),
            _fmt(n["observation_change"]),
            _fmt(n["pre_mkt_pct"]),
            n["gap_outcome"] or "—",
            n["catalyst_status"] or "no morning row",
            ", ".join(n["tags_published"]) if n["tags_published"] else "—",
            ", ".join(n["tags_fired"]) if n["tags_fired"] else "none",
        ))
    lines.append("")
    lines.append("**What the tag columns mean.** `Tags published` is copied from the screen CSV")
    lines.append("when that file has a `setup_tags` column — only some dates do. `Tags recomputed`")
    lines.append("is calculated here from `us-eod/` bars. `none` there does not mean the routine")
    lines.append("found no tag. Compression needs 50 sessions and MACD is not in `us-eod/` at all,")
    lines.append("so those two are never recomputed. The blocked list is in `setup-card.csv`.")
    lines.append("")
    lines.append("## Unchecked gaps that held")
    lines.append("")
    lines.append("Morning `PRE_GAP` names the scanner marked as not looked up, whose gap")
    lines.append("then held or extended into the observation close. Sorted by the size of")
    lines.append("the morning gap. **Not checked is not the same as no catalyst.**")
    lines.append("")
    if not card["unchecked"]:
        lines.append("None on this date, or no verified morning file to read.")
    else:
        lines.append("| Ticker | Morning gap | Observation chg | Path | Also on Stalk or Tier-A |")
        lines.append("|---|---|---|---|---|")
        for r in card["unchecked"][:25]:
            lines.append("| %s | %s | %s | %s | %s |" % (
                r["ticker"], _fmt(r["pre_mkt_pct"]), _fmt(r["settled_change_pct"]),
                r["outcome"], "yes" if r["on_board"] else "no"))
        if len(card["unchecked"]) > 25:
            lines.append("")
            lines.append("%d further unchecked held-or-extended gap(s) are in the CSV." % (
                len(card["unchecked"]) - 25))
    lines.append("")
    lines.append("A name in this table and not on the published board is a coverage hole,")
    lines.append("not a setup the screen rejected. The scanner's budget stopped at the lookup.")
    lines.append("")
    return "\n".join(lines) + "\n"


def render_card_csv(card):
    cols = ["ticker", "boards", "stylists", "n_stylists", "screen_close", "screen_change",
            "observation_close", "observation_change", "pre_mkt_pct", "gap_outcome",
            "catalyst_status", "tags_published", "tags_fired", "tags_blocked"]
    out = [",".join(cols)]
    for n in card["names"]:
        row = {
            "ticker": n["ticker"],
            "boards": "|".join(n["boards"]),
            "stylists": n["stylists"] or "",
            "n_stylists": n["n_stylists"] or "",
            "screen_close": "" if n["screen_close"] is None else n["screen_close"],
            "screen_change": "" if n["screen_change"] is None else n["screen_change"],
            "observation_close": "" if n["observation_close"] is None else n["observation_close"],
            "observation_change": "" if n["observation_change"] is None else n["observation_change"],
            "pre_mkt_pct": "" if n["pre_mkt_pct"] is None else n["pre_mkt_pct"],
            "gap_outcome": n["gap_outcome"] or "",
            "catalyst_status": n["catalyst_status"] or "",
            "tags_published": "|".join(n["tags_published"]),
            "tags_fired": "|".join(n["tags_fired"]),
            "tags_blocked": " | ".join(n["tags_blocked"]),
        }
        out.append(",".join('"%s"' % str(row[c]).replace('"', '""') if "," in str(row[c]) or '"' in str(row[c]) else str(row[c]) for c in cols))
    return "\n".join(out) + "\n"


def stylist_summary(rows):
    scored = [r for r in rows if r["path"] not in ("unscored", "no_bar", "no_close")]
    groups = {}
    for r in scored:
        key = r["stylists"] or "(stylists not in the CSV)"
        g = groups.setdefault(key, [])
        g.append(r)
    out = []
    for key, items in groups.items():
        changes = [r["entry_close_change_pct"] for r in items if r["entry_close_change_pct"] is not None]
        up = sum(1 for c in changes if c > FLAT_PP)
        down = sum(1 for c in changes if c < -FLAT_PP)
        out.append({
            "stylists": key,
            "n": len(items),
            "up": up,
            "down": down,
            "median": J.to_float(None) if not changes else _median(changes),
        })
    out.sort(key=lambda g: (-g["n"], g["stylists"]))
    return out


def _median(values):
    s = sorted(values)
    mid = len(s) // 2
    if len(s) % 2:
        return round(s[mid], 2)
    return round((s[mid - 1] + s[mid]) / 2.0, 2)


def render_journal(rows):
    scored = [r for r in rows if r["path"] not in ("unscored",)]
    unscored = [r for r in rows if r["path"] == "unscored"]
    lines = []
    lines.append("# Setup journal — next session versus the published close")
    lines.append("")
    pub = sorted({r["published_on"] for r in rows})
    lines.append(J.provenance(
        "derived join of `daily-screens/<date>/{stalk,tier-a}.csv` to the next "
        "`us-eod/<date>.csv` (no routine artifact is modified)",
        "%d published setup-row(s) across %s → %s; %d scored, %d waiting on a session that has not settled"
        % (len(rows), pub[0] if pub else "—", pub[-1] if pub else "—", len(scored), len(unscored)),
        "read-only",
    ))
    lines.append("")
    lines.append("> **Read this before the table.**")
    lines.append(">")
    lines.append("> 1. **This scores a published list. It does not recommend a name.**")
    lines.append(">    `held` means the entry session's close kept at least half the open")
    lines.append(">    gap's magnitude, in the same direction. It is a path, not a result")
    lines.append(">    to copy.")
    lines.append("> 2. **The base is the observation close** — the settled close on the day")
    lines.append(">    the sweep was published. The entry open and the entry close are both")
    lines.append(">    measured against that close, so the two numbers share one clock.")
    lines.append("> 3. **A stylist count is not a sample.** Most combinations appear once.")
    lines.append(">    The summary below does not rank them. A median over two names is a")
    lines.append(">    description, not evidence that the combination works.")
    lines.append("")
    lines.append("## By stylist combination")
    lines.append("")
    lines.append("| Stylists | Scored | Next close up | Next close down | Median next change |")
    lines.append("|---|---|---|---|---|")
    for g in stylist_summary(rows):
        if g["n"] < 2:
            continue
        lines.append("| %s | %d | %d | %d | %s |" % (
            g["stylists"], g["n"], g["up"], g["down"], _fmt(g["median"])))
    lines.append("")
    lines.append("Combinations that appear once are omitted from this table and kept in the")
    lines.append("row file. Up and down use a %.2f pp band around zero so a flat close is" % FLAT_PP)
    lines.append("neither.")
    lines.append("")
    lines.append("## Every scored setup")
    lines.append("")
    lines.append("| Published | Entry session | Ticker | Boards | Stylists | Entry open gap | Entry close chg | Path |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in sorted(scored, key=lambda r: (r["published_on"], r["ticker"])):
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
            r["published_on"], r["entry_session"], r["ticker"],
            ", ".join(r["boards"]), r["stylists"] or "—",
            _fmt(r["entry_open_gap_pct"]), _fmt(r["entry_close_change_pct"]), r["path"]))
    lines.append("")
    if unscored:
        dates = sorted({r["published_on"] for r in unscored})
        lines.append("## Not yet scored")
        lines.append("")
        lines.append("%d name-row(s) were published on %s and have no later settled session" % (
            len(unscored), ", ".join(dates)))
        lines.append("in `us-eod/`. They are waiting, not failed.")
        lines.append("")
    lines.append("## Rules")
    lines.append("")
    lines.append("| Rule | Value |")
    lines.append("|---|---|")
    lines.append("| Base | observation-session close, the day the list was published |")
    lines.append("| Entry open gap | entry open versus that close |")
    lines.append("| Entry close change | entry close versus that close |")
    lines.append("| `held` | same sign, close change at least %.0f%% of the open gap |" % (HOLD_FRACTION * 100))
    lines.append("| `faded` | same sign but under that share, or an opposite move under %.2f pp |" % FLAT_PP)
    lines.append("| `reversed` | opposite sign and a close change of at least %.2f pp |" % FLAT_PP)
    lines.append("")
    return "\n".join(lines) + "\n"


def render_journal_csv(rows):
    cols = ["published_on", "screen_session", "entry_session", "ticker", "boards",
            "stylists", "prior_close", "entry_open_gap_pct", "entry_close_change_pct", "path"]
    out = [",".join(cols)]
    for r in rows:
        vals = []
        for c in cols:
            v = r[c]
            if isinstance(v, list):
                v = "|".join(v)
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
    bars = load_bars()
    cards, journal = build_cards(bars)
    if check_only:
        print("setup cards: %d" % len(cards))
        print("journal rows: %d (%d unscored)" % (
            len(journal), sum(1 for r in journal if r["path"] == "unscored")))
        if cards:
            last = cards[-1]
            print("latest %s: stalk %d tier-a %d unchecked-held %d entry %s" % (
                last["date"], last["n_stalk"], last["n_tier_a"],
                len(last["unchecked"]), last["entry_session"]))
        return 0
    for card in cards:
        target = os.path.join(J.REPO, OUT_ROOT, card["date"])
        J.write_if_changed(os.path.join(target, "setup-card.md"), render_card(card))
        J.write_if_changed(os.path.join(target, "setup-card.csv"), render_card_csv(card))
    root = os.path.join(J.REPO, OUT_ROOT)
    J.write_if_changed(os.path.join(root, "setup-journal.md"), render_journal(journal))
    J.write_if_changed(os.path.join(root, "setup-journal.csv"), render_journal_csv(journal))
    print("setup cards %d, journal rows %d" % (len(cards), len(journal)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
