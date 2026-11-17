---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "18:30 ET (2026-11-17)"
data_date: "2026-11-17 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-16)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1086 names; totalCount 1086 = rows fetched, no truncation"
vix_quote_time: "2026-11-17 16:15:01 ET (Cboe delayed-quote CDN, 2 pulls 5 s apart — identical)"
vix_pair: "VIX 25.46 / VIX3M 24.98 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-17/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
---

# Breadth & Regime — End-of-Day — Tuesday 17 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-17. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-16) and are not blended into this file.

## TL;DR

- **Breadth and the tape agree for once: this was a broad, index-level risk-off session.** Only **34.16%** of the 1,086 large caps closed above their 20-DMA, **239 advanced against 837 declined** (net -598, ratio 0.29, median name -1.02%), and **none** of the five index ETFs (SPY, QQQ, RSP, IWM, QQQE) is above its own 20-DMA. VIX closed **25.46, +11.13%**, with VIX3M 24.98 — the ratio 1.0192 puts the `uncertainty` flag on.
- **The size cut is ON.** `size_cut_pct: 50` fires because both of its conditions hold — the index is below its 20-DMA **and** breadth (34.16%) is under the 40% trigger. The auto-generated regime line in `daily-sweep.md` says breadth is "far above the 40% trigger"; that sentence is wrong and is corrected in the flags block.
- **Positioning is not stretched, it is broken.** `late_cycle` is **false** and genuinely so: the extreme index extension is RSP at **+0.37%** above its 50-DMA, and SPY (-4.02%) and QQQ (-8.18%) are *below* theirs. This is a de-rating, not a blow-off — nothing to take profits from, but also no index-level support.

## Breadth — 2026-11-17 settled session

| Metric | Value |
|---|---|
| Universe | 1086 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **34.16%** (371 / 1086) |
| Above 50-DMA | 44.38% (482 / 1086) |
| Above 200-DMA | 44.29% (481 / 1086) |
| Advance / decline / unchanged | **239 / 837 / 9** — ratio 0.29, net **-598** |
| Median name | -1.02%  ·  mean -1.12% |
| Move distribution | ≥ +5%: 3 · +2..5%: 30 · 0..2%: 215 · −2..0: 577 · −5..−2: 226 · ≤ −5%: 34 |

## Participation — the advance/decline tally

Computed on the **same 1086-name population** as the breadth percentage, from the settled session: **239 advancing, 837 declining, 9 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **-598**, ratio **0.29**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+34.16 pp** |
| band | **BROAD** |
| large-cap % above 20-DMA | 34.16% |
| index ETFs above their 20-DMA | 0% (0 of 5) |

A **BROAD** divergence means the average large cap is materially healthier than the index — participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 732.44 | -1.01% | 755.86 | 763.15 | 732.34 | **-4.02%** | 1.57% |
| QQQ | 656.95 | -0.73% | 689.58 | 715.49 | 682.59 | **-8.18%** | 2.52% |
| RSP | 215.76 | -1.45% | 218.93 | 214.96 | 209.04 | **+0.37%** | 1.29% |
| IWM | 269.05 | -1.43% | 278.12 | 279.79 | 279.51 | **-3.84%** | 1.84% |
| QQQE | 111.98 | -1.27% | 116.29 | 118.35 | 113.72 | **-5.38%** | 1.87% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at +0.37%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **25.46** | 22.91 | +2.55 (+11.1%) | 2026-11-17 16:15:01 ET |
| VIX3M | **24.98** | 23.02 | +1.96 (+8.5%) | 2026-11-17 16:15:01 ET |

Source: Cboe delayed-quote CDN. Pulled 2 times, 5 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **1.0192** → `uncertainty: true` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **50** | size cut only when the index is below its 20-DMA **and** breadth < 40% — breadth is 34.16% |
| `uncertainty` | **true** | VIX/VIX3M = 1.0192 ≤ 1 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max +0.37%, RSP) |
| `index_below_20sma` | **true** | only 0 of 5 index ETFs are above their 20-DMA (0%) |

Payload: `daily-screens/2026-11-17/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Engineering & Construction | 8 | 50.0% | +1.73% | +0.17% |
| Precious Metals | 13 | 15.4% | +0.92% | +0.72% |
| Recreational Products | 2 | 50.0% | +0.86% | +0.86% |
| Electronic Components | 4 | 0.0% | +0.59% | +0.51% |
| Electrical Products | 9 | 0.0% | +0.40% | +0.09% |
| Food Retail | 1 | 100.0% | +0.30% | +0.30% |
| Semiconductors | 33 | 12.1% | +0.27% | +0.26% |
| Building Products | 4 | 50.0% | +0.24% | -0.36% |
| Wireless Telecommunications | 14 | 78.6% | +0.13% | -0.19% |
| Pharmaceuticals: Generic | 1 | 100.0% | +0.12% | +0.12% |
| Chemicals: Agricultural | 2 | 0.0% | -0.01% | -0.01% |
| Commercial Printing/Forms | 1 | 100.0% | -0.06% | -0.06% |
| Restaurants | 10 | 90.0% | -0.08% | -0.22% |
| Alternative Power Generation | 4 | 50.0% | -0.08% | -0.29% |
| Oil & Gas Pipelines | 14 | 21.4% | -0.16% | -0.21% |
| Auto Parts: OEM | 5 | 40.0% | -0.17% | -0.49% |
| Integrated Oil | 22 | 0.0% | -0.20% | -0.28% |
| Specialty Telecommunications | 3 | 66.7% | -0.21% | -0.31% |
| Aerospace & Defense | 28 | 39.3% | -0.25% | -0.31% |
| Marine Shipping | 1 | 0.0% | -0.26% | -0.26% |
| Industrial Conglomerates | 1 | 100.0% | -0.44% | -0.44% |
| Telecommunications Equipment | 8 | 37.5% | -0.45% | -1.07% |
| Advertising/Marketing Services | 1 | 100.0% | -0.45% | -0.45% |
| Major Banks | 86 | 12.8% | -0.48% | -0.12% |
| Cable/Satellite TV | 4 | 50.0% | -0.50% | -0.73% |
| Life/Health Insurance | 9 | 22.2% | -0.55% | -0.28% |
| Water Utilities | 3 | 66.7% | -0.58% | -1.97% |
| Computer Peripherals | 7 | 14.3% | -0.59% | -0.32% |
| Medical Specialties | 34 | 50.0% | -0.60% | -0.69% |
| Electronic Production Equipment | 4 | 0.0% | -0.64% | -0.63% |
| Multi-Line Insurance | 25 | 36.0% | -0.65% | -0.67% |
| Major Telecommunications | 2 | 100.0% | -0.67% | -0.67% |
| Trucks/Construction/Farm Machinery | 5 | 20.0% | -0.68% | -0.73% |
| Food Distributors | 2 | 50.0% | -0.69% | -0.69% |
| Pharmaceuticals: Major | 29 | 69.0% | -0.70% | -0.75% |
| Regional Banks | 35 | 22.9% | -0.71% | -0.43% |
| Food: Major Diversified | 2 | 100.0% | -0.71% | -0.71% |
| Publishing: Newspapers | 3 | 33.3% | -0.72% | -1.09% |
| Specialty Stores | 15 | 66.7% | -0.74% | -0.40% |
| Steel | 8 | 12.5% | -0.75% | -0.56% |
| Chemicals: Major Diversified | 2 | 100.0% | -0.79% | -0.79% |
| Biotechnology | 16 | 43.8% | -0.80% | -0.51% |
| Air Freight/Couriers | 9 | 77.8% | -0.81% | -0.93% |
| Industrial Machinery | 25 | 28.0% | -0.81% | -0.68% |
| Electronics Distributors | 1 | 0.0% | -0.89% | -0.89% |
| Other Metals/Minerals | 7 | 0.0% | -0.91% | -0.72% |
| Department Stores | 1 | 0.0% | -0.92% | -0.92% |
| Food: Meat/Fish/Dairy | 4 | 50.0% | -0.96% | -0.95% |
| Gas Distributors | 6 | 0.0% | -0.96% | -0.78% |
| Chemicals: Specialty | 8 | 12.5% | -0.99% | -1.59% |
| Investment Managers | 38 | 23.7% | -1.02% | -1.09% |
| Property/Casualty Insurance | 15 | 66.7% | -1.05% | -1.13% |
| Motor Vehicles | 9 | 11.1% | -1.07% | -1.40% |
| Metal Fabrication | 2 | 0.0% | -1.07% | -1.07% |
| Hotels/Resorts/Cruise lines | 9 | 77.8% | -1.11% | -1.17% |
| Movies/Entertainment | 3 | 66.7% | -1.16% | -1.23% |
| Oil & Gas Production | 5 | 0.0% | -1.17% | -0.74% |
| Beverages: Non-Alcoholic | 6 | 50.0% | -1.17% | -0.67% |
| Industrial Specialties | 3 | 66.7% | -1.19% | -0.94% |
| Real Estate Investment Trusts | 73 | 30.1% | -1.20% | -0.98% |
| Internet Software/Services | 20 | 25.0% | -1.20% | -1.45% |
| Other Transportation | 3 | 66.7% | -1.23% | -1.45% |
| Oil Refining/Marketing | 5 | 0.0% | -1.27% | -1.42% |
| Financial Conglomerates | 7 | 14.3% | -1.35% | -0.42% |
| Beverages: Alcoholic | 6 | 83.3% | -1.39% | -1.56% |
| Investment Trusts/Mutual Funds | 2 | 0.0% | -1.41% | -1.41% |
| Electronics/Appliances | 1 | 100.0% | -1.42% | -1.42% |
| Broadcasting | 3 | 100.0% | -1.46% | -1.71% |
| Medical Distributors | 3 | 100.0% | -1.54% | -1.62% |
| Pulp & Paper | 3 | 33.3% | -1.56% | -1.11% |
| Other Consumer Services | 4 | 50.0% | -1.57% | -1.73% |
| Electric Utilities | 42 | 52.4% | -1.57% | -1.38% |
| Medical/Nursing Services | 8 | 62.5% | -1.58% | -1.15% |
| Contract Drilling | 2 | 0.0% | -1.63% | -1.63% |
| Apparel/Footwear Retail | 4 | 25.0% | -1.63% | -1.04% |
| Real Estate Development | 3 | 66.7% | -1.65% | -1.85% |
| Miscellaneous Commercial Services | 16 | 50.0% | -1.67% | -1.82% |
| Specialty Insurance | 1 | 100.0% | -1.69% | -1.69% |
| Oilfield Services/Equipment | 2 | 0.0% | -1.71% | -1.71% |
| Discount Stores | 3 | 33.3% | -1.71% | -1.95% |
| Construction Materials | 6 | 0.0% | -1.73% | -1.81% |
| Insurance Brokers/Services | 6 | 100.0% | -1.82% | -1.76% |
| Railroads | 5 | 40.0% | -1.85% | -1.71% |
| Containers/Packaging | 5 | 20.0% | -1.86% | -1.15% |
| Trucking | 5 | 40.0% | -1.87% | -1.45% |
| Homebuilding | 6 | 0.0% | -1.91% | -1.92% |
| Investment Banks/Brokers | 23 | 26.1% | -1.97% | -1.57% |
| Wholesale Distributors | 9 | 33.3% | -2.01% | -1.38% |
| Finance/Rental/Leasing | 16 | 18.8% | -2.06% | -1.73% |
| Publishing: Books/Magazines | 1 | 0.0% | -2.07% | -2.07% |
| Airlines | 5 | 80.0% | -2.13% | -1.83% |
| Computer Processing Hardware | 8 | 12.5% | -2.18% | -1.90% |
| Home Improvement Chains | 2 | 100.0% | -2.22% | -2.22% |
| Services to the Health Industry | 1 | 100.0% | -2.23% | -2.23% |
| Household/Personal Care | 7 | 57.1% | -2.30% | -2.25% |
| Tools & Hardware | 3 | 66.7% | -2.33% | -2.20% |
| Environmental Services | 5 | 40.0% | -2.39% | -1.03% |
| Food: Specialty/Candy | 7 | 57.1% | -2.43% | -1.55% |
| Tobacco | 3 | 33.3% | -2.47% | -1.83% |
| Pharmaceuticals: Other | 1 | 0.0% | -2.50% | -2.50% |
| Information Technology Services | 17 | 17.6% | -2.51% | -2.84% |
| Agricultural Commodities/Milling | 2 | 0.0% | -2.54% | -2.54% |
| Hospital/Nursing Management | 3 | 100.0% | -2.75% | -2.94% |
| Home Furnishings | 1 | 0.0% | -2.84% | -2.84% |
| Data Processing Services | 7 | 42.9% | -2.85% | -3.50% |
| Electronics/Appliance Stores | 2 | 50.0% | -2.86% | -2.86% |
| Casinos/Gaming | 2 | 50.0% | -2.89% | -2.89% |
| Packaged Software | 55 | 23.6% | -2.99% | -2.93% |
| Internet Retail | 7 | 14.3% | -3.02% | -2.44% |
| Apparel/Footwear | 5 | 0.0% | -3.13% | -2.78% |
| Drugstore Chains | 1 | 0.0% | -3.14% | -3.14% |
| Electronic Equipment/Instruments | 5 | 20.0% | -3.21% | -0.93% |
| Managed Health Care | 6 | 66.7% | -3.70% | -3.43% |
| Financial Publishing/Services | 7 | 14.3% | -4.90% | -4.84% |

## Flags

- **Size cut: ON — and the generated regime line contradicts it.** `size_cut_pct: 50` fires when the index is below its 20-DMA **and** breadth is under 40%; both hold today (0 of 5 index ETFs above their 20-DMA, breadth 34.16%). The `daily-sweep.md` regime table prints "breadth 34.16% is far above the 40% trigger" — that is false, and it is a renderer defect in `tools/sweep_pipeline.py`, not a data error. The number in `_regime.json` is right; the sentence around it is wrong. Treat **size cut ON** as the operative reading.
- **"BROAD" divergence is a positioning measure, not today's tape.** It compares large caps above their 20-DMA (34.16%) with index ETFs above their 20-DMA (0%). Today itself the equal-weight fell harder than the cap-weight (**RSP -1.45% vs SPY -1.01%**) on 239 vs 837 decliners. The band says the *structure* is broader than the index; it does not say the broad market was strong today.
- **`uncertainty: true` on a thin margin** — VIX/VIX3M = 1.0192 (25.46 / 24.98). The flag is on, but it is barely above the 1.0 threshold, so it is a mild confirmation rather than a spike reading. The VIX pair is a **single settled pair**, quoted from the Cboe delayed-quote CDN at 16:15:01 ET and pulled twice 5 s apart with identical values; no mid-session print is mixed in anywhere in this document.
- **`late_cycle: false` is genuine** — the `atr_extensions` map is non-empty (all five index ETFs) and the extreme is RSP at +0.37% above its 50-DMA, so the flag was computed rather than defaulted to false.
- **The tiering order is inherited from the T+1 book, and today's fresh leaders are outside Focus/Tier-A.** Focus and Tier-A are resolved from the **2026-11-16** branch ordering (the four-percent breakout ranked by that day's gain): 186 names cleared ≥2 stylists and 28 cleared ≥3, and the cap keeps the head of that order. Consequence: **SLS (+156.4% today, 4 stylists, `fresh+t1`) is in the book and in neither list**, and the fresh book contributed 0 Tier-A names. The tiering is not wrong about the screens — the screens it ranks are yesterday's.

## Method, source health & caveats

**Sources and sessions.** Breadth, the fresh book and the movers tables are computed from the **TradingView scanner** on the **2026-11-17 settled close** (1,086 names in the breadth universe; `totalCount` equals rows fetched on both scans, so no truncation). The volatility pair is the **Cboe delayed-quote CDN**, quoted once as a pair (VIX 25.46 / VIX3M 24.98, 16:15:01 ET, two pulls 5 s apart, identical). The **screen** metrics come from shibui over the MCP-over-HTTP bridge and are **T+1 = 2026-11-16**; the book's official closes come from bridge `market-recap`. The two books are never blended: every row publishes `data_as_of` and `source` (`fresh` / `t1` / `fresh+t1`).

**Coverage.** All 9 branches were fetched uncapped, one query per branch, and paged until `rows_kept == rows_passing` on every one — 1,250 screened rows → 1,150 distinct candidates. No branch count lands on a cap (30 / 50 / 60 / 200), so the truncation fingerprint is absent.

**Caveats.** (1) shibui is T+1, so every multi-session context screen (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) describes **2026-11-16**, and the Focus/Tier-A *ordering* is inherited from that session's branch ranking — see the flags block. (2) The VIX print is a delayed CDN quote stamped 16:15:01 ET, not a live tick. (3) The industry table uses TradingView's own industry taxonomy, so a name's sector label can differ from the issuer's GICS mapping used elsewhere in the book. (4) The renderer defect noted in the flags block: `tools/sweep_pipeline.py` prints "breadth 34.16% is far above the 40% trigger" — false; the size cut is ON.

**Catalysts.** Named catalysts in this artifact are sourced from public wire copy (Reuters, Benzinga, MT Newswires, Investing.com, Yahoo Finance) fetched during the run. Where no catalyst is named, none was sourced and none is implied.
