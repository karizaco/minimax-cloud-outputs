---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-20 14:00:10 ET"
data_date: "2026-11-19"
live_date: "2026-11-20"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 866 names"
vix_quote_time: "2026-11-20 14:00:00 ET (Yahoo chart API, 5-minute bar pinned to the fire clock)"
vix_pair: "VIX 31.69 / VIX3M 28.7 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-20/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
degraded_sources: 2
---
_contract: breadth-artifact-v1 · data_date 2026-11-19 · universe 866 names · breadth 23.67% (pctile 5.7 · BELOW_NORMAL) · divergence +23.67 pp (BROAD) · AD 73/789/3_

# Breadth & Regime Snapshot — Friday, 20 November 2026 (intraday, cron #10)

Intraday breadth read, fired **2026-11-20 14:00:10 ET** on the live tape. The settled breadth numbers describe the **2026-11-19** close (shibui is T+1 — at a 14:00 ET fire on 2026-11-20 its newest settled session is 2026-11-19); the tape and the volatility pair are **2026-11-20 at 14:00:00 ET**. The two layers are never blended. This artifact is a **delayed replay**: the scheduled fire was blocked by the platform for 2585 minutes and resumed in place on 2026-11-22, so the live layer is reconstructed from 5-minute bars pinned to the fire clock rather than pulled live — the settled layer is unaffected.

## TL;DR

- **Breadth has broken down.** 23.67% of the 866 large caps are above their own 20-DMA (percentile 5.7, BELOW_NORMAL), down from 37.23% in the 2026-11-18 session, and 44.80% are above the 50-DMA (percentile 23.2, NORMAL). The 2026-11-19 session itself was a rout — **73 advancing against 789 declining** (3 unchanged, A/D ratio 0.093) — and the 10-session ADL slope has steepened to **-153.87 net advances per session**.
- **The divergence is the story: +23.67 pp, BROAD (percentile 73.0).** All 5 index ETFs sit below their own 20-DMA (0 of 5) while 23.67% of the large-cap universe is above its own — the average large cap is materially healthier than the index, so the index is the weak leg, not the average stock. The spread has narrowed for three sessions (+39.42 → +37.23 → +23.67 pp) but it is still in the top quarter of its own year. The regime carries a **50% size cut** (index below its 20-DMA and breadth under 40%) and `uncertainty: true`.
- **Read the tape as a megacap-tech liquidation, not a market liquidation.** At 14:00:00 ET on 2026-11-20 SPY was -2.13% and QQQ -3.76%, but the equal-weight RSP was only -0.74% — a 1.39 pp spread in RSP's favour — while the VIX was at 31.69 (+11.31%) with the term structure **inverted** (VIX 31.69 above VIX3M 28.7, ratio 1.1042), which is what sets `uncertainty: true`. The tape and the pair are reconstructed from bars pinned to the fire clock, not live prints, and the Cboe delayed-quote CDN is blocked from this egress.

## Breadth — 2026-11-19 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 866 |
| Above 20-DMA | 205 (23.67%) |
| Below 20-DMA | 661 (76.33%) |
| Above 50-DMA | 388 (44.80%) |
| Index ETFs above their own 20-DMA | 0 of 5 (0.0%) |
| Index ETFs above their own 50-DMA | 0 of 5 (0.0%) |
| Advance/decline — settled session | 73 advancing / 789 declining / 3 unchanged (A/D ratio 0.093) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **866 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-11-06 | 363 | 497 | 5 | -134 | -1412 | 41.15 |
| 2026-11-09 | 724 | 138 | 3 | +586 | -826 | 41.14 |
| 2026-11-10 | 392 | 467 | 6 | -75 | -901 | 29.63 |
| 2026-11-11 | 562 | 299 | 4 | +263 | -638 | 27.65 |
| 2026-11-12 | 215 | 647 | 3 | -432 | -1070 | 20.53 |
| 2026-11-13 | 520 | 337 | 8 | +183 | -887 | 14.78 |
| 2026-11-16 | 229 | 631 | 5 | -402 | -1289 | 1.46 |
| 2026-11-17 | 162 | 702 | 1 | -540 | -1829 | -48.49 |
| 2026-11-18 | 376 | 486 | 3 | -110 | -1939 | -70.14 |
| 2026-11-19 | 73 | 789 | 3 | -716 | -2655 | -153.87 |

**A/D ratio 0.093 today** (73 advancing / 789 declining). Over the last 10 sessions the net advances total **-1377** and the ADL slope is **-153.87 net advances per session** (10-session A/D ratio 0.724). The ADL is cumulative from 2026-08-26, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (263 sessions, 2025-11-04 → 2026-11-19). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 23.67% | — | — |
| `breadth_pctile_1y` | 5.7 | — | BELOW_NORMAL |
| `breadth_pct_50dma` | 44.80% | — | — |
| `breadth_pctile_1y_50dma` | 23.2 | — | NORMAL |
| `index_etfs_above_20dma` | 0 of 5 | 16.3 | BELOW_NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +23.67 pp | BROAD | 73.0 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-13 | +43.01 |
| 2026-11-16 | +51.56 |
| 2026-11-17 | +39.42 |
| 2026-11-18 | +37.23 |
| 2026-11-19 | +23.67 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 264.22 | 277.18 | 278.91 | -5.27% | -3.23 |
| QQQ | 645.04 | 683.33 | 713.09 | -9.54% | -6.01 |
| QQQE | 109.89 | 115.54 | 118.06 | -6.92% | -5.35 |
| RSP | 211.63 | 218.54 | 214.95 | -1.54% | -1.51 |
| SPY | 715.87 | 751.32 | 761.67 | -6.01% | -5.69 |

## Live tape — 2026-11-20

Index levels and the ETF tape are pinned to **2026-11-20 14:00:00 ET** — the fire's own clock. This run is a delayed replay, so the live print no longer exists on any feed: every number below is reconstructed from Yahoo's chart API 5-minute bars at that stamp (the Cboe delayed-quote CDN answers HTTP 403 from this egress, and the bridge's `market-recap` would now serve a later session's quotes, not this session's tape).

| Index | Last | Change | Bar stamp |
|---|---|---|---|
| S&P 500 | 7,021.33 | -2.18% | 14:00:00 ET |
| Nasdaq 100 | 25,516.62 | -3.80% | 14:00:00 ET |
| Russell 2000 | 2,612.89 | -1.63% | 14:00:00 ET |
| Dow Jones | 48,797.69 | -0.64% | 14:00:00 ET |

| Index ETF | Last | Change | Prior close | Bar stamp |
|---|---|---|---|---|
| SPY | 700.550 | -2.13% | 715.780 | 14:00:00 ET |
| QQQ | 620.870 | -3.76% | 645.100 | 14:00:00 ET |
| IWM | 259.850 | -1.65% | 264.200 | 14:00:00 ET |
| RSP | 210.130 | -0.74% | 211.690 | 14:00:00 ET |
| DIA | 487.490 | -0.67% | 490.770 | 14:00:00 ET |

**Sector rotation (live, 14:00:00 ET)** — the tape is being sold out of semiconductors and megacap tech while the defensives are bid: consumer staples, health care and utilities are all green, and technology is the worst sector by a wide margin.

| Sector ETF | Sector | Last | Change |
|---|---|---|---|
| XLP | Consumer staples | 91.200 | +1.45% |
| XLV | Health care | 178.644 | +0.68% |
| XLU | Utilities | 43.270 | +0.56% |
| XLE | Energy | 61.195 | +0.50% |
| XLRE | Real estate | 42.980 | +0.23% |
| XLF | Financials | 55.265 | -0.58% |
| XLB | Materials | 48.980 | -0.92% |
| XLC | Communication | 101.070 | -1.62% |
| XLY | Consumer discretionary | 113.860 | -1.71% |
| XLI | Industrials | 158.380 | -1.83% |
| XLK | Technology | 152.413 | -5.16% |

Semiconductors (SMH) 412.51 (-7.83%) — the mega-cap leg is being liquidated with the index, not leading it.

## Volatility — single pair, live

**31.69 / 28.7** — VIX 31.69, VIX3M 28.7, one pair, quoted at 14:00:00 ET on 2026-11-20 from Yahoo's chart API (^VIX / ^VIX3M), both symbols read from the SAME 5-minute bar.

- Session mode: replay — reconstructed from the pinned 5-minute bar at the fire clock (the live print is no longer available).
- Prior close: VIX 28.47 (+11.31%), VIX3M 27.07 (+6.02%) — the front end is moving more than the 3-month, which is the signature of a near-term shock.
- VIX/VIX3M = 1.1042 — the VIX is ABOVE the 3-month, an inverted term structure, which is what sets `uncertainty: true`. The gap is 10.42% — wider than the inversion that fired at the previous fire, and a real one, not a rounding-scale difference.
- The Cboe delayed-quote CDN answered HTTP 403 (Cloudflare) from this egress, so the pair came from the pinned fallback; both symbols carry the same bar stamp, so the pair is internally consistent.

This is the ONLY volatility pair in this document. It is the print that existed at the fire, not a settled close, and the settled sections above never carry a VIX number.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 50 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **All five index ETFs are below BOTH their 20-DMA and their 50-DMA** (0 of 5 on each), and RSP is the shallowest at -1.54% from its 50-DMA against SPY -6.01%, QQQ -9.54%, QQQE -6.92% and IWM -5.27%. The BROAD divergence is a 20-DMA reading; the equal-weight index is the least-broken leg on both horizons.
- **QQQ's -9.54% distance from its 50-DMA is the deepest of the five** (ATR multiple -6.01x, against -3.23x for IWM) — the mega-cap complex is the leg that broke, and it is also the leg that fell hardest on the tape (-3.76%, with SMH -7.83%).
- **The live tape repeats the settled divergence, on the same day.** RSP -0.74% against SPY -2.13% is a 1.39 pp spread in the equal-weight's favour, and the five best sectors are the defensive three plus real estate and energy. The index is being carried down by its biggest names while the average stock is not participating — which is the same BROAD reading the settled breadth gives, arrived at from the tape.
- **The breadth level is a 5.7 percentile — one of the lowest of the trailing year.** A level without a percentile is a number without a context; at this reading the participation base has effectively washed out, and the 50% size cut is the regime's own answer to that.
- **The universe moved again.** The count is 866 names today (865 in the previous two sessions' rows, 878 at the 2026-11-19 fire) — the market-cap floor is applied to the LATEST `valuation` row, so the population and the advance/decline denominator move between runs. The published 866 is today's population, not a frozen one.
- **Two sources disagree on the 2026-11-19 close.** shibui's settled close for SPY is 715.87 while Yahoo's 2026-11-19 session bar closes at 715.780 (IWM 264.22 vs 264.200, RSP 211.63 vs 211.690). The gap moves no 20-DMA or 50-DMA reading, but the two feeds are not interchangeable — flagged rather than reconciled.
- **`uncertainty` fires on a widening inversion.** VIX 31.69 against VIX3M 28.7 is a 10.42% gap, against 4.51% at the 2026-11-19 fire — the term structure is inverting harder, not healing.

## Method, source health & caveats

**Settled layer (data_date 2026-11-19).** All breadth, advance/decline, percentile and divergence numbers come from shibui through the MCP-over-HTTP bridge. shibui is T+1: at a 14:00 ET fire on 2026-11-20 its newest settled session is 2026-11-19, so the settled layer is one session behind the live tape by construction.

- **Universe** — NYSE/NASDAQ/AMEX, market cap > $10B (floor applied to the latest `valuation` row), **866 names** today. The universe is NOT frozen and the count moves as valuation rows refresh; it is published every run.
- **Advance/decline** — a real tally from `stock_quotes` with a `LAG()` self-join over the same indicator-joined population the breadth percentage uses, so advancing + declining + unchanged ties to the published universe count (73 + 789 + 3 = 866).
- **ADL** — cumulative net advances from **2026-08-26** (a level), with the 10-session OLS slope as the rate. The slope needs a full 10-session window and is published blank otherwise.
- **Percentiles** — against the trailing 1-year distribution of the same series: 263 sessions, 2025-11-04 → 2026-11-19. Bands: ABOVE_NORMAL ≥ 80, BELOW_NORMAL ≤ 20, NORMAL in between.
- **Divergence** — large-cap breadth % above the 20-DMA minus the index ETFs' share above their own 20-DMA, in percentage points. BROAD ≥ +15 pp, NARROW ≤ -15 pp.
- **Index positioning** — the five index ETFs' own 20-DMA / 50-DMA from shibui, measured on the 2026-11-19 settled close. `atr_extensions` is non-empty (5 symbols), so `late_cycle` was computed, not defaulted.

**Live layer (2026-11-20, 14:00:00 ET).** Yahoo's chart API 5-minute bars, pinned to the fire day and the fire clock: the index proxies, the five index ETFs, the eleven sector ETFs, SMH, and the ^VIX / ^VIX3M pair (both symbols from the same bar). The pair was taken from the same pinned series, so the artifact's Volatility section and the regime payload's `uncertainty` flag are the same pair.

**Source health.**

| Source | Use | Status |
|---|---|---|
| shibui via MCP bridge (`stock_data_query`) | settled breadth, A/D, index positioning | ok |
| Yahoo chart API (5-minute bars, pinned) | live tape, sector rotation, volatility pair | ok |
| Cboe delayed-quote CDN (`_VIX/_VIX3M`) | volatility pair | **blocked** — HTTP 403 (Cloudflare) from this egress; the pinned Yahoo fallback served the pair |
| bridge `market-recap` `get_quotes` | live ETF tape | not used — on a delayed replay it would serve a later session's quotes, not this session's tape |
| MCP availability probe | catalog check | ok — the finance MCPs are reached over the bridge; this is not a degradation |

**Degraded sources: 2.** (1) The Cboe delayed-quote CDN is HTTP 403 from this egress, so the volatility pair and the tape came from the pinned Yahoo fallback rather than the primary source. (2) The scheduled fire was blocked by the platform for 2585 minutes before this turn's first tool call (no error recorded in this session's transcript), and this artifact is the resumed replay of that fire.

**Caveats.** The trailing series is recomputed each run against the LATEST valuation snapshot, so a historical breadth percentage can shift slightly between runs. The live tape is a reconstruction from pinned 5-minute bars, not a live print — the numbers are what the tape showed at the fire, but they carry no quote-stamp jitter and no bid/ask information. No source number in this artifact is a cap-weight stand-in for a real advance/decline tally.
