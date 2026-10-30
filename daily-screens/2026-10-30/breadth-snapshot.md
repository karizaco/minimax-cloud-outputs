---
fire_time_et: "2026-10-30 14:03 ET"
data_date: "2026-10-29 (shibui T+1 — the last SETTLED session available at fire time; this cron fired 2026-10-30)"
breadth_universe: "NYSE/NASDAQ/AMEX, market_cap > $10B, 913 names — the skill's large-cap proxy for the S&P 500 (shibui has no sp500_constituents table)"
vix_quote_time: "2026-10-30 13:47:31 ET — CBOE delayed-quote CDN (_VIX / _VIX3M); independently cross-checked against Yahoo Finance ^VIX 21.40 @ 13:48:01 ET"
cross_reference: "end-of-day counterpart: daily-screens/2026-10-30/breadth.md (cron #09, 18:30 ET)"
volatility_pair: "VIX 21.38 / VIX3M 21.71 (ratio 0.9848) — this single pair is used everywhere in this document"
live_snapshot: "indices 2026-10-30 13:47:35 ET (CBOE CDN); index ETFs 2026-10-30 13:45:47 ET (CBOE CDN); single-name movers 2026-10-30 ~14:02 ET (Nasdaq quote API)"
regime: {"size_cut_pct": 0, "uncertainty": false, "late_cycle": false}
---

# Breadth snapshot — 2026-10-30 14:03 ET (intraday read)

> **One volatility pair is used throughout: VIX 21.38 / VIX3M 21.71, quoted at 2026-10-30 13:47:31 ET from the CBOE delayed-quote CDN.**
> The prior-session settles (VIX 17.20 / VIX3M 19.37) appear only as the labelled baseline for the change column.

## Headline

The live tape is in a violent mega-cap-technology-led risk-off. At 2026-10-30 13:47:35 ET the Nasdaq 100 was 28,288.34 (-3.79%), the S&P 500 7,569.73 (-1.95%), and VIX had spiked to 21.38 (+24.30% on the session) as the post-earnings fallout from Amazon and Intel spread through the AI-capex complex. The regime flags nevertheless still read benign — `size_cut_pct` 0, `uncertainty` false, `late_cycle` false — and that gap is the read.

Two things drive it. First, the breadth leg of this snapshot is **one session stale**: shibui is a T+1 feed, so the 913-name breadth numbers describe the 2026-10-29 settle, when breadth was genuinely healthy (69.3% of large caps above their 20-DMA). Today's tape has broken well below that. Second, the volatility leg is live, and the VIX/VIX3M ratio at 0.9848 has not yet crossed the 1.00 threshold that would flip `uncertainty` to true — the contango cushion has been all but spent (0.8879 ratio on the prior settle, i.e. 12.6% contango, now 1.5%).

Read it as: settled breadth says nothing is broken, the tape says something is, and the volatility term structure is the tie-breaker still running.

## 1. Breadth — settled session 2026-10-29 (shibui, T+1)

| Measure | Value |
|---|---|
| Universe | 913 names — NYSE/NASDAQ/AMEX, market cap > $10B |
| Above 20-DMA | **69.33%** |
| Above 50-DMA | 60.24% |
| Above 200-DMA | 59.91% |
| Index ETFs above their own 20-DMA | 2 of 5 (40%) → `index_below_20sma` = true |

This is the skill's large-cap proxy, not the S&P 500 — shibui has no constituent table, so the universe is defined by the $10B market-cap floor instead. The 10/29 reading is internally consistent with the press: roughly 400 S&P 500 members rose that day while the cap-weighted index fell 0.30%, with the damage concentrated in Alphabet and other megacaps.

## 2. Index extension — settled session 2026-10-29

| ETF | Close | 20-DMA | 50-DMA | vs 50-DMA | ATR(14) | ATR% | 252d med ATR% | True ATR extension |
|---|---|---|---|---|---|---|---|---|
| SPY | 769.36 | 771.16 | 767.63 | **+0.23%** | 6.86 | 0.89% | 0.92% | +0.54 ATR |
| RSP | 220.04 | 214.46 | 215.09 | **+2.30%** | 1.98 | 0.90% | 0.91% | +2.54 ATR |
| QQQ | 715.34 | 731.14 | 725.41 | **-1.39%** | 11.24 | 1.57% | 1.56% | -0.20 ATR |
| QQQE | 119.21 | 119.75 | 120.06 | **-0.71%** | 1.46 | 1.22% | 1.20% | -0.54 ATR |
| IWM | 284.01 | 277.52 | 284.64 | **-0.22%** | 3.57 | 1.26% | 1.30% | -2.30 ATR |

**Known upstream defect, worked around:** the skill's `emit_breadth_sql()` computes `atr_252d_avg` inside a CTE already filtered to a single date, so the 251-row window holds one row and collapses to `atr_14`. Its `extension_pct` column is therefore *distance from the 50-DMA*, not an ATR extension, and `compute_regime()`'s `late_cycle` test (`extension_pct > 6`) is a "more than 6% above the 50-DMA" test. The true ATR-extension multiple was computed separately over a real 252-session window: the widest is RSP at +2.54 ATR and the deepest is IWM at −2.30 ATR, so `late_cycle` is false under **both** the skill's metric and the spec's intended one. The flag is robust; the column name is not.

## 3. Volatility — live, quoted at 2026-10-30 13:47:31 ET (CBOE delayed-quote CDN)

| Series | Value | Prior settle | Change | Session range |
|---|---|---|---|---|
| **VIX** | **21.38** | 17.20 | +4.18 (+24.30%) | 18.54 – 21.46 (open 18.93) |
| **VIX3M** | **21.71** | 19.37 | +2.34 (+12.08%) | 20.22 – 21.72 (open 20.36) |
| VIX/VIX3M ratio | **0.9848** | 0.8879 | — | contango, but only 1.5% wide |

The pair is internally coherent and independently confirmed: CBOE's own daily history CSVs carry the same 10/29 settles (VIX 17.20, VIX3M 19.37), and Yahoo Finance printed VIX 21.40 at 13:48:01 ET — 30 seconds later and a different feed — against a 17.20 previous close. The 9-day forward vol (VIX9D 21.35) sits fractionally below spot, and the front of the VIX futures curve inverted overnight with November at 19.21 above December at 19.01 (Saxo, pre-market).

## 4. Live tape — 2026-10-30 13:47:35 ET

| Index | Level | Change | % |
|---|---|---|---|
| Nasdaq 100 | 28,288.34 | -1,114.16 | **-3.79%** |
| S&P 500 | 7,569.73 | -150.66 | **-1.95%** |
| Russell 2000 | 2,799.09 | -60.12 | -2.10% |
| Dow Jones | 51,815.00 | -528.00 | -1.01% |

| Index ETF | Price | % |
|---|---|---|
| QQQ | 688.98 | -3.69% |
| IWM | 278.10 | -2.08% |
| QQQE | 116.12 | -2.59% |
| SPY | 755.05 | -1.86% |
| RSP | 218.24 | -0.82% |

Equal-weight RSP -0.82% versus cap-weight SPY -1.86% is roughly a 1-point spread — the same cap-weight-versus-breadth divergence that defined the 10/29 session, and the clearest live signal available here that the damage is concentrated in megacaps rather than broad.

### Live sector performance — 2026-10-30 13:45:47 ET

| Sector ETF | Sector | Today |
|---|---|---|
| XLP | Consumer Staples | **+1.64%** |
| XLE | Energy | **+1.41%** |
| XLU | Utilities | **+1.03%** |
| XLV | Health Care | **+0.90%** |
| XLRE | Real Estate | **+0.64%** |
| XLB | Materials | **-0.16%** |
| XLY | Consumer Discretionary | **-0.64%** |
| XLF | Financials | **-0.65%** |
| XLC | Communication Services | **-1.24%** |
| XLI | Industrials | **-1.24%** |
| XLK | Technology | **-5.36%** |

A textbook defensive rotation out of technology into staples, health care, energy and utilities. Gold fell 3.51% (GLD 355.64) while 10-year Treasuries were essentially flat (TLT +0.13%), which points at an **inflationary** shock — crude +1.75% on Gulf/Hormuz supply risk feeding a December-hike fear — rather than a growth scare. That is why the volatility curve is still marginally in contango and why `uncertainty` has not tripped.

## 5. Sector rotation — settled 2026-07-29 → 2026-10-29

| ETF | 07-29 close | 10-29 close | 3-month change |
|---|---|---|---|
| XLE | 58.65 | 68.71 | **+17.15%** |
| XLK | 166.57 | 188.74 | **+13.31%** |
| XLV | 166.24 | 184.04 | **+10.71%** |
| SPY | 729.46 | 769.36 | **+5.47%** |
| XLY | 111.61 | 116.20 | **+4.11%** |
| XLB | 51.74 | 52.53 | **+1.53%** |
| XLP | 87.36 | 88.18 | **+0.94%** |
| XLF | 56.68 | 56.94 | **+0.46%** |
| XLI | 176.66 | 170.13 | **-3.70%** |
| XLU | 44.91 | 43.14 | **-3.94%** |
| XLRE | 45.96 | 43.06 | **-6.31%** |
| XLC | 109.51 | 101.21 | **-7.58%** |

The three-month rotation had leadership in energy (+17.15%), technology (+13.31%) and health care (+10.71%), with communication services (−7.58%), real estate (−6.31%), utilities (−3.94%) and industrials (−3.70%) lagging. Technology was the strongest three-month leader in the book and is today's worst sector by more than four points — the reversal is the story, not the rotation itself.

## 6. Single-name movers — 2026-10-30 ~14:02 ET (Nasdaq quote API)

| Ticker | Last | Change | Driver |
|---|---|---|---|
| INTC | 63.6 | **-30.92%** | Q3 beat but weak Q4 revenue outlook and a PC-demand slowdown into 2027; largest single-name drag on the tape |
| RDDT | 89.57 | **-30.89%** | Q3 earnings miss / guidance reset |
| RBLX | 42.38 | **-19.22%** | Q3 earnings; bookings and outlook disappointed |
| TWLO | 202.7 | **-16.21%** | Q3 earnings and Q4 guidance |
| SNDK | 1,129 | **-15.12%** | Q1 beat and Q2 guide above consensus, but the market read it as peak memory pricing |
| MRVL | 191 | **-12.54%** | AI-networking order-book read-through; semi complex de-rating |
| DELL | 415.9 | **-12.54%** | AI server backlog/margin concern; PC demand fear from the Intel guide |
| DDOG | 233.2 | **-12.29%** | Q3 earnings miss; software monetisation worries widening |
| AMD | 497.6 | **-12.16%** | AI accelerator demand and capex-digestion concerns |
| SNOW | 297.8 | **-9.84%** | Q3 earnings; usage-based revenue miss |
| SMCI | 31.57 | **-8.32%** | AI server order/demand concerns |
| MU | 869.1 | **-6.98%** | Memory pricing cycle peak narrative |
| TSM | 402.4 | **-6.82%** | Foundry read-through on AI capex and export restrictions |
| AVGO | 322 | **-6.67%** | Custom silicon / AI revenue-mix concerns |
| ORCL | 130.3 | **-6.64%** | AI capex-vs-cash-flow debate |
| PLTR | 184.6 | **-6.02%** | AI-valuation derating in software |
| NVDA | 202.4 | **-5.28%** | AI capex-digestion trade; less bad than the rest of the complex |
| PANW | 362.1 | **-4.86%** | Q2 earnings and guidance |
| CAT | 623.7 | **-3.66%** | Continued post-earnings derating from Thursday |
| AMZN | 238.7 | **-2.11%** | Capex blowout and -$42.4bn trailing-12M free cash flow; slower e-commerce growth |
| JPM | 337.3 | **-1.83%** | Financials lag the tape; credit fears contained |
| MSFT | 520.6 | **-1.79%** | Relative AI-monetisation strength, but dragged by the capex complex |
| GOOGL | 278.7 | **-1.80%** | Fading Thursday post-earnings pressure |
| META | 614.7 | **-1.58%** | Capex guidance drag |
| AAPL | 344.5 | **-1.26%** | Mega-cap sympathy |
| CRM | 229.5 | **-0.61%** | Resilient versus software peers |
| NFLX | 61.97 | **-0.14%** | Flat; no read-through to the tape |
| LLY | 1,426 | **+3.80%** | Earnings beat; healthcare leadership |
| COST | 1,021 | **+2.67%** | Earnings beat; consumer-staples bid |
| WMT | 124.1 | **+2.32%** | Defensive bid |
| XOM | 186.6 | **+1.82%** | Crude +1.75% on Gulf/Hormuz supply risk; energy bid |

## 7. Regime flags (computed by the skill's own `compute_regime()`)

| Flag | Value | Meaning |
|---|---|---|
| `size_cut_pct` | **0** | Reduce Tier-A sizing by 0%. Not triggered: `index_below_20sma` is true but breadth is 69.3%, far above the 40% floor. |
| `uncertainty` | **false** | Not triggered: VIX/VIX3M = 0.9848 ≤ 1.00. |
| `late_cycle` | **false** | Not triggered: no index ETF is more than 6% above its 50-DMA (max is RSP +2.30%), and none exceeds 2.6 ATR on the true extension measure. |
| `breadth_pct_spx` | 69.33 | Large-cap proxy above 20-DMA, settled 2026-10-29. |
| `index_below_20sma` | true | 2 of 5 index ETFs above their 20-DMA. |

The flags deserve a caveat rather than a clean bill of health: `size_cut_pct` and `late_cycle` are computed from the 2026-10-29 settle, so they describe a tape that no longer exists, and `uncertainty` is computed from a live volatility pair that is 1.5% away from tripping. On today's tape a human would not treat these flags as a green light.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| shibui via MCP bridge | `SELECT MAX(date) FROM shibui.stock_quotes WHERE date <= '2026-10-30'` | ok | latest = 2026-10-29 (T+1) |
| shibui via MCP bridge | `emit_breadth_sql('2026-10-29')` (skill's own module) | ok | breadth + 5 index rows |
| shibui via MCP bridge | universe / 20-50-200-DMA aggregates | ok | 913 names |
| shibui via MCP bridge | sector rotation, 2 dates × 12 tickers | ok | 24 bars |
| shibui via MCP bridge | true ATR extension, 252-session window | ok | 5 rows |
| CBOE delayed-quote CDN | `cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json` | ok (HTTP 200) | 21.38 @ 13:47:31 ET |
| CBOE delayed-quote CDN | `.../_VIX3M.json`, `.../_VIX9D.json` | ok (HTTP 200) | 21.71 / 21.35 @ 13:47:31 ET |
| CBOE delayed-quote CDN | `.../_SPX.json`, `_NDX`, `_RUT`, `_DJX` | ok (HTTP 200) | @ 13:47:35 ET |
| CBOE delayed-quote CDN | 24 index/ETF/sector tickers (SPY, QQQ, RSP, IWM, QQQE, 11 SPDR, GLD, TLT) | ok (HTTP 200) | @ 13:45–13:47 ET |
| CBOE daily history | `cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv`, `VIX3M_History.csv` | ok (HTTP 200) | 10/29 settles confirmed; the 10/30 row has not rolled yet, as expected mid-session |
| Nasdaq quote API | `api.nasdaq.com/api/quote/{SYM}/info?assetclass=stocks` (31 names) | ok (HTTP 200) | @ ~14:02 ET |
| Nasdaq quote API | `.../info?assetclass=etf` (SPY, QQQ, IWM, RSP) | ok (HTTP 200) | implied prior closes match shibui 10/29 to the cent |
| Yahoo Finance | `finance.yahoo.com/quote/%5EVIX/` (HTML) | ok (HTTP 200) | 21.40 @ 13:48:01 ET — independent cross-check of the CBOE print |
| Nasdaq | `api.nasdaq.com/api/market-info` | ok (HTTP 200) | session status only (open, closes 16:00 ET) |
| Nasdaq | `api.nasdaq.com/api/marketmovers?market=stocks&movers=advancers|decliners` | ok but **not usable** (HTTP 200) | returns only "most active by share volume" and top-mover tables — **no advance/decline counts**, so no live A/D breadth tally is available from any reachable feed |
| web_search | press cross-check for the 10/29 settle and today's catalyst | ok | Zacks, Saxo, Investrade, memorandum all agree |

## Caveats

1. **The breadth legs are one session stale.** shibui is a T+1 feed; the 913-name breadth and the 5 index extension rows describe the 2026-10-29 settle. Everything in sections 4 and 6 describes the live 2026-10-30 tape. Do not read them as one coherent snapshot.
2. **The CBOE CDN lags the fetch by roughly 15 minutes.** The payload was fetched at 14:02:35 ET but the last trade stamped on it is 13:47:31 ET. The Nasdaq mover quotes are fresher (~14:02 ET). Each table in this document carries its own as-of time for that reason; there is no single "as of" for the whole file.
3. **`compute_regime()`'s `extension_pct` is not an ATR extension** — see the note under section 2. The `late_cycle` flag is false under both the shipped metric and the spec's intended one, but the column names in the skill are misleading.
4. **No live advance/decline tally was obtainable.** The Nasdaq market-movers endpoint returns only mover tables, and no other reachable feed publishes intraday A/D counts, so live breadth is proxied only by the RSP-versus-SPY spread.
5. **One volatility pair, one timestamp.** VIX 21.38 and VIX3M 21.71 both carry the 13:47:31 ET stamp. No mid-session print has been mixed with a settled close anywhere in this document; the 17.20/19.37 settles appear solely as the labelled change baseline.

Generated by cron #10 `stock-screener-breadth-snapshot` at 2026-10-30 14:03 ET. End-of-day counterpart: `daily-screens/2026-10-30/breadth.md` (cron #09, 18:30 ET).
