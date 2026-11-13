---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-12 18:30 ET"
cron_date: "2026-11-12"
screen_data_date: "2026-11-11 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-12 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-12 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 0, uncertainty: false, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 53.07}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Thursday 12 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-12's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-11**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **The book is 1,173 candidates and the Tier-A list is 4 names** — AXGN, CRWV, NBIS, SHAZ. The FRESH book contributes **232 names** on the 2026-11-12 settled bar, **27 of which the T+1 book never found** — that is the payoff of the dual book.
- **All 4 Tier-A names are EXTENDED — 0 fresh / 4 extended.** The convergence screens found names that have already run; the extension label is what says so, and nothing is dropped for tripping it.
- **Caveat that changes how to read it:** the session was broadly soft — breadth 53.07% above the 20-DMA but advance/decline **242 / 860 / 4** (ratio 0.28) — and **QQQ sits -4.24% below its own 50-DMA** while RSP is +2.68% above it. Three of the four Tier-A names closed lower, and NBIS was the worst large-cap decliner of the session at -16.84%.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (breadth 53.07% is far above the 40% trigger) |
| `uncertainty` | **false** (VIX 18.7 / VIX3M 20.06 = 0.9322) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at +2.68%) |
| `index_below_20sma` | **true** (2 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+13.1 pp — MATCHED** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-12** — the cron day's settled bar | `A_tv_breakout_4pct` 35 · `B_tv_ep9m` 186 · `D_tv_gap_10pct` 2 · `TV_volume_breakout` 34 | 232 |
| **T+1** (cross-check) | **2026-11-11** — shibui's newest ingested session | 9 branches | 1146 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 205 |
| `t1` | context screens only | 941 |
| `fresh` | trigger screens only | 27 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 199 | 199 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 195 | 195 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 402 | 402 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 81 | 81 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 5 | 5 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 13 | 13 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 6 | 6 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 351 | 351 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 118 | 118 | complete |

Total screened rows **1370** across the 9 branches → **1173 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (4 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **AXGN** | 4 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme | `t1` | 55.40 | **-5.51%** | 5.38 | 59.84 | — | EXTENDED |
| **CRWV** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish | `fresh+t1` | 56.60 | **-6.86%** | 9.98 | 9.30 | 25.51 | EXTENDED |
| **NBIS** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 128.64 | **-16.84%** | 9.05 | -2.81 | 11.73 | EXTENDED |
| **SHAZ** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 24.29 | **-8.06%** | 12.38 | 12.00 | 14.34 | EXTENDED |

### What Tier-A is saying

- **AXGN** (4 stylists) — A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme. It closed **-5.51%** at 55.40 and carries no fresh trigger: its screen metrics are T+1. ADR% 5.38, 14-day velocity +59.84%. EXTENDED on ATR% 5.41 (88.0 percentile of the $10B+ sub-universe) and +22.29% above its own 20-DMA.
- **CRWV** (3 stylists) — A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish. It closed **-6.86%** at 56.60 and hits the fresh trigger book as well as the T+1 context book. ADR% 9.98, m1 (5-session move) +25.51%, so it is also on the parabolic short list. EXTENDED on ATR% 11.47 (99.6 percentile).
- **NBIS** (3 stylists) — A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish. It closed **-16.84%** at 128.64 — the worst large-cap decliner of the session — and still clears three screens, which is the convergence case working as designed. ATR% 14.26 (100.0 percentile) and it sits **16.25% BELOW** its own 20-DMA, so the move is a break, not a run. EXTENDED on ATR% alone.
- **SHAZ** (3 stylists) — A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish. It closed **-8.06%** at 24.29, T+1 screen metrics, ADR% 12.38 — the widest daily range of the four. EXTENDED on ATR% 14.88 (100.0 percentile) with -0.86% versus its 20-DMA.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 4 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| AXGN | 5.41 | 88.0 | 22.29 | yes |
| CRWV | 11.47 | 99.6 | 2.16 | no |
| NBIS | 14.26 | 100.0 | -16.25 | no |
| SHAZ | 14.88 | 100.0 | -0.86 | no |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **AAOI** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 52.85 | **-5.39%** | 0.62 | 14.84 | 35.9 | 10.34 |
| **AXGN** | 4 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme | `t1` | 55.40 | **-5.51%** | 1.63 | 5.41 | 69.3 | 5.38 |
| **AXTI** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 43.54 | **-7.30%** | 0.82 | 15.90 | 41.4 | 11.91 |
| **AZTA** | 2 | A_stockbee_4pct, C_qullamaggie_rs | `t1` | 43.86 | **-10.31%** | 0.88 | 6.62 | 59.2 | 6.20 |
| **CAPR** | 2 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs | `t1` | 10.24 | **-8.73%** | 0.92 | 9.30 | 62.0 | 10.13 |
| **CRWV** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish | `fresh+t1` | 56.60 | **-6.86%** | 1.55 | 11.47 | 46.0 | 9.98 |
| **FPS** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 22.15 | **-9.85%** | 1.43 | 13.42 | 40.9 | 9.57 |
| **GLXY** | 2 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish | `t1` | 15.18 | **-4.95%** | 0.80 | 11.53 | 44.4 | 10.35 |
| **LGN** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 36.27 | **-2.21%** | 1.16 | 10.77 | 45.1 | 9.24 |
| **NBIS** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 128.64 | **-16.84%** | 2.73 | 14.26 | 38.7 | 9.05 |
| **SHAZ** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 24.29 | **-8.06%** | 1.66 | 14.88 | 41.3 | 12.38 |
| **SNDK** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 937.46 | **-4.11%** | 0.87 | 11.52 | 35.9 | 7.79 |

Twelve names, eight of them closed lower — the focus list is a **screen**, not a trade list, and no catalyst was sourced for any name. The book's own extension and valuation labels are published next to every row: `tier-a-fresh.md` / `tier-a-extended.md` split Tier-A by the extension label, and `master.csv` carries the overlay's verdict and its numbers for every candidate.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 377 | no red flag, and earnings data present |
| `fail` | 664 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 129 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-12

| Metric | Value |
|---|---|
| Universe | 1106 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **53.07%** / 52.35% / 49.46% |
| Advance / decline / unchanged | **242 / 860 / 4** (ratio 0.28) |
| Median name | -0.88% |
| VIX / VIX3M | **18.7 / 20.06** (VIX -4.92% from 18.7) |
| SPY / QQQ / RSP / IWM / QQQE | 757.12 (-0.35%) / 688.17 (-0.32%) / 220.72 (-0.87%) / 278.44 (-1.64%) / 116.58 (-0.95%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| MOG.B | Moog Inc. | 347.00 | **+6.72%** |
| HUBS | HubSpot, Inc. | 215.84 | **+6.39%** |
| AMD | Advanced Micro Devices, Inc. | 585.30 | **+5.86%** |
| AVGO | Broadcom Inc. | 364.36 | **+5.54%** |
| ANET | Arista Networks, Inc. | 206.63 | **+5.06%** |
| TTEK | Tetra Tech, Inc. | 39.43 | **+4.84%** |
| VG | Venture Global, Inc. | 13.26 | **+4.74%** |
| CLS | Celestica, Inc. | 254.03 | **+4.57%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| NBIS | Nebius Group N.V. | 128.64 | -16.84% |
| GPN | Global Payments Inc. | 88.19 | -12.01% |
| SMCI | Super Micro Computer, Inc. | 26.99 | -11.30% |
| SMCIP | Super Micro Computer, Inc. - Depositary Shar | 47.32 | -10.23% |
| TIGO | Millicom International Cellular S.A. | 80.83 | -9.62% |
| SMMT | Summit Therapeutics Inc. | 15.07 | -9.41% |
| IONQ | IonQ, Inc. | 30.86 | -9.40% |
| KDP | Keurig Dr Pepper Inc. | 35.42 | -7.40% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (13):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| AAON | 31.04 | 7.45 | 78.80 | +3.24% |
| APP | 48.95 | 5.22 | 393.68 | -2.74% |
| CRWV | 25.51 | 9.98 | 56.60 | -6.86% |
| EWTX | 26.75 | 6.49 | 45.82 | -3.68% |
| FLY | 55.07 | 8.76 | 25.31 | -4.89% |
| FROG | 26.84 | 7.73 | 110.60 | +1.00% |
| FRVO | 45.39 | 9.73 | 11.65 | -9.97% |
| FUN | 39.97 | 8.09 | 11.19 | +0.81% |
| KRMN | 30.79 | 8.30 | 40.50 | -9.38% |
| MGNI | 28.17 | 4.59 | 29.34 | +0.45% |
| RKLB | 26.31 | 7.72 | 64.07 | -3.14% |
| TMDX | 26.47 | 6.19 | 92.00 | -0.01% |
| WRBY | 41.62 | 7.58 | 26.73 | -11.34% |

**Long / mean-reversion candidates (6):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| AXON | -25.64 | 5.49 | 307.11 | -2.63% |
| CAI | -26.28 | 6.35 | 23.96 | -2.16% |
| IBRX | -25.31 | 8.33 | 6.07 | -9.00% |
| IONS | -29.44 | 4.91 | 27.31 | -3.60% |
| IRTC | -33.82 | 5.75 | 93.56 | +5.50% |
| OPEN | -31.06 | 9.22 | 1.24 | -9.52% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

The theme → group → leaders funnel chose its themes from the FRESH book's universe: **XLV** and **IBB** → Health Care, **XRT** → Consumer Discretionary, from a 287-name theme candidate pool. The GICS mapping comes from shibui's `general_info`, not from a hand-maintained table, and the leaders inside those buckets are published with their ADR% and their 5- and 10-session moves — **118 names** cleared the gate.

## Method, source health & caveats

| Source | Used for | Status |
|---|---|---|
| TradingView scanner (`america/scan`) | the FRESH book (4 branches on the 2026-11-12 settled bar), the 1,106-name breadth universe, the five index ETFs, the sector/theme RS behind the Hernandez funnel, today's settled close for every candidate | ok — `totalCount` asserted on every scan (3,806 = 3,806 for the fresh universe, 1,106 = 1,106 for the breadth universe) |
| shibui over the MCP-over-HTTP bridge | 8 T+1 sweep branches, the CANSLIM growth half, the merged enrichment pass (ADR% for the whole book), the GICS mapping, the valuation/quality overlay | ok — no 429; every branch paged to completion (`rows_kept == rows_passing` on all 9); the overlay ran chunked, 200 symbols per bridge call |
| Cboe delayed-quote CDN | the VIX 18.70 / VIX3M 20.06 pair | ok — two pulls 5 s apart, identical both times |
| bridge `market-recap` | the official 16:00 ET close for the book names (`same-day-prints.md`) | ok |
| MCP availability probe | `catalog_ok total=135 finance_tools=0`; bridge packs `tradier,fmp,market-recap` | ok (no finance MCP registered — expected, not an error) |
| Yahoo JSON / Finviz | — | not used: Yahoo is 429-prone from this egress and Finviz is Cloudflare-403; the ladder above was never reached |

- **This fire was a delayed replay.** It was scheduled for 2026-11-12 18:30 ET and the work completed on 2026-11-13 at ~10:40 ET, resumed in place. Every figure describes the **2026-11-12 settled close** — the anchor was re-verified against shibui's own settled rows for 2026-11-12 (SPY 757.12, RSP 220.72, QQQ 688.17, identical on both feeds) before publication, and the screen session was FORCED to 2026-11-11 with `--t1-date` so the two books keep the same relationship they had on the night.
- **The trigger/context split is the point of this run.** The 4% breakout, EP9M, 10% gap and volume-breakout screens are computed on **2026-11-12's own settled bar**. The multi-session context screens stay on shibui's **2026-11-11** session and say so. Every candidate publishes `data_as_of` and `source`.
- **`rows_kept == rows_passing` on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200). The two largest — `K_stockbee_anticipation` (402) and `G_peoplewish` (351) — were paged to completion, so the book is complete rather than truncated at shibui's 200-row ceiling.
- **The parabolic gates were NOT re-expressed on TradingView's `Perf.W`.** `Perf.W` correlates r=0.997 with a **six**-session move and only r=0.924 with a five-session move, so the published ±25% five-session gates stay on shibui and stay T+1.
- **The prior-nine-session volume baseline is reconstructed exactly**: `average_volume_10d_calc` is the mean of the last ten sessions **including** today, so the prior-nine mean is recovered as `(10 × avg10 − volume_today) / 9` with no second data source.
- **CANSLIM is rebuilt on shibui, not read from TradingView.** TradingView's US growth columns come back NULL, so the growth half comes from shibui's `fundamentals_derived_quarterly`, each symbol's **latest reported quarter** — that table's newest `date` is a ONE-ROW reporting date, so a `MAX(date)` join returns NULL growth for every symbol and the branch returns nothing. The price half (close, change, RSI) comes from the FRESH book, so the CANSLIM screen is on the cron day's own bar.
- **The overlay is a LABEL, not a filter.** It never removes a name from the book; it tells the reader what the growth screen does not ask about. A missing trailing P/E is published as `earnings_data_missing` with `valuation_gate: unknown` — disclosed, never counted as a red flag.
- **No 1-year breadth percentile** is published in `breadth.md` — the trailing session series for the universe is not pulled by this routine. The level is published without it, and the gap is stated rather than filled with a guess.
- **This is a screen, not a trade list.** No catalyst was sourced for any name, the parabolic lists are mechanical outcomes, and the focus list has not been discretionary-reviewed.

## Files in this directory

| File | What it is |
|---|---|
| `daily-sweep.md` | this file — the primary end-of-day sweep artifact |
| `breadth.md` | the end-of-day breadth & regime read (cron #09) |
| `_regime.json` | regime payload, flat schema v2 — **the canonical slot** |
| `_summary.md` | digest the pre-market brief reads |
| `_results.json` | machine-readable candidate set, tier lists, origins, screen_coverage, the fresh/t1 book split |
| `_cache.json` | cache marker (cron date + resolved data date) |
| `master.md` / `master.csv` | deduped union |
| `focus.md` / `focus.csv` | ≥2 stylists — cron #07 and cron #08 read these |
| `tier-a.md` / `tier-a.csv` | ≥3 stylists |
| `tier-a-fresh.md` / `tier-a-extended.md` | the Tier-A extension split |
| `stockbee.md` / `qullamaggie.md` / `jeff-sun.md` / `ariel-hernandez.md` / `peoplewish.md` | the five per-stylist books |
| `short-candidates.csv` / `long-reversal-candidates.csv` | the parabolic lists, with their defining metric |
| `same-day-prints.md` / `_same-day-prints.json` | today's official close for the book names |
| `breadth-snapshot.*` | cron #10's intraday read — **NOT written by this cron** |
