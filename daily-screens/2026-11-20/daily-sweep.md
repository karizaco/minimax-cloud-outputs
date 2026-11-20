---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "18:30 ET (dispatched 18:30:04 ET)"
cron_date: "2026-11-20"
screen_data_date: "2026-11-19 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-20 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-20 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 50, uncertainty: true, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 14.94}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Friday 20 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-20's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-19**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **An AI-led liquidation, and the suite's own regime flags say so.** The S&P 500 fell **3.70% to 6,910.39** — a seventh straight down day and the first close in correction territory — the Nasdaq Composite dropped **5.28%** and turned negative for 2026, and the PHLX Semiconductor index lost **10.73%**. The volatility pair closed at **VIX 35.89 / VIX3M 30.94 (ratio 1.16, inverted)**, so `uncertainty: true`, `index_below_20sma: true` (0 of 5 index ETFs above their 20-DMA) and the **size cut is ON** at 50. Inside the $10B+ universe only **14.94%** of names sit above their 20-DMA, with **211 advancing against 844 declining**.
- **What the TRIGGER screens actually caught on today's settled bar** (the fresh book, 2026-11-20): 22 names broke out 4%+ on the day — **EVH +13.7%** (Truist upgraded to Buy, price target $6), **GAP +11.4%** (Q3 adjusted EPS beat), **PSQL +10.0%**, **GPN +9.95%**, **EFOR +7.9%**, **EVCM +7.2%**, **BKE +5.7%** (strong Q3), **NTLA +5.0%** — while the defensive rotation showed up in the theme branch (ARDT +4.0%, CALM +3.5%, IPAR +3.4%, HRL +2.1%, TSN +2.0%, CPB +1.8%).
- **The caveat that changes how the book reads: all four Tier-A names are T+1 names.** They are 2026-11-19's strength, not today's — and every one of them fell into the close: **INSM -2.17%** (after +20.6% on Thursday, when Bloomberg reported Sanofi is considering acquiring it), **OKTA -7.44%**, **VRDN -4.71%**, **NTSK -3.51%**. The 53 names carried by **today's** bar alone, and the 22 four-percent breakouts above, are the only parts of this book that describe the session the trader just saw.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **50** (size cut is ON - the index is below its 20-DMA and breadth 14.94% is UNDER the 40% trigger) |
| `uncertainty` | **true** (VIX 35.89 / VIX3M 30.94 = 1.1600) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at -3.43%) |
| `index_below_20sma` | **true** (0 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+14.9 pp — MATCHED** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-20** — the cron day's settled bar | `A_tv_breakout_4pct` 22 · `B_tv_ep9m` 288 · `D_tv_gap_10pct` 0 · `TV_volume_breakout` 31 | 314 |
| **T+1** (cross-check) | **2026-11-19** — shibui's newest ingested session | 9 branches | 1067 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 261 |
| `t1` | context screens only | 806 |
| `fresh` | trigger screens only | 53 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 41 | 41 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 224 | 224 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 506 | 506 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 45 | 45 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 0 | 0 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 4 | 4 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 18 | 18 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 368 | 368 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 32 | 32 | complete |

Total screened rows **1238** across the 9 branches → **1120 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (4 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **INSM** | 4 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme | `t1` | 141.33 | **-2.17%** | 5.08 | 28.32 | — | EXTENDED |
| **NTSK** | 3 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, G_peoplewish | `t1` | 23.93 | **-3.51%** | 8.01 | 2.06 | — | EXTENDED |
| **OKTA** | 3 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish | `t1` | 191.46 | **-7.44%** | 6.97 | -0.67 | — | EXTENDED |
| **VRDN** | 4 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme | `t1` | 29.96 | **-4.71%** | 5.06 | 27.44 | — | — |

### What Tier-A is saying

All four Tier-A names come from the **T+1 book** (`source: t1`, data_as_of 2026-11-19). The trigger screens that run on the cron day's own settled bar produced **no** name with three or more stylists — so Tier-A is a list of what was strong *yesterday*, and every one of these four fell into today's close.

| Name | Stylists | Today's move | What actually happened |
|---|---|---|---|
| **INSM** | 4 | **-2.17%** | +20.6% on Thursday 2026-11-19 on the Bloomberg report that **Sanofi is considering an acquisition**; the position was carried into a -3.6% index day |
| **NTSK** | 3 | **-3.51%** | security-software peer of OKTA/PANW, caught in the same unwind; `free_cash_flow_yield`, `debt_to_equity` flags |
| **OKTA** | 3 | **-7.44%** | bid up with PANW on the outage-driven cybersecurity trade (OKTA +12.1% on Wed 2026-11-18) — then given back with the tape; flags `trailing_pe`, `operating_pe`, `trailing_revenue_peg` |
| **VRDN** | 4 | **-4.71%** | the **only** Tier-A name that is not extended; flags `free_cash_flow_yield`; no company release sourced for today |

**The extension split is 1 fresh / 3 extended** (VRDN fresh; INSM, NTSK, OKTA extended — INSM on being 22.78% above its 20-DMA, NTSK and OKTA on ATR% of 7.52% and 7.40%). Read the tier as a *convergence* signal on the previous session, not as a buy list for this one; on a tape like this, a three-stylist agreement built on yesterday's momentum is exactly the cohort the fresh book shows getting sold (see the Focus notes).

### The extension label — the honest answer to "have these already run?"

**Tier-A is 1 fresh / 3 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| INSM | 4.80 | 81.1 | 22.78 | yes |
| NTSK | 7.52 | 93.4 | 3.31 | no |
| OKTA | 7.40 | 93.1 | -0.66 | no |
| VRDN | 4.57 | 79.5 | 6.48 | no |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **AMBA** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 53.07 | **-9.94%** | 1.98 | 7.95 | 38.2 | 5.80 |
| **DPC** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 30.74 | **-10.06%** | 1.00 | 9.53 | 47.2 | 8.56 |
| **INSM** | 4 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme | `t1` | 141.33 | **-2.17%** | 1.74 | 4.80 | 73.2 | 5.08 |
| **IVR** | 2 | A_stockbee_4pct, B_tv_ep9m, TV_volume_breakout | `fresh+t1` | 5.38 | **+3.26%** | 1.90 | 3.71 | 50.1 | 3.46 |
| **NTSK** | 3 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, G_peoplewish | `t1` | 23.93 | **-3.51%** | 1.09 | 7.52 | 57.5 | 8.01 |
| **NUAI** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs | `fresh+t1` | 3.78 | **-11.68%** | 1.34 | 13.89 | 55.0 | 15.84 |
| **OKTA** | 3 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish | `t1` | 191.46 | **-7.44%** | 1.00 | 7.40 | 49.6 | 6.97 |
| **P** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 92.05 | **-12.75%** | 1.18 | 10.56 | 35.3 | 7.54 |
| **PANW** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 343.32 | **-5.09%** | 1.52 | 6.01 | 48.8 | 5.39 |
| **PURR** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 7.48 | **-10.95%** | 1.50 | 11.30 | 36.2 | 7.90 |
| **TU** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, E_qullamaggie_5d_gainers | `fresh+t1` | 11.07 | **+2.69%** | 1.19 | 3.63 | 74.8 | 3.10 |
| **VRDN** | 4 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme | `t1` | 29.96 | **-4.71%** | 0.66 | 4.57 | 64.0 | 5.06 |

**Ten of the twelve Focus names fell**, and the two that rose are the exceptions rather than the story. The screen's own cohort is concentrated in the complex that broke: NUAI **-11.68%**, PURR **-10.95%**, DPC **-10.06%**, AMBA **-9.94%**, PANW **-5.09%**, OKTA **-7.44%**, P **-12.75%**, plus INSM, NTSK, VRDN above. The only risers are **IVR +3.26%** and **TU +2.69%** (TELUS, a Canadian telecom — a defensive holding in a risk-off tape).

That is the honest shape of a momentum book on a -3.6% day: the screen selects strength, and strength is what gets sold first when the AI trade unwinds. Two names are worth separating out because their move has a sourced reason rather than a flow explanation — **IVR** (a fresh-book name that broke out with volume on the day) and **TU**, which also carries the parabolic-short branch (`m1` +26.53%) and is the one name in Focus that is both a momentum leader and a defensive sector.

For the record, the fresh book's own downside cohort is the AI-datacenter and crypto-infrastructure complex: **CSIQ -24.94%**, **MARA -18.57%**, **SVRA -18.23%**, **IREN -17.97%**, **APLD -17.81%**, **HUT -17.65%**, **AAOI -16.55%**, **CLSK -16.27%** — every one of them also a `B_tv_ep9m` name. The screen did not miss them: it flagged them on the 2026-11-19 session and they are now the book's largest losses.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 346 | no red flag, and earnings data present |
| `fail` | 598 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 91 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-20

| Metric | Value |
|---|---|
| Universe | 1064 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **14.94%** / 32.61% / 36.00% |
| Advance / decline / unchanged | **211 / 844 / 9** (ratio 0.25) |
| Median name | -1.40% |
| VIX / VIX3M | **35.89 / 30.94** (VIX +26.20% from 28.44) |
| SPY / QQQ / RSP / IWM / QQQE | 689.81 (-3.64%) / 608.45 (-5.67%) / 207.44 (-1.98%) / 256.61 (-2.88%) / 105.41 (-4.08%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| GPN | Global Payments Inc. | 91.83 | **+9.95%** |
| BIP | Brookfield Infrastructure Partners LP Limite | 42.94 | **+4.54%** |
| HDB | HDFC Bank Limited | 27.42 | **+4.50%** |
| RKT | Rocket Companies, Inc. | 13.75 | **+4.25%** |
| MKC.V | McCormick & Company, Incorporated | 47.64 | **+3.79%** |
| GIS | General Mills, Inc. | 35.74 | **+3.65%** |
| RCI | Rogers Communication, Inc. | 35.45 | **+3.44%** |
| MKC | McCormick & Company, Incorporated | 47.40 | **+3.43%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| NBIS | Nebius Group N.V. | 81.31 | -16.11% |
| CLS | Celestica, Inc. | 201.63 | -16.07% |
| SNDK | Sandisk Corporation | 79.24 | -16.05% |
| BE | Bloom Energy Corporation | 142.45 | -15.26% |
| CRDO | Credo Technology Group Holding Ltd | 99.86 | -15.20% |
| SKM | SK Telecom Co., Ltd. | 26.99 | -14.83% |
| ALAB | Astera Labs, Inc. | 180.35 | -14.77% |
| ARM | Arm Holdings plc | 152.20 | -14.09% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (4):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| BRBR | 47.56 | 6.28 | 14.57 | -3.57% |
| MOD | 26.82 | 7.77 | 124.67 | -7.35% |
| SLS | 85.06 | 13.35 | 13.66 | -8.08% |
| TU | 26.53 | 3.10 | 11.07 | +2.69% |

**Long / mean-reversion candidates (18):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| AAOI | -25.34 | 10.99 | 32.93 | -16.55% |
| ACHR | -26.10 | 8.35 | 2.91 | -9.06% |
| ASST | -25.35 | 8.32 | 14.51 | -12.64% |
| ASTS | -25.94 | 10.80 | 23.27 | -8.92% |
| BETA | -25.16 | 8.27 | 17.13 | -9.03% |
| BTDR | -44.37 | 12.51 | 2.96 | -13.34% |
| FCEL | -25.95 | 9.08 | 6.69 | -11.86% |
| GDS | -26.38 | 6.60 | 13.33 | -9.69% |
| HTFL | -25.52 | 6.65 | 46.69 | +4.62% |
| IONQ | -26.41 | 8.34 | 20.72 | -8.76% |
| IREN | -26.03 | 10.25 | 11.82 | -17.97% |
| JOBY | -26.40 | 6.87 | 3.61 | -8.14% |
| NVTS | -25.00 | 8.42 | 6.08 | -15.20% |
| QBTS | -25.71 | 8.28 | 6.52 | -10.81% |
| QNT | -25.36 | 9.47 | 27.74 | -0.79% |
| SMMT | -29.88 | 8.55 | 9.95 | -5.87% |
| SNEX | -30.92 | 4.60 | 36.62 | -7.16% |
| TE | -34.52 | 13.92 | 1.10 | -14.73% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

The theme branch picked **Health Care (XLV, IBB)** and **Consumer Staples (XLP)** — the only two GICS buckets with positive relative strength on a day when the semiconductor index fell 10.73% and information technology fell 7.11%. The rotation is visible in the leaders' own tape: **ARDT +4.0%**, **CALM +3.5%**, **IPAR +3.4%**, **HRL +2.1%**, **TSN +2.0%**, **CPB +1.8%** on the day, and consumer staples was the **only S&P 500 sector up** (+0.68%) per the session recap. The industry table in `breadth.md` agrees at the group level: Food: Major Diversified 100% above its 20-DMA, Food: Specialty/Candy 85.7%, Hospital/Nursing and Managed Health at 0% but with positive average moves.

Two caveats on the theme. The branch's 32 names are **T+1** (2026-11-19) — the relative-strength ranking is yesterday's, and today's prices merely confirm it. And the theme pool is deliberately **sector ETFs only** (a single stock with a strong RS reading would otherwise displace a real sector), so the book is a *group* read, not a leaderboard: 104 names in the pool, 32 through the branch.

## Method, source health & caveats

**Source health — 2026-11-20 18:30 ET.**

| Source | Query / endpoint | HTTP | Status |
|---|---|---|---|
| TradingView scanner | `POST scanner.tradingview.com/america/scan` — fresh universe (3,711) + breadth universe (1,064) | 200 | ok |
| shibui-finance (bridge) | `stock_data_query` — preflight date resolve, 8 sweep branches, theme, CANSLIM growth, enrichment, overlay | 200 | ok |
| bridge `market-recap` | `get_quotes` — the official 16:00 ET close for the book names | 200 | ok |
| Cboe delayed-quote CDN | `cdn.cboe.com/.../quotes/_VIX.json` | **403** | **failed: Cloudflare block — fell back to the Yahoo chart API** |
| Yahoo chart API | `^VIX` / `^VIX3M`, same session bar, pinned to the cron day | 200 | ok (fallback) |

**Degraded sources: 1** — the Cboe volatility CDN (HTTP 403, Cloudflare). It is the only source that failed; the volatility pair itself was served in full by the Yahoo fallback, and the published `source` string names the fallback so the number is never attributed to Cboe.

**Sources and status for this run.**

| Source | Used for | Status |
|---|---|---|
| TradingView scanner (`scanner.tradingview.com/america/scan`) | the **FRESH** book on the cron day's settled bar (3,711 names, `totalCount` asserted) and the breadth universe (1,064 names) | ok |
| shibui-finance MCP over the HTTPS bridge | the **T+1** context book (screen session **2026-11-19**): 8 sweep branches, the theme branch, the CANSLIM growth half, the enrichment pass, the valuation/quality overlay | ok |
| bridge `market-recap get_quotes` | the official 16:00 ET close for the book names (`market_state: post`) | ok |
| Yahoo chart API (`^VIX`, `^VIX3M`) | the volatility pair | ok — **fallback**, after the Cboe delayed-quote CDN answered HTTP 403 |
| `mcp__*` finance tools | — | **not registered in this runtime** (not an error; the bridge is the path) |

**Method.** The run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-20's own settled bar**; the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-19**. Every row publishes `data_as_of` and `source`, and the two are never blended. The coverage assertion holds on **all 9 branches** (`rows_kept == rows_passing`, no branch landing on a cap of 30/50/60/200), and the fresh universe came back **3,711 of 3,711**.

**Caveats.**
- The screen metrics are **T+1**: every Tier-A and Focus metric describes **2026-11-19**, not the session being reported.
- `valuation_gate: unknown` (91 names) means **no reported trailing earnings** — a disclosure, never a pass and never a red flag. `fail` (598 names) means at least one of: trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, or shibui's own earnings-quality flags.
- The overlay is a **label, not a filter** — nothing is dropped from the book for tripping it.
- Nothing in this book is a recommendation; it is a screen's output with its coverage and its caveats attached.

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
