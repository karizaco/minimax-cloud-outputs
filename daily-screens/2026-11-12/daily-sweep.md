---
artifact: daily-sweep
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-12 18:30 ET"
cron_date: "2026-11-12"
screen_data_date: "2026-11-11 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-12 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-12 (settled 16:00 ET close from the TradingView scanner, re-verified against shibui's settled bars; the Cboe VIX pair is quoted 2026-11-12T16:15:01)"
regime: {size_cut_pct: 0, uncertainty: false, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 53.03}
coverage: "10/10 T+1 branches complete (rows_kept == rows_passing on every branch); 4/4 fresh TV branches complete (totalCount asserted)"
---

# Daily Screener Sweep — Thursday, 12 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-12's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window, CANSLIM growth, the Hernandez theme funnel) stay on shibui's newest ingested session as of the fire, **2026-11-11**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

> **Reconstruction note.** The fire was scheduled for **2026-11-12 18:30 ET** and the work completed at **2026-11-13 08:47 ET** — a delayed replay, resumed in place. Every number describes the **2026-11-12 settled close**; the anchor was re-verified against shibui's own settled bars after the replay (SPY 757.12, RSP 220.72, QQQ 688.17 — identical on both feeds), so nothing drifted onto the 2026-11-13 session.

## TL;DR

- **The book is 1134 candidates and the Tier-A list is 6 names** — AXGN, AZTA, CAPR, CRWV, NBIS, SHAZ. The FRESH book contributes **232 names** on today's settled bar, **52 of which the T+1 book never found**. That is the payoff of the dual book — those are names that only exist if today's own bar is read.
- **All 6 Tier-A names are EXTENDED — 0 fresh / 6 extended.** The convergence screens found the day's winners; the extension label is what says they have already run.
- **Caveat that changes how to read it**: the tape was weak but the *index* lagged it further. Breadth 53.03% above the 20-DMA with advance/decline **244 / 859 / 4** (ratio 0.28), yet **QQQ sits -4.24% below its own 50-DMA** while RSP is +2.68% above it.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (breadth 53.03% is far above the 40% trigger) |
| `uncertainty` | **false** (VIX 18.7 / VIX3M 20.06, ratio 0.9322) |
| `late_cycle` | **false** (the extreme is RSP at +2.68% above its 50-DMA) |
| `index_below_20sma` | **true** (2 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+13.03 pp — MATCHED** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-12** — the cron day's settled bar | A_tv_breakout_4pct 35 · B_tv_ep9m 186 · D_tv_gap_10pct 2 · TV_volume_breakout 34 | 232 |
| **T+1** (cross-check) | **2026-11-11** — shibui's newest ingested session | A_stockbee_4pct 199 · B_stockbee_ep9m 195 · K_stockbee_anticipation 402 · C_qullamaggie_rs 81 · D_qullamaggie_ep 5 · E_qullamaggie_5d_gainers 13 · F_qullamaggie_5d_losers 6 · G_peoplewish 351 · jeff_sun_canslim 154 · H_hernandez_theme 62 | 1082 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 180 |
| `t1` | context screens only | 902 |
| `fresh` | trigger screens only | 52 |

## Screen coverage — the assertion that makes the book publishable

Every T+1 branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on all 10 branches.**

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
| `jeff_sun_canslim` | Jeff Sun — CANSLIM growth + strength (T+1) | 154 | 154 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 62 | 62 | complete |

Total screened rows **1468** across the 10 T+1 branches, plus **257** across the 4 fresh TV branches → **1134 distinct candidates** after dedup and merge.

## Tier-A — ≥ 3 distinct stylists (6 names)

| Symbol | Stylists | Origins | Source | Close 11-12 | **Chg 11-12** | ADR% | ATR% | RSI | Val gate | Ext |
|---|---|---|---|---|---|---|---|---|---|---|
| **AXGN** | 5 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme, jeff_sun_canslim | `t1` | 55.4 | **-5.51%** | 5.16 | 5.41 | 69.3 | unknown | EXTENDED |
| **AZTA** | 3 | A_stockbee_4pct, C_qullamaggie_rs, H_hernandez_theme | `t1` | 43.86 | **-10.31%** | 6.06 | 6.62 | 59.2 | unknown | EXTENDED |
| **CAPR** | 3 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, H_hernandez_theme | `t1` | 10.24 | **-8.73%** | 10.08 | 9.3 | 62 | fail | EXTENDED |
| **CRWV** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish | `fresh+t1` | 56.6 | **-6.86%** | 9.97 | 11.47 | 46 | fail | EXTENDED |
| **NBIS** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 128.64 | **-16.84%** | 9.2 | 14.26 | 38.7 | fail | EXTENDED |
| **SHAZ** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 24.29 | **-8.06%** | 12.25 | 14.88 | 41.3 | fail | EXTENDED |

### What Tier-A is saying

- **AXGN** (5 stylists) — A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme, jeff_sun_canslim. It closed **-5.51%** at 55.4, carries no fresh trigger — its screen metrics are T+1. It unknowns the valuation gate (no red flag), and it sits at the 99.8 percentile of the $10B+ sub-universe for distance above its own 20-DMA.
- **AZTA** (3 stylists) — A_stockbee_4pct, C_qullamaggie_rs, H_hernandez_theme. It closed **-10.31%** at 43.86, carries no fresh trigger — its screen metrics are T+1. It unknowns the valuation gate (no red flag), and it sits at the 98.7 percentile of the $10B+ sub-universe for distance above its own 20-DMA.
- **CAPR** (3 stylists) — A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, H_hernandez_theme. It closed **-8.73%** at 10.24, carries no fresh trigger — its screen metrics are T+1. It fails the valuation gate (free_cash_flow_yield), and it sits at the 100 percentile of the $10B+ sub-universe for distance above its own 20-DMA.
- **CRWV** (3 stylists) — A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish. It closed **-6.86%** at 56.6, and hits the fresh trigger book as well as the T+1 context book. It fails the valuation gate (free_cash_flow_yield, debt_to_equity), and it sits at the 66.8 percentile of the $10B+ sub-universe for distance above its own 20-DMA.
- **NBIS** (3 stylists) — A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish. It closed **-16.84%** at 128.64, and hits the fresh trigger book as well as the T+1 context book. It fails the valuation gate (trailing_pe, free_cash_flow_yield), and it sits at the 1.8 percentile of the $10B+ sub-universe for distance above its own 20-DMA.
- **SHAZ** (3 stylists) — A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish. It closed **-8.06%** at 24.29, carries no fresh trigger — its screen metrics are T+1. It fails the valuation gate (free_cash_flow_yield), and it sits at the 37.8 percentile of the $10B+ sub-universe for distance above its own 20-DMA.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 6 extended.** Across the whole book, 544 of 1134 names trip an extension rule. Nothing is dropped for being extended — the label is published next to every candidate row, and the full split is in `tier-a-fresh.md` and `tier-a-extended.md`.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | Rule tripped |
|---|---|---|---|---|
| AXGN | 5.41 | 88 | +22.29% | ATR% > 5.0 (a normal large cap is 1.5-3%) (5.41); > 15% above its 20-DMA (22.29) |
| AZTA | 6.62 | 93.4 | +13.38% | ATR% > 5.0 (a normal large cap is 1.5-3%) (6.62) |
| CAPR | 9.3 | 97.9 | +35.48% | ATR% > 5.0 (a normal large cap is 1.5-3%) (9.30); > 15% above its 20-DMA (35.48) |
| CRWV | 11.47 | 99.6 | +2.16% | ATR% > 5.0 (a normal large cap is 1.5-3%) (11.47) |
| NBIS | 14.26 | 100 | -16.25% | ATR% > 5.0 (a normal large cap is 1.5-3%) (14.26) |
| SHAZ | 14.88 | 100 | -0.86% | ATR% > 5.0 (a normal large cap is 1.5-3%) (14.88) |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close 11-12 | **Chg 11-12** | RVOL 10d | ATR% | RSI | ADR% | Val gate |
|---|---|---|---|---|---|---|---|---|---|---|
| **AAOI** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 52.85 | **-5.39%** | 0.62 | 14.84 | 35.9 | 10.41 | fail |
| **AXGN** | 5 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme, jeff_sun_canslim | `t1` | 55.4 | **-5.51%** | 1.63 | 5.41 | 69.3 | 5.16 | unknown |
| **AXTI** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 43.54 | **-7.30%** | 0.82 | 15.9 | 41.4 | 11.69 | fail |
| **AZTA** | 3 | A_stockbee_4pct, C_qullamaggie_rs, H_hernandez_theme | `t1` | 43.86 | **-10.31%** | 0.88 | 6.62 | 59.2 | 6.06 | unknown |
| **CAPR** | 3 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, H_hernandez_theme | `t1` | 10.24 | **-8.73%** | 0.92 | 9.3 | 62 | 10.08 | fail |
| **CRWV** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish | `fresh+t1` | 56.6 | **-6.86%** | 1.55 | 11.47 | 46 | 9.97 | fail |
| **FPS** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 22.15 | **-9.85%** | 1.43 | 13.42 | 40.9 | 9.26 | fail |
| **GLXY** | 2 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish | `t1` | 15.18 | **-4.95%** | 0.8 | 11.53 | 44.4 | 10.54 | fail |
| **LGN** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 36.27 | **-2.21%** | 1.16 | 10.77 | 45.1 | 9.2 | fail |
| **NBIS** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 128.64 | **-16.84%** | 2.73 | 14.26 | 38.7 | 9.2 | fail |
| **SHAZ** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 24.29 | **-8.06%** | 1.66 | 14.88 | 41.3 | 12.25 | fail |
| **SNDK** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 937.46 | **-4.11%** | 0.87 | 11.52 | 35.9 | 7.78 | pass |

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 1059 | no red flag, and earnings data present |
| `fail` | 1892 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 469 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-12

| Metric | Value |
|---|---|
| Universe | 1107 names (NYSE/NASDAQ/AMEX, type stock+dr, market_cap_basic > $10B) |
| % above 20 / 50 / 200-DMA | **53.03%** / 52.3% / 49.41% |
| Advance / decline / unchanged | **244 / 859 / 4** (ratio 0.28) |
| Median name | -0.90% |
| VIX / VIX3M | **VIX 18.7 / VIX3M 20.06** (prior session 17.49 / 19.24) |
| SPY / RSP / QQQ / QQQE / IWM | 757.12 (-0.35%) / 220.72 (-0.87%) / 688.17 (-0.32%) / 116.58 (-0.95%) / 278.44 (-1.64%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| BGIN | Bgin Blockchain Limited | 2.76 | **+49.19%** |
| PLBL | Polibeli Group Ltd | 7.27 | **+28.79%** |
| AGBK | AGI Inc | 6.32 | **+17.25%** |
| NUAI | New Era Energy & Digital, Inc. | 2.72 | **+16.74%** |
| SENEB | Seneca Foods Corp. | 172.8 | **+16.51%** |

| Ticker | Name | Close | Chg |
|---|---|---|---|
| CDNL | Cardinal Infrastructure Group Inc. | 5.64 | **-62.37%** |
| ADIG | ADI Global Distribution Inc. | 9.82 | **-49.85%** |
| ENVX | Enovix Corporation | 1.8 | **-28.66%** |
| KPLT | Katapult Holdings, Inc. | 8.16 | **-27.01%** |
| BZ | KANZHUN LIMITED - American Depository Shares | 12.49 | **-25.30%** |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (13):** the names up 25%+ over five sessions, where a mean-reversion short is the mechanical outcome of the screen.

| Symbol | m1 (5d) | ADR% | Close 11-12 | Chg 11-12 |
|---|---|---|---|---|
| AAON | 31.04 | 7.24 | 78.8 | +3.24% |
| APP | 48.95 | 5.37 | 393.68 | -2.74% |
| CRWV | 25.51 | 9.97 | 56.6 | -6.86% |
| EWTX | 26.75 | 6.45 | 45.82 | -3.68% |
| FLY | 55.07 | 8.9 | 25.31 | -4.89% |
| FROG | 26.84 | 7.72 | 110.6 | +1.00% |
| FRVO | 45.39 | 9.66 | 11.65 | -9.97% |
| FUN | 39.97 | 8.19 | 11.19 | +0.81% |
| KRMN | 30.79 | 8.39 | 40.5 | -9.38% |
| MGNI | 28.17 | 4.68 | 29.34 | +0.45% |
| RKLB | 26.31 | 8 | 64.07 | -3.14% |
| TMDX | 26.47 | 6.07 | 92 | -0.01% |
| WRBY | 41.62 | 7.1 | 26.73 | -11.34% |

**Long / mean-reversion candidates (6):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close 11-12 | Chg 11-12 |
|---|---|---|---|---|
| AXON | -25.64 | 5.51 | 307.11 | -2.63% |
| CAI | -26.28 | 6.62 | 23.96 | -2.16% |
| IBRX | -25.31 | 8.26 | 6.07 | -9.00% |
| IONS | -29.44 |  | 27.31 | -3.60% |
| IRTC | -33.82 | 5.57 | 93.56 | +5.50% |
| OPEN | -31.06 | 9.76 | 1.24 | -9.52% |

## Per-stylist books

| Stylist | File | Rows |
|---|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` | 794 |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` | 102 |
| Jeff Sun, CFTe | `jeff-sun.md` | 187 |
| Ariel Hernandez | `ariel-hernandez.md` | 62 |
| peoplewish — Alec Riffle | `peoplewish.md` | 351 |

`ariel-hernandez.md` carries the theme → group → leaders funnel: the top themes by composite 1M/3M/6M relative strength (**Health Care** 49.0 (XLV) · **Consumer Staples** 19.5 (XLP) · **Financials** 18.4 (XLF)) mapped to their GICS buckets via shibui's `general_info`, with the leaders inside those buckets (21-session return ≥ 20% or 63-session return ≥ 40%, ADR% ≥ 4.5, 20-day average dollar volume ≥ $20M, market cap > $300M) — 62 names. The GICS mapping comes from shibui's `general_info`, not from a hand-maintained table.

## Method, source health & caveats

| Source | Used for | Status |
|---|---|---|
| TradingView scanner (`america/scan`) | the FRESH book (4 branches on the 2026-11-12 settled bar), the 1107-name breadth universe, the five index ETFs, the sector/theme RS that drives the Hernandez funnel, today's settled close for every candidate | ok — `totalCount` asserted on every scan (3806 = 3806 for the fresh universe, 1107 = 1107 for the breadth universe) |
| shibui over the MCP-over-HTTP bridge | 10 T+1 sweep branches, the CANSLIM growth half, the GICS mapping, the valuation/quality overlay for 3420 names | ok — no 429; every branch paged to completion; the overlay ran chunked (200 symbols per call) after the single 3,814-ticker request came back unparseable |
| Cboe delayed-quote CDN | the VIX 18.7 / VIX3M 20.06 pair | ok — two pulls 20 s apart, identical both times (`vix_stable: true`) |
| MCP availability probe | `catalog_ok total=135 finance_tools=0`; bridge packs `tradier,fmp,market-recap` | ok (no finance MCP registered — expected, not an error) |
| Yahoo JSON / Finviz | — | not used: Yahoo is 429-prone from this egress and Finviz is Cloudflare-403; the ladder above was never reached |

- **This is a delayed replay.** The fire was scheduled for 2026-11-12 18:30 ET and the work completed at 2026-11-13 08:47 ET. Every figure describes the **2026-11-12 settled close**, and the anchor was re-verified against shibui's own settled bars after the resume (SPY 757.12, RSP 220.72, QQQ 688.17 — identical on both feeds). The T+1 book stays anchored to **2026-11-11**, the session shibui had ingested at fire time, so the two books keep the same relationship they had on the night.
- **The trigger/context split is the point of this run.** The 4% breakout, EP9M, 10% gap and volume-breakout screens are computed on **2026-11-12's own settled bar**. The multi-session context screens stay on shibui's **2026-11-11** session and say so. Every candidate publishes `data_as_of` and `source`.
- **The parabolic gates were NOT re-expressed on TradingView's `Perf.W`.** `Perf.W` correlates r=0.997 with a **six**-session move and only r=0.924 with a five-session move (measured 2026-11-09), so the published ±25% five-session gates stay on shibui and stay T+1.
- **The prior-nine-session volume baseline is reconstructed exactly**: `average_volume_10d_calc` is the mean of the last ten sessions **including** today (bias 0.00% against a hand-computed reference on 11 names), so the prior-nine mean is recovered as `(10 × avg10 − volume_today) / 9` with no second data source.
- **CANSLIM was rebuilt on shibui, not read from TradingView.** TradingView's `earnings_growth_quarterly_yoy` / `sales_growth_quarterly_yoy` come back NULL for US equities, so the growth half comes from shibui's `fundamentals_derived_quarterly` (`eps_growth_yoy`, `revenue_growth_yoy`, both decimal fractions) — each symbol's **latest reported quarter**, not the single most recent quarter-end, because that table's newest `date` is a one-row reporting date. With RSI 40-80, price > $5, market cap > $1B and the stock up on its session, **154 names passed**.
- **The Hernandez theme → group step is data-driven.** The themes are the top sector ETFs by composite 1M/3M/6M relative strength (XLV, XLP, XLF); the GICS bucket comes from shibui's `general_info`, so the mapping is not hand-maintained. **62 names** passed the leader gate.
- **`rows_kept == rows_passing` on every branch.** The two largest branches — `K_stockbee_anticipation` (402) and `G_peoplewish` (351) — were paged to completion, so the book is complete rather than truncated at shibui's 200-row ceiling.
- **`ariel-hernandez.md` carries the theme funnel's names.** The `consume` step maps that file through a CANSLIM proxy; the hernandez *bucket* is the theme → group → leaders funnel, so the file was rewritten with the funnel's own names. Every other per-stylist file is `consume`'s own output.
- **The pre-market brief reads `_regime.json` and `_summary.md`** from this directory; both are written. The regime payload is the flat schema v2 with all eight keys and a non-empty `atr_extensions` map (`_regime-screener.json` is written as an alias).
- **No 1-year breadth percentile** is published in `breadth.md` — that needs the trailing session series for the universe, which this routine does not pull. The level is published without it, and the gap is stated rather than filled with a guess.
- **This is a screen, not a trade list.** No catalyst was sourced for any name; the parabolic lists are mechanical outcomes, and the focus list has not been discretionary-reviewed.

## Files in this directory

| File | What it is |
|---|---|
| `daily-sweep.md` | this file — the primary end-of-day sweep artifact |
| `breadth.md` | the end-of-day breadth & regime read (cron #09) |
| `_regime.json` | regime payload, flat schema v2 — **the canonical slot** |
| `_regime-screener.json` | alias of `_regime.json`, for readers already on that name |
| `_summary.md` | digest the pre-market brief reads |
| `_results.json` | machine-readable candidate set, tier lists, origins, screen_coverage, the fresh/t1 book split |
| `_cache.json` | cache marker (cron date + resolved data date) |
| `master.md` / `master.csv` | the full deduped union with every candidate |
| `focus.md` / `focus.csv` | Focus tier — ≥ 2 stylists OR top-5 velocity |
| `tier-a.md` / `tier-a.csv` | Tier-A — ≥ 3 distinct stylists |
| `tier-a-fresh.md` / `tier-a-extended.md` | the Tier-A split by the extension label |
| `stockbee.md`, `qullamaggie.md`, `jeff-sun.md`, `ariel-hernandez.md`, `peoplewish.md` | the per-stylist books |
| `short-candidates.csv`, `long-reversal-candidates.csv` | the parabolic short / long books |

_Generated for the 2026-11-12 18:30 ET fire of cron #09 (stock-screener-daily-sweep-18:30); published 2026-11-13 08:47 ET._
