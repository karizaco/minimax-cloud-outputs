<!-- cron #9 stock-screener-daily-sweep-18:30 | cron_date=2026-10-23 | data_date=2026-10-22 | generated=2026-10-23T11:39Z -->
# Daily stock screener sweep — 2026-10-23

**Run status: DEGRADED.** The skill's entire primary tier (shibui-finance, tradingview, tradingview-advanced,
financekit, yahoo-finance MCP servers) is **not connected in this Cloud session**. Verified, not assumed:
`mcode-tools connector tools` returns `partial=false, provider_failures=[]` with a 16-tool catalog containing only
`matrix` (multimodal) and `email_workbench`; `tool_search` returns zero finance hits for `shibui`, `tradingview`,
`stock`, and `finance`. Per the zero-fallback policy the chain terminated at **tier 2 (TradingView public screener)**
and stopped — no deeper MCP chaining, no retry loop.

- **Data date is 2026-10-22, not 2026-10-23.** The cron fired 07:30 ET, roughly two hours *before* the US open,
  so the newest settled session is Thursday 2026-10-22. Treated as the skill's T+1 case: files land in
  `daily-screens/2026-10-23/` per the cron contract, and the lag is recorded in every file header.
- **Source verified, not trusted.** TradingView closes were matched against Yahoo's 2026-10-22 regular-session
  close on 8/8 spot-checked names (NVDA, AAPL, MSFT, GOOGL, AMD, TSLA, PLTR, SMCI) — exact to the cent on all eight.
  Finviz (tier 3) returned HTTP 403 and was not used.
- **All numbers carry a row count.** 5,718 symbols scanned, 0 duplicates, 2,934
  after the pre-filter.

## Headline

Risk-off Thursday. S&P 500 −1.21%, XLK-led tech selloff, defensives bid (Consumer Durables
+3.73%, Utilities +2.22% median constituent day;
Electronic Technology -4.97%, Non-Energy Minerals
-5.37%). Breadth stayed constructive at
**65.3%** above the 20-DMA and VIX finished at **19.03** — index damage
without breadth damage.

**Tier-A: XLAB** (Exascale Labs Holdings Inc., $4.71, +73.16%) on
4 screens. **Reversal-bullish: SNX** (TD SYNNEX Corporation, $247.08) — the only name
passing all eight of Bonde's published criteria, out of 25 that cleared the five screenable filters.

## Files in this directory

| File | Contents |
| --- | --- |
| `daily-sweep.md` | this report |
| `_summary.md` | machine-read digest (pre-market brief reads this) |
| `_regime.json` | regime payload: size_cut / uncertainty / late_cycle |
| `_source-health.json` | every substitution and unavailable field, machine-read |
| `stockbee.md` / `.csv` | Bonde — 4% breakout, EP9M, anticipation coil |
| `qullamaggie.md` / `.csv` | Kullamägi — RS leaders, EP gap, parabolic short/long |
| `jeff-sun.md` / `.csv` | Sun — CANSLIM, compression |
| `ariel-hernandez.md` / `.csv` | Hernandez — theme→group funnel, sector rotation, skip-rule flags |
| `peoplewish.md` / `.csv` | peoplewish — ADR + dollar volume + velocity |
| `short-candidates.md` | parabolic short |
| `long-reversal-candidates.md` | parabolic long |
| `reversal-bullish-3:55.md` / `.csv` | Bonde 8-criteria reversal bullish + full reject funnel |
| `master.md` / `.csv` | deduped union (capped 200) |
| `stalk.md` / `.csv` | master ∩ near 20/50-DMA |
| `focus.md` / `.csv` | master ∩ ≥3 screens or top-5 velocity |
| `tier-a.md` / `.csv` | master ∩ ≥4 screens |
| `breadth.md` | breadth + regime detail |
| `catalysts.md` | sourced catalyst attribution for the highest-signal names |

## Not produced, and why

- `ipo.md` and `high-short-float.md` — **Sundays only** per the skill. Today is a Friday.
- `uncertainty` regime flag — `^VXV` and `^VXVCLS` both return zero bars from Yahoo. A VIX/VXV ratio needs both
  legs; the field is `null` in `_regime.json`, not guessed.
- Sun's VCP `contraction_ratio` — needs per-session range history that the screener does not carry. Substituted
  with a clearly-labelled volatility proxy, not presented as the published screen.
- Jeff Sun's `sales_growth_quarterly_yoy > 25` filter — column is null on this source; the filter is **dropped**,
  which makes the CANSLIM screen looser than published. `earnings_growth_quarterly_yoy` is substituted by TTM
  EPS growth. Both substitutions are logged in `_source-health.json`.

## Live-only steps not run

The sweep is a screening procedure. Steps 6 (pre-market gapper, 09:00 ET), 7 (intraday RVOL re-rank, 09:45–11:15 ET)
and the reversal-bullish entry window (15:30–16:00 ET) are all either outside this fire time or require a live
feed. `reversal-bullish-3:55.md` is computed on the 2026-10-22 settled close, so it is valid for next-session
execution, not for an entry that has already passed.

## Source health — read before using this list

- **All MCP finance tools were unavailable this run.** `mcp__shibui-finance__stock_data_query, mcp__tradingview__screen_stocks, mcp__tradingview__screen_etf, mcp__tradingview-advanced__volume_breakout_scanner, mcp__tradingview-advanced__yahoo_price, mcp__financekit__sector_rotation, mcp__yahoo-finance__*` — 
  confirmed by `mcode-tools connector tools` → `partial=false, provider_failures=[]`, catalog holds 16 tools, all `matrix`/`email_workbench`. `tool_search` returns 0 finance hits.

- **Data source: TradingView public screener** (`scanner.tradingview.com/america/scan`, POST), the skill's fallback tier 2. 2,934 names after the pre-filter (5,718 raw, 0 duplicate symbols).

- **Session date is 2026-10-22, not 2026-10-23.** The cron fired 07:30 ET, ~2 h before the open, so the newest settled session is Thursday. Verified: TV `close` matched Yahoo's 2026-10-22 regular-session close to the cent on 8/8 spot-checked names (NVDA, AAPL, MSFT, GOOGL, AMD, TSLA, PLTR, SMCI).

- Finviz (tier 3) returned **HTTP 403** and was not used.


### Every deviation from the skill's shibui SQL spec

| Spec field | What was used instead |
| --- | --- |
| ADR% (filter 4.5/5.0) | ATR(14)/close*100 instead of mean 20d (high-low)/close |
| ADV$ | average_volume_30d_calc * close |
| volume > prev_volume (Bonde A) | volume > average_volume_10d_calc |
| adr_pct 20d (Bonde RB filter 6) | not evaluated in stage 1; see RB verification pass |
| RB filter 1 (5-day low) / 5 (2-3 day decline) | require price history -> Yahoo 3mo pass on candidates only |
| RB filter 8 (close vs close_20d_ago) | close >= SMA20*0.92 proxy |
| Sun J contraction_ratio < 0.6 | NOT COMPUTABLE (needs range history); PROXY = ATR% in bottom quartile & Perf.3M>0 |
| Bonde K avg(close,7)/avg(close,65) | PROXY = (close/SMA50 - 1) |
| Bonde K 10-day base | PROXY = 1-month base (High.1M-Low.1M)/close |
| Jeff Sun sales_growth_quarterly_yoy > 25 | DROPPED (column null on this source) |
| Jeff Sun earnings_growth_quarterly_yoy > 25 | SUBSTITUTED by earnings_per_share_diluted_yoy_growth_ttm (TTM not quarterly) |
| velocity_14d (peoplewish) | SUBSTITUTED by Perf.1M (calendar month not 14 sessions) |
|  Hernandez ETF RS | equal-weight median constituent Perf.1M/3M/6M per sector+industry group |
| SPX breadth | mcap > $10B proxy per skill (no constituents table) |
| skip-rule day2_no_follow / ma_shrink_5d | NOT COMPUTABLE (needs 2+ day range history) |

- **Not computable on this source, therefore absent (not estimated):** ^VXV and ^VXVCLS both unavailable on Yahoo (0 bars) -> uncertainty flag NOT set
