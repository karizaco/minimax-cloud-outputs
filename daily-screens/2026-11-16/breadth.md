---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "2026-11-16 18:30:52 ET"
data_date: "2026-11-16 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-13)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1095 names; totalCount 1095 = rows fetched, no truncation"
vix_quote_time: "2026-11-16 16:15:01 ET (Cboe delayed-quote CDN, 2 pulls 5 s apart — identical)"
vix_pair: "VIX 22.91 / VIX3M 23.02 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-16/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---

# Breadth & Regime — End-of-Day — Monday 16 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-16. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-13) and are not blended into this file.

## TL;DR

- **43.93%** of the 1,095 $10B+ large caps closed above their 20-DMA (49.77% above the 50-DMA, 47.49% above the 200-DMA) — a majority of the large-cap universe sits below its own 20-DMA.
- **Participation was negative across the board: 297 advancing vs 787 declining** (ratio 0.38, net -490), median name -0.77%, and 80 names fell 5% or more.
- **The BROAD divergence (+43.93 pp) is a statement about the INDEX, not about the average stock.** 0 of 5 index ETFs are above their 20-DMA (QQQ -7.67% vs its 50-DMA, SPY -3.13%), so the cap-weighted index is the weak leg while equal-weight RSP holds +1.84% above its 50-DMA.

## Breadth — 2026-11-16 settled session

| Metric | Value |
|---|---|
| Universe | 1095 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **43.93%** (481 / 1095) |
| Above 50-DMA | 49.77% (545 / 1095) |
| Above 200-DMA | 47.49% (520 / 1095) |
| Advance / decline / unchanged | **297 / 787 / 11** — ratio 0.38, net **-490** |
| Median name | -0.77%  ·  mean -1.23% |
| Move distribution | ≥ +5%: 7 · +2..5%: 32 · 0..2%: 269 · −2..0: 480 · −5..−2: 227 · ≤ −5%: 80 |

## Participation — the advance/decline tally

Computed on the **same 1095-name population** as the breadth percentage, from the settled session: **297 advancing, 787 declining, 11 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **-490**, ratio **0.38**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+43.93 pp** |
| band | **BROAD** |
| large-cap % above 20-DMA | 43.93% |
| index ETFs above their 20-DMA | 0% (0 of 5) |

A **BROAD** divergence means the average large cap is materially healthier than the index — participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 739.95 | -1.91% | 757.69 | 763.82 | 732.16 | **-3.13%** | 1.54% |
| QQQ | 661.75 | -2.67% | 692.62 | 716.72 | 682.44 | **-7.67%** | 2.50% |
| RSP | 218.93 | -1.01% | 218.93 | 214.98 | 208.96 | **+1.84%** | 1.24% |
| IWM | 272.94 | -1.66% | 278.46 | 280.30 | 279.48 | **-2.63%** | 1.80% |
| QQQE | 113.42 | -2.09% | 116.62 | 118.51 | 113.68 | **-4.29%** | 1.83% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at +1.84%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **22.91** | 19.3 | +3.61 (+18.7%) | 2026-11-16 16:15:01 ET |
| VIX3M | **23.02** | 20.62 | +2.40 (+11.6%) | 2026-11-16 16:15:01 ET |

Source: Cboe delayed-quote CDN. Pulled 2 times, 5 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **0.9952** → `uncertainty: false` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | size cut only when the index is below its 20-DMA **and** breadth < 40% — breadth is 43.93% |
| `uncertainty` | **false** | VIX/VIX3M = 0.9952 ≤ 1 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max +1.84%, RSP) |
| `index_below_20sma` | **true** | only 0 of 5 index ETFs are above their 20-DMA (0%) |

Payload: `daily-screens/2026-11-16/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Managed Health Care | 6 | 83.3% | +4.12% | +3.18% |
| Food: Meat/Fish/Dairy | 4 | 75.0% | +2.92% | +1.90% |
| Specialty Insurance | 1 | 100.0% | +2.26% | +2.26% |
| Hospital/Nursing Management | 3 | 100.0% | +2.13% | +1.93% |
| Major Telecommunications | 2 | 100.0% | +1.56% | +1.56% |
| Insurance Brokers/Services | 6 | 100.0% | +1.49% | +1.43% |
| Wireless Telecommunications | 14 | 78.6% | +1.49% | +0.27% |
| Real Estate Development | 3 | 100.0% | +1.48% | +0.04% |
| Food: Major Diversified | 2 | 100.0% | +1.26% | +1.26% |
| Restaurants | 10 | 90.0% | +1.24% | +1.27% |
| Environmental Services | 5 | 60.0% | +1.06% | +1.02% |
| Hotels/Resorts/Cruise lines | 9 | 100.0% | +1.06% | +0.46% |
| Services to the Health Industry | 1 | 100.0% | +1.01% | +1.01% |
| Airlines | 5 | 100.0% | +0.84% | +0.41% |
| Household/Personal Care | 7 | 85.7% | +0.75% | +1.32% |
| Food Distributors | 2 | 50.0% | +0.62% | +0.62% |
| Commercial Printing/Forms | 1 | 100.0% | +0.46% | +0.46% |
| Railroads | 5 | 80.0% | +0.36% | +0.42% |
| Food: Specialty/Candy | 7 | 57.1% | +0.36% | +0.36% |
| Medical Distributors | 3 | 100.0% | +0.20% | +0.20% |
| Property/Casualty Insurance | 15 | 80.0% | +0.19% | +0.25% |
| Financial Publishing/Services | 7 | 85.7% | +0.12% | -0.16% |
| Publishing: Books/Magazines | 1 | 0.0% | +0.06% | +0.06% |
| Other Transportation | 3 | 100.0% | +0.05% | +0.43% |
| Beverages: Alcoholic | 6 | 83.3% | +0.04% | +0.52% |
| Advertising/Marketing Services | 1 | 100.0% | +0.02% | +0.02% |
| Data Processing Services | 7 | 57.1% | +0.02% | +0.45% |
| Specialty Stores | 15 | 80.0% | -0.02% | +0.00% |
| Discount Stores | 3 | 100.0% | -0.04% | +0.45% |
| Industrial Specialties | 3 | 100.0% | -0.08% | +0.06% |
| Medical/Nursing Services | 8 | 75.0% | -0.08% | -0.15% |
| Air Freight/Couriers | 9 | 77.8% | -0.09% | +0.16% |
| Multi-Line Insurance | 25 | 48.0% | -0.09% | +0.00% |
| Electric Utilities | 41 | 65.9% | -0.13% | +0.05% |
| Food Retail | 1 | 100.0% | -0.18% | -0.18% |
| Real Estate Investment Trusts | 74 | 52.7% | -0.19% | -0.14% |
| Other Consumer Services | 5 | 40.0% | -0.23% | -0.52% |
| Tobacco | 3 | 66.7% | -0.26% | +0.33% |
| Containers/Packaging | 5 | 20.0% | -0.27% | -0.12% |
| Broadcasting | 3 | 100.0% | -0.29% | -0.59% |
| Homebuilding | 6 | 33.3% | -0.32% | -0.28% |
| Miscellaneous Commercial Services | 16 | 68.8% | -0.33% | -0.72% |
| Publishing: Newspapers | 3 | 33.3% | -0.42% | -1.05% |
| Tools & Hardware | 3 | 100.0% | -0.61% | -0.53% |
| Trucking | 5 | 80.0% | -0.61% | -0.28% |
| Regional Banks | 35 | 22.9% | -0.63% | -0.39% |
| Building Products | 4 | 50.0% | -0.65% | -0.87% |
| Pharmaceuticals: Major | 29 | 79.3% | -0.71% | -0.38% |
| Life/Health Insurance | 9 | 44.4% | -0.76% | -0.84% |
| Home Improvement Chains | 2 | 100.0% | -0.78% | -0.78% |
| Major Banks | 88 | 19.3% | -0.81% | -0.56% |
| Electronics/Appliance Stores | 2 | 100.0% | -0.83% | -0.83% |
| Drugstore Chains | 1 | 0.0% | -0.85% | -0.85% |
| Water Utilities | 3 | 66.7% | -0.86% | +1.13% |
| Investment Trusts/Mutual Funds | 2 | 0.0% | -0.89% | -0.89% |
| Electronics Distributors | 1 | 0.0% | -0.90% | -0.90% |
| Apparel/Footwear | 5 | 0.0% | -1.01% | -0.18% |
| Finance/Rental/Leasing | 16 | 31.2% | -1.07% | -0.60% |
| Industrial Conglomerates | 1 | 100.0% | -1.08% | -1.08% |
| Department Stores | 1 | 0.0% | -1.09% | -1.09% |
| Movies/Entertainment | 3 | 100.0% | -1.09% | -0.43% |
| Medical Specialties | 34 | 55.9% | -1.12% | -0.95% |
| Construction Materials | 6 | 33.3% | -1.13% | -0.88% |
| Beverages: Non-Alcoholic | 6 | 50.0% | -1.15% | -0.94% |
| Metal Fabrication | 2 | 0.0% | -1.20% | -1.20% |
| Recreational Products | 2 | 50.0% | -1.21% | -1.21% |
| Investment Managers | 38 | 42.1% | -1.25% | -1.11% |
| Oil & Gas Pipelines | 14 | 21.4% | -1.32% | -1.28% |
| Gas Distributors | 6 | 33.3% | -1.36% | -1.52% |
| Electronics/Appliances | 1 | 100.0% | -1.37% | -1.37% |
| Cable/Satellite TV | 4 | 50.0% | -1.46% | -0.60% |
| Biotechnology | 16 | 68.8% | -1.47% | -0.83% |
| Motor Vehicles | 9 | 11.1% | -1.49% | -1.55% |
| Pulp & Paper | 3 | 66.7% | -1.50% | -0.62% |
| Home Furnishings | 1 | 0.0% | -1.50% | -1.50% |
| Investment Banks/Brokers | 25 | 32.0% | -1.55% | -0.81% |
| Wholesale Distributors | 9 | 44.4% | -1.71% | -1.28% |
| Alternative Power Generation | 4 | 50.0% | -1.79% | -1.51% |
| Packaged Software | 57 | 35.1% | -1.79% | -1.23% |
| Engineering & Construction | 8 | 50.0% | -1.83% | -2.17% |
| Information Technology Services | 17 | 23.5% | -1.88% | -1.22% |
| Casinos/Gaming | 2 | 50.0% | -1.93% | -1.93% |
| Auto Parts: OEM | 5 | 60.0% | -1.93% | -1.70% |
| Internet Software/Services | 20 | 25.0% | -1.94% | -2.11% |
| Telecommunications Equipment | 8 | 37.5% | -2.03% | -1.08% |
| Chemicals: Major Diversified | 2 | 100.0% | -2.14% | -2.14% |
| Aerospace & Defense | 28 | 39.3% | -2.18% | -1.93% |
| Apparel/Footwear Retail | 4 | 25.0% | -2.24% | -2.81% |
| Oil Refining/Marketing | 5 | 0.0% | -2.42% | -2.66% |
| Oil & Gas Production | 5 | 0.0% | -2.64% | -2.66% |
| Industrial Machinery | 25 | 32.0% | -2.65% | -2.18% |
| Aluminum | 1 | 0.0% | -2.72% | -2.72% |
| Agricultural Commodities/Milling | 2 | 0.0% | -2.86% | -2.86% |
| Financial Conglomerates | 8 | 12.5% | -2.91% | -1.86% |
| Trucks/Construction/Farm Machinery | 5 | 40.0% | -2.96% | -2.90% |
| Steel | 8 | 12.5% | -3.01% | -3.02% |
| Internet Retail | 7 | 28.6% | -3.02% | -3.34% |
| Integrated Oil | 22 | 0.0% | -3.03% | -2.86% |
| Contract Drilling | 2 | 0.0% | -3.06% | -3.06% |
| Chemicals: Specialty | 8 | 37.5% | -3.13% | -3.78% |
| Pharmaceuticals: Other | 1 | 0.0% | -3.15% | -3.15% |
| Marine Shipping | 1 | 0.0% | -3.26% | -3.26% |
| Electronic Equipment/Instruments | 5 | 20.0% | -3.39% | -3.44% |
| Precious Metals | 13 | 7.7% | -3.51% | -3.25% |
| Chemicals: Agricultural | 2 | 0.0% | -3.71% | -3.71% |
| Oilfield Services/Equipment | 2 | 0.0% | -3.74% | -3.74% |
| Electronic Components | 4 | 0.0% | -3.97% | -4.08% |
| Pharmaceuticals: Generic | 1 | 100.0% | -4.34% | -4.34% |
| Electrical Products | 9 | 11.1% | -4.43% | -4.36% |
| Computer Processing Hardware | 8 | 12.5% | -4.56% | -4.92% |
| Specialty Telecommunications | 3 | 33.3% | -4.71% | -1.26% |
| Computer Peripherals | 7 | 14.3% | -4.78% | -4.98% |
| Electronic Production Equipment | 4 | 0.0% | -5.40% | -6.85% |
| Other Metals/Minerals | 7 | 0.0% | -5.44% | -5.36% |
| Semiconductors | 33 | 15.2% | -5.45% | -5.22% |

## Flags

- **RSP** — close 218.93 against a 20-DMA of 218.9315: it is **0.0007% below** its own 20-DMA, so the "0 of 5 index ETFs above their 20-DMA" count — and with it the +43.93 pp divergence — rests on one tick. Flagging rather than rounding it away.
- **QQQE** — close 113.42 is below its 200-DMA (113.68) while SPY sits +1.06% above its own; the five ETFs are not at the same point in their cycles, so 0/5 is not a uniform read.
- **QQQ** — its 20-DMA (692.62) sits 3.36% BELOW its 50-DMA (716.72): the QQQ's own trend structure is down-sloping, not merely below-average.
- **CBRS** — close 100.99 against a 50-DMA of 148.84: the MA-based extension metrics for a name this far off its own 50-day average are distorted by the post-listing decline (perf YTD -71%). Its ATR% of 11.36 is the real signal.
- **MOD** — every metric on its row belongs to the 2026-11-13 session (`source: t1`): the 40.4% five-session move, the parabolic-short membership and the trailing P/E of 55.5 all describe the prior session, not today's close.
- **CGON** — price/sales 1,069x, no trailing P/E, and a -2.87% FCF yield: the growth screen says nothing about what the price already assumes.

## Method, source health & caveats

- **Dual book, never blended.** TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on the cron day's own settled bar (2026-11-16); multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session (2026-11-13). Every row carries `data_as_of` + `source` (`fresh` / `t1` / `fresh+t1`).
- **Coverage assertion: 9/9 branches complete** — `rows_kept == rows_passing` on every branch, and no branch count lands on a cap (30 / 50 / 60 / 200).
- **Breadth universe:** NYSE/NASDAQ/AMEX, type in {stock, dr}, `market_cap_basic` > $10B, TradingView scanner in USD — **1,095 names**, and `totalCount` 1,095 equals the rows fetched, so the scan is not truncated. The advance/decline tally uses the same population (297 + 787 + 11 = 1,095).
- **Source of record for the settled layer:** the TradingView scanner's post-close `close`, which is the official 16:00 ET print. Nasdaq's `primaryData` is the after-hours last trade and is deliberately not used in an end-of-day artifact.
- **One volatility pair** (VIX 22.91 / VIX3M 23.02, Cboe delayed-quote CDN, quoted 2026-11-16 16:15:01 ET, pulled twice 5 s apart and identical — `vix_stable: true`) is used everywhere in both artifacts; no mid-session print is mixed with the settle. Ratio 0.9952 → `uncertainty: false`; `atr_extensions` carries all five index ETFs, so `late_cycle` was genuinely computed (`false`).
- **Caveat on the divergence.** `breadth_divergence` +43.93 pp reads BROAD because the five index ETFs are 0/5 above their 20-DMA — RSP sits 0.0007% below its own 20-DMA (218.93 close vs a 218.9315 average), so that count is one tick deep. The band identifies the INDEX as the weak leg; it is not a statement that the average stock is healthy.
- **The overlay is a LABEL, not a filter.** A missing trailing P/E is published as `earnings_data_missing` with `valuation_gate: unknown` — never as a red flag and never as a pass. Nothing is dropped from the book for tripping a rule.
- **Settled vs live:** this directory holds three reads and they are not blended — the end-of-day breadth (`breadth.md`, 2026-11-16 settle), the intraday counterpart (`breadth-snapshot.md`, cron #10, 14:00 ET) and the T+1 screen metrics in `daily-sweep.md` (shibui 2026-11-13). No degraded probe applies.
