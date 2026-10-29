---
fire_time_et: 2026-10-29 14:03
data_date: 2026-10-28
data_date_note: "shibui end-of-day feed is T+1 — the breadth numbers describe the 2026-10-28 settled close, not the live 2026-10-29 session. The live tape section below carries the 2026-10-29 intraday read."
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 908 names (large-cap proxy for the S&P 500 — shibui exposes no S&P 500 constituent table, so the skill's large-cap filter stands in)"
vix_quote_time: "2026-10-29 13:48:31 ET — CBOE delayed-quote CDN (cdn.cboe.com/api/global/delayed_quotes)"
cross_reference: "end-of-day counterpart: daily-screens/2026-10-29/breadth.md (cron #09, 18:30 ET)"
producer: "cron #10 stock-screener-breadth-snapshot (intraday, 14:00 ET)"
skill: "stock-screener-suite — step 3, breadth/regime snapshot"
volatility_pair: "VIX 16.76 / VIX3M 19.11 — the only volatility pair in this document"
---

# Breadth & Regime Snapshot — 2026-10-29 (intraday, 14:03 ET)

**Headline: the tape is rotating, not breaking.** Breadth as of the 2026-10-28 settle was healthy and mildly narrowing — 63.8% of large caps above their 20-DMA, still above the 40% threshold that would trigger a size cut — while the live 2026-10-29 session is selling the AI complex hard while equal-weight and small-caps rally. Cap-weighted SPY is **-0.69%** but RSP is **+0.73%** and IWM **+0.72%**, a 1.4pp spread inside a single index in one session. Volatility is *falling* on that rotation (VIX 16.76, -0.89%), which is the tell: this is capital reallocating within equities, not risk leaving the market.

**Caveat that most changes how to read this:** the breadth numbers and the volatility numbers come from different sessions. Breadth is the 2026-10-28 settled close (shibui is a T+1 end-of-day feed and 2026-10-28 is its latest bar); VIX and the index levels are live 2026-10-29 prints at ~13:48 ET. Read the two tables as sequential — last week's positioning, this morning's tape — not as a single simultaneous snapshot.

---

## Regime payload

| Flag | Value | Trigger |
|---|---|---|
| `size_cut_pct` | **0** | Not triggered — requires index below 20-DMA **and** breadth < 40%. Breadth is 63.77% and 4 of 5 index ETFs are above their 20-DMA. |
| `uncertainty` | **false** | VIX / VIX3M = 16.76 / 19.11 = **0.877** < 1.0 — the front end is not stressed relative to the 3-month tenor. |
| `late_cycle` | **false** | No index ETF is extended. True ATR extension vs its own 252-day median ranges 0.75x (IWM) to 0.95x (QQQ) — every one below 1.0x. |
| `breadth_pct_spx` | 63.77 | Large-cap proxy above 20-DMA, 2026-10-28. |
| `index_below_20sma` | false | 4 of 5 index ETFs above their 20-DMA (80%); 3 of 5 above their 50-DMA (60%). |

The regime reads **constructive-but-not-extended**: positioning is not crowded, volatility is orderly, and there is no distribution signal in the breadth data. The regime flags are computed on the 2026-10-28 settle and have not been re-derived for the live 2026-10-29 tape.

---

## Breadth — large-cap proxy (2026-10-28 settled close)

| Metric | Count | % of universe |
|---|---|---|
| Universe (NYSE/NASDAQ/AMEX, mcap > $10B) | 908 | 100.0% |
| Above 20-DMA | 579 | **63.77%** |
| Below 20-DMA | 329 | 36.23% |
| Above 50-DMA | 493 | 54.29% |
| Above 200-DMA | 500 | 55.07% |

The 20-DMA reading is the headline breadth number and it is comfortably constructive. The more interesting split is the 20-DMA versus 50-DMA gap: 63.8% above 20-DMA but only 54.3% above 50-DMA means leadership is broad *recently* but roughly half the universe is still working back to its intermediate trend. That is a recovering-but-not-confirmed tape, which is also why the intraday equal-weight strength today is newsworthy rather than noise.

### Breadth trend, last eight sessions

| Session | Names | % above 20-DMA | % above 50-DMA |
|---|---|---|---|
| 2026-10-19 | 896 | 58.82 | 41.41 |
| 2026-10-20 | 904 | 66.15 | 48.67 |
| 2026-10-21 | 907 | **68.25** | 51.49 |
| 2026-10-22 | 901 | 66.59 | 54.50 |
| 2026-10-23 | 895 | 64.36 | 53.52 |
| 2026-10-26 | 901 | 65.37 | 54.05 |
| 2026-10-27 | 904 | 65.82 | 54.09 |
| 2026-10-28 | 908 | 63.77 | **54.30** |

Breadth peaked at 68.25% on 2026-10-21 and has eased for five straight sessions, −4.5pp to 63.77%. The 50-DMA reading has moved the other way, grinding steadily higher from 41.41% to 54.30% — so participation is migrating from short-term strength into intermediate strength rather than breaking down. Breadth is narrowing, but the character of the narrowing is orderly consolidation, not distribution. It is also worth noting the universe itself grew from 896 to 908 names, so the percentage decline is not an artifact of the filter tightening.

---

## Index position and true ATR extension (2026-10-28 settled close)

| Symbol | Close | Distance from 50-DMA | ATR% now | 252d median ATR% | ATR extension |
|---|---|---|---|---|---|
| SPY | 772.31 | +0.61% | 0.899 | 1.081 | 0.83x |
| RSP | 217.43 | +1.07% | 0.889 | 1.041 | 0.85x |
| QQQ | 725.61 | +0.03% | 1.520 | 1.606 | 0.95x |
| QQQE | 119.86 | −0.23% | 1.220 | 1.290 | 0.95x |
| IWM | 281.29 | −1.30% | 1.257 | 1.686 | **0.75x** |

> **Known bug in the skill's own breadth SQL.** `emit_breadth_sql()` computes `atr_252d_avg` inside a CTE already filtered to a single date, so the `AVG(...) OVER (... ROWS BETWEEN 251 PRECEDING AND CURRENT ROW)` window holds exactly one row and collapses to `atr_14`. The column it returns as `extension_pct` is therefore **distance from the 50-DMA**, not an ATR extension. This run confirmed the collapse again (`atr_252d_avg == atr_14` for all five symbols) and computed the genuine ATR extension separately, over a real 252-session window, as shown in the last column above. The `late_cycle` conclusion is unaffected: the skill's own column peaks at +1.07% (RSP), far below its 6% threshold, and the true extension peaks at 0.95x.

Qwik is the most extended name on its own history at 0.95x of median ATR%, and IWM the least at 0.75x — small caps are trading materially calmer than their own one-year norms. That is consistent with the live tape, where IWM is one of the better performers today.

---

## Live tape — 2026-10-29 intraday

Quotes timed 13:48–13:52 ET on 2026-10-29. The "prev close" column is the 2026-10-28 settled close, which reconciles to the cent against the shibui daily bars.

| Index / ETF | Live | Prev close (10-28) | Change | Source |
|---|---|---|---|---|
| S&P 500 (SPX) | 7698.72 | 7743.98 | −0.58% | CBOE delayed CDN |
| Nasdaq-100 (NDX) | 29330.68 | 29813.20 | **−1.62%** | CBOE delayed CDN |
| Russell 2000 (RUT) | 2852.77 | 2830.51 | **+0.79%** | CBOE delayed CDN |
| SPY | 766.99 | 772.31 | −0.69% | Nasdaq quote API |
| QQQ | 712.71 | 725.61 | **−1.78%** | Nasdaq quote API |
| QQQE | 118.63 | 119.86 | −1.03% | Nasdaq quote API |
| RSP (equal-weight S&P) | 219.02 | 217.43 | **+0.73%** | Nasdaq quote API |
| IWM | 283.31 | 281.29 | **+0.72%** | Nasdaq quote API |

This is the defining shape of the session: **the average S&P 500 stock is up while the index is down.** SPX −0.58% against RSP +0.73% means the cap-weighted index is being dragged by a handful of mega-caps while the median constituent gains. NDX at −1.62% is nearly three times the SPX move, confirming the damage is concentrated in the large-growth/AI cohort. Small caps are also participating on the upside (RUT +0.79%), which follows a two-week Russell 2000 recovery out of a ~13% August–October drawdown.

The driver is **Alphabet's Q3 miss**, the worst session in its history: EPS $2.12 against a $3.01 consensus, Search and YouTube ad revenue both light, and negative free cash flow over $9bn with capex guided higher again. Cloud revenue of $30.7bn still grew 103%, but the market is now repricing AI return on invested capital rather than AI spend. Microsoft beat on both lines (Azure +49%) and fell only −0.68% because its $45.2bn quarterly capex came in *below* the $50bn consensus — the same "capex discipline" read that hurt Alphabet. ServiceNow (−26.69%) and Fortinet (−21.96%) extend the software de-rating; Caterpillar fell −9.33% on its own results. Against that, Merck (+4.42%), Eli Lilly (+6.24%) and Meta (+2.41%) held up. Amazon and Intel report after the close, and the Fed's hawkish hold (see below) keeps December hike pricing alive as a rate-sensitive overhang.

### Live single-name movers (2026-10-29, ~14:05 ET)

| Ticker | Live | Change | Driver |
|---|---|---|---|
| NOW | 110.07 | −26.69% | Q3 profit miss; software-sector de-rating |
| FTNT | 135.85 | −21.96% | Q3 results; −5.9% on 10-28, then −22% after the bell |
| GOOGL | 282.16 | −13.15% | Q3 miss; worst session ever; FCF and capex concerns |
| GOOG | 280.13 | −12.97% | Same event (Class C) |
| CAT | 646.83 | −9.33% | Q3 results, pre-market |
| AMZN | 244.79 | −3.86% | Pre-earnings de-risking; reports after the close |
| AVGO | 344.50 | −2.08% | AI-hardware complex |
| TSM | 430.13 | −2.13% | AI-hardware complex |
| NVDA | 212.88 | −1.16% | Sector sympathy |
| MSFT | 527.39 | −0.68% | Beat, but capex below consensus |
| META | 627.27 | +2.41% | Relative safety |
| MRK | 147.16 | +4.42% | Q3 results, pre-market |
| LLY | 1368.64 | +6.24% | Strong Q3 GLP-1 results |

---

## Volatility — single pair

| Measure | Value | Prev close | Change | Quote time (ET) |
|---|---|---|---|---|
| VIX | **16.76** | 16.91 | −0.89% | 2026-10-29 13:48:31 |
| VIX3M | **19.11** | 19.22 | −0.57% | 2026-10-29 13:48:31 |

Source: CBOE delayed-quote CDN, both legs from the same feed and the same timestamp. VIX/VIX3M = **0.877**, comfortably below the 1.0 line that flags front-end stress, so `uncertainty` is false. Note that the term structure is **inverted** (VIX below VIX3M) — the market is paying up for longer-dated optionality, not for near-term protection, which is consistent with a rotation trade rather than a de-risking trade. This is the one pair of volatility readings in this document; the end-of-day counterpart may quote a different pair because it is taken at the 16:00 settle.

---

## Sector rotation — 3-month (2026-07-29 → 2026-10-28)

| ETF | Sector | 3-month return | vs SPY |
|---|---|---|---|
| XLE | Energy | **+16.71%** | +10.84 |
| XLK | Technology | +14.67% | +8.80 |
| XLV | Health care | +8.11% | +2.24 |
| **SPY** | **S&P 500** | **+5.87%** | — |
| XLY | Cons. discretionary | +3.33% | −2.54 |
| XLB | Materials | +0.23% | −5.64 |
| XLP | Cons. staples | −0.60% | −6.47 |
| XLF | Financials | −0.97% | −6.84 |
| XLI | Industrials | −4.62% | −10.49 |
| XLU | Utilities | −5.39% | −11.26 |
| XLC | Comm. services | −5.82% | −11.69 |
| XLRE | Real estate | **−8.33%** | −14.20 |

Three months of leadership is narrow and cyclical: energy and technology carry it, while real estate is last — a rate-sensitive sector giving back ground, which is what you would expect as the Fed shifts from pausing toward pricing a December hike. The interesting wrinkle is that **communication services is −5.82%** over the same window *before* today's Alphabet collapse; today's GOOGL −13% will push that materially lower. Today's intraday tape extends the same rotation in real time, with the 3-month losers (real estate, utilities, staples) the beneficiaries of capital leaving the AI complex.

---

## Largest movers in the breadth universe (2026-10-28 settled close)

Verified ticker-by-ticker against Nasdaq's historical table — every close and volume above matches to the cent.

### Gainers

| Ticker | Close | Change | Volume | Catalyst |
|---|---|---|---|---|
| GMAB | 57.29 | **+28.25%** | 29.3M | Phase 3 LiGeR-HN1: petosemtamab + pembrolizumab cut risk of death **50%** (HR 0.50, p<0.0001) in 1L head-and-neck cancer; record high on ~9x average volume |
| ICLR | 214.16 | **+17.04%** | 3.9M | Q3 adj EPS $2.66 vs $2.64 est; record $3.15B net business wins, book-to-bill 1.56x; FY26 guidance raised to $8.10–8.20B rev / $10.35–10.65 EPS; buyback lifted to $750M |
| VRT | 242.94 | **+16.48%** | 19.5M | Q3 net sales +61% to $4.31B, adj EPS $2.21; organic orders more than doubled; FY26 sales guide raised $650M to $14.45–14.85B |
| SKHY | 164.70 | **+13.30%** | 50.0M | SK hynix — memory/AI-hardware complex bid alongside Vertiv, SanDisk, Micron |
| STLA | 4.68 | **+13.04%** | 119.5M | Q3 EPS −$0.01 vs $0.25 cons and revenue $42.6B vs $46.9B, but 2026 guidance **reaffirmed**, Value Creation Program ahead of schedule, AOI margin +50bp, industrial FCF +€300M; still −58% YTD |
| EVR | 292.38 | +12.51% | 1.1M | Evercore — Q3 results (pre-open) |
| FLEX | 93.03 | +11.61% | 13.1M | Flex — Q3 results |
| VSAT | 78.26 | +11.32% | 4.7M | Viasat — Q3 results |
| JLL | 333.34 | +11.14% | 1.1M | Jones Lang LaSalle — Q3 results, consensus EPS $6.15 (+36.7%) |
| ORCL | 144.54 | +10.73% | 81.9M | Investor day: capex to peak this year/next, then fall to support ≥$30B FY29 FCF; revenue outlook through FY2030 |
| LH | 360.25 | +8.78% | 1.8M | Labcorp — Q3 results |
| ENSG | 184.11 | +8.62% | 9.7M | Ensign Group — Q3 results |

### Losers

| Ticker | Close | Change | Volume | Catalyst |
|---|---|---|---|---|
| FFIV | 365.53 | **−20.43%** | 3.6M | F5: fiscal Q4 beat (rev $917.4M +13%, adj EPS $4.42) **overridden** by FY27 revenue growth guided to 8–9% vs 11%, non-GAAP operating margin 33.7% vs 37.0% on memory/component costs, Q1 EPS guide slightly light; worst S&P 500 performer, steepest drop in over a decade; Piper Sandler downgrade to Neutral |
| LPLA | 269.19 | **−15.23%** | 5.2M | LPL Financial: adj EPS +15%, but expected assets from newly recruited advisors **−26%** YoY |
| CSGP | 27.54 | **−13.96%** | 18.3M | CoStar Group — Q3 results |
| LOGI | 98.27 | **−12.12%** | 3.0M | Logitech — Q3 results |
| CHRW | 127.60 | **−11.14%** | 4.8M | C.H. Robinson: an operating **beat** (adj EPS $1.80 +28.6%, income from ops +23.1%) sold off on cash conversion — operating cash flow −$151.3M to $124.1M on working capital |
| LII | 332.64 | −10.59% | 2.4M | Lennox International — Q3 results |
| BKR | 54.66 | −7.36% | 18.5M | Baker Hughes — capital rotated out of energy equipment into AI infrastructure |
| ODFL | 173.32 | −7.33% | 4.9M | Old Dominion Freight Line |
| BSBR | 4.54 | −6.20% | 7.2M | Santander Consumer USA |
| BBD | 2.73 | −6.19% | 101.0M | Banco Bradesco |
| FTNT | 174.08 | −5.90% | 11.1M | Fortinet — Q3 results; fell a further −22% on 2026-10-29 |
| BSX | 42.43 | −5.84% | 69.8M | Boston Scientific |

---

## Macro backdrop

The **FOMC met 2026-10-27/28** and released its statement at 14:00 ET on Wednesday 2026-10-28 — the day *before* this snapshot's fire time, so today's prints are **post-decision day 1**, not pre-statement. The Committee **held** the target range at **3.75–4.00%** on a **10–2 vote**, with Governor Lisa Cook and Cleveland Fed President Beth Hammack dissenting *in favour of a 25bp hike*. The statement kept "inflation remains elevated", upgraded activity from "solid" to "strong" pace, and added that "the accumulation of more information will help the Committee determine the policy stance appropriate to ensure a timely return of inflation to the Committee's 2 percent goal" — a hawkish hold. Fed funds futures and the dot plot now lean toward an additional 25bp in **December**, which the Fed framed as waiting out the 2026 midterms. The 2026-10-29 session adds a soft PCE print (in line) and a Q3 GDP first estimate (above consensus) alongside Alphabet and Microsoft.

For the breadth read this matters in two places: it keeps rate-sensitive sectors (real estate, utilities) under pressure on a 3-month basis, and it is the reason today's tape is a rotation *out of* the longest-duration, cap-weighted AI names rather than a broad risk-off.

---

## Method & caveats

- **Mixed-session artifact by design.** Breadth and index levels are the 2026-10-28 settled close (shibui end-of-day feed, T+1); VIX, VIX3M and the live tape are 2026-10-29 prints at ~13:48 ET. The two must not be read as simultaneous.
- **Breadth universe is a large-cap proxy, not the S&P 500.** shibui exposes no S&P 500 constituent table, so the skill's `market_cap > $10B` filter over NYSE/NASDAQ/AMEX stands in — 908 names on 2026-10-28, drifting 895–908 across the eight-session trend window.
- **The skill's `emit_breadth_sql()` has a degenerate window function** (`atr_252d_avg` collapses to `atr_14` because the CTE is date-filtered to one row per symbol). This run reproduces the bug and supplies a genuine 252-session ATR-extension window alongside it; see the Index position table.
- **Live quotes are delayed.** CBOE's delayed-quote CDN and the Nasdaq quote API both carry a short delay; the VIX legs are stamped 13:48:31 ET and the index legs 13:50–13:52 ET against a 14:03 ET fire time. Approximately 12–15 minutes stale.
- **CBOE's delayed-quote CDN covers indices only** — it returns HTTP 403 for ETFs, so SPY/QQQ/RSP/IWM/QQQE live levels come from the Nasdaq quote API instead.
- **Yahoo's JSON endpoints remain unusable** from this sandbox (HTTP 429 on chart, spark and screener alike). The Yahoo `^VIX` HTML page was deliberately avoided — it serves related-quote and trending-ticker prices that are not VIX.
- **The Yahoo `^VIX` HTML page is a decoy** and was not used: it returns 25 `regularMarketPrice` occurrences, none of which is VIX (they belong to the related-quotes stream). All volatility data here comes from the CBOE CDN.
- **`sector_rotation` (financekit) and the TradingView screens were not called** — neither server is exposed in this runtime. Sector rotation was computed from shibui daily bars instead, over a 2026-07-29 → 2026-10-28 window.
- **Mover catalysts are press-verified but not exhaustive.** Catalysts for EVR, FLEX, VSAT, JLL, LH, ENSG, CSGP, LII, ODFL are stated as earnings-driven without a specific figure; everything with a number attached was cross-checked against a second source.
- **Every Oct-28 close and volume in the mover tables was verified against Nasdaq's historical table — 17 of 17 tickers, to the cent.**
- The `> $10B` market-cap floor means large single-session losers below the line (e.g. ENPH −16% on 2026-10-28) do **not** appear in the universe tables.

## Source health

| Source | Query / URL | Status |
|---|---|---|
| shibui via MCP-over-HTTP bridge — `stock_data_query` | `emit_breadth_sql('2026-10-28')`, plus 6 custom SQL (universe, true ATR extension, sector rotation, breadth trend, gainers, losers) | **ok** — 8/8 calls returned data; bridge not rate-limited |
| shibui date resolution | `SELECT MAX(date) FROM shibui.stock_quotes WHERE date <= '2026-10-29'` | **ok** — latest_date = 2026-10-28 (T+1) |
| CBOE delayed-quote CDN | `cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json`, `_VIX3M.json` | **ok** — HTTP 200, quote time 2026-10-29 13:48:31 ET |
| CBOE delayed-quote CDN (indices) | `_SPX.json`, `_NDX.json`, `_RUT.json` | **ok** — HTTP 200, quote time 2026-10-29 13:50:35–37 ET |
| CBOE delayed-quote CDN (ETFs) | `_SPY.json`, `_QQQ.json`, `_RSP.json`, `_IWM.json`, `_QQQE.json` | **failed: HTTP 403** — CDN covers indices only; ETF levels sourced from Nasdaq instead |
| Nasdaq quote API | `api.nasdaq.com/api/quote/{SYM}/info?assetclass=etf|stocks` | **ok** — 8 ETFs + 25 stocks; `netChange` reconciles exactly to the 2026-10-28 shibui settle |
| Nasdaq historical API | `api.nasdaq.com/api/quote/{SYM}/historical?fromdate=2026-10-26&todate=2026-10-29` | **ok** — 17/17 tickers matched shibui's Oct-28 close and volume to the cent |
| stocktwits via MCP-over-HTTP bridge | `chart_data` {symbol: SPY/QQQ, period: 1D} | **ok** — intraday 5-min bars corroborate the Nasdaq live levels within ~0.1% |
| Yahoo Finance JSON (chart / spark / screener) | — | **failed: HTTP 429** persistent rate limit; not used, no fallback attempted (CBOE + Nasdaq + shibui covered the run) |
| Yahoo Finance `^VIX` HTML | `finance.yahoo.com/quote/%5EVIX/` | **not used** — known decoy (25 `regularMarketPrice` hits, none of them VIX) |
| financekit `sector_rotation` | — | **unavailable** — server not exposed in this runtime; sector rotation computed from shibui daily bars instead |
| `mcp__tradingview__*` / `mcp__tradingview-advanced__*` | — | **unavailable** — not registered in this runtime; no MCP call attempted |
| federalreserve.gov / CNBC / Reuters / Schwab | FOMC statement and calendar; session wraps | **ok** — FOMC outcome and 2026-10-29 drivers verified against primary and secondary sources |
| Yahoo JSON → Nasdaq API → Yahoo HTML fallback chain | — | **not exercised** — the primary bridge and CBOE/Nasdaq paths served every field |

---

*Cross-reference: the end-of-day counterpart is `daily-screens/2026-10-29/breadth.md` (cron #09, 18:30 ET), computed from the same settled 2026-10-28 close but with a settled volatility print. The two are expected to differ.*
