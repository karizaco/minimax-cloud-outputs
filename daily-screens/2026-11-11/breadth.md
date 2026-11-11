---
artifact: breadth
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-11 18:30 ET"
data_date: "2026-11-11 (the SETTLED session this cron reads — 16:00 ET close from the TradingView scanner; the feed is NOT T+1 for this file)"
breadth_universe: "NYSE/NASDAQ/AMEX, type stock+dr, market_cap_basic > $10B, 1114 names"
vix_quote_time: "2026-11-11T16:15:01 (Cboe delayed-quote CDN)"
vix_pair: "VIX 17.49 / VIX3M 19.24 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-11/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
index_below_20sma: false
breadth_pct_spx: 63.73
---

# Breadth & Regime — Wednesday, 11 November 2026 (end-of-day, cron #09)

The settled 16:00 ET close of 2026-11-11, read from the TradingView scanner. This is the end-of-day counterpart to `breadth-snapshot.md` (cron #10, 14:00 ET) — the two are meant to differ: #10 is a live mid-session tape, this is the close. Where they disagree, the intraday read is the one that has aged.

## TL;DR

- **Breadth is 63.73% above the 20-DMA** on 1114 large caps, with advance/decline at **675 / 425 / 14** (ratio 1.59) — a firm, broad session, not a narrow one.
- **The divergence is +3.73 pp — MATCHED.** The broad universe and the index ETFs agree: 3 of 5 index ETFs are above their own 20-DMA. Participation is not hiding inside the mega-caps.
- **Caveat that changes how to read it:** VIX 17.49 / VIX3M 19.24 (ratio 0.9090) with `uncertainty: false`, but **QQQ is -3.99% below its own 50-DMA** while RSP is +3.60% above it — the cap-weighted index is the weak leg even though the average stock is fine.

## Breadth — the settled session

| Metric | Value |
|---|---|
| Universe | 1114 names (NYSE/NASDAQ/AMEX, type stock+dr, market_cap_basic > $10B) |
| % above 20-DMA | **63.73%** |
| % above 50-DMA | 55.48% |
| % above 200-DMA | 50.81% |
| Advance / decline / unchanged | **675 / 425 / 14** (ratio 1.59, net +250) |
| Median name | +0.25% |
| VIX / VIX3M | **VIX 17.49 / VIX3M 19.24** (prior 19.46 / 20.64; ratio 0.9090) |

| Index ETF | Close | Chg | vs 20-DMA | vs 50-DMA |
|---|---|---|---|---|
| SPY | 759.81 | +1.32% | -0.05% | -0.67% |
| RSP | 222.65 | +0.80% | +2.13% | +3.60% |
| QQQ | 690.38 | +2.31% | -1.22% | -3.99% |
| QQQE | 117.70 | +2.24% | +0.55% | -0.94% |
| IWM | 283.09 | +0.89% | +1.88% | +0.59% |

## Breadth divergence — broad market versus index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+3.73 pp — MATCHED** |
| large-cap % above 20-DMA | 63.73% |
| index ETFs above 20-DMA | 3 of 5 (60%) |

A MATCHED reading means the broad universe and the index ETFs agree — the average large cap is neither materially healthier nor materially weaker than the index.

## Regime

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (breadth 63.73% is far above the 40% trigger) |
| `uncertainty` | **false** (VIX 17.49 / VIX3M 19.24, ratio 0.9090) |
| `late_cycle` | **false** (no index ETF more than 6% above its 50-DMA; the extreme is RSP at +3.60%) |
| `index_below_20sma` | **false** (3 of 5 index ETFs above their 20-DMA) |

## Flags

- **QQQ is the weak leg:** -3.99% below its 50-DMA while RSP is +3.60% above it. The cap-weighted index is not participating as strongly as the average stock.
- **No 1-year breadth percentile is published here.** That needs the trailing session series for this universe, which this routine does not pull. The level is published without it and the gap is stated rather than filled with a guess.

## Method, source health & caveats

| Source | Used for | Status |
|---|---|---|
| TradingView scanner (`america/scan`) | the settled close of 2026-11-11: % above the 20/50/200-DMA, the advance/decline tally, the five index ETF rows | ok — `totalCount` asserted (2307 = 2307) |
| Cboe delayed-quote CDN | the VIX 17.49 / VIX3M 19.24 pair | ok — pulled twice, 20 s apart, identical both times (`vix_stable: true`) |
| shibui over the MCP-over-HTTP bridge | the T+1 cross-check on 2026-11-10 (7 rows) | ok — one call |

- **This is the SETTLED close, not a live tape.** The scanner's `close` for 2026-11-11 is the 16:00 ET print. The intraday read (`breadth-snapshot.md`, cron #10) was taken at 14:00 ET on the same session and is expected to differ.
- **The volatility pair is ONE pair** — VIX 17.49 / VIX3M 19.24, quote time 2026-11-11T16:15:01 (Cboe delayed-quote CDN). No mid-session print is mixed with the settled close anywhere in this document.
- **The `late_cycle` extension map is non-empty** (5 index symbols), so the flag was computed rather than defaulted.
- **The shibui cross-check is a DIFFERENT population** (market cap from `shibui.valuation` vs the scanner's `market_cap_basic`), so its level is not interchangeable with the published number. It is published as a cross-check only.

_Generated 2026-11-11 by cron #09 (stock-screener-daily-sweep-18:30) at 2026-11-11 18:30 ET._
