<!-- cron #9 | cron_date=2026-10-23 | data_date=2026-10-22 | generated=2026-10-23T11:39Z -->
# Daily screen summary — 2026-10-22 (cron fired 2026-10-23)

- **Regime:** risk-off session. Breadth **65.3%** above the 20-DMA
  (mcap > $10B proxy (858 names); no SPX constituents table on this source), VIX **19.03** (settled 2026-10-22), S&P 500 −1.21%.
  4 of 5 indices sit below their 20-DMA (SPY, QQQ, QQQE, IWM) yet breadth is healthy — narrow index damage, broad
  participation. `late_cycle=False`, `size_cut_pct=None` (breadth ≥ 40% blocks it),
  `uncertainty=None` (**not computable** — VXV unavailable).
- **Tier-A (≥4 screens):** **XLAB** — Exascale Labs Holdings Inc., $4.71, +73.16% on
  4 independent screens (bonde_4pct, bonde_ep9m, peoplewish_adr_velocity, qull_parabolic_short). ADR% 14.59.
  Catalyst in `catalysts.md`: a week-old $8.2M NVIDIA/Sunon 8-K, not fresh news.
- **Parabolic short / long:** **2 short candidates**, **0 long
  candidates.** Both small-number screens are near-empty because the tape is one-directional; see
  `short-candidates.md` / `long-reversal-candidates.md`.
- **3:55 PM reversal-bullish:** **SNX** — TD SYNNEX Corporation, close $247.08, DCR 0.903,
  tail/body 18.38, ADR20 3.32%, body-low stop $246.56 (-0.21%).
  **1 of 25** stage-1 candidates passed all eight of Bonde's criteria.

## Screen yield

| Screen | Stylist | Hits |
| --- | --- | ---: |
| A. 4% breakout | Bonde | 60 |
| B. EP9 Million | Bonde | 40 |
| K. Anticipation (coil, proxy) | Bonde | 3 |
| C. Multi-timeframe RS | Kullamägi | 33 |
| D. EP 10%+ gap | Kullamägi | 0 |
| E. Parabolic short | Kullamägi | 2 |
| F. Parabolic long | Kullamägi | 0 |
| H. CANSLIM | Sun | 40 |
| J. Compression (proxy) | Sun | 40 |
| G. ADR + velocity | peoplewish | 40 |
| L. Reversal bullish (8/8) | Bonde | 1 of 25 |

Universe: 5,718 raw → **2,934** after the pre-filter
(close>$3, mcap>$300M, 30d avg vol>100k, NYSE/NASDAQ/AMEX). Tiers: master 200,
stalk 39, focus 5, tier-a 1.

## Empty screens — read these before assuming a bug

- **D. EP (10%+ gap) = 0.** Only three names in the entire 2,934-name universe opened ≥10%
  above the prior close (BHVN +37.0%, XLAB +17.6%, AVEX +13.2%); none cleared the ≥10× RVOL **and** ≥$50M ADV gates.
- **F. Parabolic long = 0.** 38 names fell ≥25% over five sessions, but every liquid one is 30–42% *below* its
  200-DMA (TTMI −42%, CRS −34%). The screen requires a pullback that is still near the 200-DMA; there were none.

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
