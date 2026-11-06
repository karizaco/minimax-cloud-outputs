---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-06 14:00:51 ET"
data_date: "2026-11-05"
live_date: "2026-11-06"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 891 names"
vix_quote_time: "2026-11-06 13:48:46 ET (Cboe delayed-quote CDN, 15-minute delayed)"
vix_pair: "VIX 24.54 / VIX3M 23.68 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-06/breadth.md (fire day); same-session end-of-day read: daily-screens/2026-11-05/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 0
uncertainty: true
late_cycle: false
---
_contract: breadth-artifact-v1 · data_date 2026-11-05 · universe 891 names · breadth 59.26% (pctile 60.3 · NORMAL) · divergence +39.26 pp (BROAD) · AD 155/734/2_

# Breadth & Regime Snapshot — Friday, 06 November 2026 (intraday, cron #10)

Friday 06 November 2026 · 14:00 ET intraday snapshot. The breadth numbers describe the **settled 2026-11-05 session** (shibui is T+1); the tape and the volatility pair are **live 2026-11-06** as of 13:48 ET. Two sessions, two labels, never blended. Source of record for the live layer: Cboe delayed-quote CDN, cross-checked against Nasdaq and the `market-recap` bridge.

## TL;DR

- **Breadth fell but stayed normal.** 59.26% of 891 large caps are above their 20-DMA (1-year percentile 60.3, band NORMAL) after the 11-05 AI-trade rout — the *level* is unremarkable; the damage was in the session, not in the trend.
- **The divergence is the story: +39.26 pp, band BROAD, 91st percentile.** The average large cap is 39 points healthier than the index ETFs — only **1 of 5** index ETFs sits above its own 20-DMA. The mega-caps are the weak leg, not the strong one.
- **Caveat that changes how to read it: today's tape is the mirror image.** At 13:48 ET RSP is **-0.05%** while SPY is +0.73% and QQQ +1.71% — the relief bounce is megacap-led and the broad market is not participating. BROAD describes the settled 11-05 session, not today's posture.

## Breadth — 2026-11-05 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 891 |
| Above 20-DMA | 528 (59.26%) |
| Below 20-DMA | 363 (40.74%) |
| Above 50-DMA | 505 (56.68%) |
| Index ETFs above their own 20-DMA | 1 of 5 (20.0%) |
| Index ETFs above their own 50-DMA | 1 of 5 (20.0%) |
| Advance/decline — settled session | 155 advancing / 734 declining / 2 unchanged (A/D ratio 0.211) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **891 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-10-23 | 261 | 628 | 2 | -367 | -1716 | 88.78 |
| 2026-10-26 | 515 | 371 | 5 | +144 | -1572 | 82.61 |
| 2026-10-27 | 452 | 436 | 3 | +16 | -1556 | 71.11 |
| 2026-10-28 | 457 | 429 | 5 | +28 | -1528 | 45.67 |
| 2026-10-29 | 666 | 225 | 0 | +441 | -1087 | 65.81 |
| 2026-10-30 | 376 | 515 | 0 | -139 | -1226 | 67.28 |
| 2026-11-02 | 587 | 304 | 0 | +283 | -943 | 61.33 |
| 2026-11-03 | 347 | 542 | 2 | -195 | -1138 | 62.22 |
| 2026-11-04 | 650 | 240 | 1 | +410 | -728 | 86.13 |
| 2026-11-05 | 155 | 734 | 2 | -579 | -1307 | 80.58 |

**A/D ratio 0.211 today** (155 advancing / 734 declining). Over the last 10 sessions the net advances total **+42** and the ADL slope is **+80.58 net advances per session** (10-session A/D ratio 1.009). The ADL is cumulative from 2026-08-12, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (262 sessions, 2025-10-22 → 2026-11-05). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 59.26% | — | — |
| `breadth_pctile_1y` | 60.3 | — | NORMAL |
| `breadth_pct_50dma` | 56.68% | — | — |
| `breadth_pctile_1y_50dma` | 51.9 | — | NORMAL |
| `index_etfs_above_20dma` | 1 of 5 | 28.2 | NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +39.26 pp | BROAD | 91.2 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-10-30 | +24.31 |
| 2026-11-02 | +25.99 |
| 2026-11-03 | +24.53 |
| 2026-11-04 | +29.92 |
| 2026-11-05 | +39.26 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 270.98 | 277.11 | 282.63 | -4.12% | -2.57 |
| QQQ | 647.05 | 712.40 | 722.27 | -10.41% | -6.81 |
| QQQE | 111.52 | 118.12 | 119.36 | -6.57% | -5.24 |
| RSP | 216.87 | 216.57 | 214.89 | +0.92% | 0.91 |
| SPY | 733.00 | 765.53 | 766.40 | -4.36% | -4.23 |

## Live tape — 2026-11-06

**Indices** (Cboe delayed-quote CDN, 13:48–13:49 ET, 15-minute delayed)

| Index | Level | Change | Quote time (ET) |
|---|---|---|---|
| S&P 500 (SPX) | 7,407.00 | +0.72% | 13:48:55 |
| Nasdaq 100 (NDX) | 27,066.72 | +1.64% | 13:49:55 |
| Russell 2000 (RUT) | 2,758.04 | +1.03% | 13:49:55 |

**Index ETFs** — the shape matters more than the level

| ETF | Last | Change | 11-05 settle |
|---|---|---|---|
| SPY | 738.37 | +0.73% | 733.00 |
| QQQ | 658.14 | **+1.71%** | 647.05 |
| QQQE | 112.30 | +0.70% | 111.52 |
| RSP (equal weight) | 216.76 | **-0.05%** | 216.87 |
| IWM | 274.23 | +1.20% | 270.98 |
| DIA | 514.45 | +0.04% | 514.27 |

The equal-weight ETF is **flat while the cap-weighted index is up** — today is a megacap-led bounce, and that is the opposite shape to the settled 11-05 session, where the broad market fell far harder than the index. Three independent feeds agree on the shape: Cboe (13:48 ET) SPY +0.73% / QQQ +1.71% / RSP -0.05%; Nasdaq (14:04 ET) SPY +0.76% / QQQ +1.81% / RSP -0.06%; `market-recap` bridge (14:05 ET) SPY +0.72% / QQQ +1.77% / RSP -0.11%.

**Sector rotation** (11 SPDR sectors, 13:48 ET)

| Sector ETF | Change | | Sector ETF | Change |
|---|---|---|---|---|
| XLK (tech) | +1.58% | | XLI (industrials) | +0.46% |
| XLC (comm. svc) | +0.99% | | XLV (health care) | +0.22% |
| XLY (cons. disc.) | +0.70% | | XLU (utilities) | +0.13% |
| XLE (energy) | +0.54% | | XLB (materials) | -0.06% |
| | | | XLF (financials) | -0.07% |
| | | | XLRE (real estate) | -0.16% |
| | | | XLP (staples) | **-0.69%** |

Leadership is the 11-05 losers: tech and communication services lead, while staples, real estate and financials lag. Defensive and rate-sensitive sectors did not participate in the bounce, and small caps (+1.20% IWM) underperformed the Nasdaq 100 (+1.64%).

## Volatility — single pair, live

**One pair, one timestamp, used everywhere in this document.**

| Contract | Last | Change | Prior settle |
|---|---|---|---|
| VIX | 24.54 | -12.92% | 28.18 |
| VIX3M | 23.68 | -7.32% | 25.55 |

- **VIX/VIX3M = 1.036** — the front month is still above the 3-month, so the term structure is **inverted** and the regime flag `uncertainty` is **true**.
- The pair was pulled **twice** and both pulls returned 24.54 / 23.68 at 13:48:46 ET (`vix_stable: true`) — one number per field, no mid-session/settled mix.
- The 11-05 settle of **28.18** is Cboe's own prior-close field and matches the reported close exactly (a +69.7% one-day jump from 16.61 — the third-largest percentage rise in the VIX since 1990, after the 11-03 midterm result repriced the AI-infrastructure trade).
- Today's 24.54 is a **partial retrace of that shock, not a normalised market**: the VIX is still 48% above its 11-04 close, and the curve has not yet returned to contango.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

1. **The universe denominator moved under a fixed filter — 891 names today, 18 fewer than the 909 published for the previous snapshot (2026-11-05, describing the 11-04 settle).** The venue list (NYSE/NASDAQ/AMEX) and the $10B market-cap floor are unchanged; the `valuation` snapshot behind the floor refreshed, so the denominator changed while the filter did not. The drop reconciles exactly: the previous artifact's 11-04 tally was **658 advancing / 250 declining / 1 unchanged** on 909 names, and the same session on today's 891-name set is **650 / 240 / 1** — the 8 + 10 difference is precisely the 18 names that fell out of the universe. Every percentage on this page is computed on the 891-name set; do not read it against a 909-name denominator as if the population were unchanged.
2. **The 11-05 session net and the 10-session ADL slope point in opposite directions, and the two are not in conflict.** The session net is **-579 advances** (155 advancing / 734 declining / 2 unchanged, A/D ratio 0.211), while the 10-session ADL slope still reads **+80.58 net advances per session** and the 10-session net is **+42**. All three are correct and they reconcile: the 10-session net sums the 10 bars from 2026-10-23 to 2026-11-05 and therefore carries 10-23's own -367, whereas the cumulative ADL has risen **+409** since 10-23's close (-1716 → -1307). The slope is an OLS fit over the last 10 cumulative points, so a single -579 bar bends the level without flipping the fitted rate. Quote the session net for what happened on 11-05 and the slope for the trend — never one for the other.
3. **The settled divergence and the live tape point opposite ways.** The settled 11-05 read is BROAD (+39.26 pp: the average large cap healthier than the index); today's live tape is narrow (RSP -0.05% against SPY +0.73%). Read the band as a description of the session it was measured on, not as today's posture.
4. **`late_cycle` is false while the index is deeply below its 50-DMA.** QQQ sits **-10.41%** below its own 50-DMA (the deepest of the five), but the rule fires only when an index ETF is **more than 6% above** its 50-DMA. The flag's silence is an artefact of that rule, not a sign that the index is unstretched. `atr_extensions` is populated with all five ETFs, so the flag was computed on real data.

## Method, source health & caveats

- **Settled layer — source of record:** shibui via the MCP-over-HTTP bridge. Four aggregate queries: the universe and its valuation snapshot, the 20/50-DMA split, the `LAG()` advance/decline self-join, and the index-ETF positioning rows. The universe is the indicator-joined large-cap set, so `advancing + declining + unchanged` equals the published 891 exactly — no second denominator is mixed in.
- **T+1 split:** shibui's newest settled session at this fire is **2026-11-05**, so `data_date` = 2026-11-05 and `live_date` = 2026-11-06. The 11-05 close is independently confirmed: SPX settled at 7,353.73 on 11-05, which matches Cboe's prior-close field exactly. The settled and live layers are never blended into one number.
- **Live layer:** Cboe delayed-quote CDN (`_SPX`, `_NDX`, `_RUT`, `_VIX`, `_VIX3M`, SPY, QQQ, QQQE, RSP, IWM, DIA and the 11 SPDR sector ETFs), 15-minute delayed — quote times 13:48–13:49 ET. Cross-checks: Nasdaq `/info` (14:04–14:05 ET) and the `market-recap` bridge (14:05 ET). All three agree on sign and on the narrow shape; the largest spread between them is 0.09 pp (RSP).
- **Independent cross-check of the settled layer — cron #09's end-of-day read of the same session** (`daily-screens/2026-11-05/breadth.md`, 18:30 ET, published from the TradingView scanner on a *different* population — 981 names, no domicile filter): it reads breadth **58.31%** against this artifact's **59.26%**, advance/decline **145 / 832 / 4** against **155 / 734 / 2**, divergence **+38.31 pp** against **+39.26 pp**, and — on the part that is population-independent — **1 of the 5 index ETFs above its 20-DMA (RSP)**, `size_cut_pct` 0 and `uncertainty` true, all three identical. The two reads are **not two measurements of one series** (different universes, different market-cap sources), so the ~1 pp breadth gap is a population difference, not a data conflict; the matching ETF count and regime flags are the meaningful agreement.
- **Percentile windows:** 262 sessions, 2025-10-22 → 2026-11-05, expanding (each row is ranked against every session from the start of the window to that row).
- **Volatility pair:** pulled twice within the run, identical both times (`vix_stable: true`). `vix_stable` and the pair's quote time are carried in `breadth-snapshot.json`.
- **Session context (sourced, not inferred):** the 11-05 session was an AI-trade rout on fears that the Democratic midterm sweep would slow AI data-centre build-out — Nasdaq Composite -5.5%, S&P 500 -4.36%, semiconductors -12%. Today's driver is the October jobs report released 08:30 ET (payrolls **+165K** vs ~59–65K expected, unemployment **4.1%** from 4.2%, prior two months revised +84K), which added to market pricing for a December rate hike. **There is no FOMC meeting today** — the Fed's 2026 calendar has no November meeting and the next decision is 8-9 December.
- **Delivery note:** this file is the first publication of the 11-05 session's breadth — the previous snapshot (`daily-screens/2026-11-05/breadth-snapshot.md`, cron #10, 14:00 ET on 11-05) describes the 11-04 settle, so day-over-day continuity rests on the trailing series in the CSV rather than on a file-to-file diff.
- **Degradation:** none. No source in this run failed or was rate-limited.
