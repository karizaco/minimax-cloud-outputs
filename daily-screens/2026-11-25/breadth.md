---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "18:30 ET, 2026-11-25 (scheduled fire; window check OK, stall_min 0 — not a replay)"
data_date: "2026-11-25 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-24)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1086 names; totalCount 1086 = rows fetched, no truncation"
vix_quote_time: "2026-11-25 16:15:01 ET (Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-25 (first observed 2026-11-19, reproduced 2026-11-25); both symbols read from the same session bar, 1 pull(s) 0 s apart — identical)"
vix_pair: "VIX 28.29 / VIX3M 26.29 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-25/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 0
uncertainty: true
late_cycle: false
---

# Breadth & Regime — End-of-Day — Wednesday 25 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-25. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-24) and are not blended into this file.

## TL;DR

The 2026-11-25 close was a **broad** session with a **weak index**: 775 names advanced against 294 declined (ratio 2.64) and the median large cap gained +0.67%, yet **not one of the five index ETFs is above its 20-DMA** and only 41.07% of the $10B+ universe is above its own — a **+41.07 pp BROAD divergence**, so participation is genuinely broader than the headline index. Volatility is the caution flag: the single VIX/VIX3M pair reads **28.29 / 26.29** (ratio 1.0761, VIX +7.32% on the day), so `uncertainty` is true. `size_cut_pct` stays **0** only because breadth sits 1.07 pp above its 40% trigger, and `late_cycle` is false — the extreme index is RSP at +0.43% above its 50-DMA while QQQ is 10.34% below its own. In short: the tape was healthy and the index posture is broken, which is the opposite of what the index level alone suggests.

## Breadth — 2026-11-25 settled session

| Metric | Value |
|---|---|
| Universe | 1086 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **41.07%** (446 / 1086) |
| Above 50-DMA | 47.05% (511 / 1086) |
| Above 200-DMA | 43.28% (470 / 1086) |
| Advance / decline / unchanged | **775 / 294 / 17** — ratio 2.64, net **+481** |
| Median name | +0.67%  ·  mean +0.83% |
| Move distribution | ≥ +5%: 21 · +2..5%: 186 · 0..2%: 585 · −2..0: 249 · −5..−2: 40 · ≤ −5%: 5 |

## Participation — the advance/decline tally

Computed on the **same 1086-name population** as the breadth percentage, from the settled session: **775 advancing, 294 declining, 17 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **+481**, ratio **2.64**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+41.07 pp** |
| band | **BROAD** |
| large-cap % above 20-DMA | 41.07% |
| index ETFs above their 20-DMA | 0% (0 of 5) |

A **BROAD** divergence: the average large cap is materially healthier than the index - participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 716.70 | -0.29% | 740.33 | 757.89 | 733.16 | **-5.43%** | 2.17% |
| QQQ | 633.93 | -0.65% | 666.73 | 707.05 | 683.50 | **-10.34%** | 3.40% |
| RSP | 215.74 | +0.83% | 217.60 | 214.82 | 209.40 | **+0.43%** | 1.65% |
| IWM | 268.87 | +0.65% | 274.39 | 277.16 | 279.59 | **-2.99%** | 2.18% |
| QQQE | 109.84 | +0.24% | 113.59 | 117.38 | 113.93 | **-6.42%** | 2.44% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at +0.43%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **28.29** | 26.36 | +1.93 (+7.3%) | 2026-11-25 16:15:01 ET |
| VIX3M | **26.29** | 25.47 | +0.82 (+3.2%) | 2026-11-25 16:15:01 ET |

Source: Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-25 (first observed 2026-11-19, reproduced 2026-11-25); both symbols read from the same session bar. Pulled 1 time(s), 0 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **1.0761** → `uncertainty: true` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | size cut is off - breadth 41.07% is not under the 40% trigger |
| `uncertainty` | **true** | the flag fires when VIX/VIX3M > 1.0; the ratio is 1.0761 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max +0.43%, RSP) |
| `index_below_20sma` | **true** | only 0 of 5 index ETFs are above their 20-DMA (0%) |

Payload: `daily-screens/2026-11-25/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Specialty Telecommunications | 3 | 0.0% | +3.90% | +1.30% |
| Agricultural Commodities/Milling | 2 | 0.0% | +3.79% | +3.79% |
| Motor Vehicles | 9 | 44.4% | +3.43% | +2.77% |
| Investment Trusts/Mutual Funds | 2 | 0.0% | +3.40% | +3.40% |
| Precious Metals | 13 | 7.7% | +3.37% | +3.14% |
| Construction Materials | 6 | 83.3% | +3.22% | +3.01% |
| Trucks/Construction/Farm Machinery | 7 | 57.1% | +2.95% | +2.48% |
| Home Furnishings | 1 | 100.0% | +2.88% | +2.88% |
| Containers/Packaging | 5 | 60.0% | +2.85% | +2.89% |
| Homebuilding | 6 | 100.0% | +2.82% | +2.81% |
| Food: Major Diversified | 2 | 100.0% | +2.77% | +2.77% |
| Casinos/Gaming | 2 | 50.0% | +2.76% | +2.76% |
| Oil & Gas Production | 5 | 0.0% | +2.67% | +2.33% |
| Hospital/Nursing Management | 3 | 100.0% | +2.65% | +2.02% |
| Pulp & Paper | 3 | 66.7% | +2.62% | +2.13% |
| Information Technology Services | 17 | 52.9% | +2.60% | +1.86% |
| Wholesale Distributors | 9 | 44.4% | +2.56% | +1.28% |
| Cable/Satellite TV | 4 | 50.0% | +2.56% | +0.92% |
| Trucking | 5 | 60.0% | +2.45% | +2.52% |
| Industrial Specialties | 3 | 100.0% | +2.38% | +2.40% |
| Computer Processing Hardware | 8 | 12.5% | +2.36% | +2.31% |
| Water Utilities | 3 | 100.0% | +2.34% | +1.76% |
| Real Estate Development | 3 | 100.0% | +2.31% | +3.30% |
| Other Metals/Minerals | 7 | 0.0% | +2.16% | +2.14% |
| Auto Parts: OEM | 5 | 80.0% | +2.16% | +2.00% |
| Insurance Brokers/Services | 6 | 100.0% | +2.15% | +1.81% |
| Contract Drilling | 2 | 0.0% | +2.14% | +2.14% |
| Home Improvement Chains | 2 | 100.0% | +2.07% | +2.07% |
| Specialty Insurance | 1 | 100.0% | +1.99% | +1.99% |
| Tobacco | 3 | 33.3% | +1.97% | +1.95% |
| Steel | 8 | 0.0% | +1.95% | +1.59% |
| Chemicals: Specialty | 6 | 50.0% | +1.80% | +1.94% |
| Oilfield Services/Equipment | 2 | 0.0% | +1.79% | +1.79% |
| Railroads | 5 | 60.0% | +1.70% | +2.16% |
| Chemicals: Major Diversified | 2 | 100.0% | +1.68% | +1.68% |
| Other Transportation | 3 | 33.3% | +1.67% | +1.26% |
| Advertising/Marketing Services | 1 | 100.0% | +1.65% | +1.65% |
| Finance/Rental/Leasing | 16 | 31.2% | +1.64% | +1.72% |
| Internet Software/Services | 20 | 45.0% | +1.59% | +1.89% |
| Air Freight/Couriers | 9 | 44.4% | +1.58% | +1.21% |
| Electronics/Appliances | 1 | 100.0% | +1.56% | +1.56% |
| Metal Fabrication | 2 | 0.0% | +1.55% | +1.55% |
| Integrated Oil | 22 | 4.5% | +1.53% | +1.12% |
| Food Distributors | 2 | 100.0% | +1.47% | +1.47% |
| Household/Personal Care | 7 | 100.0% | +1.45% | +0.88% |
| Industrial Conglomerates | 1 | 100.0% | +1.44% | +1.44% |
| Financial Conglomerates | 6 | 0.0% | +1.35% | +1.09% |
| Publishing: Books/Magazines | 1 | 100.0% | +1.34% | +1.34% |
| Food: Specialty/Candy | 7 | 85.7% | +1.32% | +1.19% |
| Beverages: Non-Alcoholic | 6 | 50.0% | +1.30% | +0.80% |
| Apparel/Footwear | 5 | 40.0% | +1.25% | +1.31% |
| Aerospace & Defense | 28 | 25.0% | +1.20% | +0.76% |
| Miscellaneous Commercial Services | 16 | 50.0% | +1.19% | +1.37% |
| Restaurants | 10 | 90.0% | +1.11% | +1.24% |
| Internet Retail | 7 | 14.3% | +1.03% | +1.56% |
| Gas Distributors | 6 | 33.3% | +0.99% | +0.86% |
| Environmental Services | 5 | 60.0% | +0.95% | +0.80% |
| Publishing: Newspapers | 3 | 33.3% | +0.94% | +0.71% |
| Movies/Entertainment | 3 | 100.0% | +0.85% | +1.05% |
| Financial Publishing/Services | 7 | 14.3% | +0.80% | +1.19% |
| Property/Casualty Insurance | 15 | 86.7% | +0.79% | +0.75% |
| Apparel/Footwear Retail | 4 | 75.0% | +0.78% | +1.04% |
| Medical Distributors | 3 | 100.0% | +0.78% | +1.17% |
| Specialty Stores | 15 | 66.7% | +0.77% | +1.32% |
| Building Products | 4 | 75.0% | +0.73% | +2.24% |
| Other Consumer Services | 4 | 25.0% | +0.73% | +0.60% |
| Oil & Gas Pipelines | 14 | 21.4% | +0.72% | +0.69% |
| Chemicals: Agricultural | 2 | 0.0% | +0.71% | +0.71% |
| Investment Managers | 38 | 26.3% | +0.66% | +0.56% |
| Telecommunications Equipment | 8 | 37.5% | +0.66% | +0.78% |
| Tools & Hardware | 3 | 33.3% | +0.65% | +0.79% |
| Electronic Equipment/Instruments | 5 | 0.0% | +0.61% | +0.16% |
| Packaged Software | 56 | 39.3% | +0.57% | +0.77% |
| Electronics/Appliance Stores | 2 | 100.0% | +0.56% | +0.56% |
| Multi-Line Insurance | 25 | 60.0% | +0.54% | +0.55% |
| Recreational Products | 2 | 50.0% | +0.54% | +0.54% |
| Life/Health Insurance | 9 | 33.3% | +0.52% | +0.76% |
| Electronics Distributors | 1 | 0.0% | +0.52% | +0.52% |
| Managed Health Care | 6 | 0.0% | +0.51% | +0.77% |
| Food: Meat/Fish/Dairy | 4 | 50.0% | +0.48% | -0.17% |
| Regional Banks | 35 | 20.0% | +0.47% | +0.51% |
| Drugstore Chains | 1 | 0.0% | +0.46% | +0.46% |
| Biotechnology | 18 | 72.2% | +0.42% | +0.19% |
| Electrical Products | 8 | 12.5% | +0.42% | +0.41% |
| Investment Banks/Brokers | 24 | 25.0% | +0.41% | +0.21% |
| Electric Utilities | 41 | 56.1% | +0.39% | +0.50% |
| Wireless Telecommunications | 14 | 64.3% | +0.38% | +0.29% |
| Real Estate Investment Trusts | 75 | 40.0% | +0.38% | +0.22% |
| Engineering & Construction | 9 | 33.3% | +0.28% | +0.36% |
| Beverages: Alcoholic | 6 | 16.7% | +0.26% | -0.06% |
| Marine Shipping | 1 | 100.0% | +0.25% | +0.25% |
| Department Stores | 1 | 100.0% | +0.23% | +0.23% |
| Major Banks | 85 | 22.4% | +0.20% | +0.06% |
| Commercial Printing/Forms | 1 | 100.0% | +0.19% | +0.19% |
| Semiconductors | 33 | 3.0% | +0.11% | -0.07% |
| Pharmaceuticals: Major | 30 | 70.0% | +0.10% | -0.05% |
| Industrial Machinery | 25 | 52.0% | +0.07% | +0.28% |
| Services to the Health Industry | 1 | 100.0% | +0.01% | +0.01% |
| Medical Specialties | 32 | 62.5% | -0.10% | +0.27% |
| Broadcasting | 3 | 33.3% | -0.21% | -0.84% |
| Medical/Nursing Services | 8 | 37.5% | -0.23% | -0.03% |
| Food Retail | 1 | 100.0% | -0.41% | -0.41% |
| Alternative Power Generation | 2 | 50.0% | -0.42% | -0.42% |
| Electronic Production Equipment | 4 | 0.0% | -0.46% | -0.38% |
| Major Telecommunications | 2 | 100.0% | -0.47% | -0.47% |
| Pharmaceuticals: Generic | 1 | 0.0% | -0.60% | -0.60% |
| Hotels/Resorts/Cruise lines | 9 | 22.2% | -0.64% | -0.60% |
| Airlines | 5 | 40.0% | -0.70% | +0.19% |
| Oil Refining/Marketing | 5 | 0.0% | -0.76% | -0.51% |
| Computer Peripherals | 7 | 14.3% | -0.85% | -0.55% |
| Electronic Components | 4 | 0.0% | -1.34% | -1.22% |
| Discount Stores | 3 | 66.7% | -1.46% | -1.58% |
| Data Processing Services | 7 | 57.1% | -1.74% | +0.39% |
| Pharmaceuticals: Other | 1 | 0.0% | -3.04% | -3.04% |

## Flags

- `uncertainty: true` — VIX/VIX3M = 1.0761 (> 1.0). The VIX rose +7.32% to 28.29; this is a term-structure inversion, not a vol spike on the day.
- `index_below_20sma: true` — 0 of 5 index ETFs above their 20-DMA. QQQ is -10.34% below its 50-DMA and SPY -5.43%; RSP +0.43% is the only one positive.
- `size_cut_pct: 0` (size cut OFF) — but the headroom is thin: breadth 41.07% against a 40% trigger, 1.07 pp. One more session of erosion flips it on.
- `late_cycle: false` — no index ETF more than 6% above its 50-DMA (max RSP +0.43%). Nothing here is late-cycle extended.
- `breadth_divergence: +41.07 pp — BROAD` — the index is the weak leg, not the average name. Do not read the SPY/QQQ level as the state of the market.
- Coverage collision (disclosed, not a defect) — two context branches land on a legacy cap value (`B_stockbee_ep9m` 200, `C_qullamaggie_rs` 60); both verified complete via `rows_passing == rows_kept` with no per-branch LIMIT in the SQL.
- Cross-reference — the 14:00 ET intraday read sits beside this one at `daily-screens/2026-11-25/breadth-snapshot.md` (cron #10). Different quote times, different universes; this file is the end-of-day read.

## Method, source health & caveats

**Sources — every one named, with its status.**

| Source | Used for | Status |
|---|---|---|
| TradingView scanner (`POST scanner.tradingview.com/america/scan`) | the FRESH trigger book (3,728 names, mcap > $300M) and the settled breadth layer (1,086 names, mcap > $10B) | **ok** — `totalCount` equals rows fetched on both pulls, so neither book is truncated |
| shibui-finance over the MCP-over-HTTP bridge (`shibui stock_data_query`) | 9 context branches on the 2026-11-24 session, the ADR%/streak/GICS enrichment, the CANSLIM growth half, the valuation/quality overlay (1,181 symbols) | **ok** |
| bridge `market-recap get_quotes` | the official 16:00 ET close for every book name (`market_state: post`) | **ok** |
| Yahoo chart API (`^VIX` / `^VIX3M`) | the single volatility pair (quote time 2026-11-25 16:15:01 ET) | **ok** — but see the degraded source below |
| Cboe delayed-quote CDN | the primary volatility pair | **failed: HTTP 403 (Cloudflare)** from this egress |
| Finviz | — | not used (retired from the source chain) |

**degraded_sources: 1** — the Cboe delayed-quote CDN. The volatility pair came from the documented Yahoo chart-API fallback instead, with `^VIX` and `^VIX3M` read from the **same session bar** and published as one pair everywhere in these files.

**Sessions and lag.** The SCREEN metrics in `daily-sweep.md` describe shibui's newest ingested session, **2026-11-24** — shibui is T+1. The breadth numbers and the trigger book describe the **2026-11-25 settled close**. Every row publishes `data_as_of` and `source` (`fresh` / `t1` / `fresh+t1`); the two books are never blended.

**Coverage.** All 9 context branches and all 4 fresh branches were fetched as one query per branch, uncapped, and paged until the rows collected equalled `rows_passing` (`COUNT(*) OVER ()` computed inside the branch, before any cap). `rows_kept == rows_passing` on every branch. Two context counts land on a legacy cap value — `B_stockbee_ep9m` 200 and `C_qullamaggie_rs` 60 — and both were verified complete: the branch SQL carries no per-branch LIMIT, so `rows_passing` is the true passing count rather than a cap. The 10% gap branch's 0 is a screen outcome (two names in the universe opened ≥ +10%, both failing the $3 close and $50M ADV gates).

**What could not be verified.** The same-day close column comes from the bridge's `market-recap` batch (`market_state: post`) rather than a Nasdaq `/info` `secondaryData` pull — both carry the official 16:00 ET print, but they are different publishers and were not cross-checked against each other here. No catalyst was sourced for any name in this artifact: the movers tables are price facts, and nothing in them should be read as an explained move.
