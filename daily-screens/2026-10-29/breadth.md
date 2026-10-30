---
fire_time_et: "18:32 ET"
data_date: "2026-10-28"
data_feed_lag: "T+1 — shibui had not ingested 2026-10-29 when this cron fired; every breadth number describes the 2026-10-28 session"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 908 names (shibui valuation, latest-row-first)"
index_breadth_universe: "SPY, RSP, QQQ, QQQE, IWM — 5 index ETFs"
vix_quote_time: "2026-10-28 16:00 ET settle — Cboe daily_prices history CSV (VIX_History.csv / VIX3M_History.csv), cross-checked against the Cboe delayed-quote CDN prev_day_close"
vix_pair: "16.91 / 19.22 (ratio 0.88) — the single volatility pair used throughout this document"
cross_reference: "intraday counterpart: daily-screens/2026-10-29/breadth-snapshot.md (cron #10, 14:00 ET)"
author: "cron #9 stock-screener-daily-sweep-18:30 (Mavis, Cloud runtime)"
---

# Breadth and regime snapshot — 2026-10-29 (end-of-day read)

_Data date 2026-10-28 · cron date 2026-10-29 · computed from shibui's daily close series._

This is the **end-of-day** breadth read. The intraday counterpart fired at 14:00 ET into
`daily-screens/2026-10-29/breadth-snapshot.md` and is the authoritative *live-tape* view; this file is
authoritative for the **settled** session and will differ from it in the VIX quote time and, historically,
in the breadth population.

## Regime

| Flag | Value | Meaning |
|---|---|---|
| `size_cut_pct` | 0 | Percent to trim every Tier-A position. Zero means no size cut. |
| `uncertainty` | false | VIX above VIX3M signals front-end stress. |
| `late_cycle` | false | An index ETF more than 6% extended above its 50-day MA. |
| Large-cap breadth | 63.77% | Share of the 908 names above $10B trading above their 20-day MA. |
| Index breadth | 80% above 20-DMA | Share of SPY/RSP/QQQ/QQQE/IWM above their 20-day MA (4 of 5). |
| VIX / VIX3M | 16.91 / 19.22 (ratio 0.88) | Below 1.0 means no front-end stress premium. |

The index breadth reading and the large-cap breadth reading agree here: four of the five index ETFs are
above their 20-day moving average and 63.8% of the large-cap cohort is too. The
size-cut rule needs *both* an index below its 20-day average and breadth under 40%, so the regime resolves
to a **zero size cut**.

**One caveat that changes how breadth should be read.** The universe is a large-cap proxy, not the whole
market. An independent all-stock read for the same 2026-10-28 session puts only ~34% of *every* US stock
above its 50-day average (3,531 advancers vs 2,993 decliners), against 63.77% /
54.30% inside the $10B+ cohort. Strength is concentrated in large caps.

## Index ETF extension from the 50-day MA

| Ticker | Close | 20-DMA | 50-DMA | Extension vs 50-DMA | ATR(14) | ATR% | ATR% vs 252d median |
|---|---|---|---|---|---|---|---|
| SPY | $772.31 | $770.90 | $767.63 | +0.61% | 6.95 | 0.90 | 0.83× |
| RSP | $217.43 | $213.91 | $215.13 | +1.07% | 1.93 | 0.89 | 0.85× |
| QQQ | $725.61 | $732.48 | $725.42 | +0.03% | 11.03 | 1.52 | 0.95× |
| QQQE | $119.86 | $119.82 | $120.13 | -0.23% | 1.46 | 1.22 | 0.95× |
| IWM | $281.29 | $277.27 | $285.00 | -1.30% | 3.54 | 1.26 | 0.75× |

Extension against the 50-day MA is the `late_cycle` input. The final column is the *true* ATR extension
multiple — current ATR as a percentage of close, divided by the 252-session median of that same measure.
The skill's own breadth SQL computes `atr_252d_avg` inside a CTE already filtered to a single date, so
that window function collapses to `atr_14` and the column is really just the distance from the 50-day MA;
the separate query above fixes it. **No index ETF is extended on its own ATR** — the highest is QQQ at
0.95× its own 252-day median, and IWM is the calmest at
0.75× — so `late_cycle` stays false.

## Sector and industry-group relative strength

| ETF | 1M | 3M | 6M | Composite |
|---|---|---|---|---|
| IBB | +2.52% | +13.89% | +30.82% | 47.23 |
| XLE | +11.23% | +16.10% | +15.96% | 43.28 |
| XLV | +5.27% | +9.91% | +25.82% | 40.99 |
| XOP | +12.17% | +14.58% | +12.74% | 39.50 |
| VGT | -1.01% | +8.81% | +19.84% | 27.64 |
| XLK | -1.80% | +8.69% | +20.04% | 26.93 |
| XBI | +0.45% | +3.99% | +22.20% | 26.64 |
| SPY | +1.06% | +4.13% | +8.53% | 13.72 |
| SMH | -6.46% | +5.34% | +13.63% | 12.50 |
| XLP | +6.10% | +1.60% | +4.73% | 12.43 |
| SOXX | -8.02% | +3.45% | +15.99% | 11.42 |
| XLF | +3.93% | -1.53% | +8.11% | 10.51 |
| OIH | +7.58% | +8.85% | -8.23% | 8.21 |
| XLB | +5.62% | +0.43% | +1.77% | 7.81 |
| XLY | +5.66% | +2.62% | -1.29% | 6.99 |
| KRE | +3.27% | -4.99% | +4.46% | 2.73 |
| PBJ | +4.62% | -2.56% | -4.51% | -2.45 |
| XLU | +7.00% | -4.86% | -6.98% | -4.84 |
| XLI | -0.38% | -5.55% | -0.85% | -6.78 |
| XLRE | +1.91% | -7.00% | -3.46% | -8.55 |
| VIS | -0.62% | -5.80% | -2.63% | -9.05 |
| PPA | +1.37% | -8.43% | -3.34% | -10.41 |
| JETS | -5.57% | -14.87% | +8.18% | -12.25 |
| XME | -2.49% | -0.54% | -11.60% | -14.64 |
| XLC | -7.47% | -3.23% | -10.54% | -21.24 |
| URA | -8.72% | -7.98% | -30.89% | -47.59 |
| TAN | -5.64% | -17.78% | -26.98% | -50.40 |

The top three themes by composite relative strength are **IBB** (2.52% / 13.89% / 30.82%), **XLE** (11.23% / 16.10% / 15.96%) and **XLV** (5.27% / 9.91% / 25.82%). Those buckets are what the Hernandez theme→group screen pulled its leaders from.

Three ETFs in the full theme set — **IGV, ARKK and IYT** — have no row in shibui's ETF feed and are excluded
from the table above rather than sourced from a different feed on a different date. The TradingView scanner
was used as an independent cross-check on the 2026-10-29 settle and returns the **same three leading
themes** (IBB (48.3), XLV (47.1), XLE (45.3)), so the theme ranking is robust to the one-session offset.

## Roll-forward — 2026-10-29 settled index closes

These are the 2026-10-29 4:00 PM prints, pulled separately from the Nasdaq quote API. They are **not**
part of the breadth computation above, which describes the 2026-10-28 session. No second volatility
reading is quoted anywhere in this document.

| Ticker | Close 10-29 | Chg 10-29 |
|---|---|---|
| SPY | $769.49 | -0.37% |
| QQQ | $715.34 | -1.42% |
| RSP | $220.02 | +1.19% |
| IWM | $284.01 | +0.97% |
| QQQE | $119.21 | -0.54% |

The 2026-10-29 session was a rotation, not a sell-off: equal-weight RSP +1.19% and small-cap IWM +0.97%
against cap-weight SPY -0.37% and QQQ -1.42%. The S&P 500 closed -0.61% with Health Care +2.4%, Real Estate
+2.2% and Consumer Staples +1.5% leading and Communication Services -1.9% and Technology -1.2% lagging,
after Alphabet and Caterpillar missed on AI capex and with hot CPI keeping a December Fed hike live after
the 10-2 hawkish hold on 10-28.

## Source health

| Source | Endpoint / query | Status | Result |
|---|---|---|---|
| shibui-finance (MCP-over-HTTP bridge) | `stock_data_query` — breadth + index extension + sector RS + ATR extension | ok | NYSE/NASDAQ/AMEX, market cap > $10B, 908 names, 2026-10-28 |
| Cboe daily_prices | `VIX_History.csv`, `VIX3M_History.csv` | ok | 16.91 / 19.22 for 2026-10-28 |
| Cboe delayed-quote CDN | `quotes/_VIX.json`, `quotes/_VIX3M.json` | ok | cross-check only; `prev_day_close` 16.91 / 19.22 match the history CSV |
| Nasdaq quote API | `/quote/{SYM}/info` (secondaryData = official close) | ok | 5 index ETFs, 2026-10-29 settle |
| TradingView scanner | `POST scanner.tradingview.com/america/scan` | ok | theme cross-check on the 2026-10-29 settle |
| Finviz screener | `finviz.co` | failed: 403 Cloudflare | tier-2 fallback unavailable |
| Yahoo Finance JSON | `query1/query2.finance.yahoo.com` | failed: 429 rate-limited | tier-2 fallback unavailable |

_Data date 2026-10-28 (shibui T+1) · cron date 2026-10-29, fired 18:32 ET · intraday counterpart:
`daily-screens/2026-10-29/breadth-snapshot.md` (cron #10, 14:00 ET)._
