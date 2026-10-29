# Breadth / Regime Snapshot — 2026-10-28

**Regime: risk-ON but narrow, and the calm is a pre-event calm.** Broad participation is healthy — 596 of 905 large-caps (65.86%) closed above their 20-DMA on 2026-10-27 — yet the cap-weighted indices sit mostly *below* their own 20-DMA (only 2 of 5 ETFs above), because the AI complex absorbed a punishing October and the industrials are the weakest three-month sector of the eleven. Volatility looks serene: VIX 17.3 against a VIX3M of 19.31 (ratio 0.90, under the 1.0 uncertainty threshold), and every index ETF trading at or below its own 252-day median ATR%. Regime flags come back **clean**: no size cut, no uncertainty band, no late-cycle extension.

**The single most important caveat: the FOMC decision was released at 14:00 ET today — one minute before this snapshot was taken — with Chair Warsh speaking at 14:30.** The VIX print here is timestamped 13:46:16 ET, i.e. **pre-statement**, and every breadth, ATR and rotation figure is from the 2026-10-27 close. Nothing in this document reflects the Fed's decision, Warsh's tone, or the market's reaction to either. The compressed-volatility reading should be read as *the tape going into a central-bank event*, not as an all-clear. Markets priced a hold at roughly 93% (CME FedWatch at the 2026-10-27 close) against a backdrop of elevated inflation and a hiking bias — the September hike was the first in three years, and a December hike is priced near 80%.

### Deviations and caveats (read first)

- **The FOMC statement landed at 14:00 ET, during this run.** The volatility data is a 13:46 ET print and the breadth data is a 2026-10-27 close. Treat the volatility section as pre-event context, not as a current market state.
- **Data lag — shibui is T+1.** Every breadth, ATR and rotation number below is the **2026-10-27 close**. The cron fired 2026-10-28 at 14:01 ET.
- **`financekit sector_rotation` is not available in this runtime.** Sector rotation was recomputed locally from shibui sector-ETF prices over the 3-month window — a faithful price-based substitute, not the same provider's output.
- **`tradingview-advanced yahoo_price` is not available in this runtime.** VIX and VIX3M come from the CBOE official delayed-quote feed, cross-checked against the CBOE product page and Yahoo's options chain.
- **The helper's `atr_252d_avg` column is degenerate.** `emit_breadth_sql()` computes it with a window over a CTE already filtered to a single date, so the partition holds exactly one row and the value collapses to `atr_14` for every symbol. The canonical `extension_pct` is consequently *distance from the 50-DMA*, not an ATR extension. A true ATR-extension multiple over a proper 252-session window is supplied alongside it.
- **This is a large-cap breadth proxy, not the S&P 500.** shibui has no index-constituents table, so breadth is computed over NYSE/NASDAQ/AMEX names with market cap above $10B (905 names on 2026-10-27).

### Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | 50 only when index < 20-DMA **and** breadth < 40%; breadth is 65.86%, so no cut |
| `uncertainty` | false | VIX/VIX3M = 17.3/19.31 = 0.8959; > 1.0 would flag stress |
| `late_cycle` | false | no index ETF is more than 6% above its 50-DMA (max is RSP at +1.09%) |
| `breadth_pct_spx` | 65.86% | large-cap proxy above 20-DMA |
| `index_below_20sma` | true | 2 of 5 index ETFs above their 20-DMA |

All three flags are benign, and the interesting tension is internal: `index_below_20sma` is true while breadth is 65.86%. That combination is the signature of a **narrow, sector-driven tape** rather than a broad decline — the average large-cap is fine, the indices are held back by a few heavyweights that are recovering from their own drawdowns. `size_cut_pct` stays at 0 because the skill's rule requires *both* conditions and breadth never approaches 40%. Note that the `uncertainty` flag is a *volatility* test, not an event test: it says nothing about the Fed statement landing 60 seconds after this file was written.

### Breadth

| Metric | Value |
|---|---|
| Universe (NYSE/NASDAQ/AMEX, mcap > $10B) | 905 |
| Above 20-DMA | 596 |
| Below 20-DMA | 308 |
| Missing 20-DMA | 1 |
| **% above 20-DMA** | **65.86%** |

A 65.86% reading is solidly constructive — roughly two thirds of the large-cap universe is in an uptrend, and the index ETFs are *less* extended than that average implies. That gap is the whole story of this session: the median large-cap is in an uptrend while the cap-weighted indices are not.

### Index extension — 50-DMA distance and true ATR extension

| ETF | Close | SMA-20 | vs SMA-20 | SMA-50 | vs SMA-50 | ATR-14 | ATR% | ATR ext × 252d med |
|---|---|---|---|---|---|---|---|---|
| SPY | 769.66 | 770.41 | -0.10% | 767.53 | +0.28% | 7.164 | 0.931% | 0.861× |
| RSP | 217.52 | 213.44 | +1.91% | 215.18 | +1.09% | 1.968 | 0.905% | 0.869× |
| QQQ | 721.25 | 733.18 | -1.63% | 725.26 | -0.55% | 11.426 | 1.584% | 0.986× |
| QQQE | 119.31 | 119.84 | -0.44% | 120.19 | -0.73% | 1.497 | 1.255% | 0.973× |
| IWM | 280.18 | 277.10 | +1.11% | 285.37 | -1.82% | 3.620 | 1.292% | 0.766× |

Only **RSP** (equal-weight, +1.91% over its 20-DMA) and **IWM** (+1.11%) are above their 20-DMA; QQQ is the weakest at −1.63%. SPY sits a hair below its 20-DMA (−0.10%) while still above its 50-DMA (+0.28%), so the broad index is consolidating just under a short-term trend line rather than breaking down. IWM is the one to watch on the downside: it is above its 20-DMA but 1.82% *below* its 50-DMA, and industrials are the worst three-month sector in the rotation table below.

The right-hand column is the more informative one. Every index ETF trades **below** its own 252-day median ATR% (0.766× to 0.986×), IWM most of all. That is textbook volatility compression — and it is the correct interpretation to pair with the FOMC event risk. The market was coiled into a central-bank decision with realised volatility well under its own one-year norm. Whether that coiled energy resolves into a bigger move than the VIX quote implied is exactly what this snapshot cannot tell you, because the quote predates the statement.

### Volatility

| Metric | Value | Prev close | Change |
|---|---|---|---|
| VIX | 17.3 | 17.52 | -0.22 (-1.26%) |
| VIX3M | 19.31 | 19.57 | -0.26 (-1.33%) |
| **VIX / VIX3M** | **0.8959** | — | below the 1.00 uncertainty threshold |
| Quote timestamp | 2026-10-28T13:46:16 ET (pre-FOMC) | — | CBOE delayed feed |

Both legs of the complex are falling together and the front end (17.3) sits *below* the 3-month (19.31) — the calm, contango-ish configuration. The CBOE product page reports the same session VIX at $17.31 and the prior close of 17.52 is confirmed independently by Yahoo's options chain. The skill spec's original `^VXV` has no live Yahoo data, so the skill's own patched approach of using VIX3M was kept. **The ratio is computed on a 13:46:16 ET print, fourteen minutes before the FOMC statement — re-read it before acting on it.**

### Sector rotation — 3 months to 2026-10-27

| Rank | ETF | Sector | 3-mo return | vs SPY (pp) |
|---|---|---|---|---|
| 1 | XLE | Energy | +18.48% | +14.59 |
| 2 | XLK | Technology | +10.75% | +6.86 |
| 3 | XLV | Health Care | +7.13% | +3.24 |
| 4 | XLY | Cons. Discretionary | +2.64% | -1.25 |
| 5 | XLP | Cons. Staples | +0.10% | -3.79 |
| 6 | XLB | Materials | -1.07% | -4.96 |
| 7 | XLF | Financials | -2.99% | -6.88 |
| 8 | XLC | Communication | -5.55% | -9.44 |
| 9 | XLU | Utilities | -5.87% | -9.76 |
| 10 | XLRE | Real Estate | -7.76% | -11.65 |
| 11 | XLI | Industrials | -7.98% | -11.87 |
| — | **SPY** | **Benchmark** | **+3.89%** | **0.00** |

The leadership is unambiguous: **Energy (+18.48%, +14.59 pp vs SPY)**, then Technology (+10.75%) and Health Care (+7.13%). The laggards are just as clear — Industrials (−7.98%), Real Estate (−7.76%) and Utilities (−5.87%) sit roughly 10–12 pp behind the benchmark, with Financials (−2.99%) and Communication Services (−5.55%) also negative.

That ordering is the rotation table's most important message in a hiking-cycle regime. The Fed raised in September for the first time in three years and the statement said inflation remains elevated; a December hike is priced near 80%. Energy leading and real estate, utilities and industrials lagging is the textbook expression of that backdrop — an inflation hedge bid against rate-sensitive and cyclically-exposed groups. It is a rotation *within* a market that is not de-risking broadly: SPY still returned +3.89% over the window, and 65.86% of large-caps stayed above their 20-DMA throughout.

### Large-cap movers — 2026-10-27 close

| Top gainers | Close | Prev close | Change |
|---|---|---|---|
| SOFI | 16.40 | 14.46 | +13.42% |
| PNR | 62.29 | 55.22 | +12.80% |
| CLS | 276.54 | 246.65 | +12.12% |
| NBIS | 170.47 | 153.27 | +11.22% |
| CRDO | 167.43 | 151.15 | +10.77% |
| ALAB | 286.69 | 259.51 | +10.47% |
| CBRS | 119.31 | 108.37 | +10.10% |
| LECO | 282.37 | 258.65 | +9.17% |

| Top losers | Close | Prev close | Change |
|---|---|---|---|
| XYL | 92.86 | 108.24 | -14.21% |
| BA | 168.18 | 188.31 | -10.69% |
| VLO | 387.34 | 426.76 | -9.24% |
| DINO | 114.21 | 125.25 | -8.81% |
| AIT | 297.58 | 324.68 | -8.35% |

The 2026-10-27 session was an **AI-infrastructure rebound**. The gainers are dominated by the AI complex — **CLS** +12.12% (Q3 revenue up 83%, raised guidance, AI data-centre demand), **NBIS** +11.22%, **CRDO** +10.77% and **ALAB** +10.47% (both AI-connectivity silicon) — with **SOFI** +13.42% the largest move of all on a Q3 beat and raised full-year guidance, and **PNR** +12.80% also in CNBC's midday movers list. Yahoo's market wrap for the session recorded SOFI at $16.40 (+13.42%), CLS +12.12%, NBIS +11.22% and ALAB at $286.69 (+10.47%) — every one of those matches the shibui figures in this table to the cent, which is a clean independent validation of the data path.

The rebound is a bounce inside a drawdown, not a trend break: Nebius, CoreWeave and IREN were each down more than 35% over October, and Astera had slid roughly 21% over the prior month before these two sessions. That is precisely why QQQ and QQQE remain below their 20-DMA while the equal-weight RSP is above it. On the other side, the losers are led by refiners **VLO** −9.24% and **DINO** −8.81% alongside **XYL** −14.21% and **BA** −10.69%, consistent with oil easing on the day — a reminder that the 3-month energy leadership and the 1-day energy tape pointed in opposite directions.

### Method & caveats

- Breadth, index extension, sector rotation and movers are **one query per component** against shibui via the MCP-over-HTTP bridge, using the SQL emitted by the skill's own `emit_breadth_sql()` — imported and executed directly, so the query text is byte-identical to the spec rather than retyped.
- The regime payload is produced by the skill's own `compute_regime()` function, fed the unmodified breadth rows plus the two volatility readings — not re-implemented by hand.
- Sector rotation uses a 3-month price window from 2026-07-28 to 2026-10-27. Relative strength is the simple return spread versus SPY in percentage points; the raw ratio-of-ratios is not used.
- The true ATR-extension multiple uses a 252-session trailing median of ATR% over 312 available sessions per symbol, from the same shibui source. It is supplementary and does not feed the regime flags.
- No figure in this report was hand-transcribed: every number is read from saved JSON responses by the generator script. Press-sourced numbers (Fed pricing, index moves, mover closes) are labelled and cited by outlet in the text above.
- VIX/VIX3M are 20-minute-delayed quotes and predate the FOMC statement; all shibui figures are settled closes. The report intentionally mixes a live pre-event volatility reading with a settled-yesterday breadth picture, as the skill specifies.

### Source health

| Source | Endpoint / query | Status | Result |
|---|---|---|---|
| shibui (bridge) | `SELECT MAX(date) FROM shibui.stock_quotes WHERE date <= '2026-10-28'` | ok | `2026-10-27` — T+1 lag confirmed |
| shibui (bridge) | `emit_breadth_sql('2026-10-27')` (canonical) | ok | 7 rows — 5 index ATR extensions + breadth + index summary |
| shibui (bridge) | breadth universe aggregate | ok | 905 large-caps, 596 above 20-DMA |
| shibui (bridge) | 252-session ATR extension (supplementary) | ok | 5 rows |
| shibui (bridge) | sector ETF 3-mo relative strength | ok | 11 rows |
| shibui (bridge) | large-cap movers / losers | ok | 8 + 5 rows |
| CBOE | `cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json` | ok | VIX 17.3 @ 2026-10-28T13:46:16 ET |
| CBOE | `cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX3M.json` | ok | VIX3M 19.31 @ 2026-10-28T13:46:16 ET |
| CBOE (cross-check) | cboe.com VIX product page via web_search | ok | spot 17.31, prev close 17.52 — agrees with API |
| Yahoo (cross-check) | finance.yahoo.com/quote/^VIX/options | ok | prev close 17.52 confirmed |
| Yahoo (cross-check) | market wrap, 2026-10-27 | ok | SOFI $16.40 +13.42%, CLS +12.12%, NBIS +11.22%, ALAB $286.69 +10.47% — matches shibui |
| Press (cross-check) | CNBC / Investopedia / Perplexity movers, 2026-10-27 | ok | SOFI, PNR confirmed in CNBC movers list; ALAB close confirmed |
| Press (event) | CNBC / AFP / FOMC minutes, 2026-10-28 | ok | FOMC statement 14:00 ET, Warsh 14:30 ET; hold ~93% priced; target 3.75-4.00% |
| Yahoo JSON API | chart / spark / screener | **failed: 429 rate-limited** | not used — persistent per runtime contract |
| Nasdaq API | `api.nasdaq.com/api/quote/VIX/info?assetclass=index` | failed: `data: null` | index not covered — fell back to CBOE |
| CBOE CDN (no redirect follow) | `_VIX.json` | failed: 307 | resolved with `-L` |
| financekit | `sector_rotation` | **unavailable** | MCP server not registered in this runtime; recomputed from shibui |
| tradingview-advanced | `yahoo_price` | **unavailable** | MCP server not registered in this runtime; substituted CBOE feed |

### Files

- `daily-screens/2026-10-28/breadth-snapshot.md` — this report
- `daily-screens/2026-10-28/_regime.json` — machine-readable regime payload
