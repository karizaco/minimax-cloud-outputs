---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "2026-11-12 18:30 ET"
data_date: "2026-11-12 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-11)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1106 names; totalCount 1106 = rows fetched, no truncation"
vix_quote_time: "2026-11-12 16:15:01 ET (Cboe delayed-quote CDN, 2 pulls 5 s apart — identical)"
vix_pair: "VIX 18.7 / VIX3M 20.06 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-12/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---

# Breadth & Regime — End-of-Day — Thursday 12 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-12. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-11) and are not blended into this file.

## TL;DR

- **Breadth is 53.07% above the 20-DMA** on 1,106 large caps, but the session itself was broadly soft: advance/decline **242 / 860 / 4** (ratio 0.28, net -618), median name -0.88%, mean -1.06%.
- **The divergence is +13.07 pp — MATCHED.** 2 of 5 index ETFs are above their own 20-DMA, so the broad universe is still ahead of the index without leaving the matched band.
- **Caveat that changes how to read it:** VIX 18.70 / VIX3M 20.06 (ratio 0.9322) with `uncertainty: false`, but **QQQ sits -4.24% below its own 50-DMA while RSP is +2.68% above it** — the cap-weighted index is the weak leg, and breadth is a LEVEL while advance/decline is a RATE; today they disagree in sign.

## Breadth — 2026-11-12 settled session

| Metric | Value |
|---|---|
| Universe | 1106 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **53.07%** (587 / 1106) |
| Above 50-DMA | 52.35% (579 / 1106) |
| Above 200-DMA | 49.46% (547 / 1106) |
| Advance / decline / unchanged | **242 / 860 / 4** — ratio 0.28, net **-618** |
| Median name | -0.88%  ·  mean -1.06% |
| Move distribution | ≥ +5%: 5 · +2..5%: 22 · 0..2%: 219 · −2..0: 631 · −5..−2: 201 · ≤ −5%: 28 |

## Participation — the advance/decline tally

Computed on the **same 1106-name population** as the breadth percentage, from the settled session: **242 advancing, 860 declining, 4 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **-618**, ratio **0.28**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+13.07 pp** |
| band | **MATCHED** |
| large-cap % above 20-DMA | 53.07% |
| index ETFs above their 20-DMA | 40% (2 of 5) |

A **MATCHED** divergence means the average large cap is materially healthier than the index — participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 757.12 | -0.35% | 759.47 | 764.80 | 731.62 | **-1.00%** | 1.45% |
| QQQ | 688.17 | -0.32% | 696.94 | 718.62 | 681.99 | **-4.24%** | 2.37% |
| RSP | 220.72 | -0.87% | 218.30 | 214.96 | 208.74 | **+2.68%** | 1.24% |
| IWM | 278.44 | -1.64% | 278.02 | 281.12 | 279.34 | **-0.95%** | 1.76% |
| QQQE | 116.58 | -0.95% | 116.90 | 118.76 | 113.58 | **-1.83%** | 1.76% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at +2.68%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **18.7** | 18.7 | +0.00 (+0.0%) | 2026-11-12 16:15:01 ET |
| VIX3M | **20.06** | 20.06 | +0.00 (+0.0%) | 2026-11-12 16:15:01 ET |

Source: Cboe delayed-quote CDN. Pulled 2 times, 5 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **0.9322** → `uncertainty: false` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | size cut only when the index is below its 20-DMA **and** breadth < 40% — breadth is 53.07% |
| `uncertainty` | **false** | VIX/VIX3M = 0.9322 ≤ 1 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max +2.68%, RSP) |
| `index_below_20sma` | **true** | only 2 of 5 index ETFs are above their 20-DMA (40%) |

Payload: `daily-screens/2026-11-12/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Marine Shipping | 1 | 0.0% | +2.68% | +2.68% |
| Oil Refining/Marketing | 5 | 0.0% | +1.83% | +1.64% |
| Integrated Oil | 22 | 0.0% | +1.20% | +1.34% |
| Pharmaceuticals: Generic | 1 | 100.0% | +0.95% | +0.95% |
| Oil & Gas Pipelines | 14 | 35.7% | +0.85% | +0.58% |
| Electronic Components | 4 | 25.0% | +0.78% | -0.20% |
| Railroads | 5 | 80.0% | +0.70% | +0.80% |
| Computer Peripherals | 7 | 14.3% | +0.64% | +0.40% |
| Oil & Gas Production | 5 | 20.0% | +0.57% | +0.67% |
| Gas Distributors | 6 | 50.0% | +0.56% | +0.68% |
| Food Retail | 1 | 100.0% | +0.46% | +0.46% |
| Environmental Services | 5 | 60.0% | +0.39% | +1.32% |
| Electronics Distributors | 2 | 50.0% | +0.39% | +0.39% |
| Chemicals: Agricultural | 2 | 100.0% | +0.38% | +0.38% |
| Services to the Health Industry | 1 | 100.0% | +0.37% | +0.37% |
| Drugstore Chains | 1 | 100.0% | +0.30% | +0.30% |
| Tobacco | 3 | 66.7% | +0.28% | +0.16% |
| Publishing: Books/Magazines | 1 | 0.0% | +0.17% | +0.17% |
| Alternative Power Generation | 4 | 75.0% | +0.16% | +0.03% |
| Data Processing Services | 7 | 71.4% | +0.05% | -0.14% |
| Building Products | 4 | 75.0% | -0.02% | -0.89% |
| Medical Distributors | 3 | 100.0% | -0.05% | -0.14% |
| Agricultural Commodities/Milling | 2 | 0.0% | -0.11% | -0.11% |
| Chemicals: Specialty | 8 | 62.5% | -0.15% | -0.80% |
| Information Technology Services | 17 | 41.2% | -0.18% | -0.28% |
| Household/Personal Care | 7 | 85.7% | -0.24% | -0.10% |
| Property/Casualty Insurance | 15 | 80.0% | -0.26% | -0.33% |
| Managed Health Care | 6 | 66.7% | -0.28% | -0.10% |
| Major Telecommunications | 2 | 100.0% | -0.31% | -0.31% |
| Pulp & Paper | 3 | 66.7% | -0.32% | -0.65% |
| Investment Trusts/Mutual Funds | 2 | 0.0% | -0.35% | -0.35% |
| Trucking | 5 | 60.0% | -0.36% | -0.22% |
| Engineering & Construction | 8 | 75.0% | -0.38% | -0.53% |
| Electric Utilities | 41 | 61.0% | -0.43% | -0.14% |
| Beverages: Alcoholic | 6 | 83.3% | -0.52% | -0.24% |
| Commercial Printing/Forms | 1 | 100.0% | -0.57% | -0.57% |
| Food: Major Diversified | 2 | 50.0% | -0.58% | -0.58% |
| Telecommunications Equipment | 8 | 50.0% | -0.59% | -0.45% |
| Electrical Products | 9 | 22.2% | -0.59% | -0.49% |
| Contract Drilling | 2 | 0.0% | -0.61% | -0.61% |
| Oilfield Services/Equipment | 2 | 0.0% | -0.62% | -0.62% |
| Restaurants | 10 | 90.0% | -0.69% | -0.50% |
| Electronics/Appliance Stores | 2 | 100.0% | -0.70% | -0.70% |
| Chemicals: Major Diversified | 2 | 100.0% | -0.77% | -0.77% |
| Metal Fabrication | 2 | 50.0% | -0.79% | -0.79% |
| Multi-Line Insurance | 25 | 48.0% | -0.80% | -0.81% |
| Pharmaceuticals: Major | 29 | 86.2% | -0.81% | -0.74% |
| Electronic Production Equipment | 5 | 40.0% | -0.84% | -0.76% |
| Internet Software/Services | 20 | 30.0% | -0.87% | -0.97% |
| Other Consumer Services | 5 | 60.0% | -0.91% | -0.57% |
| Regional Banks | 35 | 31.4% | -0.91% | -0.74% |
| Real Estate Investment Trusts | 74 | 48.6% | -0.97% | -0.88% |
| Packaged Software | 57 | 43.9% | -1.01% | -0.30% |
| Major Banks | 88 | 23.9% | -1.02% | -0.94% |
| Specialty Stores | 15 | 86.7% | -1.06% | -0.54% |
| Apparel/Footwear Retail | 4 | 75.0% | -1.07% | -1.10% |
| Semiconductors | 34 | 50.0% | -1.07% | -1.47% |
| Steel | 8 | 37.5% | -1.11% | -0.89% |
| Miscellaneous Commercial Services | 16 | 75.0% | -1.12% | -0.87% |
| Food Distributors | 2 | 50.0% | -1.14% | -1.14% |
| Medical Specialties | 35 | 65.7% | -1.14% | -0.92% |
| Life/Health Insurance | 9 | 44.4% | -1.18% | -1.26% |
| Industrial Machinery | 25 | 64.0% | -1.21% | -1.08% |
| Auto Parts: OEM | 6 | 66.7% | -1.24% | -0.83% |
| Air Freight/Couriers | 9 | 66.7% | -1.27% | -1.14% |
| Food: Specialty/Candy | 7 | 57.1% | -1.27% | -1.13% |
| Insurance Brokers/Services | 6 | 83.3% | -1.30% | -1.36% |
| Financial Publishing/Services | 7 | 85.7% | -1.30% | -1.39% |
| Movies/Entertainment | 3 | 100.0% | -1.30% | -1.19% |
| Trucks/Construction/Farm Machinery | 7 | 71.4% | -1.32% | -1.21% |
| Medical/Nursing Services | 8 | 75.0% | -1.32% | -0.74% |
| Home Improvement Chains | 2 | 100.0% | -1.33% | -1.33% |
| Other Transportation | 3 | 100.0% | -1.33% | -1.12% |
| Aerospace & Defense | 28 | 71.4% | -1.35% | -1.48% |
| Containers/Packaging | 5 | 60.0% | -1.37% | -1.33% |
| Industrial Conglomerates | 1 | 100.0% | -1.40% | -1.40% |
| Investment Banks/Brokers | 25 | 48.0% | -1.41% | -1.04% |
| Wireless Telecommunications | 14 | 64.3% | -1.43% | -0.80% |
| Aluminum | 1 | 100.0% | -1.44% | -1.44% |
| Tools & Hardware | 3 | 100.0% | -1.54% | -1.83% |
| Discount Stores | 3 | 100.0% | -1.54% | -1.43% |
| Hospital/Nursing Management | 3 | 100.0% | -1.55% | -1.49% |
| Food: Meat/Fish/Dairy | 4 | 75.0% | -1.56% | -0.78% |
| Water Utilities | 3 | 66.7% | -1.62% | -1.39% |
| Hotels/Resorts/Cruise lines | 9 | 100.0% | -1.64% | -1.31% |
| Investment Managers | 38 | 57.9% | -1.66% | -1.54% |
| Real Estate Development | 3 | 66.7% | -1.67% | -1.73% |
| Department Stores | 1 | 0.0% | -1.87% | -1.87% |
| Beverages: Non-Alcoholic | 6 | 50.0% | -1.93% | -1.08% |
| Wholesale Distributors | 9 | 55.6% | -1.94% | -0.55% |
| Industrial Specialties | 3 | 100.0% | -1.95% | -2.10% |
| Construction Materials | 6 | 66.7% | -1.96% | -1.76% |
| Finance/Rental/Leasing | 16 | 37.5% | -2.06% | -1.12% |
| Financial Conglomerates | 8 | 37.5% | -2.07% | -1.73% |
| Publishing: Newspapers | 3 | 33.3% | -2.11% | -2.09% |
| Other Metals/Minerals | 7 | 14.3% | -2.13% | -2.55% |
| Cable/Satellite TV | 4 | 50.0% | -2.21% | -2.01% |
| Homebuilding | 6 | 33.3% | -2.27% | -2.03% |
| Internet Retail | 7 | 42.9% | -2.29% | -2.07% |
| Advertising/Marketing Services | 1 | 100.0% | -2.30% | -2.30% |
| Specialty Insurance | 1 | 100.0% | -2.40% | -2.40% |
| Pharmaceuticals: Other | 1 | 0.0% | -2.41% | -2.41% |
| Electronic Equipment/Instruments | 7 | 85.7% | -2.42% | -2.51% |
| Recreational Products | 2 | 100.0% | -2.46% | -2.46% |
| Biotechnology | 18 | 72.2% | -2.48% | -1.48% |
| Motor Vehicles | 9 | 66.7% | -2.54% | -2.86% |
| Broadcasting | 3 | 33.3% | -2.71% | -3.17% |
| Apparel/Footwear | 5 | 20.0% | -2.83% | -2.78% |
| Electronics/Appliances | 1 | 100.0% | -2.99% | -2.99% |
| Home Furnishings | 1 | 0.0% | -2.99% | -2.99% |
| Casinos/Gaming | 2 | 100.0% | -3.18% | -3.18% |
| Specialty Telecommunications | 3 | 33.3% | -3.21% | -3.98% |
| Precious Metals | 13 | 23.1% | -3.91% | -4.17% |
| Airlines | 5 | 100.0% | -4.06% | -3.76% |
| Computer Processing Hardware | 8 | 12.5% | -4.43% | -2.16% |

## Flags

- **The index is the weak leg.** QQQ is -4.24% versus its own 50-DMA while RSP is +2.68%; only IWM is below its 20-DMA by less than a percent. The average large cap is healthier than the cap-weighted index.
- **Breadth and advance/decline disagree in sign.** 53.07% of names are still above their 20-DMA, yet just 242 of 1,106 advanced today. Breadth is a level and A/D is a rate — the level is stale, the rate is today's tape.
- **The volatility pair is one pair and it is settled.** VIX 18.70 / VIX3M 20.06, quote time 2026-11-12 16:15:01 ET, two pulls 5 s apart and identical. No mid-session print is mixed in anywhere in this document.
- **No 1-year breadth percentile is published here.** The trailing session series for this universe is not pulled by this routine, so the level is published without it and the gap is stated rather than filled with a guess.

## Method, source health & caveats

- **This fire was a delayed replay.** It was scheduled for 2026-11-12 18:30 ET and the work completed on 2026-11-13 at ~10:40 ET, resumed in place. Every figure describes the **2026-11-12 settled close** — the anchor was re-verified against shibui's own settled rows for 2026-11-12 (SPY 757.12, RSP 220.72, QQQ 688.17, identical on both feeds) before publication, and the screen session was FORCED to 2026-11-11 with `--t1-date` so the two books keep the same relationship they had on the night.
- **The trigger/context split is the point of this run.** The 4% breakout, EP9M, 10% gap and volume-breakout screens are computed on **2026-11-12's own settled bar**. The multi-session context screens stay on shibui's **2026-11-11** session and say so. Every candidate publishes `data_as_of` and `source`.
- **`rows_kept == rows_passing` on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200). The two largest — `K_stockbee_anticipation` (402) and `G_peoplewish` (351) — were paged to completion, so the book is complete rather than truncated at shibui's 200-row ceiling.
- **The parabolic gates were NOT re-expressed on TradingView's `Perf.W`.** `Perf.W` correlates r=0.997 with a **six**-session move and only r=0.924 with a five-session move, so the published ±25% five-session gates stay on shibui and stay T+1.
- **The prior-nine-session volume baseline is reconstructed exactly**: `average_volume_10d_calc` is the mean of the last ten sessions **including** today, so the prior-nine mean is recovered as `(10 × avg10 − volume_today) / 9` with no second data source.
- **CANSLIM is rebuilt on shibui, not read from TradingView.** TradingView's US growth columns come back NULL, so the growth half comes from shibui's `fundamentals_derived_quarterly`, each symbol's **latest reported quarter** — that table's newest `date` is a ONE-ROW reporting date, so a `MAX(date)` join returns NULL growth for every symbol and the branch returns nothing. The price half (close, change, RSI) comes from the FRESH book, so the CANSLIM screen is on the cron day's own bar.
- **The overlay is a LABEL, not a filter.** It never removes a name from the book; it tells the reader what the growth screen does not ask about. A missing trailing P/E is published as `earnings_data_missing` with `valuation_gate: unknown` — disclosed, never counted as a red flag.
- **No 1-year breadth percentile** is published in `breadth.md` — the trailing session series for the universe is not pulled by this routine. The level is published without it, and the gap is stated rather than filled with a guess.
- **This is a screen, not a trade list.** No catalyst was sourced for any name, the parabolic lists are mechanical outcomes, and the focus list has not been discretionary-reviewed.
