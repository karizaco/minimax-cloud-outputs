---
fire_time_et: 2026-10-30 18:30 ET
data_date: 2026-10-30 (settled 16:00 ET close). Multi-stylist screens ran on shibui's 2026-10-29 bar (shibui is T+1); breadth, volatility and the EOD overlay are 2026-10-30 settles.
breadth_universe: US listings on NASDAQ/NYSE/AMEX with market cap > $10B — 1,001 names (993 stocks + 8 funds), TradingView america scan, market_cap_basic filter. Cross-check on shibui's own large-cap definition (market_cap > $10B, exchange in NYSE/NASDAQ/AMEX): 913 names.
vix_quote_time: CBOE delayed-quote CDN, trade stamp 2026-10-30T16:15:01 ET — VIX 19.42 / VIX3M 20.78 (VIX3M independently confirmed against CBOE VIX3M_History.csv 10/30 row, 20.780000).
cross_reference: intraday counterpart: daily-screens/2026-10-30/breadth-snapshot.md (cron #10, 14:00 ET)
---

# Breadth & regime — end-of-day read (2026-10-30)

This is the **18:30 ET end-of-day** breadth read, taken from the settled 16:00 ET close of Friday
October 30, 2026. Cron #10's `breadth-snapshot.md` is the 14:00 ET intraday read of the same session;
the two are expected to differ, and here they differ because this file is pinned to the settled tape
while the intraday file was pinned to a live print.

## Market close

| Index / ETF | Close | Chg | vs 20-DMA |
|---|---:|---:|:--:|
| S&P 500 (CBOE _SPX) | 7,580.07 | -1.82% | below |
| Nasdaq-100 (CBOE _NDX) | 28,384.85 | -3.46% | below |
| Russell 2000 (CBOE _RUT) | 2,811.84 | -1.66% | below |
| SPY | 755.72 | -1.77% | below |
| RSP (equal weight) | 218.31 | -0.79% | above |
| QQQ | 690.49 | -3.47% | below |
| IWM | 279.33 | -1.65% | above |
| QQQE | 116.29 | -2.45% | below |
| DIA | 517.13 | -1.07% | below |

The session was an **AI-led unwind, not a broad risk-off**. SPY lost 1.77% while RSP fell only 0.79%,
a 0.98-point cap-concentration spread, and only 2 of the 5 index ETFs closed above their 20-DMA. The
press attributes it to Alphabet's Thursday miss, then Amazon's and Intel's weak results and guidance
overnight — Intel's Q4 revenue forecast of $15.0-16.0B against $16.5B in Q3 is what broke the
semiconductor complex, and Amazon's $220B 2026 capex plan re-opened the AI-return question.

## Breadth

| Metric | 2026-10-30 (TradingView, 1,001 names) | 2026-10-29 (shibui, 913 names) |
|---|---:|---:|
| % above 20-DMA | **58.0%** | 69.3% |
| % above 50-DMA | 47.8% | 60.2% |
| Advancers / decliners | 402 / 589 | — |
| Median daily change | -0.36% | — |

Breadth fell roughly 11 points session-over-session on the comparable shibui measure and roughly 4
points on the TradingView measure, but it did **not** break down: nearly three-fifths of large caps
still closed above their 20-DMA. That is a leadership rotation, not distribution. The signal that
matters for position sizing is that the **median** name is down, the **index** is down, and the
**equal-weight** index is down a third as much as the cap-weighted one — money left AI, not the
market.

## Index extension

| ETF | Close | vs 50-DMA | ATR% vs own 252d median |
|---|---:|---:|---:|
| SPY | 755.72 | -1.53% | 0.82x |
| QQQ | 690.49 | -4.76% | 0.98x |
| RSP | 218.31 | +1.52% | 0.87x |
| IWM | 279.33 | -1.74% | 0.75x |
| QQQE | 116.29 | -3.04% | 0.95x |

Every index sits **below** its 50-DMA except RSP, and no index is stretched on its own volatility
history — QQQ, the most extended name, still trades at 0.98x its 252-day median ATR%. This is a
de-rating, not a blow-off, and `late_cycle` stays false.

## Volatility

| Instrument | Close | Chg | Source |
|---|---:|---:|---|
| VIX | 19.42 | +12.91% | CBOE delayed-quote CDN, 16:15:01 ET |
| VIX3M | 20.78 | +7.28% | CBOE delayed-quote CDN, 16:15:01 ET |
| VIX / VIX3M ratio | 0.93 | — | derived |

The ratio sits **below 1.0**, so the front end is not yet priced above the 3-month tenor and the
`uncertainty` flag stays false. That is worth flagging as a genuine caveat rather than comfort:
VIX at 19.42 is a 13% one-day jump and Bloomberg reported an intraday touch of the highest level
since April, but the term structure has **not** inverted into stress. A ratio of 0.93 with SPX 1.8%
down is a shock absorbed by duration, not a demand for crash hedging.

## Regime payload

```json
{
  "size_cut_pct": 0,
  "uncertainty": false,
  "late_cycle": false,
  "breadth_pct_spx": 58.0,
  "index_below_20sma": true,
  "vix": 19.42,
  "vix3m": 20.78,
  "vix_vix3m_ratio": 0.9346
}
```

`size_cut_pct` is **0** because the index-below-20-DMA condition (2 of 5 ETFs) did not coincide with
breadth under 40% — at 58.0% there is no mechanical size cut, though discretionary sizing should lean
smaller into a 19+ VIX tape.

## Sector rotation (10-30 settle)

| Sector ETF | Chg 10-30 | 1M | 3M |
|---|---:|---:|---:|
| XLE Energy | +1.91% | +13.26% | +18.82% |
| XLP Staples | +1.41% | +8.84% | +5.39% |
| XLU Utilities | +0.67% | +9.04% | -2.65% |
| XLV Health Care | +0.45% | +8.65% | +13.90% |
| XLB Materials | +0.40% | +7.00% | +3.59% |
| XLRE Real Estate | +0.26% | +3.97% | -4.66% |
| XLY Cons. Discretionary | -0.71% | +5.60% | -0.05% |
| XLF Financials | -0.76% | +4.67% | -0.53% |
| XLC Comm. Services | -1.29% | -10.38% | -6.48% |
| XLI Industrials | -1.60% | -1.28% | -7.26% |
| XLK Technology | **-4.89%** | -8.16% | +1.16% |

Energy, staples, utilities, health care and real estate were **all** green on a day the Nasdaq fell
3.46%. The theme ranking used by the Hernandez funnel is the composite of 1M/3M/6M performance, which
picks **XLE (16.88), XLV (16.31) and IBB (15.93)** — the same three themes as the previous session
with #2 and #3 swapping.

## Source health

| Source | Endpoint / query | Status | Result |
|---|---|---|---|
| shibui-finance (MCP bridge) | `stock_data_query`, 11 queries | ok | All 11 returned; one Binder Error on first attempt (`rn` not projected in a CTE) was re-issued corrected against the same source |
| shibui breadth aggregate | `market_cap > 10B` join, 2026-10-29 | ok | 913 names, 69.33% above 20-DMA |
| TradingView scanner | `POST scanner.tradingview.com/america/scan`, 5 calls | ok | 0 rate limits; `change` column is percent units |
| CBOE delayed quotes | `cdn.cboe.com/.../delayed_quotes/quotes/_VIX.json` etc. | ok | 16:14-16:15 ET stamps; `close` field is the 16:00 settle (after-hours print is in `current_price`) |
| CBOE history CSV | `VIX_History.csv`, `VIX3M_History.csv` | partial | VIX3M rolled to 10/30; **VIX_History.csv still ends 10/29**, so the 10-30 VIX came from the delayed-quote CDN, not the CSV |
| Nasdaq quote API | `api.nasdaq.com/api/quote/{SYM}/info` | ok | `secondaryData` used for official close (SPY 755.78 vs CBOE 755.72; both -1.77%) |
| Yahoo JSON (chart/spark/screener) | — | not used | No need — the whole read was served by shibui + TV + CBOE |
| web_search | catalyst research | ok | 8 searches; market wrap, CDNA, INTC, ILMN, APPS, GRAL, PURR catalysts confirmed |
