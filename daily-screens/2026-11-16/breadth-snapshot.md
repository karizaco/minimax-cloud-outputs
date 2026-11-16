---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-16 14:01:00 ET"
data_date: "2026-11-13"
live_date: "2026-11-16"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 899 names"
vix_quote_time: "2026-11-16 13:46:31 ET (Cboe delayed-quote CDN — ~16 min delayed vs the snapshot clock)"
vix_pair: "VIX 23.47 / VIX3M 23.13 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-16/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 0
uncertainty: true
late_cycle: false
---
_contract: breadth-artifact-v1 · data_date 2026-11-13 · universe 899 names · breadth 61.96% (pctile 67.3 · NORMAL) · divergence +41.96 pp (BROAD) · AD 537/354/8_

# Breadth & Regime Snapshot — Monday, 16 November 2026 (intraday, cron #10)

Intraday breadth & regime read — fired **2026-11-16 14:01:00 ET**. The settled layer describes the **2026-11-13** session (shibui is T+1, so at a Monday fire the newest settled session is the prior Friday); the tape and the volatility pair are **live 2026-11-16**. Sources of record — settled layer: the shibui MCP server over the HTTPS bridge; live tape: the `market-recap` bridge (`get_quotes`, Yahoo-sourced), pulled 14:02:58 ET; volatility pair: the Cboe delayed-quote CDN, quote stamp 13:46:31 ET.

## TL;DR

- **Breadth did:** **61.96%** of the **899-name** large-cap universe closed above its own 20-DMA on the 2026-11-13 settled session (63.85% above the 50-DMA) — the 20-DMA level sits at the **67.3** percentile of its own trailing year (**NORMAL**), while the 50-DMA split is at the **80.0** percentile (**ABOVE_NORMAL**). Participation was positive: **537 advancing / 354 declining / 8 unchanged** (A/D ratio **1.517**, net **+183**), with the 10-session ADL slope at **+13.67 net advances per session**.
- **The one divergence that changes position sizing: +41.96 pp, band BROAD, 1-year percentile 93.5** — only **1 of the 5 index ETFs** (RSP) sits above its own 20-DMA, so the cap-weighted index is the weak leg while the average large cap is not. The spread widened in each of the last three sessions (+9.30 → +22.18 → +41.96 pp).
- **The caveat that changes how to read it:** the settled layer is Friday 2026-11-13, and today's live tape is a broad risk-off session — SPX −1.73%, NDX −2.36%, and the VIX **+21.61%** to 23.47 with the front month now **inverted above VIX3M** (ratio 1.015), which flips the `uncertainty` regime flag to **true** for the first time in this published series. Read the settled breadth as a posture, not as today's tape.

## Breadth — 2026-11-13 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 899 |
| Above 20-DMA | 557 (61.96%) |
| Below 20-DMA | 342 (38.04%) |
| Above 50-DMA | 574 (63.85%) |
| Index ETFs above their own 20-DMA | 1 of 5 (20.0%) |
| Index ETFs above their own 50-DMA | 1 of 5 (20.0%) |
| Advance/decline — settled session | 537 advancing / 354 declining / 8 unchanged (A/D ratio 1.517) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **899 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-11-02 | 588 | 311 | 0 | +277 | -578 | 62.48 |
| 2026-11-03 | 355 | 542 | 2 | -187 | -765 | 62.57 |
| 2026-11-04 | 646 | 252 | 1 | +394 | -371 | 85.59 |
| 2026-11-05 | 154 | 743 | 2 | -589 | -960 | 77.78 |
| 2026-11-06 | 382 | 511 | 6 | -129 | -1089 | 38.65 |
| 2026-11-09 | 752 | 144 | 3 | +608 | -481 | 39.61 |
| 2026-11-10 | 399 | 494 | 6 | -95 | -576 | 28.3 |
| 2026-11-11 | 585 | 309 | 5 | +276 | -300 | 27.35 |
| 2026-11-12 | 221 | 675 | 3 | -454 | -754 | 20.25 |
| 2026-11-13 | 537 | 354 | 8 | +183 | -571 | 13.67 |

**A/D ratio 1.517 today** (537 advancing / 354 declining). Over the last 10 sessions the net advances total **+284** and the ADL slope is **+13.67 net advances per session** (10-session A/D ratio 1.066). The ADL is cumulative from 2026-08-20, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (260 sessions, 2025-11-03 → 2026-11-13). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 61.96% | — | — |
| `breadth_pctile_1y` | 67.3 | — | NORMAL |
| `breadth_pct_50dma` | 63.85% | — | — |
| `breadth_pctile_1y_50dma` | 80.0 | — | ABOVE_NORMAL |
| `index_etfs_above_20dma` | 1 of 5 | 29.2 | NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +41.96 pp | BROAD | 93.5 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-09 | +27.41 |
| 2026-11-10 | +27.07 |
| 2026-11-11 | +9.30 |
| 2026-11-12 | +22.18 |
| 2026-11-13 | +41.96 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 277.54 | 278.38 | 280.76 | -1.15% | -0.71 |
| QQQ | 679.89 | 695.45 | 717.87 | -5.29% | -3.39 |
| QQQE | 115.84 | 116.84 | 118.65 | -2.37% | -1.86 |
| RSP | 221.16 | 218.65 | 214.98 | +2.87% | 2.82 |
| SPY | 754.37 | 759.02 | 764.43 | -1.32% | -1.26 |

## Live tape — 2026-11-16

| Instrument | Last | Chg | Chg % | Prior close | Volume | Day range | As of (ET) |
|---|---|---|---|---|---|---|---|
| S&P 500 (^GSPC) | 7,430.66 | -131.01 | -1.73% | 7,561.67 | 1,483,900,000 | 7,406.87–7,515.60 | 14:02:57 |
| Nasdaq 100 (^NDX) | 27,283.12 | -660.62 | -2.36% | 27,943.74 | 851,288,411 | 27,152.02–27,621.64 | 14:02:56 |
| Russell 2000 (^RUT) | 2,740.77 | -49.72 | -1.78% | 2,790.49 | not published | 2,736.47–2,777.41 | 13:47:54 |
| Dow (^DJI) | 51,704.04 | -643.51 | -1.23% | 52,347.55 | 389,686,016 | 51,601.34–52,324.00 | 14:02:57 |
| SPY (S&P 500) | 741.13 | -13.24 | -1.76% | 754.37 | 27,739,410 | 738.73–749.82 | 14:02:57 |
| RSP (S&P 500 equal weight) | 219.27 | -1.90 | -0.86% | 221.16 | 6,176,679 | 218.62–221.25 | 14:02:53 |
| QQQ (Nasdaq 100) | 663.73 | -16.16 | -2.38% | 679.89 | 25,492,776 | 660.53–672.14 | 14:02:56 |
| QQQE (Nasdaq-100 equal weight) | 113.89 | -1.95 | -1.68% | 115.84 | 104,168 | 113.48–114.94 | 14:02:28 |
| IWM (Russell 2000) | 273.21 | -4.34 | -1.56% | 277.54 | 14,334,441 | 271.97–276.54 | 14:02:53 |

**Live participation read:** RSP −0.86% against SPY −1.76% — a **+0.90 pp** spread in favour of the equal-weight line; QQQE −1.68% against QQQ −2.38% — **+0.70 pp**. That is a cap-weight participation proxy (**not an advance/decline tally**) — no live A/D count was computed, and the advance/decline counts in this artifact are the **settled** 2026-11-13 tally. The live tape is nevertheless repeating the settled divergence's shape: the cap-weighted index is the weak leg while the average name holds up better.

Source: market-recap MCP bridge (`get_quotes`, Yahoo-sourced), pulled 2026-11-16 14:02:58 ET; regular session **live** (`market_state: open` on every line). The indices are quoted on their own tickers — the Cboe index prints are a ~16-minute delayed feed and are used only as a staleness cross-check, never as the published level.

## Volatility — single pair, live

| Pair | Level | Chg | Chg % | Prior close | Quote time (ET) |
|---|---|---|---|---|---|
| VIX | 23.47 | +4.17 | +21.61% | 19.30 | 2026-11-16 13:46:31 |
| VIX3M | 23.13 | +2.51 | +12.17% | 20.62 | 2026-11-16 13:46:31 |

**One pair, used everywhere in this document: VIX 23.47 / VIX3M 23.13** — ratio **1.015**, **backwardation**: the front month is now **above** the 3-month, so the `uncertainty` regime flag flips to **true**. The two prior published fires were both in contango and both carried the flag false (2026-11-12: 18.02 / 19.66 = 0.917; 2026-11-13: 19.29 / 20.57 = 0.938). The prior closes above are the 2026-11-13 settles, so the +21.61% is today's move measured against Friday — the same session the settled breadth layer describes.

Source: Cboe delayed-quote CDN (`_VIX.json` / `_VIX3M.json`). The pair is pulled **twice** during the run and the two pulls are compared:
- pull 1: VIX 23.47 / VIX3M 23.13 at 2026-11-16T13:46:31 ET
- pull 2: VIX 23.47 / VIX3M 23.13 at 2026-11-16T13:46:31 ET

⇒ `vix_stable: true` — the two pulls agree to within 0.01. Session mode: regular hours — live print. **The stamp gap:** the published pair is stamped 13:46:31 ET while the snapshot clock is 14:03 ET — the CDN's ~16-minute delay, disclosed rather than hidden. The live layer reuses this one reading rather than pulling a third time, so this artifact carries exactly one volatility pair.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

1. **VIX — the front month is inverted against its own 3-month.** 23.47 against 23.13 (ratio 1.015) — the pair's term structure has flipped into backwardation, and that flip is what drives the `uncertainty` regime flag to true. Both pulls agree, so this is the feed's reading, not a flapping quote; the level itself is a ~16-minute delayed print.
2. **VIX — a delayed print of a fast-moving series.** Stamped 2026-11-16 13:46:31 ET against a snapshot clock of 14:03 ET, with the level **+21.61%** above the 19.30 prior settle. On a series that moved this much today the stamp gap is material: a same-minute quote could differ, and the published number is the feed's stamp rather than a live second.
3. **QQQE — a thin line.** Volume **104,168** shares against QQQ's **25,492,776** (0.4% of the share count), and an `as_of` stamp of 14:02:28 ET against 14:02:56 ET for the rest of the tape. Its −1.68% — and the +0.70 pp QQQE-vs-QQQ spread — is a thin-line read; the participation story rests on the SPY/RSP pair.
4. **Russell 2000 — the feed publishes no volume and a 15-minute-old stamp.** `^RUT`'s `volume` is null and its `as_of` is 13:47:54 ET against 14:02:57 ET for the other three indices, so its −1.78% is stale relative to the rest of the tape. The IWM ETF line (14:02:53 ET, volume 14,334,441) is the usable small-cap read.
5. **Cboe index print against the market-recap print.** Cboe SPX reads 7,418.64 at 13:46:33 ET against market-recap's 7,430.66 at 14:02:57 ET (NDX 27,226.37 against 27,283.12; RUT 2,739.63 against 2,740.77). The gap is the Cboe feed's delay, not a data error — the tape uses the fresher market-recap print, and the Cboe feed is used only for the volatility pair.

## Method, source health & caveats

**Sources tried, and their status.**

| Source | Used for | Status |
|---|---|---|
| shibui MCP server over the HTTPS bridge (`stock_data_query`) | the settled layer — breadth, the advance/decline tally, the 10-session ADL, the index-ETF series, the ATR extensions | OK |
| Cboe delayed-quote CDN (`_VIX.json`, `_VIX3M.json`) | the single VIX/VIX3M pair | OK — ~16-minute delayed feed, pulled twice, both pulls agree |
| market-recap MCP bridge (`get_quotes`, Yahoo-sourced) | the live tape — 4 indices and 5 index ETFs | OK — live regular session, one pull at 14:02:58 ET |
| TradingView scanner, Nasdaq quote API, Yahoo chart API | — | not called; under this contract the settled layer's source of record is shibui and the live layer is covered by the two sources above |

**The universe is not frozen.** The market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **899 names**, down from **901** in the 2026-11-13 fire and **914** in the 2026-11-12 fire. The venue list and the $10B floor are unchanged, so the series stays comparable; the drift does move the numbers slightly — the 2026-11-12 divergence re-reads **+22.18 pp** here against the **+22.26 pp** the 2026-11-13 fire published for that same session, for the same reason.

**Settled vs live.** `data_date` **2026-11-13** is the SETTLED session the breadth numbers describe (shibui is T+1, so at a Monday fire its newest settled session is the prior Friday). `live_date` **2026-11-16** is the LIVE tape session. The two are never blended. The two layers are anchored to the same settle: SPY's settled close in the breadth layer (754.37) is exactly the live tape's prior close.

**Percentile windows.** The percentiles are against the trailing 1-year distribution of the same series (**260 sessions**, 2025-11-03 → 2026-11-13); the ADL base date is **2026-08-20** and the published A/D window is 2026-11-02 → 2026-11-13. The A/D tally uses the SAME population as the breadth percentage (the indicator-joined large-cap set), so advancing + declining + unchanged = 537 + 354 + 8 = **899**, the published universe count.

**`atr_extensions`.** Present and non-empty — IWM −1.15%, QQQ −5.29%, QQQE −2.37%, RSP +2.87%, SPY −1.32%. `late_cycle` is false because no index ETF is more than 6% above its own 50-DMA (the largest extension is RSP at +2.87%). The producer emits the index identifier as `ticker`, so the extension map is read from that key — an empty map would mean a failed probe, not a quiet `late_cycle = false`.

**One volatility reading.** The helper pulled the pair twice and both pulls agree; the live layer reuses that one reading rather than pulling again, so this artifact contains exactly one VIX/VIX3M pair and no second volatility number.

**Degraded probes: none.** No `probe_failed:` marker applies to this run.
