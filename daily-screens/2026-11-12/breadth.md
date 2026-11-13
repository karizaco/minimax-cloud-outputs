---
artifact: breadth
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-12 18:30 ET"
data_date: "2026-11-12 (the SETTLED session this cron reads — 16:00 ET close from the TradingView scanner; the feed is NOT T+1 for this file)"
breadth_universe: "NYSE/NASDAQ/AMEX, type stock+dr, market_cap_basic > $10B, 1107 names"
vix_quote_time: "2026-11-12T16:15:01 (Cboe delayed-quote CDN)"
vix_pair: "VIX 18.7 / VIX3M 20.06 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-12/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
index_below_20sma: true
breadth_pct_spx: 53.03
---

# Breadth & Regime — Thursday, 12 November 2026 (end-of-day, cron #09)

The settled 16:00 ET close of 2026-11-12, read from the TradingView scanner. This is the end-of-day counterpart to `breadth-snapshot.md` (cron #10, 14:00 ET) — the two are meant to differ: #10 is a live mid-session tape, this is the close. Where they disagree, the intraday read is the one that has aged.

> **Reconstruction note.** This fire was scheduled for 2026-11-12 18:30 ET and the work was completed at 2026-11-13 08:47 ET — a delayed replay of the 2026-11-12 session. Every number below describes the **2026-11-12 settled close**; the anchor was re-verified against shibui's own settled bars (SPY 757.12, RSP 220.72, QQQ 688.17 — identical on both feeds).

## TL;DR

- **Breadth is 53.03% above the 20-DMA** on 1107 large caps, but the session itself was soft: advance/decline **244 / 859 / 4** (ratio 0.28, net -615), median name -0.90%.
- **The divergence is +13.03 pp — MATCHED.** 2 of 5 index ETFs are above their own 20-DMA, so the broad universe is still ahead of the index, but not by enough to leave the MATCHED band.
- **Caveat that changes how to read it:** VIX 18.7 / VIX3M 20.06 (ratio 0.9322) with `uncertainty: false`, but **QQQ is -4.24% versus its own 50-DMA while RSP is +2.68%** — the cap-weighted index is the weak leg even though half the universe is still above its 20-DMA.

## Breadth — the settled session

| Metric | Value |
|---|---|
| Universe | 1107 names (NYSE/NASDAQ/AMEX, type stock+dr, market_cap_basic > $10B) |
| % above 20-DMA | **53.03%** |
| % above 50-DMA | 52.3% |
| % above 200-DMA | 49.41% |
| Advance / decline / unchanged | **244 / 859 / 4** (ratio 0.28, net -615) |
| Median name | -0.90% |
| VIX / VIX3M | **VIX 18.7 / VIX3M 20.06** (prior session 17.49 / 19.24) |

| Index ETF | Close | Chg | vs 20-DMA | vs 50-DMA |
|---|---|---|---|---|
| SPY | 757.12 | -0.35% | -0.31% | -1.00% |
| RSP | 220.72 | -0.87% | +1.11% | +2.68% |
| QQQ | 688.17 | -0.32% | -1.26% | -4.24% |
| QQQE | 116.58 | -0.95% | -0.27% | -1.83% |
| IWM | 278.44 | -1.64% | +0.15% | -0.95% |

## Breadth divergence — broad market versus index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+13.03 pp — MATCHED** |
| large-cap % above 20-DMA | 53.03% |
| index ETFs above 20-DMA | 2 of 5 (40%) |

A MATCHED reading means the broad universe and the index ETFs broadly agree — the average large cap is neither materially healthier nor materially weaker than the index.

## Regime

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (breadth 53.03% is far above the 40% trigger) |
| `uncertainty` | **false** (VIX 18.7 / VIX3M 20.06, ratio 0.9322) |
| `late_cycle` | **false** (no index ETF more than 6% above its 50-DMA; the extreme is RSP at +2.68%) |
| `index_below_20sma` | **true** (2 of 5 index ETFs above their 20-DMA) |

## Flags

- **The index is the weak leg:** QQQ is -4.24% versus its own 50-DMA while RSP is +2.68%. Breadth above the 20-DMA survives because the tape has been sliding, not because the index is leading.
- **A/D and breadth disagree in sign:** 53.03% of names are above their 20-DMA, yet only 244 of 1107 advanced today. Breadth is a LEVEL, A/D is a RATE — read them together.
- **No 1-year breadth percentile is published here.** That needs the trailing session series for this universe, which this routine does not pull. The level is published without it and the gap is stated rather than filled with a guess.

## Method, source health & caveats

| Source | Used for | Status |
|---|---|---|
| TradingView scanner (`america/scan`) | the settled close of 2026-11-12: % above the 20/50/200-DMA, the advance/decline tally, the five index ETF rows | ok — `totalCount` asserted (1107 = 1107) |
| Cboe delayed-quote CDN | the VIX 18.7 / VIX3M 20.06 pair | ok — pulled twice, 20 s apart, identical both times (`vix_stable: true`) |
| shibui over the MCP-over-HTTP bridge | the settled-close anchor for the five index ETFs | ok — SPY/RSP/QQQ identical on both feeds |

- **This is the SETTLED close, not a live tape.** The scanner's `close` for 2026-11-12 is the 16:00 ET print, and it was re-verified against shibui's settled bars after the replay.
- **The volatility pair is ONE pair** — VIX 18.7 / VIX3M 20.06, quote time 2026-11-12T16:15:01 (Cboe delayed-quote CDN). No mid-session print is mixed with the settled close anywhere in this document. The prior session's pair (17.49 / 19.24) is quoted once, from the published 2026-11-11 end-of-day read.
- **The `late_cycle` extension map is non-empty** (5 index symbols), so the flag was computed rather than defaulted.
- **The universe is not frozen** — the market-cap floor is applied to the scanner's `market_cap_basic`, and that row refreshes, so the count moves session to session. Publish it every run; do not treat a change as a data error.

_Generated for the 2026-11-12 18:30 ET fire of cron #09 (stock-screener-daily-sweep-18:30); published 2026-11-13 08:47 ET._
