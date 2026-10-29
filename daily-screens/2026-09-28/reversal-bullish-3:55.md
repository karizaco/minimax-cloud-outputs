# Reversal Bullish (Bonde) — 3:55 PM ET — 2026-09-28 (Mon)

_Source: TradingView scanner (universe) + Yahoo Finance (OHLC) — shibui MCP not available in this session._
_Universe: large-cap US (mcap > $5B, avg vol 30d > 1M), today's change < 0, close ≥ $15._
_Latest bar used: Friday close 2026-09-25 (cron fired pre-market Mon 2026-09-28; T+1 case.)_
_Filter chain: 8 Bonde criteria from Stockbee's published playbook._

## Results (passed all 8 Bonde criteria)

**0 candidates** passed all 8 strict Bonde criteria. Market context: post-weekend scan, Fri close used.

Filter-by-filter rejections (out of 341 in universe):

| Stage | Rejected | Reason |
|---|---|---|
| Universe gate | 0 | mcap>5B, avg-vol>1M, change<0, close≥15 |
| F1 (5-day low) | 195 | Today low not below prior 5-day min low |
| F2 (DCR ≥ 0.5) | 113 | Closed in lower half of day range |
| F4 (small body) | 8 | Body > 40% of day range |
| F3 (tail:body ≥ 3) | 14 | Bottom tail too short |
| F5 (2-day decline) | 3 | No prior drop |
| F6 (ADR ≥ 3%) | 5 | Slow mover |
| F8 (close ≥ close_20d_ago × 0.92) | 3 | Long-term downtrend |
| **PASSED ALL 8** | **0** | |

This is consistent with Bonde's published expectation: the 3:55 PM RB scan is intentionally strict and frequently returns 0–3 names. Do **not** pad with marginal setups.

## Near Misses (passed F1–F7, failed F8 trend filter)

3 stocks had today's 5-day low + reversal candle + ADR ≥ 3% + prior decline, but are in a longer-term downtrend (close < 0.92× close_20d_ago). Manual review only.

| # | Symbol | Close | DCR | Body% | Tail:Body | ADR% | 20d Trend | 2d Drop |
|---|---|---|---|---|---|---|---|
| 1 | SSRM | $35.68 | 0.82 | 0.10 | 8.4 | 3.53 | -8.54% | -1.71% |
| 2 | INTU | $275.79 | 0.73 | 0.04 | 15.2 | 3.97 | -20.75% | -3.84% |
| 3 | HRB | $42.19 | 0.68 | 0.02 | 31.0 | 3.08 | -19.65% | -0.82% |

Bonde's common rejections table marks similar long-term-downtrend names as rejected (XPEV, TFII, ERIC). Treat these as 'do not trade' unless trend reverses.

## Discretionary Notes

- **Day-of-week**: this is a Monday-morning cron firing 4:55 ET. Bonde's RB scan is designed for 15:30–16:00 ET window on the SAME trading day so the trader can place a 15:58–16:00 MOC order. The next valid fire is today's 15:55 ET.
- **Latest available data**: 2026-09-25 (Fri close). The Sep 28 (today) intraday is not yet known.
- **Universe size**: 341 large-cap US equities passed the TradingView screen (mcap > $5B, avg 30d vol > 1M, down-day, ≥ $15). Tighter than the Bonde canonical scan; relaxes the 'institutional 1,000+ holders' proxy from market-cap-only.
- **Source path**: PRIMARY chain shibui-finance unavailable → fallback to TradingView scanner + Yahoo Finance v8 chart (Finviz blocked by Cloudflare 403; yahoo-finance MCP unavailable).

_Generated at 2026-09-28 09:02 UTC (cron #4 reversal-bullish-3:55)._