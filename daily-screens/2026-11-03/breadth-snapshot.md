---
cron: 10-stock-screener-breadth-snapshot
date: 2026-11-03
fire_time_et: 14:00
artifact_built_et: 14:09
read_type: intraday (live tape) — 14:00 ET cron #10
data_date: 2026-11-02
data_date_note: >
  shibui is an end-of-day feed and its latest settled bar at this 14:00 ET fire is the
  2026-11-02 (Mon) close. The breadth percentages and moving averages below describe that
  2026-11-02 session. Today's 2026-11-03 session is still in progress, so the live tape and
  the volatility pair below are 2026-11-03 intraday. The two are labelled separately and are
  never blended into one number.
breadth_universe: "NYSE / NASDAQ / AMEX, market cap > $10B, 902 names"
vix_quote_time: "2026-11-03 13:49:31 ET (Cboe delayed-quote CDN, _VIX.json / _VIX3M.json)"
vix_pair: "VIX 20.51 / VIX3M 21.12 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-03/breadth.md (cron #09, 18:30 ET)"
regime: "size_cut 0% · uncertainty false · late_cycle false"
source: "shibui via MCP-over-HTTP bridge (breadth) + market-recap bridge / Cboe delayed-quote CDN (live tape, volatility)"
---

# Breadth & Regime Snapshot — 2026-11-03 (intraday, 14:00 ET)

## Headline

Breadth improved into the close of Monday and is **healthy: 65.19% of the 902 large caps are
above their 20-DMA**, up from 63.72% at the 2026-10-30 settle. But today's tape is the exact
mirror image of yesterday's: **the average stock is not participating in the bounce.** SPY is
+0.54% while RSP is −0.03% — a **−0.57 pp equal-weight spread** — and the leadership sits in
exactly the sectors that led nowhere over the past three months: **XLK +1.49%, XLI +1.27%,
XLC +1.21%**, while staples (XLP −1.63%) and materials (XLB −1.59%) lag. Yesterday oil dragged
tech down and energy up; today oil keeps falling and tech snaps back.

This is a rotation back into the beaten-down complex, not a new leadership. Over the settled
three months the biggest winners were energy (+14.39%) and health care (+13.78%) and the biggest
losers were communication services (−9.95%) and industrials (−7.34%) — and today the losers are
the winners. The Nasdaq-100, which entered a **correction** on Monday (more than 10% below its
October 6 closing peak), is +0.93% at midday.

Volatility is falling with the index: **VIX 20.51 (−3.03%) against VIX3M 21.12, a ratio of
0.971** — orderly contango, `uncertainty = false`. But note the clock: this is **election day**,
results come tonight, and the one macro print this morning (JOLTS) was a large beat that pushed
the 10-year yield up 6.4 bp to 4.958% — a rate headwind landing directly on the tech complex
that is leading today.

## Breadth — 2026-11-02 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE / NASDAQ / AMEX, market cap > $10B |
| Names in universe | 902 |
| Above 20-DMA | 588 (65.19%) |
| Below 20-DMA | 314 (34.81%) |
| Index ETFs above their own 20-DMA | 2 of 5 (40%) — SPY, QQQ, QQQE below; RSP, IWM above |
| Index ETFs above their own 50-DMA | 1 of 5 (20%) — RSP only |

**Verified two independent ways.** The skill's `emit_breadth_sql()` returns 65.1885%; a
separate query that recomputes each name's 20-day average close directly from `stock_quotes`
(rather than reading `technical_indicators.sma_20`) returns **588 of 902 = 65.18847%** — the same
number to the fourth decimal. Both agree exactly.

**Against yesterday's published reading:** 63.72% (10-30, 904 names) → 65.19% (11-02, 902
names). Breadth is genuinely improving, but the universe is not frozen — the market-cap filter is
applied to the latest `valuation` row, so it moved by two names as those rows refreshed. The
comparison is directionally valid, not a like-for-like universe diff.

### The divergence, quantified

| | 20-DMA (2026-11-02) | Live 2026-11-03 price | Position |
|---|---|---|---|
| SPY | 769.33 | 756.13 | **below** |
| RSP | 215.34 | 219.92 | above |
| QQQ | 724.43 | 687.12 | **below** |
| QQQE | 119.18 | 116.39 | **below** |
| IWM | 277.20 | 281.04 | above |

Live prices leave the index breadth reading **unchanged at 2 of 5 (40%)** — the settle and the
live tape agree on which indices are broken. The Nasdaq-100 and the equal-weight index have not
recovered their 20-DMAs; the bounce is not yet a trend change.

## Index positioning — distance from 50-DMA (2026-11-02 settle)

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple (close − 50DMA) ÷ atr_252d |
|---|---|---|---|---|---|
| SPY | 752.10 | 769.33 | 767.22 | −1.97% | −1.92 ATR |
| RSP | 219.98 | 215.34 | 215.02 | +2.31% | +2.29 ATR |
| QQQ | 681.09 | 724.43 | 724.35 | −5.97% | −3.94 ATR |
| QQQE | 115.89 | 119.18 | 119.80 | −3.26% | −2.62 ATR |
| IWM | 279.14 | 277.20 | 283.86 | −1.66% | −1.04 ATR |

No index is more than 6% above its 50-DMA, and none is more than 6 ATR extensions above it →
`late_cycle = false`. On the live tape RSP is +2.28% above its 50-DMA and every other index is
below; nothing changes the flag.

**Caveat on this table.** The skill's `extension_pct` column is `(close − sma_50)/sma_50` —
**distance from the 50-DMA, not an ATR extension**, despite the column name. The `atr_252d_avg`
that now sits beside it *is* a genuine trailing window in the current `emit_breadth_sql` (it no
longer collapses to `atr_14`, as it did before the skill's SQL was repaired), so the ATR-multiple
column above is computed here directly as `(close − sma_50) ÷ atr_252d_avg`. It is used only for
the `late_cycle` flag, which it answers identically.

## Live tape — 2026-11-03, ~13:49–14:05 ET

### Indices (Cboe delayed-quote CDN, 13:49–13:50 ET)

| Index | Level | Change |
|---|---|---|
| S&P 500 (SPX) | 7,585.35 | +0.58% |
| Nasdaq 100 (NDX) | 28,250.01 | +0.93% |
| Russell 2000 (RUT) | 2,828.38 | +0.80% |
| Dow Jones (DJX) | 51,854 | −0.25% |

The Dow is the only benchmark down — the same "Election Day trading splits the benchmarks"
pattern the press flagged at 10:26 ET (Dow −0.49%, S&P +0.38%, Nasdaq Composite +0.81%).
`DJX` is the Dow scaled by 1/100.

### ETFs (market-recap bridge, 14:05 ET)

| Symbol | Price | Change | Prev close (2026-11-02) | Day high | Day low |
|---|---|---|---|---|---|
| SPY | 756.13 | +0.54% | 752.10 | 757.07 | 752.41 |
| RSP | 219.92 | **−0.03%** | 219.98 | 220.50 | 218.55 |
| QQQ | 687.12 | +0.89% | 681.09 | 688.69 | 683.18 |
| QQQE | 116.39 | +0.43% | 115.89 | 116.69 | 115.85 |
| IWM | 281.04 | +0.68% | 279.14 | 282.00 | 279.34 |
| DIA | 517.94 | −0.27% | 519.34 | 518.36 | 515.19 |

**RSP − SPY = −0.57 pp.** Every `prev close` above is the 2026-11-02 settle and matches shibui's
2026-11-02 bar to the cent — for all 17 ETF symbols, not just the index five. That is an
independent confirmation that the shibui date resolution landed on the correct session. The
Cboe index `prev_day_close` values are the same session too: SPX 7,541.40, RUT 2,805.88 and
Dow 51,984 — all matching the independently published Monday closes to the decimal.

### Sector rotation

| Sector ETF | 2026-11-03 intraday | 3 months (2026-08-03 → 2026-11-02, settled) |
|---|---|---|
| XLK — Technology | **+1.49%** | −2.15% |
| XLI — Industrials | +1.27% | −7.34% |
| XLC — Communication services | +1.21% | **−9.95%** |
| XLV — Health care | +0.17% | +13.78% |
| XLU — Utilities | −0.19% | −1.56% |
| XLRE — Real estate | −0.23% | −3.41% |
| XLF — Financials | −0.37% | +0.31% |
| XLE — Energy | −0.36% | **+14.39%** |
| XLY — Consumer discretionary | −0.59% | −0.04% |
| XLB — Materials | −1.59% | +5.21% |
| XLP — Consumer staples | **−1.63%** | +7.04% |
| SPY | +0.54% | −0.74% |

Today's tape is a **full one-day reversal of yesterday's**: yesterday the quarter's leaders
(energy, health care) were the day's winners and tech was the loser; today the quarter's worst
three (communication services, industrials, technology) are the day's best three and the
quarter's best two (energy, health care) are flat-to-red. Energy has now given back three
sessions of leadership while oil keeps falling.

Two features of today's tape argue against reading it as a healthy broadening: the
**defensive sectors are the laggards** (staples −1.63%, utilities −0.19%, real estate −0.23%
— risk-on behaviour, not hedging), and the **equal-weight index is flat while cap-weight is
green**, which is the opposite of yesterday's +0.88 pp equal-weight spread.

## Volatility — single pair, live

| Instrument | Value | Prev close | Change | Quote time (ET) | Source |
|---|---|---|---|---|---|
| VIX | **20.51** | 21.15 | −3.03% | 2026-11-03 13:49:31 | Cboe delayed-quote CDN `_VIX.json` |
| VIX3M | **21.12** | 21.60 | −2.22% | 2026-11-03 13:49:31 | Cboe delayed-quote CDN `_VIX3M.json` |

**VIX / VIX3M = 0.971** → below 1.0 → front-end vol is *not* elevated against the 3-month
curve, so `uncertainty = false`. The curve is in an orderly contango shape and the front end is
falling faster than the back end (VIX −3.03% vs VIX3M −2.22%) as the index grinds higher —
a market that is not paying up for election-day uncertainty, at least not on this print.

**Cross-check:** Yahoo Finance's ^VIX page read 20.45 @ 12:50:31 PM CST (13:50:31 ET) against
Cboe's **20.51 @ 13:49:31 ET** — one minute apart, 0.29% apart, identical 21.15 prior close.
Cboe is the published figure.

## Regime

Computed with the skill's own `compute_regime()` over the unmodified breadth rows plus the
live VIX/VIX3M pair.

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | size cut triggers only when index is below 20-DMA **and** breadth < 40%. Breadth is 65.19%, so no cut. |
| `uncertainty` | **false** | VIX/VIX3M = 0.971 < 1.0 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (or 6 ATR extensions above it) |
| `index_below_20sma` | true | only 2 of 5 index ETFs are above their 20-DMA, settle and live alike |

**Read:** the regime flags are benign and unchanged from yesterday, but `index_below_20sma = true`
alongside 65.19% breadth is the same cap-concentration signature as yesterday, not a
contradiction — the index is below its 20-DMA because mega-cap technology is, not because the
average stock is. Nothing in the regime flags calls for a size cut.

## Events in the window

- **US midterm elections, today.** Polls close on a staggered schedule — Florida, Georgia and
  Virginia ~19:00 ET; Ohio and North Carolina ~19:30 ET; Maine, Michigan, Pennsylvania and Texas
  ~20:00 ET. Polls favour Democrats for the House, with the Senate still genuinely uncertain;
  "a divided government seems to be very good for markets" (Kim Forrest, Bokeh Capital).
  The session's pattern — Dow red while the Nasdaq and small caps are green — is the market
  pricing a lower-odds legislative outcome rather than an economic shock.
- **JOLTS (September), 10:00 ET: 7.523M job openings vs 7.100M expected** (August revised to
  7.190M). Hires +131k to 5.402M; layoffs −127k to 1.641M, the fewest since March 2025; quits
  up to 3.37M, the highest in ~18 months. A firmer labour market than expected — and the
  **10-year yield at 4.958%, up 6.4 bp** as of 10:26 ET. That is a rate headwind on the exact
  complex leading today.
- **No FOMC meeting in November 2026.** The last meeting was Oct 27–28 (a hawkish hold at
  3.75–4.00% on a 10–2 vote); the next is **Dec 8–9, with a SEP and dots**. Today's volatility
  print is therefore not event-driven by the Fed.
- **Oil keeps falling** — Brent −2.4% intraday, extending Monday's drop, with the US–Iran
  peace-deal story and a "defensive" strike on Qeshm Island priced and then unpriced.
- **Earnings after today's bell: AMD.** Monday's prints are still driving the tape — Apple
  −4.4% pre-market on memory-chip cost guidance, Palantir −6.1% despite a revenue beat. NVDA
  +2.8%, MRVL +4.6%, INTC +4.3% and AMD +4.2% pre-earnings into the bounce.
- **The week ahead:** ADP + ISM Services + trade balance (Wed Nov 4), **October nonfarm payrolls
  (Fri Nov 6, 08:30 ET)** with the street at +65k and unemployment 4.2%.
- **Seasonality is with the bulls** into the election result, and the Nasdaq-100 sits just above
  its 200-day after entering a correction on Monday (51% of its constituents in bear markets).

## Source health

| Source | Endpoint / query | Status | Notes |
|---|---|---|---|
| MCP catalog probe | `probe_mcp.py` | **ok** — `catalog_ok total=135 finance_tools=0` | no `mcp__*` finance tool registered; not an error |
| MCP bridge | `mcp_bridge.py` → `shibui stock_data_query` | **ok** | 4 calls: date resolution, breadth, independent recompute, sector rotation; latest bar 2026-11-02 |
| MCP bridge | `mcp_bridge.py` → `market-recap get_quotes` | **ok** | live ETF tape, as_of 2026-11-03 14:05:05 ET; `market_state: open` |
| Cboe delayed-quote CDN | `cdn.cboe.com/.../_VIX.json`, `_VIX3M.json`, `_SPX/_NDX/_RUT/_DJX` | **ok** | requires `curl -L` (307); prints are stamped 13:49–13:50 ET, ~15 min behind the 14:05 fetch |
| Yahoo ^VIX page | `finance.yahoo.com/quote/%5EVIX/` | **ok (cross-check only)** | 20.45 @ 13:50:31 ET vs Cboe 20.51 — page carries decoy `regularMarketPrice` hits for other tickers |
| FOMC calendar | `federalreserve.gov/monetarypolicy/fomccalendars.htm` | **ok** | no November 2026 meeting; next Dec 8–9 |
| BLS release calendar + JOLTS | `bls.gov/schedule/2026/11_sched_list.htm`, Reuters/AP reports | **ok** | September JOLTS, 10:00 ET |
| Press cross-check | Reuters / Schwab / Barron's / PRNewswire-CNBC, 2026-11-03 | **ok** | Monday's index closes and the morning's index levels confirmed; press snapshots are earlier in the session than the Cboe/bridge prints |

**errors: 0.** No source was blocked or rate-limited.

## Method & caveats

- The breadth percentages and the 20/50-DMA columns describe the **2026-11-02 settle**; the
  index/ETF levels and the volatility pair are **live 2026-11-03 intraday**. Both are labelled
  at every appearance. The 2026-11-03 close does not exist yet at 14:00 ET.
- **The Cboe prints carry a ~15-minute lag** (stamped 13:49–13:50 ET at a 14:05 ET fetch), and
  the bridge's ETF tape is stamped 14:05:05 ET. They are close enough to read together but are
  not the same instant; the artifact reports each source's own timestamp rather than a single
  blended "as of".
- **No live advance/decline tally exists on any reachable feed** (Nasdaq's marketmovers endpoint
  returns only top-mover tables). The RSP-vs-SPY spread (−0.57 pp) is the intraday breadth
  proxy, and it is the same cap-concentration signal the settled breadth measures.
- The universe is **not frozen** between runs — the market-cap floor is applied to the latest
  `valuation` row, so the count moved 904 → 902 names since the 2026-10-30 reading. Breadth
  percentages across days are comparable in direction, not as a fixed population.
- The `atr_extensions` block in `_regime-intraday.json` carries the skill's `extension_pct`
  (distance-from-50-DMA) plus a separately computed `atr_extension_multiple`; the flag
  `late_cycle` is identical on either measure.
- The 3-month sector column is the 2026-08-03 → 2026-11-02 settled move; the intraday column
  is 2026-11-03 live. The two sessions are never mixed inside one number.
- The end-of-day counterpart for the 2026-11-02 session is cron #09's `breadth.md`; this file
  is the intraday read and is expected to differ from it (different VIX quote time, and #09
  draws its breadth from the settled close).
