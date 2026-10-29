# Reversal Bullish (Bonde) — 3:55 PM ET — 2026-10-20 (Tue)

_Source: TradingView scanner (universe) + Yahoo Finance (OHLC) — shibui MCP not available in this sandbox._
_Universe: US large/mega-cap (mcap > $5B, avg 30d vol > 1M), today's change < 0, close >= $15._
_Latest bar used: 2026-10-19 (Mon close) (cron fired pre-market Tue; T+1 case)._
_Filter chain: 8 Bonde criteria from Stockbee's published playbook._

## Results — 1 candidate(s) passed all 8 Bonde criteria

| # | Symbol | Close | DCR | Body% | Tail:Body | ADR% | 20d Trend | 2d Drop | 5d Low | Body Low Stop | Mkt Cap |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **META** | $705.44 | 0.77 | 0.12 | 6.7 | 3.53 | -4.83% | -4.25% | $702.71 | $705.44 | $1797.1B |

**Bonde's discipline:** select 1-3 ideas; prefer higher-priced; entry 3:58-4:00 PM ET or MOC; stop = low of candle body next morning, sized <= 2.5% loss; hold 1-3 days.

**Per-stock notes:**
- **META** ($705.44, Meta Platforms): DCR 0.77 (clean reversal). ADR 3.53% (over Bonde's 3% floor). 20d trend -4.83% (inside the 0.92x window). Tail:body 6.73 (well-formed). Highest-priced name this cycle — matches Bonde's 'prefer higher priced' rule. Mega-cap social/AI advertising; heavy news sensitivity. Verify the setup still holds at 15:55 ET intraday before entry.

## Near Misses — 1 stocks failed only F8 (long-term trend)

| # | Symbol | Close | DCR | Body% | Tail:Body | ADR% | 20d Trend |
|---|---|---|---|---|---|---|---|
| 1 | GIL | $40.86 | 0.80 | 0.03 | 23.3 | 3.69 | -11.48% |

Manual review only — Bonde's common-rejections table marks similar long-term-downtrend names as 'do not trade'.

## Filter-chain diagnostic (out of 494 in universe)

| Stage | Rejected | Reason |
|---|---|---|
| F1 (5-day low) | 429 | Today low NOT below prior 5-day min low |
| F2 (DCR >= 0.5) | 56 | Closed in lower half of day range |
| F4 (small body) | 1 | Body > 40% of day range |
| F3 (tail:body >= 3) | 2 | Bottom tail too short |
| F6 (ADR >= 3%) | 3 | Slow mover |
| F8 (close >= close_20d_ago x 0.92) | 1 | Long-term downtrend |
| no_data | 1 | Yahoo OHLC unavailable |
| **PASSED ALL 8** | **1** | |

## Discretionary Notes

- **Day-of-week**: cron fired 04:55 ET (pre-market Tue). Bonde's RB scan is designed for the 15:30-16:00 ET same-day window so the trader can place a 15:58-16:00 MOC order. **This is a planning artifact for the 15:55 ET fire today** — verify META still setups at 15:55 ET intraday.
- **Latest available data**: 2026-10-19 (Mon close). Oct 20 intraday not yet known (T+1 lag).
- **Universe size**: 494 large-cap US equities — moderate drop day (RBA -5.3%, FIGR -5.3%, CBRS -5.2%, MOS -4.8%). Monday's post-selloff exhaustion persists: only 65/494 names printed a new 5-day low.
- **Source path**: PRIMARY chain shibui-finance unavailable -> fallback to TradingView scanner + Yahoo Finance v8 chart (Finviz blocked by Cloudflare 403; chain terminated per zero-fallback policy).

## Recent runs (cross-day summary)

- 2026-10-09 (Fri close): 12 picks (RVTY, A, RGEN, ILMN, TEM, MAIR, PTCT, SWKS, GH, BMNR, ALGM, HBM).
- 2026-10-12 (Mon close): ALAB (1 pick).
- 2026-10-15 (Thu close): 21 picks — broadest this month (semicap/optical heavy).
- 2026-10-16 (Fri close): 0 picks (setup exhaustion after broad selloff).
- 2026-10-20 (Tue close): META (1 pick, Meta Platforms).
