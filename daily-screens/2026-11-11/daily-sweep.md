---
artifact: daily-sweep
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-11 18:30 ET"
cron_date: "2026-11-11"
screen_data_date: "2026-11-10 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-11 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-11 (settled 16:00 ET close from the TradingView scanner; the Cboe VIX pair is quoted 2026-11-11T16:15:01)"
regime: {size_cut_pct: 0, uncertainty: false, late_cycle: false, index_below_20sma: false, breadth_pct_spx: 63.73}
coverage: "10/10 T+1 branches complete (rows_kept == rows_passing on every branch); 4/4 fresh TV branches complete (totalCount asserted)"
---

# Daily Screener Sweep — Wednesday, 11 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-11's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window, CANSLIM growth, the Hernandez theme funnel) stay on shibui's newest ingested session, **2026-11-10**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **The book is 1125 candidates and the Tier-A list is 4 names** — AAON, LQDA, QNT, ZETA. The FRESH book contributes **319 names** on today's settled bar, **109 of which the T+1 book never found**. That is the payoff of the dual book — those are names that only exist if today's own bar is read.
- **All 4 Tier-A names are EXTENDED — 0 fresh / 4 extended.** The convergence screens found the day's winners; the extension label is what says they have already run.
- **Caveat that changes how to read it**: the tape was strong but the *index* lagged it. Breadth 63.73% above the 20-DMA with advance/decline **675 / 425 / 14** (ratio 1.59), yet **QQQ sits -3.99% below its own 50-DMA** while RSP is +3.60% above it.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (breadth 63.73% is far above the 40% trigger) |
| `uncertainty` | **false** (VIX 17.49 / VIX3M 19.24, ratio 0.9090) |
| `late_cycle` | **false** (the extreme is RSP at +3.60% above its 50-DMA) |
| `index_below_20sma` | **false** (3 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+3.73 pp — MATCHED** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-11** — the cron day's settled bar | A_tv_breakout_4pct 134 · B_tv_ep9m 198 · D_tv_gap_10pct 7 · TV_volume_breakout 56 | 319 |
| **T+1** (cross-check) | **2026-11-10** — shibui's newest ingested session | A_stockbee_4pct 60 · B_stockbee_ep9m 204 · K_stockbee_anticipation 309 · C_qullamaggie_rs 79 · D_qullamaggie_ep 2 · E_qullamaggie_5d_gainers 16 · F_qullamaggie_5d_losers 10 · G_peoplewish 361 · jeff_sun_canslim 69 · H_hernandez_theme 153 | 1016 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 210 |
| `t1` | context screens only | 806 |
| `fresh` | trigger screens only | 109 |

## Screen coverage — the assertion that makes the book publishable

Every T+1 branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on all 10 branches.**

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 60 | 60 | complete · **cap fingerprint — independently verified, see caveats** |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 204 | 204 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 309 | 309 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 79 | 79 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 2 | 2 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 16 | 16 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 10 | 10 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 361 | 361 | complete |
| `jeff_sun_canslim` | Jeff Sun — CANSLIM growth + strength (T+1) | 69 | 69 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 153 | 153 | complete |

Total screened rows **1263** across the 10 T+1 branches, plus **395** across the 4 fresh TV branches → **1125 distinct candidates** after dedup and merge.

## Tier-A — ≥ 3 distinct stylists (4 names)

| Symbol | Stylists | Origins | Source | Close 11-11 | **Chg 11-11** | ADR% | ATR% | RSI | Val gate | Ext |
|---|---|---|---|---|---|---|---|---|---|---|
| **AAON** | 4 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish, jeff_sun_canslim | `t1` | 76.33 | **+1.76%** | 7.33 | 7.77 | 54.5 | fail | EXTENDED |
| **LQDA** | 5 | A_stockbee_4pct, A_tv_breakout_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme, TV_volume_breakout | `fresh+t1` | 55.21 | **+7.41%** | 7.91 | 7.28 | 65.8 | pass | EXTENDED |
| **QNT** | 3 | A_stockbee_4pct, E_qullamaggie_5d_gainers, G_peoplewish | `t1` | 40.57 | **-5.65%** | 9.02 | 8.83 | 52.9 | fail | EXTENDED |
| **ZETA** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish, TV_volume_breakout | `fresh+t1` | 37.74 | **+7.61%** | 5.55 | 5.16 | 67.6 | fail | EXTENDED |

### What Tier-A is saying

- **AAON** (4 stylists) — A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish, jeff_sun_canslim. It closed **+1.76%** at 76.33, carries no fresh trigger — its screen metrics are T+1. It fails the valuation gate on free_cash_flow_yield, and it sits at the 92.0 percentile of the $10B+ sub-universe for distance above its own 20-DMA.
- **LQDA** (5 stylists) — A_stockbee_4pct, A_tv_breakout_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme, TV_volume_breakout. It closed **+7.41%** at 55.21, and hits the fresh trigger book as well as the T+1 context book. It passes the valuation gate, and it sits at the 99.8 percentile of the $10B+ sub-universe for distance above its own 20-DMA.
- **QNT** (3 stylists) — A_stockbee_4pct, E_qullamaggie_5d_gainers, G_peoplewish. It closed **-5.65%** at 40.57, carries no fresh trigger — its screen metrics are T+1. It fails the valuation gate on free_cash_flow_yield, and it sits at the 96.2 percentile of the $10B+ sub-universe for distance above its own 20-DMA.
- **ZETA** (3 stylists) — A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish, TV_volume_breakout. It closed **+7.61%** at 37.74, and hits the fresh trigger book as well as the T+1 context book. It fails the valuation gate on trailing_pe, operating_pe, trailing_revenue_peg, and it sits at the 98.2 percentile of the $10B+ sub-universe for distance above its own 20-DMA.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 4 extended.** Across the whole book, 556 of 1125 names trip an extension rule. Nothing is dropped for being extended — the label is published next to every candidate row, and the full split is in `tier-a-fresh.md` and `tier-a-extended.md`.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | Rule tripped |
|---|---|---|---|---|
| AAON | 7.77 | 96.0 | 9.04% | ATR% > 5.0 (a normal large cap is 1.5-3%) (7.77) |
| LQDA | 7.28 | 95.0 | 28.31% | ATR% > 5.0 (a normal large cap is 1.5-3%) (7.28); > 15% above its 20-DMA (28.31) |
| QNT | 8.83 | 97.9 | 11.25% | ATR% > 5.0 (a normal large cap is 1.5-3%) (8.83) |
| ZETA | 5.16 | 86.3 | 14.99% | ATR% > 5.0 (a normal large cap is 1.5-3%) (5.16) |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close 11-11 | **Chg 11-11** | RVOL 10d | ATR% | RSI | ADR% | Val gate |
|---|---|---|---|---|---|---|---|---|---|---|
| **AAON** | 4 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish, jeff_sun_canslim | `t1` | 76.33 | **+1.76%** | 0.77 | 7.77 | 54.5 | 7.33 | fail |
| **BW** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, TV_volume_breakout | `fresh+t1` | 4.84 | **+8.04%** | 1.91 | 9.84 | 52.6 | 8.73 | fail |
| **CHTR** | 2 | A_stockbee_4pct, C_qullamaggie_rs | `t1` | 136.31 | **+1.68%** | 0.93 | 5.04 | 67.4 | 4.87 | fail |
| **GDYN** | 2 | A_stockbee_4pct, C_qullamaggie_rs | `t1` | 13.83 | **-1.64%** | 0.45 | 4.71 | 77.9 | 5.77 | fail |
| **HROW** | 2 | A_stockbee_4pct, jeff_sun_canslim | `t1` | 29.37 | **-3.26%** | 1.25 | 6.10 | 50.4 | 5.41 | fail |
| **LQDA** | 5 | A_stockbee_4pct, A_tv_breakout_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme, TV_volume_breakout | `fresh+t1` | 55.21 | **+7.41%** | 1.54 | 7.28 | 65.8 | 7.91 | pass |
| **LUMN** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 4.45 | **-5.52%** | 1.07 | 7.96 | 42.8 | 7.53 | fail |
| **MARA** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 7.66 | **+4.36%** | 1.17 | 9.03 | 47.9 | 8.78 | fail |
| **PEPG** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, D_tv_gap_10pct | `fresh+t1` | 5.26 | **+14.10%** | 1.38 | 10.45 | 83.6 | 10.91 | fail |
| **QNT** | 3 | A_stockbee_4pct, E_qullamaggie_5d_gainers, G_peoplewish | `t1` | 40.57 | **-5.65%** | 1.14 | 8.83 | 52.9 | 9.02 | fail |
| **TNGX** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, G_peoplewish | `fresh+t1` | 25.73 | **+5.88%** | 1.17 | 7.61 | 58.4 | 7.97 | fail |
| **ZETA** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish, TV_volume_breakout | `fresh+t1` | 37.74 | **+7.61%** | 1.65 | 5.16 | 67.6 | 5.55 | fail |

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 351 | no red flag, and earnings data present |
| `fail` | 647 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 127 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-11

| Metric | Value |
|---|---|
| Universe | 1114 names (NYSE/NASDAQ/AMEX, type stock+dr, market_cap_basic > $10B) |
| % above 20 / 50 / 200-DMA | **63.73%** / 55.48% / 50.81% |
| Advance / decline / unchanged | **675 / 425 / 14** (ratio 1.59) |
| Median name | +0.25% |
| VIX / VIX3M | **VIX 17.49 / VIX3M 19.24** (prior 19.46 / 20.64) |
| SPY / RSP / QQQ / QQQE / IWM | 759.81 (+1.32%) / 222.65 (+0.80%) / 690.38 (+2.31%) / 117.70 (+2.24%) / 283.09 (+0.89%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| CRWV | CoreWeave, Inc. | 60.77 | **+24.71%** |
| NBIS | Nebius Group N.V. | 154.69 | **+15.44%** |
| SNDK | Sandisk Corporation | 977.69 | **+13.69%** |
| BE | Bloom Energy Corporation | 209.47 | **+12.97%** |
| ARM | Arm Holdings plc | 203.36 | **+12.05%** |
| MU | Micron Technology, Inc. | 811.30 | **+11.89%** |
| DELL | Dell Technologies Inc. | 373.68 | **+11.75%** |
| ENTG | Entegris, Inc. | 154.22 | **+11.29%** |
| LITE | Lumentum Holdings Inc. | 648.06 | **+10.67%** |
| LSCC | Lattice Semiconductor Corporation | 122.77 | **+10.36%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| SMMT | Summit Therapeutics Inc. | 16.64 | -6.67% |
| RVMD | Revolution Medicines, Inc. | 180.70 | -6.40% |
| QNT | Quantinuum Inc. | 40.57 | -5.65% |
| NTES | NetEase, Inc. | 122.13 | -4.61% |
| HMC | Honda Motor Company, Ltd. | 33.35 | -4.39% |
| EQX | Equinox Gold Corp. | 10.80 | -3.83% |
| SE | Sea Limited | 73.99 | -3.66% |
| STLA | Stellantis N.V. | 4.11 | -3.52% |
| ABNB | Airbnb, Inc. | 181.13 | -3.09% |
| PBR.A | Petroleo Brasileiro S.A. Petrobras | 15.70 | -3.09% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (16):** the names up 25%+ over five sessions, where a mean-reversion short is the mechanical outcome of the screen.

| Symbol | m1 (5d) | ADR% | Close 11-11 | Chg 11-11 |
|---|---|---|---|---|
| ACHC | 30.45 | 5.42 | 38.80 | +0.41% |
| APP | 61.10 | 5.36 | 404.77 | +2.34% |
| AUGO | 26.83 | 6.38 | 81.40 | +0.11% |
| FLY | 39.29 | 8.62 | 26.61 | +12.28% |
| FUN | 36.19 | 8.60 | 11.10 | +9.25% |
| JBLU | 25.79 | 9.07 | 4.02 | +0.50% |
| KD | 33.46 | 6.03 | 17.13 | -0.81% |
| MGNI | 27.66 | 4.80 | 29.21 | +2.42% |
| OUST | 31.88 | 7.87 | 38.22 | +0.00% |
| QNT | 32.02 | 9.02 | 40.57 | -5.65% |
| RIOT | 28.96 | 9.30 | 18.28 | +1.11% |
| RYTM | 31.83 | 4.85 | 112.16 | -1.57% |
| TMDX | 35.05 | 6.12 | 92.01 | +1.17% |
| UI | 25.76 | 4.55 | 679.42 | -0.95% |
| WRBY | 36.28 | 7.16 | 30.15 | +0.84% |
| XNCR | 28.56 | 6.56 | 39.97 | +1.47% |

**Long / mean-reversion candidates (10):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close 11-11 | Chg 11-11 |
|---|---|---|---|---|
| AXON | -27.37 | 5.44 | 315.42 | +4.26% |
| CAI | -25.63 | 6.64 | 24.49 | +0.25% |
| CLMT | -26.24 | 6.48 | 35.89 | +2.81% |
| DOX | -33.59 | 3.42 | 43.12 | +4.00% |
| FIS | -27.39 | 3.72 | 30.21 | +6.71% |
| HIMS | -25.56 | 8.20 | 20.81 | +8.78% |
| IONS | -30.26 | 4.78 | 28.33 | +0.50% |
| IRTC | -31.90 | 5.43 | 88.68 | +3.04% |
| NRIX | -38.50 | 6.11 | 16.33 | +2.83% |
| TE | -26.86 | 11.21 | 2.13 | +2.90% |

## Per-stylist books

| Stylist | File | Rows |
|---|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` | 685 |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` | 108 |
| Jeff Sun, CFTe | `jeff-sun.md` | 124 |
| Ariel Hernandez | `ariel-hernandez.md` | 69 |
| peoplewish — Alec Riffle | `peoplewish.md` | 361 |

`ariel-hernandez.md` carries the theme → group → leaders funnel: the top themes by composite 1M/3M/6M relative strength (**Health Services** 49.9 · **Health Technology** 42.7 · **Commercial Services** 37.2) mapped to their GICS buckets via shibui's `general_info`, with the leaders inside those buckets (21-session return > 15%, market cap > $2B) — 153 names: Health Care 79 · Industrials 74. The GICS mapping comes from shibui's `general_info`, not from a hand-maintained table.

## Method, source health & caveats

| Source | Used for | Status |
|---|---|---|
| TradingView scanner (`america/scan`) | the FRESH book (4 branches on the 2026-11-11 settled bar), the 1114-name breadth universe, index ETFs, the sector/theme RS that drives the Hernandez funnel, today's settled close for every candidate | ok — `totalCount` asserted on every scan (3828 = 3828 for the fresh universe, 2307 = 2307 for the breadth universe) |
| shibui over the MCP-over-HTTP bridge | 10 T+1 sweep branches, the CANSLIM growth half, ADR% enrichment for all 1125 candidates, the GICS mapping, the shibui breadth cross-check | ok — no 429; every branch paged to completion; ADR enrichment returned 1121 of 1125 (4 names — CECO, HPE/PC, ORCL/PD, PBR.A — carry no valuation row) |
| Cboe delayed-quote CDN | the VIX 17.49 / VIX3M 19.24 pair | ok — two pulls 20 s apart, identical both times |
| MCP availability probe | `catalog_ok total=135 finance_tools=0`; bridge packs `tradier,fmp,market-recap` | ok (no finance MCP registered — expected, not an error) |
| Yahoo JSON / Finviz | — | not used: Yahoo is 429-prone from this egress and Finviz is Cloudflare-403; the ladder above was never reached |

- **The trigger/context split is the point of this run.** The 4% breakout, EP9M, 10% gap and volume-breakout screens are computed on **2026-11-11's own settled bar**. The multi-session context screens stay on shibui's **2026-11-10** session and say so. Every candidate publishes `data_as_of` and `source`.
- **`A_stockbee_4pct` landed on exactly 60 — the documented cap fingerprint — and it is a genuine screen outcome, not a truncation.** The branch carries no inner `LIMIT` (`rows_passing` is `COUNT(*) OVER ()` computed inside the branch, before any cap applies), and an independent `COUNT(*)` query over the same predicate returns exactly 60. It is flagged here rather than quietly published.
- **The parabolic gates were NOT re-expressed on TradingView's `Perf.W`.** `Perf.W` correlates r=0.997 with a **six**-session move and only r=0.924 with a five-session move (measured 2026-11-09), so the published ±25% / −50% five-session gates stay on shibui and stay T+1.
- **The prior-nine-session volume baseline is reconstructed exactly**: `average_volume_10d_calc` is the mean of the last ten sessions **including** today (bias 0.00% against a hand-computed reference on 11 names), so the prior-nine mean is recovered as `(10 × avg10 − volume_today) / 9` with no second data source.
- **CANSLIM was rebuilt on shibui, not read from TradingView.** TradingView's `earnings_growth_quarterly_yoy` / `sales_growth_quarterly_yoy` come back **NULL** for US equities (verified today: AAPL → None), so the growth half is taken from shibui's `fundamentals_derived_quarterly` (`eps_growth_yoy`, `revenue_growth_yoy`, both decimal fractions), with RSI 40-80, price > $5 and market cap > $1B. 69 names passed.
- **The Hernandez theme → group step is data-driven.** The themes are the top TradingView sector groups by composite 1M/3M/6M relative strength; the GICS bucket comes from shibui's `general_info`. The Commercial Services theme maps to Industrials at only **42%** of its resolved members — a genuinely mixed bucket, published as such rather than presented as a clean theme.
- **The scanner accepts only ONE equality filter per field.** Two `type` equal filters (stock + dr) return `totalCount` 0, so the breadth universe is pulled on the market-cap floor and the type/venue filter is applied locally. The pull asserted `totalCount` (2307 = 2307).
- **`rows_kept == rows_passing` on every branch.** The one cap fingerprint (`A_stockbee_4pct` = 60) was independently verified as a true count, above.
- **The pre-market brief reads `_regime.json` and `_summary.md`** from this directory; both are written. The regime payload is the flat schema v2 with all eight keys and a non-empty `atr_extensions` map.
- **No 1-year breadth percentile** is published in `breadth.md` — that needs the trailing session series for the universe, which this routine does not pull. The level is published without it, and the gap is stated rather than filled with a guess.
- **This is a screen, not a trade list.** No catalyst was sourced for any name; the parabolic lists are mechanical outcomes, and the focus list has not been discretionary-reviewed.

## Files in this directory

| File | What it is |
|---|---|
| `daily-sweep.md` | this file — the primary end-of-day sweep artifact |
| `breadth.md` | the end-of-day breadth & regime read (cron #09) |
| `_regime.json` | regime payload, flat schema v2 — **the canonical slot** |
| `_summary.md` | digest the pre-market brief reads |
| `_results.json` | machine-readable candidate set, tier lists, origins, screen_coverage, the fresh/t1 book split |
| `_cache.json` | cache marker (cron date + resolved data date) |
| `master.md / master.csv` | deduped union |
| `focus.md / focus.csv` | ≥2 stylists — cron #07 and cron #08 read these |
| `tier-a.md / tier-a.csv` | ≥3 stylists |
| `tier-a-fresh.md / tier-a-extended.md` | the Tier-A extension split (0 fresh / 4 extended today) |
| `stockbee.md / qullamaggie.md / jeff-sun.md / ariel-hernandez.md / peoplewish.md` | the five per-stylist books |
| `short-candidates.csv / long-reversal-candidates.csv` | the parabolic lists |
| `breadth-snapshot.*` | cron #10's intraday read — **NOT written by this cron** |

_Generated 2026-11-11 by cron #09 (stock-screener-daily-sweep-18:30). Window check passed (fire on schedule, platform stall 1 min)._
