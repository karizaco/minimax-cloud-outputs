---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-13 14:01:01 ET"
data_date: "2026-11-12"
live_date: "2026-11-13"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 901 names"
vix_quote_time: "2026-11-13 13:50:31 ET (Cboe delayed-quote CDN)"
vix_pair: "VIX 19.29 / VIX3M 20.57 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-13/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---
_contract: breadth-artifact-v1 · data_date 2026-11-12 · universe 901 names · breadth 62.26% (pctile 69.1 · NORMAL) · divergence +22.26 pp (BROAD) · AD 222/676/3_

# Breadth & Regime Snapshot — Friday, 13 November 2026 (intraday, cron #10)

Intraday breadth read, fired 2026-11-13 14:01:01 ET (Friday). **The breadth numbers below describe the SETTLED session of 2026-11-12** — shibui is T+1, so on the 2026-11-13 fire its newest settled session is the prior day. **The tape and the volatility pair are LIVE**, each timestamped on its own block. Universe: NYSE/NASDAQ/AMEX, market cap > $10B, 901 names. Source of record for the settled layer: the shibui MCP server over the HTTPS bridge.

## TL;DR

- **Breadth did:** 62.26% of the 901 large caps closed above their own 20-DMA on 2026-11-12 — a **NORMAL** reading at the **69.1** percentile of its own trailing 1-year distribution, down from 69.37% at the 94.3 percentile (ABOVE_NORMAL) on 2026-11-11.
- **The one divergence that changes position sizing: +22.26 pp (BROAD, 1-year percentile 72.9)** — the average large cap is materially healthier than the index ETFs, of which only 2 of 5 sit above their own 20-DMA. The cap-weighted index is the weak leg, not the average stock.
- **The caveat that changes how to read it:** the settled session itself was a down session — **222 advancing against 676 declining** (ratio 0.328, net -454), against 594/315 in the prior fire's settled session. A NORMAL breadth level with a BROAD divergence means participation is intact while the index sells off, and the live tape repeats the same shape.

## Breadth — 2026-11-12 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 901 |
| Above 20-DMA | 561 (62.26%) |
| Below 20-DMA | 340 (37.74%) |
| Above 50-DMA | 562 (62.38%) |
| Index ETFs above their own 20-DMA | 2 of 5 (40.0%) |
| Index ETFs above their own 50-DMA | 1 of 5 (20.0%) |
| Advance/decline — settled session | 222 advancing / 676 declining / 3 unchanged (A/D ratio 0.328) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **901 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-10-30 | 374 | 527 | 0 | -153 | -1119 | 70.68 |
| 2026-11-02 | 588 | 313 | 0 | +275 | -844 | 63.48 |
| 2026-11-03 | 358 | 541 | 2 | -183 | -1027 | 63.47 |
| 2026-11-04 | 645 | 255 | 1 | +390 | -637 | 86.18 |
| 2026-11-05 | 153 | 746 | 2 | -593 | -1230 | 77.65 |
| 2026-11-06 | 384 | 511 | 6 | -127 | -1357 | 38.15 |
| 2026-11-09 | 754 | 144 | 3 | +610 | -747 | 38.99 |
| 2026-11-10 | 401 | 494 | 6 | -93 | -840 | 27.81 |
| 2026-11-11 | 587 | 309 | 5 | +278 | -562 | 27.22 |
| 2026-11-12 | 222 | 676 | 3 | -454 | -1016 | 20.48 |

**A/D ratio 0.328 today** (222 advancing / 676 declining). Over the last 10 sessions the net advances total **-50** and the ADL slope is **+20.48 net advances per session** (10-session A/D ratio 0.989). The ADL is cumulative from 2026-08-19, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (262 sessions, 2025-10-29 → 2026-11-12). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 62.26% | — | — |
| `breadth_pctile_1y` | 69.1 | — | NORMAL |
| `breadth_pct_50dma` | 62.38% | — | — |
| `breadth_pctile_1y_50dma` | 74.0 | — | NORMAL |
| `index_etfs_above_20dma` | 2 of 5 | 43.5 | NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +22.26 pp | BROAD | 72.9 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-06 | +55.60 |
| 2026-11-09 | +27.26 |
| 2026-11-10 | +26.93 |
| 2026-11-11 | +9.26 |
| 2026-11-12 | +22.26 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 278.44 | 278.02 | 281.12 | -0.95% | -0.59 |
| QQQ | 688.17 | 696.94 | 718.62 | -4.24% | -2.72 |
| QQQE | 116.58 | 116.90 | 118.76 | -1.83% | -1.44 |
| RSP | 220.72 | 218.30 | 214.96 | +2.68% | 2.63 |
| SPY | 757.12 | 759.47 | 764.80 | -1.00% | -0.96 |

## Live tape — 2026-11-13

| Instrument | Last | Chg | Chg % | Prior close | Volume | Day range | As of (ET) |
|---|---|---|---|---|---|---|---|
| S&P 500 (^GSPC) | 7554.35 | -38.05 | -0.50% | 7592.4 | 1,475,518,000 | 7499.4–7621.78 | 14:04:51 |
| Nasdaq 100 (^NDX) | 27923.48 | -365.708 | -1.29% | 28289.188 | 963,713,246 | 27609.713–28295.799 | 14:04:50 |
| Russell 2000 (^RUT) | 2784.4487 | -14.6116 | -0.52% | 2799.0603 | — | 2763.7166–2805.902 | 13:49:50 |
| Dow (^DJI) | 52294.54 | -2.55 | +0.00% | 52297.09 | 420,978,671 | 52017.86–52521.48 | 14:04:50 |
| SPY (S&P 500) | 753.35 | -3.77 | -0.50% | 757.12 | 20,544,305 | 747.89–760.12 | 14:04:50 |
| RSP (S&P 500 equal weight) | 220.92 | +0.2 | +0.09% | 220.72 | 3,869,908 | 219.43–221.82 | 14:04:43 |
| QQQ (Nasdaq 100) | 679.435 | -8.735 | -1.27% | 688.17 | 27,685,877 | 671.71–688.75 | 14:04:50 |
| QQQE (Nasdaq 100 equal weight) | 115.7 | -0.88 | -0.75% | 116.58 | 103,333 | 114.685–116.67 | 14:01:26 |
| IWM (Russell 2000) | 276.985 | -1.455 | -0.52% | 278.44 | 11,247,082 | 274.665–279.16 | 14:04:50 |

Source: market-recap MCP bridge (`get_quotes`, Yahoo-sourced), pulled 2026-11-13 14:05:54 ET; regular session **live**. Indices are quoted on their own tickers — the Cboe index prints are a ~15-minute delayed feed and are used only as the volatility pair below.

## Volatility — single pair, live

| Pair | Level | Chg | Chg % | Prior close | Session range | Quote time (ET) |
|---|---|---|---|---|---|---|
| VIX | 19.29 | +0.59 | +3.16% | 18.7 | 18.13–20.92 | 2026-11-13 13:50:31 |
| VIX3M | 20.57 | +0.51 | +2.54% | 20.06 | 19.77–21.48 | 2026-11-13 13:50:31 |

**One pair, used everywhere in this document: VIX 19.29 / VIX3M 20.57** — ratio **0.938**, contango — VIX below VIX3M, so the `uncertainty` regime flag stays **false**. The level, the change, the prior close and the quote time are the helper's own pull; the session-range column is the intraday low–high of the same feed as of its pull at 14:06:49 ET.

Source: Cboe delayed-quote CDN (_VIX.json / _VIX3M.json). The pair is pulled **twice** during the run and the two pulls are compared:
- pull 1: VIX 19.29 / VIX3M 20.57 at 2026-11-13T13:50:31 ET
- pull 2: VIX 19.29 / VIX3M 20.57 at 2026-11-13T13:50:31 ET

⇒ `vix_stable: true` — the two pulls agree to within 0.01 (VIX 19.29 → 19.29).

Session mode: regular hours — live print.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | false | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

1. **VIX — the published pair is a delayed print.** The Cboe feed serves a ~15-minute delayed quote; the pair is stamped 2026-11-13 13:50:31 ET while the snapshot clock is 14:05:54 ET, and the session high is 20.92 — the published 19.29 sits 1.63 points below that high. The two pulls agree to within 0.01, so the print itself is stable — but it is still not a same-minute quote.
2. **QQQE — a thin line.** Volume 103,333 shares against QQQ's 27,685,877 (≈0.4% of the share count), and its `as_of` stamp is 14:01:26 ET against 14:04:50 ET for the rest of the tape. Its -0.75% is a thin-line read — the Nasdaq-100 equal-weight comparison is correspondingly noisier than the SPY/RSP pair, which is the pair the divergence story actually rests on.
3. **Nasdaq 100 — the two index feeds disagree by 0.07 pp.** The Cboe print reads 27904.9277 (stamped 2026-11-13T13:51:35 ET) against the market-recap/Yahoo print 27923.48 (14:04:50 ET). The gap is the Cboe feed's staleness, not a data error; the live tape uses the fresher market-recap print and the Cboe feed is used only for the volatility pair.

## Method, source health & caveats

**Sources tried, and their status.**

| Source | Used for | Status |
|---|---|---|
| shibui MCP server over the HTTPS bridge (`stock_data_query`) | the settled layer — breadth, advance/decline tally, the 10-session ADL, the index-ETF series, the ATR extensions | OK |
| Cboe delayed-quote CDN (`_VIX.json`, `_VIX3M.json`) | the single VIX/VIX3M pair | OK — ~15-minute delayed feed, pulled twice |
| market-recap MCP bridge (`get_quotes`, Yahoo-sourced) | the live tape — 5 index ETFs and 4 indices | OK — live regular session |
| TradingView scanner, Nasdaq quote API, Yahoo chart API | — | not called; the settled layer's source of record under this contract is shibui, and the live layer is covered by the two sources above |

**The universe is not frozen.** The market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **901 names**, down from **914** in the 2026-11-12 fire and **905** in the 2026-11-11 fire. The venue list and the $10B floor are unchanged, so the series stays comparable; the drift does move the numbers slightly — the 2026-11-11 divergence re-reads +9.26 pp here against the +9.37 pp yesterday's artifact published for that same session, for the same reason.

**Settled vs live.** `data_date` **2026-11-12** is the SETTLED session the breadth numbers describe (shibui is T+1, so on a 2026-11-13 fire its newest settled session is the prior day). `live_date` **2026-11-13** is the LIVE tape session. The two are never blended.

**Percentile windows.** The percentiles are against the trailing 1-year distribution of the same series (262 sessions, 2025-10-29 → 2026-11-12); the ADL base date is 2026-08-19. The A/D tally uses the SAME population as the breadth percentage (the indicator-joined large-cap set), so advancing + declining + unchanged = 901.

**`atr_extensions`.** Present and non-empty — IWM -0.95%, QQQ -4.24%, QQQE -1.83%, RSP +2.68%, SPY -1.00%. `late_cycle` is false because no index ETF is more than 6% above its own 50-DMA (the largest extension is RSP). The producer emits the index identifier as `ticker`, so the extension map is read from that key — an empty map would mean a failed probe, not a quiet `late_cycle = false`.

**Degraded probes: none.** No `probe_failed:` marker applies to this run.
