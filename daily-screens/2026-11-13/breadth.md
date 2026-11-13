---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "2026-11-13 18:31 ET"
data_date: "2026-11-13 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-12)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1100 names; totalCount 1100 = rows fetched, no truncation"
vix_quote_time: "2026-11-13 16:15:01 ET (Cboe delayed-quote CDN, 2 pulls 5 s apart — identical)"
vix_pair: "VIX 19.3 / VIX3M 20.62 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-13/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---

# Breadth & Regime — End-of-Day — Friday 13 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-13. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-12) and are not blended into this file.

## TL;DR

- **52.82% of the $10B+ universe closed above its 20-DMA**, advances beat declines **579 / 510** (net +69) — but only **1 of 5** index ETFs is above its 20-DMA and QQQ closed **-5.29%** below its 50-DMA. Breadth divergence **+32.82pp (BROAD)**: the average large cap is healthier than the index, so this is not a megacap-led advance.
- **Regime: `size_cut_pct` 0, `uncertainty` false, `late_cycle` false.** VIX 19.30 / VIX3M 20.62 = 0.936 (term structure still inverted), and the widest index extension is RSP at **+2.87%** above its 50-DMA — well inside the 6% `late_cycle` trigger. `index_below_20sma` is **true**: the index's own posture is the weak leg, while breadth itself sits mid-range.
- **The damage is concentrated in semiconductors**: Semiconductors 29.4% above their 20-DMA (avg -3.19%), Electronic Production Equipment -4.48%, Computer Peripherals -2.99%. VIX +3.2% on the day; the largest decliners (NBIS -9.92%, AMD -8.75%, KEP -8.72%) are AI/data-centre and semiconductor names.

## Breadth — 2026-11-13 settled session

| Metric | Value |
|---|---|
| Universe | 1100 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **52.82%** (581 / 1100) |
| Above 50-DMA | 53.64% (590 / 1100) |
| Above 200-DMA | 49.82% (548 / 1100) |
| Advance / decline / unchanged | **579 / 510 / 11** — ratio 1.14, net **+69** |
| Median name | +0.09%  ·  mean -0.07% |
| Move distribution | ≥ +5%: 5 · +2..5%: 71 · 0..2%: 514 · −2..0: 401 · −5..−2: 89 · ≤ −5%: 20 |

## Participation — the advance/decline tally

Computed on the **same 1100-name population** as the breadth percentage, from the settled session: **579 advancing, 510 declining, 11 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **+69**, ratio **1.14**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+32.82 pp** |
| band | **BROAD** |
| large-cap % above 20-DMA | 52.82% |
| index ETFs above their 20-DMA | 20% (1 of 5) |

A **BROAD** divergence means the average large cap is materially healthier than the index — participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 754.37 | -0.36% | 759.02 | 764.43 | 731.92 | **-1.32%** | 1.46% |
| QQQ | 679.89 | -1.20% | 695.45 | 717.87 | 682.24 | **-5.29%** | 2.40% |
| RSP | 221.16 | +0.20% | 218.66 | 214.98 | 208.86 | **+2.87%** | 1.22% |
| IWM | 277.54 | -0.32% | 278.38 | 280.76 | 279.41 | **-1.15%** | 1.76% |
| QQQE | 115.84 | -0.63% | 116.84 | 118.65 | 113.63 | **-2.37%** | 1.76% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at +2.87%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **19.3** | 18.7 | +0.60 (+3.2%) | 2026-11-13 16:15:01 ET |
| VIX3M | **20.62** | 20.06 | +0.56 (+2.8%) | 2026-11-13 16:15:01 ET |

Source: Cboe delayed-quote CDN. Pulled 2 times, 5 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **0.9360** → `uncertainty: false` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | size cut only when the index is below its 20-DMA **and** breadth < 40% — breadth is 52.82% |
| `uncertainty` | **false** | VIX/VIX3M = 0.9360 ≤ 1 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max +2.87%, RSP) |
| `index_below_20sma` | **true** | only 1 of 5 index ETFs are above their 20-DMA (20%) |

Payload: `daily-screens/2026-11-13/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Investment Trusts/Mutual Funds | 2 | 0.0% | +3.69% | +3.69% |
| Broadcasting | 3 | 100.0% | +2.85% | +4.09% |
| Electronics/Appliances | 1 | 100.0% | +2.84% | +2.84% |
| Oilfield Services/Equipment | 2 | 0.0% | +2.59% | +2.59% |
| Food: Major Diversified | 2 | 100.0% | +2.48% | +2.48% |
| Trucking | 5 | 80.0% | +2.35% | +2.24% |
| Publishing: Newspapers | 3 | 33.3% | +2.33% | +2.45% |
| Agricultural Commodities/Milling | 2 | 50.0% | +2.19% | +2.19% |
| Medical Distributors | 3 | 100.0% | +2.07% | +2.39% |
| Beverages: Non-Alcoholic | 6 | 83.3% | +2.04% | +1.91% |
| Commercial Printing/Forms | 1 | 100.0% | +1.99% | +1.99% |
| Pharmaceuticals: Generic | 1 | 100.0% | +1.95% | +1.95% |
| Department Stores | 1 | 0.0% | +1.86% | +1.86% |
| Insurance Brokers/Services | 6 | 100.0% | +1.68% | +1.78% |
| Beverages: Alcoholic | 6 | 83.3% | +1.46% | +1.37% |
| Water Utilities | 3 | 66.7% | +1.44% | +1.37% |
| Food Retail | 1 | 100.0% | +1.42% | +1.42% |
| Contract Drilling | 2 | 50.0% | +1.34% | +1.34% |
| Advertising/Marketing Services | 1 | 100.0% | +1.31% | +1.31% |
| Household/Personal Care | 7 | 100.0% | +1.24% | +1.14% |
| Tobacco | 3 | 66.7% | +1.16% | +1.17% |
| Food: Specialty/Candy | 7 | 57.1% | +1.16% | +0.97% |
| Building Products | 4 | 50.0% | +1.12% | +0.57% |
| Cable/Satellite TV | 4 | 50.0% | +1.00% | +0.30% |
| Apparel/Footwear | 5 | 20.0% | +1.00% | +1.14% |
| Integrated Oil | 22 | 4.5% | +0.98% | +0.88% |
| Major Telecommunications | 2 | 100.0% | +0.98% | +0.98% |
| Food: Meat/Fish/Dairy | 4 | 75.0% | +0.95% | +1.18% |
| Publishing: Books/Magazines | 1 | 0.0% | +0.93% | +0.93% |
| Casinos/Gaming | 2 | 50.0% | +0.84% | +0.84% |
| Oil Refining/Marketing | 5 | 0.0% | +0.80% | +0.76% |
| Electronics/Appliance Stores | 2 | 100.0% | +0.77% | +0.77% |
| Pharmaceuticals: Major | 29 | 86.2% | +0.75% | +0.49% |
| Specialty Stores | 15 | 80.0% | +0.73% | +0.69% |
| Specialty Insurance | 1 | 100.0% | +0.72% | +0.72% |
| Miscellaneous Commercial Services | 16 | 75.0% | +0.70% | +0.69% |
| Hotels/Resorts/Cruise lines | 9 | 100.0% | +0.66% | +0.40% |
| Real Estate Development | 3 | 100.0% | +0.66% | +0.44% |
| Food Distributors | 2 | 50.0% | +0.66% | +0.66% |
| Restaurants | 10 | 80.0% | +0.65% | +0.21% |
| Oil & Gas Production | 5 | 20.0% | +0.63% | +0.72% |
| Air Freight/Couriers | 9 | 77.8% | +0.58% | +0.67% |
| Gas Distributors | 6 | 50.0% | +0.58% | +0.60% |
| Medical Specialties | 34 | 64.7% | +0.58% | +0.51% |
| Managed Health Care | 6 | 66.7% | +0.57% | +0.41% |
| Financial Publishing/Services | 7 | 85.7% | +0.57% | +0.39% |
| Finance/Rental/Leasing | 16 | 43.8% | +0.54% | +0.81% |
| Internet Retail | 7 | 42.9% | +0.50% | +0.65% |
| Medical/Nursing Services | 8 | 75.0% | +0.48% | +0.29% |
| Tools & Hardware | 3 | 100.0% | +0.47% | +0.22% |
| Other Transportation | 3 | 100.0% | +0.46% | +0.82% |
| Marine Shipping | 1 | 0.0% | +0.45% | +0.45% |
| Internet Software/Services | 20 | 35.0% | +0.36% | +0.10% |
| Regional Banks | 35 | 45.7% | +0.36% | +0.05% |
| Property/Casualty Insurance | 15 | 80.0% | +0.29% | +0.42% |
| Home Furnishings | 1 | 0.0% | +0.23% | +0.23% |
| Homebuilding | 6 | 33.3% | +0.23% | +0.06% |
| Oil & Gas Pipelines | 14 | 35.7% | +0.20% | -0.00% |
| Other Consumer Services | 5 | 60.0% | +0.17% | +0.01% |
| Movies/Entertainment | 3 | 100.0% | +0.13% | +0.63% |
| Home Improvement Chains | 2 | 100.0% | +0.12% | +0.12% |
| Industrial Specialties | 3 | 100.0% | +0.11% | +0.17% |
| Pulp & Paper | 3 | 66.7% | +0.09% | +0.57% |
| Chemicals: Agricultural | 2 | 100.0% | +0.08% | +0.08% |
| Data Processing Services | 7 | 71.4% | +0.06% | +0.11% |
| Wireless Telecommunications | 14 | 64.3% | +0.00% | -0.08% |
| Containers/Packaging | 5 | 60.0% | +0.00% | +0.18% |
| Multi-Line Insurance | 25 | 48.0% | -0.00% | +0.14% |
| Packaged Software | 57 | 35.1% | -0.00% | +0.12% |
| Investment Managers | 38 | 57.9% | -0.01% | +0.27% |
| Services to the Health Industry | 1 | 100.0% | -0.02% | -0.02% |
| Environmental Services | 5 | 60.0% | -0.03% | -0.01% |
| Electric Utilities | 41 | 68.3% | -0.05% | +0.22% |
| Construction Materials | 6 | 50.0% | -0.05% | -0.20% |
| Major Banks | 88 | 28.4% | -0.05% | -0.09% |
| Hospital/Nursing Management | 3 | 100.0% | -0.16% | -0.29% |
| Life/Health Insurance | 9 | 44.4% | -0.17% | +0.32% |
| Real Estate Investment Trusts | 74 | 52.7% | -0.22% | -0.20% |
| Aerospace & Defense | 28 | 67.9% | -0.22% | -0.48% |
| Investment Banks/Brokers | 24 | 50.0% | -0.28% | -0.01% |
| Chemicals: Specialty | 8 | 62.5% | -0.29% | -0.11% |
| Alternative Power Generation | 4 | 100.0% | -0.31% | +0.34% |
| Metal Fabrication | 2 | 50.0% | -0.32% | -0.32% |
| Engineering & Construction | 7 | 71.4% | -0.36% | -0.51% |
| Motor Vehicles | 9 | 55.6% | -0.37% | -0.29% |
| Precious Metals | 13 | 23.1% | -0.39% | -0.29% |
| Auto Parts: OEM | 6 | 66.7% | -0.40% | -0.52% |
| Drugstore Chains | 1 | 0.0% | -0.49% | -0.49% |
| Information Technology Services | 17 | 35.3% | -0.54% | -0.26% |
| Trucks/Construction/Farm Machinery | 7 | 71.4% | -0.54% | -0.77% |
| Chemicals: Major Diversified | 2 | 100.0% | -0.59% | -0.59% |
| Airlines | 5 | 100.0% | -0.64% | -0.35% |
| Wholesale Distributors | 9 | 55.6% | -0.72% | -0.74% |
| Railroads | 5 | 80.0% | -0.76% | -0.58% |
| Recreational Products | 2 | 50.0% | -0.80% | -0.80% |
| Industrial Machinery | 25 | 64.0% | -0.83% | -0.44% |
| Discount Stores | 3 | 100.0% | -0.93% | -0.35% |
| Biotechnology | 18 | 66.7% | -0.94% | -0.38% |
| Electronic Equipment/Instruments | 6 | 50.0% | -1.23% | -1.24% |
| Industrial Conglomerates | 1 | 100.0% | -1.39% | -1.39% |
| Specialty Telecommunications | 3 | 33.3% | -1.40% | -0.59% |
| Financial Conglomerates | 8 | 25.0% | -1.48% | -1.35% |
| Steel | 8 | 25.0% | -1.52% | -1.37% |
| Electrical Products | 9 | 22.2% | -1.73% | -1.69% |
| Aluminum | 1 | 0.0% | -1.76% | -1.76% |
| Apparel/Footwear Retail | 4 | 25.0% | -1.82% | -1.76% |
| Electronics Distributors | 1 | 0.0% | -2.03% | -2.03% |
| Telecommunications Equipment | 8 | 37.5% | -2.04% | -1.53% |
| Other Metals/Minerals | 7 | 14.3% | -2.05% | -2.00% |
| Pharmaceuticals: Other | 1 | 0.0% | -2.30% | -2.30% |
| Computer Processing Hardware | 8 | 12.5% | -2.50% | -2.85% |
| Computer Peripherals | 7 | 28.6% | -2.99% | -3.09% |
| Electronic Components | 4 | 0.0% | -3.09% | -3.14% |
| Semiconductors | 34 | 29.4% | -3.19% | -2.73% |
| Electronic Production Equipment | 4 | 0.0% | -4.48% | -4.47% |

## Flags

- **`index_below_20sma: true`** — only 1 of 5 index ETFs is above its 20-DMA: QQQ **-5.29%** vs its 50-DMA, QQQE -2.37%, SPY -1.32%, IWM -1.15%; RSP is the only one positive (+2.87%). `size_cut_pct` stays **0** because breadth is 52.82%, but the index leg is the weak one.
- **Breadth divergence +32.82pp (BROAD)** — participation is broader than the index. This is the opposite of a megacap-led advance.
- **52.82% is a coin flip, not a thrust** — net +69 advances on 1,100 names, median name **+0.09%** but mean **-0.07%**: the average name fell while the median rose, so the day's gains sat in a minority of names. 20 names fell 5%+, 5 rose 5%+.
- **Semis are where the damage is** — Semiconductors 29.4% above their 20-DMA (avg -3.19%), Electronic Production Equipment -4.48%, Electronic Components -3.09%, Computer Peripherals -2.99%. The broadest groups were fine: Pharmaceuticals: Major 86.2%, Property/Casualty 80.0%, Specialty Stores 80.0%.
- **VIX +3.2% to 19.30, VIX/VIX3M 0.936** — the term structure is still inverted, so `uncertainty` is **false**; the level, not the shape, is what moved.
- **The quote is a 16:15:01 ET delayed print** from the Cboe CDN (two pulls 5 s apart, identical), not the 16:00 close — the volatility level carries a ~15-minute stamp.

## Method, source health & caveats

**Sources and what each one owns.** TradingView's scanner is the source of record for the cron day's settled bar (`close` = the official 16:00 ET print) and for the breadth universe; shibui-finance, reached over the MCP-over-HTTP bridge, owns every multi-session context screen; the bridge's `market-recap get_quotes` owns the official close printed on each book row; the Cboe delayed-quote CDN owns the single VIX/VIX3M pair used everywhere in this file.

**The dual book, and which session each row describes.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-13's own settled bar** and are the primary book (232 names). The CONTEXT screens (5-day gainers/losers, 14-day velocity, the anticipation coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-12**, and are labelled T+1 (1,147 names). Every row carries `data_as_of` and `source` (`fresh` 41 · `t1` 956 · `fresh+t1` 191); the two are never blended.

**The coverage assertion.** Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. `rows_kept == rows_passing` on **9 of 9** branches, and no branch count lands on a cap (30/50/60/200) — the truncation fingerprint.

**What the labels mean.** `EXTENDED` is a label, never a filter: ATR > 5.0%, RSI > 75, more than 15% above the 20-DMA, or 3+ consecutive up sessions. Tier-A is published twice (fresh and extended) and nothing is dropped for tripping a rule. The valuation/quality overlay is also a label: 557 names carry at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags), 321 pass, and **96 are `unknown`** — no red flag but no reported trailing earnings either, which is disclosed, never counted as a flag.

**Caveats.** The context screens are one session stale (shibui is T+1) — the multi-session constructs are only mildly affected, but any single-session metric drawn from them is not today's. The breadth universe (TradingView, `market_cap_basic` > $10B, 1,100 names) is **one** population; the skill's shibui T+1 breadth SQL (a different market-cap source, so a different name set) was fetched as the cross-check but its numbers are not rendered into this artifact — only the settled read is published here. The VIX quote carries a ~15-minute delayed stamp (16:15:01 ET). The path of intraday prints is not reconstructed here, so no points between the open and the close are published.
