---
artifact: breadth
contract: SWEEP_PIPELINE_V1
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "18:30 ET (2026-11-23)"
data_date: "2026-11-23 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-20)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1070 names; totalCount 1070 = rows fetched, no truncation"
vix_quote_time: "2026-11-23 16:15:01 ET (Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-19; both symbols read from the same session bar, 1 pull(s) 0 s apart — identical)"
vix_pair: "VIX 26.62 / VIX3M 25.5 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-23/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
---

# Breadth & Regime — End-of-Day — Monday 23 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-23. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1 = 2026-11-20) and are not blended into this file.

## TL;DR

**924 of 1,070 large caps advanced on 2026-11-23 and the median name was +2.34%, yet only 31.50% of them are above their own 20-DMA and not one of the five index ETFs is.** That is not a contradiction — it is the signature of a V-shaped bounce off a washout low: Nvidia's reinstatement of Jensen Huang as CEO (8-K pre-bell) triggered a violent relief rally (NVDA +31.48%, QQQ +7.00%, SPY +4.71%) and the VIX collapsed 25.8% to 26.62 from Friday's 35.89 close, but the trend structure is still broken — QQQ remains -8.28% below its 50-DMA and the S&P is still in correction. The advance/decline tally (broad participation in the tape) and the percentage-above-20-DMA (broken trend) are measuring different things and disagree **on purpose**. Volatility is calmer but not calm: VIX 26.62 / VIX3M 25.50 = **1.0439**, so `uncertainty` stays on. Regime: size cut **ON** (50), index below its 20-DMA, not late cycle.

## Breadth — 2026-11-23 settled session

| Metric | Value |
|---|---|
| Universe | 1070 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **31.50%** (337 / 1070) |
| Above 50-DMA | 42.06% (450 / 1070) |
| Above 200-DMA | 41.03% (439 / 1070) |
| Advance / decline / unchanged | **924 / 141 / 5** — ratio 6.55, net **+783** |
| Median name | +2.34%  ·  mean +3.21% |
| Move distribution | ≥ +5%: 226 · +2..5%: 377 · 0..2%: 326 · −2..0: 114 · −5..−2: 24 · ≤ −5%: 3 |

## Participation — the advance/decline tally

Computed on the **same 1070-name population** as the breadth percentage, from the settled session: **924 advancing, 141 declining, 5 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **+783**, ratio **6.55**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+31.50 pp** |
| band | **BROAD** |
| large-cap % above 20-DMA | 31.50% |
| index ETFs above their 20-DMA | 0% (0 of 5) |

A **BROAD** divergence: the average large cap is materially healthier than the index - participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 722.29 | +4.71% | 745.65 | 759.41 | 732.91 | **-4.89%** | 2.13% |
| QQQ | 651.03 | +7.00% | 675.47 | 709.79 | 683.27 | **-8.28%** | 3.22% |
| RSP | 212.82 | +2.59% | 217.86 | 214.75 | 209.28 | **-0.90%** | 1.58% |
| IWM | 265.74 | +3.56% | 275.66 | 277.82 | 279.57 | **-4.35%** | 2.16% |
| QQQE | 110.62 | +4.94% | 114.58 | 117.66 | 113.87 | **-5.98%** | 2.37% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at -0.90%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **26.62** | 35.89 | -9.27 (-25.8%) | 2026-11-23 16:15:01 ET |
| VIX3M | **25.5** | 30.94 | -5.44 (-17.6%) | 2026-11-23 16:15:01 ET |

Source: Yahoo chart API (^VIX / ^VIX3M) - FALLBACK: the Cboe delayed-quote CDN returned HTTP 403 (Cloudflare) from this egress on 2026-11-19; both symbols read from the same session bar. Pulled 1 time(s), 0 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **1.0439** → `uncertainty: true` (the flag fires above 1.0).

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **50** | size cut is ON - the index is below its 20-DMA and breadth 31.50% is UNDER the 40% trigger |
| `uncertainty` | **true** | the flag fires when VIX/VIX3M > 1.0; the ratio is 1.0439 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max -0.90%, RSP) |
| `index_below_20sma` | **true** | only 0 of 5 index ETFs are above their 20-DMA (0%) |

Payload: `daily-screens/2026-11-23/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Industry breadth (the breadth universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Semiconductors | 33 | 15.2% | +14.01% | +14.89% |
| Electronic Production Equipment | 4 | 0.0% | +13.95% | +13.06% |
| Computer Processing Hardware | 8 | 12.5% | +12.77% | +12.97% |
| Electronic Components | 4 | 0.0% | +10.36% | +10.44% |
| Alternative Power Generation | 1 | 100.0% | +9.58% | +9.58% |
| Computer Peripherals | 7 | 14.3% | +9.51% | +9.73% |
| Electrical Products | 8 | 25.0% | +8.13% | +7.63% |
| Other Metals/Minerals | 7 | 14.3% | +6.96% | +7.45% |
| Electronics Distributors | 1 | 0.0% | +6.82% | +6.82% |
| Electronic Equipment/Instruments | 5 | 0.0% | +6.81% | +5.13% |
| Specialty Telecommunications | 3 | 0.0% | +6.47% | +4.74% |
| Precious Metals | 13 | 0.0% | +6.38% | +6.39% |
| Industrial Machinery | 25 | 40.0% | +6.30% | +5.25% |
| Engineering & Construction | 9 | 66.7% | +6.24% | +7.65% |
| Telecommunications Equipment | 8 | 37.5% | +6.23% | +5.70% |
| Electronics/Appliances | 1 | 100.0% | +5.99% | +5.99% |
| Airlines | 5 | 40.0% | +5.57% | +5.37% |
| Packaged Software | 56 | 30.4% | +5.54% | +4.53% |
| Trucks/Construction/Farm Machinery | 6 | 16.7% | +5.51% | +5.34% |
| Biotechnology | 16 | 43.8% | +5.32% | +3.33% |
| Chemicals: Major Diversified | 2 | 100.0% | +5.20% | +5.20% |
| Auto Parts: OEM | 5 | 40.0% | +5.12% | +5.06% |
| Financial Conglomerates | 6 | 0.0% | +5.00% | +4.91% |
| Metal Fabrication | 2 | 50.0% | +4.86% | +4.86% |
| Home Furnishings | 1 | 0.0% | +4.72% | +4.72% |
| Motor Vehicles | 9 | 22.2% | +4.69% | +3.72% |
| Pharmaceuticals: Other | 1 | 0.0% | +4.34% | +4.34% |
| Construction Materials | 6 | 33.3% | +4.23% | +4.10% |
| Department Stores | 1 | 100.0% | +4.13% | +4.13% |
| Information Technology Services | 17 | 5.9% | +3.96% | +2.07% |
| Wholesale Distributors | 9 | 11.1% | +3.78% | +4.56% |
| Internet Retail | 7 | 0.0% | +3.73% | +3.47% |
| Aerospace & Defense | 28 | 17.9% | +3.70% | +3.44% |
| Steel | 8 | 0.0% | +3.69% | +3.61% |
| Industrial Conglomerates | 1 | 100.0% | +3.62% | +3.62% |
| Investment Managers | 38 | 28.9% | +3.52% | +3.62% |
| Apparel/Footwear | 5 | 0.0% | +3.51% | +3.40% |
| Investment Banks/Brokers | 24 | 12.5% | +3.45% | +3.49% |
| Hotels/Resorts/Cruise lines | 9 | 55.6% | +3.26% | +2.44% |
| Miscellaneous Commercial Services | 15 | 33.3% | +3.24% | +3.41% |
| Internet Software/Services | 19 | 26.3% | +3.20% | +2.82% |
| Tools & Hardware | 3 | 66.7% | +3.20% | +3.08% |
| Movies/Entertainment | 3 | 66.7% | +3.11% | +3.38% |
| Recreational Products | 2 | 0.0% | +2.97% | +2.97% |
| Finance/Rental/Leasing | 16 | 12.5% | +2.91% | +2.46% |
| Industrial Specialties | 3 | 66.7% | +2.85% | +2.86% |
| Major Banks | 85 | 37.6% | +2.76% | +2.99% |
| Medical Specialties | 33 | 51.5% | +2.75% | +2.77% |
| Marine Shipping | 1 | 0.0% | +2.74% | +2.74% |
| Life/Health Insurance | 9 | 33.3% | +2.65% | +2.32% |
| Advertising/Marketing Services | 1 | 100.0% | +2.51% | +2.51% |
| Containers/Packaging | 5 | 0.0% | +2.50% | +1.75% |
| Data Processing Services | 7 | 28.6% | +2.46% | +2.26% |
| Financial Publishing/Services | 7 | 14.3% | +2.36% | +2.78% |
| Hospital/Nursing Management | 3 | 0.0% | +2.27% | +2.17% |
| Restaurants | 10 | 70.0% | +2.26% | +1.98% |
| Home Improvement Chains | 2 | 100.0% | +2.23% | +2.23% |
| Food Distributors | 2 | 100.0% | +2.18% | +2.18% |
| Pharmaceuticals: Major | 29 | 37.9% | +2.16% | +1.65% |
| Air Freight/Couriers | 9 | 44.4% | +2.10% | +2.18% |
| Broadcasting | 3 | 33.3% | +2.02% | +2.12% |
| Pharmaceuticals: Generic | 1 | 0.0% | +1.91% | +1.91% |
| Regional Banks | 33 | 21.2% | +1.88% | +1.92% |
| Services to the Health Industry | 1 | 100.0% | +1.87% | +1.87% |
| Real Estate Development | 3 | 33.3% | +1.86% | +2.06% |
| Multi-Line Insurance | 25 | 52.0% | +1.73% | +1.98% |
| Environmental Services | 5 | 40.0% | +1.70% | +1.11% |
| Contract Drilling | 2 | 0.0% | +1.67% | +1.67% |
| Electric Utilities | 41 | 53.7% | +1.64% | +1.16% |
| Homebuilding | 6 | 0.0% | +1.55% | +1.33% |
| Chemicals: Specialty | 6 | 33.3% | +1.54% | +2.60% |
| Other Consumer Services | 4 | 25.0% | +1.38% | +1.67% |
| Real Estate Investment Trusts | 67 | 41.8% | +1.36% | +1.46% |
| Trucking | 5 | 0.0% | +1.35% | +1.89% |
| Railroads | 5 | 0.0% | +1.21% | +1.23% |
| Other Transportation | 3 | 33.3% | +1.16% | +0.94% |
| Medical/Nursing Services | 8 | 12.5% | +1.11% | +1.27% |
| Wireless Telecommunications | 14 | 64.3% | +1.00% | +0.21% |
| Agricultural Commodities/Milling | 2 | 0.0% | +0.97% | +0.97% |
| Publishing: Newspapers | 3 | 0.0% | +0.92% | +1.51% |
| Chemicals: Agricultural | 2 | 0.0% | +0.91% | +0.91% |
| Oilfield Services/Equipment | 2 | 0.0% | +0.80% | +0.80% |
| Specialty Stores | 15 | 53.3% | +0.74% | +1.05% |
| Electronics/Appliance Stores | 2 | 50.0% | +0.72% | +0.72% |
| Apparel/Footwear Retail | 4 | 50.0% | +0.69% | +0.71% |
| Household/Personal Care | 7 | 57.1% | +0.61% | +0.03% |
| Building Products | 4 | 50.0% | +0.57% | +2.23% |
| Casinos/Gaming | 2 | 50.0% | +0.54% | +0.54% |
| Gas Distributors | 6 | 16.7% | +0.49% | +0.30% |
| Specialty Insurance | 1 | 100.0% | +0.46% | +0.46% |
| Food: Specialty/Candy | 7 | 71.4% | +0.45% | -0.05% |
| Discount Stores | 3 | 66.7% | +0.42% | +0.83% |
| Major Telecommunications | 2 | 100.0% | +0.40% | +0.40% |
| Property/Casualty Insurance | 15 | 60.0% | +0.34% | +0.41% |
| Cable/Satellite TV | 4 | 75.0% | +0.34% | +0.19% |
| Oil & Gas Pipelines | 14 | 0.0% | +0.17% | +0.07% |
| Commercial Printing/Forms | 1 | 100.0% | +0.12% | +0.12% |
| Water Utilities | 3 | 0.0% | +0.04% | -1.48% |
| Insurance Brokers/Services | 6 | 83.3% | -0.06% | -0.13% |
| Pulp & Paper | 3 | 0.0% | -0.23% | +1.65% |
| Publishing: Books/Magazines | 1 | 0.0% | -0.24% | -0.24% |
| Beverages: Non-Alcoholic | 6 | 0.0% | -0.34% | -0.01% |
| Tobacco | 3 | 0.0% | -0.51% | -0.86% |
| Medical Distributors | 3 | 66.7% | -0.88% | -0.35% |
| Integrated Oil | 22 | 0.0% | -1.20% | -1.35% |
| Oil Refining/Marketing | 5 | 0.0% | -1.25% | -0.93% |
| Managed Health Care | 6 | 0.0% | -1.33% | -0.92% |
| Beverages: Alcoholic | 6 | 0.0% | -1.45% | -1.53% |
| Drugstore Chains | 1 | 0.0% | -1.47% | -1.47% |
| Food: Major Diversified | 2 | 100.0% | -1.51% | -1.51% |
| Oil & Gas Production | 5 | 0.0% | -1.77% | -1.45% |
| Food Retail | 1 | 0.0% | -1.88% | -1.88% |
| Food: Meat/Fish/Dairy | 4 | 50.0% | -1.92% | -2.26% |
| Investment Trusts/Mutual Funds | 2 | 0.0% | -2.15% | -2.15% |

## Flags

- **`D_qullamaggie_ep` returned 0 rows.** It also returned 0 on 2026-11-19 and 2026-11-20, so this is a persistently empty screen on this universe and not today's truncation — but it is disclosed rather than hidden, and the branch is counted as complete (0 passed = 0 kept).
- **Volatility source.** The Cboe delayed-quote CDN answered **HTTP 403** from this egress, so the pair was read from the **Yahoo chart-API fallback**, both symbols from the same 2026-11-23 session bar, quoted at **16:15:01 ET**. One pair, used everywhere in this document.
- **The +31.50 pp divergence is BROAD by construction** — 0% of index ETFs above their 20-DMA against 31.50% of the large-cap universe above theirs. It measures how far the trend structure lags the tape; it is not a disagreement between two sources.
- **shibui is T+1.** The cross-check rows describe **2026-11-20** (QQQ -14.42% vs its 50-DMA); the published numbers describe **2026-11-23** (QQQ -8.28%). The two sessions are never blended.
- **Concentration risk in the movers table.** The top of the large-cap gainer list is dominated by one theme: NVDA, KYMR, ALAB, CRDO, CRWV, SITM, ASX, DELL, NBIS, SKHY, UMC, MU, MRVL, TSM, ASML. Semiconductors averaged +14.01% today — and only 15.15% of them are above their own 20-DMA.
- **CrowdStrike (CRWD) closed -8.92%** on a day the Nasdaq rose 6.5%: the rally was not a blanket software bid, and the single largest decliner in the $10B+ universe is a software name.
- **All nine branches are complete** (`rows_kept == rows_passing`) and no branch landed on a cap; every one of the 1,477 candidates publishes its own `data_as_of` + `source`.

## Method, source health & caveats

### Method

- **The dual book.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) ran on **2026-11-23's own settled bar** from the TradingView scanner. The multi-session CONTEXT screens (5-day gainers/losers, the 14-day velocity, the coil, the 252-session RS window) stay on shibui's **2026-11-20** session and are labelled T+1. Every row publishes `data_as_of` + `source` (`fresh` / `t1` / `fresh+t1`); the two are never blended.
- **Volume basis.** The scanner publishes no prior-session volume, so the expansion test runs against the prior-**nine**-session mean, reconstructed as `(10 × average_volume_10d_calc − volume_today) / 9` — a stricter gate than shibui's "volume > prev_session", published as its own gate. The 5-session move stays on shibui's `m1` because TradingView's `Perf.W` is a **six**-session measure (r = 0.997 against a six-session move, 0.924 against five).
- **Close convention.** The official 16:00 ET print. TradingView's `close` equals Nasdaq's `secondaryData`; `primaryData` is the after-hours print and is **not** used.
- **Coverage.** 1,952 screened rows across 9 branches → 1,477 distinct candidates. `rows_kept == rows_passing` on all nine branches; no branch landed on 30 / 50 / 60 / 200, so no book was truncated.
- **Quality overlay.** 1,002 symbols queried; 598 `fail`, 321 `pass`, 83 `unknown` (no trailing earnings — **disclosed, not counted as a red flag**), 475 with no overlay row. A flag never removes a name from the book.

### Caveats

- **A bounce is not a trend repair.** 31.50% above the 20-DMA with 0 of 5 index ETFs above theirs is the honest state of the tape after a violent relief rally; the size-cut flag is ON for that reason.
- **The catalyst is single-stock.** One 8-K from one board produced a large share of today's index move. Any read of today's tape is heavily conditioned on it.
- **Not verified:** no intraday path, no option-chain or flow confirmation, and no independent per-name catalyst check for the Focus names — the theme branch's leader selection is published as-is from the screen.
- **The screen's context numbers are one session stale** (shibui 2026-11-20). The fresh book is the primary; the T+1 book is the cross-check, and where they disagree the artifact publishes both rather than substituting one.
