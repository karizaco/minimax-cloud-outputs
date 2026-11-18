---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "2026-11-18 18:30 ET"
data_date: "2026-11-18 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-17)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1081 names; totalCount 1081 = rows fetched, no truncation"
vix_quote_time: "2026-11-18 16:15:01 ET (Cboe delayed-quote CDN, 2 pulls 5 s apart — identical)"
vix_pair: "VIX 24.56 / VIX3M 24.29 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-18/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
---

# Breadth & Regime — End-of-Day — Wednesday 18 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-18. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-17) and are not blended into this file.

## TL;DR

- **Breadth broke down into the close: 32.01% of the 1,081 large caps are above their own 20-DMA** (346 / 1,081), with 43.57% above the 50-DMA and 43.48% above the 200-DMA. **470 advancing against 603 declining** (8 unchanged), a ratio of 0.78 and a net **-133** on the same population; the median name closed **-0.20%**.
- **The divergence is still BROAD at +32.01 pp**, and it is the same story as this morning's: the average large cap is materially healthier than the index, so **the index is the weak leg** — all five index ETFs are below their own 20-DMA, SPY is **-4.24%** and QQQ **-7.68%** versus their 50-DMA, and RSP (+0.21%) is the only one above its own 50-DMA.
- **Caveat on comparability:** this is the settled **2026-11-18** tape on a 1,081-name TradingView universe ($10B+ market cap). Cron #10's intraday file measured the **2026-11-17** session on a **877-name** shibui universe and quoted a live VIX of 23.54/23.53 at 13:47 ET. The two files are deliberately different — this is the end-of-day read, with one volatility pair (24.56 / 24.29, 16:15:01 ET) used throughout.

## Breadth — 2026-11-18 settled session

| Metric | Value |
|---|---|
| Universe | 1081 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **32.01%** (346 / 1081) |
| Above 50-DMA | 43.57% (471 / 1081) |
| Above 200-DMA | 43.48% (470 / 1081) |
| Advance / decline / unchanged | **470 / 603 / 8** — ratio 0.78, net **-133** |
| Median name | -0.20%  ·  mean -0.29% |
| Move distribution | ≥ +5%: 22 · +2..5%: 83 · 0..2%: 373 · −2..0: 420 · −5..−2: 151 · ≤ −5%: 32 |

## Participation — the advance/decline tally

Computed on the **same 1081-name population** as the breadth percentage, from the settled session: **470 advancing, 603 declining, 8 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **-133**, ratio **0.78**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+32.01 pp** |
| band | **BROAD** |
| large-cap % above 20-DMA | 32.01% |
| index ETFs above their 20-DMA | 0% (0 of 5) |

A **BROAD** divergence means the average large cap is materially healthier than the index — participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 730.20 | -0.31% | 753.72 | 762.51 | 732.55 | **-4.24%** | 1.55% |
| QQQ | 659.51 | +0.39% | 686.30 | 714.36 | 682.81 | **-7.68%** | 2.44% |
| RSP | 215.43 | -0.15% | 218.87 | 214.98 | 209.13 | **+0.21%** | 1.28% |
| IWM | 270.12 | +0.40% | 277.80 | 279.38 | 279.55 | **-3.31%** | 1.82% |
| QQQE | 112.01 | +0.03% | 115.92 | 118.22 | 113.76 | **-5.25%** | 1.82% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at +0.21%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **24.56** | 25.46 | -0.90 (-3.5%) | 2026-11-18 16:15:01 ET |
| VIX3M | **24.29** | 24.98 | -0.69 (-2.8%) | 2026-11-18 16:15:01 ET |

Source: Cboe delayed-quote CDN. Pulled 2 times, 5 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **1.0111** → `uncertainty: true` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **50** | size cut only when the index is below its 20-DMA **and** breadth < 40% — breadth is 32.01% |
| `uncertainty` | **true** | VIX/VIX3M = 1.0111 ≤ 1 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max +0.21%, RSP) |
| `index_below_20sma` | **true** | only 0 of 5 index ETFs are above their 20-DMA (0%) |

Payload: `daily-screens/2026-11-18/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Home Furnishings | 1 | 0.0% | +7.39% | +7.39% |
| Electronics/Appliances | 1 | 100.0% | +4.53% | +4.53% |
| Apparel/Footwear Retail | 4 | 75.0% | +4.46% | +4.36% |
| Electronics/Appliance Stores | 2 | 100.0% | +3.28% | +3.28% |
| Movies/Entertainment | 3 | 100.0% | +2.92% | +2.98% |
| Apparel/Footwear | 5 | 20.0% | +2.74% | +1.82% |
| Building Products | 4 | 50.0% | +2.01% | +1.78% |
| Commercial Printing/Forms | 1 | 100.0% | +1.63% | +1.63% |
| Hotels/Resorts/Cruise lines | 9 | 88.9% | +1.61% | +0.75% |
| Alternative Power Generation | 4 | 75.0% | +1.56% | +1.06% |
| Chemicals: Major Diversified | 2 | 100.0% | +1.41% | +1.41% |
| Construction Materials | 6 | 33.3% | +1.31% | +1.92% |
| Services to the Health Industry | 1 | 100.0% | +1.30% | +1.30% |
| Recreational Products | 2 | 50.0% | +1.30% | +1.30% |
| Industrial Specialties | 3 | 100.0% | +1.29% | +1.54% |
| Electrical Products | 9 | 22.2% | +1.24% | +0.36% |
| Food: Specialty/Candy | 7 | 57.1% | +1.24% | +0.82% |
| Discount Stores | 3 | 33.3% | +1.23% | +1.49% |
| Industrial Machinery | 25 | 36.0% | +1.21% | +1.44% |
| Engineering & Construction | 8 | 62.5% | +1.05% | +0.65% |
| Specialty Stores | 15 | 86.7% | +0.96% | +0.90% |
| Restaurants | 10 | 90.0% | +0.95% | +0.76% |
| Medical Specialties | 34 | 55.9% | +0.93% | +1.20% |
| Tools & Hardware | 3 | 66.7% | +0.91% | +0.56% |
| Electronic Equipment/Instruments | 5 | 20.0% | +0.90% | +1.00% |
| Electronic Production Equipment | 4 | 0.0% | +0.89% | +1.30% |
| Telecommunications Equipment | 8 | 37.5% | +0.87% | +0.41% |
| Computer Peripherals | 7 | 28.6% | +0.80% | +1.72% |
| Electronic Components | 4 | 0.0% | +0.80% | +0.30% |
| Food: Meat/Fish/Dairy | 4 | 50.0% | +0.75% | +0.57% |
| Advertising/Marketing Services | 1 | 100.0% | +0.65% | +0.65% |
| Airlines | 5 | 60.0% | +0.62% | +0.69% |
| Data Processing Services | 7 | 57.1% | +0.60% | -0.38% |
| Trucking | 5 | 80.0% | +0.60% | +0.92% |
| Homebuilding | 6 | 0.0% | +0.59% | +0.65% |
| Packaged Software | 55 | 27.3% | +0.55% | +0.04% |
| Other Consumer Services | 4 | 50.0% | +0.49% | +0.16% |
| Insurance Brokers/Services | 6 | 100.0% | +0.44% | +0.13% |
| Food: Major Diversified | 2 | 100.0% | +0.44% | +0.44% |
| Pulp & Paper | 3 | 66.7% | +0.40% | +1.09% |
| Food Distributors | 2 | 50.0% | +0.39% | +0.39% |
| Railroads | 5 | 40.0% | +0.36% | +0.37% |
| Electric Utilities | 42 | 52.4% | +0.35% | +0.37% |
| Major Telecommunications | 2 | 100.0% | +0.33% | +0.33% |
| Home Improvement Chains | 2 | 50.0% | +0.32% | +0.32% |
| Real Estate Development | 3 | 66.7% | +0.31% | +0.43% |
| Auto Parts: OEM | 5 | 40.0% | +0.28% | +0.60% |
| Real Estate Investment Trusts | 73 | 24.7% | +0.25% | +0.16% |
| Beverages: Alcoholic | 6 | 66.7% | +0.22% | -0.36% |
| Internet Retail | 7 | 28.6% | +0.21% | -0.95% |
| Publishing: Books/Magazines | 1 | 0.0% | +0.18% | +0.18% |
| Beverages: Non-Alcoholic | 6 | 50.0% | +0.16% | +0.50% |
| Wholesale Distributors | 9 | 44.4% | +0.10% | -0.41% |
| Industrial Conglomerates | 1 | 100.0% | +0.09% | +0.09% |
| Department Stores | 1 | 0.0% | +0.08% | +0.08% |
| Containers/Packaging | 5 | 0.0% | +0.07% | +0.00% |
| Metal Fabrication | 2 | 0.0% | -0.02% | -0.02% |
| Air Freight/Couriers | 9 | 77.8% | -0.03% | -0.35% |
| Information Technology Services | 17 | 17.6% | -0.07% | -1.11% |
| Semiconductors | 33 | 12.1% | -0.13% | -0.11% |
| Internet Software/Services | 20 | 30.0% | -0.15% | +0.05% |
| Finance/Rental/Leasing | 16 | 12.5% | -0.18% | -0.32% |
| Water Utilities | 3 | 66.7% | -0.28% | +1.16% |
| Gas Distributors | 6 | 16.7% | -0.28% | -0.28% |
| Biotechnology | 16 | 43.8% | -0.36% | -0.49% |
| Investment Managers | 38 | 10.5% | -0.37% | -0.36% |
| Financial Publishing/Services | 7 | 0.0% | -0.37% | -0.35% |
| Life/Health Insurance | 9 | 22.2% | -0.39% | -0.65% |
| Household/Personal Care | 7 | 57.1% | -0.44% | -0.76% |
| Specialty Telecommunications | 2 | 100.0% | -0.49% | -0.49% |
| Aerospace & Defense | 28 | 25.0% | -0.52% | -0.67% |
| Motor Vehicles | 9 | 22.2% | -0.52% | -0.53% |
| Cable/Satellite TV | 4 | 50.0% | -0.54% | +0.11% |
| Medical Distributors | 3 | 100.0% | -0.55% | -0.64% |
| Multi-Line Insurance | 25 | 24.0% | -0.56% | -0.68% |
| Specialty Insurance | 1 | 100.0% | -0.57% | -0.57% |
| Broadcasting | 3 | 33.3% | -0.58% | -1.55% |
| Electronics Distributors | 1 | 0.0% | -0.60% | -0.60% |
| Regional Banks | 35 | 22.9% | -0.61% | -0.46% |
| Wireless Telecommunications | 14 | 71.4% | -0.68% | -0.29% |
| Computer Processing Hardware | 8 | 12.5% | -0.69% | -0.17% |
| Contract Drilling | 2 | 0.0% | -0.72% | -0.72% |
| Property/Casualty Insurance | 15 | 60.0% | -0.77% | -0.89% |
| Trucks/Construction/Farm Machinery | 5 | 20.0% | -0.81% | -0.69% |
| Pharmaceuticals: Major | 29 | 48.3% | -0.85% | -1.28% |
| Investment Banks/Brokers | 23 | 21.7% | -0.86% | -0.24% |
| Major Banks | 85 | 7.1% | -0.86% | -0.59% |
| Miscellaneous Commercial Services | 15 | 26.7% | -0.87% | -0.56% |
| Pharmaceuticals: Generic | 1 | 100.0% | -0.92% | -0.92% |
| Oilfield Services/Equipment | 2 | 0.0% | -1.02% | -1.02% |
| Oil & Gas Pipelines | 14 | 7.1% | -1.08% | -0.99% |
| Other Transportation | 3 | 66.7% | -1.10% | -1.03% |
| Tobacco | 3 | 0.0% | -1.17% | -1.12% |
| Oil & Gas Production | 5 | 0.0% | -1.23% | -1.52% |
| Environmental Services | 5 | 40.0% | -1.30% | -1.29% |
| Steel | 8 | 0.0% | -1.59% | -0.77% |
| Publishing: Newspapers | 3 | 33.3% | -1.61% | -0.91% |
| Pharmaceuticals: Other | 1 | 0.0% | -1.76% | -1.76% |
| Casinos/Gaming | 2 | 50.0% | -1.84% | -1.84% |
| Medical/Nursing Services | 8 | 50.0% | -1.86% | -1.88% |
| Investment Trusts/Mutual Funds | 2 | 0.0% | -1.90% | -1.90% |
| Chemicals: Specialty | 8 | 0.0% | -2.17% | -2.09% |
| Agricultural Commodities/Milling | 2 | 0.0% | -2.48% | -2.48% |
| Financial Conglomerates | 6 | 0.0% | -2.49% | -2.20% |
| Food Retail | 1 | 100.0% | -2.58% | -2.58% |
| Other Metals/Minerals | 7 | 14.3% | -3.21% | -4.49% |
| Integrated Oil | 22 | 0.0% | -3.49% | -3.61% |
| Hospital/Nursing Management | 3 | 0.0% | -3.95% | -3.80% |
| Chemicals: Agricultural | 2 | 0.0% | -4.75% | -4.75% |
| Drugstore Chains | 1 | 0.0% | -5.20% | -5.20% |
| Oil Refining/Marketing | 5 | 0.0% | -5.33% | -5.50% |
| Precious Metals | 13 | 0.0% | -5.78% | -5.92% |
| Managed Health Care | 6 | 0.0% | -7.90% | -7.33% |

## Flags

- **The `uncertainty` flag is marginal:** VIX/VIX3M = 1.0111, only 0.011 above the 1.0 trigger — a VIX roughly 0.3 lower would flip it off. It is a real flag, but it is not a strong one.
- **SLS** — Tier-A on a parabolic five-session run (+128.79%) that ended **-6.27% today**; ATR% 12.80 (99.7th pctile), +74.86% above its 20-DMA. The extension label is a state detector, not a forward signal.
- **ALAB and RYTM are Tier-A on the 2026-11-17 screen only** — neither name triggered on the 2026-11-18 bar (ALAB +2.43%, RYTM +2.08%, both under the 4% gate).
- **Managed Health Care is the one industry group where no constituent is above its own 20-DMA** and the average name fell **-7.90%** (HUM -12.98%, UNH -10.21%, ELV -7.63%, CNC -7.03%) — a group move, not a distorted print.
- **RYTM and SLS carry no trailing P/E.** That is published as `earnings_data_missing` with the valuation gate disclosed; a missing value is never counted as a red flag.
- **All five index ETFs are below their 20-DMA while only RSP is above its 50-DMA** — an unusual configuration. `late_cycle` is `false` only because no index is more than 6% *above* its 50-DMA (the extreme is RSP at +0.21%); the map in `_regime.json` is non-empty, so the flag was genuinely computed.

## Method, source health & caveats

- **Sources.** TradingView scanner (the 2026-11-18 settled bar: the fresh book, the breadth universe, the theme pool); shibui over the MCP-over-HTTP bridge (the T+1 context screens, the CANSLIM growth half, the valuation/quality overlay); the Cboe delayed-quote CDN (the VIX/VIX3M pair, pulled twice 5 s apart and identical); the bridge's `market-recap` (the official 16:00 ET close for the book's names, `market_state: post`).
- **Universes.** Breadth: 1,081 names — NYSE/NASDAQ/AMEX, type in {stock, dr}, `market_cap_basic > $10B`; `totalCount 1081` = rows fetched, no truncation. Fresh book: 3,756 names (same venue/type filter, `market_cap_basic > $300M`), of which 337 passed a trigger gate. The published book is the 1,179 distinct candidates.
- **Coverage.** 9/9 branches fetched uncapped and paged until `rows_kept == rows_passing`; no branch count landed on 30 / 50 / 60 / 200. The theme branch is a published screen over a 226-name pool.
- **Caveats.** shibui is T+1, so every CONTEXT screen describes **2026-11-17** while every TRIGGER screen describes **2026-11-18**; the parabolic five-session move stays on shibui (T+1) and is deliberately **not** re-expressed on the scanner's `Perf.W`, which measures a six-session window. The valuation overlay is a **label, not a filter** — 582 of 992 names carry a red flag and 93 have no reported trailing earnings (disclosed, never counted as a flag). Finviz is Cloudflare-blocked from this egress and is not in the chain; Yahoo JSON was not needed because the bridge is the quote source of record.
