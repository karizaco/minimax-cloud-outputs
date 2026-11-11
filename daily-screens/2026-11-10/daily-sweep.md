---
artifact: daily-sweep
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-10 18:30 ET"
cron_date: "2026-11-10"
screen_data_date: "2026-11-09 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-10 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-10 (official 16:00 ET close, bridge market-recap; TradingView agrees on 40/40 book names)"
regime: {size_cut_pct: 0, uncertainty: false, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 62.03}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Tuesday, 10 November 2026 (end-of-day, cron #09)

This run is the **first to use the dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-10's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-09**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **The book is 1356 candidates and the Tier-A list is 4 names** — FRVO, PRAX, QXO, WRBY. The FRESH book contributes **286 names** on today's settled bar: 258 that the T+1 book also carries, and **28 that only the fresh book found**. That is the payoff of the dual-book change — on the 2026-11-09 run the same 4%-breakout-plus-volume gate returned 68 names of which **25 were absent from the published book entirely**.
- **All four Tier-A names are EXTENDED — 0 fresh / 4 extended.** Every one of them trips both the ATR% and the >15%-above-20-DMA extension rules, and all four sit in the 99th percentile of the $10B+ sub-universe for distance above their 20-DMA. The convergence screens found the day's winners; the extension label is what says they have already run.
- **Caveat that changes how to read it**: the tape deteriorated under the book. Breadth fell to 62.03% above the 20-DMA with advance/decline at **428 / 678 / 8** (ratio 0.63), and **QQQ is -6.20% below its own 50-DMA** — the weakest leg of the tape, and further from its trend than at any point this month.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (breadth 62.03% is far above the 40% trigger) |
| `uncertainty` | **false** (VIX 19.46 / VIX3M 20.64 = 0.9428) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at +2.82%) |
| `index_below_20sma` | **true** (2 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+22.0 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-10** — the cron day's settled bar | `A_tv_breakout_4pct` 72 · `B_tv_ep9m` 206 · `D_tv_gap_10pct` 2 · `TV_volume_breakout` 63 | 286 |
| **T+1** (cross-check) | **2026-11-09** — shibui's newest ingested session | `A_stockbee_4pct` 468 · `B_stockbee_ep9m` 225 · `K_stockbee_anticipation` 285 · `C_qullamaggie_rs` 83 · `D_qullamaggie_ep` 1 · `E_qullamaggie_5d_gainers` 22 · `F_qullamaggie_5d_losers` 8 · `G_peoplewish` 356 · `H_hernandez_theme` 159 | 1,070 T+1-only |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 258 |
| `t1` | context screens only | 1,070 |
| `fresh` | trigger screens only | 28 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on all nine branches**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 468 | 468 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 225 | 225 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 285 | 285 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 83 | 83 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 1 | 1 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 22 | 22 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 8 | 8 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 356 | 356 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 159 | 159 | complete |

Total screened rows **1607** across the nine branches → **1356 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (4 names)

| Symbol | Stylists | Origins | Source | Close 11-10 | **Chg 11-10** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **FRVO** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, E_qullamaggie_5d_gainers, G_peoplewish | `fresh+t1` | 11.38 | **+0.00%** | 9.34 | 22.50 | 37.94 | EXTENDED |
| **PRAX** | 4 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme | `t1` | 337.59 | **+1.39%** | 5.54 | 25.89 | — | EXTENDED |
| **QXO** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, G_peoplewish | `fresh+t1` | 13.73 | **-0.36%** | 6.22 | 31.74 | — | EXTENDED |
| **WRBY** | 4 | A_stockbee_4pct, B_stockbee_ep9m, E_qullamaggie_5d_gainers, G_peoplewish, H_hernandez_theme | `t1` | 29.90 | **-1.03%** | 7.12 | 17.92 | 26.61 | EXTENDED |

### What Tier-A is saying

- **FRVO** (3 stylists, 5 origins) — the only name that hits both the fresh and the T+1 EP9M screen, plus the 5-day-gainer parabolic book and peoplewish. It closed **flat** today at 11.38 after a +26.09% move on 11-09: the gap is still open but the fuel is spent. It fails the valuation gate on negative free-cash-flow yield (−16.76%), so the growth the screens see is not yet cash.
- **PRAX** (4 stylists, 4 origins) — the strongest convergence in the book: Stockbee's 4% breakout, Qullamägi's RS-leader screen, peoplewish, AND the Hernandez theme funnel (XLV health care) all picked it. Its metrics are T+1 (2026-11-09) — it has no fresh trigger — and it is +23.50% above its own 20-DMA. Free-cash-flow yield is negative (−3.30%).
- **QXO** (3 stylists, 5 origins) — the freshest of the four: it hits the fresh 4% breakout and fresh EP9M books today AND the T+1 breakout, EP9M, RS-leader and peoplewish screens. It closed −0.36% at 13.73 after +19.20% on 11-09. It is the only Tier-A name whose valuation gate is `unknown` rather than `fail` (no trailing P/E reported) — which is a **disclosure, not a pass**.
- **WRBY** (4 stylists, 5 origins) — Stockbee breakout + EP9M, the 5-day-gainer parabolic short, peoplewish, and the XLV theme funnel. It carries the book's heaviest valuation flag set: **trailing P/E 499.8, operating P/E 2426, EV/EBIT 2411, PEG 48.1**, plus shibui's own `LARGE_NON_OPERATING` earnings-quality flag. The screens love it; the price already assumes a lot.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 4 extended.** Every one of the four trips both extension rules, and the percentile column makes it sharper: all four sit in the **99th percentile** of the $10B+ sub-universe for distance above their own 20-DMA (`pct_above_sma20_pctile_lc` 99.5–99.8).

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| FRVO | 9.83 | 98.2 | 24.46 | yes |
| PRAX | 5.21 | 86.0 | 23.50 | yes |
| QXO | 5.99 | 90.0 | 21.52 | yes |
| WRBY | 7.21 | 94.2 | 18.79 | yes |

Nothing is dropped for being extended — the label is published next to every candidate row, and the full split is in `tier-a-fresh.md` (empty) and `tier-a-extended.md` (4 names).

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close 11-10 | **Chg 11-10** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|---|
| **BW** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, TV_volume_breakout | `fresh+t1` | 4.48 | **+18.21%** | 3.14 | 10.06 | 47.9 | 7.79 |
| **FRVO** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, E_qullamaggie_5d_gainers, G_peoplewish | `fresh+t1` | 11.38 | **+0.00%** | 1.58 | 9.83 | 54.4 | 9.34 |
| **IAM** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, TV_volume_breakout | `fresh+t1` | 14.78 | **+10.46%** | 1.61 | 17.79 | 44.2 | 16.09 |
| **IMVT** | 2 | A_stockbee_4pct, H_hernandez_theme | `t1` | 35.71 | **+1.59%** | 1.01 | 4.35 | 67.6 | 4.27 |
| **LUNR** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 11.81 | **-1.91%** | 1.18 | 9.07 | 51.1 | 8.64 |
| **MPWR** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 1357.60 | **-2.19%** | 0.79 | 6.33 | 56.5 | 5.54 |
| **PL** | 2 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish | `t1` | 14.27 | **-0.70%** | 0.85 | 7.20 | 49.2 | 6.44 |
| **PRAX** | 4 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme | `t1` | 337.59 | **+1.39%** | 1.23 | 5.21 | 67.7 | 5.54 |
| **QXO** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, G_peoplewish | `fresh+t1` | 13.73 | **-0.36%** | 0.81 | 5.99 | 64.9 | 6.22 |
| **TLS** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, TV_volume_breakout | `fresh+t1` | 7.67 | **+6.97%** | 2.23 | 6.56 | 78.0 | 7.54 |
| **TTD** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, TV_volume_breakout | `fresh+t1` | 15.42 | **+3.28%** | 2.89 | 5.03 | 70.7 | 4.87 |
| **WRBY** | 4 | A_stockbee_4pct, B_stockbee_ep9m, E_qullamaggie_5d_gainers, G_peoplewish, H_hernandez_theme | `t1` | 29.90 | **-1.03%** | 1.06 | 7.21 | 64.6 | 7.12 |

Two Focus names are **fresh-trigger names that were invisible to the T+1 book**: **IAM** (+10.46% today, ATR 17.79% — the highest-volatility name in the list) and **TLS** (+6.97%, RSI 77.97). Both carry `A_tv_breakout_4pct` and `TV_volume_breakout` from today's settled bar; neither had a T+1 trigger. **BW** (+18.21%, RVOL 3.14) is the largest mover in the Focus list and did the same.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 361 | no red flag, and earnings data present |
| `fail` | 684 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 129 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag. On the 2026-11-09 run, counting a null P/E as a red flag would have flagged 910 of 1,232 names (73%) — a label that fires on three quarters of the book is as useless as one that never fires.

## Today's tape — the settled close of 2026-11-10

| Metric | Value |
|---|---|
| Universe | 1114 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **62.03%** / 53.68% / 49.55% |
| Advance / decline / unchanged | **428 / 678 / 8** (ratio 0.63) |
| Median name | -0.31% |
| VIX / VIX3M | **19.46 / 20.64** (VIX -2.31% from 19.92) |
| SPY / QQQ / RSP / IWM / QQQE | 749.92 (-0.37%) / 674.76 (-0.68%) / 220.88 (-0.03%) / 280.58 (-0.68%) / 115.12 (-0.36%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| CHTR | Charter Communications, Inc. | 134.06 | **+10.61%** |
| TTWO | Take-Two Interactive Software, Inc. | 224.64 | **+8.31%** |
| QNT | Quantinuum Inc. | 43.00 | **+7.39%** |
| EMBJ | Embraer S.A. | 82.50 | **+7.05%** |
| RKLB | Rocket Lab Corporation | 62.71 | **+6.54%** |
| BTSG | BrightSpring Health Services, Inc. | 72.49 | **+4.83%** |
| RRC | Range Resources Corporation | 51.20 | **+4.81%** |
| AMG | Affiliated Managers Group, Inc. | 401.32 | **+4.74%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| HL/PB | Hecla Mining Company Preferred Stock | 51.70 | -18.48% |
| PS | Pershing Square Inc. | 44.20 | -14.92% |
| ASTS | AST SpaceMobile, Inc. | 33.69 | -8.67% |
| INIO | INNIO N.V. | 13.77 | -7.65% |
| SKYD | Skydance Corporation | 8.04 | -7.59% |
| GFL | GFL Environmental Inc. Subordinate voting sh | 42.41 | -7.56% |
| ONON | On Holding AG | 34.70 | -7.54% |
| EQX | Equinox Gold Corp. | 11.23 | -7.11% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (22):** the names up 25%+ over five sessions, where a mean-reversion short is the mechanical outcome of the screen.

| Symbol | m1 (5d) | ADR% | Close 11-10 | Chg 11-10 |
|---|---|---|---|---|
| ACHC | 30.35 | 5.49 | 38.64 | +0.08% |
| APP | 79.16 | 5.22 | 395.51 | -3.53% |
| ARRY | 36.58 | 8.10 | 4.73 | -8.86% |
| AUGO | 31.33 | 6.35 | 81.31 | -6.53% |
| EWTX | 27.89 | 6.51 | 46.53 | -4.53% |
| FLY | 49.23 | 8.46 | 23.70 | -2.51% |
| FROG | 27.11 | 7.85 | 103.55 | -4.28% |
| FRVO | 37.94 | 9.34 | 11.38 | +0.00% |
| FUN | 39.20 | 8.94 | 10.16 | -5.58% |
| IONQ | 25.45 | 7.64 | 34.99 | -0.99% |
| JOBY | 28.48 | 6.33 | 5.92 | -4.21% |
| MGNI | 34.20 | 4.81 | 28.52 | -1.79% |
| OUST | 36.68 | 7.62 | 38.22 | -0.91% |
| QNT | 29.37 | 8.82 | 43.00 | +7.39% |
| RIOT | 49.16 | 9.26 | 18.08 | +2.38% |
| TMDX | 40.68 | 5.84 | 90.94 | -3.03% |
| U | 32.31 | 5.69 | 50.34 | -2.12% |
| UI | 26.96 | 4.63 | 685.94 | +0.04% |
| WOLF | 25.28 | 9.55 | 26.23 | +0.42% |
| WRBY | 26.61 | 7.12 | 29.90 | -1.03% |
| XMTR | 26.29 | 8.18 | 119.31 | -1.06% |
| XNCR | 30.11 | 6.75 | 39.39 | +2.07% |

**Long / mean-reversion candidates (8):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close 11-10 | Chg 11-10 |
|---|---|---|---|---|
| AXON | -28.74 | 5.34 | 302.54 | -0.21% |
| CVI | -30.08 | 6.82 | 38.71 | -1.00% |
| DOX | -34.31 | 3.31 | 41.46 | -0.67% |
| FIS | -29.41 | 3.73 | 28.31 | -0.11% |
| IRTC | -29.67 | 5.26 | 86.06 | -3.01% |
| NRIX | -37.20 | 6.13 | 15.88 | -1.61% |
| SNDX | -27.10 | 7.80 | 9.49 | -0.63% |
| VCYT | -47.10 | 6.67 | 24.06 | -7.18% |

## Per-stylist books

| Stylist | File | Rows |
|---|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` | 977 |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` | 113 |
| Jeff Sun, CFTe | `jeff-sun.md` | 129 |
| Ariel Hernandez | `ariel-hernandez.md` | 71 |
| peoplewish — Alec Riffle | `peoplewish.md` | 357 |

`ariel-hernandez.md` carries the theme → group → leaders funnel: the top themes by composite 1M/3M/6M relative strength (**XLV** health care, composite +54.7; **IBB** biotech, +42.8; **XRT** retail, +28.1) mapped to their GICS buckets, with the **159 leaders** inside those buckets (1M RS > 15, market cap > $2B) — 88 in the XLV/health-care bucket and 71 in the XRT/consumer-discretionary bucket. The GICS mapping comes from shibui's `general_info`, not from a hand-maintained table.

## Method, source health & caveats

| Source | Used for | Status |
|---|---|---|
| TradingView scanner (`america/scan`) | the FRESH book (4 branches on the 2026-11-10 settled bar), the 1114-name breadth universe, index ETFs, sector/thematic RS, the same-day close for every candidate | ok — `totalCount` asserted on every scan (3820 = 3820 for the fresh universe, 1114 = 1114 for the breadth universe) |
| shibui over the MCP-over-HTTP bridge | 8 sweep branches (T+1 context), the CANSLIM growth half, ADR% enrichment for all 1174 candidates, the GICS mapping, the shibui breadth cross-check | ok — no 429; every branch paged to completion |
| bridge `market-recap get_quotes` | today's official close for the 40 book names | ok — the batch caps at 40 symbols per call; 40 names took one batch |
| Cboe delayed-quote CDN | VIX / VIX3M pair, two pulls 20 s apart | ok — identical both times |
| MCP availability probe | `catalog_ok total=135 finance_tools=0`; bridge packs `tradier,fmp,market-recap` | ok (no finance MCP registered — expected, not an error) |
| Yahoo JSON / Finviz | — | not used: Yahoo is 429-prone from this egress and Finviz is Cloudflare-403; the ladder above was never reached |

- **The trigger/context split is the point of this run.** The 4% breakout, EP9M, 10% gap and volume-breakout screens are computed on **2026-11-10's own settled bar**. The multi-session context screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's **2026-11-09** session and say so. Every candidate publishes `data_as_of` and `source`.
- **The parabolic gates were NOT re-expressed on TradingView's `Perf.W`.** Measured on 2026-11-09 against shibui's own history, `Perf.W` correlates r=0.997 with a **six**-session move and only r=0.924 with a five-session move. Copying the published ±25% / −50% five-session gates onto a six-session window would silently shift the parabolic books.
- **The prior-nine-session volume baseline is reconstructed exactly**: `average_volume_10d_calc` is the mean of the last ten sessions **including** today (bias 0.00% against a hand-computed reference on 11 names), so the prior-nine mean is recovered as `(10 × avg10 − volume_today) / 9` with no second data source.
- **The day-alignment assertion passed**: the scanner's implied previous close — `close / (1 + change/100)` — is **752.69 for SPY** and **679.35 for QQQ**, and both match shibui's settled 2026-11-09 close exactly (SPY 752.69, QQQ 679.35). The scanner is on the 2026-11-10 session, not a stale one.
- **A defect in the skill's own ADR emitter was found and worked around at run time.** `screen.py emit_adr_enrichment_sql()` filters `q.symbol IN (<bare tickers>)`, but `shibui.stock_quotes.symbol` is venue-suffixed (`AAPL.NASDAQ`) — the bare ticker is `q.ticker`. The emitted query returns **zero rows for every chunk**, silently, which is the exact trap the skill's own data-source section warns about. This run emits the same query on the correct column, and the enrichment returned **1174 of 1174** candidates. The emitter itself is a repo fix, not a run-time fix.
- **`rows_kept == rows_passing` on every branch**, and no count lands on 30 / 50 / 60 / 200 — the truncation fingerprint is absent.
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
| `master.md` / `master.csv` | deduped union |
| `focus.md` / `focus.csv` | ≥2 stylists — cron #07 and cron #08 read these |
| `tier-a.md` / `tier-a.csv` | ≥3 stylists |
| `tier-a-fresh.md` / `tier-a-extended.md` | the Tier-A extension split (0 fresh / 4 extended today) |
| `stockbee.md` / `qullamaggie.md` / `jeff-sun.md` / `ariel-hernandez.md` / `peoplewish.md` | the five per-stylist books |
| `short-candidates.csv` / `long-reversal-candidates.csv` | the parabolic lists |
| `same-day-prints.md` / `_same-day-prints.json` | today's official close for all 40 book names |
| `breadth-snapshot.*` | cron #10's intraday read — **NOT written by this cron** |

_Generated 2026-11-10 by cron #09 (stock-screener-daily-sweep-18:30). Window check passed, fire on schedule (platform stall 1 min)._
