---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "18:30 ET"
data_date: "2026-11-19 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-18)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1066 names; totalCount 1066 = rows fetched, no truncation"
vix_quote_time: "2026-11-19 16:15:01 ET (Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-19; both symbols read from the same session bar, 1 pull(s) 0 s apart — identical)"
vix_pair: "VIX 28.44 / VIX3M 27.03 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-19/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
---

# Breadth & Regime — End-of-Day — Thursday 19 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-19. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-18) and are not blended into this file.

## TL;DR

- **The market finished at its lows.** The Nasdaq was 2% higher intraday and closed **-2.25% at 23,879.20**; the Dow lost 1,101 points to **49,097.06**, its first close below 50,000 since June; the S&P 500 fell **2.02% to 7,175.83**, a sixth straight loss and the worst streak since April 2024, and it closed roughly 1% below its 200-DMA. The trigger was Anthropic's Nasdaq debut - the moment the AI IPO opened, investors took profits in the AI complex.
- **Breadth is the tell: 939 decliners against 117 advancers** (ratio 0.12) in the 1,066-name $10B+ universe, median name **-1.50%**, and only **21.20%** of the universe above its 20-DMA against 38.18% above the 50-DMA and 38.56% above the 200-DMA. A tape that is falling, not one that is broken long-term.
- **Volatility confirmed the stress: VIX 28.44 (+15.80%)**, its highest close since 30 March, against VIX3M 27.03 - a ratio of **1.0522**, so `uncertainty` is **true**. All five index ETFs closed below their 20-DMA (`index_below_20sma: true`), while `late_cycle` is **false** because no index ETF is more than 6% above its 50-DMA (the extreme is RSP at -1.54%).
- **Leadership was defensive:** Health Care and Consumer Staples topped the sector table; semiconductors and packaged software were the weakest. `size_cut_pct` reads **50** - the size-cut posture is **on**, because the index is below its 20-DMA *and* breadth (21.20%) is under the 40% trigger.

## Breadth — 2026-11-19 settled session

| Metric | Value |
|---|---|
| Universe | 1066 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **21.20%** (226 / 1066) |
| Above 50-DMA | 38.18% (407 / 1066) |
| Above 200-DMA | 38.56% (411 / 1066) |
| Advance / decline / unchanged | **117 / 939 / 10** — ratio 0.12, net **-822** |
| Median name | -1.50%  ·  mean -1.58% |
| Move distribution | ≥ +5%: 7 · +2..5%: 13 · 0..2%: 107 · −2..0: 571 · −5..−2: 329 · ≤ −5%: 39 |

## Participation — the advance/decline tally

Computed on the **same 1066-name population** as the breadth percentage, from the settled session: **117 advancing, 939 declining, 10 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **-822**, ratio **0.12**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+21.20 pp** |
| band | **BROAD** |
| large-cap % above 20-DMA | 21.20% |
| index ETFs above their 20-DMA | 0% (0 of 5) |

A **BROAD** divergence means the average large cap is materially healthier than the index — participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 715.87 | -1.96% | 751.32 | 761.67 | 732.69 | **-6.01%** | 1.71% |
| QQQ | 645.04 | -2.19% | 683.33 | 713.09 | 683.00 | **-9.54%** | 2.67% |
| RSP | 211.63 | -1.76% | 218.54 | 214.95 | 209.19 | **-1.54%** | 1.37% |
| IWM | 264.22 | -2.18% | 277.18 | 278.91 | 279.57 | **-5.27%** | 1.94% |
| QQQE | 109.89 | -1.89% | 115.54 | 118.06 | 113.80 | **-6.92%** | 1.98% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at -1.54%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **28.44** | 24.56 | +3.88 (+15.8%) | 2026-11-19 16:15:01 ET |
| VIX3M | **27.03** | 24.29 | +2.74 (+11.3%) | 2026-11-19 16:15:01 ET |

Source: Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-19; both symbols read from the same session bar. Pulled 1 time(s), 0 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **1.0522** → `uncertainty: true` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **50** | size cut is ON - the index is below its 20-DMA and breadth 21.20% is UNDER the 40% trigger |
| `uncertainty` | **true** | the flag fires when VIX/VIX3M > 1.0; the ratio is 1.0522 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max -1.54%, RSP) |
| `index_below_20sma` | **true** | only 0 of 5 index ETFs are above their 20-DMA (0%) |

Payload: `daily-screens/2026-11-19/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Department Stores | 1 | 100.0% | +11.04% | +11.04% |
| Chemicals: Agricultural | 2 | 0.0% | +0.52% | +0.52% |
| Electronics/Appliance Stores | 2 | 50.0% | +0.24% | +0.24% |
| Computer Peripherals | 7 | 14.3% | +0.17% | -1.17% |
| Services to the Health Industry | 1 | 100.0% | -0.23% | -0.23% |
| Pharmaceuticals: Other | 1 | 0.0% | -0.24% | -0.24% |
| Metal Fabrication | 2 | 0.0% | -0.27% | -0.27% |
| Multi-Line Insurance | 25 | 16.0% | -0.36% | -0.41% |
| Property/Casualty Insurance | 15 | 60.0% | -0.40% | -0.30% |
| Oilfield Services/Equipment | 2 | 0.0% | -0.44% | -0.44% |
| Life/Health Insurance | 9 | 44.4% | -0.58% | -0.35% |
| Commercial Printing/Forms | 1 | 100.0% | -0.61% | -0.61% |
| Oil & Gas Production | 5 | 0.0% | -0.66% | -0.20% |
| Electric Utilities | 41 | 34.1% | -0.67% | -0.83% |
| Specialty Insurance | 1 | 100.0% | -0.69% | -0.69% |
| Environmental Services | 5 | 40.0% | -0.69% | -0.86% |
| Investment Banks/Brokers | 23 | 13.0% | -0.74% | -0.75% |
| Major Banks | 85 | 9.4% | -0.83% | -0.70% |
| Computer Processing Hardware | 7 | 14.3% | -0.88% | -1.04% |
| Alternative Power Generation | 4 | 50.0% | -0.89% | -1.00% |
| Oil & Gas Pipelines | 14 | 0.0% | -0.94% | -0.84% |
| Regional Banks | 34 | 14.7% | -0.96% | -0.56% |
| Home Improvement Chains | 2 | 50.0% | -0.96% | -0.96% |
| Chemicals: Major Diversified | 2 | 100.0% | -0.96% | -0.96% |
| Wireless Telecommunications | 14 | 50.0% | -1.00% | -0.95% |
| Real Estate Investment Trusts | 66 | 15.2% | -1.00% | -1.07% |
| Data Processing Services | 7 | 14.3% | -1.03% | -0.90% |
| Food Distributors | 2 | 50.0% | -1.03% | -1.03% |
| Food: Major Diversified | 2 | 100.0% | -1.09% | -1.09% |
| Oil Refining/Marketing | 5 | 0.0% | -1.11% | -1.02% |
| Publishing: Books/Magazines | 1 | 0.0% | -1.11% | -1.11% |
| Water Utilities | 3 | 66.7% | -1.12% | -1.08% |
| Biotechnology | 16 | 25.0% | -1.13% | -1.29% |
| Chemicals: Specialty | 7 | 0.0% | -1.18% | -1.12% |
| Contract Drilling | 2 | 0.0% | -1.19% | -1.19% |
| Insurance Brokers/Services | 6 | 100.0% | -1.20% | -0.60% |
| Food: Meat/Fish/Dairy | 4 | 50.0% | -1.21% | -0.97% |
| Agricultural Commodities/Milling | 2 | 0.0% | -1.25% | -1.25% |
| Pharmaceuticals: Major | 29 | 34.5% | -1.25% | -1.85% |
| Motor Vehicles | 9 | 11.1% | -1.31% | -0.98% |
| Medical Specialties | 33 | 30.3% | -1.32% | -1.57% |
| Industrial Machinery | 25 | 24.0% | -1.39% | -1.75% |
| Investment Trusts/Mutual Funds | 2 | 0.0% | -1.39% | -1.39% |
| Industrial Conglomerates | 1 | 0.0% | -1.43% | -1.43% |
| Food: Specialty/Candy | 7 | 42.9% | -1.46% | -1.31% |
| Electronic Components | 4 | 0.0% | -1.46% | -1.45% |
| Steel | 8 | 0.0% | -1.49% | -1.52% |
| Discount Stores | 3 | 33.3% | -1.53% | -1.54% |
| Integrated Oil | 22 | 0.0% | -1.55% | -1.06% |
| Aerospace & Defense | 28 | 14.3% | -1.56% | -1.63% |
| Financial Publishing/Services | 7 | 0.0% | -1.58% | -1.78% |
| Auto Parts: OEM | 5 | 40.0% | -1.58% | -1.40% |
| Food Retail | 1 | 0.0% | -1.61% | -1.61% |
| Information Technology Services | 17 | 11.8% | -1.61% | -2.03% |
| Drugstore Chains | 1 | 0.0% | -1.61% | -1.61% |
| Electronics Distributors | 1 | 0.0% | -1.64% | -1.64% |
| Gas Distributors | 6 | 0.0% | -1.64% | -1.61% |
| Wholesale Distributors | 9 | 11.1% | -1.66% | -1.70% |
| Air Freight/Couriers | 9 | 44.4% | -1.67% | -1.15% |
| Trucking | 5 | 40.0% | -1.67% | -0.90% |
| Telecommunications Equipment | 8 | 37.5% | -1.71% | -1.42% |
| Tools & Hardware | 3 | 0.0% | -1.72% | -1.31% |
| Major Telecommunications | 2 | 100.0% | -1.73% | -1.73% |
| Investment Managers | 38 | 0.0% | -1.74% | -1.55% |
| Building Products | 3 | 66.7% | -1.82% | -1.83% |
| Beverages: Alcoholic | 6 | 66.7% | -1.88% | -1.80% |
| Airlines | 5 | 20.0% | -1.95% | -1.95% |
| Financial Conglomerates | 6 | 0.0% | -1.97% | -1.33% |
| Industrial Specialties | 3 | 33.3% | -1.97% | -1.95% |
| Real Estate Development | 3 | 33.3% | -2.01% | -1.69% |
| Restaurants | 10 | 80.0% | -2.04% | -1.98% |
| Beverages: Non-Alcoholic | 6 | 33.3% | -2.06% | -2.10% |
| Household/Personal Care | 7 | 42.9% | -2.06% | -1.95% |
| Medical Distributors | 3 | 66.7% | -2.08% | -2.05% |
| Railroads | 5 | 0.0% | -2.13% | -2.06% |
| Apparel/Footwear Retail | 4 | 50.0% | -2.18% | -2.19% |
| Electrical Products | 8 | 12.5% | -2.18% | -2.18% |
| Broadcasting | 3 | 33.3% | -2.18% | -2.90% |
| Construction Materials | 6 | 0.0% | -2.22% | -2.09% |
| Semiconductors | 33 | 12.1% | -2.22% | -2.28% |
| Internet Retail | 7 | 0.0% | -2.27% | -3.49% |
| Electronic Equipment/Instruments | 5 | 0.0% | -2.29% | -1.98% |
| Finance/Rental/Leasing | 16 | 6.2% | -2.30% | -2.34% |
| Trucks/Construction/Farm Machinery | 5 | 0.0% | -2.30% | -3.08% |
| Other Transportation | 3 | 33.3% | -2.32% | -1.47% |
| Tobacco | 3 | 0.0% | -2.37% | -2.07% |
| Internet Software/Services | 19 | 21.1% | -2.48% | -2.41% |
| Homebuilding | 6 | 0.0% | -2.51% | -2.33% |
| Other Metals/Minerals | 7 | 0.0% | -2.52% | -1.63% |
| Movies/Entertainment | 3 | 66.7% | -2.53% | -1.72% |
| Packaged Software | 55 | 25.5% | -2.55% | -2.35% |
| Miscellaneous Commercial Services | 15 | 20.0% | -2.57% | -2.46% |
| Cable/Satellite TV | 4 | 50.0% | -2.60% | -2.91% |
| Containers/Packaging | 5 | 0.0% | -2.62% | -2.49% |
| Electronic Production Equipment | 4 | 0.0% | -2.67% | -2.49% |
| Medical/Nursing Services | 7 | 28.6% | -2.70% | -1.96% |
| Pulp & Paper | 3 | 0.0% | -2.84% | -2.50% |
| Engineering & Construction | 9 | 22.2% | -2.87% | -2.51% |
| Other Consumer Services | 4 | 50.0% | -2.91% | -2.95% |
| Specialty Stores | 15 | 46.7% | -2.91% | -1.04% |
| Advertising/Marketing Services | 1 | 100.0% | -2.95% | -2.95% |
| Casinos/Gaming | 2 | 50.0% | -2.98% | -2.98% |
| Managed Health Care | 6 | 0.0% | -3.06% | -2.72% |
| Publishing: Newspapers | 3 | 0.0% | -3.11% | -3.14% |
| Precious Metals | 13 | 0.0% | -3.42% | -3.16% |
| Hotels/Resorts/Cruise lines | 9 | 44.4% | -3.84% | -3.76% |
| Recreational Products | 2 | 0.0% | -3.98% | -3.98% |
| Hospital/Nursing Management | 3 | 0.0% | -4.06% | -3.36% |
| Specialty Telecommunications | 2 | 0.0% | -4.14% | -4.14% |
| Apparel/Footwear | 5 | 0.0% | -4.52% | -4.96% |
| Home Furnishings | 1 | 0.0% | -4.82% | -4.82% |
| Electronics/Appliances | 1 | 100.0% | -5.78% | -5.78% |
| Pharmaceuticals: Generic | 1 | 0.0% | -8.74% | -8.74% |

## Flags

- **Size cut ON.** `size_cut_pct: 50` - index below its 20-DMA and breadth 21.20% under the 40% trigger. The 20/50/200-DMA split (21.20% / 38.18% / 38.56%) says a falling tape, not a broken long-term one.
- **Volatility pair, one source, cross-checked.** The Cboe delayed-quote CDN (`cdn.cboe.com/.../_VIX.json`) returned **HTTP 403** (a Cloudflare interstitial) from this egress, so the pair was read from Yahoo's chart API instead - **both** symbols from the **same** session bar, pinned to 2026-11-19. The reading matches the published close for the session exactly (VIX 28.44, +3.88, +15.80%, 4:15 PM ET), so this is the settled close, not a stale or intraday print. `vix_stable: true` (single pull).
- **Uncertainty is on, and it is not marginal.** VIX/VIX3M = 1.0522, above the 1.0 line - the flag fires. The VIX3M curve (27.03) is only 5% below the VIX (28.44), which is what a stress print looks like rather than a front-month kink.
- **Index posture:** 0 of 5 index ETFs above their 20-DMA; none more than 6% above its 50-DMA, so `late_cycle` is **false**.
- **A genuine zero, not a truncated branch:** the 10% gap trigger published **0** names on the settled bar (`rows_passing` 0 = `rows_kept` 0) - no $10B+ name gapped +10% today.
- **One transient retry, no data lost:** the shibui enrichment pass hit a gateway error on attempt 1 and succeeded on retry; the coverage assertion passed on every branch afterwards.

## Method, source health & caveats

**Sources.** TradingView's per-country scanner is the primary source for everything measured on the cron day's settled bar (the fresh trigger book, the breadth universe, the index ETFs and the movers tables); shibui-finance over the MCP-over-HTTP bridge supplies the multi-session context screens (T+1), the ADR%, the CANSLIM growth half and the valuation/quality overlay; the volatility pair comes from the Cboe delayed-quote CDN, or - on this run - from Yahoo's chart API, because the Cboe CDN answered HTTP 403 from this egress (see the flags).

**The two clocks.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) are computed on **2026-11-19's own settled bar**; the CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-18**. Every row publishes `data_as_of` and `source` (`fresh` / `t1` / `fresh+t1`), and the two books are never blended. The breadth read in `breadth.md` is NOT T+1 - it is computed from the cron day's settled close.

**Coverage.** Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`; `rows_kept == rows_passing` on **9 of 9** branches and no branch count lands on a cap (30 / 50 / 60 / 200). 1,269 screened rows -> 1,129 distinct candidates; fresh book 270 names, T+1 book 1,093.

**What could not be verified.** (1) The Cboe volatility CDN was unavailable from this egress, so the VIX/VIX3M pair was served by Yahoo's chart API - cross-checked against the published session close, which matched to the cent, but it is a different vendor than the suite normally uses. (2) The screen metrics are one session behind the close, so the four trigger branches and the context branches describe different tapes by construction. (3) shibui's own quotes are T+1 and its valuation rows are the latest available at or before the resolved date, so the market-cap floor and the overlay inherit that lag. (4) No analyst-consensus or fundamentals feed was used for the multi-session context beyond shibui's quarterly growth columns; the overlay's PEG and P/E come from shibui's `fundamentals_derived_daily` and are as stale as that table is.

**One degraded source, one retry.** The Cboe volatility CDN (HTTP 403) is the only degraded input on this run; the shibui enrichment gateway error was retried and succeeded, so it is not counted as a degradation.
