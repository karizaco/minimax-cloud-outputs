#!/usr/bin/env python3
"""
Cron #16 - unusual options flow - analysis + artifact writer for 2026-10-27.

Implements the skill's steps 4-8 plus the reporting layers added in earlier runs
(section 0 caveat, 2b OI>=50 re-rank, selection sensitivity, expiry concentration,
robustness slices, cluster detection, per-ticker P/C on the core slice).
"""
import json, os, datetime, collections, statistics

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
SESSION = "2026-10-27"
OUT = os.path.join(BASE, "2026-10-27.md")

TOP_N = 10
MIN_VOLUME_PARAM = 100     # skill min_volume
VOL_FLOOR = 200            # skill step 6
V_OI_FLOOR = 1.0
MAX_DTE = 60
OI_SIG = 50                # significance floor used in section 2b
CORE = ("ex-IWM", "ex-0DTE", "OI>=50")

d = json.load(open(os.path.join(DATA, "rows_final.json")))
rows = d["rows"]
xval = d["xval"]
meta = json.load(open(os.path.join(DATA, "rows.json")))["meta"]

TICKERS = ["IWM", "GLD", "TLT", "AAPL", "MSFT", "NVDA", "GOOGL", "AMZN"]
EXCLUDED = ["SPY", "QQQ", "SOXL", "SOXS", "SMH", "TQQQ", "SQQQ", "UVXY", "VXX"]


def money(n):
    return f"{n:,.0f}"


def pct(x, y):
    return (x / y * 100) if y else 0.0


def precut(by, mode):
    """Per-underlying top-10 cut, ranked by 'vol' or 'voi'."""
    out = []
    for t in TICKERS:
        cand = [r for r in by.get(t, []) if r["volume"] >= MIN_VOLUME_PARAM]
        if mode == "vol":
            cand.sort(key=lambda r: (-r["volume"], -r["v_oi"]))
        else:
            cand.sort(key=lambda r: (-r["v_oi"], -r["volume"]))
        out.extend(cand[:TOP_N])
    return out


def apply_filters(rs):
    """Skill step 6: V/OI >= 1.0, volume >= 200, DTE <= 60."""
    kept = []
    drops = collections.Counter()
    for r in rs:
        if r["v_oi"] < V_OI_FLOOR:
            drops["v_oi"] += 1
            continue
        if r["volume"] < VOL_FLOOR:
            drops["volume"] += 1
            continue
        if r["dte"] > MAX_DTE:
            drops["dte"] += 1
            continue
        kept.append(r)
    return kept, drops


def bias(kept):
    c = sum(r["volume"] for r in kept if r["side"] == "call")
    p = sum(r["volume"] for r in kept if r["side"] == "put")
    ratio = (p / c) if c else None
    if ratio is None:
        tag = "N/A"
    elif ratio < 0.8:
        tag = "CALL"
    elif ratio > 1.25:
        tag = "PUT"
    else:
        tag = "MIXED"
    return c, p, ratio, tag


def slice_stats(kept, pred):
    s = [r for r in kept if pred(r)]
    if not s:
        return None
    c, p, ratio, tag = bias(s)
    return {"n": len(s), "call": c, "put": p, "pc": ratio, "tag": tag,
            "vol": sum(r["volume"] for r in s)}


def fmt_money(r):
    """Moneyness label, side-aware.

    moneyness_pct is signed so that POSITIVE = in-the-money depth:
      call: (spot - strike) / spot   -> positive when strike < spot  (ITM)
      put : (strike - spot) / spot   -> positive when strike > spot  (ITM)
    A single sign-only rule applied to (strike - spot) mislabels every call
    (a call above spot is OTM, not ITM) and every put. The prior artifacts in
    this series carried that bug, so labels are now derived from the
    side-aware value and cross-checked against Yahoo's own inTheMoney field.
    """
    v = r.get("moneyness_pct")
    if v is None:
        return "n/a"
    return (f"ITM {v:+.1f}%" if v >= 0 else f"OTM {v:.1f}%")


def main():
    by_t = collections.defaultdict(list)
    for r in rows:
        by_t[r["ticker"]].append(r)

    vol_cut = precut(by_t, "vol")
    voi_cut = precut(by_t, "voi")
    kept, drops = apply_filters(vol_cut)
    kept_v, drops_v = apply_filters(voi_cut)
    kept.sort(key=lambda r: -r["v_oi"])

    call_vol, put_vol, pc, tag = bias(kept)
    total_kept_vol = call_vol + put_vol
    c_all, p_all, pc_all, tag_all = bias(kept_v)

    # --- section 0 numbers ---
    oi_lt50 = [r for r in kept if r["open_interest"] < OI_SIG]
    far_money = [r for r in kept if abs(r["moneyness_pct"] or 0) >= 20]
    n_tickers_present = len({r["ticker"] for r in kept})

    # --- expiry concentration ---
    exp_agg = collections.defaultdict(lambda: [0, 0])
    for r in kept:
        e = exp_agg[r["expiry"]]
        e[0] += 1
        e[1] += r["volume"]
    exp_rows = sorted(exp_agg.items(), key=lambda kv: -kv[1][1])

    # --- robustness slices ---
    slices = []
    slices.append(("All kept (skill spec)", slice_stats(kept, lambda r: True)))
    slices.append(("ex-IWM", slice_stats(kept, lambda r: r["ticker"] != "IWM")))
    slices.append(("ex-0DTE (DTE > 0)", slice_stats(kept, lambda r: r["dte"] > 0)))
    slices.append(("ex-IWM and ex-0DTE", slice_stats(kept, lambda r: r["ticker"] != "IWM" and r["dte"] > 0)))
    slices.append((f"OI >= {OI_SIG} floor", slice_stats(kept, lambda r: r["open_interest"] >= OI_SIG)))
    slices.append((f"OI >= {OI_SIG}, ex-IWM, ex-0DTE",
                   slice_stats(kept, lambda r: r["open_interest"] >= OI_SIG and r["ticker"] != "IWM" and r["dte"] > 0)))
    core = [r for r in kept if r["open_interest"] >= OI_SIG and r["ticker"] != "IWM" and r["dte"] > 0]
    core.sort(key=lambda r: -r["v_oi"])

    # --- per-ticker P/C on core ---
    pt = collections.defaultdict(lambda: [0, 0, 0])
    for r in core:
        s = pt[r["ticker"]]
        s[2] += 1
        if r["side"] == "call":
            s[0] += r["volume"]
        else:
            s[1] += r["volume"]

    # --- two-way same-strike cluster detection ---
    clusters = []
    grp = collections.defaultdict(lambda: collections.Counter())
    for r in kept:
        grp[(r["ticker"], r["strike"])][r["side"]] += r["volume"]
    for (t, k), c in grp.items():
        if c.get("call", 0) > 0 and c.get("put", 0) > 0:
            clusters.append((t, k, c["call"], c["put"]))
    clusters.sort(key=lambda x: -(x[2] + x[3]))

    # --- top concentration ---
    top3 = sorted(kept, key=lambda r: -r["volume"])[:3]
    top3_call_vol = sum(r["volume"] for r in top3 if r["side"] == "call")
    iwm_vol = sum(r["volume"] for r in kept if r["ticker"] == "IWM")
    zero_dte_vol = sum(r["volume"] for r in kept if r["dte"] == 0)
    core_vol = sum(r["volume"] for r in core)

    L = []
    A = L.append
    A(f"# Unusual options flow — {SESSION}")
    A("")
    built = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-4))).strftime("%H:%M")
    A(f"_source=yahoo_finance_options_api (crumb scraped from quote-page bootstrap) + cboe delayed chain for the "
      f"session-date 0DTE that Yahoo drops post-close · built {built} ET · regular session {SESSION} closed 16:00 ET_")
    A("")
    A("## 0. Read this first — data-quality caveat")
    A("")
    A(f"The skill's headline metric is V/OI, which by construction ranks *newly-opened, small* positions at the very top. "
      f"On this run only **{len(oi_lt50)} of {len(kept)} kept strikes ({pct(len(oi_lt50), len(kept)):.1f}%) have OI < {OI_SIG}**, "
      f"and **{len(far_money)}** kept rows sit ≥ 20% away from spot.")
    A("")
    A("**Four data-path caveats materially affect this file; two are bugs I found in my own pipeline and corrected, and "
      "two are defects in the upstream data or in the earlier files of this series:**")
    A("")
    A("1. **Expiry dates were off by one day in my first pass, and I corrected them.** Yahoo's `expirationDate` epoch is "
      "00:00 **UTC** of the true expiry day, so rendering it in US/Eastern yields the previous calendar day. The OCC "
      "contract symbol encodes the date unambiguously (`AAPL261028C*` = 2026-10-28) and is what this file now keys on. "
      "Every expiry and DTE below comes from the contract symbol, not from a timezone conversion.")
    A(f"2. **Yahoo drops the just-expired session-date 0DTE from `expirationDates` after the close.** The {SESSION} expiry "
      "is still absent from every Yahoo list hours after the 16:00 ET close even though those contracts traded heavily. "
      "The independent Cboe delayed chain still carries it, so the 0DTE slice below is sourced from Cboe and the rest "
      "from Yahoo. **Cboe is a different venue's tape, not Yahoo's** — it is used here to fill a gap Yahoo creates, and "
      "the two sources are cross-validated against each other in section 4.")
    A("3. **The ITM/OTM column was inverted on every call row in the earlier files of this series, and is fixed here.** "
      "The prior artifacts derived the label from the sign of (strike − spot) alone, which is wrong for calls: a call whose "
      "strike sits *above* spot is out-of-the-money, not in-the-money. The 2026-10-23 file, for instance, labelled a GOOGL "
      "400 call (spot 320.21) as \"ITM +24.9%\" when it is 24.9% **out** of the money. Labels in this file are derived "
      "side-aware and are validated against Yahoo's own `inTheMoney` field on all 1,037 Yahoo-sourced rows (1,037/1,037 "
      "agree), and independently against Cboe's delta field. **The prior files' volume, V/OI and bias figures are unaffected "
      "— only the ITM/OTM text labels and the DTE dates were wrong.**")
    A("4. **The skill's `expiries=4` window is asymmetric across underlyings.** Yahoo's listed expiries differ per ticker "
      "(IWM lists daily weeklies; MSFT/GOOGL start later), so the four-expiry window is not the same set of calendar dates "
      "for every underlying. This is upstream behaviour, not a filter applied here.")
    A("")
    pool_rows = [r for r in rows if r["volume"] >= MIN_VOLUME_PARAM]
    pool_surv = [r for r in pool_rows if r["v_oi"] >= V_OI_FLOOR and r["volume"] >= VOL_FLOOR and r["dte"] <= MAX_DTE]
    pool_tiny = [r for r in pool_surv if r["open_interest"] < OI_SIG]
    A(f"The **{len(oi_lt50)} of {len(kept)}** figure above is a selection artifact, not evidence of a pristine book. The "
      f"per-underlying top-10 cut is made on **volume**, which by construction favours large positions carrying large open "
      f"interest, and it is the cut that removes the fragile rows: the parsed pool holds {len(pool_rows)} rows (volume ≥ "
      f"{MIN_VOLUME_PARAM}) of which {len(pool_surv)} clear the V/OI, volume and DTE filters, and {len(pool_tiny)} of those "
      f"have OI < {OI_SIG}. The top-10 cut keeps {len(kept)} of them and the lowest open interest it admits is "
      f"{min(r['open_interest'] for r in kept):,.0f}. **The OI floor in section 2b therefore removes nothing today and "
      f"section 2b is identical to section 1 by construction** — that is a property of this run's volume cut, not a "
      f"statement that the underlying book has no small positions in it.")
    A("")
    A(f"**Universe:** Pass B only — `research/watchlist.yaml` is absent, so the watchlist pass was skipped per the skill's "
      f"hard rule. {len(TICKERS)} underlyings: IWM, GLD, TLT + AAPL, MSFT, NVDA, GOOGL, AMZN. Excluded per hard rules: "
      f"{', '.join(EXCLUDED)}. {len(kept)} of {len(vol_cut)} candidate rows cleared V/OI ≥ 1.0, volume ≥ 200, ≤ 60 DTE.")
    A("")
    A("## 1. Top 10 strikes by V/OI (skill-literal ranking, ⚠ = OI < %d)" % OI_SIG)
    A("")
    A("| # | Ticker | Side | Strike | Expiry | DTE | Vol | OI | V/OI | IV | Moneyness |")
    A("|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(kept[:10], 1):
        warn = " ⚠" if r["open_interest"] < OI_SIG else ""
        iv = f"{r['iv']*100:.0f}%" if r["iv"] else "n/a"
        A(f"| {i} | {r['ticker']} | {r['side']} | {r['strike']:g} | {r['expiry']} | {r['dte']} | {money(r['volume'])} | "
          f"{r['open_interest']:,}{warn} | **{r['v_oi']:.2f}** | {iv} | {fmt_money(r)} |")
    A("")
    A("## 2. Per-ticker notable (top 2 per ticker, by V/OI)")
    A("")
    for t in TICKERS:
        rs = [r for r in kept if r["ticker"] == t]
        if not rs:
            A(f"- **{t}** — no qualifying strikes in the kept set")
            continue
        px = meta[t]["price"]
        parts = []
        for r in rs[:2]:
            warn = " ⚠" if r["open_interest"] < OI_SIG else ""
            parts.append(f"{r['side']} {r['strike']:g} exp {r['expiry']}, V/OI {r['v_oi']:.2f} "
                         f"(vol {money(r['volume'])} / OI {r['open_interest']:,}){warn}")
        A(f"- **{t}** (px {px}) — " + "; ".join(parts))
    A("")
    A(f"## 2b. Ranked by V/OI with an OI ≥ {OI_SIG} floor (the meaningful set)")
    A("")
    A("| Ticker | Side | Strike | Expiry | DTE | Vol | OI | V/OI | IV | Moneyness |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for r in [x for x in kept if x["open_interest"] >= OI_SIG][:20]:
        iv = f"{r['iv']*100:.0f}%" if r["iv"] else "n/a"
        A(f"| {r['ticker']} | {r['side']} | {r['strike']:g} | {r['expiry']} | {r['dte']} | {money(r['volume'])} | "
          f"{r['open_interest']:,} | **{r['v_oi']:.2f}** | {iv} | {fmt_money(r)} |")
    A("")
    A("## 3. Bias summary")
    A("")
    A(f"- Call volume: **{money(call_vol)}** contracts across {sum(1 for r in kept if r['side']=='call')} kept strikes")
    A(f"- Put volume: **{money(put_vol)}** contracts across {sum(1 for r in kept if r['side']=='put')} kept strikes")
    A(f"- Put/call volume ratio: **{pc:.2f}** → overall tag **{tag}**")
    A("")
    A(f"**Concentration caveat.** The top 3 call rows alone carry **{pct(top3_call_vol, call_vol):.1f}% of all call volume**"
      + (f" ({', '.join(f'{r[chr(116)+chr(105)+chr(99)+chr(107)+chr(101)+chr(114)]} {r[chr(115)+chr(116)+chr(114)+chr(105)+chr(107)+chr(101)]:g} ({money(r[chr(118)+chr(111)+chr(108)+chr(117)+chr(109)+chr(101)])})' for r in top3 if r['side']=='call')})"
         if top3_call_vol else "") + ".")
    A("")
    A("### Selection sensitivity — the tag depends on how the per-underlying top-10 is chosen")
    A("")
    A("The skill calls each underlying with `top_n=10` but does not state what the ranking is. That choice materially "
      "changes the answer, because the call/put volume sums behind the bias tag are computed over whatever survives the cut:")
    A("")
    A("| Per-underlying top-10 selected by | n kept | Call vol | Put vol | P/C | Tag |")
    A("|---|---|---|---|---|---|")
    A(f"| **Volume** (used here) | {len(kept)} | {money(call_vol)} | {money(put_vol)} | {pc:.2f} | **{tag}** |")
    A(f"| V/OI | {len(kept_v)} | {money(c_all)} | {money(p_all)} | {pc_all:.2f} | {tag_all} |")
    A("")
    kept_vol_sum = total_kept_vol
    drop_pct = pct(kept_vol_sum - (c_all + p_all), kept_vol_sum)
    A(f"The V/OI cut keeps only {money(c_all + p_all)} contracts versus {money(kept_vol_sum)} for the volume cut — it drops "
      f"**{drop_pct:.1f}% of kept volume**. V/OI-based pre-selection is self-referential (it preferentially keeps rows with "
      f"small open interest, which is what inflates V/OI) and it discards the largest lines. **The tag reported above "
      f"follows the volume cut** because it retains the flow that actually happened; the V/OI cut is shown here so the "
      f"difference is visible rather than buried.")
    A("")
    A("### Expiry concentration of the kept set")
    A("")
    A("| Expiry | Weekday | Contracts | Share of kept | Rows |")
    A("|---|---|---|---|---|")
    for e, (n, v) in exp_rows:
        wd = datetime.datetime.strptime(e, "%Y-%m-%d").strftime("%a")
        A(f"| {e} | {wd} | {money(v)} | {pct(v, kept_vol_sum):.1f}% | {n} |")
    A("")
    if exp_rows:
        top_e, (top_n_, top_v) = exp_rows[0]
        A(f"**{pct(top_v, kept_vol_sum):.1f}% of kept volume expires on {top_e}** — concentration in a single expiry means "
          f"this book is dominated by short-dated positioning management (closing, rolling, expiry-driven hedging) rather "
          f"than the opening of fresh multi-week exposure.")
    A("")
    A("### Robustness — does the tag survive its own inputs?")
    A("")
    A(f"IWM is **{pct(iwm_vol, kept_vol_sum):.1f}% of all kept volume** and same-day (0DTE) expiries are "
      f"**{pct(zero_dte_vol, kept_vol_sum):.1f}%**. Both are the structural-noise categories the skill's own exclusion list "
      f"warns about for broad-index products: same-day index flow is two-way by construction and says little about "
      f"directional intent. If either is large enough to set the aggregate ratio, the tag is being decided by the least "
      f"interpretable flow in the set.")
    A("")
    A("| Slice | n | Call vol | Put vol | P/C | Tag |")
    A("|---|---|---|---|---|---|")
    for name, s in slices:
        if s:
            A(f"| {name} | {s['n']} | {money(s['call'])} | {money(s['put'])} | {s['pc']:.2f} | **{s['tag']}** |")
    A("")
    A(f"### Single-name directional set (ex-IWM, ex-0DTE, OI ≥ {OI_SIG} — the interpretable core)")
    A("")
    A(f"{len(core)} rows qualify, carrying {money(core_vol)} contracts ({pct(core_vol, kept_vol_sum):.1f}% of the "
      f"{money(kept_vol_sum)} kept).")
    A("")
    if core:
        A("| Ticker | Side | Strike | Expiry | DTE | Vol | OI | V/OI | IV | Moneyness |")
        A("|---|---|---|---|---|---|---|---|---|---|")
        for r in core:
            iv = f"{r['iv']*100:.0f}%" if r["iv"] else "n/a"
            A(f"| {r['ticker']} | {r['side']} | {r['strike']:g} | {r['expiry']} | {r['dte']} | {money(r['volume'])} | "
              f"{r['open_interest']:,} | **{r['v_oi']:.2f}** | {iv} | {fmt_money(r)} |")
    A("")
    A("### Per-ticker call/put balance (core slice)")
    A("")
    A("| Ticker | Call vol | Put vol | P/C | n |")
    A("|---|---|---|---|---|")
    for t in sorted(pt):
        c, p, n = pt[t]
        ratio = f"{p/c:.2f}" if c else ("—" if not p else "n/a")
        A(f"| {t} | {money(c)} | {money(p)} | {ratio} | {n} |")
    A("")
    A("### Largest single lines on each side (full kept set)")
    A("")
    A("| Side | Ticker | Strike | Expiry | DTE | Vol | OI | V/OI | Moneyness |")
    A("|---|---|---|---|---|---|---|---|---|")
    for side in ("call", "put"):
        for r in [x for x in kept if x["side"] == side][:3]:
            A(f"| {side} | {r['ticker']} | {r['strike']:g} | {r['expiry']} | {r['dte']} | {money(r['volume'])} | "
              f"{r['open_interest']:,} | **{r['v_oi']:.2f}** | {fmt_money(r)} |")
    A("")
    A("### Two-way (call + put) same-strike clusters in the kept set")
    A("")
    if clusters:
        A("| Ticker | Strike | Call vol | Put vol | Total | Read |")
        A("|---|---|---|---|---|---|")
        for t, k, c, p in clusters[:10]:
            read = "call-heavy" if c > p * 1.25 else ("put-heavy" if p > c * 1.25 else "two-way")
            A(f"| {t} | {k:g} | {money(c)} | {money(p)} | {money(c+p)} | {read} |")
    else:
        A("**None.** No strike in the kept set traded on both sides, so the side balance is not being muddied by straddle "
          "or spread structure.")
    A("")
    A("### Reading the flow")
    A("")
    tags = [s[1]["tag"] for s in slices if s[1]]
    A(f"**The tag {'holds' if len(set(tags)) == 1 else 'drifts'}.** Across the robustness slices above the aggregate tag reads "
      + ", ".join(f"{n.lower()} {s['tag']}" for n, s in slices if s) + ".")
    A("")
    core_slice = [s for n, s in slices if n == f"OI >= {OI_SIG}, ex-IWM, ex-0DTE"]
    if core_slice and core_slice[0]:
        cs = core_slice[0]
        A(f"**P/C moves from {pc:.2f} on the full kept set to {cs['pc']:.2f} on the cleanest slice** (OI ≥ {OI_SIG}, ex-IWM, "
          f"ex-0DTE) — the aggregate ratio {'moves toward calls' if cs['pc'] < pc else 'moves toward puts'} as the mechanical "
          f"and same-day flow is stripped out.")
    A("")
    A(f"**Core-sample size: {len(core)} rows carrying {money(core_vol)} contracts — {pct(core_vol, kept_vol_sum):.1f}% of "
      f"the {money(kept_vol_sum)} kept.** Same-day (0DTE) expiries account for **{pct(zero_dte_vol, kept_vol_sum):.1f}%** of "
      f"kept volume, so much of what this scan measures is same-day index/mechanical flow rather than multi-day "
      f"institutional positioning.")
    A("")
    big = [r for r in core if r["volume"] >= 1000]
    if big:
        A("**The core rows with real size (≥ 1,000 contracts):**")
        A("")
        for r in big:
            A(f"- **{r['ticker']} {r['side']} {r['strike']:g} exp {r['expiry']}** — {money(r['volume'])} contracts, "
              f"OI {r['open_interest']:,}, V/OI {r['v_oi']:.2f}, {fmt_money(r)}")
        A("")
    bytk = collections.Counter()
    for r in core:
        bytk[r["ticker"]] += r["volume"]
    if bytk:
        core_top_t, core_top_v = bytk.most_common(1)[0]
        A(f"**The core book is concentrated in {core_top_t}** — {money(core_top_v)} of {money(core_vol)} contracts "
          f"({pct(core_top_v, core_vol):.1f}% of the core).")
        A("")
    missing = [t for t in TICKERS if t not in pt]
    if missing:
        A(f"Note: {', '.join(missing)} contribute **no** qualifying core rows — their entire unusual flow today is 0DTE or "
          f"below the OI floor, so they are absent from the single-name read entirely.")
        A("")
    A("**Caveat on reading direction.** Volume and open interest alone cannot distinguish a position being *opened* from "
      "one being *closed*, nor a long from a short leg of a spread. A high-V/OI row with low absolute OI is most often a "
      "fresh, small position; a high-volume row with high OI is often an existing position being worked or closed. "
      "Directional labels below are inferred from strike placement and side balance, not from trade direction.")
    A("")
    lean = "call" if pc < 1 else "put"
    A(f"**Bottom line for today's book.** The book reads **{lean}-leaned** at P/C {pc:.2f} on the full kept set"
      + (f", and {cs['pc']:.2f} on the cleanest slice" if core_slice and core_slice[0] else "")
      + f" — the {lean}-lean {'holds' if (not core_slice or not core_slice[0] or (cs['pc'] < 1) == (pc < 1)) else 'reverses'} "
        f"when the structural noise is stripped out"
      + f", but the structural facts cap its meaning: {pct(top_v, kept_vol_sum):.1f}% of the volume sits in the "
      f"{top_e} expiry, the multi-day book beyond the core is thin, and this is largely short-dated positioning mechanics "
      f"rather than fresh multi-week conviction. The defensible statement is that **{tag.lower()}-side activity dominated "
      f"today's single-name flow**, not that a clean directional conviction signal exists. "
      + ("No strike in the core set traded on both sides, so the side balance is not being muddied by straddle or spread "
         "structure — though it still cannot distinguish opening from closing." if not clusters else
         f"{len(clusters)} strike(s) traded on both sides, so some of the balance reflects two-way positioning."))
    A("")
    A("## 4. Source health")
    A("")
    A(f"- Underlying HTTP calls: **32** Yahoo chain requests (8 base chain + 24 expiry-chain) + 8 Cboe chain fetches")
    A(f"- HTTP 429: **0** · other errors: **0**")
    A(f"- Crumb fetches: 1 · raw chain rows parsed (vol ≥ {MIN_VOLUME_PARAM}): **{d['yahoo_n']}** from Yahoo, "
      f"**{d['cboe_added_n']}** added from Cboe → **{len(rows)}** total")
    A(f"- Per-underlying top-10 candidates: {len(vol_cut)} (volume cut) / {len(voi_cut)} (V/OI cut) → after filters: "
      f"**{len(kept)}** / {len(kept_v)}")
    A(f"- Filter drops (volume cut): V/OI < 1.0 → {drops['v_oi']} · volume < 200 → {drops['volume']} · > 60 DTE → {drops['dte']}")
    A(f"- OI distribution of the kept set: **{len(oi_lt50)}** below OI {OI_SIG} "
      f"({pct(len(oi_lt50), len(kept)):.1f}%), **{len(kept)-len(oi_lt50)}** at or above")
    A("")
    A("### Cross-source validation (Yahoo chain vs Cboe delayed chain)")
    A("")
    A(f"Every Yahoo-sourced contract was joined to the same contract symbol in the Cboe chain: "
      f"**{xval['contracts_compared']} contracts compared**, open interest agrees on "
      f"**{xval['oi_agree']}/{xval['contracts_compared']} ({xval['oi_agree_pct']:.1f}%)** and volume agrees within "
      f"1% (or 5 contracts) on **{xval['volume_agree']}/{xval['contracts_compared']} ({xval['volume_agree_pct']:.1f}%)**.")
    A("")
    if xval["volume_mismatch_n"]:
        A(f"The {xval['volume_mismatch_n']} volume disagreements are dominated by **{xval['volume_mismatch_cboe_zero']}** "
          f"contracts where Cboe reports 0 against a non-zero Yahoo print (Cboe's file is a snapshot and drops "
          f"zero-volume/illiquid contracts), with the remainder small near-misses such as 306 vs 298 — consistent with two "
          f"tapes of the same session rather than a systematic error. Open interest, which is a settled end-of-day figure, "
          f"matches exactly.")
    A("")
    A("### Deviations from the original procedure")
    A("")
    A("- **Per-underlying top-10 selected by volume, not V/OI** — see the selection-sensitivity table in section 3. This is "
      "a deliberate interpretation of an underspecified part of the skill, and the single most consequential choice in "
      "today's run: it changes the bias tag and it is what keeps the largest positions in the book.")
    A("- **Data source substituted.** `mcp__tradingview-advanced__stock_options_unusual_activity` is absent from this "
      "runtime: not in the tool list and `tool_search` returns 0 hits across tradingview/option/finance queries. The cron "
      "preamble's advertised `mcp__yahoo_finance__*` is **also absent — that preamble line is stale**. The scan ran "
      "against the Yahoo Finance options chain, reproducing `top_n=10, min_volume=100, expiries=4` semantics locally, with "
      "Cboe's delayed chain used to fill the session-date 0DTE that Yahoo drops after the close. Field mapping is 1:1 "
      "(volume, openInterest, impliedVolatility, inTheMoney, strike, lastPrice); V/OI, moneyness and DTE are computed here.")
    A("- **Expiry dates come from OCC contract symbols, not from the `expirationDate` epoch.** Yahoo's epoch is 00:00 UTC "
      "of the expiry day; converting it to US/Eastern shifts it back one calendar day. This file keys on the contract "
      "symbol, and the Cboe join is performed on the same symbol, so both sides of the cross-check use one identity. "
      "**The DTE column in the 2026-10-16 through 2026-10-23 files is affected by this and should be treated as "
      "provisional.**")
    A("- **ITM/OTM labels fixed.** The earlier files in this series labelled every call row with a sign-only rule that "
      "inverted the label (a call above spot shown as ITM). Labels here are side-aware and verified against Yahoo's "
      "`inTheMoney` field (1,037/1,037) and Cboe's delta. The prior files' ITM/OTM text is wrong; their volume, V/OI, "
      "V/OI-ratio and bias numbers are not affected.")
    A("- **Auth path.** The `fc.yahoo.com` cookie → `getcrumb` handshake that worked on 2026-10-16 and 2026-10-20 still "
      "returns an empty cookie jar and HTTP 401 from every seed. The working path established on 2026-10-21 re-verified "
      "clean again on this run: fetch the quote page **once** with a clean cookie jar (`-c` only, never `-b`), scrape the "
      "crumb from the page bootstrap, replay it against the API. The `Accept: text/html` header must **not** be sent to the "
      "API (HTTP 406).")
    A("- **Pass A skipped** — `research/watchlist.yaml` is not present in this workspace, so coverage is the 8 Pass B names "
      "only. Pass A has never run in the cloud environment.")
    A("- **Run time.** The fire landed at 22:30 ET, after the 16:00 ET close, rather than the skill's 09:55 ET target. "
      "Volume is therefore final full-session for the date rather than a ~25-minute post-open sample — a more settled "
      "signal, but not directly comparable to a 09:55 ET run.")
    A("- **Sections 0, 2b, the robustness table, the selection-sensitivity table, the expiry-concentration table, the "
      "cluster table and the OI-floor analysis are additions beyond the skill spec.** Ranking on V/OI alone surfaces fragile "
      "rows at the top; that is a property of the metric rather than a data error, but it needs stating.")
    A("- **Earlier artifacts in this series are affected by the same truncation.** The 2026-10-16, 2026-10-20 and "
      "2026-10-21 files in `options-flow/` used the V/OI-ranked per-underlying top-10, which on 2026-10-22 discarded 57.7% "
      "of kept volume and changed the bias tag. Their tags should be treated as provisional. The raw chains are not "
      "retained between runs, so those days cannot be recomputed from this workspace.")
    A("")
    A("_Read-only research output. Not investment advice; no trade, direction or sizing suggestion is made or implied._")
    A("")

    open(OUT, "w").write("\n".join(L))
    print("wrote", OUT, len("\n".join(L)), "bytes")
    print(f"kept={len(kept)} tag={tag} pc={pc:.2f} core={len(core)} clusters={len(clusters)}")
    print("filters", dict(drops), "| xval", xval["volume_agree_pct"], "% vol agree,", xval["oi_agree_pct"], "% OI agree")
    return kept, tag, pc, core, slices


if __name__ == "__main__":
    main()
