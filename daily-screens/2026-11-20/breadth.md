---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "18:30 ET (dispatched 18:30:04 ET)"
data_date: "2026-11-20 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-19)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1064 names; totalCount 1064 = rows fetched, no truncation"
vix_quote_time: "2026-11-20 16:15:01 ET (Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-19; both symbols read from the same session bar, 1 pull(s) 0 s apart — identical)"
vix_pair: "VIX 35.89 / VIX3M 30.94 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-20/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
---

# Breadth & Regime — End-of-Day — Friday 20 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-20. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-19) and are not blended into this file.

## TL;DR

A **thrust into the close with no broadening underneath**: the index ETFs are below their 20-DMA (0 of 5), the average large cap is barely above it (**14.94%**), and the tape ran **211 advancing against 844 declining** (ratio 0.25, net **-633**). Volatility confirms the stress — **VIX 35.89, +26.20%** from 28.44, and the term structure is **inverted** (VIX/VIX3M **1.1600**), so `uncertainty: true`.

The suite's regime reads this as a **size-cut session**: `size_cut_pct: 50`, `index_below_20sma: true`, and `late_cycle: false` — the last one is genuinely computed, not defaulted, since every one of the five index ETFs is *below* its 50-DMA (SPY -9.26%, QQQ -14.42%, QQQE -10.52%, IWM -7.78%, RSP -3.43%). The equal-weight ETF held up best and the cap-weighted growth ETFs held up worst, which is the signature of a megacap-led unwind rather than a broad liquidation.

## Breadth — 2026-11-20 settled session

| Metric | Value |
|---|---|
| Universe | 1064 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **14.94%** (159 / 1064) |
| Above 50-DMA | 32.61% (347 / 1064) |
| Above 200-DMA | 36.00% (383 / 1064) |
| Advance / decline / unchanged | **211 / 844 / 9** — ratio 0.25, net **-633** |
| Median name | -1.40%  ·  mean -2.22% |
| Move distribution | ≥ +5%: 1 · +2..5%: 23 · 0..2%: 196 · −2..0: 400 · −5..−2: 282 · ≤ −5%: 162 |

## Participation — the advance/decline tally

Computed on the **same 1064-name population** as the breadth percentage, from the settled session: **211 advancing, 844 declining, 9 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **-633**, ratio **0.25**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+14.94 pp** |
| band | **MATCHED** |
| large-cap % above 20-DMA | 14.94% |
| index ETFs above their 20-DMA | 0% (0 of 5) |

A **MATCHED** divergence: the average large cap and the index ETFs are in the same posture - the index's own position is representative of the typical large cap, with a divergence of +14.94 pp (the band flips at +/-15 pp).

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 689.81 | -3.64% | 747.81 | 760.18 | 732.76 | **-9.26%** | 1.97% |
| QQQ | 608.45 | -5.67% | 678.53 | 710.96 | 683.06 | **-14.42%** | 3.09% |
| RSP | 207.44 | -1.98% | 218.08 | 214.80 | 209.23 | **-3.43%** | 1.53% |
| IWM | 256.61 | -2.88% | 276.23 | 278.26 | 279.57 | **-7.78%** | 2.12% |
| QQQE | 105.41 | -4.08% | 114.95 | 117.80 | 113.83 | **-10.52%** | 2.25% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at -3.43%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **35.89** | 28.44 | +7.45 (+26.2%) | 2026-11-20 16:15:01 ET |
| VIX3M | **30.94** | 27.03 | +3.91 (+14.5%) | 2026-11-20 16:15:01 ET |

Source: Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-19; both symbols read from the same session bar. Pulled 1 time(s), 0 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **1.1600** → `uncertainty: true` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **50** | size cut is ON - the index is below its 20-DMA and breadth 14.94% is UNDER the 40% trigger |
| `uncertainty` | **true** | the flag fires when VIX/VIX3M > 1.0; the ratio is 1.1600 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max -3.43%, RSP) |
| `index_below_20sma` | **true** | only 0 of 5 index ETFs are above their 20-DMA (0%) |

Payload: `daily-screens/2026-11-20/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Food: Major Diversified | 2 | 100.0% | +2.77% | +2.77% |
| Hospital/Nursing Management | 3 | 0.0% | +1.90% | +2.54% |
| Food: Specialty/Candy | 7 | 85.7% | +1.88% | +1.30% |
| Pharmaceuticals: Generic | 1 | 0.0% | +1.79% | +1.79% |
| Food: Meat/Fish/Dairy | 4 | 50.0% | +1.50% | +1.91% |
| Pharmaceuticals: Other | 1 | 0.0% | +1.11% | +1.11% |
| Marine Shipping | 1 | 0.0% | +1.03% | +1.03% |
| Drugstore Chains | 1 | 0.0% | +1.00% | +1.00% |
| Specialty Insurance | 1 | 100.0% | +0.97% | +0.97% |
| Food Distributors | 2 | 50.0% | +0.91% | +0.91% |
| Homebuilding | 6 | 0.0% | +0.86% | +1.05% |
| Major Telecommunications | 2 | 100.0% | +0.82% | +0.82% |
| Home Improvement Chains | 2 | 50.0% | +0.75% | +0.75% |
| Food Retail | 1 | 100.0% | +0.74% | +0.74% |
| Insurance Brokers/Services | 6 | 100.0% | +0.65% | +0.69% |
| Household/Personal Care | 7 | 57.1% | +0.46% | +0.91% |
| Property/Casualty Insurance | 15 | 60.0% | +0.26% | +0.41% |
| Managed Health Care | 6 | 0.0% | +0.10% | +0.17% |
| Medical Distributors | 3 | 66.7% | +0.10% | +0.22% |
| Financial Publishing/Services | 7 | 0.0% | +0.01% | -0.12% |
| Beverages: Non-Alcoholic | 6 | 16.7% | -0.05% | -0.30% |
| Medical/Nursing Services | 8 | 12.5% | -0.07% | -0.31% |
| Publishing: Books/Magazines | 1 | 0.0% | -0.12% | -0.12% |
| Commercial Printing/Forms | 1 | 100.0% | -0.12% | -0.12% |
| Water Utilities | 3 | 66.7% | -0.14% | +0.69% |
| Environmental Services | 5 | 40.0% | -0.26% | -0.27% |
| Industrial Conglomerates | 1 | 0.0% | -0.27% | -0.27% |
| Services to the Health Industry | 1 | 100.0% | -0.31% | -0.31% |
| Real Estate Investment Trusts | 71 | 7.0% | -0.36% | -0.29% |
| Advertising/Marketing Services | 1 | 100.0% | -0.46% | -0.46% |
| Alternative Power Generation | 4 | 25.0% | -0.57% | -0.19% |
| Agricultural Commodities/Milling | 2 | 0.0% | -0.59% | -0.59% |
| Multi-Line Insurance | 25 | 20.0% | -0.60% | -0.32% |
| Electric Utilities | 41 | 31.7% | -0.61% | -0.17% |
| Pharmaceuticals: Major | 29 | 27.6% | -0.65% | -0.51% |
| Integrated Oil | 22 | 0.0% | -0.66% | -0.66% |
| Oil & Gas Production | 5 | 0.0% | -0.66% | -0.92% |
| Tobacco | 3 | 0.0% | -0.69% | -1.07% |
| Publishing: Newspapers | 3 | 0.0% | -0.81% | -0.78% |
| Containers/Packaging | 5 | 0.0% | -0.85% | -0.40% |
| Wireless Telecommunications | 14 | 50.0% | -0.85% | +0.07% |
| Industrial Specialties | 3 | 0.0% | -0.88% | -1.08% |
| Beverages: Alcoholic | 6 | 50.0% | -1.05% | -1.01% |
| Restaurants | 10 | 50.0% | -1.15% | -1.16% |
| Electronics/Appliance Stores | 2 | 50.0% | -1.17% | -1.17% |
| Cable/Satellite TV | 4 | 50.0% | -1.28% | -0.97% |
| Chemicals: Agricultural | 2 | 0.0% | -1.30% | -1.30% |
| Medical Specialties | 33 | 24.2% | -1.39% | -1.53% |
| Gas Distributors | 6 | 0.0% | -1.43% | -1.53% |
| Apparel/Footwear Retail | 4 | 50.0% | -1.45% | -1.50% |
| Casinos/Gaming | 2 | 0.0% | -1.51% | -1.51% |
| Major Banks | 85 | 5.9% | -1.52% | -1.29% |
| Tools & Hardware | 3 | 0.0% | -1.52% | -1.27% |
| Regional Banks | 33 | 12.1% | -1.55% | -1.55% |
| Oil Refining/Marketing | 5 | 0.0% | -1.58% | -1.37% |
| Railroads | 5 | 0.0% | -1.64% | -1.75% |
| Real Estate Development | 3 | 0.0% | -1.65% | -1.78% |
| Oil & Gas Pipelines | 14 | 0.0% | -1.67% | -1.43% |
| Other Transportation | 3 | 33.3% | -1.68% | -2.39% |
| Construction Materials | 6 | 0.0% | -1.68% | -1.35% |
| Specialty Stores | 15 | 40.0% | -1.69% | -0.77% |
| Finance/Rental/Leasing | 16 | 12.5% | -1.71% | -2.19% |
| Life/Health Insurance | 9 | 0.0% | -1.73% | -2.10% |
| Pulp & Paper | 3 | 0.0% | -1.78% | -1.83% |
| Biotechnology | 15 | 20.0% | -1.81% | -1.73% |
| Hotels/Resorts/Cruise lines | 9 | 22.2% | -1.82% | -1.79% |
| Investment Trusts/Mutual Funds | 2 | 0.0% | -1.91% | -1.91% |
| Electronics/Appliances | 1 | 0.0% | -1.92% | -1.92% |
| Broadcasting | 3 | 33.3% | -1.94% | -1.47% |
| Other Consumer Services | 4 | 25.0% | -1.99% | -1.70% |
| Information Technology Services | 17 | 0.0% | -2.02% | -0.18% |
| Internet Software/Services | 19 | 15.8% | -2.03% | -2.41% |
| Movies/Entertainment | 3 | 33.3% | -2.05% | -1.92% |
| Miscellaneous Commercial Services | 15 | 13.3% | -2.06% | -1.31% |
| Internet Retail | 7 | 0.0% | -2.09% | -2.68% |
| Building Products | 4 | 25.0% | -2.15% | -1.50% |
| Data Processing Services | 7 | 14.3% | -2.23% | -2.56% |
| Chemicals: Specialty | 6 | 0.0% | -2.41% | -2.03% |
| Discount Stores | 3 | 33.3% | -2.42% | -2.23% |
| Investment Managers | 38 | 0.0% | -2.42% | -2.49% |
| Air Freight/Couriers | 9 | 11.1% | -2.47% | -2.65% |
| Home Furnishings | 1 | 0.0% | -2.67% | -2.67% |
| Department Stores | 1 | 100.0% | -2.70% | -2.70% |
| Apparel/Footwear | 5 | 0.0% | -2.72% | -2.76% |
| Investment Banks/Brokers | 23 | 4.3% | -2.78% | -2.13% |
| Chemicals: Major Diversified | 1 | 0.0% | -2.85% | -2.85% |
| Aerospace & Defense | 27 | 0.0% | -3.04% | -2.59% |
| Recreational Products | 2 | 0.0% | -3.10% | -3.10% |
| Auto Parts: OEM | 4 | 0.0% | -3.18% | -3.34% |
| Airlines | 5 | 0.0% | -3.27% | -3.35% |
| Trucks/Construction/Farm Machinery | 5 | 0.0% | -3.29% | -2.98% |
| Engineering & Construction | 9 | 11.1% | -3.59% | -2.86% |
| Financial Conglomerates | 6 | 0.0% | -3.76% | -3.48% |
| Packaged Software | 54 | 14.8% | -3.80% | -3.12% |
| Oilfield Services/Equipment | 2 | 0.0% | -4.00% | -4.00% |
| Contract Drilling | 2 | 0.0% | -4.09% | -4.09% |
| Trucking | 4 | 0.0% | -4.11% | -3.52% |
| Steel | 8 | 0.0% | -4.21% | -4.00% |
| Wholesale Distributors | 9 | 0.0% | -4.24% | -4.47% |
| Industrial Machinery | 24 | 12.5% | -4.33% | -3.15% |
| Motor Vehicles | 9 | 11.1% | -4.54% | -3.72% |
| Metal Fabrication | 2 | 0.0% | -4.93% | -4.93% |
| Precious Metals | 12 | 0.0% | -4.97% | -5.23% |
| Electronics Distributors | 1 | 0.0% | -4.99% | -4.99% |
| Other Metals/Minerals | 7 | 0.0% | -5.14% | -5.26% |
| Telecommunications Equipment | 8 | 12.5% | -5.22% | -4.11% |
| Electrical Products | 8 | 12.5% | -6.59% | -5.80% |
| Electronic Equipment/Instruments | 5 | 0.0% | -6.75% | -7.07% |
| Computer Processing Hardware | 7 | 14.3% | -7.44% | -9.19% |
| Specialty Telecommunications | 2 | 0.0% | -8.20% | -8.20% |
| Semiconductors | 33 | 0.0% | -10.00% | -10.15% |
| Electronic Components | 4 | 0.0% | -10.14% | -9.35% |
| Computer Peripherals | 7 | 0.0% | -10.64% | -12.02% |
| Electronic Production Equipment | 4 | 0.0% | -11.53% | -10.44% |

## Flags

- **Size cut is ON (`size_cut_pct: 50`) with `uncertainty: true` and `index_below_20sma: true`.** This is the suite's own reduce-size regime; `late_cycle: false` is computed from a non-empty `atr_extensions` map, not defaulted.
- **The divergence band sits on its edge.** `breadth_divergence` is **+14.94 pp** — large-cap breadth (14.94% above the 20-DMA) against 0 of 5 index ETFs above theirs — which is **0.06 pp below the +15 pp** threshold that would read `BROAD`, so the published band is `MATCHED`. Read the numbers, not the band word. (The sentence under the band is now derived from the band; it used to be unconditional and contradicted its own label.)
- **The VIX pair came from ONE pull, not two.** The Cboe delayed-quote CDN answered **HTTP 403** (Cloudflare) from this egress — the same block recorded on 2026-11-19 — so the pair was read from the **Yahoo chart API fallback** (`^VIX`/`^VIX3M`, both from the same session bar, 2026-11-20 16:15:01 ET). The fallback pulls once, so the published `vix_stable: true` is **vacuous on this run** — one pull cannot differ from itself. It is not evidence the quote was stable.
- **The universe is not one company's worth of listings.** It carries foreign listings and ADRs (SKM -14.83% in the decliners) and the scanner can publish a broker line alongside the primary (**MKC.V** and **MKC** both appear, different closes) — so a movers table can show the same company twice.
- **The breadth population is TradingView's, not shibui's.** 1,064 names with `market_cap_basic` > $10B. The shibui breadth SQL carried alongside it uses `valuation.market_cap` on a different population, so the two breadth numbers are **not two readings of one series** and are never blended.

## Method, source health & caveats

**Sources and status for this run.**

| Source | Used for | Status |
|---|---|---|
| TradingView scanner (`scanner.tradingview.com/america/scan`) | the **FRESH** book on the cron day's settled bar (3,711 names, `totalCount` asserted) and the breadth universe (1,064 names) | ok |
| shibui-finance MCP over the HTTPS bridge | the **T+1** context book (screen session **2026-11-19**): 8 sweep branches, the theme branch, the CANSLIM growth half, the enrichment pass, the valuation/quality overlay | ok |
| bridge `market-recap get_quotes` | the official 16:00 ET close for the book names (`market_state: post`) | ok |
| Yahoo chart API (`^VIX`, `^VIX3M`) | the volatility pair | ok — **fallback**, after the Cboe delayed-quote CDN answered HTTP 403 |
| `mcp__*` finance tools | — | **not registered in this runtime** (not an error; the bridge is the path) |

**Method.** The run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-20's own settled bar**; the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-19**. Every row publishes `data_as_of` and `source`, and the two are never blended. The coverage assertion holds on **all 9 branches** (`rows_kept == rows_passing`, no branch landing on a cap of 30/50/60/200), and the fresh universe came back **3,711 of 3,711**.

**Caveats.**
- The screen metrics are **T+1**: every Tier-A and Focus metric describes **2026-11-19**, not the session being reported.
- `valuation_gate: unknown` (91 names) means **no reported trailing earnings** — a disclosure, never a pass and never a red flag. `fail` (598 names) means at least one of: trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, or shibui's own earnings-quality flags.
- The overlay is a **label, not a filter** — nothing is dropped from the book for tripping it.
- Nothing in this book is a recommendation; it is a screen's output with its coverage and its caveats attached.
