---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-13 18:31 ET"
cron_date: "2026-11-13"
screen_data_date: "2026-11-12 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-13 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-13 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 0, uncertainty: false, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 52.82}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Friday 13 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-13's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-12**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **Breadth is a coin flip, but the INDEX is the weak leg.** 52.82% of the $10B+ universe closed above its 20-DMA and advances beat declines 579/510 (net +69), yet only **1 of 5** index ETFs is above its 20-DMA and QQQ closed 5.29% below its 50-DMA. Divergence **+32.82pp (BROAD)**: the average large cap is healthier than the headline index — not a megacap-led tape, and not a thrust.
- **The book is broad and mostly already extended.** 1,188 distinct candidates; Tier-A is 5 names (AMD, CHA, DPC, IRTC, LUNR) and **4 of the 5 are EXTENDED** (AMD ATR 7.85% = 95.9th pctile of the $10B+ set; LUNR ATR 9.02% = 97.4th). **CHA is the only Tier-A name that is not extended** — and it is +14.52% above its 20-DMA, one strong day from being labelled extended itself.
- **Today's tape is a semiconductor unwind.** AMD -8.75% on 49.2M shares, the weakest industry groups are Semiconductors (29.4% above their 20-DMA, avg -3.19%) and Electronic Production Equipment (-4.48%); VIX +3.2% to 19.30. The fresh-book triggers that did fire are small/mid caps: BGIN +40.58%, SBC +37.64%, NMAX +31.41%, LFTO +30.63%, MOD +27.86%.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (breadth 52.82% is far above the 40% trigger) |
| `uncertainty` | **false** (VIX 19.3 / VIX3M 20.62 = 0.9360) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at +2.87%) |
| `index_below_20sma` | **true** (1 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+32.8 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-13** — the cron day's settled bar | `A_tv_breakout_4pct` 59 · `B_tv_ep9m` 172 · `D_tv_gap_10pct` 2 · `TV_volume_breakout` 43 | 232 |
| **T+1** (cross-check) | **2026-11-12** — shibui's newest ingested session | 9 branches | 1147 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 191 |
| `t1` | context screens only | 956 |
| `fresh` | trigger screens only | 41 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 33 | 33 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 181 | 181 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 462 | 462 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 81 | 81 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 2 | 2 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 49 | 49 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 4 | 4 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 344 | 344 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 145 | 145 | complete |

Total screened rows **1301** across the 9 branches → **1188 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (5 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **AMD** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, E_qullamaggie_5d_gainers, G_peoplewish | `fresh+t1` | 534.06 | **-8.75%** | 5.93 | 13.26 | 44.73 | EXTENDED |
| **CHA** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, H_hernandez_theme, TV_volume_breakout | `fresh+t1` | 14.37 | **+6.37%** | 3.62 | — | — | — |
| **DPC** | 3 | A_stockbee_4pct, E_qullamaggie_5d_gainers, G_peoplewish | `t1` | 34.26 | **-0.20%** | 8.76 | 34.47 | 26.31 | EXTENDED |
| **IRTC** | 3 | A_stockbee_4pct, F_qullamaggie_5d_losers, G_peoplewish | `t1` | 91.91 | **-1.76%** | 5.75 | -22.85 | -28.14 | EXTENDED |
| **LUNR** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish | `fresh+t1` | 13.00 | **-0.23%** | 8.60 | 23.86 | 51.16 | EXTENDED |

### What Tier-A is saying

- **AMD** — 3 stylists, 5 origins. **-8.75% today** on 49.2M shares (close 534.06); the 5-session screen move is +44.73%, ATR 7.85% (95.9th pctile of the $10B+ set), flagged `trailing_pe` + `operating_pe`. EXTENDED. This is a distribution print inside a name that has already run — not a fresh trigger, and the volume is exit liquidity rather than accumulation.
- **CHA** — 3 stylists, 4 origins. **+6.37% today** (14.37). The only Tier-A name that is NOT extended: ATR 3.99%, RSI 71.5, +14.52% above its 20-DMA, and no valuation red flag. Cleanest setup on the list, and also the one most at risk of being labelled extended on the next strong close.
- **LUNR** — 6 origins, the most agreement in the book, but **-0.23% today** and EXTENDED (ATR 9.02% = 97.4th pctile, +17.88% above its 20-DMA, flagged `free_cash_flow_yield`). Six screen hits here describe a *week* of momentum, not an event today.
- **DPC** — 3 stylists, **T+1-only** (no fresh-book trigger today), -0.20% today, EXTENDED (+16.70% above its 20-DMA, ATR 8.32%), flagged `free_cash_flow_yield`.
- **IRTC** — 3 stylists, **T+1-only**, -1.76% today, and **18.47% BELOW its 20-DMA** with RSI 35.3 — it is no longer a momentum name at all. Extended on the ATR rule alone (7.63%), flagged `debt_to_equity` > 1.5. The weakest of the five.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 1 fresh / 4 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| AMD | 7.85 | 95.9 | 2.90 | no |
| CHA | 3.99 | 77.5 | 14.52 | no |
| DPC | 8.32 | 96.7 | 16.70 | yes |
| IRTC | 7.63 | 95.5 | -18.47 | no |
| LUNR | 9.02 | 97.4 | 17.88 | yes |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **AMD** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, E_qullamaggie_5d_gainers, G_peoplewish | `fresh+t1` | 534.06 | **-8.75%** | 1.04 | 7.85 | 50.4 | 5.93 |
| **ANET** | 2 | A_stockbee_4pct, B_stockbee_ep9m, E_qullamaggie_5d_gainers | `t1` | 197.29 | **-4.52%** | 0.77 | 6.07 | 55.2 | 4.77 |
| **CHA** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, H_hernandez_theme, TV_volume_breakout | `fresh+t1` | 14.37 | **+6.37%** | 2.03 | 3.99 | 71.5 | 3.62 |
| **DPC** | 3 | A_stockbee_4pct, E_qullamaggie_5d_gainers, G_peoplewish | `t1` | 34.26 | **-0.20%** | 0.78 | 8.32 | 54.9 | 8.76 |
| **FIGR** | 2 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish | `t1` | 25.22 | **-1.75%** | 0.60 | 7.87 | 50.7 | 7.67 |
| **HUBS** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 217.25 | **+0.65%** | 0.78 | 6.22 | 46.3 | 5.68 |
| **IBP** | 2 | A_stockbee_4pct, H_hernandez_theme | `t1` | 229.00 | **+2.34%** | 1.88 | 4.58 | 60.6 | 4.48 |
| **IRTC** | 3 | A_stockbee_4pct, F_qullamaggie_5d_losers, G_peoplewish | `t1` | 91.91 | **-1.76%** | 0.63 | 7.63 | 35.3 | 5.75 |
| **LMND** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 44.19 | **+2.86%** | 1.21 | 5.63 | 51.4 | 5.58 |
| **LUNR** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish | `fresh+t1` | 13.00 | **-0.23%** | 1.00 | 9.02 | 57.0 | 8.60 |
| **PLBL** | 2 | A_stockbee_4pct, H_hernandez_theme | `t1` | 7.24 | **-0.41%** | 0.82 | 5.43 | 75.6 | 5.21 |
| **TOP** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, TV_volume_breakout | `fresh+t1` | 17.00 | **+10.17%** | 1.60 | 10.39 | 62.6 | 13.16 |

- **TOP +10.17%** (17.00) — 2 stylists, ATR 10.39% (the widest volatility in Focus), +13.16% above its 20-DMA. Momentum continuation, not a fresh base.
- **FRMI +26.70%** (2.61) — 5-session +34.64%, ADR 12.21%, and it is inside the parabolic-short book. Extended, thin, and a state detector rather than a forward-looking signal.
- **PLBL** — RSI 75.6, the only Focus name over the RSI>75 line, and T+1-only, so nothing fired on it today.
- **The T+1-only Focus names carry no trigger from today's tape**: DPC -0.20%, IRTC -1.76%, ANET -4.52%, FIGR -1.75%, HUBS +0.65%, LMND +2.86%, IBP +2.34%, PLBL -0.41%. Read them as *yesterday's* agreement, not today's action — every row publishes its `source` and `data_as_of` for exactly this reason.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 321 | no red flag, and earnings data present |
| `fail` | 557 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 96 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-13

| Metric | Value |
|---|---|
| Universe | 1100 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **52.82%** / 53.64% / 49.82% |
| Advance / decline / unchanged | **579 / 510 / 11** (ratio 1.14) |
| Median name | +0.09% |
| VIX / VIX3M | **19.3 / 20.62** (VIX +3.21% from 18.7) |
| SPY / QQQ / RSP / IWM / QQQE | 754.37 (-0.36%) / 679.89 (-1.20%) / 221.16 (+0.20%) / 277.54 (-0.32%) / 115.84 (-0.63%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| NU | Nu Holdings Ltd. | 13.22 | **+11.75%** |
| CBRS | Cerebras Systems Inc. | 108.72 | **+11.22%** |
| MOG.B | Moog Inc. | 347.00 | **+6.72%** |
| ALNY | Alnylam Pharmaceuticals, Inc. | 165.04 | **+5.36%** |
| U | Unity Software Inc. | 52.81 | **+5.24%** |
| SHG | Shinhan Financial Group Co Ltd | 66.59 | **+4.42%** |
| CHTR | Charter Communications, Inc. | 138.39 | **+4.32%** |
| STE | STERIS plc (Ireland) | 264.32 | **+4.29%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| NBIS | Nebius Group N.V. | 115.88 | -9.92% |
| AMD | Advanced Micro Devices, Inc. | 534.06 | -8.75% |
| KEP | Korea Electric Power Corporation | 10.16 | -8.72% |
| FN | Fabrinet | 327.98 | -7.31% |
| DELL | Dell Technologies Inc. | 344.53 | -7.18% |
| TSEM | Tower Semiconductor Ltd. | 146.89 | -6.95% |
| IONQ | IonQ, Inc. | 28.88 | -6.42% |
| CSCO | Cisco Systems, Inc. | 95.64 | -6.24% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (49):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| AAON | 44.80 | 7.45 | 80.25 | +1.84% |
| ACMR | 26.89 | 7.17 | 47.95 | -3.87% |
| ALAB | 26.92 | 8.53 | 221.83 | -2.62% |
| AMD | 44.73 | 5.93 | 534.06 | -8.75% |
| ANET | 29.83 | 4.77 | 197.29 | -4.52% |
| CIEN | 27.37 | 7.31 | 280.54 | -4.57% |
| CIFR | 28.83 | 11.63 | 6.86 | -4.06% |
| COHR | 36.71 | 8.64 | 218.15 | -6.00% |
| COHU | 28.94 | 8.65 | 43.59 | -3.13% |
| CORZ | 26.36 | 8.29 | 14.52 | +0.97% |
| CRWV | 29.64 | 9.98 | 53.13 | -6.13% |
| DOCN | 27.40 | 8.81 | 86.32 | -4.16% |
| DPC | 26.31 | 8.76 | 34.26 | -0.20% |
| FLY | 66.79 | 8.76 | 25.21 | -0.40% |
| FORM | 28.65 | 7.22 | 87.53 | -5.19% |
| FRMI | 34.64 | 12.21 | 2.61 | +26.70% |
| FROG | 48.22 | 7.73 | 113.60 | +2.71% |
| FRVO | 49.55 | 9.73 | 11.51 | -1.20% |
| GEO | 28.01 | 4.73 | 32.53 | +0.96% |
| HUT | 34.87 | 10.20 | 57.57 | -7.11% |
| KRMN | 26.21 | 8.30 | 40.66 | +0.40% |
| LGN | 42.74 | 9.24 | 35.00 | -3.50% |
| LQDA | 30.64 | 7.36 | 57.41 | -1.22% |
| LRCX | 26.23 | 5.48 | 225.92 | -3.36% |
| LUNR | 51.16 | 8.60 | 13.00 | -0.23% |
| MKSI | 25.27 | 5.44 | 215.65 | -2.64% |
| MPWR | 27.93 | 5.86 | 1390.54 | -3.93% |
| MRCY | 27.28 | 6.24 | 81.42 | -2.42% |
| MTSI | 29.11 | 7.31 | 232.06 | -5.57% |
| MXL | 33.06 | 9.70 | 55.78 | -5.39% |
| NET | 30.26 | 6.30 | 305.81 | -3.98% |
| OKLO | 27.34 | 7.78 | 23.92 | -2.17% |
| ONTO | 34.41 | 6.71 | 203.62 | -2.89% |
| PENG | 34.61 | 9.58 | 47.36 | -5.47% |
| QNT | 25.62 | 8.96 | 35.40 | -5.50% |
| RDW | 29.73 | 7.81 | 7.73 | -3.74% |
| RKLB | 39.31 | 7.72 | 61.53 | -3.96% |
| SANM | 26.30 | 6.93 | 158.31 | -3.75% |
| SEI | 27.60 | 8.90 | 63.81 | -1.07% |
| SITM | 32.55 | 7.78 | 444.54 | -5.53% |
| SMTC | 30.48 | 8.06 | 114.59 | -4.06% |
| TMDX | 33.37 | 6.19 | 91.38 | -0.67% |
| UCTT | 29.30 | 7.77 | 46.35 | -3.64% |
| UI | 32.87 | 4.41 | 669.76 | -1.97% |
| VSH | 26.20 | 7.00 | 26.62 | -4.21% |
| WOLF | 30.21 | 9.01 | 24.83 | -6.34% |
| WULF | 29.37 | 9.71 | 12.62 | -3.22% |
| XE | 25.11 | 8.13 | 11.08 | -1.60% |
| ZETA | 26.47 | 5.46 | 36.65 | -1.66% |

**Long / mean-reversion candidates (4):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| BZ | -29.67 | 3.57 | 12.96 | +3.76% |
| IONS | -29.61 | 4.91 | 29.06 | +6.41% |
| IRTC | -28.14 | 5.75 | 91.91 | -1.76% |
| OPEN | -31.01 | 9.22 | 1.19 | -3.64% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

**Theme → group → leaders (Hernandez):** the winning themes are **XLV, IBB and XRT** — Health Care (XLV + IBB) and Consumer Discretionary (XRT) — 145 names. Composite relative-strength leaders: **REPL** (rs 1M/3M/6M 81.7 / 44.1 / 346.7), **KOD** (22.7 / 197.3 / 196.5), **CDNA** (20.9 / 65.6 / 289.4), **XNCR** (58.3 / 61.9 / 218.1), **XERS** (65.3 / 100.0 / 164.4). Note this is a **T+1 context screen** — its RS window describes the 2026-11-12 session, and the sector ETFs are the only admissible themes (a single stock can out-rank a real sector theme on raw RS).

## Method, source health & caveats

| Source | Query / endpoint | Status |
|---|---|---|
| TradingView scanner (`POST scanner.tradingview.com/america/scan`) | fresh book universe: 3,796 names (`totalCount` 3,796 = rows fetched, no truncation); breadth universe: 1,100 names, `totalCount` 1,100 = rows fetched | **ok** |
| shibui-finance over the MCP bridge (`stock_data_query`) | 9 T+1 branches, the CANSLIM growth half, the merged enrichment pass and the valuation/quality overlay — screen session **2026-11-12** (T+1) | **ok** |
| bridge `market-recap get_quotes` | the official 16:00 ET close for the book names (`market_state: post`) — the `chg` column in this artifact | **ok** |
| Cboe delayed-quote CDN | VIX / VIX3M pair, quote time 2026-11-13 16:15:01 ET, 2 pulls 5 s apart — identical (`vix_stable: true`) | **ok** |
| MCP catalog probe (`probe_mcp.py`) | `catalog_ok total=135 finance_tools=0` — no finance MCP registered on this runtime; the MCP-over-HTTP bridge is the finance path | **ok** |
| shibui T+1 breadth cross-check | the skill's breadth SQL on shibui's newest ingested session (2026-11-12) — fetched and returned rows, but its numbers are **not** rendered into this artifact, so only the settled TradingView read is published here | **ok** (fetched; not published) |

**`degraded_sources: 0`** — no source was rate-limited, blocked or partially unavailable in this run.

**Sources and what each one owns.** TradingView's scanner is the source of record for the cron day's settled bar (`close` = the official 16:00 ET print) and for the breadth universe; shibui-finance, reached over the MCP-over-HTTP bridge, owns every multi-session context screen; the bridge's `market-recap get_quotes` owns the official close printed on each book row; the Cboe delayed-quote CDN owns the single VIX/VIX3M pair used everywhere in this file.

**The dual book, and which session each row describes.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-13's own settled bar** and are the primary book (232 names). The CONTEXT screens (5-day gainers/losers, 14-day velocity, the anticipation coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-12**, and are labelled T+1 (1,147 names). Every row carries `data_as_of` and `source` (`fresh` 41 · `t1` 956 · `fresh+t1` 191); the two are never blended.

**The coverage assertion.** Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. `rows_kept == rows_passing` on **9 of 9** branches, and no branch count lands on a cap (30/50/60/200) — the truncation fingerprint.

**What the labels mean.** `EXTENDED` is a label, never a filter: ATR > 5.0%, RSI > 75, more than 15% above the 20-DMA, or 3+ consecutive up sessions. Tier-A is published twice (fresh and extended) and nothing is dropped for tripping a rule. The valuation/quality overlay is also a label: 557 names carry at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags), 321 pass, and **96 are `unknown`** — no red flag but no reported trailing earnings either, which is disclosed, never counted as a flag.

**Caveats.** The context screens are one session stale (shibui is T+1) — the multi-session constructs are only mildly affected, but any single-session metric drawn from them is not today's. The breadth universe (TradingView, `market_cap_basic` > $10B, 1,100 names) is **one** population; the skill's shibui T+1 breadth SQL (a different market-cap source, so a different name set) was fetched as the cross-check but its numbers are not rendered into this artifact — only the settled read is published here. The VIX quote carries a ~15-minute delayed stamp (16:15:01 ET). The path of intraday prints is not reconstructed here, so no points between the open and the close are published.

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
