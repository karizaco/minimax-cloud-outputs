---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-18 14:01:01 ET"
data_date: "2026-11-17"
live_date: "2026-11-18"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 877 names"
vix_quote_time: "2026-11-18T13:47:31 ET (Cboe delayed-quote CDN (_VIX.json / _VIX3M.json))"
vix_pair: "VIX 23.54 / VIX3M 23.53 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-18/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
---
_contract: breadth-artifact-v1 · data_date 2026-11-17 · universe 877 names · breadth 39.11% (pctile 17.9 · BELOW_NORMAL) · divergence +39.11 pp (BROAD) · AD 163/713/1_

# Breadth & Regime Snapshot — Wednesday, 18 November 2026 (intraday, cron #10)

Intraday breadth read, fired **2026-11-18 14:01 ET** on the live tape. The settled breadth numbers describe the **2026-11-17** close (shibui is T+1); the tape and the volatility pair are **live 2026-11-18 at ~14:02 ET**. The two layers are never blended.

## TL;DR

- **Breadth broke down.** 39.11% of the 877 large caps are above their own 20-DMA (percentile 17.9, BELOW_NORMAL), down from 51.54% a session earlier; 53.02% are above the 50-DMA (percentile 35.1, NORMAL). The 2026-11-17 session itself was a broad down day — 163 advancing against 713 declining, and the 10-session ADL slope has turned to -49.45 net advances per session.
- **The divergence is the story: +39.11 pp, BROAD (percentile 90.5).** All five index ETFs (SPY, RSP, QQQ, QQQE, IWM) are below their own 20-DMA while 39% of the large-cap universe is still above it — the average large cap is materially healthier than the index, so the index is the weak leg, not the average stock.
- **Read it as a level, not as live participation.** The BROAD spread is a 20-DMA reading that lags the tape: the session it describes was broadly negative, and today's tape is mixed (SPY -0.07%, QQQ +0.49%, IWM +0.72%, DIA -0.93%) with energy (-3.03%) and health care (-1.83%) dragging while discretionary leads (+2.15%).

## Breadth — 2026-11-17 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 877 |
| Above 20-DMA | 343 (39.11%) |
| Below 20-DMA | 534 (60.89%) |
| Above 50-DMA | 465 (53.02%) |
| Index ETFs above their own 20-DMA | 0 of 5 (0.0%) |
| Index ETFs above their own 50-DMA | 1 of 5 (20.0%) |
| Advance/decline — settled session | 163 advancing / 713 declining / 1 unchanged (A/D ratio 0.229) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **877 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-11-04 | 630 | 246 | 1 | +384 | -717 | 87.25 |
| 2026-11-05 | 150 | 725 | 2 | -575 | -1292 | 80.19 |
| 2026-11-06 | 368 | 504 | 5 | -136 | -1428 | 41.05 |
| 2026-11-09 | 732 | 142 | 3 | +590 | -838 | 40.86 |
| 2026-11-10 | 395 | 476 | 6 | -81 | -919 | 28.82 |
| 2026-11-11 | 571 | 302 | 4 | +269 | -650 | 26.82 |
| 2026-11-12 | 218 | 656 | 3 | -438 | -1088 | 19.75 |
| 2026-11-13 | 530 | 339 | 8 | +191 | -897 | 14.36 |
| 2026-11-16 | 232 | 640 | 5 | -408 | -1305 | 1.07 |
| 2026-11-17 | 163 | 713 | 1 | -550 | -1855 | -49.45 |

**A/D ratio 0.229 today** (163 advancing / 713 declining). Over the last 10 sessions the net advances total **-754** and the ADL slope is **-49.45 net advances per session** (10-session A/D ratio 0.841). The ADL is cumulative from 2026-08-24, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (262 sessions, 2025-11-03 → 2026-11-17). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 39.11% | — | — |
| `breadth_pctile_1y` | 17.9 | — | BELOW_NORMAL |
| `breadth_pct_50dma` | 53.02% | — | — |
| `breadth_pctile_1y_50dma` | 35.1 | — | NORMAL |
| `index_etfs_above_20dma` | 0 of 5 | 15.6 | BELOW_NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +39.11 pp | BROAD | 90.5 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-11 | +9.56 |
| 2026-11-12 | +22.94 |
| 2026-11-13 | +42.83 |
| 2026-11-16 | +51.54 |
| 2026-11-17 | +39.11 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 269.05 | 278.12 | 279.79 | -3.84% | -2.36 |
| QQQ | 656.95 | 689.58 | 715.49 | -8.18% | -5.2 |
| QQQE | 111.98 | 116.29 | 118.35 | -5.38% | -4.19 |
| RSP | 215.76 | 218.93 | 214.96 | +0.37% | 0.36 |
| SPY | 732.44 | 755.86 | 763.15 | -4.02% | -3.83 |

## Live tape — 2026-11-18

Index levels (Cboe delayed quote CDN, 13:47:35 ET) and the live ETF tape (bridge `market-recap`, 14:02 ET) — live 2026-11-18, market open.

| Index | Last | Change | Quote time |
|---|---|---|---|
| ^SPX | 7,351.25 | +0.15% | 13:47:35 ET (delayed) |
| ^NDX | 27,195.62 | +0.72% | 13:47:35 ET (delayed) |
| ^RUT | 2,733.49 | +1.17% | 13:47:35 ET (delayed) |
| ^DJX | 503.93 | -0.72% | 13:47:35 ET (delayed) |

| Index ETF | Last | Change | Prior close | Quote time |
|---|---|---|---|---|
| SPY | 731.930 | -0.07% | 732.440 | 14:02:53 ET |
| QQQ | 660.190 | +0.49% | 656.950 | 14:02:54 ET |
| IWM | 270.990 | +0.72% | 269.050 | 14:02:50 ET |
| RSP | 216.061 | +0.14% | 215.760 | 14:02:50 ET |
| DIA | 502.595 | -0.93% | 507.310 | 14:02:51 ET |

**Sector rotation (live, 14:02 ET)** — the tape is rotating away from energy and health care and into consumer discretionary:

| Sector ETF | Sector | Last | Change |
|---|---|---|---|
| XLY | Consumer discretionary | 119.615 | +2.15% |
| XLC | Communication | 106.150 | +0.85% |
| XLU | Utilities | 43.650 | +0.53% |
| XLK | Technology | 163.780 | +0.32% |
| XLRE | Real estate | 43.680 | +0.21% |
| XLI | Industrials | 164.990 | +0.15% |
| XLP | Consumer staples | 91.530 | +0.08% |
| XLB | Materials | 50.480 | -0.71% |
| XLF | Financials | 56.560 | -0.89% |
| XLV | Health care | 181.845 | -1.83% |
| XLE | Energy | 61.440 | -3.03% |

Semiconductors (SMH) 457.75 (-0.51%) — it traded as high as 469.50 and reversed 2.50% off that high, while QQQ held +0.49%.

## Volatility — single pair, live

**23.54 / 23.53** — VIX 23.54, VIX3M 23.53, one pair, quoted at 13:47:31 ET from the Cboe delayed-quote CDN (_VIX.json / _VIX3M.json).

- Session mode: regular hours — live print.
- Prior close: VIX 25.46 (-7.54%), VIX3M 24.98 (-5.80%) — volatility is coming off the highs but is still elevated.
- VIX/VIX3M = 1.0004 — at/just above parity, which is what sets `uncertainty: true`.
- Two pulls 30 s apart returned the same pair (`vix_stable: true`), so this is a live print rather than a settling artefact.

This is the ONLY volatility pair in this document. It is live, not settled — the settled sections above never carry a VIX number.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 50 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **RSP is the only one of the five index ETFs still above its own 50-DMA** (+0.37%), while SPY (-4.02%), QQQ (-8.18%), QQQE (-5.38%) and IWM (-3.84%) sit below theirs. The BROAD divergence is a 20-DMA reading; on the 50-DMA horizon the equal-weight index is the healthy one — flagging the two horizons disagreeing rather than picking one.
- **QQQ's -8.18% distance from its 50-DMA is the largest of the five**, with an ATR multiple of -5.2x — the mega-cap complex is the leg that broke.
- **The universe count fell to 877 names** (890 at the 2026-11-17 fire, 914 at the 2026-11-12 fire). The market-cap floor is applied to the latest `valuation` row, so the population — and the advance/decline denominator — moves between runs.
- **`uncertainty` fires on a rounding-scale difference**: VIX 23.54 vs VIX3M 23.53 is a 0.04% gap, so the flag is technically true but marginal.

## Method, source health & caveats

**Settled layer (data_date 2026-11-17).** All breadth, advance/decline, percentile and divergence numbers come from shibui through the MCP-over-HTTP bridge (6 calls, one session). shibui is T+1: at a 14:00 ET fire on 2026-11-18 its newest settled session is 2026-11-17, so the settled layer is one session behind the live tape by construction.

- **Universe** — NYSE/NASDAQ/AMEX, market cap > $10B (floor applied to the latest `valuation` row), **877 names** today. The universe is NOT frozen and the count moves as valuation rows refresh; it is published every run.
- **Advance/decline** — a real tally from `stock_quotes` with a `LAG()` self-join over the same indicator-joined population the breadth percentage uses, so advancing + declining + unchanged ties to the published universe count (163 + 713 + 1 = 877).
- **ADL** — cumulative net advances from **2026-08-24** (a level), with the 10-session OLS slope as the rate. The slope needs a full 10-session window and is published blank otherwise.
- **Percentiles** — against the trailing 1-year distribution of the same series: 262 sessions, 2025-11-03 → 2026-11-17. Bands: ABOVE_NORMAL ≥ 80, BELOW_NORMAL ≤ 20, NORMAL in between.
- **Divergence** — large-cap breadth % above the 20-DMA minus the index ETFs' share above their own 20-DMA, in percentage points. BROAD ≥ +15 pp, NARROW ≤ -15 pp.
- **Index positioning** — the five index ETFs' own 20-DMA / 50-DMA from shibui, measured on the 2026-11-17 settled close. `atr_extensions` is non-empty (5 symbols), so `late_cycle` was computed, not defaulted.

**Live layer (2026-11-18, ~14:02 ET).** Bridge `market-recap` `get_quotes` for the index and sector ETFs (17 symbols, one batched call, `market_state: open`), the Cboe delayed-quote CDN for the index levels (13:47:35 ET) and for the VIX/VIX3M pair (13:47:31 ET). The two layers are never blended: the breadth numbers are settled, the tape and the volatility pair are live.

**Source health.**

| Source | Use | Status |
|---|---|---|
| shibui via MCP bridge (`stock_data_query`) | settled breadth, A/D, index positioning | ok |
| bridge `market-recap` `get_quotes` | live index + sector ETF tape | ok |
| Cboe delayed-quote CDN (`_SPX/_NDX/_RUT/_DJX`) | live index levels | ok |
| Cboe delayed-quote CDN (`_VIX/_VIX3M`) | volatility pair | ok (stable across two pulls) |
| MCP availability probe | catalog check | ok — 136 tools, 0 registered finance MCPs (the servers are reached over the bridge; this is not a degradation) |

**Caveats.** The trailing series is recomputed each run against the LATEST valuation snapshot, so a historical breadth percentage can shift slightly between runs — the 2026-11-16 breadth reads 51.54% in today's CSV against 51.01% in the 2026-11-17 artifact (a different universe: 877 vs 890 names). The live tape's index levels are the Cboe's ~15-minute delayed stamp while the ETF quotes are live. No source failed and no number in this artifact is a cap-weight stand-in for a real tally.
