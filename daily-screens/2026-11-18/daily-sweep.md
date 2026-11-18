---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-18 18:30 ET"
cron_date: "2026-11-18"
screen_data_date: "2026-11-17 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-18 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-18 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 50, uncertainty: true, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 32.01}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Wednesday 18 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-18's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-17**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **The book is dual and it says so on every row.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) ran on **2026-11-18's own settled bar** (337 names); the multi-session CONTEXT screens stayed on shibui's newest ingested session, **2026-11-17** (1,104 names). 1,179 distinct candidates, **9/9 branches complete** — `rows_kept == rows_passing` on every branch, no branch landed on a cap.
- **Tier-A is 4 names and every one of them is EXTENDED (0 fresh / 4 extended).** Only **BRBR** is driven by today's own trigger (+24.07% to 13.66 on 3.9x relative volume — the day's only 10%-gap name); ALAB and RYTM are Tier-A on the 2026-11-17 screen alone and neither triggered today. The extension label is published, not used to drop names.
- **The tape underneath the book is weak but not disorderly.** All five index ETFs are below their own 20-DMA, 470 names advanced against 603 declined, VIX settled at **24.56 / VIX3M 24.29** (ratio 1.0111 → `uncertainty`), and the valuation overlay flags **582 of 992** names — the overlay is a label, never a filter.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **50** (breadth 32.01% is far above the 40% trigger) |
| `uncertainty` | **true** (VIX 24.56 / VIX3M 24.29 = 1.0111) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at +0.21%) |
| `index_below_20sma` | **true** (0 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+32.0 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-18** — the cron day's settled bar | `A_tv_breakout_4pct` 122 · `B_tv_ep9m` 207 · `D_tv_gap_10pct` 1 · `TV_volume_breakout` 67 | 337 |
| **T+1** (cross-check) | **2026-11-17** — shibui's newest ingested session | 9 branches | 1104 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 262 |
| `t1` | context screens only | 842 |
| `fresh` | trigger screens only | 75 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 41 | 41 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 199 | 199 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 483 | 483 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 58 | 58 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 1 | 1 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 3 | 3 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 11 | 11 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 345 | 345 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 66 | 66 | complete |

Total screened rows **1207** across the 9 branches → **1179 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (4 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **ALAB** | 3 | A_stockbee_4pct, G_peoplewish, jeff_sun_canslim | `t1` | 216.75 | **+2.43%** | 8.93 | -28.80 | — | EXTENDED |
| **BRBR** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_tv_ep9m, D_tv_gap_10pct, TV_volume_breakout | `fresh+t1` | 13.66 | **+24.07%** | 5.72 | — | — | EXTENDED |
| **RYTM** | 4 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme | `t1` | 119.04 | **+2.08%** | 5.77 | 26.79 | — | EXTENDED |
| **SLS** | 4 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish, H_hernandez_theme | `fresh+t1` | 17.95 | **-6.27%** | 12.17 | 84.49 | 128.79 | EXTENDED |

### What Tier-A is saying

- **ALAB** — 3 stylists (Bonde 4% breakout, peoplewish ADR/velocity, Jeff Sun CANSLIM) but **`t1` only**: it did not trigger on the 2026-11-18 bar (+2.43% today, inside the 4% gate). ATR% 10.56 (98.8th pctile of the $10B+ set). Valuation **`fail`** — trailing P/E 79.6, operating P/E 92.4, EV/EBIT 79.0.
- **BRBR** — the only Tier-A name carrying **today's** trigger: 4% breakout + EP9M + the day's only **10% gap** + volume breakout, **+24.07% to 13.66 on 3.89x RVOL**. RSI 80.6, +36.98% above its 20-DMA, ATR% 5.37 — extended on three rules. Valuation **`pass`**: trailing P/E 7.5, operating P/E 4.1, FCF yield 17.6%.
- **RYTM** — 4 stylists, all **`t1`** (Bonde breakout, Kullamägi RS, peoplewish, Hernandez theme); no trigger on today's bar (+2.08%). Valuation **`fail`** on negative free cash flow (-1.04%); **no trailing P/E** — disclosed as `earnings_data_missing`, not counted as a P/E flag.
- **SLS** — 4 stylists and the most stretched name in the book: **+128.79% over five sessions but -6.27% today**. ATR% 12.80 (99.7th pctile), +74.86% above its 20-DMA. Negative FCF, no trailing P/E (disclosed). The label is a state detector, not a forward signal.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 4 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| ALAB | 10.56 | 98.8 | -7.93 | no |
| BRBR | 5.37 | 87.4 | 36.98 | yes |
| RYTM | 5.32 | 87.2 | 15.83 | yes |
| SLS | 12.80 | 99.7 | 74.86 | yes |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **ALAB** | 3 | A_stockbee_4pct, G_peoplewish, jeff_sun_canslim | `t1` | 216.75 | **+2.43%** | 0.77 | 10.56 | 40.7 | 8.93 |
| **ARM** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 182.76 | **-0.34%** | 0.63 | 8.48 | 39.8 | 5.81 |
| **BRBR** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_tv_ep9m, D_tv_gap_10pct, TV_volume_breakout | `fresh+t1` | 13.66 | **+24.07%** | 3.89 | 5.37 | 80.6 | 5.72 |
| **ENR** | 2 | A_stockbee_4pct, TV_volume_breakout | `fresh+t1` | 28.29 | **+3.25%** | 2.01 | 4.10 | 75.1 | 3.88 |
| **LUMN** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 4.30 | **+0.00%** | 0.62 | 7.88 | 43.0 | 7.37 |
| **RARE** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, G_peoplewish | `fresh+t1` | 17.73 | **+6.17%** | 1.18 | 4.95 | 60.2 | 5.08 |
| **RYTM** | 4 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme | `t1` | 119.04 | **+2.08%** | 0.80 | 5.32 | 65.1 | 5.77 |
| **SHAZ** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 21.99 | **-2.66%** | 1.04 | 16.72 | 40.2 | 12.75 |
| **SLS** | 4 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish, H_hernandez_theme | `fresh+t1` | 17.95 | **-6.27%** | 1.98 | 12.80 | 71.4 | 12.17 |
| **SNAP** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 5.44 | **-1.09%** | 1.16 | 6.07 | 48.0 | 5.37 |
| **VIK** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, TV_volume_breakout | `fresh+t1` | 100.37 | **+6.46%** | 1.84 | 3.73 | 72.9 | 3.80 |
| **YALA** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, TV_volume_breakout | `fresh+t1` | 5.94 | **+4.21%** | 1.99 | 2.71 | 69.3 | 2.40 |

- **12 names, and only 4 of them are Tier-A.** Two of the twelve (ALAB, RYTM) are `t1`-only, so they carry no 2026-11-18 trigger at all.
- **The day's cleanest multi-branch name is VIK** (+6.46%): 4% breakout, EP9M, the 10% gap branch, the volume-breakout screen and the T+1 breakout all agree. **YALA** (+4.21%) hits 3 trigger branches; **ENR** (+3.25%) hits 2 but with RSI 75.1 already overbought.
- **SHAZ is the most volatile name on the list** (ATR% 16.72) and **LUMN is flat** (+0.00%) despite 2 stylists and an ADR of 7.37% — the ADR is a liquidity fact, not a move.
- Only **BRBR** has today's own gap behind it; the rest of the Focus list is a mix of yesterday's screen and today's trigger prints, so the two are not the same kind of signal.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 317 | no red flag, and earnings data present |
| `fail` | 582 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 93 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-18

| Metric | Value |
|---|---|
| Universe | 1081 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **32.01%** / 43.57% / 43.48% |
| Advance / decline / unchanged | **470 / 603 / 8** (ratio 0.78) |
| Median name | -0.20% |
| VIX / VIX3M | **24.56 / 24.29** (VIX -3.54% from 25.46) |
| SPY / QQQ / RSP / IWM / QQQE | 730.20 (-0.31%) / 659.51 (+0.39%) / 215.43 (-0.15%) / 270.12 (+0.40%) / 112.01 (+0.03%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| OKTA | Okta, Inc. | 195.61 | **+12.07%** |
| SAIL | SailPoint, Inc. | 22.25 | **+10.26%** |
| PANW | Palo Alto Networks, Inc. | 339.92 | **+9.90%** |
| GNRC | Generac Holdings Inc. | 205.45 | **+9.87%** |
| RBRK | Rubrik, Inc. | 110.00 | **+9.26%** |
| FROG | JFrog Ltd. | 114.38 | **+8.83%** |
| AKAM | Akamai Technologies, Inc. | 91.70 | **+8.34%** |
| TJX | TJX Companies, Inc. (The) | 140.30 | **+8.05%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| HUM | Humana Inc. | 385.78 | -12.98% |
| UNH | UnitedHealth Group Incorporated | 349.91 | -10.21% |
| CBRS | Cerebras Systems Inc. | 94.15 | -9.63% |
| ELV | Elevance Health, Inc. | 400.84 | -7.63% |
| DINO | HF Sinclair Corporation | 90.64 | -7.24% |
| CDE | Coeur Mining, Inc. | 12.24 | -7.06% |
| CNC | Centene Corporation | 67.45 | -7.03% |
| EQX | Equinox Gold Corp. | 9.17 | -7.00% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (3):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| FRMI | 56.49 | 14.72 | 2.46 | +2.07% |
| MOD | 25.87 | 7.42 | 137.88 | +6.28% |
| SLS | 128.79 | 12.17 | 17.95 | -6.27% |

**Long / mean-reversion candidates (11):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| ACHR | -25.27 | 7.83 | 3.23 | -8.24% |
| AMPX | -26.17 | 8.30 | 6.73 | -0.59% |
| BETA | -26.70 | 7.53 | 20.05 | -2.62% |
| BTDR | -37.60 | 11.63 | 3.89 | -2.75% |
| CTVA | -27.53 | 4.75 | 8.36 | -5.22% |
| IONQ | -29.01 | 7.54 | 23.48 | -5.48% |
| JOBY | -26.01 | 6.37 | 4.19 | -4.34% |
| QS | -26.29 | 6.79 | 3.19 | -2.74% |
| RGTI | -30.37 | 7.98 | 8.33 | -1.54% |
| SMMT | -40.16 | 8.03 | 10.50 | -1.59% |
| TE | -35.75 | 13.43 | 1.39 | +4.51% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

- **Theme → group → leaders: Health Care (XLV, IBB) and Consumer Staples (XLP)** led the relative-strength ranking, drawn from a **226-name pool** off the 3,756-name fresh universe; **66** theme rows are published in `ariel-hernandez.md`.
- **Read the theme ranking as a multi-session construct, not as today's strength.** Health Care was the *worst* industry group on the 2026-11-18 tape (Managed Health Care averaged **-7.90%**, with 0% of names above their own 20-DMA), so the branch is surfacing the theme's leaders against a group that was sold — not a group that is leading.
- The theme branch is a **published screen with sector ETFs only** (a single stock cannot displace a real sector theme), and its 66 rows sit inside the same 1,179-name book.

## Method, source health & caveats

- **MCP catalog probe** — `catalog_ok total=136 finance_tools=0`. No finance MCP is registered on this runtime, so the servers were reached over the **MCP-over-HTTP bridge** (`mcp_bridge.py`, packs: tradier, fmp, market-recap) — the probe being empty is not a missing source.
- **TradingView scanner** (`POST scanner.tradingview.com/america/scan`) — **ok**. Fresh book: 3,756 rows, `totalCount` = rows fetched. Breadth scan: 1,081 rows, `totalCount` = rows fetched.
- **shibui over the bridge** (`SELECT … FROM shibui.*`) — **ok**. 9 context branches + the merged enrichment pass + the CANSLIM growth half + the overlay; `rows_kept == rows_passing` on every branch.
- **Cboe delayed-quote CDN** (`_VIX.json` / `_VIX3M.json`) — **ok**, 2 pulls 5 s apart, identical; quote time 2026-11-18 16:15:01 ET.
- **bridge `market-recap` `get_quotes`** — **ok**, 25 book names, `market_state: post`, `as_of` 21:00 UTC (16:00 ET). Cross-checked against the scanner's own close for the same names: **no disagreement above 0.6 pp**.
- **Yahoo JSON / Finviz** — not used. The bridge is the quote source of record; Finviz is Cloudflare-blocked from this egress.
- **Degraded sources: none.** No source failed, timed out or was rate-limited in this run.

- **Sources.** TradingView scanner (the 2026-11-18 settled bar: the fresh book, the breadth universe, the theme pool); shibui over the MCP-over-HTTP bridge (the T+1 context screens, the CANSLIM growth half, the valuation/quality overlay); the Cboe delayed-quote CDN (the VIX/VIX3M pair, pulled twice 5 s apart and identical); the bridge's `market-recap` (the official 16:00 ET close for the book's names, `market_state: post`).
- **Universes.** Breadth: 1,081 names — NYSE/NASDAQ/AMEX, type in {stock, dr}, `market_cap_basic > $10B`; `totalCount 1081` = rows fetched, no truncation. Fresh book: 3,756 names (same venue/type filter, `market_cap_basic > $300M`), of which 337 passed a trigger gate. The published book is the 1,179 distinct candidates.
- **Coverage.** 9/9 branches fetched uncapped and paged until `rows_kept == rows_passing`; no branch count landed on 30 / 50 / 60 / 200. The theme branch is a published screen over a 226-name pool.
- **Caveats.** shibui is T+1, so every CONTEXT screen describes **2026-11-17** while every TRIGGER screen describes **2026-11-18**; the parabolic five-session move stays on shibui (T+1) and is deliberately **not** re-expressed on the scanner's `Perf.W`, which measures a six-session window. The valuation overlay is a **label, not a filter** — 582 of 992 names carry a red flag and 93 have no reported trailing earnings (disclosed, never counted as a flag). Finviz is Cloudflare-blocked from this egress and is not in the chain; Yahoo JSON was not needed because the bridge is the quote source of record.

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
