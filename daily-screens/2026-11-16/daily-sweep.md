---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-16 18:30:52 ET"
cron_date: "2026-11-16"
screen_data_date: "2026-11-13 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-16 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-16 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 0, uncertainty: false, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 43.93}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Monday 16 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-16's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-13**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **Breadth broke down.** Only **43.93%** of the 1,095 $10B+ large caps closed above their 20-DMA, and the settled tape printed **297 advancing vs 787 declining** (ratio 0.38, net -490) with a -0.77% median name — a broadly weak tape, not an index-only wobble. The BROAD divergence (+43.93 pp) identifies the INDEX as the weak leg (0 of 5 index ETFs above their 20-DMA), not a healthy average stock.
- **Volatility stepped up.** VIX **22.91** (+18.7% from 19.30) against VIX3M 23.02 is a ratio of **0.9952** — just under the 1.0 uncertainty trigger — while every index ETF sits below its 20-DMA (QQQ -7.67% vs its 50-DMA).
- **Tier-A is 3 names and every one of them is EXTENDED** (0 fresh), and **11 of the 12 Focus names fail the valuation overlay**. The book is a momentum pocket inside a tape that is losing participation.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (breadth 43.93% is far above the 40% trigger) |
| `uncertainty` | **false** (VIX 22.91 / VIX3M 23.02 = 0.9952) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at +1.84%) |
| `index_below_20sma` | **true** (0 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+43.9 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-16** — the cron day's settled bar | `A_tv_breakout_4pct` 35 · `B_tv_ep9m` 210 · `D_tv_gap_10pct` 2 · `TV_volume_breakout` 36 | 254 |
| **T+1** (cross-check) | **2026-11-13** — shibui's newest ingested session | 9 branches | 1114 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 205 |
| `t1` | context screens only | 909 |
| `fresh` | trigger screens only | 49 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 71 | 71 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 170 | 170 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 534 | 534 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 64 | 64 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 2 | 2 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 6 | 6 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 4 | 4 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 334 | 334 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 57 | 57 | complete |

Total screened rows **1242** across the 9 branches → **1163 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (3 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **CBRS** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 100.99 | **-7.11%** | 9.10 | 0.32 | 11.20 | EXTENDED |
| **CGON** | 5 | A_stockbee_4pct, A_tv_breakout_4pct, B_tv_ep9m, D_tv_gap_10pct, G_peoplewish, H_hernandez_theme, TV_volume_breakout | `fresh+t1` | 84.78 | **+13.95%** | 5.93 | 20.86 | — | EXTENDED |
| **MOD** | 3 | A_stockbee_4pct, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish | `t1` | 130.55 | **-3.77%** | 7.41 | 4.14 | 40.42 | EXTENDED |

### What Tier-A is saying

**CGON — CG Oncology.** 5 stylists and 7 origins: the widest convergence in the book, and the only Tier-A name carried by all four TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout). It closed **+13.95%** on 6.25x relative volume, and its 14-day velocity of 20.86 is the highest of any candidate. The label says EXTENDED on two rules — **25.71% above its 20-DMA** (99.8th percentile of the $10B+ set) and ATR 6.44% (92.2). Overlay: negative FCF yield (-2.87%) and no trailing P/E (price/sales 1,069x) → `valuation_gate: fail`, severity `watch`.

**CBRS — Cerebras Systems.** 3 stylists, but today it failed: **-7.11%** on the settled close, and the only fresh origin it has is the EP9M volume gate (its T+1 close was 108.72 against today's 100.99). ATR **11.36%** is the 99.0th percentile of the large-cap set — a ~10%-a-day name. Overlay: negative FCF yield, no trailing earnings → `fail` / `watch`.

**MOD.** 3 stylists on T+1 data only: its 40.4% five-session move put it in the parabolic-short book and it closed **-3.77%** today. The overlay is the worst of the three — trailing P/E **55.5** and negative FCF yield → `fail` / **`flagged`** (2 flags).

**What Tier-A is not saying.** All three names are extended, all three fail the overlay, and one of the three is a stale row that describes 2026-11-13 rather than today. A 3-name Tier-A drawn from a 1,163-name book on 43.93% breadth is a thin book — size to that, not to the 5-stylist headline on CGON.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 3 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| CBRS | 11.36 | 99.0 | -2.75 | no |
| CGON | 6.44 | 92.2 | 25.71 | yes |
| MOD | 9.25 | 97.4 | 5.82 | no |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **ALM** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 8.15 | **-0.85%** | 1.17 | 9.39 | 37.3 | 7.54 |
| **ALNY** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 159.73 | **-3.22%** | 0.63 | 6.49 | 32.5 | 5.26 |
| **CBRS** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 100.99 | **-7.11%** | 1.03 | 11.36 | 40.9 | 9.10 |
| **CGON** | 5 | A_stockbee_4pct, A_tv_breakout_4pct, B_tv_ep9m, D_tv_gap_10pct, G_peoplewish, H_hernandez_theme, TV_volume_breakout | `fresh+t1` | 84.78 | **+13.95%** | 6.25 | 6.44 | 71.6 | 5.93 |
| **CPRI** | 2 | A_stockbee_4pct, C_qullamaggie_rs | `t1` | 20.55 | **-4.24%** | 0.82 | 4.59 | 62.4 | 4.51 |
| **FENC** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, TV_volume_breakout | `fresh+t1` | 12.76 | **+9.81%** | 3.50 | 6.10 | 68.7 | 6.85 |
| **FOUR** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 42.48 | **-5.14%** | 0.65 | 6.20 | 52.5 | 5.68 |
| **MOD** | 3 | A_stockbee_4pct, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish | `t1` | 130.55 | **-3.77%** | 0.73 | 9.25 | 49.7 | 7.41 |
| **SENS** | 2 | A_stockbee_4pct, TV_volume_breakout | `fresh+t1` | 10.90 | **+3.02%** | 2.09 | 8.80 | 64.1 | 9.82 |
| **TNDM** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 18.48 | **-7.92%** | 0.82 | 7.62 | 51.8 | 6.63 |
| **U** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 51.88 | **-1.76%** | 0.54 | 5.20 | 67.6 | 5.38 |
| **VKTX** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 26.80 | **-8.28%** | 0.84 | 7.07 | 46.9 | 6.03 |

Nine of the 12 Focus names closed lower; only **CGON (+13.95%)**, **FENC (+9.81%)** and **SENS (+3.02%)** were green. Seven of the 12 are T+1-only rows (ALM, ALNY, CPRI, FOUR, MOD, TNDM, VKTX) — their screen metrics describe 2026-11-13, so they are prior-session context, not today's triggers.

The overlay flags **11 of the 12**; **U** is the only name with no red flag, and even it has no reported trailing earnings (`valuation_gate: unknown` — disclosed, not a pass).

The book is a health-care / biotech momentum pocket inside a broadly red tape: the same session that carried MOH +11.27% and CNC +4.91% also printed ASTS -12.33%, ALAB -8.79% and IONQ -8.41%.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 341 | no red flag, and earnings data present |
| `fail` | 598 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 101 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-16

| Metric | Value |
|---|---|
| Universe | 1095 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **43.93%** / 49.77% / 47.49% |
| Advance / decline / unchanged | **297 / 787 / 11** (ratio 0.38) |
| Median name | -0.77% |
| VIX / VIX3M | **22.91 / 23.02** (VIX +18.70% from 19.3) |
| SPY / QQQ / RSP / IWM / QQQE | 739.95 (-1.91%) / 661.75 (-2.67%) / 218.93 (-1.01%) / 272.94 (-1.66%) / 113.42 (-2.09%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| TU | Telus Corporation | 9.57 | **+12.19%** |
| MOH | Molina Healthcare Inc | 233.09 | **+11.27%** |
| HTHT | H World Group Limited | 54.88 | **+8.91%** |
| TSN | Tyson Foods, Inc. | 63.95 | **+8.72%** |
| HUBS | HubSpot, Inc. | 231.98 | **+6.78%** |
| MOG.B | Moog Inc. | 347.00 | **+6.72%** |
| HNGE | Hinge Health, Inc. | 121.29 | **+5.11%** |
| CNC | Centene Corporation | 74.77 | **+4.91%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| ASTS | AST SpaceMobile, Inc. | 28.58 | -12.33% |
| NTRA | Natera, Inc. | 288.48 | -9.59% |
| TEM | Tempus AI, Inc. | 64.76 | -9.55% |
| TSEM | Tower Semiconductor Ltd. | 133.42 | -9.17% |
| ALAB | Astera Labs, Inc. | 202.34 | -8.79% |
| SNDK | Sandisk Corporation | 809.11 | -8.58% |
| LITE | Lumentum Holdings Inc. | 546.00 | -8.48% |
| IONQ | IonQ, Inc. | 26.45 | -8.41% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (6):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| AAON | 40.32 | 7.60 | 78.20 | -2.55% |
| FRMI | 66.24 | 13.96 | 2.48 | -4.98% |
| FRVO | 27.53 | 9.84 | 10.98 | -4.60% |
| LGN | 25.40 | 9.42 | 34.18 | -2.34% |
| LQDA | 29.30 | 7.34 | 56.37 | -1.81% |
| MOD | 40.42 | 7.41 | 130.55 | -3.77% |

**Long / mean-reversion candidates (4):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| BZ | -26.57 | 3.83 | 12.67 | -2.24% |
| IBRX | -30.28 | 8.07 | 5.98 | -0.66% |
| IONS | -26.28 | 5.01 | 28.01 | -3.61% |
| LEGN | -25.21 | 6.38 | 15.99 | -8.63% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

Theme ranking puts **XLV** first (composite 1M/3M/6M RS +5.4 / +11.4 / +27.3 = 44.2), **IBB** second (29.1) and **XLP** third (22.2) — Health Care and Consumer Staples, two defensive buckets, are the strongest groups on the tape. The theme → group → leaders branch then picks names inside those GICS buckets: **REPL** (1M RS +82.5), **SGRY** (+80.3), **XERS** (+66.3), **LQDA** (+62.1), **AXGN** (+55.4), **VRDN** (+51.5) — and **CGON** at +37.1, the only one of them whose origin is the fresh book.

The industry table in `breadth.md` corroborates: Managed Health Care is **83.3%** above its 20-DMA and averaged **+4.12%** today, the strongest group in the universe, while Semiconductors are **15.2%** above and averaged **-5.45%**.

## Method, source health & caveats

- **TradingView scanner (post-close)** — fresh book 3,764 names (`totalCount` 3,764 = rows fetched), breadth universe 1,095 names (`totalCount` 1,095). No truncation on either scan.
- **shibui over the MCP-over-HTTP bridge** — the 9 screen branches, the CANSLIM growth half and the valuation/quality overlay (1,040 symbols). The screen session resolved to **2026-11-13** (T+1, published as `screen_data_date`).
- **Cboe delayed-quote CDN** — VIX/VIX3M, pulled twice 5 s apart and identical both times (`vix_stable: true`).
- **bridge market-recap** — the official 16:00 ET prints for the book names (`same-day-prints.md`).
- No source was degraded, blocked or rate-limited: **errors: 0**.

- **Dual book, never blended.** TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on the cron day's own settled bar (2026-11-16); multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session (2026-11-13). Every row carries `data_as_of` + `source` (`fresh` / `t1` / `fresh+t1`).
- **Coverage assertion: 9/9 branches complete** — `rows_kept == rows_passing` on every branch, and no branch count lands on a cap (30 / 50 / 60 / 200).
- **Breadth universe:** NYSE/NASDAQ/AMEX, type in {stock, dr}, `market_cap_basic` > $10B, TradingView scanner in USD — **1,095 names**, and `totalCount` 1,095 equals the rows fetched, so the scan is not truncated. The advance/decline tally uses the same population (297 + 787 + 11 = 1,095).
- **Source of record for the settled layer:** the TradingView scanner's post-close `close`, which is the official 16:00 ET print. Nasdaq's `primaryData` is the after-hours last trade and is deliberately not used in an end-of-day artifact.
- **One volatility pair** (VIX 22.91 / VIX3M 23.02, Cboe delayed-quote CDN, quoted 2026-11-16 16:15:01 ET, pulled twice 5 s apart and identical — `vix_stable: true`) is used everywhere in both artifacts; no mid-session print is mixed with the settle. Ratio 0.9952 → `uncertainty: false`; `atr_extensions` carries all five index ETFs, so `late_cycle` was genuinely computed (`false`).
- **Caveat on the divergence.** `breadth_divergence` +43.93 pp reads BROAD because the five index ETFs are 0/5 above their 20-DMA — RSP sits 0.0007% below its own 20-DMA (218.93 close vs a 218.9315 average), so that count is one tick deep. The band identifies the INDEX as the weak leg; it is not a statement that the average stock is healthy.
- **The overlay is a LABEL, not a filter.** A missing trailing P/E is published as `earnings_data_missing` with `valuation_gate: unknown` — never as a red flag and never as a pass. Nothing is dropped from the book for tripping a rule.
- **Settled vs live:** this directory holds three reads and they are not blended — the end-of-day breadth (`breadth.md`, 2026-11-16 settle), the intraday counterpart (`breadth-snapshot.md`, cron #10, 14:00 ET) and the T+1 screen metrics in `daily-sweep.md` (shibui 2026-11-13). No degraded probe applies.

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
