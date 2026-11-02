---
cron: 10-stock-screener-breadth-snapshot
date: 2026-11-02
fire_time_et: 14:00
artifact_built_et: 14:06
read_type: intraday (live tape) — 14:00 ET cron #10
data_date: 2026-10-30
data_date_note: >
  shibui is an end-of-day feed and its latest settled bar at this 14:00 ET fire is the
  2026-10-30 (Fri) close. The breadth percentages and moving averages below describe that
  2026-10-30 session. Today's 2026-11-02 session is still in progress, so the live tape and
  the volatility pair below are 2026-11-02 intraday. The two are labelled separately and are
  never blended into one number.
breadth_universe: "NYSE / NASDAQ / AMEX, market cap > $10B, 904 names"
vix_quote_time: "2026-11-02 13:48:31 ET (Cboe delayed-quote CDN, _VIX.json / _VIX3M.json)"
vix_pair: "VIX 20.05 / VIX3M 20.90 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-02/breadth.md (cron #09, 18:30 ET)"
regime: "size_cut 0% · uncertainty false · late_cycle false"
source: "shibui via MCP-over-HTTP bridge (breadth) + market-recap bridge / Cboe delayed-quote CDN (live tape, volatility)"
---

# Breadth & Regime Snapshot — 2026-11-02 (intraday, 14:00 ET)

## Headline

Breadth is healthy but the cap-weighted index is not: **63.7% of the 904 large caps are above
their 20-DMA (2026-10-30 settle) while SPY itself sits below its own 20-DMA.** That gap is the
story of the tape today, and it is confirmed live — **RSP (equal weight) is +0.99% against SPY
+0.11%, a +0.88 pp spread.** The average stock is participating; mega-cap technology is not.
The tape also faded: SPY is 0.96% off its intraday high of 763.86 while **VIX is up 3.24% to
20.05** — volatility rising into a flat index is a fade signature, not a rally signature.

The catalyst is oil, not the economy. Brent fell ~7.6% and WTI ~7.1% on renewed U.S.–Iran
diplomacy, which crushed energy (XLE −3.40%) and handed the proceeds to fuel-sensitive
cyclicals (XLY +2.75%, XLB +2.00%, XLF +1.92%, XLI +1.54%). ISM Manufacturing (Oct) came in at
**55.5 vs 54.6 expected** (prior 54.5) with Prices Paid cooling to 75.2 vs 77.0 expected — a
growth beat with softer input-cost inflation.

## Breadth — 2026-10-30 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE / NASDAQ / AMEX, market cap > $10B |
| Names in universe | 904 |
| Above 20-DMA | 576 (63.72%) |
| Below 20-DMA | 328 (36.28%) |
| Index ETFs above their own 20-DMA | 2 of 5 (40%) — SPY, QQQ, QQQE below; RSP, IWM above |
| Index ETFs above their own 50-DMA | 1 of 5 (20%) — RSP only |

**Verified two independent ways.** The skill's `emit_breadth_sql()` returns 63.7168%; a
separate query that recomputes each name's 20-day average close directly from
`stock_quotes` (rather than reading `technical_indicators.sma_20`) returns **576 of 904 = the
same 63.7168%**. Both agree exactly.

### The divergence, quantified

| | 20-DMA (2026-10-30) | Live 2026-11-02 price | Position |
|---|---|---|---|
| SPY | 770.47 | 756.54 | **below** |
| RSP | 214.89 | 220.47 | above |
| QQQ | 728.19 | 687.76 | **below** |
| QQQE | 119.50 | 116.74 | **below** |
| IWM | 277.41 | 280.30 | above |

Live prices leave the index breadth reading **unchanged at 2 of 5 (40%)** — the settle and the
live tape agree on which indices are broken.

## Index positioning — distance from 50-DMA (2026-10-30)

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA |
|---|---|---|---|---|
| SPY | 755.72 | 770.47 | 767.49 | −1.53% |
| RSP | 218.31 | 214.89 | 215.05 | +1.52% |
| QQQ | 690.49 | 728.19 | 725.00 | −4.76% |
| QQQE | 116.29 | 119.50 | 119.94 | −3.04% |
| IWM | 279.33 | 277.41 | 284.27 | −1.74% |

No index is more than 6% above its 50-DMA → `late_cycle = false`. **Caveat on this column:** the
skill's SQL computes `atr_252d_avg` inside a CTE already filtered to a single date, so the
window function has one row to average and the value collapses to `atr_14` — the published
figure is distance-from-50-DMA, not a true ATR extension multiple. It is used here only for the
`late_cycle` flag, which it answers correctly.

## Live tape — 2026-11-02, ~13:48–14:05 ET

### Indices (Cboe delayed-quote CDN, 13:48 ET)

| Index | Level | Change |
|---|---|---|
| S&P 500 (SPX) | 7,597.88 | +0.24% |
| Nasdaq 100 (NDX) | 28,343.79 | −0.14% |
| Russell 2000 (RUT) | 2,821.73 | +0.35% |
| Dow Jones (DJX) | 52,256 | +0.94% |

### ETFs (market-recap bridge, 14:05 ET)

| Symbol | Price | Change | Prev close (2026-10-30) | Day high | Day low |
|---|---|---|---|---|---|
| SPY | 756.54 | +0.11% | 755.72 | 763.86 | 756.39 |
| RSP | 220.47 | **+0.99%** | 218.31 | 220.95 | 219.51 |
| QQQ | 687.76 | −0.40% | 690.49 | 699.43 | 687.59 |
| IWM | 280.30 | +0.35% | 279.33 | 283.19 | 280.23 |
| QQQE | 116.74 | +0.39% | 116.29 | 117.89 | 116.74 |
| DIA | 521.60 | +0.86% | 517.13 | 523.68 | 520.68 |

**RSP − SPY = +0.88 pp.** Every `prev close` above is the 2026-10-30 settle and matches
shibui's 2026-10-30 bar to the cent — an independent confirmation that the shibui date
resolution landed on the correct session.

### Sector rotation

| Sector ETF | 2026-11-02 intraday | 3 months (2026-07-31 → 2026-10-30, settled) |
|---|---|---|
| XLY — Consumer discretionary | **+2.75%** | −0.61% |
| XLB — Materials | +2.00% | +4.58% |
| XLF — Financials | +1.92% | −0.76% |
| XLP — Staples | +1.62% | +5.14% |
| XLI — Industrials | +1.54% | −6.92% |
| XLC — Communication services | +0.97% | −7.71% |
| XLRE — Real estate | +0.97% | −4.22% |
| XLU — Utilities | +0.69% | −2.08% |
| XLV — Health care | −0.16% | +13.74% |
| XLK — Technology | **−1.78%** | +2.37% |
| XLE — Energy | **−3.40%** | **+17.58%** |
| SPY | +0.11% | +1.16% |

Today's tape is a **full one-day reversal of the quarter's leadership**: energy, the best 3-month
sector at +17.58%, is the worst today at −3.40%; and health care, second-best at +13.74%, is
flat-to-red. The gainers today (discretionary, materials, financials, industrials) were among
the 3-month laggards. That is an oil-price rotation, not a growth rotation.

## Volatility — single pair, live

| Instrument | Value | Prev close | Change | Quote time (ET) | Source |
|---|---|---|---|---|---|
| VIX | **20.05** | 19.42 | +3.24% | 2026-11-02 13:48:31 | Cboe delayed-quote CDN `_VIX.json` |
| VIX3M | **20.90** | 20.78 | +0.58% | 2026-11-02 13:48:31 | Cboe delayed-quote CDN `_VIX3M.json` |

**VIX / VIX3M = 0.959** → below 1.0 → front-end vol is *not* elevated against the 3-month
curve, so `uncertainty = false`. The curve is in an orderly contango shape, but the front end is
rising faster than the back end (VIX +3.24% vs VIX3M +0.58%) on a flat index tape — a
short-dated hedging bid, not a stress signal.

**Cross-check:** Yahoo Finance's ^VIX page read 20.02 @ 12:49:46 PM CST (13:49:46 ET) against
Cboe's 20.05 @ 13:48:31 ET — 30 seconds apart, 0.15% apart, identical 19.42 prior close. Cboe
is the published figure.

## Regime

Computed with the skill's own `compute_regime()` over the unmodified breadth rows plus the
live VIX/VIX3M pair.

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | size cut triggers only when index is below 20-DMA **and** breadth < 40%. Breadth is 63.72%, so no cut. |
| `uncertainty` | **false** | VIX/VIX3M = 0.959 < 1.0 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA |
| `index_below_20sma` | true | only 2 of 5 index ETFs are above their 20-DMA |

**Read:** the regime flags are benign, but `index_below_20sma = true` alongside 63.7% breadth is
not a contradiction — it is the cap-concentration signature. The index is below its 20-DMA
because the mega-cap technology complex is below its 20-DMA, not because the average stock is.
Nothing in the regime flags calls for a size cut.

## Events in the window

- **No FOMC meeting in November 2026.** The last meeting was Oct 27–28 (a hawkish hold at
  3.75–4.00% on a 10–2 vote); the next is Dec 8–9 with SEP/dots. Today's volatility print is
  therefore **not** event-driven by the Fed.
- **ISM Manufacturing (Oct), 10:00 ET: 55.5 vs 54.6 expected** (prior 54.5). Prices Paid 75.2 vs
  77.0 expected (prior 77.9) — a growth beat with cooler input costs.
- **U.S.–Iran diplomacy**: President Pezeshkian said the Supreme Leader authorised the
  government to pursue dialogue; VP Vance reached out to Mohsen Rezaei. Brent −7.6% to ~$104.82,
  WTI −7.1% to ~$96.72 — the steepest one-day crude drop since July 27.
- **The week ahead**: U.S. midterm elections (Tue Nov 3), JOLTS + factory orders (Wed), ADP +
  ISM Services (Thu), **October nonfarm payrolls + UMich sentiment (Fri Nov 6)**, and Apple's
  earnings after today's bell.
- **Fed speakers**: Goolsbee at 11:15 ET, Senior Loan Officer Opinion Survey at 16:00 ET.

## Source health

| Source | Endpoint / query | Status | Notes |
|---|---|---|---|
| MCP catalog probe | `probe_mcp.py` | **ok** — `catalog_ok total=133 finance_tools=0` | no `mcp__*` finance tool registered; not an error |
| MCP bridge | `mcp_bridge.py` → `shibui stock_data_query` | **ok** | breadth, sector closes, universe count; latest bar 2026-10-30 |
| MCP bridge | `mcp_bridge.py` → `market-recap get_quotes` | **ok** | live ETF tape, as_of 2026-11-02 14:05:32 ET |
| MCP bridge | `mcp_bridge.py` → `market-recap top_movers` | **ok** | Yahoo predefined screener; 40/50 anonymous quota used |
| Cboe delayed-quote CDN | `cdn.cboe.com/.../\_VIX.json`, `_VIX3M.json`, `_SPX/_NDX/_RUT/_DJX` | **ok** | requires `curl -L` (307); plain ETF tickers work, underscore variants 403 |
| Yahoo ^VIX page | `finance.yahoo.com/quote/%5EVIX/` | **ok (cross-check only)** | 20.02 @ 13:49:46 ET vs Cboe 20.05 — page carries 25 decoy `regularMarketPrice` hits for other tickers |
| FOMC calendar | `federalreserve.gov/monetarypolicy/fomccalendars.htm` | **ok** | no November 2026 meeting |
| Press cross-check | AP / Benzinga / CNBC / Newsquawk, 2026-11-02 | **ok** | index levels and sector moves confirmed; press intraday snapshots are earlier in the session than the CBOE/bridge prints |

**errors: 0.** No source was blocked or rate-limited.

## Method & caveats

- The breadth percentages and the 20/50-DMA columns describe the **2026-10-30 settle**; the
  index/ETF levels and the volatility pair are **live 2026-11-02 intraday**. Both are labelled
  at every appearance. The 2026-11-02 close does not exist yet at 14:00 ET.
- **No live advance/decline tally exists on any reachable feed** (Nasdaq's marketmovers endpoint
  returns only top-mover tables). The RSP-vs-SPY spread (+0.88 pp) is the intraday breadth
  proxy, and it is the same cap-concentration signal the settled breadth measures.
- The `atr_extensions` column in `_regime-intraday.json` is distance-from-50-DMA, not a true ATR
  extension multiple, because of the single-row window bug in the skill's own SQL.
- The 3-month sector column is the 2026-07-31 → 2026-10-30 settled move; the intraday column
  is 2026-11-02 live. The two sessions are never mixed inside one number.
- The end-of-day counterpart for the 2026-10-30 session is cron #09's `breadth.md`; this file
  is the intraday read and is expected to differ from it (different VIX quote time, and #09
  draws its breadth from the settled close).
