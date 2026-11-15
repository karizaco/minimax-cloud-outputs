---
date: 2026-11-09
market: asx
slot: open
producer: grok-bot/asx-stocks-in-play
contract: intl-stocks-in-play-v1
source: Grok Bot box digest (Fundamental asx stocks-in-play routine)
generated_at: 2026-11-09T20:00:00+07:00
status: degraded
---

Provenance: Fundamental digest at /home/box/asx-in-play/2026-11-09-open.md; built at 2026-11-09T20:00:00+07:00; covered session open.

**Deviations:** digest reports a skipped section

# ASX stocks in play — 2026-11-09 open
Run ~10:40 AEDT (06:40 Asia/Bangkok). ASX cash open (not a holiday). Floors: price ≥ A$0.05; mcap ≥ A$30m or turnover ≥ A$150k; sort = tier then A$ turnover desc. Tags: TV = TradingView MCP screener/batch (early-session; RVol = relative_volume_10d_calc, many large caps still low as session is young); MI = Market Index HTTP top-gainers/losers/halts; ANN = MarkitDigital PS announcements (UTC → AEDT +11); WEB = web search for result/strategy figures. Prior file 2026-11-06-open.md had no overnight_carry.

Market colour: no index level pulled this run (unverified, omitted).

## Soft-A
| Ticker | Last | Chg | RVol | Mcap | Turnover | Why |
|---|---|---|---|---|---|---|
| DNL | 3.54 TV | **−7.33%** TV (gap −7.07%) | 0.22× TV | A$6.69B TV | A$4.29m TV | 08:29 PS FY26 results (Appendix 4E/presentation, ANN). WEB: FY26 underlying explosives EBIT A$485.1m (+12%), FY27 EBIT guide A$515–555m (Quartr summary). Sold off despite growth/guide → Soft-A (soft RVol). |
| VNT | 5.29 MI | **−7.68%** MI | n/a | A$4.31B MI | A$2.21m MI | 08:13 PS strategy/simplification/FY26 outlook (ANN). WEB: ≥A$60m annualised savings by Dec 2027, ~A$30m one-off costs, 3 sectors from 1 Dec; 2H FY26 revenue expected below pcp (Telecom/Energy deferrals); FY26 NPATA +7–10% growth kept. |
| EOS | 7.27 TV | **+3.56%** TV (gap +5.56%) | 0.27× TV | A$1.61B TV | A$5.50m TV | 08:22 PS: new Middle East counter-drone order US$16m (ANN). Gap clears 4%; RVol soft. |
| ANZ | 40.11 TV | −0.57% TV (gap +0.72%) | 0.11× TV | A$121.6B TV | A$20.8m TV | 07:30 PS FY26 result + dividend (ANN); figures not pulled this run (unverified). Muted tape → Soft-A low priority. |
| PLA | 0.38 TV | 0.00% TV (gap −5.26%) | 2.45× TV | A$354m TV | A$169k TV | 10:36 PS: A$50m equity raise + DFC financing term sheet after trading halt (ANN). Dilutive; gap −5.3% then back to flat; just over floor. |

## TECH_WATCH
- PDN: 7.965 TV, +6.77% (gap +3.89%), RVol 0.13× TV, mcap A$3.21B, A$3.39m TV. No PS in ANN → technical only.

## Tier B
- NXT 10.24 −1.54% A$5.50m TV (gap −1.9%): GMG disclosed 9.9% NEXTDC stake (PS 09:17); prior Goodman/Digital Realty raid ongoing → BUYOUT_NEAR context, file only. GMG 27.93 +0.32% A$4.85m.
- AMX 0.365 TV +8.96%, RVol ~253× TV (stale-looking), mcap A$28.5m, A$3.52m TV: 05-Nov PS "Review of Strategic Options". Sub-A$30m mcap but passes turnover; no same-session PS.
- IMM 0.026 MI +23.8% A$424k MI mcap A$38m: 08:29 PS IMP761 late-breaking abstract at ACR. Thin liquidity.
- NMR 0.047 TV +20.5% A$46k (mcap A$46m): JV with Citigold (PS 10:29 AEDT). CTO +10.7% A$19k same JV. Below turnover floor.
- LYC +3.74% A$4.97m, MIN +3.65% A$4.04m, GMD +3.69% A$5.60m, PLS +3.18% A$7.37m, SCG −2.49% A$5.90m: below move thresholds.
- Large caps (BHP, CBA, NAB, WBC, TLS, CSL) flat/low RVol — no PS, file only.

## Tier C
| Ticker | Note |
|---|---|
| SSM | Halted since 4:37pm 06/11 (MI halts list; may be stale vs ANN). 09:04 PS: acquire Programmed (Persol) for A$975m (EV A$1,092m), A$475m equity raise at A$2.03; completion ~1 Mar 2027 (WEB, stockwirex). Last 2.20 TV (−1.35%, A$2.98m) — resumption status not verified. Watch reopen/bookbuild price vs A$2.03. |
| SET | Placement + entitlement offer after halt (LIC-type, Solaris Equity Income Plus) — likely fund wrapper; file only. |
| BB1, KNI, WCE, CTN, MEL | Trading halts on MI list; small, not chatted. |
| NS1 | Voluntary administration + suspension (PS overnight). |

## Other PS noted (file only)
IGO Nova mining concluded, beats guidance (A$727k, +1.2%); VEA 2026 strategy update (−0.2%); CDA acquisition (−0.4%); OZM Mulgabbie resource 294koz (−4.3%, A$20k); PHO Gasaat scoping study +6.9% A$61k.

## Market Index browser pages
Not read in this run (headless run had no desktop browser). Highest-turnover and unusual-volume were not browsed; TV screener by Value.Traded (263 rows ≥ A$150k) used as stand-in.

## ⚠️ Skipped
⚠️ Skipped: Market Index unusual-volume returned “No results available” on two browser loads (header correctly dated prior close 6 Nov). Highest-turnover and Stockhead recovered in parent browser pass; see addendum.

## Source health
| Source | Status | Notes |
|--------|--------|-------|
| TradingView MCP run_screener (australia, Value.Traded) | ok | 40 rows of 263 |
| TradingView MCP get_symbol_data_batch (21 syms) | ok | no missing |
| MarkitDigital PS announcements (pages 0–3) | ok | |
| Market Index top-gainers / top-losers / trading-halts (HTTP) | ok | halts list may lag |
| Market Index highest-turnover / unusual-volume | skipped | browser-only; no browser in run |
| Stockhead RSS | blocked | HTML page not feed; browser unavailable |
| Web search (DNL/VNT/SSM figures) | ok | secondary sites, treat as unverified vs ASX PDFs |

## overnight_carry
SSM — Programmed deal/A$475m raise at A$2.03: check reopen and price vs raise at next slot. PLA — A$50m raise terms.

## Required browser coverage addendum — 06:42 Asia/Bangkok
- Market Index highest-turnover: browser OK; Nov 9 delayed table rendered. ANZ A$40.13, −0.52%, A$21.23m turnover. Other top rows include BHP A$32.24m (+1.91%), MQG A$16.42m (−0.12%), CBA A$15.14m (−0.28%). Original slot figures above retained, not mixed with later quotes.
- Market Index unusual-volume: prior-close header 6/11/26 AEDT, expected Friday context, but “No results available” after two loads. No volume rows available.
- Stockhead: browser homepage recovered after RSS failure; Rise and Shine Nov 9 visible, no Nov 9 market wrap yet. Prior wrap Nov 6. Homepage headlines alone do not promote additional candidates without liquidity/catalyst validation.
- SSM Market Index company page: HALTED badge, volume 0 and turnover A$0, displayed A$2.20. No reopen time. Treat A$2.20 as displayed reference, not evidence of trading or resumption.
- Browser traffic used our computer's network because the user's computer was offline.

| Browser source | Final status | Detail |
|---|---|---|
| Market Index highest-turnover | browser | Current Nov 9 table rendered |
| Market Index unusual-volume | skipped | Prior-close date correct; empty results twice |
| Stockhead homepage | browser | Recovered after RSS failure |
| Market Index SSM company | browser | HALTED badge; no reopening confirmed |
