---
date: 2026-11-25
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:31-22:48
session: 467398660554950
scheduled_at_ms: 1795663801383
status: ok
source: MCP bridge market-recap (get_quotes, price_history); TradingView scanner (postmarket_* columns); CBOE daily statistics and dated VIX/VXN close files; cron #20 us-eod/2026-11-25.csv; refs/watchlist.yaml; web (NYSE, AP, AFP, Reuters, MarketWatch, Investopedia, Investing.com, Yahoo, Barron's, Danske, Schwab)
primary_source: MCP bridge market-recap - Yahoo-sourced batch quotes and dated daily history
universe: cron #20 us-eod/2026-11-25.csv - 4,902 rows, 4,840 priced; cap-weighted sector columns cover 4,301 rows after share-class de-duplication and flag exclusions
degraded_sources: 1
---

# Post-market brief — Wednesday, 25 November 2026

## TL;DR

The Dow erased a 1,105-point intraday loss and closed **+0.33%** while the S&P 500 slipped **-0.25%** and the Nasdaq fell **-0.62%** — but the tape underneath was broad, not weak. The median name gained **+0.49%** (`median_name_move_pct`) with **3,003 advancers** against **1,674 decliners**, and `liquid_adv_dec_ratio` was **2.69** in the $2bn-plus set. The cap-weight penalty is the number that explains the headline: `cap_weight_penalty_bp` = **-112**, the equal-weight index up 0.83% while the cap-weighted one fell 0.29%. The AI complex caused the washout (NVDA -3.91% after being 9% lower intraday) and the market bought it back into the close — VIX ended 28.29 (+7.32%) after a 34.95 intraday high, and the Nasdaq gave back a 4.6% intraday loss.

**Tomorrow the US cash market is closed — Thursday 26 November is Thanksgiving**, with no regular session, no pre-market and no after-hours. Friday 27 November is a 13:00 ET early close. So the only live setup is the overnight futures bid (ES +0.58% against the 25 November settle, **+0.76% against the cash close**), and it resolves at Friday's short session, not at a Thursday bell.

## Tomorrow's setup — Thursday 26 November 2026

**There is no US cash session tomorrow.** NYSE and Nasdaq are shut for Thanksgiving Day; CME equity-index futures halt at 1:00 pm ET and reopen at 6:00 pm ET; the SIFMA bond market is recommended closed. Friday 27 November runs 09:30–13:00 ET. Everything below is therefore the setup for **Friday's short session**, not a Thursday open.

### Futures and the overnight setup

Every futures row below is stamped 22:21 ET — nine minutes before the fire, and after the 18:00 ET Globex reopen, so this is the live overnight session and not a stale settlement. The prior settle is the dated 25 November settlement from the bridge's `price_history`, not the cash close: a futures quote measured against the wrong base is the single most common way a setup gets described wrongly, so both denominators are published.

| Contract | Last (22:21 ET) | vs prior settle | vs the cash close it tracks |
|---|---|---|---|
| ES=F | 7,237.25 | **+0.58%** vs settle 7,195.75 | **+0.76%** vs S&P 500 7,182.78 |
| NQ=F | 26,311.00 | **+0.81%** vs settle 26,100.25 | **+1.01%** vs Nasdaq 100 26,046.90 |
| YM=F | 50,404.00 | **+0.35%** vs settle 50,228 | **+0.44%** vs Dow 50,182.95 |
| RTY=F | 2,717.60 | **+0.43%** vs settle 2,706.10 | **+0.50%** vs Russell 2000 2,704.06 |
| ZN=F | 106.84375 | **-0.32%** vs settle 107.1875 | n/a — no cash bond index in the feed |
| GC=F (Dec gold) | 3,604.30 | **+1.94%** vs settle 3,535.80 | see the gold note below |

**Read the overnight against the cash close, not the settle.** ES settled 7,195.75 on a session in which the cash index fell 0.25%; the overnight took it to 7,237.25, 0.76% above where the cash index actually closed. The Globex range is wide — 7,187 to 7,250, about 0.9% — so this is a genuine bid with a wide range, not a thin drift. NQ is the strongest leg at +1.01% above the Nasdaq 100 close: the futures are paying for the mega-cap names that were sold hardest.

**Gold is the outlier and the two instruments disagree.** The December gold future is +1.94% above its 25 November settlement of 3,535.80 — a settle that itself fell 0.73% on the day. The gold ETF closed +0.61% at 327.45 but its extended-hours print was **326.48, -0.30%**. The ETF's thin after-hours book did not mark the future; treat the **future** as the overnight signal and the ETF as the session leg. Neither is wrong and they are not blended.

**The Asia leg was a bounce, and it is stamped.** After a Wednesday in which the Nikkei fell about 3% and the Kospi fell 6%, Asian equities rebounded overnight: Nikkei 225 **57,804.92, +1.4%**; Kospi **4,758.82, +1.3%**; Hang Seng 22,274.79, +1.4%; Shanghai Composite 3,478.05, +0.1%; Taiwan's Taiex +3.05%; MSCI Asia Pacific +0.4% — all at roughly 02:00 GMT (21:00 ET Wednesday). The Bank of Korea raised its benchmark 25bp to 3.25%, a two-year high. These are live prints and they move: across the same morning the Nikkei was quoted between +1.21% and +1.85% and the Kospi between +0.9% and +2.0%, so treat the levels as a snapshot rather than a settled number.

### Economic calendar

Tomorrow (Thursday 26 November) carries **no US releases** — the exchanges are closed and the holiday is the schedule. The releases that matter land on Friday 27 November, before the 13:00 ET close:

| Time (ET) | Release | Period | Consensus |
|---|---|---|---|
| 08:30 | Advance goods trade balance | October | -$132.4bn (one calendar prints -$133bn) |
| 08:30 | Wholesale inventories; retail inventories | October | — |
| 08:30 | Initial jobless claims | week to 21 Nov | moved up a day for the holiday |
| 10:00 | Multivariate Core Trend Inflation (NY Fed) | October | — |
| 12:45 | NY Fed Staff Nowcast | — | — |

Overnight and European: Japan Tokyo CPI 00:30 ET, China industrial profits 02:30 ET, the ECB's one-year CPI expectations survey 10:00 ET, euro-area consumer and economic confidence 11:00 ET.

For context on what set up today's tape: **third-quarter GDP second estimate 3.5%** against 3.4% expected; **October PCE 3.8% year over year** against 3.6% expected, with core at 3.2–3.3% year over year (two calendars differ by 0.1pp) versus 3.1% expected and core +0.3% month over month; personal spending +0.4% month over month; durable-goods core capital-goods orders +0.8%; new home sales 645,000 against 676,000 expected; the Atlanta Fed's Q4 GDPNow revised down to **2.90% from 3.20%**; a 7-year note auction at 4.708% against a 4.894% prior; and the Fed's Beige Book at 14:00 ET. Two tariff headlines sat on top: a proposed 10% duty on Brazilian aircraft, and a package targeting 14 economies on structural excess manufacturing capacity.

### Earnings calendar

**Tomorrow has no US earnings calendar** — the exchange is closed and no company is scheduled. For Friday 27 November the vendors disagree on both the count and the roster: EarningsWhispers lists 13 names (all before the open), MetaCap 32 reports, QuarterlyEarnings.info 34 companies (29 before the open, 2 after), ATLAS 22, Digrin 15, investz 8, stockmarketagent 3. Published as the **intersection of two or more sources**: **XYF** and **MOV** (before the open), **TRX**, **KT**, **NAT** (after the close, EPS estimate $0.10), **CHA** (time not announced), plus the tanker pair **FRO** and **HAFN** (before the open — single-source). Friday's 13:00 ET early close also means an after-the-close report lands after the market is already shut, so it is a Monday event, not a Friday one.

### News to watch for the top movers

The three largest liquid names of the session and the biggest decliners:

- **HPQ +11.49% to 31.15** — fiscal Q4 2026 beat (revenue $16.0bn, +9.3% year over year) with above-consensus fiscal 2027 guidance and a dividend increase. The best S&P 500 performer of the day, and it rose while the chip complex was selling.
- **JOBY +11.11% to 3.90** — no company-specific catalyst was found in the sources read; treat the move as unexplained.
- **ASTS +10.25% to 26.02** — said it targets 45 satellites in orbit by mid-2027, escalating its deployment timeline and capital requirements. The same day, the federal communications regulator cleared a rival's orbital data-centre constellation of up to one million satellites.
- **NTNX -15.19% to 46.30** — the chief executive's unexpected departure, reported by Barron's. The largest decline in the liquid set.
- **URBN -10.33% to 76.74** — a Q3 comparable-sales slowdown; several analysts cut estimates. "Higher fuel costs weigh on apparel retail earnings" was the sector read, and apparel names were bid elsewhere on the day.

### Tomorrow's three things to watch

- **VERA — 34.43 after-hours last, 29.50 gap-fill, 37.34 after-hours high** — the drug regulator pushed Vertex's competing kidney-drug review out to 28 February 2027, which widens Vera's window to build share; watch whether the 16.72% after-hours move holds above the 29.50 prior close at Friday's open.
- **PANW — 342.87 after-hours last, 356.14 gap-fill, 333.55 after-hours low** — a former executive's accounting-fraud allegations, which the firm denies, reset the base; the 333.55 low is the level to defend into Friday's 13:00 ET close.
- **ASTS — 26.98 after-hours last, 26.02 gap-fill, 27.02 after-hours high** — raised its 2027 deployment target to 45 satellites, and the regulator cleared a rival's orbital data-centre constellation the same day; 27.02 is the level to clear.

## Day's tape

### Market read

| metric | value | source |
|---|---|---|
| advancers | 3,003 | cron #20 `us-eod/2026-11-25.csv` (4,840 priced names) |
| decliners | 1,674 | same |
| unchanged | 163 | same |
| median_name_move_pct | +0.49 | same, `change_pct` |
| cap_weight_penalty_bp | -112 | bridge `price_history` — SPY -0.29% vs RSP +0.83% |
| liquid_adv_dec_ratio | 2.69 | same CSV, `market_cap` > $2.0bn — 1,771 names: 1,275 advancers / 474 decliners |

The index and the tape tell opposite stories, and the spread between them is the story: the median name rose 0.49% and 3,003 names advanced, yet the S&P 500 fell 0.25% because the cap-weighted index is dominated by the handful of AI names being sold. A -112 basis point cap-weight penalty on a down day for the index is a **broadening** tape, not a broad capitulation — the opposite of the 20 November print, when the penalty was -166 basis points on a -3.64% index day. Cross-check: MarketWatch's exchange-level count put NYSE advancers at 1,941 against 762 decliners and Nasdaq at 2,944 against 2,015 — a different population from the 4,840-name universe above, but directionally the same.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-19 | -1.962 | -1.764 | -20 |
| 2026-11-20 | -3.640 | -1.980 | -166 |
| 2026-11-23 | +4.709 | +2.594 | +212 |
| 2026-11-24 | -0.486 | +0.536 | -102 |
| 2026-11-25 | -0.289 | +0.832 | -112 |

The penalty has printed negative on four of the last five sessions. The one positive print (23 November, +212) came with a +4.71% index day, so the pattern is not simply "risk-off favours equal weight" — it is that the index's own direction is being set by a small AI cohort and the rest of the market is moving the other way.

### Index, ETF and volatility levels

| Instrument | Close | Change | Day range | as_of (ET) |
|---|---|---|---|---|
| S&P 500 | 7,182.78 | -0.25% | 6,970.11 – 7,199.31 | 16:32 |
| Nasdaq Composite | 23,585.80 | -0.62% | 22,632.40 – 23,627.45 | 17:15 |
| Dow Jones Industrial Average | 50,182.95 | +0.33% | 48,913.74 – 50,395.24 | 16:32 |
| Russell 2000 | 2,704.06 | +0.71% | 2,623.78 – 2,710.05 | 16:30 |
| Nasdaq 100 | 26,046.90 | -0.64% | 24,970.66 – 26,081.65 | 17:15 |
| Philadelphia Semiconductor (^SOX) | 8,774.86 | -0.65% | 8,129.23 – 8,781.01 | 17:15 |
| Cboe VIX | 28.29 | +7.32% | 27.49 – 34.95 | 16:15 |
| Cboe VXN | 38.53 | +5.79% | 38.27 – 44.18 | 16:15 |
| SPY | 716.70 | -0.29% | 695.45 – 718.43 | 16:00 |
| QQQ | 633.93 | -0.65% | 607.76 – 634.89 | 16:00 |
| IWM | 268.87 | +0.65% | 260.84 – 269.77 | 16:00 |
| DIA | 501.27 | +0.31% | 488.62 – 503.39 | 16:00 |
| RSP | 215.74 | +0.83% | 210.54 – 216.59 | 16:00 |
| SMH | 422.46 | -1.01% | 393.88 – 422.94 | 16:00 |

**The intraday story is the story.** The S&P 500 traded down to 6,970.11 — 3.2% below the prior close — and the Nasdaq to 22,632.40, 4.6% down, before both closed well off their lows. The Dow's low of 48,913.74 was 1,105 points below the prior close and it closed 1,269 points above that low. NVDA was 9% lower intraday (141.17 against a 155.38 prior close) and closed -3.91%; the semiconductor ETF's low of 393.88 was 7.2% below its close. Eight of the eleven S&P 500 sectors closed higher even as the two headline indices were red.

**Volatility is dated, not quoted.** The VIX and VXN closes above are read from the bridge's dated `price_history` and cross-check to the cent against Cboe's own dated close files (VXN_History.csv, VIX_History.csv): VXN 38.53 on 2026-11-25, VIX 28.29. Both volatility indices spiked in the morning (VIX 34.95, VXN 44.18) and gave back the spike into the close, but both closed in the upper third of their range — the market did not settle down.

### Cross-asset

| Asset | Level | Change | as_of (ET) |
|---|---|---|---|
| Gold, December future (GC=F) | 3,604.30 | +1.94% vs the 25 Nov settle of 3,535.80 | 22:21 |
| Gold ETF (GLD) | 327.45 close | +0.61% session; after-hours 326.48 (-0.30%) | 16:00 close / AH snapshot |
| 10-year Treasury yield (^TNX) | 4.848% | -5.6bp from 4.904% | 14:59:53 |
| 10-year Treasury future (ZN=F) | 106.84375 | -0.32% vs the 25 Nov settle of 107.1875 | 22:21 |
| Long-duration bonds (TLT) | 82.24 | +0.92% | 16:00 |
| WTI crude (CL=F) | 84.20 | +0.62% | 22:21 |
| Dollar index (DX-Y.NYB) | 103.80 | +0.13% | 22:21 |
| Bitcoin (BTC-USD) | 60,606.57 | +0.38% | 22:31 |

Yields fell 5.6bp on the session and the bond future is drifting lower again overnight. Gold is the clearest overnight divergence: a hot PCE print that pushed yields down did not stop the gold bid, and the December future is now 1.94% above its own settlement while the ETF's after-hours book still shows it slightly lower.

### Day's movers

Liquid set ($2bn+ market cap), closes and changes from the bridge:

| Ticker | Close | Change | Sector | Catalyst |
|---|---|---|---|---|
| HPQ | 31.15 | +11.49% | Information Technology | Q4 FY2026 beat, above-consensus FY2027 guidance, dividend raised |
| JOBY | 3.90 | +11.11% | Industrials | no company-specific catalyst found in the sources read |
| ASTS | 26.02 | +10.25% | Communication Services | 45 satellites in orbit by mid-2027; rival's orbital data-centre constellation cleared |
| CAR | 141.82 | +9.62% | Industrials | not sourced |
| DKNG | 17.65 | +9.56% | Consumer Discretionary | not sourced |
| COGT | 36.08 | +9.30% | Health Care | regulator approved EKITNA for previously treated GIST on Phase 3 PEAK data |
| NTNX | 46.30 | -15.19% | Information Technology | chief executive's unexpected departure |
| URBN | 76.74 | -10.33% | Consumer Discretionary | Q3 comparable-sales slowdown, estimates cut |
| CENT | 38.12 | -7.59% | Consumer Staples | not sourced |
| IBRX | 5.645 | -5.92% | Health Care | not sourced |
| LRCX | 185.01 | -5.68% | Information Technology | not sourced |

### Watchlist EOD review

The published watchlist (`refs/watchlist.yaml`, 8 names) — closes and day ranges from the bridge, volume and relative volume from the equity universe file, after-hours prints from the TradingView scanner.

| Ticker | Close | Day change | Day range | Volume vs average | After-hours print |
|---|---|---|---|---|---|
| AAPL | 355.58 | +0.43% | 345.13 – 356.75 | 52.8m, 1.10x | 355.10 (-0.13%), hi 355.90, lo 354.57, 9.92m |
| MSFT | 489.93 | -1.25% | 477.39 – 493.44 | 25.9m, 0.96x | 491.59 (+0.34%), hi 492.91, lo 488.75, 5.53m |
| NVDA | 149.30 | -3.91% | 141.17 – 150.37 | 356.8m, 1.38x | 151.22 (+1.29%), hi 152.10, lo 148.40, 23.50m |
| GOOGL | 273.10 | -2.13% | 262.73 – 273.62 | 40.4m, 1.03x | 274.99 (+0.69%), hi 275.63, lo 272.24, 5.38m |
| AMZN | 244.43 | -3.12% | 235.96 – 246.55 | 61.1m, 1.26x | 246.77 (+0.96%), hi 247.26, lo 243.91, 12.11m |
| IWM | 268.87 | +0.65% | 260.84 – 269.77 | 31.9m, n/a (ETF, outside the equity universe) | 270.31 (+0.54%), hi 270.31, lo 268.53, 1.00m |
| GLD | 327.45 | +0.61% | 313.96 – 328.68 | 16.9m, n/a (ETF) | 326.48 (-0.30%), hi 329.27, lo 326.00, 0.54m |
| TLT | 82.24 | +0.92% | 82.17 – 82.81 | 48.9m, n/a (ETF) | 82.03 (-0.26%), hi 82.29, lo 82.00, 4.00m |

No watchlist name reported after the close on 25 November. The interesting line is the reversal in the after-hours tape: the four mega-cap software names that were sold in the cash session were bid after hours (NVDA +1.29% on 23.50m shares, AMZN +0.96%, GOOGL +0.69%, MSFT +0.34%), while AAPL was the only one left slightly lower (-0.13%). The ETF legs went the other way — GLD -0.30% and TLT -0.26% after hours — which is the thin-book warning the gold and bond futures disagree with.

## Sector rotation

Top three and bottom three by cap-weighted return, from the universe's `sector` column, de-duplicated on `cap_source_symbol` with cron #20's flags applied. The sector ETF is the independent cross-check.

| Sector | cap-weighted % | median % | Sector ETF | ETF % | Gap |
|---|---|---|---|---|---|
| Materials | **+1.97** | +2.13 | XLB | +2.07 | -0.10pp |
| Industrials | **+1.09** | +1.34 | XLI | +0.83 | +0.26pp |
| Real Estate | **+0.92** | +0.88 | XLRE | +0.92 | 0.00pp |
| Information Technology | **-0.77** | +0.77 | XLK | -0.83 | +0.06pp |
| Consumer Discretionary | **-0.66** | +0.76 | XLY | -0.20 | -0.46pp |
| Health Care | **-0.46** | 0.00 | XLV | -0.56 | +0.10pp |

**Coverage note.** Eleven sectors are ranked. The cap-weighted columns cover 4,301 of the universe's 4,902 rows (87.8%) after dropping 290 rows flagged `CAP_CARRIED` (a second share class carrying the parent's cap — Berkshire's A and B lines each carry the full $1.24tn and would double the denominator), 79 flagged `EX_DISTRIBUTION`, 116 flagged `NO_SECTOR` and 71 flagged `NO_CAP`, plus 45 rows without a price. The `NO_SECTOR` bucket is excluded because it is not a sector: including it would displace Health Care from the bottom three. Every published cap-weighted sector return is inside ±20%.

**The one number worth pausing on is Information Technology: cap-weighted -0.77% while the median technology name rose +0.77%** — a 1.53pp spread. The XLK cross-check (-0.83%) matches the cap-weighted column almost exactly, so this is constituent concentration rather than a rotation: the mega-cap AI cohort (NVDA -3.91%, ORCL -5.03%, MU -4.37%) is dragging a sector whose median constituent went up. Materials, Industrials and Real Estate at the top is the same story read from the other side — money rotating out of the AI complex into cyclicals and rate-sensitive real estate on a 5.6bp fall in the 10-year yield. No sector/ETF gap exceeds 0.5pp, so no sector row needs a constituent carve-out.

## After-hours movers

The extended-hours screen from the TradingView scanner: `type` in stock/dr, `market_cap_basic` above $1bn, `postmarket_volume` above 50,000, sorted both directions and ranked by absolute `postmarket_change`. Five gainers, five losers. Every row carries its levels, because a percentage without a level is not actionable.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| VERA | 29.50 | 34.43 | 37.34 | 29.50 | 631,580 | +16.72% | 26.58% | 29.50 |
| KNTK | 54.70 | 58.58 | 62.20 | 54.63 | 160,972 | +7.09% | 13.84% | 54.70 |
| GRDN | 52.11 | 55.35 | 55.35 | 52.11 | 117,878 | +6.22% | 6.22% | 52.11 |
| AGLT | 6.49 | 6.85 | 6.97 | 6.49 | 87,990 | +5.55% | 7.40% | 6.49 |
| ASST | 14.95 | 15.72 | 16.50 | 14.94 | 368,097 | +5.15% | 10.37% | 14.95 |
| AVPT | 17.30 | 15.95 | 17.30 | 15.60 | 301,512 | -7.82% | 9.83% | 17.30 |
| VRTX | 564.12 | 524.04 | 569.98 | 520.00 | 394,067 | -7.10% | 8.87% | 564.12 |
| LAMR | 156.39 | 146.61 | 156.39 | 146.61 | 71,959 | -6.25% | 6.26% | 156.39 |
| GENB | 11.31 | 10.66 | 11.31 | 10.66 | 70,026 | -5.76% | 5.76% | 11.31 |
| PRMB | 23.20 | 22.32 | 23.20 | 22.32 | 624,897 | -3.80% | 3.80% | 23.20 |

Every row in the table traded back through its 16:00 close in the extended session, so `gap_fill_level` is the prior close in all ten cases — the gap fills at the prior close, and each name's after-hours high or low is the extension beyond it. Every row passed the identity check `postmarket_change = (postmarket_close − close) / close × 100`, and every row's prior close was confirmed against the bridge's quote for the primary listing — no venue-routed or rounded stale close survived into this table.

The tape also carried large-cap moves that the $1bn floor keeps out of the table: **SNDK +4.17% to 76.68** after falling 5.57% in the cash session on 7.95m after-hours shares, and **MU +2.33% to 615.28** — the memory complex bouncing with the futures, not reporting. **ANT +1.76% to 84.25** on 52.34m shares and **DE +0.66% to 645.23** complete the large-cap after-hours picture.

## After-hours earnings reactions

Tonight's after-hours tape was driven by **regulation and litigation, not by earnings** — no watchlist name reported, and the ten biggest movers on the screen are all event-driven.

- **VRTX -7.10% to 524.04 / VERA +16.72% to 34.43 — one decision, two opposite moves.** Vertex said the FDA extended the review timeline for **povetacicept** in IgA nephropathy, pushing the decision date from 30 November 2026 to no later than 28 February 2027. Vera's TRUTAKNA, which already carries accelerated approval, benefits from a longer head-to-head-free window. Vendor prints for the same news ranged from -7.0% to -7.6% for VRTX and +15.6% to +17.0% for VERA; the scanner's 22:35-ish snapshot is the source of record above.
- **PANW -3.73% to 342.87** — a former executive accused the company of accounting fraud; the firm denies the claims. This is litigation, not a report (Palto Alto Networks' last earnings were 18 November). VRTX's and PANW's after-hours lows are 520.00 and 333.55 respectively.
- **SNDK +4.17% to 76.68 and MU +2.33% to 615.28** — the AI-memory complex rebounding with the futures after a -5.57% cash session for SNDK. Neither company reported; Sandisk's next report is expected in February.
- **DE +0.66% to 645.23** — Deere reported before the open and was slightly higher after hours.
- **LAMR -6.25%, GENB -5.76%, AVPT -7.82%, PRMB -3.80%, KNTK +7.09%, GRDN +6.22%, AGLT +5.55%, ASST +5.15%** — no catalyst was sourced for any of these in the sources read, so none is asserted here. They are published with their levels and left unattributed.

## Open research queue

1. **Is the -112 basis point cap-weight penalty a rotation or a hiding place?** It matters because the index's direction and the market's direction have separated, and a broadening tape looks like resilience while the AI complex is being marked down underneath it. The penalty has printed negative on four of the last five sessions, and the one positive print came with a +4.71% index day. What would resolve it: the penalty for Friday's 13:00 ET session read against the median name move, and whether equal-weight relative strength survives into a full session rather than a shortened one.
2. **Is the overnight futures bid a real risk-on signal or a thin pre-holiday book?** ES is 0.76% above the cash close with a 0.9% Globex range, but Friday is a 13:00 ET session, the futures week closes early at 1:15 pm ET, and no cash market will price the move until Friday morning. What would resolve it: whether the bid holds through the futures exchange's 6:00 pm ET Thursday reopen and the Asian session, and whether volume behind the move is real.
3. **Does the FDA delay reprice the IgA-nephropathy market or only Vera's quarter?** A rival's three-month delay moved VERA +16.72% and VRTX -7.10% — a large move for a timing change, and the two together imply a meaningful share shift rather than a delay. What would resolve it: TRUTAKNA's prescription and launch trajectory in the December quarter, and any change to Vertex's commercial guidance.

## Source health

| Source | Used for | Status |
|---|---|---|
| MCP bridge `market-recap` `get_quotes` (31 symbols, retrieved 22:31 ET) | index, ETF, futures, watchlist closes and day ranges | ok, with one degraded row — see below |
| MCP bridge `market-recap` `price_history` (SPY, RSP, ^VIX, ^VXN, NVDA, ES/NQ/YM/RTY/ZN/GC) | cap-weight penalty history, dated volatility closes, dated futures settlements | ok |
| MCP bridge `get_quotes` **^VXN row** | — | **degraded: stale.** The row carried `as_of` 2026-11-24 with a close of 36.42 (+0.30%) — the prior session's reading — while every other index row in the same call carried 2026-11-25. The published VXN close of 38.53 (+5.79%) comes from the bridge's dated `price_history` and agrees to the cent with Cboe's `VXN_History.csv`. **Counted as 1 degraded source.** |
| CBOE `VIX_History.csv` / `VXN_History.csv` | volatility cross-check | ok — VIX 28.29 and VXN 38.53 for 2026-11-25, matching the bridge's dated history to the cent |
| CBOE daily statistics page (`selectedDate` 2026-11-25, `prevTradingDay` 2026-11-25) | put/call ratio | ok — session date equals the fire date |
| TradingView scanner, `postmarket_*` columns (2,003 names screened; 200 rows per direction) | after-hours movers table, watchlist after-hours prints | ok — both directions pulled, rows keyed on the bare ticker |
| TradingView scanner, no market-cap floor (3,257 names) | the session's real leaderboard | ok — published below, not in the table |
| cron #20 `us-eod/2026-11-25.csv` (4,902 rows) | participation read, sector rotation, liquid-set counts | ok — the fire-date file was published; 3,390 rows `CONFIRMED`, 1,459 `UNCONFIRMED`, 53 `NO_BAR`, the same settle mix as the prior-day file |
| `refs/watchlist.yaml` | watchlist section | ok — 8 names |
| Web: NYSE, AP, AFP, Reuters, MarketWatch, Investopedia, Investing.com, Barron's, Yahoo, Danske, Schwab, Globe and Mail | session narrative, holiday schedule, Asia leg, calendars, catalysts | ok |
| MCP availability probe | runtime catalog | `catalog_ok total=138 finance_tools=0` — no financial MCP registered, as expected; the bridge is the market-data path |

**The $1bn floor hides the session's real leaderboard.** The same extended-hours screen without the market-cap floor produced these moves, which the table above cannot show:

| ticker | prior_close | after-hours | change |
|---|---|---|---|
| POM | 1.61 | 2.81 | +74.53% |
| NCPL | 1.87 | 2.67 | +42.78% |
| NXAT | 0.6448 | 0.8205 | +27.25% |
| RAYA | 0.655 | 0.8199 | +25.18% |
| DOGZ | 0.2282 | 0.2821 | +23.62% |
| VVOS | 0.046 | 0.0297 | -35.43% |
| VIVK | 0.137 | 0.0931 | -32.04% |
| JDZG | 0.109 | 0.0757 | -30.55% |
| STAK | 2.74 | 2.12 | -22.63% |
| SUGP | 0.8255 | 0.65 | -21.26% |

**Put/call, dated to the fire session.** CBOE's daily statistics payload for `selectedDate` 2026-11-25 (which equals `prevTradingDay`, so it is the session that just closed): **total put/call 0.978** — 8,707,205 calls against 8,519,982 puts on 17,227,187 contracts. The splits come from the same payload and reconcile with that total: index options 1.045, equity options 0.643, exchange-traded products 1.309, SPX+SPXW+SPXO 0.990, VIX options 1.559. A total near 1.0 with index options above it and equity options well below it is a hedging-heavy tape in index products and a constructive one in single names — consistent with the pattern of the day.

**Other notes.** The after-hours prints are a snapshot as of the fire (roughly 22:35–22:45 ET) and the tape keeps moving; where another vendor's number differs materially it is named rather than blended — VRTX prints ranged -7.0% to -7.6% and VERA +15.6% to +17.0% across vendors. The gold and Treasury ETF after-hours prints (-0.30% and -0.26%) are thin-book prints that do not mark their futures, and the futures are published separately with their own basis. The bridge's quote rows and its dated history disagree on the futures basis for two contracts: the quote row for ZN=F carries a previous close of 107.08 against the dated 25 November settlement of 107.19, and the quote row for GC=F carries 3,564.60 against the dated settlement of 3,535.80. The settlement column in the setup table uses the dated rows; the two bases are disclosed rather than merged. The 10-year yield quote is stamped 14:59:53 ET, its own index convention, and is published with that stamp rather than as a 16:00 close. The Asian index levels carry the 02:00 GMT stamp of the source that published them, and the same morning's readings ranged from +1.21% to +1.85% for the Nikkei and +0.9% to +2.0% for the Kospi.

## Method notes

- **Window.** The shared `window_check.sh` was fetched at run time with its `WINDOW_CHECK_V2` capability marker required, and was evaluated against the fire's own scheduled instant (`scheduled_at_ms` 1795663801383 = 2026-11-25 22:30 ET), not the wall clock. It returned `fire-date: 2026-11-25`, `replay: no`, `stall_min: 0`. This is not a delayed replay.
- **Population.** The participation read, the median name move and the liquid-set ratio all use one population — cron #20's `us-eod/2026-11-25.csv`, 4,902 rows, 4,840 priced — so those counts are comparable with the prior session's published breadth. The liquid set is `market_cap` above $2.0bn, 1,771 names. The sector columns are a different population (4,301 rows) because de-duplication and the flag exclusions necessarily remove rows; that coverage is stated above rather than averaged in.
- **One source per field.** Prices, closes and movers come from the bridge's `market-recap` pack; the volatility closes come from the bridge's dated history cross-checked against Cboe's dated files; extended-hours prints come from the TradingView scanner and are dated to the snapshot; the put/call split comes from one CBOE payload. Where two sources disagree by more than 0.6%, the bridge is preferred and the other number is named in the source notes rather than published alongside it.
- **Futures basis.** Both denominators are published for every futures row: the dated prior settlement and the cash index close the contract tracks. The overnight is judged on the cash-close comparison, because that is the number that answers whether the overnight extended the session's move.
- **After-hours levels.** `gap_fill_level` is deterministic: the prior close when the after-hours range spans it, otherwise the after-hours midpoint. All ten rows in the table fell in the first case. The identity check and a bridge confirmation of each prior close against the primary listing were applied before publication; no row failed.
- **Degradation.** One source degraded: the bridge's ^VXN quote row returned the prior session's reading. The published VXN value comes from a dated source that agrees with Cboe's file, so no published number is affected — but the count is disclosed rather than hidden. The errors count in the reply equals this count.
- **Not done.** No trading, no position sizing, no portfolio commentary. Producer names whose catalyst could not be sourced are published with their levels and no attribution.
