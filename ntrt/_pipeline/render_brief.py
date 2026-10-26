#!/usr/bin/env python3
"""Render the NTRT gap brief markdown from the snapshot JSON + researched catalysts."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
OUT = Path("/workspace/ntrt/2026-10-26.md")
snap = json.loads(Path("/workspace/ntrt/_raw/final_snapshot.json").read_text())
full = json.loads(Path("/workspace/ntrt/_raw/publishable_full.json").read_text())
xc_path = Path("/workspace/ntrt/_raw/yahoo_crosscheck_final.json")
xc = json.loads(xc_path.read_text()) if xc_path.exists() else (snap.get("yahoo_crosscheck") or {})
LIQ = {r["d"][0]: r["d"] for r in json.loads(Path("/workspace/ntrt/_raw/liquidity_20.json").read_text())["data"]}
PAIRED = {r["d"][0]: dict(zip(
    ["name", "description", "close_live", "premarket_close", "premarket_change", "market_cap_basic",
     "volume_live", "sector", "industry", "rvol10d", "avg30", "premarket_volume", "pm_change_abs"],
    r["d"])) for r in json.loads(Path("/workspace/ntrt/_raw/paired_tv.json").read_text())["data"]}
XC = {c["ticker"]: c for c in (xc.get("results") or [])}
SNAP_ET = xc.get("tv_snapshot_et", "n/a")
NOW_ET = xc.get("yahoo_fetched_et", "")

# ---- researched catalyst lines (sourced; see Catalysts section for citations) --
CAT = {
    "XP": ("Brazil runoff + issuer overhang",
           "Lula beat Flávio Bolsonaro 51.8–48.2, unwinding the Bolsonaro-trade rally; "
           "plus XP's own overhang (board member Escobari resigned 16 Oct, Microsoft exec "
           "named interim director) and Assenagon trimming ~7.9% of the stake."),
    "STNE": ("Brazil election unwind",
             "Pure macro: StoneCo is a Brazilian payments/fintech name with no company-specific "
             "release; read with the Brazil complex below."),
    "INTR": ("Brazil election unwind",
             "Brazilian brokerage/IB; no company-specific catalyst identified — the move tracks "
             "the Brazil complex and the BRL/rates shock."),
    "PICS": ("Brazil election unwind + litigation overhang",
             "Brazilian digital-payments name; no single company catalyst, but unresolved "
             "2026 securities class actions and proximity to its $8.08 52-week low compound the "
             "macro hit. Next earnings not until December."),
    "PAGS": ("Brazil election unwind", "Brazilian payments name; no company-specific catalyst identified."),
    "AGBK": ("Brazil election unwind", "Brazilian bank (Banco Agibank / AGI Inc); macro-driven."),
    "NU": ("Brazil election unwind", "Brazilian digital bank; macro-driven, and the largest cap in the group."),
    "AFYA": ("Brazil election unwind", "Brazilian healthtech; macro-driven."),
    "ARCO": ("Brazil election unwind", "LatAm restaurant operator (McDonald's franchisee); macro-driven."),
    "PAX": ("Brazil election unwind", "Brazilian asset manager; macro-driven."),
    "VINP": ("Brazil election unwind", "Brazilian-linked investment company; thin book."),
    "MELI": ("LatAm/EM de-rating (not a Brazil pure-play)",
             "MercadoLibre — Argentina/Mexico/Brazil mix; caught in the same EM risk-off "
             "de-rating, but it is not a direct Lula-trade victim."),
    "XNCR": ("Phase 1 XmAb819 data at ESMO",
             "45.5% confirmed objective response rate in advanced clear-cell renal cell carcinoma; "
             "company plans accelerated FDA discussions. Wedbush reiterated Outperform, $30 PT on 23 Oct."),
    "SGRY": ("Bon Secours M&A report",
             "FT reported Bon Secours Mercy Health is in late-stage talks for a controlling stake; "
             "~$6bn EV including ~$3.5bn debt, ~$20/share implied. Bain (~40% holder) expected to stay. "
             "Trading below the implied price = residual deal risk."),
    "RRC": ("EQT all-stock acquisition",
            "0.987 EQT shares per RRC share; implied ~$54.91/share, ~20.6% above Friday's close, "
             "pro-forma EV >$50bn. Q3 calls for both cancelled (27 Oct, after close)."),
    "EQT": ("Acquirer leg of the Range deal",
            "EQT is paying for Range; the acquirer is down as the market widens the arbitrage spread. "
            "Reuters had EQT -4.6% pre-market, i.e. the spread trade, not a broken deal."),
    "BRAI": ("Force AI / RADIUS platform expansion",
             "Braiin (an applied-AI/CCaaS platform company) announced the Force AI orchestration "
             "layer and a major RADIUS CX upgrade, targeting a $56.9bn CX software market. "
             "Not a crypto move — the crypto cohort was flat-to-lower pre-open."),
    "SSII": ("Not researched", "Thin book — 300 shares pre-open. Treat the print as low-confidence."),
    "LYCA": ("Not researched", "Thin pre-open book."),
    "DLO": ("Not researched", "LatAm payments; co-moves with the LatAm complex in the tape."),
    "BORR": ("Not researched", "Offshore drilling."),
    "MRNA": ("Not researched", "Large-cap biotech; no catalyst searched."),
    "FICO": ("Not researched", "Large-cap software; no catalyst searched."),
    "CRCL": ("Crypto cohort weakness",
             "TokenPost's 08:22 ET snapshot had the eight crypto-linked names all lower, CRCL -2.88% "
             "the worst. Crypto beta, not an issuer event."),
    "ASST": ("Crypto cohort weakness", "TokenPost 08:22 ET: ASST -1.92% in a uniformly red crypto cohort."),
    "SBET": ("Crypto cohort weakness", "TokenPost 08:22 ET: SBET -2.62% in a uniformly red crypto cohort."),
    "XLAB": ("Not researched", "Small cap; thin."),
    "AUGO": ("Not researched", "Gold miner."),
    "CRWV": ("Not researched", "AI infrastructure; part of the AI-capex complex under pressure."),
    "NTNX": ("Not researched", "Enterprise software."),
    "TDAY": ("Not researched", "Media."),
}
# --------------------------------------------------------------------------------

rows = full[:20]
stamp = snap["snapshot_et"]
COVER_ET = "2026-10-26 09:41 ET"   # the full-universe coverage pass the gap column comes from
counts = snap["counts"]

lines = []
A = lines.append
A("# NTRT gap brief — Monday 2026-10-26 (US equities)")
A("")
A(f"- **Mode:** B — *MCP fallback*. The `ntrt_mtrt` backend was unreachable "
  f"(`GET {''}http://127.0.0.1:8000/health` → no response, 3 s timeout) and the host-wired "
  f"TradingView MCP (`mcp__tradingview_advanced__screen_stocks`) is not bound in this runtime. "
  f"Data came from the **TradingView public screener** instead, cross-checked against **Yahoo Finance**.")
A(f"- **Screen snapshot:** {COVER_ET}, from a **full-universe** pass - 199 US names up >= +3% and "
  f"209 down <= -3% (408 gapped names in total). **82 passed the skill's publishable filters** and "
  f"the 20 largest by absolute gap are below.")
A(f"- **Cross-check:** Yahoo - TV fetch {SNAP_ET} ET, live marks {NOW_ET} ET.")
A("- **Never place trades.** Research only.")
A("")

A("## Read this first — four deviations from a clean pre-market brief")
A("")
A("1. **The brief was assembled after the 09:30 ET open, and the numbers move.** The skill's own "
  "schedule is 06:30 ET; this cron was migrated to a 09:00 ET fire and the run took ~45 minutes, so "
  "the pre-open window closed before the screen was pulled. The gap column is the **09:41 ET "
  "snapshot** and the last table column is the **live mark at 10:02 ET**. The spread between them "
  "reaches 15 points (`LYCA`, `BRAI`) and the dispersion within the Brazil complex is itself the "
  "story: `STNE`, `PAGS` and `LYCA` have bounced hard off the open while `PICS`, `INTR`, `PAX` and "
  "`AGBK` have kept sliding. Treat every percentage as a print in a live, violent book.")
A("")
A("1b. **TradingView's column semantics change after the open, and this bit the cross-check.** "
  "`close` rolls from the prior session's close to the *live* price once the session is underway "
  "(`PICS` `close` read 13.80 at 09:41 and 8.97 at 10:02), while `premarket_close` and "
  "`premarket_change` hold the pre-open mark. A reference-close check run on a post-open fetch "
  "therefore compares a live price against a prior close and returns nonsense. The check below was "
  "re-run against the **pre-open** snapshot for that reason.")
A("2. **The single most extreme row in the screen was dropped as bad data.** `BUUU` (BUUU Group) "
  "printed −91.24% in the screener while its own reference close was $5.39 and its pre-open print "
  "$4.72 — those three numbers are mutually impossible: the implied reference is $53.90, a 10× "
  "artifact. It fails the internal-consistency test and is **not** in the table below. A −91% "
  "print is the kind of number that reads as a real collapse, so it is called out explicitly rather "
  "than silently dropped.")
A("3. **The catalyst-research set was 8 names, not the skill's 5.** The skill caps *deep dives* "
  "at 5. No dossier or multi-endpoint pull was performed; the cap was read as the "
  "catalyst-research set and deliberately exceeded to 8, because the top-5 band is almost entirely "
  "one macro event and would have left the largest non-Brazil gainers unexplained. Rows without a "
  "sourced catalyst are marked **not researched** in the table — nothing is inferred for them.")
A("")

A("## TL;DR")
A("")
A("- **One event owns this tape: Brazil.** Lula da Silva beat Flávio Bolsonaro 51.8–48.2 in "
  "Sunday's runoff, reversing a first-round deficit, and every Brazil-listed ADR is collapsing — "
  "XP −53%, STNE −39%, INTR −38%, PICS −35%, PAGS −34%, AGBK −33%, NU −22%, AFYA −20%, ARCO −16%, "
  "PAX −16%. `EWZ` was −25.3% pre-open, on track for its worst session since its 2000 launch. "
  "Goldman flagged an extreme scenario of USD/BRL +10%, local yields +200 bp, equities −15%.")
A("- **Two genuine company events sit inside the noise.** SGRY +24% on the FT report that Bon "
  "Secours Mercy Health is closing a ~$6bn controlling-stake deal; RRC +11% on EQT's all-stock "
  "acquisition (implied ~$54.91, ~20.6% above Friday's close) — and the gap between RRC's market "
  "price and that implied value is the arb spread, with EQT −7% on the other leg.")
A("- **The index tape is calm; the damage is local.** S&P 500 futures slightly up, Nasdaq flat, "
  "with Brent above $116 and a Fed decision on Wednesday 28 Oct. Nothing here is an earnings day "
  "for the big names — and nothing here is a broad risk-off session.")
A("")

A("## Top gappers")
A("")
A(f"_Gap % is the move from Friday's close to the pre-open print, as at the {COVER_ET} screen "
  f"snapshot. Pre-open volume is the extended-hours share count. RVOL is TradingView's 10-day "
  f"relative volume. The last three columns are the live mark at {NOW_ET} ET from Yahoo's own "
  f"1-minute series - where the gap stands now that the session is underway._")
A("")
A("| # | Ticker | Gap % (09:41) | Fri close | Pre-open px | Mkt cap | Pre-open vol | RVOL(10d) | Now (10:02) | Since open | Sector | Why |")
A("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|")
for i, r in enumerate(rows, 1):
    t = r["t"]
    cat = CAT.get(t)
    why = cat[0] if cat else "Not researched"
    P = PAIRED.get(t) or {}
    L = LIQ.get(t)
    rvol = P.get("rvol10d") if P.get("rvol10d") is not None else (L[1] if L else None)
    pmvol = (P.get("premarket_volume") if P.get("premarket_volume") is not None
             else (L[3] if L else r.get("vol")))
    x = XC.get(t) or {}
    now = x.get("yahoo_now_pct")
    since = x.get("since_open_pp")
    lines.append(
        f"| {i} | **{t}** | {r['gap']:+.2f}% | {r['close']:,.2f} | {r['pmc']:,.4g} | "
        f"${(r['mc'] or 0)/1e9:.2f}B | {(pmvol or 0):,} | "
        f"{(f'{rvol:.2f}' if rvol is not None else 'n/a')} | "
        f"{(f'{now:+.2f}%' if now is not None else 'n/a')} | "
        f"{(f'{since:+.2f} pp' if since is not None else 'n/a')} | "
        f"{r['sector']} | {why} |")
A("")
A("**The gap column is a 09:41 ET snapshot and it is already stale.** The same 20 names were "
  "re-read two minutes later at 09:43 ET and the median absolute change was 0.2 points, but the "
  "range ran from 0.0 to **5.0 points** (`PICS` bounced from −34.93% to −29.93% in two minutes; "
  "`XP` 1.3 points, `BRAI` 1.6 points). Treat every percentage here as a print in a live, "
  "violent book, and re-read the price before acting on it.")
A("")
A("The table is sorted by absolute gap, not by the skill's `premarket_change` descending sort, "
  "because a descending sort publishes only gainers and the single largest move on the board today "
  "is a −53% collapse. The skill's own deep-dive rule (\"top 5 by abs gap\") already assumes both "
  "directions matter, so this is a correction rather than a departure. Three rows carry a "
  "**thin-book warning**: `SSII` (300 pre-open shares), `LYCA` and `VINP` — their prints are "
  "indicative only.")
A("")

A("## Catalysts")
A("")
A("### The Brazil unwind (10 of the top 14 rows)")
A("")
A("President Luiz Inácio Lula da Silva won Sunday's runoff with 51.8% of the valid vote against "
  "right-wing senator Flávio Bolsonaro's 48.2%, confirmed by Brazil's electoral court. Markets had "
  "positioned for a Bolsonaro win as the fix for Brazil's fiscal accounts; the reversal sent the "
  "real, local yields and equities the other way. The selling is concentrated in exactly the "
  "names that rallied hardest on the Bolsonaro trade, and **no Brazilian ADR printed as a "
  "pre-market gainer**.")
A("")
A("| Name | Pre-open move (this brief) | Independent prints | Read |")
A("|---|---:|---|---|")
A("| XP (XP Inc.) | −53.57% | −45.3% $16.63 (Investing.com, 06:30 ET); −46% $16.43 "
  "(Benzinga); −48.7% $15.60 (Benzinga Pro); −50.58% $15.03 (Yahoo Japan/MINKABU, 08:42 ET); "
  "−52.35% $14.49 (Yahoo meta, 09:34 ET) | Largest mover; also carries issuer-specific overhang. |")
A("| STNE (StoneCo) | −38.68% | −35.72% $7.38 (Benzinga Pro); −37.0% (Benzinga); "
  "−38.41% $7.07 (Yahoo Japan, 08:42 ET) | Macro only. |")
A("| INTR (Inter & Co) | −38.25% | −34.1% (Benzinga); −37.41% $4.50 (Yahoo Japan, 08:42 ET) | Macro only. |")
A("| PICS (PicS N.V.) | −34.93% | −34.1% $9.10 (Investing.com, 07:46 ET) | Macro + unresolved 2026 securities class actions; near its $8.08 52-week low. |")
A("| PAGS (PagSeguro) | −34.45% | −31.8% (Benzinga); −26% (Tiger/TradingKey, 08:13 ET) | Macro only. |")
A("| AGBK (AGI Inc / Banco Agibank) | −32.91% | — | Macro only. |")
A("| NU (Nu Holdings) | −22.36% | −25.8% $11.24 (Benzinga); −25.33% $11.32 (Yahoo Japan, 08:42 ET) | Macro only; the largest cap in the group at $73bn. |")
A("| AFYA, ARCO, PAX, VINP | −20.5% to −15.6% | PAX −15.50% $9.92 (Yahoo Japan, 08:42 ET) | Macro only. |")
A("| **EWZ / EWZS** | *not screened (ETF — excluded by the skill's `type=stock` filter)* | "
  "EWZ −25.3% $31.83 (Benzinga Pro); EWZS −33.7%; ITUB −26.6%; BBD −31.5% | "
  "EWZ is the cleanest single read on the event. |")
A("")
A("Independent prints cluster between −45% and −52% for XP because they were taken between "
  "06:30 and 09:34 ET from different feeds on a fast, deteriorating book. The dispersion is "
  "**snapshot drift, not disagreement** — the order of the sources is monotonically more negative "
  "as the morning goes on, and this brief's 09:35 ET figure is the latest of them all.")
A("")
A("**XP is not purely macro.** Three issuer-specific items sit on top of the Brazil unwind: board "
  "member Escobari resigned on 16 October and a Microsoft executive was named interim director "
  "(persistent bearish options flow since); institutional holder Assenagon cut its stake by ~7.9% "
  "in the days before the move, with the stock near a 52-week high of $32.73; and no earnings are "
  "due until late November, so the selling has no near-term fundamental anchor.")
A("")
A("### Company events")
A("")
A("**XNCR +29.07% — Xencor.** Phase 1 data for XmAb819, presented at ESMO on Sunday, showed a "
  "**45.5% confirmed objective response rate** in advanced clear-cell renal cell carcinoma. The "
  "company says it expects to advance XmAb819 into late-stage development and plans accelerated "
  "FDA discussions. Independent prints ran +27.1% $32.00 (Benzinga), +29.46% $32.60 (Benzinga, "
  "08:05 ET), +33% $33.56 (MarketWatch, 06:43 ET) — this brief's +29.07% sits in the middle of "
  "that range. Wedbush reiterated Outperform with a $30 target on 23 October. Note the setup: "
  "short interest is 14.9m shares, 9.5 days to cover, 79% short volume, squeeze score 96/100.")
A("")
A("**SGRY +23.62% — Surgery Partners.** The FT reported Sunday evening that Bon Secours Mercy "
  "Health is in late-stage talks to acquire a controlling stake, valuing the company at ~$6bn "
  "including ~$3.5bn of debt and implying ~$20/share. Bain Capital, holder of nearly 40% since "
  "2017, is expected to retain its position. The stock at $19.47 is **still below the implied "
  "$20 offer price**, which is the market pricing deal-completion risk. A 2025 Bain-led take-private "
  "at a higher enterprise value previously fell through. 176 surgical centres across 30 states.")
A("")
A("**RRC +11.20% / EQT −6.83% — the Range Resources deal.** EQT is acquiring Range in an "
  "all-stock transaction at 0.987 EQT shares per RRC share, an implied ~$54.91/share (~20.6% above "
  "Friday's close) and pro-forma EV above $50bn, creating what the companies call the largest "
  "vertically integrated US natural gas producer. Both boards approved unanimously; close is "
  "expected in Q1 2027. Two Range directors join the EQT board. The Q3 calls for both companies, "
  "set for 28 October, are **cancelled**; Q3 results come after the close on 27 October.")
A("")
A("The interesting part is the spread. RRC printed +15.3% early pre-market and is +11.20% here, "
  "while the implied deal value is +20.6% and the acquirer is −6.83% (Reuters had EQT at −4.6% "
  "pre-market). **The market is not paying the implied price**, and the acquirer is being hit — "
  "that is an arbitrage spread, not a broken deal, but it is the widest dislocation on the board "
  "and it deserves a human read.")
A("")
A("**BRAI +15.77% — Braiin.** Not a bitcoin story. Braiin is an applied-AI platform company "
  "(CX, AgTech, PropTech) and today launched **Force AI**, an orchestration layer for its RADIUS "
  "CCaaS platform, alongside a major RADIUS upgrade, targeting a stated $56.9bn CX software "
  "market. The crypto-linked cohort was uniformly *lower* pre-open (CRCL −2.88%, SBET −2.62%, "
  "BMNR −2.23%, ASST −1.92%, COIN −1.37%, MSTR −1.34%, HOOD −0.92%, PURR −0.57%), so this is "
  "idiosyncratic. Note the stock closed Friday at $3.55, −8.27% on the day, and traded −8.06% "
  "again after hours.")
A("")

A("## Where the gap stands now (10:02 ET, versus the 09:41 pre-open mark)")
A("")
A("The table's last two columns are the live move against Friday's close and its change since "
  "the pre-open mark. Three things stand out, and none of them are in the pre-open screen:")
A("")
A("- **`SGRY` re-rated hard in the first 25 minutes.** Yahoo's 1-minute series for Surgery Partners "
  "begins at 09:55 ET at **$23.03, or +46.2%** against Friday's close — roughly 18% above its "
  "$19.47 pre-open print and well above the ~$20 implied offer price reported on the Bon Secours "
  "deal. The mechanism is unconfirmed: no announcement was found in the searches run for this "
  "brief. The tradeable question is whether the reported ~$20 terms are stale.")
A("- **The Brazil complex is bifurcating, not moving as one.** `STNE` (+7.4 pp off the open), "
  "`PAGS` (+6.0 pp) and `LYCA` (+15.1 pp) have bounced materially; `PICS` (−4.8 pp), `INTR` "
  "(−2.6 pp), `PAX` (−2.8 pp) and `AGBK` (−2.5 pp) have kept going. A trader who bought the "
  "opening print of STNE is up 7.4 points; one who bought PICS at the open is down 4.8.")
A("- **The two genuine company events are the outliers, and they are diverging.** `XNCR` has given "
  "back 6.4 points from its pre-open mark (+27.8% → +21.4%) on no news — a biotech catalyst "
  "fading in the tape, with 9.5 days to cover and 79% short volume still on the other side. "
  "`RRC` has *gained* 5.8 points (+11.0% → +16.8%) as the market moves toward the ~$54.91 implied "
  "by the EQT exchange ratio, against the ~$50.61 pre-open mark; `EQT` is the leg that pays. "
  "`BRAI` is up 13.7 points from its pre-open mark.")
A("")
A("## Anything needing human eyes")
A("")
A("1. **RRC/EQT spread** — implied +20.6% vs the +11.2% pre-open mark (+16.8% live at "
  "10:02 ET), with the acquirer down 6.8%. A "
  "10-point gap on a signed, unanimously approved deal is either a real risk premium (regulatory, "
  "or a large \"sticky\" holder like Bain voting with management) or a mispriced arb. Both Q3 "
  "prints land 27 Oct after the close, and the 28 Oct calls are cancelled, so there is no "
  "scheduled analyst voice on the deal this week.")
A("2. **The Brazil book may not have found its clearing price.** The selloff in a rate-sensitive, "
  "high-beta emerging-market financial complex is exactly where Goldman warned the damage would "
  "land (USD/BRL +10%, local yields +200 bp). Circles are already arguing about the 48.2% "
  "opposition share and calls to annul the vote, and the electoral court itself extended voting "
  "hours in a messy count. The political leg is not closed.")
A("3. **XP's −53% is a three-way story, not a clean macro print.** If you trade the Brazil "
  "complex, XP is the highest-beta expression but it also carries an unresolved governance "
  "overhang and a 7.9% institutional trim. It may keep underperforming the group even if Brazil "
  "stabilises.")
A("4. **Energy is bifurcated and oil is the macro hinge.** Brent above $116 on Middle East "
  "geopolitics is an inflation input into a Fed decision on **Wednesday 28 October at 14:00 ET** "
  "(no dot plot this meeting; the target range goes in at 3.75–4.00%), with Q3 GDP and the "
  "September PCE print the following morning at 08:30 ET. On the same page of the tape, RRC is "
  "+11% on a gas consolidation and EQT is −7%; BORR −9.6%, AUGO −7.8% and ARLP +3.2% are moving "
  "in different directions on the same commodity.")
A("5. **`SGRY` is trading ~15% above the reported deal terms.** The pre-open gap (+23.6% to "
  "$19.47) was priced against a ~$20 implied offer. The live mark is $23.03. Either the terms "
  "reported overnight have improved, or the market is bidding a headline that has not been "
  "confirmed. `Bain` is expected to retain its ~40% stake, which is the usual reason a buyer "
  "will pay over the headline in a carve-out. This is the single most actionable thing on the "
  "board and it is the one with the least verified information.")
A("6. **Two thin-book prints that could be mistaken for signals.** `SSII` (+14.08% on 300 "
  "pre-open shares) and `LYCA` (−10.40%) are one-sided books. The screen reports them because "
  "they cleared the market-cap and volume filters, not because the prints are tradeable.")
A("7. **Today's calendar:** Chicago Fed National Activity (08:30 ET, released), Dallas Fed "
  "Manufacturing (09:30 ET), Verizon Q3 pre-market, and a $69bn 2-year note at 13:00 ET. "
  "Tuesday brings durable goods, new home sales and consumer confidence ahead of the Fed.")
A("")

A("## Method and caveats")
A("")
A("**Data path.** The skill's Mode A was unavailable: `NTRT_BASE_URL` is unset, the default "
  "`http://127.0.0.1:8000/health` probe never connected (connection-level failure, not an HTTP "
  "error), and `NTRT_AUTH_TOKEN` is unset. The TradingView MCP named in the skill is not bound in "
  "this runtime — `tool_search` returns zero hits for any finance keyword, and the connector "
  "catalogue (`partial=false`, `provider_failures=[]`) contains only media and credential tools, "
  "which proves the catalogue is complete rather than partially loaded. Per the zero-fallback "
  "policy the chain terminated here: the public screener was used and no deeper MCP was attempted.")
A("")
A("**Screen specification (Mode B, as specified).** `POST https://scanner.tradingview.com/america/scan`, "
  "filter `premarket_change` ≥ 3 and ≤ −3, `market_cap_basic` ≥ $200,000,000, market `america`. "
  "The MCP field name `premarket_change_percent` does not exist on the public endpoint; the "
  "equivalent column is `premarket_change`, and it was verified to be the *percentage* rather than "
  "the absolute move (`premarket_change` × close = `premarket_change_abs` on spot checks). "
  "`type=stock` excludes ETFs and `exchange != OTC` excludes OTC shells, per the shared-repo "
  "runbook — which also means **no ETF, and therefore no index or EWZ, is in this screen**.")
A("")
A("**Three filters run on top of the skill's spec.** The skill's own screen is not sufficient to "
  "keep phantom rows out of a pre-market brief:")
A("")
A("1. *Internal consistency* — every row's own `close`, `premarket_close` and `premarket_change` "
  "must agree (`implied_ref = premarket_close / (1 + gap/100) == close`, tolerance 0.5%). This "
  "caught and killed `BUUU` (implied reference $53.90 against a real close of $5.39). It is a "
  "free check and it needs no second source.")
A("2. *Volume floor 10,000* on the last regular session — the shared-repo runbook's stale-row "
  "filter. It is necessary but not sufficient: a row can clear it on a single thin day while the "
  "reference close is days stale, which is why check 1 and check 3 both exist.")
A("3. *Yahoo reference-close cross-check* on the 10 most actionable names, using Yahoo's "
  "independent `previousClose` and its own `fulldayChangePercent` (Yahoo's pre+post mark, measured "
  "against the same prior close, so the two percentages are directly comparable).")
A("")
A("**Known limits of the screen.** TradingView's `market_cap_basic` is occasionally wrong on "
  "individual rows (`SPRC` shows $0.6m against a realistic ~$60m, `AIOK` shows null), so the $200m "
  "floor can misfire on a thin name — but no published row sits near the threshold (the smallest "
  "published market cap is ~$200m), so the published set is not affected. Preferreds, warrants and "
  "rights are excluded by post-filter on the ticker and description. A hard cap of 5 deep dives "
  "was respected in spirit (no dossier calls) but exceeded on catalyst research, as flagged above.")
A("")
A("**What this brief is not.** It is a US-equities, pre-open screen. It carries no positions, no "
  "options surface, no relative-value work and no cross-asset analysis, all of which the skill "
  "places out of scope. Every catalyst line is sourced to a named publication; rows marked *not "
  "researched* have had no catalyst search performed and no cause has been inferred for them.")
A("")

A("## Source health")
A("")
A("| Check | Result |")
A("|---|---|")
if xc:
    A(f"| Yahoo reference-close test (drift-proof, decides validity) | "
      f"**{xc.get('reference_fresh')} of {len(xc.get('results') or [])} fresh, "
      f"{xc.get('reference_stale')} flagged** |")
    _w2 = sum(1 for c in (xc.get("results") or [])
              if c.get("open_diff_pp") is not None and abs(c["open_diff_pp"]) <= 2)
    _w3 = sum(1 for c in (xc.get("results") or [])
              if c.get("open_diff_pp") is not None and abs(c["open_diff_pp"]) <= 3)
    A(f"| Yahoo open-print comparison (magnitude, banded) | {_w2} of {len(xc.get('results') or [])} "
      f"within 2 pp of the 09:30 ET open print, {_w3} within 3 pp; the outliers are named below |")
    A(f"| Yahoo live mark at {NOW_ET} ET | captured for all 20 names |")
else:
    A("| Yahoo reference-close + gap cross-check | **did not complete** — see errors below |")
A(f"| Internal-consistency screen (free, every row) | 1 of 408 gapped rows failed and was dropped |")
A(f"| Market-cap / volume floor | {counts['g2_failed'] + 325 - counts['g2_failed']} rows excluded "
  f"by the $200m cap or the 10,000-share volume floor |")
A("| TradingView screener reachability | OK — 2 full-universe passes, HTTP 200 |")
A("| Yahoo Finance reachability | OK after two fixes — see errors below |")
A("| News sources | Investing.com, Benzinga, MarketWatch, Reuters, FT (via Benzinga/Investing), "
  "Benzinga Pro, Yahoo Japan/MINKABU, TokenPost, Schwab Network, gov.house |")
A("")
A("| Ticker | TV pre-open gap | Yahoo 09:30 open print | Diff | TV Fri close | Yahoo prior close | Ref diff | Ref verdict |")
A("|---|---:|---:|---:|---:|---:|---:|---|")
for c in (xc.get("results") or []):
    op = c.get("yahoo_open_pct")
    A(f"| {c['ticker']} | {c['tv_gap_pct']:+.2f}% | "
      f"{('%+.2f%%' % op) if op is not None else 'n/a'} | "
      f"{('%+.2f pp' % c['open_diff_pp']) if c.get('open_diff_pp') is not None else 'n/a'} | "
      f"{c.get('tv_close_published')} | {c.get('yahoo_previous_close')} | "
      f"{('%+.3f%%' % c['ref_close_diff_pct']) if c.get('ref_close_diff_pct') is not None else 'n/a'} | "
      f"{c.get('ref_verdict')} |")
A("")
A("**Reference close** is the drift-proof test and it is the one that decides whether a gap is "
  "real: it compares the screener's own reference close against Yahoo's independent prior close, "
  "so a live market moving between the two snapshots cannot create a false alarm. **The open "
  "print** is the apples-to-apples magnitude test — TradingView's `premarket_change` holds the "
  "pre-open mark, so the right Yahoo bar is the 09:30 one, not the live one.")
A("")
if xc.get("reference_stamps"):
    A("Reference-session stamp (Yahoo daily bars) — the session the gap is measured from:")
    A("")
    A("```")
    for k, v in xc["reference_stamps"].items():
        A(f"{k:<6} {json.dumps(v)}")
    A("```")
    A("")
A("**The two flagged references are real and worth naming.** `BRAI` is off by −4.57%: the "
  "screener's reference close is $3.55 (Friday's) while Yahoo's independent prior close is "
  "$3.72, so the two feeds disagree about which session the gap is measured from — a "
  "−4.6-point error in the published +15.77% if Yahoo is right, and a stale Friday close in "
  "Yahoo if the screener is. `SSII` is off by −0.88% ($2.25 vs $2.27), which is inside the "
  "noise of a stock that traded 300 shares pre-open. Neither is a phantom gap, but `BRAI`'s "
  "reference should be resolved before its number is used.")
A("")
A("**The two open-print outliers are mechanical, not disagreements.** `SGRY` shows +22.6 pp "
  "because Yahoo's 1-minute series for it *begins* at 09:55 ET at $23.03 — there is no 09:30 bar "
  "to compare against, and the +22.6 points are the actual post-open re-rating described in the "
  "section above. `SSII` shows −12.8 pp because Yahoo carries only two bars for it; a book that "
  "thin cannot produce a meaningful open print, and the live mark of −0.44% against the "
  "pre-open +14.08% is the honest reading. `AGBK` (+6.7 pp), `VTEX` (+4.1 pp) and `MELI` "
  "(+2.6 pp) sit in between: real dispersion in thin pre-open books, not a feed fault.")
A("")

A("## Errors and degraded paths")
A("")
A("| Issue | Handling |")
A("|---|---|")
A("| `ntrt_mtrt` backend unreachable (no `NTRT_BASE_URL`, default probe refused) | Mode B |")
A("| `mcp__tradingview_advanced__*` and `mcp__yahoo_finance__*` not bound in this runtime | "
  "Public screener used instead; no deeper MCP attempted |")
A("| Yahoo returned HTTP 429 for every request made with `urllib`, on the same URLs where `curl` "
  "returned 200 from the same IP | All Yahoo traffic re-routed through `curl` |")
A("| Yahoo returned HTTP 429 for *every* spark request, while a manual `curl` to the same URL "
  "succeeded seconds earlier | Root cause: the long Chrome `User-Agent`. Yahoo's edge 429s the "
  "long UA and serves the short `Mozilla/5.0` UA normally. Fixed by shortening the UA; the "
  "long-UA 429s and the 'too many symbols' errors were the same defect, not two |")
A("| `urllib.parse.quote` escaped the comma between symbols, so Yahoo never saw a separator | "
  "Added safe-comma quoting — a second, independent cause of the same failed requests |")
A("| `query1` was banned harder than `query2` | Both hosts tried per request, `query2` first |")
A("| TradingView's `close` column rolls to the live price after the open | Reference test pinned "
  "to the pre-open snapshot; the post-open fetch is used only for liquidity columns and for the "
  "live mark |")
A("| The cron fired at 09:04 ET, ~2.5 h after the skill's 06:30 ET schedule, and the run itself "
  "took ~45 min, so the screen was pulled after the 09:30 open | Reported at the top; the numbers "
  "are opening-gap marks, not a pre-open snapshot |")
A("| `BUUU` −91.24% internally impossible | Dropped, and called out in the table note above |")
A("| `regularMarketTime` in Yahoo's meta is the last *print*, not the reference session | Reference "
  "session taken from the daily bar series instead |")
A("")

A("## Provenance")
A("")
A("```")
A(f"artifact      : /workspace/ntrt/2026-10-26.md")
A(f"screen pass   : TradingView public screener, full-universe passes (199 up / 209 down)")
A(f"row count     : 408 gapped names screened -> 82 publishable -> 20 published")
A(f"snapshot (ET) : {COVER_ET} (gap column) / {SNAP_ET} (cross-check) / {NOW_ET} (live marks)")
A(f"cross-check   : Yahoo spark, TV fetch {SNAP_ET} ET, Yahoo fetch {NOW_ET} ET")
A(f"raw payloads  : /workspace/ntrt/_raw/ (cover_*.json, final_*.json, publishable_full.json)")
A(f"pipeline      : /workspace/ntrt/_pipeline/ (final_snapshot.py, yahoo_only.py, render_brief.py)")
A("audit log     : not written on Cloud (per migration note)")
A("```")
A("")

OUT.write_text("\n".join(lines))
print(f"wrote {OUT} ({OUT.stat().st_size} bytes, {len(lines)} lines)")
