---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "18:30 ET (2026-11-24)"
data_date: "2026-11-24 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-23)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1079 names; totalCount 1079 = rows fetched, no truncation"
vix_quote_time: "2026-11-24 16:15:01 ET (Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-19; both symbols read from the same session bar, 1 pull(s) 0 s apart — identical)"
vix_pair: "VIX 26.36 / VIX3M 25.47 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-24/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
---

# Breadth & Regime — End-of-Day — Tuesday 24 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-24. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-23) and are not blended into this file.

## TL;DR

**621 of 1,079 large caps advanced on 2026-11-24 and the median name was +0.45%, yet the Nasdaq fell 1.48% and not one of the five index ETFs is above its own 20-DMA.** That is not a contradiction — it is the fingerprint of a **single-complex unwind inside a market that was still rising**. Monday's historic relief rally (NVDA +31.48% on Jensen Huang's reinstatement, S&P +4.7%, Nasdaq +6.5%) was handed straight back by the AI trade: chip stocks lost roughly **$870B**, SOXX closed **-8%**, NVDA fell **5.86%** to 155.38 and ADI plunged **17.37%** on a weak guide. But the same tape rotated *into* biotech and retail (INSM +14.13% on Sanofi's $41B cash acquisition, DKS +14.59%, DLTR +11.18%, Biotechnology +5.19% on average). So the advance/decline tally (broad participation, +169 net) and the percentage-above-20-DMA (broken trend, 34.94%) are measuring different things and disagree **on purpose** — the divergence reads **+34.94 pp, BROAD**. Volatility is the tell: VIX **26.36** vs VIX3M **25.47** = **1.0349**, so `uncertainty` is on, but the VIX actually **fell 1.0%** on a day the chip complex lost a quarter of its market value — this is rotation, not capitulation. Regime: size cut **ON** (50), index below its 20-DMA, not late cycle.

## Breadth — 2026-11-24 settled session

| Metric | Value |
|---|---|
| Universe | 1079 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **34.94%** (377 / 1079) |
| Above 50-DMA | 43.65% (471 / 1079) |
| Above 200-DMA | 41.61% (449 / 1079) |
| Advance / decline / unchanged | **621 / 452 / 6** — ratio 1.37, net **+169** |
| Median name | +0.45%  ·  mean +0.02% |
| Move distribution | ≥ +5%: 28 · +2..5%: 171 · 0..2%: 428 · −2..0: 286 · −5..−2: 88 · ≤ −5%: 78 |

## Participation — the advance/decline tally

Computed on the **same 1079-name population** as the breadth percentage, from the settled session: **621 advancing, 452 declining, 6 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **+169**, ratio **1.37**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+34.94 pp** |
| band | **BROAD** |
| large-cap % above 20-DMA | 34.94% |
| index ETFs above their 20-DMA | 0% (0 of 5) |

A **BROAD** divergence: the average large cap is materially healthier than the index - participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 718.78 | -0.49% | 743.11 | 758.64 | 733.04 | **-5.25%** | 2.08% |
| QQQ | 638.10 | -1.99% | 671.31 | 708.47 | 683.39 | **-9.93%** | 3.27% |
| RSP | 213.96 | +0.54% | 217.68 | 214.75 | 209.34 | **-0.37%** | 1.58% |
| IWM | 267.14 | +0.53% | 275.01 | 277.46 | 279.58 | **-3.72%** | 2.11% |
| QQQE | 109.58 | -0.94% | 114.09 | 117.51 | 113.90 | **-6.75%** | 2.34% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at -0.37%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **26.36** | 26.62 | -0.26 (-1.0%) | 2026-11-24 16:15:01 ET |
| VIX3M | **25.47** | 25.5 | -0.03 (-0.1%) | 2026-11-24 16:15:01 ET |

Source: Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-19; both symbols read from the same session bar. Pulled 1 time(s), 0 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **1.0349** → `uncertainty: true` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **50** | size cut is ON - the index is below its 20-DMA and breadth 34.94% is UNDER the 40% trigger |
| `uncertainty` | **true** | the flag fires when VIX/VIX3M > 1.0; the ratio is 1.0349 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max -0.37%, RSP) |
| `index_below_20sma` | **true** | only 0 of 5 index ETFs are above their 20-DMA (0%) |

Payload: `daily-screens/2026-11-24/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Pharmaceuticals: Other | 1 | 100.0% | +7.72% | +7.72% |
| Discount Stores | 3 | 66.7% | +6.30% | +4.38% |
| Biotechnology | 18 | 83.3% | +5.19% | +4.98% |
| Food Retail | 1 | 100.0% | +4.42% | +4.42% |
| Pharmaceuticals: Major | 30 | 76.7% | +4.05% | +3.41% |
| Homebuilding | 6 | 50.0% | +3.73% | +3.69% |
| Insurance Brokers/Services | 6 | 100.0% | +3.58% | +3.29% |
| Apparel/Footwear Retail | 4 | 50.0% | +3.31% | +3.61% |
| Pulp & Paper | 3 | 66.7% | +3.10% | +2.27% |
| Apparel/Footwear | 5 | 20.0% | +3.07% | +3.14% |
| Medical Distributors | 3 | 100.0% | +3.03% | +2.83% |
| Managed Health Care | 6 | 0.0% | +2.56% | +2.02% |
| Marine Shipping | 1 | 0.0% | +2.33% | +2.33% |
| Specialty Stores | 15 | 60.0% | +2.30% | +2.11% |
| Cable/Satellite TV | 4 | 50.0% | +2.28% | +2.68% |
| Publishing: Newspapers | 3 | 33.3% | +2.25% | +2.08% |
| Advertising/Marketing Services | 1 | 100.0% | +2.19% | +2.19% |
| Home Improvement Chains | 2 | 100.0% | +2.19% | +2.19% |
| Beverages: Alcoholic | 6 | 16.7% | +2.13% | +2.38% |
| Household/Personal Care | 7 | 85.7% | +2.05% | +1.69% |
| Home Furnishings | 1 | 0.0% | +1.98% | +1.98% |
| Movies/Entertainment | 3 | 100.0% | +1.90% | +1.86% |
| Publishing: Books/Magazines | 1 | 0.0% | +1.90% | +1.90% |
| Oil & Gas Production | 5 | 0.0% | +1.90% | +1.80% |
| Real Estate Development | 3 | 66.7% | +1.89% | +1.56% |
| Water Utilities | 3 | 100.0% | +1.82% | +2.04% |
| Broadcasting | 3 | 33.3% | +1.79% | +1.89% |
| Medical/Nursing Services | 8 | 37.5% | +1.75% | +1.66% |
| Major Telecommunications | 2 | 100.0% | +1.72% | +1.72% |
| Food: Specialty/Candy | 7 | 85.7% | +1.69% | +2.32% |
| Electronics/Appliance Stores | 2 | 50.0% | +1.68% | +1.68% |
| Food: Major Diversified | 2 | 100.0% | +1.68% | +1.68% |
| Electronics/Appliances | 1 | 100.0% | +1.58% | +1.58% |
| Chemicals: Agricultural | 2 | 0.0% | +1.54% | +1.54% |
| Restaurants | 10 | 80.0% | +1.51% | +1.68% |
| Medical Specialties | 32 | 59.4% | +1.50% | +1.72% |
| Industrial Conglomerates | 1 | 100.0% | +1.46% | +1.46% |
| Internet Software/Services | 20 | 40.0% | +1.44% | +0.78% |
| Containers/Packaging | 5 | 20.0% | +1.40% | +1.15% |
| Specialty Insurance | 1 | 100.0% | +1.37% | +1.37% |
| Drugstore Chains | 1 | 0.0% | +1.31% | +1.31% |
| Food: Meat/Fish/Dairy | 4 | 50.0% | +1.30% | +0.78% |
| Gas Distributors | 6 | 16.7% | +1.29% | +1.36% |
| Tobacco | 3 | 0.0% | +1.28% | +1.38% |
| Environmental Services | 5 | 60.0% | +1.16% | +1.28% |
| Beverages: Non-Alcoholic | 6 | 50.0% | +1.12% | +1.27% |
| Other Transportation | 3 | 33.3% | +1.07% | +0.98% |
| Railroads | 5 | 20.0% | +1.06% | +0.67% |
| Miscellaneous Commercial Services | 16 | 31.2% | +1.06% | +1.22% |
| Construction Materials | 6 | 66.7% | +0.95% | +1.19% |
| Services to the Health Industry | 1 | 100.0% | +0.95% | +0.95% |
| Property/Casualty Insurance | 15 | 80.0% | +0.88% | +0.83% |
| Oil & Gas Pipelines | 14 | 0.0% | +0.86% | +0.71% |
| Financial Publishing/Services | 7 | 0.0% | +0.81% | +1.00% |
| Internet Retail | 7 | 14.3% | +0.76% | -0.85% |
| Contract Drilling | 2 | 0.0% | +0.74% | +0.74% |
| Hotels/Resorts/Cruise lines | 9 | 44.4% | +0.70% | +0.40% |
| Food Distributors | 2 | 100.0% | +0.61% | +0.61% |
| Integrated Oil | 22 | 0.0% | +0.54% | +0.95% |
| Real Estate Investment Trusts | 75 | 34.7% | +0.53% | +0.49% |
| Casinos/Gaming | 2 | 50.0% | +0.51% | +0.51% |
| Industrial Specialties | 3 | 66.7% | +0.49% | +0.66% |
| Other Consumer Services | 4 | 25.0% | +0.37% | +0.54% |
| Hospital/Nursing Management | 3 | 0.0% | +0.36% | +0.38% |
| Pharmaceuticals: Generic | 1 | 0.0% | +0.30% | +0.30% |
| Multi-Line Insurance | 25 | 56.0% | +0.27% | +0.50% |
| Recreational Products | 2 | 0.0% | +0.22% | +0.22% |
| Information Technology Services | 17 | 23.5% | +0.17% | +1.61% |
| Finance/Rental/Leasing | 16 | 18.8% | +0.15% | +0.08% |
| Chemicals: Specialty | 6 | 33.3% | +0.15% | +0.81% |
| Department Stores | 1 | 100.0% | +0.09% | +0.09% |
| Motor Vehicles | 9 | 22.2% | +0.04% | -0.20% |
| Wireless Telecommunications | 14 | 64.3% | +0.01% | +0.78% |
| Investment Managers | 38 | 18.4% | -0.07% | -0.23% |
| Wholesale Distributors | 9 | 11.1% | -0.16% | +0.06% |
| Life/Health Insurance | 9 | 22.2% | -0.17% | -0.27% |
| Electric Utilities | 41 | 53.7% | -0.18% | +0.16% |
| Packaged Software | 57 | 33.3% | -0.27% | +0.74% |
| Airlines | 5 | 40.0% | -0.28% | +0.19% |
| Major Banks | 85 | 31.8% | -0.31% | -0.45% |
| Oilfield Services/Equipment | 2 | 0.0% | -0.31% | -0.31% |
| Data Processing Services | 7 | 57.1% | -0.34% | +0.49% |
| Chemicals: Major Diversified | 1 | 100.0% | -0.36% | -0.36% |
| Tools & Hardware | 3 | 33.3% | -0.37% | -0.14% |
| Regional Banks | 34 | 11.8% | -0.38% | -0.20% |
| Air Freight/Couriers | 9 | 33.3% | -0.41% | -0.76% |
| Building Products | 4 | 50.0% | -0.41% | +0.68% |
| Metal Fabrication | 2 | 0.0% | -0.48% | -0.48% |
| Investment Banks/Brokers | 24 | 25.0% | -0.52% | -0.47% |
| Oil Refining/Marketing | 5 | 0.0% | -0.57% | -0.71% |
| Investment Trusts/Mutual Funds | 2 | 0.0% | -0.64% | -0.64% |
| Auto Parts: OEM | 4 | 50.0% | -0.69% | -0.53% |
| Trucking | 6 | 16.7% | -0.69% | -0.62% |
| Aerospace & Defense | 28 | 14.3% | -0.75% | -0.42% |
| Commercial Printing/Forms | 1 | 100.0% | -1.10% | -1.10% |
| Industrial Machinery | 25 | 36.0% | -1.44% | -0.94% |
| Trucks/Construction/Farm Machinery | 5 | 20.0% | -1.64% | -1.31% |
| Steel | 8 | 0.0% | -1.67% | -0.89% |
| Telecommunications Equipment | 8 | 50.0% | -1.72% | -0.42% |
| Precious Metals | 13 | 0.0% | -1.72% | -1.63% |
| Engineering & Construction | 9 | 33.3% | -1.74% | -1.23% |
| Financial Conglomerates | 6 | 0.0% | -2.45% | -1.71% |
| Electronic Equipment/Instruments | 4 | 0.0% | -2.85% | -2.72% |
| Electrical Products | 8 | 12.5% | -3.96% | -3.33% |
| Other Metals/Minerals | 7 | 0.0% | -4.09% | -3.98% |
| Specialty Telecommunications | 2 | 0.0% | -4.33% | -4.33% |
| Alternative Power Generation | 1 | 0.0% | -4.70% | -4.70% |
| Electronics Distributors | 1 | 0.0% | -6.15% | -6.15% |
| Agricultural Commodities/Milling | 2 | 0.0% | -6.20% | -6.20% |
| Electronic Components | 4 | 0.0% | -6.35% | -6.25% |
| Computer Peripherals | 7 | 14.3% | -6.52% | -7.23% |
| Semiconductors | 33 | 0.0% | -7.84% | -8.36% |
| Electronic Production Equipment | 4 | 0.0% | -8.13% | -7.84% |
| Computer Processing Hardware | 7 | 14.3% | -8.75% | -7.79% |

## Flags

- **All nine branches are complete** (`rows_kept == rows_passing` on every branch) and no branch landed on a cap (30 / 50 / 60 / 200), so no book was truncated. 1,668 screened rows → 1,378 distinct candidates.
- **The book is one factor.** 11 of the 12 Focus names and 7 of the 8 Tier-A names are semiconductor / AI hardware. The screens reacted to one unwind, not to the market.
- **Tier-A is 0 fresh / 8 extended** — seven of the eight on ATR% alone, and KYMR trips three of the four rules. Nothing was dropped for tripping the label.
- **Volatility source.** The Cboe delayed-quote CDN answered **HTTP 403** (Cloudflare) from this egress, so the pair was read from the **Yahoo chart-API fallback**, both symbols from the same 2026-11-24 session bar, quoted at **16:15:01 ET**. One pair, used everywhere in this document.
- **The +34.94 pp divergence is BROAD by construction** — 34.94% of the large-cap universe above its own 20-DMA against 0% of the index ETFs. It measures how far the trend structure lags the tape, not a disagreement between two sources.
- **shibui is T+1.** The context screens describe **2026-11-23**; the trigger screens and this breadth read describe **2026-11-24**. The two sessions are never blended.
- **Volume, not panic.** NVDA printed RVOL 0.81, CRWV 0.70, NBIS 0.70 — the AI unwind happened on light volume, while the day's gainers (retail, biotech) carried real expansion.
- **Concentration risk in the movers table.** The decliner list is one theme: ADI, HPE, ALAB, SITM, MTSI, CRDO, FN. Computer Processing Hardware averaged **-8.75%** and Electronic Production Equipment **-8.13%**, both with 0% of names above their 20-DMA.
- **Sector breadth confirms the rotation, not a market decline.** Biotechnology 83.3% above its 20-DMA, Pharmaceuticals: Major 76.7%, Discount Stores 66.7% — against Semiconductors at **0%**.

## Method, source health & caveats

### Method

- **The dual book.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) ran on **2026-11-24's own settled bar** from the TradingView scanner. The multi-session CONTEXT screens (5-day gainers/losers, the 14-day velocity, the coil, the 252-session RS window) stay on shibui's **2026-11-23** session and are labelled T+1. Every row publishes `data_as_of` + `source` (`fresh` / `t1` / `fresh+t1`); the two are never blended.
- **Volume basis.** The scanner publishes no prior-session volume, so the expansion test runs against the prior-**nine**-session mean, reconstructed as `(10 × average_volume_10d_calc − volume_today) / 9` — a stricter gate than shibui's "volume > prev_session", published as its own gate. The 5-session move stays on shibui's `m1` because TradingView's `Perf.W` is a **six**-session measure (r = 0.997 against a six-session move, 0.924 against five).
- **Close convention.** The official 16:00 ET print. TradingView's `close` equals Nasdaq's `secondaryData`; `primaryData` is the after-hours print and is **not** used.
- **Coverage.** 1,668 screened rows across 9 branches → 1,378 distinct candidates. `rows_kept == rows_passing` on all nine branches; no branch landed on 30 / 50 / 60 / 200, so no book was truncated.
- **Quality overlay.** 1,188 symbols queried; 721 `fail`, 355 `pass`, 112 `unknown` (no trailing earnings — **disclosed, not counted as a red flag**). A flag never removes a name from the book.

### Caveats

- **A one-complex unwind is not a market view.** The Nasdaq fell 1.48% while the median large cap rose 0.45%; read the index as the AI complex, not as the market's verdict.
- **"Extended" is a label, not a filter.** All 8 Tier-A names carry it and none was dropped; seven trip it on ATR% alone, which fires on 15.8% of the $10B+ universe by itself.
- **The catalyst is single-stock on both sides.** ADI's guide and HPE's margin outlook drove the two largest decliners, and Sanofi's Insmed acquisition drove the largest biotech move — index-level reads of today inherit those single-name shocks.
- **Not verified:** no intraday path, no option-chain or flow confirmation, no independent per-name catalyst check for the Focus names, and the theme branch's leader selection is published as-is from the screen.
- **The screen's context numbers are one session stale** (shibui 2026-11-23). The fresh book is the primary; the T+1 book is the cross-check, and where they disagree the artifact publishes both rather than substituting one.
