---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "2026-11-27 18:30:03 ET"
data_date: "2026-11-27 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-25)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1090 names; totalCount 1090 = rows fetched, no truncation"
vix_quote_time: "2026-11-27 13:15:00 ET (Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-27 (first observed 2026-11-19, reproduced 2026-11-25); both symbols read from the same session bar, 1 pull(s) 0 s apart — identical)"
vix_pair: "VIX 23.81 / VIX3M 23.82 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-27/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---

# Breadth & Regime — End-of-Day — Friday 27 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-27. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-25) and are not blended into this file.

## TL;DR

- **Breadth on the 2026-11-27 settled close: 50.64% of the $10B+ universe (1090 names) above its 20-DMA**, with **831 advancing against 247 declining** (net **+584**, ratio 3.36, median name +0.78%). Participation was strong and broad — this is not a narrow advance.
- **The divergence is the story: +30.64 pp, band BROAD.** Only **1 of 5** index ETFs (RSP) is above its own 20-DMA, while SPY sits **−3.81%** and QQQ **−7.76%** below their 50-DMA. The average large cap is materially healthier than the cap-weighted index — so the index is the weak leg, and the tape is participation-led rather than megacap-led. `index_below_20sma: true`, `size_cut_pct: 0`, `late_cycle: false`.
- **Caveat that changes how to read it:** the volatility pair came from a **fallback feed** (the Cboe delayed-quote CDN answered HTTP 403 from this egress), so VIX 23.81 / VIX3M 23.82 (ratio 0.9996, `uncertainty: false`) is the Yahoo chart-API fallback, and it was pulled **once** — the stability check was not exercised. The universe is `type in {stock, dr}` and contains class lines and a PBC structure, so the 1090 names are not all common shares.

## Breadth — 2026-11-27 settled session

| Metric | Value |
|---|---|
| Universe | 1090 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **50.64%** (552 / 1090) |
| Above 50-DMA | 50.28% (548 / 1090) |
| Above 200-DMA | 45.87% (500 / 1090) |
| Advance / decline / unchanged | **831 / 247 / 12** — ratio 3.36, net **+584** |
| Median name | +0.78%  ·  mean +1.35% |
| Move distribution | ≥ +5%: 71 · +2..5%: 199 · 0..2%: 573 · −2..0: 239 · −5..−2: 6 · ≤ −5%: 2 |

## Participation — the advance/decline tally

Computed on the **same 1090-name population** as the breadth percentage, from the settled session: **831 advancing, 247 declining, 12 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **+584**, ratio **3.36**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+30.64 pp** |
| band | **BROAD** |
| large-cap % above 20-DMA | 50.64% |
| index ETFs above their 20-DMA | 20% (1 of 5) |

A **BROAD** divergence: the average large cap is materially healthier than the index - participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 728.32 | +1.62% | 738.28 | 757.20 | 733.34 | **-3.81%** | 2.11% |
| QQQ | 650.99 | +2.69% | 663.51 | 705.73 | 683.69 | **-7.76%** | 3.26% |
| RSP | 218.38 | +1.22% | 217.51 | 214.93 | 209.48 | **+1.61%** | 1.60% |
| IWM | 273.79 | +1.83% | 273.88 | 276.93 | 279.63 | **-1.13%** | 2.12% |
| QQQE | 112.50 | +2.42% | 113.25 | 117.28 | 113.98 | **-4.07%** | 2.38% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at +1.61%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **23.81** | 26.8 | -2.99 (-11.2%) | 2026-11-27 13:15:00 ET |
| VIX3M | **23.82** | 26.29 | -2.47 (-9.4%) | 2026-11-27 13:15:00 ET |

Source: Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-27 (first observed 2026-11-19, reproduced 2026-11-25); both symbols read from the same session bar. Pulled 1 time(s), 0 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **0.9996** → `uncertainty: false` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | size cut is off - breadth 50.64% is not under the 40% trigger |
| `uncertainty` | **false** | the flag fires when VIX/VIX3M > 1.0; the ratio is 0.9996 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max +1.61%, RSP) |
| `index_below_20sma` | **true** | only 1 of 5 index ETFs are above their 20-DMA (20%) |

Payload: `daily-screens/2026-11-27/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Computer Peripherals | 7 | 14.3% | +7.38% | +7.15% |
| Precious Metals | 13 | 30.8% | +6.62% | +6.87% |
| Semiconductors | 33 | 12.1% | +5.17% | +4.96% |
| Electronic Components | 5 | 0.0% | +5.07% | +4.83% |
| Electronic Production Equipment | 4 | 0.0% | +4.64% | +4.44% |
| Water Utilities | 3 | 100.0% | +4.27% | +0.89% |
| Specialty Telecommunications | 2 | 0.0% | +4.01% | +4.01% |
| Other Metals/Minerals | 7 | 14.3% | +3.65% | +3.93% |
| Electronic Equipment/Instruments | 5 | 0.0% | +3.43% | +3.22% |
| Electrical Products | 8 | 25.0% | +3.29% | +2.49% |
| Electronics Distributors | 1 | 0.0% | +3.23% | +3.23% |
| Computer Processing Hardware | 9 | 33.3% | +3.14% | +3.21% |
| Steel | 8 | 12.5% | +3.08% | +2.92% |
| Pulp & Paper | 3 | 100.0% | +2.96% | +1.68% |
| Airlines | 5 | 60.0% | +2.87% | +2.74% |
| Agricultural Commodities/Milling | 2 | 0.0% | +2.71% | +2.71% |
| Internet Retail | 7 | 42.9% | +2.71% | +3.68% |
| Motor Vehicles | 9 | 55.6% | +2.64% | +1.44% |
| Telecommunications Equipment | 8 | 50.0% | +2.63% | +2.87% |
| Alternative Power Generation | 2 | 100.0% | +2.55% | +2.55% |
| Oil Refining/Marketing | 5 | 0.0% | +2.37% | +2.10% |
| Aerospace & Defense | 28 | 53.6% | +2.35% | +1.81% |
| Contract Drilling | 2 | 0.0% | +2.33% | +2.33% |
| Packaged Software | 57 | 45.6% | +2.24% | +2.06% |
| Casinos/Gaming | 2 | 50.0% | +2.22% | +2.22% |
| Trucks/Construction/Farm Machinery | 7 | 71.4% | +2.14% | +2.06% |
| Oilfield Services/Equipment | 2 | 0.0% | +2.11% | +2.11% |
| Home Furnishings | 1 | 100.0% | +2.03% | +2.03% |
| Electronics/Appliances | 1 | 100.0% | +1.93% | +1.93% |
| Drugstore Chains | 1 | 0.0% | +1.91% | +1.91% |
| Investment Banks/Brokers | 25 | 44.0% | +1.81% | +1.20% |
| Hospital/Nursing Management | 3 | 100.0% | +1.76% | +2.01% |
| Cable/Satellite TV | 5 | 40.0% | +1.70% | +1.38% |
| Advertising/Marketing Services | 1 | 100.0% | +1.69% | +1.69% |
| Chemicals: Agricultural | 2 | 50.0% | +1.64% | +1.64% |
| Information Technology Services | 15 | 66.7% | +1.62% | +1.51% |
| Internet Software/Services | 20 | 60.0% | +1.58% | +0.82% |
| Miscellaneous Commercial Services | 16 | 75.0% | +1.57% | +1.49% |
| Engineering & Construction | 9 | 55.6% | +1.55% | +1.77% |
| Metal Fabrication | 2 | 100.0% | +1.54% | +1.54% |
| Broadcasting | 3 | 33.3% | +1.53% | +1.53% |
| Chemicals: Specialty | 6 | 50.0% | +1.50% | +1.53% |
| Chemicals: Major Diversified | 2 | 100.0% | +1.47% | +1.47% |
| Industrial Machinery | 25 | 56.0% | +1.46% | +0.98% |
| Construction Materials | 6 | 83.3% | +1.43% | +1.26% |
| Containers/Packaging | 5 | 100.0% | +1.43% | +0.60% |
| Wholesale Distributors | 9 | 44.4% | +1.42% | +1.43% |
| Trucking | 5 | 60.0% | +1.42% | +1.60% |
| Real Estate Development | 3 | 100.0% | +1.40% | +1.39% |
| Finance/Rental/Leasing | 16 | 50.0% | +1.38% | +1.36% |
| Food Distributors | 2 | 100.0% | +1.33% | +1.33% |
| Oil & Gas Production | 5 | 40.0% | +1.30% | +1.17% |
| Financial Conglomerates | 6 | 33.3% | +1.29% | +0.96% |
| Integrated Oil | 22 | 9.1% | +1.28% | +1.05% |
| Investment Managers | 38 | 47.4% | +1.28% | +1.54% |
| Investment Trusts/Mutual Funds | 2 | 50.0% | +1.26% | +1.26% |
| Hotels/Resorts/Cruise lines | 9 | 77.8% | +1.18% | +0.77% |
| Department Stores | 1 | 100.0% | +1.16% | +1.16% |
| Air Freight/Couriers | 9 | 55.6% | +1.12% | +0.90% |
| Wireless Telecommunications | 14 | 71.4% | +1.08% | +0.71% |
| Major Banks | 85 | 30.6% | +1.07% | +0.18% |
| Auto Parts: OEM | 5 | 60.0% | +1.06% | +1.88% |
| Movies/Entertainment | 3 | 100.0% | +0.95% | +1.18% |
| Apparel/Footwear | 5 | 60.0% | +0.93% | +0.92% |
| Oil & Gas Pipelines | 14 | 28.6% | +0.93% | +0.80% |
| Tobacco | 3 | 66.7% | +0.88% | +0.80% |
| Specialty Insurance | 1 | 100.0% | +0.86% | +0.86% |
| Other Consumer Services | 5 | 40.0% | +0.85% | +0.70% |
| Industrial Conglomerates | 1 | 100.0% | +0.74% | +0.74% |
| Specialty Stores | 15 | 66.7% | +0.70% | +0.13% |
| Tools & Hardware | 3 | 33.3% | +0.68% | +0.70% |
| Life/Health Insurance | 9 | 55.6% | +0.66% | +0.43% |
| Medical/Nursing Services | 8 | 62.5% | +0.65% | +1.00% |
| Beverages: Alcoholic | 6 | 33.3% | +0.65% | -0.42% |
| Multi-Line Insurance | 25 | 76.0% | +0.56% | +0.41% |
| Regional Banks | 35 | 28.6% | +0.56% | +0.54% |
| Insurance Brokers/Services | 6 | 100.0% | +0.54% | +0.29% |
| Publishing: Newspapers | 3 | 33.3% | +0.53% | +0.84% |
| Other Transportation | 3 | 33.3% | +0.51% | +0.42% |
| Managed Health Care | 6 | 0.0% | +0.45% | +0.58% |
| Gas Distributors | 6 | 33.3% | +0.43% | +0.07% |
| Financial Publishing/Services | 7 | 14.3% | +0.38% | +0.46% |
| Medical Specialties | 31 | 71.0% | +0.35% | +0.34% |
| Industrial Specialties | 3 | 100.0% | +0.35% | +0.22% |
| Pharmaceuticals: Major | 36 | 69.4% | +0.30% | +0.38% |
| Home Improvement Chains | 2 | 100.0% | +0.30% | +0.30% |
| Property/Casualty Insurance | 15 | 86.7% | +0.28% | +0.25% |
| Restaurants | 10 | 100.0% | +0.28% | +0.19% |
| Biotechnology | 14 | 85.7% | +0.22% | -0.04% |
| Railroads | 5 | 40.0% | +0.21% | +0.27% |
| Pharmaceuticals: Generic | 1 | 0.0% | +0.20% | +0.20% |
| Data Processing Services | 7 | 57.1% | +0.16% | +0.43% |
| Food: Meat/Fish/Dairy | 4 | 100.0% | +0.15% | +0.42% |
| Electric Utilities | 41 | 53.7% | +0.12% | -0.01% |
| Household/Personal Care | 7 | 100.0% | +0.12% | -0.21% |
| Real Estate Investment Trusts | 75 | 44.0% | +0.10% | +0.00% |
| Marine Shipping | 1 | 100.0% | +0.02% | +0.02% |
| Medical Distributors | 3 | 100.0% | -0.03% | -0.02% |
| Environmental Services | 5 | 60.0% | -0.03% | -0.32% |
| Beverages: Non-Alcoholic | 6 | 50.0% | -0.07% | -0.11% |
| Recreational Products | 2 | 50.0% | -0.11% | -0.11% |
| Homebuilding | 6 | 100.0% | -0.17% | -0.14% |
| Commercial Printing/Forms | 1 | 100.0% | -0.18% | -0.18% |
| Publishing: Books/Magazines | 1 | 100.0% | -0.29% | -0.29% |
| Apparel/Footwear Retail | 4 | 50.0% | -0.29% | -0.40% |
| Major Telecommunications | 2 | 100.0% | -0.32% | -0.32% |
| Electronics/Appliance Stores | 2 | 100.0% | -0.39% | -0.39% |
| Food: Specialty/Candy | 7 | 85.7% | -0.57% | -0.38% |
| Food: Major Diversified | 2 | 100.0% | -0.59% | -0.59% |
| Food Retail | 1 | 100.0% | -0.67% | -0.67% |
| Services to the Health Industry | 1 | 100.0% | -0.88% | -0.88% |
| Building Products | 4 | 75.0% | -0.95% | +0.45% |
| Pharmaceuticals: Other | 1 | 0.0% | -0.96% | -0.96% |
| Discount Stores | 3 | 66.7% | -1.36% | -1.35% |

## Flags

- **The volatility pair was pulled ONCE, not twice.** `vix_stable: true` here means "one pull, nothing to disagree with" — a print that moved between pulls would not have been caught. Both symbols were read from the same session bar (2026-11-27 13:15:00 ET), so the pair is internally consistent; its cross-source corroboration is missing.
- **The movers table's Chg column is the scanner's `change` field**, not a re-derived close-to-close change. On this feed that field can lag the `close` it is paired with (measured >1% off on a large share of names on other sessions), so treat XP +18.07%, SNDK +15.96% and COHR +14.07% as the vendor's own change field rather than an independently recomputed print.
- **Class lines and non-common structures sit inside the "large-cap" universe.** **WSO.B** (Watsco class B) is the top decliner at −5.38% and **CHTRP** (Charter preferred A) closes at −2.24%; the $10B cap is company-level, so a class line's move percentage is not comparable with its common shares.
- **ANT (Anthropic, PBC Class A)** appears in the movers table at +10.98% on 91.88 — a public-benefit-corporation line, not a conventional listed operating company, so it is a poor candidate for the screen's own market-cap and ADR assumptions.
- **BSP (Bending Spoons S.p.A.)** at −2.72% is a foreign private issuer inside the $10B universe; its line is not comparable with a US domestic listing on the same metrics.
- No per-symbol data defect was found in the advance/decline tally: 831 + 247 + 12 = **1090**, exactly the published universe count, so the participation figures and the breadth percentage share one denominator.

## Method, source health & caveats

**The dual book and what each date means.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) are computed on **2026-11-27's own settled bar** from the TradingView scanner, whose `close` is the official 16:00 ET print — 144 names, of which 21 are fresh-only. The multi-session CONTEXT screens (5-day gainers/losers, the 14-day velocity, the anticipation/coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-25** (T+1). Every row in `_results.json` carries `data_as_of` and `source` (`fresh` / `t1` / `fresh+t1`); the two books are published side by side and never blended, and they are never substituted for one another.

**Coverage assertion.** Every branch was fetched as its own uncapped query with `COUNT(*) OVER () AS rows_passing` computed inside the branch, then paged until the rows collected equalled `rows_passing`. **9/9 branches complete**, no branch carries an inner `LIMIT`, and no branch count lands on a cap value (30 / 50 / 60 / 200) — so a count of 150 or 213 here is a screen outcome, not a truncation. The coverage table is published in the method section above and in `_results.json` under `screen_coverage`.

**Universes are not interchangeable.** The screen pre-filter is close > $3, market cap > $300M, 30-day average volume > 100k, NYSE/NASDAQ/AMEX. The breadth universe is a different population — `market_cap_basic > $10B`, `type in {stock, dr}` — and the two are never mixed in one denominator. `Perf.W` is deliberately NOT used as the 5-session move: TradingView's weekly performance correlates r=0.997 with a SIX-session move against only r=0.924 with a five-session move, so the parabolic gates (+25% / −25% / −50%) stay on shibui and stay labelled T+1 rather than being silently shifted by a session.

**The overlay is a label, never a filter.** 671 of 1145 screened names carry at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags); 101 are `unknown` — no red flag but no reported trailing earnings either, which is a **disclosure, not a flag** and is never counted as one. Nothing is dropped from the book for tripping a rule; the extension label is published on every row for the same reason, and Tier-A is published twice (`tier-a-fresh.md`, `tier-a-extended.md`).

**Known feed caveat.** The scanner's `change` column can lag the `close` it is paired with on this feed, so where a move and a close are both published the close from the same pull is the anchor and the change field is labelled as the vendor's own.

**Volatility.** The Cboe delayed-quote CDN answered HTTP 403 from this egress, so the pair was served by the Yahoo chart-API fallback, read from a single session bar and published with its quote time. The pair was pulled **once**, so `vix_stable: true` reflects an absence of disagreement opportunity, not a demonstrated stability.
