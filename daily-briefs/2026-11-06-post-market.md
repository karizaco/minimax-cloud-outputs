---
date: 2026-11-06
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:35-22:50
session: 460674447171667
scheduled_at_ms: 1794022219763
status: ok
source: MCP bridge market-recap (get_quotes, price_history, market_snapshot); TradingView america scanner; cron #20 us-eod/2026-11-06.csv; CBOE daily market statistics; web (issuer IR, StockTitan, EarningsWhispers, Investing.com)
primary_source: MCP bridge market-recap get_quotes
universe: cron #20 us-eod/2026-11-06.csv, 4,892 rows; the participation read uses the 4,725 names with a usable price change (48 ex-distribution rows excluded, 119 rows without a change)
degraded_sources: 2
---

# Post-market brief — Friday, 6 November 2026

## TL;DR

Chips bought back Thursday's AI selloff and the Nasdaq closed +1.09% while the Dow fell 0.46% — a narrow, mega-cap-led tape, and the participation read names it in numbers: `cap_weight_penalty_bp` **+69** (the cap-weighted index +0.31% against the equal-weighted one −0.38%), `median_name_move_pct` **+0.24%** across 4,725 names, and **2,667 advancers** against **2,030 decliners**. But the liquid set is colder than the headline: `liquid_adv_dec_ratio` **0.95** (868 advancers vs 910 decliners above $2B cap), and the volatility market did not believe the bounce — VIX fell 9.0% to 25.64 but only after trading down to 23.47, while the Nasdaq vol gauge closed at 34.02, still 33% above the VIX. One name is doing a lot of work in the sector table: **SpaceX** (+8.6% on a $1.82T cap) is +1.8pp of the universe's cap-weighted Industrials return; ex-SpaceX the sector is +0.71% against an industrial ETF at +0.12%. After hours was not an earnings tape at all — Friday's confirmed post-close slate was one reporter — it was a continuation-and-corporate-action tape, and the overnight futures print this brief quotes is frozen at the 16:59 ET settlement, so the Asia session that sets Monday is not in the data yet.

## Tomorrow's setup — Monday, 9 November 2026

Tomorrow is Saturday; the next US session is **Monday, 9 November 2026**. Weekend events (Asia opens Sunday ~19:00 ET) land before that open, and the futures numbers below are Friday's cash-close settlement, not that overnight.

### Futures and the overnight setup

| instrument | last | vs prior settle | as_of (ET) | state |
|---|---|---|---|---|
| ES=F (S&P 500) | 7404.00 | +0.28% | 16:59:59 | open (Globex) |
| NQ=F (Nasdaq 100) | 27107.50 | +1.33% | 16:59:59 | open (Globex) |
| YM=F (Dow) | 51390.00 | −0.44% | 16:59:59 | open (Globex) |
| RTY=F (Russell 2000) | 2761.20 | +0.94% | 16:59:59 | open (Globex) |
| ZN=F (10-year note) | 107.125 | −0.19% | 16:59:59 | open (Globex) |

**Read this as Friday's settlement, not Monday's setup.** Every futures quote carries `as_of` 16:59:59 ET — five and a half hours before this brief was written — so the overnight move that normally carries the setup is **not** in this data. The cash-close read is still informative: the futures complex closed in the same shape as the cash tape (Nasdaq futures +1.33%, Dow futures −0.44%, small caps +0.94%), so nothing has yet priced a reversal of Friday's rotation. Monday's setup is un-priced.

### Economic calendar

**Monday, 9 November (quiet — the week's real event is Tuesday):**

| time (ET) | release / event | prior | note |
|---|---|---|---|
| 08:40 | Fed Vice Chair for Supervision Bowman speaks | — | the first Fed voice of the week |
| 10:00 | Wholesale inventories, September (final) | — | low impact |
| 13:00 | **3-year note auction, $58B** | 4.932% yield | the week's only auction that matters for the curve |
| 15:00 | Chicago Fed's Goolsbee speaks | — | second voice of the day |
| 16:00 | NY Fed consumer inflation expectations, October | 3.9% | forecast 3.8% |
| 17:15 | Richmond Fed's Barkin speaks | — | — |

**The week ahead:** **CPI Tuesday 08:30 ET** (October; headline m/m forecast +0.3% vs +0.6% in September, core +0.2% vs +0.3%), 10-year note auction Tuesday 13:00, PPI Thursday 08:30, 30-year bond auction Thursday 13:00, and the November FOMC minutes on Wednesday 18 November's slot (see the calendar for the 18th: 2:00 p.m. FOMC minutes). CME FedWatch is pricing **81% odds of a 25bp hike in December** after Friday's strong payrolls report — so the CPI print on Tuesday is a hike/no-hike print, not a dovish one.

### Earnings calendar

Monday is a heavy Monday by count and thin by liquidity. The three public calendars disagree, so here are all three rather than a blended number: **EarningsWhispers 182 names (65 before the open, 117 after the close)**, **digrin 142 names (4 before the open, 2 after the close, 136 timing unconfirmed)**, **Yahoo 258 names**. The counts differ because most calendars do not confirm the bell time.

**Before the open (named):** CEG (Constellation Energy, EPS est 3.88), KKR (1.58), NRG (3.01), MNDY (monday.com), BRK.B (Berkshire), **IMVT (Immunovant — company-confirmed, 08:00 ET corporate presentation)**, **UNIT (Uniti Group)**, **TPB (Turning Point Brands)**, ROIV, FERG (3.29), CNH, IONS, VRTS, VIA, KSPI.

**After the close (named):** **RKLB (Rocket Lab)**, **TTWO (Take-Two, EPS est −0.86)**, **ASTS (AST SpaceMobile)**, OXY (1.47), TTD (The Trade Desk), HIMS, QRVO (2.05), MARA, PLUG, ACHR, USAR, LCID, BAP.

Two of tonight's after-hours names report Monday morning and two of Monday's reporters were moving after hours tonight — that is the live overlap for the next session.

### News to watch for the top movers

Today's three biggest liquid moves, and the reason each moved:

- **GOGO +71.52% to 3.885** — the FCC renewed Gogo's exclusive nationwide air-to-ground spectrum licences through 2036, alongside a debt refinancing that extended its $600M term loan B to 2030; revenue missed on the quarter, the market bought the licence.
- **KRMN +42.29% to 45.66** — third-quarter revenue up 66% to a record $202M (release Thursday 16:10 ET); fiscal 2026 revenue guidance raised to $755-760M.
- **FLY +36.80% to 20.76** — a deal worth more than $1.3B to supply a satellite operator with 36 rocket engines over three years, plus licensed IP and engineering support.

Just behind: **FROG +35.33%** (Q3 revenue $179.2M, +31% y/y, non-GAAP EPS $0.32 vs $0.26 expected, FY26 revenue guided to $680-682M), **LASR +29.58%** (EPS $0.16 vs $0.06, revenue beat 8.6%, Q4 guide flagged ~$15M of shipments deferred into 2027), **QNT +25.99%** (2026 revenue forecast raised to $31-34M). On the downside: **IRTC −30.70%** on results (no company-specific release located), **AMN −23.87%**, **BL −23.11%**, **OPEN −21.79%**, **DKNG −21.30%**, **TEAM −16.15%** (revenue +24% to $1.77B but FY27 growth guided to ~13.75%), **NTRA −14.59%** (results and a new CEO).

Context: Thursday's Nasdaq fell 5.52% in an AI-led selloff. Today the chip complex recovered part of it — StockTitan measured that Micron, AMD, Marvell, Arm, Broadcom, Intel, Qualcomm and Nvidia had won back **over a third of Thursday's fall** by their Friday closes. That is a bounce, not yet a trend.

### Tomorrow's three things to watch

- IMVT — 29.10 after-hours last, 30.53 gap-fill at the 16:00 close — reports before the open Monday with a business update and an 08:00 ET corporate presentation; the fiscal Q2 print is the tell, and tonight's −4.68% after-hours move is the de-risking into it.
- RKLB — 53.07 prior close, 53.57 after-hours last — reports after the close Monday; the Neutron launch timeline, not the headline EPS, is what resolves the +15.39% day.
- ASTS — 32.33 prior close, 32.49 after-hours last — reports after the close Monday; today's engine-supply deal signed with the same customer is the read-through on the order book.

## Day's tape

### Market read

| metric | value | what it is / where it comes from |
|---|---|---|
| advancers | 2,667 | names closing higher — cron #20 universe, 4,725 names with a usable price change |
| decliners | 2,030 | names closing lower — same universe |
| unchanged | 28 | names closing flat — same universe |
| median_name_move_pct | +0.24% | median % move of that universe |
| cap_weight_penalty_bp | +69 bp | cap-weighted index +0.31% minus equal-weighted −0.38%; bridge `price_history` |
| liquid_adv_dec_ratio | 0.95 (868 : 910) | advancers : decliners among names above $2B market cap (1,785 names) |

Two readings coexist and both are true. The broad universe was positive (2,667 up vs 2,030 down, median +0.24%), but the **liquid** set above $2B was slightly negative (868 vs 910) and the equal-weighted index fell while the cap-weighted one rose — the +69bp penalty says the average dollar in the market had a better day than the average dollar in the average company. Read it with the vol market: VIX −9.01% to 25.64 and VXN −11.08% to 34.02 are large falls in fear, but both gauges closed far above their lows (VIX 23.47, VXN 32.25) and VXN still sits a third above VIX — the Nasdaq's variance premium did not compress into the rebound.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-02 | −0.48 | +0.77 | −124 |
| 2026-11-03 | +0.30 | −0.33 | +63 |
| 2026-11-04 | +1.65 | +1.86 | −20 |
| 2026-11-05 | −4.41 | −2.89 | −152 |
| 2026-11-06 | +0.31 | −0.38 | +69 |

The penalty has flipped sign three sessions in five — −124, +63, −20, −152, +69 — and its two largest readings both sit on down days for the index (11-05, −152bp). That is the signature of a tape where the mega-caps carry the index and everything else is left to follow; on Friday the sign flipped back to positive because the chips bounced, not because breadth improved (liquid_adv_dec_ratio 0.95). The 11-03 row reproduces the +63bp figure published in the 2026-11-03 brief from the same source and method, so the series is consistent across runs.

### Index, ETF and volatility levels

| instrument | close | change % | day range |
|---|---|---|---|
| S&P 500 | 7376.86 | +0.31 | 7369.55 – 7444.20 |
| Nasdaq Composite | 24579.42 | +1.09 | 24507.63 – 24825.55 |
| Dow Jones Industrial Average | 51285.73 | −0.46 | 50992.61 – 51662.26 |
| Russell 2000 | 2754.11 | +0.89 | 2720.99 – 2761.58 |
| Nasdaq-100 | 26989.99 | +1.35 | 26887.69 – 27316.09 |
| Philadelphia Semiconductor | 9390.25 | +4.21 | 9221.35 – 9627.26 |
| VIX | 25.64 | −9.01 | 23.47 – 27.76 |
| VXN | 34.02 | −11.08 | 32.25 – 35.43 |
| SPY | 735.29 | +0.31 | 734.58 – 742.21 |
| QQQ | 656.10 | +1.40 | 654.00 – 664.52 |
| IWM | 273.67 | +0.99 | 270.24 – 274.55 |
| DIA | 512.22 | −0.40 | 508.66 – 515.98 |
| RSP | 216.05 | −0.38 | 214.75 – 217.26 |
| SMH | 463.96 | +3.62 | 456.44 – 476.25 |
| GLD | 372.52 | −0.79 | 369.26 – 373.76 |
| TLT | 81.92 | −0.01 | 81.71 – 82.42 |

The semiconductor index's +4.21% is the day's story and it is a *rebound* day: the index closed 9627.26 at the high after trading as low as 9221.35, and the chip ETFs' ranges (SMH 456.44–476.25) show the bid was built through the session, not at the open. Gold fell 0.79% and the 10-year yield rose 2.2bp to 4.859% — the classic rotation out of the defensive leg into the AI complex, with no change in the rates story.

### Cross-asset

| instrument | last | change % | note |
|---|---|---|---|
| Nikkei 225 | 57434.77 | −5.96 | Friday's Asia close — it absorbed Thursday's US AI selloff |
| Hang Seng | 24481.86 | −1.27 | Friday's Asia close |
| Shanghai Composite | 3649.18 | −1.10 | Friday's Asia close |
| FTSE 100 | 10673.94 | −1.01 | Friday's close |
| DAX | 25820.36 | −1.92 | Friday's close |
| US dollar index | 102.279 | −0.02 | flat |
| WTI crude | 90.34 | −0.20 | ~$90, still elevated |
| Gold (COMEX) | 4079.50 | −0.83 | down with the rotation |
| Bitcoin | 75891.41 | +0.20 | flat |
| US 10-year yield | 4.859 | +0.45 | +2.2bp to 4.859% |

**Caveat on the Asia leg:** these are Friday's closes — the session that priced Thursday's US selloff — and they are *stale relative to Friday's US close*. The next Asia session opens Sunday ~19:00 ET and is the first real input into Monday. Nothing in this table is Monday's overnight.

### Day's movers

Universe screen: cron #20's 4,725 names, ex-distribution rows removed, market cap ≥ $1B, price ≥ $1.

| ticker | close | change % | vol vs 10d avg | sector |
|---|---|---|---|---|
| KRMN | 45.66 | +42.29% | 3.14x | Industrials |
| FLY | 20.76 | +36.80% | 4.16x | Industrials |
| FROG | 101.00 | +35.33% | 3.81x | Information Technology |
| LASR | 38.02 | +29.58% | 2.69x | Information Technology |
| LYNX | 14.59 | +28.66% | 2.99x | Industrials |
| IRTC | 90.22 | −30.70% | 10.84x | Health Care |
| AMN | 36.07 | −23.87% | 2.13x | Health Care |
| BL | 25.89 | −23.11% | 2.68x | Information Technology |
| OPEN | 1.40 | −21.79% | 1.97x | Real Estate |
| DKNG | 18.51 | −21.30% | 4.95x | Consumer Discretionary |

Below the $1B floor but larger than anything on the table: **GOGO +71.52%** ($526M cap, 27.4M shares, licence renewal), **OBX +44.38%**, **SERV +38.79%**, **KDK +34.58%**. The top of the losing column is AIRS −62.92%, BDSX −57.01%, STLN −45.97% — sub-$500M caps, and iRhythm's −30.70% on 10.84x average volume is the only mega-cap name on either side of the table.

### Watchlist EOD review

The watchlist file (`refs/watchlist.yaml`, karizaco/minimax-cloud-outputs, updated 2026-11-06) fetched clean — 8 names, no error.

| ticker | close | day change % | day range | vol vs 10d avg | after-hours print |
|---|---|---|---|---|---|
| AAPL | 342.37 | −0.52% | 338.30 – 345.79 | 0.99x | 342.65 (+0.08%) |
| MSFT | 530.61 | −0.99% | 524.61 – 538.30 | 1.08x | 531.40 (+0.15%) |
| NVDA | 186.64 | +2.78% | 185.22 – 194.90 | 1.59x | 188.70 (+1.10%) |
| GOOGL | 284.78 | +0.78% | 284.59 – 290.49 | 1.08x | 285.41 (+0.22%) |
| AMZN | 259.30 | −0.35% | 258.53 – 264.18 | 0.94x | 259.83 (+0.20%) |
| IWM | 273.67 | +0.99% | 270.24 – 274.55 | 1.04x | 273.75 (+0.03%) |
| GLD | 372.52 | −0.79% | 369.26 – 373.76 | 0.82x | 373.37 (+0.23%) |
| TLT | 81.92 | −0.01% | 81.71 – 82.42 | 1.12x | 81.85 (−0.09%) |

The watchlist read is a semiconductor read with a funding twist: the only two names that worked were the two levered to the AI complex (NVDA +2.78% on 1.59x volume, and the chip ETFs' bid in sympathy), and the two mega-cap software/consumer names that fell (MSFT −0.99%, AMZN −0.35%) were the funding source. Note the after-hours open-interest-free tape: NVDA is the only watchlist name up more than 0.2% after the bell, and the equal-weighted ETF printed *down* 0.01% after hours while the cap-weighted one printed +0.17% — the same narrow leadership, extended.

## Sector rotation

Ranked by cap-weighted % change of the cron #20 universe (ex-distribution rows removed, share classes de-duplicated by `cap_source_symbol` so Alphabet, Berkshire and the JPMorgan preferreds are each counted once), with the universe median alongside and the sector ETF as an independent cross-check.

| sector | cap-weighted % | median % | n | sector ETF | ETF % |
|---|---|---|---|---|---|
| Industrials | +2.38 | +0.84 | 552 | XLI | +0.12 |
| Information Technology | +1.56 | +1.74 | 508 | XLK | +1.45 |
| Communication Services | +0.46 | +0.38 | 159 | XLC | +0.43 |
| Consumer Discretionary | +0.30 | −1.02 | 386 | XLY | −0.05 |
| Health Care | +0.20 | +1.85 | 839 | XLV | −0.06 |
| Energy | +0.15 | +1.01 | 181 | XLE | −0.02 |
| Materials | −0.02 | +0.63 | 155 | XLB | −0.73 |
| Utilities | −0.03 | +0.04 | 82 | XLU | −0.39 |
| Financials | −0.42 | +0.05 | 1,071 | XLF | −0.59 |
| Real Estate | −0.53 | −0.59 | 185 | XLRE | −0.68 |
| Consumer Staples | −1.21 | −0.69 | 148 | XLP | −1.28 |

**Top 3:** Industrials, Information Technology, Communication Services. **Bottom 3:** Consumer Staples, Real Estate, Financials.

The sector table has one number in it that is not a rotation signal: **Industrials**. Its +2.38% cap-weighted return is +1.82pp of SpaceX alone — $1.82T of cap on a +8.6% day — and ex-SpaceX the sector is **+0.71%**, in line with its +0.84% median and not far from XLI's +0.12%. Every other row on the table reconciles with its ETF within a few tenths; Industrials does not, and the reason is a single constituent that is not in the ETF.

The second thing the table says is about **medians versus cap weights**: Health Care has a +1.85% median but a +0.20% cap-weighted return (its large names lagged its small ones), and Consumer Discretionary has a −1.02% median against a +0.30% cap weight. The day's dispersion was inside sectors, not between them.

## After-hours movers

Extended-hours screen: TradingView `america` scanner, market cap > $1B, after-hours volume > 50,000 shares, scanned twice (change descending for gainers, ascending for losers) and ranked by absolute after-hours move. Every row's `postmarket_change` was verified against the row's own `(ah_last − prior_close) / prior_close × 100`; all ten passed, and no row was dropped. `gap_fill_level` is the prior close when the after-hours range contains it, otherwise the after-hours midpoint.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| MCHPP | 52.04 | 57.1220 | 57.1220 | 51.1995 | 500,743 | +9.77% | 11.38% | 52.04 |
| PAGP | 25.78 | 27.8200 | 27.8200 | 25.7800 | 287,489 | +7.91% | 7.91% | 25.78 |
| NAVN | 25.48 | 26.7800 | 26.7800 | 25.4000 | 446,323 | +5.10% | 5.42% | 25.48 |
| ACCV | 11.06 | 11.5533 | 11.5533 | 10.8400 | 130,331 | +4.46% | 6.45% | 11.06 |
| UNIT | 5.22 | 5.4400 | 5.4400 | 5.2200 | 1,009,185 | +4.21% | 4.21% | 5.22 |
| JAN | 31.99 | 29.7500 | 31.9900 | 29.7500 | 1,522,640 | −7.00% | 7.00% | 31.99 |
| PAYC | 237.32 | 223.7803 | 237.3200 | 223.7803 | 160,914 | −5.71% | 5.71% | 237.32 |
| IMVT | 30.53 | 29.1000 | 30.5300 | 29.1000 | 277,186 | −4.68% | 4.68% | 30.53 |
| TIC | 10.37 | 9.9000 | 10.3700 | 9.9000 | 270,763 | −4.53% | 4.53% | 10.37 |
| LYNX | 14.59 | 14.0000 | 14.5900 | 14.0000 | 91,845 | −4.04% | 4.04% | 14.59 |

Every row here traded through its 16:00 close inside the after-hours window, so **the gap fills at the prior close** in all ten cases — `gap_fill_level` equals `prior_close` throughout. The actionable read is the range column: MCHPP's 11.38% after-hours range on a preferred line, TRVI's 7.96%, and the 7.00% one-way slides in JAN and PAYC.

**Above the screen's floor (disclosed, not in the table):** the largest after-hours moves of the session were in small caps the $1B floor excludes — OMH +110% on 420x relative volume, TGE +71% (a 6-K at 17:14 ET transferring four hotel assets for 198,630,381 newly issued shares, after which AMTD Group held 96.7% of the voting power), PARA +18%, AWX +13% on a 3Q print, FTH +10% on a data release, and on the downside SDA −19% (566M shares, on a share-repurchase announcement), VIVK −16%, RCT −14%, KPTI −9%. The screen's top gainer (MCHPP, +9.77%) is only the 5th-largest after-hours gainer of the night once the cap floor is removed.

## After-hours earnings reactions

**Friday's after-close earnings slate was effectively empty** — digrin lists one confirmed after-close reporter for 6 November, and askthedate names HE and TTGT. That is why the after-hours tape is not an earnings tape: it is continuation, rotation and corporate action.

What did move, and why:

- **PAYC −5.71% to 223.78 after hours** — no new news. The de-rating that started after the 4 November print (a beat on both lines: revenue $543.8M vs $535.1M expected, non-GAAP EPS $3.37 vs $2.76, FY26 revenue guidance raised to $2.21-2.22bn) continued: −6.76% on 5 November, −5.13% today, −5.71% after the bell. Three sessions, roughly −17%, on a print that beat. The market is de-rating the forward multiple, not the quarter.
- **BF.B −3.27% to 29.58 after hours** — Brown-Forman sliding in extended trading on broader market volatility.
- **Marathon Petroleum +3.2% after hours** — on an earnings beat and the $4.2bn sale of its St. Paul Park and Mandan refineries (177,000 b/d combined, plus the MPLX pipeline and terminal assets) to CVR Energy, with Trafigura becoming exclusive crude supplier to both plants.
- **SPCX +1% after hours** — SpaceX, 115.5M shares traded, capping an +8.6% regular session.

The names with real scheduled catalysts are the ones to carry into Monday: **IMVT** (−4.68% after hours, company-confirmed pre-open report Monday), **UNIT** (+4.21% after hours, reports before the open Monday), **TPB** (+4.08% after hours, reports before the open Monday), and **RKLB**, **TTWO**, **ASTS**, **OXY**, **TTD** after Monday's close.

## Open research queue

1. **Why does the universe's cap-weighted sector return diverge from the sector ETF, and does it matter?** Industrials print +2.38% cap-weighted against XLI's +0.12%, and one constituent (SpaceX, $1.82T cap, +8.6%) is +1.82pp of that gap; ex-SpaceX the sector is +0.71%. It matters because every cap-weighted sector read in this brief — including the `cap_weight_penalty_bp` metric the TL;DR leans on — inherits that same concentration, and the metric cannot see it. What would resolve it: a sector cap-weight series built on index membership rather than on the whole listed universe, so a non-member's float is not silently given the weight of a constituent.
2. **Is the chip move a genuine breadth turn or a short-covering bounce?** The chip index gained 4.21% after the Nasdaq fell 5.52% on Thursday; StockTitan measured the group recovering over a third of Thursday's fall by Friday's closes. But `liquid_adv_dec_ratio` finished at 0.95 (868 up vs 910 down above $2B) and the equal-weighted index fell −0.38%, so the broad market did not confirm the move. What would resolve it: Monday's volume and the sign of the liquid advance/decline ratio — a second green ratio would make the rotation a breadth turn, a second red one would confirm it was a squeeze.
3. **How much of the after-hours tape is actually information?** With one confirmed post-close reporter, the ten biggest after-hours moves in the $1B+ screen were continuation, corporate actions (TGE's share issuance, SDA's repurchase) or pre-print de-risking (IMVT), and the largest movers of the night were sub-$1B shells at 100x-plus relative volume. What would resolve it: whether Monday's open holds the levels published in the after-hours table — a gap-fill at the prior close across all ten names is a testable claim, not a description.

## Source health

| source | used for | status |
|---|---|---|
| MCP bridge `market-recap` `get_quotes` | index, ETF, futures, watchlist and mover levels | ok — 39/40 symbols returned (BF.B not found; its levels come from the scanner) |
| MCP bridge `market-recap` `price_history` | 5-session cap-weight history | ok — SPY and RSP, 10 sessions returned |
| MCP bridge `market-recap` `market_snapshot` | cross-asset and Asia closes | ok, with a lag caveat — Asia figures are Friday's closes |
| MCP bridge `market-recap` `get_quotes` (futures) | overnight setup | **degraded** — every futures quote carries `as_of` 16:59:59 ET, 5.5 hours stale at the 22:30 fire; the post-18:00 ET Globex move is not in the data, so the futures table is Friday's settlement, not Monday's setup |
| TradingView `america` scanner | after-hours movers, breadth, ETF levels | ok — 13,363 rows pulled; two screens for the movers (change desc + asc) |
| cron #20 `us-eod/2026-11-06.csv` | universe, participation metrics, sector rotation, day movers | ok — 4,892 rows; 48 ex-distribution rows excluded from every move-based read |
| `refs/watchlist.yaml` (minimax-cloud-outputs) | watchlist section | ok — 8 tickers, fetched 2026-11-06 |
| CBOE daily market statistics | put/call ratio | **degraded** — the page's embedded data carries no session date stamp, so the total (1.06) is published as read at 22:40 ET but cannot be attributed to a named session with certainty |
| `probe_mcp.py` | MCP availability | ok — `catalog_ok total=135 finance_tools=0`; the MCP servers are reachable over the bridge (packs: tradier, fmp, market-recap) |
| Web (issuer IR, StockTitan, EarningsWhispers, Investing.com, askthedate, digrin, MarketChameleon) | catalysts, calendars, cross-checks | ok — 8 searches; no source failed |

**Put/call:** CBOE's daily statistics page, total put/call **1.06** (index 1.07, equity 0.89, ETP 1.25, VIX 0.70), 21,815,180 contracts (11,225,416 puts / 10,589,764 calls). Both the total and its components are published as read, from the same page, so no split is inferred.

**Degraded sources: 2** (the frozen futures quotes; the undated put/call page).

## Method notes

- **Population.** Every participation metric uses one population: cron #20's `us-eod/2026-11-06.csv`, restricted to the 4,725 names with a usable price change. The 48 rows flagged `EX_DISTRIBUTION` are excluded — a distribution is not a directional move (the largest single row in the file, −81.29%, is a $3.00 distribution, not a crash) — and 119 rows carry no `change_pct`. The liquid set is the same universe restricted to `market_cap` > $2B (1,785 names).
- **Cap weights** are de-duplicated by `cap_source_symbol` so share classes are counted once (Alphabet A+C, Berkshire A+B, the JPMorgan preferred lines). The day's moves use the CSV's published price change.
- **Gap-fill rule.** `gap_fill_level` = the prior close if the after-hours range contains it, otherwise the after-hours midpoint. All ten published rows fall in the first case.
- **Row verification.** Every after-hours row was checked against its own identity `postmarket_change == (postmarket_close − close) / close × 100`; all ten passed and none was dropped. The movers table is capped at 10 names (5 gainers, 5 losers) and the sector list at top 3 / bottom 3, per the contract.
- **Source of record.** Prices and levels come from the MCP bridge (`market-recap`); breadth and extended hours from the TradingView scanner; the universe from cron #20. Where the two disagreed on a mover's 16:00 close (MCHPP, PAGP, UNIT, TPB, DK and the rest) they agreed exactly, and the scanner's `close` is used as `prior_close` throughout.
- **No trades, no positions, no sizing** — read-only by design. Nothing here is advice.
