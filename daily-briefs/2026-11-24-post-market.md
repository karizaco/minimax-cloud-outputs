---
date: 2026-11-24
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:21-22:35
session: 467042785964127
scheduled_at_ms: 1795577404057
status: ok
source: MCP-over-HTTP bridge (market-recap: get_quotes, price_history, top_movers) - TradingView scanner (after-hours, universe) - cron #20 us-eod/2026-11-24.csv (participation + sector universe) - CBOE daily statistics page and dated VIX/VXN history files - watchlist.yaml - issuer IR and press (StockTitan, Benzinga, Reuters, Bloomberg, CNBC, Market Chameleon, GuruFocus) - calendar vendors (ATLAS, EarningsWhispers, Digrin, Nexqual, MarketChameleon, RapidTradeView, OpenCapital) - Macro Bullseye / FRC / Wells Fargo / Schwab for the economic calendar
primary_source: bridge market-recap get_quotes and price_history (Yahoo-sourced, cross-checked against CNBC by the bridge's own agreement block)
universe: cron #20 us-eod/2026-11-24.csv - 4,878 rows, 4,848 priced names, 4,420 cap-weighted-eligible names after de-duplication and flag exclusions
degraded_sources: 1
---

# Post-market brief — Tuesday, 24 November 2026

## TL;DR

Monday's Huang-reinstatement rally unwound in one session: the S&P 500 fell 0.50%, the Nasdaq 1.48% and the PHLX Semiconductor index 7.88%, giving back 64% of Monday's gain, while the Dow added 0.85% and the Russell 2000 added 0.57%. The index was down but the median stock was not — median_name_move_pct was **+0.10%**, with **2,547 advancers** against **2,152 decliners** (149 unchanged), and SPY -0.49% versus RSP +0.54% is a **cap_weight_penalty_bp of -102**. In the liquid set (market cap above $2B), liquid_adv_dec_ratio was **1.29** (992 advancers : 768 decliners): a narrow, mega-cap-led tape, with the damage concentrated in semiconductors (MU -11.01%, AMD -8.86%, INTC -8.15%, NVDA -5.86%) and the landing place being health care (cap-weighted +3.07%, median +2.82%). Tomorrow is a macro day, not an earnings day: 8:30 ET brings October PCE, the Q3 GDP second estimate, durable goods and claims, with the 2:00 ET Beige Book behind it — and the overnight is already pointing down, with the Taiex -6.32%, the Kospi -5.92% and ES futures -0.29% against the cash index close.

## Tomorrow's setup — Wednesday, 25 November 2026

### Futures and the overnight setup

Every futures row below was stamped `as_of` 22:21 ET — nine minutes before the fire — so this is the live Globex session, not a stale settlement. The change is published against **both** denominators: the prior settle, and the cash index close (the number that answers "did the overnight extend the session's move?").

| Contract | Last | vs prior settle | vs cash index close | as_of (ET) | Globex range |
|---|---|---|---|---|---|
| ES=F (S&P 500 E-mini) | 7,180.50 | -0.51% (settle 7,217.50) | **-0.29%** (^GSPC 7,201.09) | 22:21 | 7,160.25 – 7,224.00 |
| NQ=F (Nasdaq-100) | 26,024.25 | -0.96% (settle 26,275.75) | -0.72% (^NDX 26,214.17) | 22:21 | 25,905.25 – 26,350.75 |
| YM=F (Dow E-mini) | 49,912 | -0.30% (settle 50,061) | -0.21% (^DJI 50,018.70) | 22:21 | 49,817 – 50,060 |
| RTY=F (Russell 2000) | 2,679.10 | -0.38% (settle 2,689.30) | -0.22% (^RUT 2,684.94) | 22:21 | 2,672.60 – 2,690.10 |
| ZN=F (10-year note) | 106.875 | +0.01% (settle 106.859) | n/a | 22:21 | 106.6875 – 106.90625 |
| GC=F (gold) | 3,555.90 | -0.17% (settle 3,561.90) | n/a | 22:21 | 3,532.40 – 3,573.90 |
| CL=F (WTI crude) | 80.91 | -1.39% (settle 82.05) | n/a | 22:21 | 80.64 – 81.86 |

**Read:** against the settle the overnight looks like another down day (-0.51%); against the cash index close it is **-0.29%**, roughly 60% of the session's -0.50% fall. The Globex session faded 0.8% from 7,224.00 to 7,160.25 and has recovered about 0.28% off that low. Futures are not carrying a fresh leg down — they are carrying the session's own loss into Wednesday.

**The Asia cash leg is the worse half of the overnight**, and each level carries its own stamp because these are live, moving numbers:

| Asian index | Level | Change | as_of (ET) | Session range |
|---|---|---|---|---|
| Taiex (^TWII) | 37,586.64 | **-6.32%** | 22:12 | 36,681.90 – 39,983.91 |
| Kospi (^KS11) | 4,709.53 | **-5.92%** | 22:12 | 4,687.51 – 4,823.36 |
| Nikkei 225 (^N225) | 56,710.43 | **-3.30%** | 21:35 | 56,502.97 – 58,472.56 |
| Shanghai Composite (000001.SS) | 3,513.90 | -0.97% | 22:17 | 3,508.39 – 3,526.34 |
| Hang Seng (^HSI) | 22,348.39 | +0.58% | 22:17 | 22,252.81 – 22,507.83 |
| Straits Times (^STI) | 4,952.61 | -0.13% | 22:17 | 4,920.48 – 4,958.06 |

Reuters and Bloomberg attribute the Asian move to the same AI-trade doubts that hit Wall Street plus fresh US tariff threats; the Taiex has been as much as 8.6% lower and the Kospi as much as 5.8% lower intraday. The Nikkei stamp is 21:35 ET, ~40 minutes older than the others.

**Gold: publish both legs, never blend them.** GLD closed **-2.27%** at 325.45 and its after-hours print at 22:35 ET is **325.20 (-0.08%)**, while the gold future is 3,555.90, **-0.17%** against the 3,561.90 settle and trading between 3,532.40 and 3,573.90. The ETF's thin after-hours book is repricing lazily while the future trades continuously — treat the future as the overnight signal and the ETF as the session leg. Neither number is wrong.

### Economic calendar

| Time (ET) | Release | Consensus | Previous |
|---|---|---|---|
| 7:25 | Bowman speaks (pre-recorded, FOMC voter) | — | — |
| 8:30 | **Personal income and spending — PCE inflation, October** (core MoM +0.3%, core YoY 3.2%; headline MoM +0.3%, YoY 3.8%) | core MoM +0.3%, core YoY 3.2%, headline MoM +0.3%, YoY 3.8% | core MoM +0.3%, core YoY 3.1%, headline MoM +0.5%, YoY 3.6% |
| 8:30 | **GDP, second estimate, Q3** | 3.5% annualised | 3.4% |
| 8:30 | Durable goods orders, October | +0.4% MoM (ex-transport +0.5%) | +1.9% MoM |
| 8:30 | Initial jobless claims, week ending 21 Nov | 200K | 203K |
| 10:00 | New home sales, October | 0.65M | 0.676M |
| 11:30 | 7-year Treasury note auction | — | — |
| 1:00 | Baker Hughes rig count | — | — |
| 2:00 | **Fed Beige Book** | — | — |

The core PCE YoY consensus of 3.2% (from 3.1%) is the line that matters: the selloff narrative all session has been "December rate hike worries" after Monday's melt-up, and the Beige Book at 2:00 ET is the second chance to reprice it. Tomorrow is also the **last full session before Thanksgiving** (26 November; 27 November is an early close), so expect thin volume into PCE.

### Earnings calendar

Vendors disagree sharply on the count for Wednesday 25 November: ATLAS 27, EarningsWhispers 29, Digrin 65, Nexqual 10, MarketChameleon 15, RapidTradeView 17, OpenCapital 14. The roster below is the **intersection of two or more vendors**; anything one vendor carries alone is not published as scheduled.

| Ticker | Company | When | EPS estimate |
|---|---|---|---|
| DE | Deere & Company | before the open | $4.03 – $4.17 |
| LI | Li Auto | before the open | -$0.08 to -$0.84 (vendors disagree) |
| BZ | Kanzhun | before the open | $0.11 – $2.24 (vendors disagree) |
| GDS | GDS Holdings | before the open | -$1.28 |
| HDL | Super Hi International | before the open | $0.01 (after the close at one vendor) |
| IMKTA | Ingles Markets | before the open | n/a |
| OMSE | OMS Energy Technologies | before the open | n/a |
| GASS | StealthGas | before the open | $0.39 – $0.43 |
| DSX | Diana Shipping | before the open | $0.08 – $0.10 |
| NNOX | Nano-X Imaging | before the open | -$0.14 to -$0.15 |
| PSNY | Polestar Automotive | before the open | -$1.80 to -$2.42 |
| BMA | Banco Macro | after the close | $1.44 – $1.59 |
| FINV | FinVolution | after the close | n/a |

Deere is the only mega-cap on the board; the EPS estimates for BZ and LI differ across vendors by an order of magnitude, so treat the numbers as indicative only.

### News to watch for the top movers

| Ticker | Close | Move | The news |
|---|---|---|---|
| EMBC | 8.08 | **+40.64%** | Fiscal Q4 revenue +13.1% to $298.7M; initial fiscal 2027 outlook given |
| AMTM | 24.80 | **+20.10%** | Fiscal 2026 revenue $13.8B (-4%); fiscal 2027 outlook $13.8–14.05B; first buyback authorised, up to $500M |
| ANF | 168.10 | **+19.69%** | Record Q3 net sales $1.4B (+11%); FY26 EPS outlook raised to $13.70–$13.90 |
| KSS | 25.33 | +19.48% | Q3 net sales +1.3% to $3.5B; full-year outlook raised (EPS $2.15 includes a $1.16 tax benefit) |
| COGT | 33.01 | +17.43% | FDA approved Ekitna (advanced GIST, post-imatinib) at 9:27 ET |
| INSM | 170.15 | +14.13% | Sanofi agreed to buy it for $175/share in cash, about $41.0B in total; close expected in H1 2027 |

### Tomorrow's three things to watch

- GDS — 13.79 close, 14.03 after-hours — reports before the open with EPS estimated at -$1.28; the data-centre landlord is the cleanest overnight read on the AI capex that broke today, and it is already +1.75% in the after-hours session.
- DELL — 295.28 close, 297.98 after-hours, range 287–313 — record Q3 revenue of $54.9B and a $132.3B AI backlog reported tonight; the market has already faded it from 313, so tomorrow's open prices AI demand against a tape that just sold the trade for two days.
- AMBA — 27.77 after-hours, -37.55%, low 24.33 — Q4 revenue guided to $70–75M against $115.2M in Q3, with management naming rising memory prices as the cause; the read-through to embedded and edge-AI names at the open is the day's first real test of the chip unwind.

## Day's tape

### Market read

The participation read, on one population — cron #20's `us-eod/2026-11-24.csv` (4,848 priced names).

| metric | value | where it comes from |
|---|---|---|
| advancers | 2,547 | cron #20 universe, `change_pct` > 0 |
| decliners | 2,152 | cron #20 universe, `change_pct` < 0 |
| unchanged | 149 | cron #20 universe, `change_pct` = 0 |
| median_name_move_pct | **+0.10%** | cron #20 universe, median `change_pct` of 4,848 priced names |
| cap_weight_penalty_bp | **-102** | bridge `price_history`: SPY -0.486% − RSP +0.536% |
| liquid_adv_dec_ratio | **1.29** (992 adv : 768 dec) | cron #20 universe, market cap above $2B (1,772 names) |

**Read:** the index was down and the median stock was up. A -102bp cap-weight penalty is the single cleanest number in the tape: the average mega-cap lost roughly 1% more than the average small-cap, and the entire index loss is the semiconductor complex plus two mega-caps. The liquid set's 1.29 ratio confirms it was not a broad flight to safety — capital rotated *within* the market, into health care, staples, energy and retail, and out of semiconductors.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-18 | -0.306 | -0.153 | -15 |
| 2026-11-19 | -1.962 | -1.764 | -20 |
| 2026-11-20 | -3.640 | -1.980 | -166 |
| 2026-11-23 | +4.709 | +2.594 | +212 |
| 2026-11-24 | -0.486 | +0.536 | **-102** |

The penalty has flipped sign every session this week: +212bp on Monday's melt-up, -102bp on Tuesday's reversal. Two days of mean reversion inside the AI complex, not a change of regime.

### Index, ETF and volatility levels

| Instrument | Close / level | Change | as_of (ET) |
|---|---|---|---|
| S&P 500 (^GSPC) | 7,201.09 | -0.50% | 16:54 |
| Nasdaq Composite (^IXIC) | 23,733.54 | -1.48% | 17:15 |
| Nasdaq 100 (^NDX) | 26,214.17 | -1.99% | 17:15 |
| Dow (^DJI) | 50,018.70 | +0.85% | 16:54 |
| Russell 2000 (^RUT) | 2,684.94 | +0.57% | 16:30 |
| PHLX Semiconductor (^SOX) | 8,832.50 | **-7.88%** | 17:15 |
| SPY | 718.78 | -0.49% | 16:00 |
| QQQ | 638.10 | -1.99% | 16:00 |
| IWM | 267.14 | +0.53% | 16:00 |
| DIA | 499.74 | +0.79% | 16:00 |
| RSP | 213.96 | +0.54% | 16:00 |
| SMH | 426.75 | -7.26% | 16:00 |
| GLD | 325.45 | -2.27% | 16:00 |
| TLT | 81.49 | -0.24% | 16:00 |
| VIX | 26.36 | -0.98% | 16:15 |
| VXN | 36.42 | **+0.30%** | 16:15 |

The volatility indices are read from the bridge's **dated** history (`price_history`) and cross-checked against CBOE's own dated close files, which agree to the cent: VIX 26.36 and VXN 36.42 for 24 November. The bridge's *quote* row for ^VXN carried the 23 November reading (36.31, -19.76%) with a stale `as_of`, while every other symbol in the same call was current — the dated history is what is published here, and the stale quote row was discarded, not published.

**Put/call: total 0.95 for the session dated 2026-11-24** (CBOE daily statistics, `selectedDate` = 2026-11-24, `prevTradingDay` = 2026-11-24). From the same payload: index 1.12, equity 0.57, ETP 1.13, VIX 0.90, SPX+SPXW+SPXO 1.15, XSP 1.37. No component split is published that is not in that payload.

Note the volatility paradox worth holding overnight: **VIX fell 0.98% and VXN rose 0.30% on a day the chip complex lost 8%** — because the damage was concentrated, not systemic. The 2,547-against-2,152 breadth supports the same read.

### Cross-asset

| Instrument | Last | Change | Note |
|---|---|---|---|
| Gold future (GC=F) | 3,555.90 | -0.17% vs settle | range 3,532.40–3,573.90; the ETF's AH print is far lazier (GLD 325.20, -0.08%) |
| WTI crude (CL=F) | 80.91 | -1.39% vs settle | range 80.64–81.86 |
| 10-year note (ZN=F) | 106.875 | +0.01% | unchanged despite the rate-hike narrative |
| Dollar index (DX-Y.NYB) | 103.91 | +0.09% | |

### Day's movers

Bridge-verified regular-session closes, market cap above $2B.

| Ticker | Close | Move | Driver |
|---|---|---|---|
| EMBC | 8.08 | +40.64% | FQ4 revenue +13.1% to $298.7M; initial FY27 outlook |
| AMTM | 24.80 | +20.10% | FY26 revenue $13.8B; FY27 outlook $13.8–14.05B; $500M buyback |
| ANF | 168.10 | +19.69% | record Q3 net sales $1.4B (+11%); FY26 EPS raised to $13.70–$13.90 |
| KSS | 25.33 | +19.48% | Q3 sales +1.3% to $3.5B; FY outlook raised |
| COGT | 33.01 | +17.43% | FDA approval of Ekitna |
| SHOE | 11.58 | -18.39% | Q3 net sales $280.0M (from $297.2M); FY sales and earnings guidance lowered |
| DY | 179.01 | -18.02% | Q3 contract revenue +41.6% to $2.06B; FY contract revenue outlook updated to $7.66–7.73B |
| ADI | 312.95 | -17.37% | FQ4 revenue +42% to $4.37B, but Q1 guide $4.4B ± $150M |
| SMTC | 86.46 | -16.97% | record quarterly sales $423.0M (+58%); Q4 guide $480.0M ± $5.0M on a longer quarter |
| HPE | 40.19 | -16.31% | FQ4 revenue +50% to $14.5B, FY27 outlook raised to $59.4–63.1B, but adjusted gross margin fell 2.2 points |

The pattern in the losers is the whole story of the session: **three companies that beat, raised, and still got sold** (ADI, SMTC, HPE) because the AI complex was being repriced as a group.

### Watchlist EOD review

| Ticker | Close | Day | Day range | Volume | Rel. volume | After-hours print |
|---|---|---|---|---|---|---|
| AAPL | 354.07 | +1.43% | 345.88 – 354.40 | 41,270,446 | 0.77 | 353.88 (-0.05%), range 353.13–354.39 |
| MSFT | 496.13 | +0.74% | 488.43 – 501.82 | 23,104,459 | 0.76 | 495.00 (-0.23%), range 493.50–498.32 |
| NVDA | 155.38 | **-5.86%** | 150.50 – 159.92 | 386,202,701 | **1.49** | 151.95 (-2.21%), range 151.25–155.50 |
| GOOGL | 279.05 | -1.08% | 276.03 – 281.78 | 33,923,550 | 0.79 | 278.88 (-0.06%), range 278.20–280.26 |
| AMZN | 252.29 | -1.21% | 250.53 – 255.56 | 33,920,333 | 0.66 | 251.46 (-0.33%), range 250.91–252.75 |
| IWM | 267.14 | +0.53% | 263.97 – 268.31 | 30,121,262 | n/a (ETF) | 266.48 (-0.25%), range 266.10–267.38 |
| GLD | 325.45 | -2.27% | 324.90 – 332.74 | 9,525,606 | n/a (ETF) | 325.20 (-0.08%), range 324.31–326.92 |
| TLT | 81.49 | -0.24% | 81.47 – 82.02 | 29,961,557 | n/a (ETF) | 81.40 (-0.11%), range 81.31–81.51 |

Watchlist read: the mega-cap core held up (AAPL and MSFT green, GOOGL and AMZN mildly red) while NVDA took the group's damage on 1.49× relative volume — the heaviest turnover in the list by a wide margin. The after-hours book is quiet across the whole list: no name is more than 2.3% off its close, so the after-hours tape has not yet voted on whether Monday's AI rally survives.

## Sector rotation

Cap-weighted on the de-duplicated cron #20 universe (one row per `cap_source_symbol`, preferring the primary listing over the `CAP_CARRIED` carrier row, `NO_CAP` and `NO_SECTOR` rows excluded), cross-checked against each sector's ETF and against representative names via the bridge.

| Sector | Cap-weighted % | Median % | Sector ETF | ETF % | Gap | Names |
|---|---|---|---|---|---|---|
| **Health Care** | **+3.07%** | +2.82% | XLV | +2.95% | +0.12pp | 841 |
| **Consumer Staples** | **+1.23%** | +0.53% | XLP | +1.66% | -0.43pp | 148 |
| **Real Estate** | **+0.88%** | +1.08% | XLRE | +1.31% | -0.43pp | 189 |
| Energy | +0.87% | +0.24% | XLE | +0.97% | -0.10pp | 185 |
| Financials | +0.75% | +0.10% | XLF | +0.83% | -0.08pp | 1,172 |
| Utilities | +0.20% | +0.53% | XLU | +0.18% | +0.02pp | 81 |
| Consumer Discretionary | +0.12% | +0.59% | XLY | +0.68% | -0.56pp | 391 |
| Communication Services | -0.33% | +0.60% | XLC | +0.82% | **-1.15pp** | 160 |
| Materials | -0.57% | -0.04% | XLB | +0.54% | **-1.11pp** | 155 |
| **Industrials** | **-1.60%** | -0.97% | XLI | -0.53% | **-1.07pp** | 557 |
| **Information Technology** | **-2.93%** | -2.63% | XLK | -3.26% | +0.33pp | 507 |

**Top three:** Health Care, Consumer Staples, Real Estate. **Bottom three:** Information Technology, Industrials, Materials.

**Three gaps are constituent effects, not rotation** — each is published with and without the constituent:

- **Industrials -1.60% → -0.71% ex-SPCX.** SpaceX carries $1.67T of the sector's $8.39T and fell 5.17%; ex-SPCX the sector is -0.71% against XLI's -0.53%, a gap of 0.18pp.
- **Communication Services -0.33% → +1.60% ex-GOOGL and META.** Those two hold $4.92T of the sector's $6.61T and were -0.92% and -1.16%; ex-them the sector is +1.60% against XLC's +0.82%.
- **Materials -0.57% → -0.06% ex-SCCO.** Silvercorp Metals fell 7.12% on $111B of a $1.52T sector, which is the whole of the gap to XLB's +0.54%.

**Information Technology's -2.93% is broad, not one name**: ex-NVDA it is still -2.15% against XLK's -3.26%. Health Care's +3.07% is equally broad — a median of +2.82% across 841 names, with LLY +3.15%, MRK +4.50%, ABBV +4.10%, AMGN +5.55% and GILD +4.75% at the top; INSM's $41B Sanofi deal is only 0.05pp of it. **The sector rotation is defensive, not risk-off**: money moved out of semiconductors into health care, staples, real estate and energy while the small-cap and equal-weight legs of the market were green.

## After-hours movers

The contract screen: TradingView's US scanner, `type` in (stock, dr), market cap above $1B, after-hours volume above 50,000, ranked by absolute after-hours change, 5 gainers and 5 losers. Every row carries its full level set. The `gap_fill_level` rule is applied as specified: where the after-hours range contains the 16:00 close, the gap fills at the close.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| STGW | 10.80 | 11.91 | 11.91 | 10.80 | 261,306 | +10.28% | 10.28% | 10.80 |
| PBLS | 33.14 | 36.39 | 36.39 | 33.14 | 67,328 | +9.81% | 9.81% | 33.14 |
| CTRI | 20.87 | 22.25 | 22.35 | 20.87 | 221,657 | +6.61% | 7.09% | 20.87 |
| SVM | 6.61 | 6.89 | 6.89 | 6.61 | 116,333 | +4.21% | 4.21% | 6.61 |
| SKM | 25.99 | 27.03 | 27.05 | 25.98 | 249,602 | +4.00% | 4.12% | 25.99 |
| AMBA | 44.47 | 27.77 | 44.47 | 24.33 | 3,988,192 | **-37.55%** | 45.29% | 44.47 |
| URBN | 85.58 | 75.10 | 86.01 | 72.98 | 730,605 | -12.25% | 15.23% | 85.58 |
| OC | 115.87 | 103.19 | 115.93 | 103.19 | 185,430 | -10.94% | 11.00% | 115.87 |
| NTNX | 54.59 | 49.80 | 55.02 | 48.70 | 1,053,494 | -8.77% | 11.58% | 54.59 |
| WDAY | 179.23 | 166.64 | 188.83 | 162.99 | 931,166 | -7.02% | 14.42% | 179.23 |

Every published row was verified on its own identity (`postmarket_change` = the change from the settled close), and every venue is a major US exchange — NASDAQ, NYSE or AMEX. No OTC row is published.

**The screen has a floor, and this time the floor hides the leaders.** Pulled without the market-cap floor, the same screen's top gainers are sub-$1B or near-zero-cap names: ZNB +100.77%, FCHL +53.13%, SVRE +47.79%, DKI +35.39%, APUS +34.74%. On the loser side AMBA at -37.55% *is* the session's leaderboard topper, followed by ONFO -24.58% and AREC -21.50%. The table above is the contract screen, not the whole after-hours tape. Note also that the screen's `type` filter excludes ETFs, so an independent leaderboard (MarketChameleon, 20:00 ET) is topped by leveraged ETFs — ANDD +5.2%, NVDQ +4.9%, UVIX +4.7% — that this screen cannot show.

**The tape keeps moving after the fire.** MarketChameleon at 20:00 ET independently printed AMBA -37.6% to $27.77, URBN -12.1% to $75.25 and OC -10.9% to $103.19 — within a rounding error of the 22:35 ET scanner prints published above. Earlier vendor prints differ materially: Benzinga had AMBA -44.38% at 17:00 ET and StockTitan had GDRX +18.33% at 18:02 ET, while the 22:35 ET scanner has GDRX at 2.93, **-2.33%** after a 4.05 high. The scanner's print is the source of record here.

## After-hours earnings reactions

| Ticker | After-hours | The catalyst |
|---|---|---|
| AMBA | -37.55% (27.77) | Q3 revenue +6.2% to $115.2M, adj EPS $0.28 (from $0.27); **Q4 revenue guided to $70–75M**. CEO: rising memory prices are leading customers to cut their own outlooks. Trading was halted for a period |
| URBN | -12.25% (75.10) | Record Q3 sales $1.67B (+8.9%), EPS $1.54 — a beat, sold anyway |
| OC | -10.94% (103.19) | No new company release located. Q3 (early November) missed, with Q4 revenue guided to $2.0–2.2B and roofing headwinds into early 2027 |
| NTNX | -8.77% (49.80) | Q1 revenue $772.4M (+15%); CEO Rajiv Ramaswami to step down once a successor is named |
| WDAY | -7.02% (166.64) | Q3 revenue $2.705B (+11.2%), subscription revenue +12.8% |
| ADSK | -3.58% (246.55) | Q3 revenue $2.16B (+17%); finance chief said the full-year billings and revenue midpoints were raised |
| ONC | -3.76% (400.00) | No company release located in this run |
| GDRX | -2.33% (2.93) | Q3 revenue $218.4M (+11%), FY guidance $844–850M — the print spiked to 4.05 in the early session and gave it all back |
| DELL | +0.92% (297.98) | Record Q3 revenue $54.9B (+103%) and a $132.3B AI order backlog — the strongest print of the night, faded from a 313 high to 287 before the close of the after-hours book |

Three things in this section matter more than the individual percentages. **First**, AMBA's guide is the most consequential line of the night: memory-cost inflation is now being transmitted into customer forecasts, which is a demand problem for the whole embedded-AI supply chain, not just one company's guidance. **Second**, the software names were sold on good numbers (URBN, WDAY, ADSK all beat) — the market is de-rating software multiples, not the results. **Third**, DELL's +103% revenue and $132.3B AI backlog is the strongest single piece of evidence that AI infrastructure demand did not break on Monday or Tuesday, and the market's fade from 313 to 298 shows it did not believe it either.

## Open research queue

1. **Does the equal-weight market's resilience survive PCE?** The cap-weight penalty has flipped sign every session this week (+212bp Monday, -102bp Tuesday) while the median name stayed positive. If core PCE prints at or above the 3.2% YoY consensus tomorrow and the penalty flips back positive, this week's rotation was a de-risking of one crowded complex rather than the start of an index-level decline. *What would resolve it:* the 2026-11-25 close's cap-weight penalty and the median name move, read together with the 8:30 ET release. *Why it matters:* it decides whether a -102bp penalty is a fact about semiconductors or a fact about the market.
2. **What exactly is in the $132.3B AI backlog?** DELL's backlog is the one hard demand number the AI complex produced tonight, and the market faded it from 313 to 298. Either the backlog is non-firm, or the market is discounting its timing, or the multiple is doing the work. *What would resolve it:* the backlog's conversion terms and cancellation language in the 10-Q, and whether the customer set overlaps with the hyperscaler capex that AMBA says is being deferred. *Why it matters:* it is the single cleanest test of whether the AI trade is a demand problem or a valuation problem.
3. **Is the memory-cost shock reaching end demand, or only intermediate pricing?** AMBA's CEO blamed rising memory prices for customers cutting their own outlooks. If that is a cost pass-through rather than a demand collapse, memory names (MU -11.01%) are a pricing problem that reverses; if it is end demand, the chip unwind has further to run. *What would resolve it:* the DRAM/NAND contract-price commentary in the next reporting season and whether MU's December guidance holds. *Why it matters:* it is the difference between a two-day air pocket and the start of a genuine de-rating of the AI supply chain.

## Source health

| Source | Query / URL | Status |
|---|---|---|
| MCP bridge, `market-recap` get_quotes | batch of 16 index/ETF symbols, `as_of` per row | ok — 16/16 found, every row dated 2026-11-24 |
| MCP bridge, `market-recap` price_history | 32 symbols, 2026-11-05 → 2026-11-24 | ok — used for SPY/RSP history, dated VIX/VXN, ES/NQ settles, and named-mover closes |
| MCP bridge, `market-recap` get_quotes (futures) | ES=F, NQ=F, YM=F, RTY=F, ZN=F, GC=F, CL=F, DX-Y.NYB | ok — all `as_of` 22:21 ET, live Globex |
| MCP bridge, `market-recap` get_quotes (Asia) | ^N225, ^KS11, ^HSI, 000001.SS, ^TWII, ^STI | ok — live, each row stamped; ^N225's stamp (21:35 ET) is ~40 min older than the rest |
| TradingView scanner, after-hours | `POST https://scanner.tradingview.com/america/scan`, 4 bodies (capped up/down, uncapped up/down) | ok — 2,072 names on the capped screen, 2,719 uncapped; 200-row pages, `totalCount` verified, all identities passed |
| TradingView scanner, targeted pull | `tv_scan.py pull --names` for 33 names | ok — one call per batch, coverage asserted (33/33) |
| cron #20 universe | `us-eod/2026-11-24.csv` (4,878 rows) | **degraded** — 1,626 of 4,420 cap-eligible names are `UNCONFIRMED` (unsettled close), carrying **65.6%** of the cap-weighted denominator; named movers diverge from the bridge (NVDA -7.33% vs -5.86%; ENTG -18.51% vs -10.02%). The participation and sector columns are on those unsettled closes; every *named* move in this brief is taken from the bridge instead |
| CBOE daily statistics | `https://www.cboe.com/us/options/market_statistics/daily/` | ok — `selectedDate` = 2026-11-24 = fire date; total and component ratios read from one payload |
| CBOE dated history | `cdn.cboe.com/.../VIX_History.csv`, `VXN_History.csv` | ok — 24 November closes agree to the cent with the bridge's dated history (26.36, 36.42) |
| Watchlist | `refs/watchlist.yaml` on the outputs repo | ok — 8 names, published file, not a local copy |
| MCP availability probe | `probe_mcp.py` | ok — `catalog_ok total=135 finance_tools=0`; the bridge packs (tradier, marketdata-app, market-recap) answered on every call |
| Web — issuer and press | StockTitan, Benzinga, Reuters, Bloomberg, CNBC, MarketChameleon, GuruFocus, Medtronic IR, Sanofi/Insmed release | ok — every catalyst in this brief is sourced to one of these; OC and ONC have **no** located catalyst and are published as such |
| Web — earnings calendar | ATLAS 27, EarningsWhispers 29, Digrin 65, Nexqual 10, MarketChameleon 15, RapidTradeView 17, OpenCapital 14 | ok — counts disagree; the published roster is the intersection of two or more vendors and the disagreement is disclosed above |
| Web — economic calendar | Macro Bullseye, FRC, Wells Fargo week-ahead, Schwab | ok — the 8:30 ET PCE/GDP/claims block and the 2:00 ET Beige Book agree across all four |

**Degraded source count: 1** — cron #20's EOD CSV settle quality, described above.

## Method notes

- **The participation read and the sector rotation come from cron #20's universe; the named moves come from the bridge.** One number per field, one source per field: where the CSV and the bridge disagree for a named security (NVDA, ENTG, MSFT, GOOGL, LLY, MRK, XOM, NEE), the bridge's dated close is published, because the quote source of record carries an independent CNBC cross-check and the CSV row is flagged `UNCONFIRMED`. The *aggregates* (advancers, decliners, median, sector cap-weighted) necessarily use the CSV, because a universe of 4,848 names cannot be re-quoted from a metered bridge — so those columns inherit the unsettled closes, which is the one degradation in this run.
- **Sector de-duplication:** one row per `cap_source_symbol`, keeping the row whose `data_quality` does not contain `CAP_CARRIED`; rows flagged `NO_CAP`, `NO_SECTOR` or `EX_DISTRIBUTION` are excluded from every cap-weighted column. 152 share-class keys had more than one row. Every published cap-weighted sector return is inside ±20% (the widest is -2.93%), and the concentration gaps are published with and without the constituent.
- **The volatility indices are read from dated history, not from the quote row.** The bridge's `get_quotes` returned the 23 November ^VXN reading (36.31, -19.76%) with a stale `as_of` while every other symbol in the same call was current; the published VXN close of 36.42 (+0.30%) comes from `price_history` and is confirmed by CBOE's own dated file.
- **The overnight is published against two denominators.** Against the 16:59 ET settle the ES move is -0.51%; against the cash index close it is -0.29%. The cash-close comparison is the one that answers whether the overnight extended the session's move, and the published Globex range shows the session faded 0.8% and has recovered about 0.28% of it.
- **The after-hours tape is a snapshot at the fire (22:35 ET).** The scanner's print is the source of record; earlier vendor prints are named in `## After-hours movers` rather than blended into the table. Every published row passed the `postmarket_change` identity check and carries a major-US-exchange venue.
- **The `gap_fill_level` rule is applied exactly as specified.** Where the after-hours range contains the 16:00 close the gap fills at the close; all ten published rows fall in that case, so `gap_fill_level` equals `prior_close` throughout.
- **No trade, no position, no P&L is published** — this brief is read-only by design.
