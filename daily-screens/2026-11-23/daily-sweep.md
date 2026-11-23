---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "18:30 ET (2026-11-23)"
cron_date: "2026-11-23"
screen_data_date: "2026-11-20 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-23 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-23 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 50, uncertainty: true, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 31.5}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Monday 23 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-23's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-20**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **A violent relief bounce, not a repair.** Nvidia's board reinstated Jensen Huang as CEO in an 8-K before the bell, and the AI complex snapped back hard: NVDA **+31.48%** to 165.05 on 779M shares, QQQ **+7.00%**, SPY **+4.71%**, IWM **+3.56%**, RSP **+2.59%**. Participation was broad in the tape — **924 advancing / 141 declining / 5 unchanged** on the 1,070-name $10B+ universe, median name **+2.34%** — and VIX collapsed to **26.62** from 35.89 (**-25.8%**).
- **The trend structure did not come with it.** Not one of the five index ETFs is above its own 20-DMA, only **31.50%** of the large-cap universe is above its 20-DMA, and QQQ is still **-8.28%** below its 50-DMA (it was -14.42% on the 2026-11-20 screen session). Regime stays defensive: `size_cut_pct` **50** (size cut ON), `index_below_20sma` **true**, `uncertainty` **true** (VIX/VIX3M = 1.0439), `late_cycle` **false**.
- **Tier-A is 4 names — INTC, IREN, NVDA, SNDK — and every one is a washout bounce, not a continuation.** All four are still below their own 20-DMA (-5.84%, -27.21%, -7.75%, -26.49%), and all four trip the extension label on ATR% alone: **0 fresh / 4 extended**. "Three stylists agree" here means the same high-beta washout was counted three times, not that three independent screens found a leader.
- **The book is a mean-reversion book, and it says so.** 47 long/mean-reversion candidates (5-session -25%+) against only **3** parabolic-short candidates (+25%+). Today's leaders were the highest-beta damage: Semiconductors averaged **+14.01%** today while only **15.15%** of them sit above their 20-DMA. Managed health care (-1.33%), oil & gas production (-1.77%) and food retail (-1.88%) went the other way — the tape paid for last week's damage and nothing more.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **50** (size cut is ON - the index is below its 20-DMA and breadth 31.50% is UNDER the 40% trigger) |
| `uncertainty` | **true** (VIX 26.62 / VIX3M 25.5 = 1.0439) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at -0.90%) |
| `index_below_20sma` | **true** (0 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+31.5 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-23** — the cron day's settled bar | `A_tv_breakout_4pct` 610 · `B_tv_ep9m` 242 · `D_tv_gap_10pct` 160 · `TV_volume_breakout` 184 | 817 |
| **T+1** (cross-check) | **2026-11-20** — shibui's newest ingested session | 9 branches | 1190 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 530 |
| `t1` | context screens only | 660 |
| `fresh` | trigger screens only | 287 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 20 | 20 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 282 | 282 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 446 | 446 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 29 | 29 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 0 | 0 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 3 | 3 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 47 | 47 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 387 | 387 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 44 | 44 | complete |

Total screened rows **1258** across the 9 branches → **1477 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (4 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **INTC** | 3 | A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, G_peoplewish | `fresh+t1` | 59.66 | **+16.34%** | 6.18 | -14.49 | — | EXTENDED |
| **IREN** | 3 | A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, F_qullamaggie_5d_losers, G_peoplewish | `fresh+t1` | 14.64 | **+23.86%** | 10.91 | -46.32 | -34.95 | EXTENDED |
| **NVDA** | 4 | A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, G_peoplewish, TV_volume_breakout, jeff_sun_canslim | `fresh+t1` | 165.05 | **+31.48%** | 5.38 | -37.87 | — | EXTENDED |
| **SNDK** | 3 | B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, F_qullamaggie_5d_losers, G_peoplewish | `fresh+t1` | 87.71 | **+10.69%** | 9.06 | -41.04 | -28.37 | EXTENDED |

### What Tier-A is saying

- **NVDA — 4 stylists, +31.48% to 165.05.** The session itself: the catalyst is the board's reinstatement of Jensen Huang (8-K pre-bell), and it is the single largest one-day market-cap gain on record. Volume 779M shares, RVOL 1.78. But the trend is not repaired — still **-7.75%** below its own 20-DMA and **-19.91%** below its 50-DMA, and the extension label fires on ATR% 8.01% only. The quality overlay is `fail` on shibui's own `earnings_quality_flags`, **not** on the multiples: trailing P/E 15.75, PEG 0.15, FCF yield 4.18%, debt/equity 0.17. Highest-conviction name in the book, and it is a relief bounce on a leadership decision, not a new trend.
- **IREN — 3 stylists, +23.86% to 14.64.** The most violent and the most damaged. ATR% **18.03**, **-27.21%** below its 20-DMA, **-51.94%** below its 50-DMA, 14-day velocity **-46.32%**, 5-session move `m1` **-34.95%**. It is in the **long / mean-reversion** book, not the momentum book — it is a dead-cat-bounce candidate. Worst quality on the sheet: FCF yield **-135.7%** and debt/equity **2.00** → `flagged`.
- **SNDK — 3 stylists, +10.69% to 87.71.** The cleanest balance sheet in Tier-A — trailing P/E 4.78, PEG 0.01, FCF yield 18.71%, debt/equity 0.00 → `pass`, the only Tier-A name with no red flag. It is also the most broken technically: **-26.49%** below its 20-DMA, **-47.18%** below its 50-DMA, `m1` -28.37%. **RVOL 0.99 — the bounce had no volume expansion at all.**
- **INTC — 3 stylists, +16.34% to 59.66.** Gapped +10% and extended. ATR% 9.16, RSI 39.90, **-33.32%** below its 50-DMA, 14-day velocity -14.49%. Quality `fail` on operating P/E **146.8**; trailing P/E is missing and is therefore **disclosed, not counted as a flag** (`valuation_gate: fail` on the one value that exists).
- **What the tier is really saying:** all four names are below their own 20-DMA and all four carry the extension label for the same reason (ATR% alone). Six of the suite's branches are momentum/breakout/velocity screens, so on a washout-rebound day they all fire on the same names. Tier-A is measuring agreement among correlated momentum screens, so read the tier as *where the beta was*, not as *four independent setups*.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 4 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| INTC | 9.16 | 96.6 | -5.84 | no |
| IREN | 18.03 | 99.9 | -27.21 | no |
| NVDA | 8.01 | 95.2 | -7.75 | no |
| SNDK | 15.05 | 99.9 | -26.49 | no |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **ANT** | 2 | B_stockbee_ep9m, G_peoplewish | `t1` | 87.64 | **-1.43%** | — | — | — | 16.86 |
| **CBLL** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, TV_volume_breakout | `fresh+t1` | 29.29 | **+6.94%** | 2.64 | 4.88 | 63.6 | 5.31 |
| **GPN** | 2 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish | `t1` | 91.47 | **-0.39%** | 0.88 | 4.90 | 52.2 | 5.40 |
| **HTFL** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 48.31 | **+3.47%** | 0.91 | 7.42 | 44.2 | 6.74 |
| **INTC** | 3 | A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, G_peoplewish | `fresh+t1` | 59.66 | **+16.34%** | 1.37 | 9.16 | 39.9 | 6.18 |
| **IREN** | 3 | A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, F_qullamaggie_5d_losers, G_peoplewish | `fresh+t1` | 14.64 | **+23.86%** | 1.39 | 18.03 | 33.5 | 10.91 |
| **KVYO** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, G_peoplewish | `fresh+t1` | 23.30 | **+4.77%** | 1.09 | 5.23 | 66.2 | 5.58 |
| **NOK** | 2 | A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct | `fresh+t1` | 7.55 | **+9.74%** | 1.23 | 6.34 | 41.1 | 4.22 |
| **NTLA** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 10.15 | **+1.50%** | 1.51 | 8.49 | 42.3 | 7.69 |
| **NVDA** | 4 | A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, G_peoplewish, TV_volume_breakout, jeff_sun_canslim | `fresh+t1` | 165.05 | **+31.48%** | 1.78 | 8.01 | 42.9 | 5.38 |
| **PLMR** | 2 | A_stockbee_4pct, jeff_sun_canslim | `t1` | 164.44 | **+0.52%** | 1.08 | 3.38 | 70.7 | 3.51 |
| **SNDK** | 3 | B_stockbee_ep9m, B_tv_ep9m, D_tv_gap_10pct, F_qullamaggie_5d_losers, G_peoplewish | `fresh+t1` | 87.71 | **+10.69%** | 0.99 | 15.05 | 31.0 | 9.06 |

- **12 names, of which 4 are Tier-A.** The eight non-Tier-A names: **ANT** -1.43% (T+1 only — Anthropic is still digesting its record IPO debut), **CBLL** +6.94% (RVOL 2.64, RSI 63.59, +8.51% above its 20-DMA), **GPN** -0.39%, **HTFL** +3.47%, **KVYO** +4.77% (+9.08% above its 20-DMA, +23.68% above its 50-DMA, but trailing P/E **799** and PEG **32.6** → `flagged`), **NOK** +9.74% (gapped +10% then extended; no trailing earnings → `valuation_gate: unknown`), **NTLA** +1.50%, **PLMR** +0.52% (RSI 70.74, +16.90% above its 50-DMA, quality `pass`).
- **The two healthiest names in Focus barely moved.** CBLL and PLMR are the only Focus names with their trend structure intact, and they closed +6.94% and +0.52%. Every large Focus gainer is a name that was just crushed — the book is ordered by how much damage was repaired, not by how strong the structure is.
- **Concentration:** 5 of the 12 Focus names are semiconductor/AI hardware or memory (INTC, IREN, NVDA, SNDK, NOK). The Focus list is a single-factor list today: high-beta AI hardware mean-reversion.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 321 | no red flag, and earnings data present |
| `fail` | 598 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 83 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-23

| Metric | Value |
|---|---|
| Universe | 1070 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **31.50%** / 42.06% / 41.03% |
| Advance / decline / unchanged | **924 / 141 / 5** (ratio 6.55) |
| Median name | +2.34% |
| VIX / VIX3M | **26.62 / 25.5** (VIX -25.83% from 35.89) |
| SPY / QQQ / RSP / IWM / QQQE | 722.29 (+4.71%) / 651.03 (+7.00%) / 212.82 (+2.59%) / 265.74 (+3.56%) / 110.62 (+4.94%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| NVDA | NVIDIA Corporation | 165.05 | **+31.48%** |
| KYMR | Kymera Therapeutics, Inc. | 150.37 | **+30.40%** |
| ALAB | Astera Labs, Inc. | 222.12 | **+23.16%** |
| CRDO | Credo Technology Group Holding Ltd | 122.46 | **+22.63%** |
| CRWV | CoreWeave, Inc. | 48.33 | **+22.32%** |
| SITM | SiTime Corporation | 438.82 | **+21.48%** |
| ASX | ASE Technology Holding Co., Ltd. | 31.88 | **+21.36%** |
| DELL | Dell Technologies Inc. | 334.91 | **+20.46%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| CRWD | CrowdStrike Holdings, Inc. | 208.97 | -8.92% |
| WSO.B | Watsco, Inc. | 296.40 | -5.38% |
| TU | Telus Corporation | 10.50 | -5.15% |
| VOD | Vodafone Group Plc | 13.38 | -4.56% |
| IP | International Paper Company | 28.98 | -4.55% |
| BURL | Burlington Stores, Inc. | 235.16 | -4.15% |
| ELV | Elevance Health, Inc. | 379.55 | -3.78% |
| BF.A | Brown Forman Inc | 29.61 | -3.68% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (3):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| BRBR | 37.97 | 6.49 | 15.22 | +4.46% |
| SLS | 73.79 | 13.79 | 13.28 | -2.78% |
| TU | 29.78 | 3.13 | 10.50 | -5.15% |

**Long / mean-reversion candidates (47):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| AAOI | -33.99 | 11.45 | 38.70 | +17.52% |
| ACHR | -27.79 | 8.57 | 3.07 | +5.50% |
| AEHR | -30.08 | 11.65 | 48.51 | +21.76% |
| APLD | -28.05 | 9.54 | 13.82 | +20.28% |
| ASST | -32.07 | 8.84 | 15.47 | +6.62% |
| ASTS | -28.62 | 11.06 | 25.67 | +10.31% |
| ASX | -26.10 | 6.18 | 31.88 | +21.36% |
| AVAV | -26.15 | 7.12 | 90.67 | +4.47% |
| AXTI | -26.94 | 12.60 | 38.02 | +24.37% |
| BE | -25.83 | 9.43 | 168.15 | +18.04% |
| BETA | -26.58 | 8.45 | 16.59 | -3.15% |
| BMNR | -26.17 | 7.28 | 14.42 | +11.09% |
| BTDR | -47.23 | 13.03 | 3.39 | +14.72% |
| CLSK | -26.47 | 10.16 | 5.53 | +13.09% |
| CRWV | -25.64 | 10.43 | 48.33 | +22.32% |
| EXK | -25.72 | 5.57 | 6.13 | +8.11% |
| FLY | -29.83 | 10.29 | 19.14 | +8.20% |
| FRMI | -25.29 | 16.23 | 2.10 | +7.69% |
| GDS | -32.71 | 6.95 | 15.12 | +13.43% |
| HIMS | -26.00 | 8.30 | 15.06 | +3.15% |
| INFQ | -25.47 | 8.27 | 6.75 | +6.80% |
| IONQ | -28.25 | 8.69 | 23.34 | +12.64% |
| IREN | -34.95 | 10.91 | 14.64 | +23.86% |
| JOBY | -29.13 | 7.15 | 3.85 | +6.65% |
| KEEL | -26.08 | 10.47 | 1.60 | +16.36% |
| KRMN | -28.06 | 9.23 | 30.32 | +3.66% |
| LUNR | -32.50 | 10.15 | 9.75 | +11.11% |
| MARA | -27.25 | 9.32 | 5.58 | +9.73% |
| MSTR | -30.30 | 6.31 | 84.40 | +8.48% |
| MXL | -25.69 | 10.15 | 50.31 | +21.38% |
| NBIS | -29.83 | 10.36 | 97.80 | +20.28% |
| NVTS | -32.07 | 9.00 | 7.33 | +20.56% |
| NXT | -29.36 | 7.76 | 70.58 | +5.13% |
| ONDS | -27.13 | 8.75 | 4.03 | +7.18% |
| OUST | -28.91 | 8.64 | 27.90 | +17.23% |
| QBTS | -31.80 | 8.73 | 7.31 | +12.12% |
| RDW | -26.91 | 8.89 | 6.42 | +13.63% |
| REAL | -25.81 | 7.14 | 11.74 | +8.91% |
| RGTI | -25.57 | 9.02 | 8.10 | +13.06% |
| RKLB | -26.18 | 8.81 | 49.63 | +9.27% |
| SHAZ | -25.40 | 14.03 | 19.41 | +15.33% |
| SMMT | -29.68 | 8.76 | 10.32 | +3.72% |
| SMR | -27.90 | 8.98 | 3.53 | +5.06% |
| SNDK | -28.37 | 9.06 | 87.71 | +10.69% |
| SNEX | -36.02 | 4.99 | 39.48 | +7.81% |
| SOUN | -25.21 | 6.55 | 2.90 | +10.92% |
| TE | -42.41 | 14.55 | 1.20 | +9.09% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

The theme → group → leaders branch picked **XLV, IBB, XLP** (Health Care + Consumer Staples) from a 147-name pool, publishing 44 names. Two things the reader should know: (1) this branch is **T+1** (shibui's 2026-11-20 session), so it is a **pre-bounce** snapshot — it reflects the relative strength of defensives *after* last week's crash and *before* today's rebound; (2) today's tape was the opposite of what this branch says. Semiconductors averaged **+14.01%** and led the tape, while managed health care averaged **-1.33%** and the staples/retail complex was negative. Read the theme branch as the book that was working into the washout, not as a description of today's leadership. The themes are sector ETFs only — a single stock with strong relative strength (as SKY did on 2026-11-10) cannot displace a real sector theme.

## Method, source health & caveats

### Source health

| Source | What it served | Status |
|---|---|---|
| TradingView scanner (`scanner.tradingview.com/america/scan`) | the fresh book (3,708 names; `totalCount` 3,708 = rows fetched, no truncation) and the settled breadth read (1,070 names, $10B+) | **ok** |
| MCP bridge `market-recap` `get_quotes` | the official 16:00 ET close for the book names (66 symbols, 2 batched calls); every quote cross-checked against a second feed — `agreement: agrees`, `difference_pct` 0.00 | **ok** |
| MCP bridge `shibui` `stock_data_query` | the 8 T+1 context branches, the CANSLIM growth half and the merged enrichment pass; newest ingested session **2026-11-20** (T+1 — one session behind the cron day) | **ok** (lag disclosed, not blended) |
| Yahoo chart API (`^VIX` / `^VIX3M`) | the volatility pair, both symbols from the same 2026-11-23 session bar, quoted 16:15:01 ET | **ok** — *fallback* |
| Cboe delayed-quote CDN | the primary volatility source | **failed: HTTP 403 (Cloudflare)** — the Yahoo fallback served the pair |
| Web search (Investopedia / Benzinga / AP / Barron's) | the day's catalyst only (Nvidia's 8-K reinstating Jensen Huang as CEO) | **ok** — no published number comes from it |

**Degraded sources: 1** — the Cboe delayed-quote CDN (HTTP 403). The volatility pair was published from the Yahoo fallback instead, and the `source` string names it.

### Method

- **The dual book.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) ran on **2026-11-23's own settled bar** from the TradingView scanner. The multi-session CONTEXT screens (5-day gainers/losers, the 14-day velocity, the coil, the 252-session RS window) stay on shibui's **2026-11-20** session and are labelled T+1. Every row publishes `data_as_of` + `source` (`fresh` / `t1` / `fresh+t1`); the two are never blended.
- **Volume basis.** The scanner publishes no prior-session volume, so the expansion test runs against the prior-**nine**-session mean, reconstructed as `(10 × average_volume_10d_calc − volume_today) / 9` — a stricter gate than shibui's "volume > prev_session", published as its own gate. The 5-session move stays on shibui's `m1` because TradingView's `Perf.W` is a **six**-session measure (r = 0.997 against a six-session move, 0.924 against five).
- **Close convention.** The official 16:00 ET print. TradingView's `close` equals Nasdaq's `secondaryData`; `primaryData` is the after-hours print and is **not** used.
- **Coverage.** 1,952 screened rows across 9 branches → 1,477 distinct candidates. `rows_kept == rows_passing` on all nine branches; no branch landed on 30 / 50 / 60 / 200, so no book was truncated.
- **Quality overlay.** 1,002 symbols queried; 598 `fail`, 321 `pass`, 83 `unknown` (no trailing earnings — **disclosed, not counted as a red flag**), 475 with no overlay row. A flag never removes a name from the book.

### Caveats

- **A bounce is not a trend repair.** 31.50% above the 20-DMA with 0 of 5 index ETFs above theirs is the honest state of the tape after a violent relief rally; the size-cut flag is ON for that reason.
- **The catalyst is single-stock.** One 8-K from one board produced a large share of today's index move. Any read of today's tape is heavily conditioned on it.
- **Not verified:** no intraday path, no option-chain or flow confirmation, and no independent per-name catalyst check for the Focus names — the theme branch's leader selection is published as-is from the screen.
- **The screen's context numbers are one session stale** (shibui 2026-11-20). The fresh book is the primary; the T+1 book is the cross-check, and where they disagree the artifact publishes both rather than substituting one.

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
