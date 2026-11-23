# Cron #05 eod-international-daily — Monday, 23 November 2026

## TL;DR

- **A violent risk-on rebound after Friday's AI rout.** Nvidia reinstated Jensen Huang as CEO with immediate effect and its shares surged 33%, lifting the Nasdaq 6.7% and the S&P 500 more than 4%, and every European board followed: the STOXX 600 **+1.81%** to 636.97, the DAX **+2.15%** to 25,337.27 (its first close back above 25,000), the CAC 40 +1.48%, the FTSE MIB +0.65%, the TSX **+2.69%** to 34,081.44 and the TAIEX **+2.16%** to 36,811.89 after a 1,213-point intraday swing. **2,841 names were published across 15 of the 16 boards** - **Tokyo was closed**, so Japan contributes no rows and its index level above is the 20 November session, while the ASX 200 was the one major board left behind at **-0.26%** to 8,570.60, an eighth straight fall, because the session opened before Wall Street's recovery had been priced.
- **The one consequential move was the AI-hardware complex reversing, with gold miners running alongside it.** The names a US trader can actually reach: **ASML +8.92%** (ADR), **ASM International +8.29%** (ADR), **Infineon +6.56%** (ADR), **AIXTRON +8.91%** (ADR), **AT&S +13.03%** (OTC), **ams-OSRAM +11.03%** (ADR), **BE Semiconductor +9.25%** (ADR), **Technoprobe +8.75%** (ADR), **Prysmian +6.52%** (ADR), **Shopify +8.96%** (NASDAQ), **BlackBerry +8.38%** (NYSE), **Capstone Copper +8.36%** (ADR) and **Fincantieri +5.24%** (OTC). In Taiwan the same trade closed at the limit: **MediaTek +10.00%**, **Delta Electronics +10.00%**, **UMC +9.96%**, **Elite Material +9.96%**, **Powerchip +9.98%**, with 68 names closing limit-up. Gold recovered 2-4% from a 14-month low and took the Canadian gold complex with it - **Montage Gold +12.46%**, **Seabridge +11.45%**, **G Mining +10.93%**, **Hudbay +10.87%**, and **Sitka Gold +23.53%** after AngloGold Ashanti agreed to buy a 15% stake for at least US$72.8m.
- **The caveat that changes how to read it: `market_cap` is in USD while `open`/`high`/`low`/`close` are in the listing currency** (the `currency` column says which) - and three further facts change the numbers themselves. **Tokyo did not trade**: the TSE was shut for Labor Thanksgiving Day with JPX BCP testing from 21 to 23 November, so Japan has no rows at all and the only Japan level published is the 20 November session. Taiwan's **+10.00% prints are limit prices, not calculated moves**, and the FSC's ban on short selling below the previous close is what produced the Taiwan limit-up cluster. Two rows carry a **contract-adjustment artefact** and are kept out of every table: **ASX:ZIP +363.50%** (a 1-for-5 consolidation; the real move is about -7.3%) and **EURONEXT:ALAGR +11,119.51%** (a 210-share price-basis artefact).

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| au | 1 | 1545 | 1545 | 294 | $300M + vol >= 100,000 | 4 | 1230 | 16 | 1 | 0 | 3 | 0 |
| tw | 2 | 2343 | 2343 | 777 | $200M | 58 | 1508 | 0 | 0 | 0 | 1 | 0 |
| ca | 3 | 4284 | 2704 | 598 | $200M | 64 | 1918 | 0 | 124 | 0 | 22 | 0 |
| eu-de | 1 | 4302 | 708 | 122 | $300M + vol >= 50,000 | 4 | 401 | 181 | 0 | 0 | 0 | 0 |
| eu-fr | 1 | 542 | 542 | 258 | $100M | 1 | 283 | 0 | 0 | 0 | 4 | 0 |
| eu-it | 1 | 378 | 378 | 177 | $100M | 2 | 199 | 0 | 0 | 0 | 4 | 0 |
| eu-es | 1 | 230 | 230 | 134 | $100M | 24 | 72 | 0 | 0 | 0 | 17 | 0 |
| eu-nl | 1 | 78 | 78 | 55 | $100M | 0 | 23 | 0 | 0 | 0 | 0 | 0 |
| eu-be | 1 | 101 | 101 | 76 | $100M | 1 | 24 | 0 | 0 | 0 | 2 | 0 |
| eu-at | 1 | 65 | 65 | 49 | $100M | 2 | 14 | 0 | 0 | 0 | 4 | 0 |
| eu-pt | 1 | 30 | 30 | 26 | $50M | 0 | 4 | 0 | 0 | 0 | 1 | 0 |
| eu-ie | 1 | 19 | 19 | 16 | $200M | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| eu-fi | 1 | 189 | 189 | 101 | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| eu-dk | 1 | 133 | 133 | 75 | $100M | 1 | 57 | 0 | 0 | 0 | 1 | 0 |
| eu-gr | 1 | 127 | 127 | 83 | $50M | 0 | 44 | 0 | 0 | 0 | 1 | 0 |
| **total** | | 14366 | 9192 | **2841** | | 165 | 5864 | 197 | 125 | 0 | 60 | 0 |

**`jp` has no row in this table because there was no Japanese session.** The Tokyo Stock Exchange was **closed on 23 November for Labor Thanksgiving Day** (JPX's own market-holidays calendar; the JPX derivatives notice of 20 November adds that the group ran BCP testing from 21 to 23 November). The session probe answered `traded=unknown` - its last bar is 2026-11-20 - and the closure was confirmed three ways before the region was removed: Yahoo's daily bars for `^N225` **and** for TSE constituents (`9984.T`, `7203.T`, `6758.T`, `8306.T`) all stop at 20 November; the JPX calendar names the day; and the TradingView Japan pull returned the 20 November session **verbatim** - `TSE:9984` close 3,025 with a -14.4755% change and volume 109,918,800, byte-identical to the 20 November published row. A confirmed closure means the region is **removed** from the artifact (no `jp.csv`, no rows in any table, a `closed_regions` block in `_manifest.json`), because building it would publish the last session's close AND its last session's move under today's date. Japan's last-session index levels are in the table below, carrying 20 November's date.

The exclusion counts are the per-reason counts in `_excluded.json`, not estimates. The reconciliation identity `unique_instruments == written + sum(excluded)` holds for every region.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 8,570.60 | -22.00 / -0.26% | 2026-11-23 | TradingView SP:XJO; samso Market Update, 23 Nov (close 4:30pm AEDT) and ABC's live blog both report 8,570.60, down 22.0 points or 0.26% - an eighth straight falling session, opened -0.6% |
| jp | Nikkei 225 | 56,436.65 | -3,007.56 / -5.06% | 2026-11-20 | **shut 23 Nov - Labor Thanksgiving Day** (JPX market-holidays calendar; the JPX derivatives notice adds that the group ran BCP testing from 21 to 23 November). This is the LAST session's close (20 Nov), carried with that session's date; TradingView TVC:NI225 repeats the 20 November level and its -5.06% change, and Yahoo's daily bars for ^N225 and for TSE constituents (9984.T, 7203.T, 6758.T, 8306.T) all stop at 2026-11-20 |
| jp | TOPIX | 3,674.22 | -3.88% | 2026-11-20 | **shut 23 Nov - Labor Thanksgiving Day**; the 20 November session's close, carried with that session's date (TradingView TSE:TOPIX) |
| tw | TAIEX | 36,811.89 | +778.60 / +2.16% | 2026-11-23 | TradingView TWSE:IX0001; CNA (Focus Taiwan) and TVBS World Taiwan report the close at 36,811.89, up 778.60 points or 2.16%, after a 1,213.07-point swing between 35,442.41 and 37,108.20, on turnover of about NT$1.08tn |
| ca | S&P/TSX Composite | 34,081.44 | +2.69% | 2026-11-23 | TradingView TSX:TSX; Reuters had it up 2.78% at 34,111.75 by 10:08 ET - the biggest intraday jump since April 2025 - with the materials sector up 6.2% |
| eu-de | DAX | 25,337.27 | +534.49 / +2.15% | 2026-11-23 | TradingView XETR:DAX and the Xetra official close of 23 Nov 17:50 (dpa-AFX via vwd/tradegate): 25,337.27, up 534.49 or 2.15% - the first close back above 25,000 since the rout began |
| eu-fr | CAC 40 | 8,044.84 | +1.48% | 2026-11-23 | TradingView EURONEXT:PX1 and ideal-investisseur's 17:35 close table: 8,044.84, +1.48%, with the SBF 120 up 1.47% |
| eu-it | FTSE MIB | 49,021.93 | +0.65% | 2026-11-23 | TradingView FTSE:FTSEMIB and Borsa Italiana's close report: 49,021.93, +0.65% - the gain was capped by the ex-dividend adjustment on nine major companies (worth about -1.41%) |
| eu-es | IBEX 35 | 19,181.10 | +1.63% | 2026-11-23 | TradingView BME:IBC |
| eu-nl | AEX | 1,089.08 | +2.15% | 2026-11-23 | TradingView EURONEXT:AEX |
| eu-be | BEL 20 | 5,887.79 | +1.55% | 2026-11-23 | TradingView EURONEXT:BEL20 |
| eu-at | ATX | 6,342.01 | +2.22% | 2026-11-23 | TradingView VIE:ATX |
| eu-pt | PSI 20 | 9,315.86 | +0.39% | 2026-11-23 | TradingView EURONEXT:PSI20 |
| eu-ie | ISEQ | 14,641.94 | +1.83% | 2026-11-23 | TradingView EURONEXT:ISEQ |
| eu-fi | OMX Helsinki 25 | 6,013.38 | +1.83% | 2026-11-23 | TradingView OMXHEX:OMXH25 |
| eu-dk | OMX Copenhagen 20 | 1,615.46 | +1.33% | 2026-11-23 | TradingView OMXCOP:OMXC20 |
| eu-gr | ATHEX General | 2,562.36 | +9.66 / +0.38% | 2026-11-23 | **Euronext Athens' own index page** (the ATHEX Composite Share Price Index, GD): close 2,562.36, high 2,570.53, low 2,524.13, +0.38%, volume 53,506,686, turnover EUR413.18m - the venue's own print, since the ATHEX has no Yahoo symbol and no TradingView venue index |
| *context* | STOXX 600 | 636.97 | +1.81% | 2026-11-23 | TradingView STOXX:SXXP; Reuters had the pan-European index up 1.5% at 14:34 GMT in the middle of the session, its biggest one-day jump since 9 November, after five consecutive falls |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 291 | -0.42% | 111 / 168 / 12 | -12.23% | +363.50% |
| tw | 776 | +1.19% | 499 / 231 / 46 | -9.98% | +17.06% |
| ca | 576 | +1.22% | 422 / 134 / 20 | -15.04% | +23.53% |
| eu-de | 122 | +1.65% | 98 / 22 / 2 | -5.73% | +13.32% |
| eu-fr | 254 | +0.38% | 143 / 81 / 30 | -13.66% | +11119.51% |
| eu-it | 173 | +1.00% | 124 / 40 / 9 | -4.03% | +17.24% |
| eu-es | 117 | +0.50% | 70 / 29 / 18 | -2.83% | +12.15% |
| eu-nl | 55 | +1.27% | 41 / 13 / 1 | -3.16% | +9.25% |
| eu-be | 74 | +0.63% | 50 / 19 / 5 | -2.92% | +6.57% |
| eu-at | 45 | +1.90% | 31 / 10 / 4 | -4.13% | +13.03% |
| eu-pt | 25 | +0.00% | 10 / 12 / 3 | -2.65% | +3.21% |
| eu-ie | 16 | +0.79% | 11 / 5 / 0 | -6.91% | +19.33% |
| eu-fi | 101 | +0.82% | 69 / 29 / 3 | -6.96% | +8.91% |
| eu-dk | 74 | +1.16% | 59 / 9 / 6 | -3.11% | +7.23% |
| eu-gr | 82 | -0.21% | 27 / 45 / 10 | -4.83% | +5.29% |

The breadth table is computed from the written rows, so an index move and the typical name can disagree. On this session **the typical name lagged its index almost everywhere**: Australia (index -0.26% against a median published name of **-0.42%**), Taiwan (index +2.16% against a median published name of **+1.19%**), Canada (index +2.69% against a median published name of **+1.22%**), Germany (index +2.15% against a median published name of **+1.65%**), France (index +1.48% against a median published name of **+0.38%**), Spain (index +1.63% against a median published name of **+0.50%**), the Netherlands (index +2.15% against a median published name of **+1.27%**), Belgium (index +1.55% against a median published name of **+0.63%**), Austria (index +2.22% against a median published name of **+1.90%**), Portugal (index +0.39% against a median published name of **+0.00%**), Ireland (index +1.83% against a median published name of **+0.79%**), Finland (index +1.83% against a median published name of **+0.82%**), Denmark (index +1.33% against a median published name of **+1.16%**), Greece (index +0.38% against a median published name of **-0.21%**). The rebound was **narrow**: the index was carried by the AI-hardware names - Jenoptik +13.32%, AIXTRON +8.91%, ASML +8.92%, BE Semiconductor +9.25% - while the median name lagged behind them, because the boards that rallied on the AI trade are the ones whose weighting is concentrated in it. The sharpest disagreement is **Greece**, where the index closed up +0.38% while the median published name was **-0.21%** - a board that rose on its index heavyweights alone. The opposite case is Italy, where the median name rose harder than the index.

**The `Min` and `Max` columns carry the two contract-adjustment rows** - `ASX:ZIP` at +363.50% and `EURONEXT:ALAGR` at +11,119.51% - because the breadth table is computed from the written rows and those rows stay in the CSVs with the source's own field. They are excluded from every published table; the arithmetic is explained in the caveats.

## Top movers

Liquid names (volume ≥ 100,000, market cap at or above the region's floor) whose move cleared ±5%, with the driver that was actually sourced, largest absolute move first within the region. A row with no sourced driver is not here - it is under `## No catalyst`. Each region also publishes its single biggest liquid mover even when it did not clear ±5%, so no region is silent; a region with no name at all says so instead of publishing an unsourced row.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:ALQ` | ALS Ltd. | **-12.23%** | 16.94 AUD | 3,199,681 | $6.50B | none | Fell 12.23% to 16.94 AUD - a 52-week low, on its H1 FY27 result: statutory net profit jumped 110% to just under A$300m and underlying NPAT rose 23.6% to A$214.6m (a record, ahead of consensus) with the interim dividend lifted 20% to 23.3 cents - but Life Sciences revenue fell 6.6% and its EBIT margin contracted about 95bp to 13.7% on weak US Environmental and Nuvisan results, and the company cut its Life Sciences growth outlook; Barrenjoey and Macquarie both trimmed their price targets (ABC live blog, 23 Nov; Investing.com, 23 Nov; samso Market Update, 23 Nov) |
| `ASX:SGM` | Sims Ltd. | **+9.69%** | 21.28 AUD | 1,324,758 | $2.48B | ADR | Rose 9.69% to 21.28 AUD - the top mover on the ASX 200, on mixed broker reaction - Macquarie downgraded the waste-management and recycler while Jefferies raised its price target (ABC live blog, 23 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TWSE:2308` | Delta Electronics, Inc. | **+10.00%** | 990 TWD | 31,400,403 | $70.91B | none | Rose 10.00% to 990 TWD - locked at its limit-up price in the power-management and AI-server rebound, after its odd-lot trading value rose more than 80% on Friday's -10% limit-down close (CNA via Focus Taiwan, 23 Nov; Taipei Times, 23 Nov) |
| `TWSE:2454` | MediaTek Inc | **+10.00%** | 3685 TWD | 17,907,134 | $162.29B | none | Rose 10.00% to 3685 TWD - locked at its limit-up price and led the large-cap technology rebound; its Nvidia partnership - a convertible-bond investment and co-development of next-generation AI computing platforms - and reports that Google may redirect TPU chip orders toward MediaTek amplified the move (CNA via Focus Taiwan, 23 Nov; Investing.com, 23 Nov) |
| `TWSE:3665` | BizLink Holding Inc. | **+10.00%** | 1430 TWD | 4,327,818 | $7.87B | none | Rose 10.00% to 1430 TWD - locked at its limit-up price - one of the thousand-dollar stocks (Alchip-KY, Elite Material, Phison, BizLink-KY and Accton Technology) that all closed limit up (UURL, 23 Nov) |
| `TWSE:2368` | Gold Circuit Electronics Ltd | **+9.99%** | 782 TWD | 15,044,815 | $11.32B | none | Rose 9.99% to 782 TWD - locked at its limit-up price - with no company-specific release found for 23 November - it closed at its **+10% limit price** with the AI-supply-chain complex, after Taiwan's Financial Supervisory Commission banned short selling below the previous day's closing price and raised the short-sale margin from 130% to 150% effective 23 November, and the National Stabilization Fund confirmed it had entered the market (its 10th activation, with about NT$500bn available) (TVBS World Taiwan, 23 Nov; UURL, 23 Nov) |
| `TWSE:6213` | ITEQ Corporation | **+9.99%** | 391 TWD | 27,929,382 | $3.92B | none | Rose 9.99% to 391 TWD - locked at its limit-up price - with no company-specific release found for 23 November - it closed at its **+10% limit price** with the AI-supply-chain complex, after Taiwan's Financial Supervisory Commission banned short selling below the previous day's closing price and raised the short-sale margin from 130% to 150% effective 23 November, and the National Stabilization Fund confirmed it had entered the market (its 10th activation, with about NT$500bn available) (TVBS World Taiwan, 23 Nov; UURL, 23 Nov) |
| `TWSE:6139` | L&K Engineering Co. Ltd. | **+9.98%** | 551 TWD | 3,782,499 | $3.58B | none | Rose 9.98% to 551 TWD - locked at its limit-up price - with no company-specific release found for 23 November - it closed at its **+10% limit price** with the AI-supply-chain complex, after Taiwan's Financial Supervisory Commission banned short selling below the previous day's closing price and raised the short-sale margin from 130% to 150% effective 23 November, and the National Stabilization Fund confirmed it had entered the market (its 10th activation, with about NT$500bn available) (TVBS World Taiwan, 23 Nov; UURL, 23 Nov) |
| `TWSE:6770` | Powerchip Semiconductor Manufacturing Corp. | **+9.98%** | 48.5 TWD | 106,711,351 | $6.30B | none | Rose 9.98% to 48.5 TWD - locked at its limit-up price with the memory complex - Powerchip, Winbond, Macronix and Nanya all rebounded 3-4% intraday while PSMC, Phison, Transcend, Innodisk and Silicon Power closed limit up (BigGo Finance, 23 Nov; UURL, 23 Nov) |
| `TWSE:2383` | Elite Material Co., Ltd. | **+9.96%** | 3090 TWD | 8,686,513 | $30.54B | none | Rose 9.96% to 3090 TWD - locked at its limit-up price - one of the thousand-dollar stocks that closed limit up in the substrate complex (UURL, 23 Nov) |
| `TWSE:6526` | Airoha Technology Corp. | **+9.96%** | 607 TWD | 1,501,241 | $2.80B | none | Rose 9.96% to 607 TWD - locked at its limit-up price - with no company-specific release found for 23 November - it closed at its **+10% limit price** with the AI-supply-chain complex, after Taiwan's Financial Supervisory Commission banned short selling below the previous day's closing price and raised the short-sale margin from 130% to 150% effective 23 November, and the National Stabilization Fund confirmed it had entered the market (its 10th activation, with about NT$500bn available) (TVBS World Taiwan, 23 Nov; UURL, 23 Nov) |
| `TWSE:2303` | United Microelectronics Corp. | **+9.96%** | 88.3 TWD | 300,769,461 | $30.54B | ADR | Rose 9.96% to 88.3 TWD - locked at its limit-up price and became the bellwether for the bulls after hitting the limit-up price shortly after the open on 31,134 lots worth more than NT$2.6bn (BigGo Finance, 23 Nov; TVBS World Taiwan, 23 Nov) |
| `TWSE:2451` | Transcend Information, Inc. | **+9.95%** | 232 TWD | 6,408,726 | $2.76B | none | Rose 9.95% to 232 TWD - locked at its limit-up price in the memory rebound (UURL, 23 Nov) |
| `TPEX:6274` | Taiwan Union Technology Corporation | **+9.95%** | 685 TWD | 18,272,337 | $5.66B | none | Rose 9.95% to 685 TWD - locked at its limit-up price - with no company-specific release found for 23 November - it closed at its **+10% limit price** with the AI-supply-chain complex, after Taiwan's Financial Supervisory Commission banned short selling below the previous day's closing price and raised the short-sale margin from 130% to 150% effective 23 November, and the National Stabilization Fund confirmed it had entered the market (its 10th activation, with about NT$500bn available) (TVBS World Taiwan, 23 Nov; UURL, 23 Nov) |
| `TWSE:1303` | Nan Ya Plastics Corporation | **+9.95%** | 226.5 TWD | 128,627,770 | $49.56B | none | Rose 9.95% to 226.5 TWD - locked at its limit-up price - with no company-specific release found for 23 November - it closed at its **+10% limit price** with the AI-supply-chain complex, after Taiwan's Financial Supervisory Commission banned short selling below the previous day's closing price and raised the short-sale margin from 130% to 150% effective 23 November, and the National Stabilization Fund confirmed it had entered the market (its 10th activation, with about NT$500bn available) (TVBS World Taiwan, 23 Nov; UURL, 23 Nov) |
| `TWSE:2466` | Cosmo Electronics Corporation | **+9.95%** | 425.5 TWD | 361,977 | $2.04B | none | Rose 9.95% to 425.5 TWD - locked at its limit-up price - with no company-specific release found for 23 November - it closed at its **+10% limit price** with the AI-supply-chain complex, after Taiwan's Financial Supervisory Commission banned short selling below the previous day's closing price and raised the short-sale margin from 130% to 150% effective 23 November, and the National Stabilization Fund confirmed it had entered the market (its 10th activation, with about NT$500bn available) (TVBS World Taiwan, 23 Nov; UURL, 23 Nov) |

45 further liquid name(s) cleared ±5% in this region and are in `tw.csv`; they moved with the same sourced complex as the table above.

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:MAU` | Montage Gold Corp. | **+12.46%** | 13.81 CAD | 1,589,041 | $3.49B | OTC | Rose 12.46% to 13.81 CAD - with no company-specific release found for 23 November - it moved with the precious-metals complex as gold recovered from a 14-month low (spot gold +2.2% to +4.3% on the day, to about US$3,607-3,683/oz) and silver gained about 5% (Reuters, 23 Nov; CNBC, 23 Nov; RTTNews, 23 Nov) |
| `TSX:HPS.A` | Hammond Power Solutions Inc. Class A | **+11.79%** | 191.1 CAD | 105,194 | $1.42B | OTC | Rose 11.79% to 191.1 CAD - with the AI-power and electrification complex that re-rated with Huang's return; Bloomberg named Hammond Power Solutions a top performer of the session at +12% (Bloomberg, 23 Nov; RTTNews, 23 Nov) |
| `TSX:SEA` | Seabridge Gold Inc | **+11.45%** | 27.64 CAD | 397,234 | $1.87B | NYSE | Rose 11.45% to 27.64 CAD - with no company-specific release found for 23 November - it moved with the precious-metals complex as gold recovered from a 14-month low (spot gold +2.2% to +4.3% on the day, to about US$3,607-3,683/oz) and silver gained about 5% (RTTNews, 23 Nov; Bloomberg, 23 Nov) |
| `TSX:GMIN` | G Mining Ventures Corp | **+10.93%** | 41.5 CAD | 803,113 | $7.73B | OTC | Rose 10.93% to 41.5 CAD - with no company-specific release found for 23 November - it moved with the precious-metals complex as gold recovered from a 14-month low (spot gold +2.2% to +4.3% on the day, to about US$3,607-3,683/oz) and silver gained about 5% (RTTNews, 23 Nov; Bloomberg, 23 Nov) |
| `TSX:HBM` | Hudbay Minerals Inc | **+10.87%** | 25.71 CAD | 3,624,976 | $7.19B | NYSE | Rose 10.87% to 25.71 CAD - with no company-specific release found for 23 November - it moved with the base-metals complex as copper added nearly 3% and gold recovered about 4% from a 14-month low (Reuters, 23 Nov; CNBC, 23 Nov) (RTTNews, 23 Nov) |
| `TSX:SKE` | Skeena Resources Limited | **+9.88%** | 37.04 CAD | 563,130 | $2.96B | NYSE | Rose 9.88% to 37.04 CAD - with no company-specific release found for 23 November - it moved with the precious-metals complex as gold recovered from a 14-month low (spot gold +2.2% to +4.3% on the day, to about US$3,607-3,683/oz) and silver gained about 5% (RTTNews, 23 Nov) |
| `TSX:SXGC` | Southern Cross Gold Consolidated Ltd. | **+9.76%** | 6.86 CAD | 540,507 | $1.18B | OTC | Rose 9.76% to 6.86 CAD - with no company-specific release found for 23 November - it moved with the precious-metals complex as gold recovered from a 14-month low (spot gold +2.2% to +4.3% on the day, to about US$3,607-3,683/oz) and silver gained about 5% (RTTNews, 23 Nov) |
| `TSX:CGG` | China Gold International Resources Corp. Ltd. | **+9.16%** | 26.33 CAD | 146,305 | $6.99B | OTC | Rose 9.16% to 26.33 CAD - with no company-specific release found for 23 November - it moved with the precious-metals complex as gold recovered from a 14-month low (spot gold +2.2% to +4.3% on the day, to about US$3,607-3,683/oz) and silver gained about 5% (RTTNews, 23 Nov) |
| `TSX:ERO` | Ero Copper Corp. | **+9.10%** | 33.56 CAD | 463,891 | $2.24B | NYSE | Rose 9.10% to 33.56 CAD - with no company-specific release found for 23 November - it moved with the base-metals complex as copper added nearly 3% and gold recovered about 4% from a 14-month low (Reuters, 23 Nov; CNBC, 23 Nov) (RTTNews, 23 Nov) |
| `TSX:SHOP` | Shopify, Inc. Class A | **+8.96%** | 192.96 CAD | 2,114,338 | $158.96B | NASDAQ | Rose 8.96% to 192.96 CAD - with no company-specific release found for 23 November - it moved with the AI-technology complex that re-rated after Huang's return, with the Canadian information-technology sector the day's best  Bloomberg had Shopify up more than 10% intraday (Bloomberg, 23 Nov) |
| `TSX:SGD` | Snowline Gold Corp. | **+8.72%** | 11.6 CAD | 343,876 | $1.40B | OTC | Rose 8.72% to 11.6 CAD - with no company-specific release found for 23 November - it moved with the precious-metals complex as gold recovered from a 14-month low (spot gold +2.2% to +4.3% on the day, to about US$3,607-3,683/oz) and silver gained about 5% (RTTNews, 23 Nov) |
| `TSX:EDR` | Endeavour Silver Corp. | **+8.62%** | 8.82 CAD | 1,434,784 | $1.68B | NYSE | Rose 8.62% to 8.82 CAD - with no company-specific release found for 23 November - it moved with the precious-metals complex as gold recovered from a 14-month low (spot gold +2.2% to +4.3% on the day, to about US$3,607-3,683/oz) and silver gained about 5% (RTTNews, 23 Nov) |
| `TSX:BB` | BlackBerry Limited | **+8.38%** | 12.03 CAD | 2,853,312 | $4.55B | NYSE | Rose 8.38% to 12.03 CAD - the top gainer in the Canadian information-technology sector at +10% intraday - with no company-specific release found for 23 November - it moved with the AI-technology complex that re-rated after Huang's return, with the Canadian information-technology sector the day's best  (RTTNews, 23 Nov) |
| `TSXV:SIG` | Sitka Gold Corp. | **+23.53%** | 0.84 CAD | 1,234,412 | $205.86M | OTC | Rose 23.53% to 0.84 CAD - the largest move on the TSX Venture board, after AngloGold Ashanti agreed to invest at least US$72.8m for a **15% stake** through AngloGold Canada - an offering valued between $83m and $102m for 76.6m-79.5m common shares, a roughly 40% premium; the stock was halted and resumed trading the same afternoon (Sitka Gold release, 23 Nov; The Northern Miner, 23 Nov; CIRO trade-resumption notice, 23 Nov) |

37 further liquid name(s) cleared ±5% in this region and are in `ca.csv`; they moved with the same sourced complex as the table above.

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:JEN` | Jenoptik AG | **+13.32%** | 36.06 EUR | 205,004 | $2.00B | OTC | Rose 13.32% to 36.06 EUR - the top MDAX gainer, with the AI-hardware complex - dpa-AFX named Siltronic, AIXTRON, SÜSS MicroTec and Jenoptik as direct or indirect beneficiaries of AI and its technical prerequisites, mostly in the semiconductor industry (dpa-AFX, 23 Nov; finanzen.ch, 23 Nov) |
| `XETR:AIXA` | AIXTRON SE | **+8.91%** | 32.04 EUR | 1,001,906 | $3.64B | ADR | Rose 8.91% to 32.04 EUR - with the AI/semiconductor-equipment complex, named by dpa-AFX among the AI beneficiaries (dpa-AFX, 23 Nov; finanzen.ch, 23 Nov) |
| `XETR:WAF` | Siltronic AG | **+7.16%** | 54.65 EUR | 137,321 | $1.85B | ADR | Rose 7.16% to 54.65 EUR - with the AI/semiconductor complex, named by dpa-AFX among the AI beneficiaries (dpa-AFX, 23 Nov; finanzen.net, 23 Nov) |
| `XETR:ENR` | Siemens Energy AG | **+6.88%** | 126.46 EUR | 3,032,676 | $109.19B | ADR | Rose 6.88% to 126.46 EUR - named by dpa-AFX, with Hochtief, among the day's AI beneficiaries whose gains ran from 5.6% to 7.7% (dpa-AFX, 23 Nov; Tradegate, 23 Nov) |
| `XETR:IFX` | Infineon Technologies AG | **+6.56%** | 48.42 EUR | 7,547,293 | $64.90B | ADR | Rose 6.56% to 48.42 EUR - with the AI/semiconductor complex; Infineon was the second-biggest DAX gainer of the session (dpa-AFX, 23 Nov; Tradegate, 23 Nov) |
| `XETR:HOT` | HOCHTIEF Aktiengesellschaft | **+5.38%** | 356.2 EUR | 53,836 | $27.92B | OTC | Rose 5.38% to 356.2 EUR - named by dpa-AFX, with Siemens Energy, among the AI beneficiaries (dpa-AFX, 23 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:FRVIA` | Forvia SE | **+10.52%** | 8.282 EUR | 1,549,346 | $1.62B | none | Rose 10.52% to 8.282 EUR - the best SBF 120 performer of the session, after a **Kepler Cheuvreux buy rating** (ideal-investisseur, 23 Nov; Investing.com, 23 Nov) |
| `EURONEXT:ETL` | Eutelsat Communications SA | **+8.85%** | 1.605 EUR | 2,076,570 | $1.91B | ADR | Rose 8.85% to 1.605 EUR - among the SBF 120 leaders - the satellite operator reversed the week's trend as Wall Street came out of its worst session since 2020 (ideal-investisseur, 23 Nov) |
| `EURONEXT:SOI` | Soitec SA | **+5.40%** | 101.5 EUR | 670,192 | $3.78B | none | Rose 5.40% to 101.5 EUR - with the semiconductor-substrate complex - the AI rebound, itself after steep price-target cuts at two major banks, Jefferies and HSBC (ideal-investisseur, 23 Nov; Il Sole 24 Ore Radiocor, 23 Nov) |
| `EURONEXT:ERA` | Eramet SA | **-5.25%** | 16.6 EUR | 164,470 | $1.21B | none | Fell 5.25% to 16.6 EUR - touching EUR16.52 intraday - a **ten-year low** and the worst SBF 120 performer of the session, while trading without the preemptive subscription right since 16 November following a capital increase (ideal-investisseur, 23 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:TPRO` | Technoprobe SpA | **+8.75%** | 20.02 EUR | 3,722,972 | $12.94B | ADR | Rose 8.75% to 20.02 EUR - with the Milan technology rebound as Jensen Huang returned to Nvidia leadership; Reuters had it +10% (Reuters via MarketScreener, 23 Nov; Il Sole 24 Ore Radiocor, 23 Nov) |
| `MIL:PRY` | Prysmian S.p.A. | **+6.52%** | 107.05 EUR | 1,110,682 | $33.01B | ADR | Rose 6.52% to 107.05 EUR - with no company-specific release found for 23 November - it moved with the European technology complex, which was led by chip-equipment makers after Nvidia reinstated Jensen Huang as CEO (the Stoxx technology sub-index +2.22%, the Nasdaq +6.7%) (Reuters via MarketScreener, 23 Nov; Il Sole 24 Ore Radiocor, 23 Nov) |
| `MIL:FCT` | Fincantieri S.p.A. | **+5.24%** | 11.345 EUR | 2,200,882 | $4.49B | OTC | Rose 5.24% to 11.345 EUR - leading the FTSE MIB in a well-bought European defence sector, after the major order secured from Carnival (Reuters via MarketScreener, 23 Nov; Il Sole 24 Ore Radiocor, 23 Nov) |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `BME:TRE` | Tecnicas Reunidas SA | **+6.04%** | 30.2 EUR | 281,453 | $2.44B | none | Rose 6.04% to 30.2 EUR - after its CNMV disclosure that it will execute **three hydrogen-ready combined-cycle gas power plants for RWE in Germany**; it also published the end of its buy-back programme, covering the transactions between 12 and 17 November (CNMV relevant information, 23 Nov) |

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:BESI` | BE Semiconductor Industries N.V. | **+9.25%** | 155.9 EUR | 738,184 | $12.64B | ADR | Rose 9.25% to 155.9 EUR - one of the three Dutch chip-equipment makers that led the recovery (Il Sole 24 Ore Radiocor, 23 Nov; Business Times, 23 Nov) |
| `EURONEXT:ASML` | ASML Holding NV | **+8.92%** | 1272.2 EUR | 954,133 | $489.67B | ADR | Rose 8.92% to 1272.2 EUR - the largest of the three Dutch semiconductor-equipment makers that led the European technology recovery (Il Sole 24 Ore Radiocor, 23 Nov; Business Times, 23 Nov) |
| `EURONEXT:ASM` | ASM International N.V. | **+8.29%** | 692.6 EUR | 238,546 | $34.16B | ADR | Rose 8.29% to 692.6 EUR - one of the three Dutch chip-equipment makers that led the recovery (Il Sole 24 Ore Radiocor, 23 Nov; Business Times, 23 Nov) |

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:MELE` | Melexis NV | **+5.14%** | 55.2 EUR | 60,960 | $2.33B | none | Rose 5.14% to 55.2 EUR - with the European semiconductor complex, the Stoxx technology sub-index adding 2.22% as Huang's return revived the AI trade (Il Sole 24 Ore Radiocor, 23 Nov; Business Times, 23 Nov) |

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | **+13.03%** | 110.2 EUR | 241,206 | $4.16B | OTC | Rose 13.03% to 110.2 EUR - with the AI-linked substrate complex; AT&S sits in the same AI-beneficiary group dpa-AFX named for the German session - Siltronic, AIXTRON, SÜSS MicroTec and Jenoptik (dpa-AFX, 23 Nov) |
| `VIE:AMS2` | ams-OSRAM AG | **+11.03%** | 15.1 EUR | 9,412 | $1.48B | ADR | Rose 11.03% to 15.1 EUR - with no company-specific release found for 23 November - it moved with the European technology complex, which was led by chip-equipment makers after Nvidia reinstated Jensen Huang as CEO (the Stoxx technology sub-index +2.22%, the Nasdaq +6.7%) (Il Sole 24 Ore Radiocor, 23 Nov) |

### eu-pt

No liquid name cleared ±5% with a sourced driver in this region.

### eu-ie

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:GL9` | Glanbia PLC | **-6.91%** | 17.92 EUR | 813,016 | $5.02B | ADR | Fell 6.91% to 17.92 EUR - the Irish Times reports EUR18.09, -6.03%, at the close, so the two readings of the close differ by 0.95% - after a **US rival restocked major US stores at a much more competitive price** for consumers; the stock sold off through the morning while the market rallied (Irish Times, 23 Nov) |
| `EURONEXT:KMR` | Kenmare Resources PLC | **+19.33%** | 3.58 EUR | 22,642 | $289.49M | OTC | Rose 19.33% to 3.58 EUR - with the mined-metals complex, Kenmare being a zinc producer: gold recovered about 4%, silver about 5% and copper nearly 3%, and the STOXX miners rose about 1.4%; no company-specific release for 23 November could be sourced (Reuters, 23 Nov; CNBC, 23 Nov) |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:NOKIA` | Nokia Oyj | **+8.91%** | 7.018 EUR | 19,619,183 | $40.02B | none | Rose 8.91% to 7.018 EUR - with no company-specific release found for 23 November - it moved with the European technology complex, which was led by chip-equipment makers after Nvidia reinstated Jensen Huang as CEO (the Stoxx technology sub-index +2.22%, the Nasdaq +6.7%) (Il Sole 24 Ore Radiocor, 23 Nov; Business Times, 23 Nov) |

### eu-dk

No liquid name cleared ±5% with a sourced driver in this region.

### eu-gr

No liquid name cleared ±5% with a sourced driver in this region.

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a +100% or a -50% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows. **Most of them are sub-$0.05 micro-caps whose percentage carries little information** - their prices, not their percentages, are the signal.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:HE8 | Helios Energy Ltd | **+100.00%** | 666,037 | below the $300M cap floor |
| ASX:GSE | Gulf Stream Energy Ltd | **-66.67%** | 267,857 | below the $300M cap floor |
| ASX:MML | McLaren Minerals Limited | **-63.64%** | 11,131,607 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:7932 | e-Ray Technology Co., Ltd. | **+17.28%** | 210,056 | below the $200M cap floor |
| TPEX:6990 | Plum-Monix Industry Co Ltd | **+16.16%** | 295,769 | below the $200M cap floor |
| TPEX:3585 | Advance Materials Corporation | **+14.71%** | 1,026,326 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| CSE:TONE | Triple One Metals Inc | **+100.00%** | 119,500 | below the $200M cap floor |
| TSXV:CRI | Churchill Resources Inc | **+100.00%** | 3,592,056 | below the $200M cap floor |
| TSXV:EGR | EGR Exploration Ltd | **+100.00%** | 417,000 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| XETR:SNG | SINGULUS TECHNOLOGIES AG | **+21.05%** | 187,101 | below the $300M cap floor |
| XETR:TPG0 | Platform Group SE & Co. KGaA | **+12.90%** | 670,799 | below the $300M cap floor |
| XETR:LPK | LPKF Laser & Electronics SE | **+10.12%** | 761,915 | below the $300M cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALNEV | Neovacs SA | **+83.44%** | 3,377,361 | below the $100M cap floor |
| EURONEXT:ALREE | REED | **+75.00%** | 11,541,460 | below the $100M cap floor |
| EURONEXT:CO | Casino, Guichard-Perrachon SA | **+18.59%** | 1,031,701 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:ENY | Energy SpA | **-29.96%** | 121,500 | below the $100M cap floor |
| MIL:CLE | Class Editori S.p.A. | **+8.72%** | 132,128 | below the $100M cap floor |
| MIL:MTV | Mondo TV S.p.A. | **-7.50%** | 2,510,342 | below the $100M cap floor |

### eu-es

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| BME:CITY | Club De Futbol Intercity SAD | **-5.31%** | 12,950,417 | below the $100M cap floor |

### eu-nl

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:AVTX | Avantium N.V. | **+6.96%** | 618,549 | below the $100M cap floor |

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:OXUR | Oxurion NV | **+20.00%** | 1,977,910 | below the $100M cap floor |
| EURONEXT:AGFB | Agfa-Gevaert NV | **-8.98%** | 312,701 | below the $100M cap floor |

### eu-at

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-pt

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-ie

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-fi

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-dk

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-gr

No name below the cap floor cleared the volume gate and the move threshold in this region.

## No catalyst

The names that moved with **no sourced driver**: no company release, no filing, no analyst action, and no NAMED sector or macro complex behind them that could be sourced - a name that rose only because the market rose is not a catalyst. Separate, so they do not dilute the mover table.

### au

No moved name without a sourced driver in this region.

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TWSE:3532` | Formosa Sumco Technology Corporation | **-9.92%** | 168 TWD | 5,526,475 | $2.19B | none | Fell 9.92% to 168 TWD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TWSE:8996` | Kaori Heat Treatment Co., Ltd. | **-7.04%** | 858 TWD | 5,680,370 | $2.62B | none | Fell 7.04% to 858 TWD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TPEX:7856` | Hermes Testing Solutions Inc. | **-6.51%** | 1580 TWD | 1,247,488 | $1.69B | none | Fell 6.51% to 1580 TWD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TWSE:2891` | CTBC Financial Holding Company Ltd. | **-6.18%** | 63.8 TWD | 109,371,042 | $40.58B | none | Fell 6.18% to 63.8 TWD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TWSE:9910` | Feng Tay Enterprise Co., Ltd. | **-6.00%** | 54.8 TWD | 2,403,705 | $1.75B | none | Fell 6.00% to 54.8 TWD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TWSE:2258` | Foxtron Vehicle Technologies Co., Ltd. | **-5.96%** | 25.25 TWD | 851,586 | $1.43B | none | Fell 5.96% to 25.25 TWD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TWSE:3443` | Global Unichip Corp. | **-5.19%** | 5120 TWD | 8,632,562 | $21.95B | none | Fell 5.19% to 5120 TWD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TPEX:3644` | Linco Technology Co., Ltd. | **+17.06%** | 295 TWD | 356,182 | $636.72M | none | Rose 17.06% to 295 TWD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TSX:ARE` | Aecon Group Inc. | **+8.15%** | 53.37 CAD | 403,225 | $2.36B | OTC | Rose 8.15% to 53.37 CAD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TSX:FTT` | Finning International Inc. | **+6.53%** | 82.73 CAD | 582,455 | $7.03B | OTC | Rose 6.53% to 82.73 CAD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TSX:ATZ` | Aritzia, Inc. | **+6.48%** | 144.74 CAD | 795,371 | $10.74B | OTC | Rose 6.48% to 144.74 CAD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TSX:GRGD` | Groupe Dynamite Inc. | **+6.36%** | 50.15 CAD | 149,274 | $3.59B | OTC | Rose 6.36% to 50.15 CAD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TSX:ATS` | ATS Corporation | **+5.54%** | 24.94 CAD | 468,299 | $1.58B | NYSE | Rose 5.54% to 24.94 CAD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `TSX:MG` | Magna International Inc. | **+5.06%** | 88.26 CAD | 1,747,508 | $15.15B | NYSE | Rose 5.06% to 88.26 CAD with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `XETR:AG1` | AUTO1 Group SE | **+9.23%** | 14.91 EUR | 857,556 | $3.33B | ADR | Rose 9.23% to 14.91 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `XETR:SZG` | Salzgitter AG | **+7.71%** | 46.64 EUR | 203,584 | $2.86B | ADR | Rose 7.71% to 46.64 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `XETR:NEM` | Nemetschek SE | **-5.73%** | 51 EUR | 602,071 | $6.86B | ADR | Fell 5.73% to 51 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `XETR:KGX` | KION GROUP AG | **+5.00%** | 30.66 EUR | 362,686 | $4.20B | ADR | Rose 5.00% to 30.66 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:FR` | Valeo SE | **+5.72%** | 10.995 EUR | 1,212,339 | $2.80B | ADR | Rose 5.72% to 10.995 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `EURONEXT:ALVIO` | Valerio Therapeutics | **-13.66%** | 0.3065 EUR | 968,408 | $228.62M | none | Fell 13.66% to 0.3065 EUR the second consecutive double-digit fall - Yahoo's ALVIO.PA read EUR0.3240, -8.73%, at 10:30 GMT+1 and the close came in at EUR0.3065, -13.66%; the line is down 22.7% over November and 49.6% over three months, and its 52-week high is EUR0.98 against a EUR0.10 low (Yahoo Finance, 23 Nov; DataCedar, 23 Nov). No company release or analyst action for 23 November could be sourced |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `MIL:MOL` | Moltiply Group S.p.A. | **+5.39%** | 35.2 EUR | 17,120 | $1.37B | none | Rose 5.39% to 35.2 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |
| `MIL:ADV` | Adventure SpA | **+17.24%** | 6.12 EUR | 10,875 | $336.99M | none | Rose 17.24% to 6.12 EUR an illiquid Euronext Growth Milan line - the move came on 10,875 shares, and Borsa Italiana's own page shows the line as `Inaccessible` with a last contract of 17 November, after an 8-for-1 share split effective 19 October and a capital reconstruction on 13 November; an `Internal Dealing` notice was filed on 23 November (Borsa Italiana, 23 Nov; eMarketstorage, 23 Nov). No driver could be sourced |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `BME:BKY` | Berkeley Energia Limited | **+12.15%** | 0.517 EUR | 9,479,301 | $218.72M | none | Rose 12.15% to 0.517 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |

### eu-nl

No moved name without a sourced driver in this region.

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:UMI` | Umicore SA | **+6.57%** | 16.88 EUR | 756,820 | $4.18B | ADR | Rose 6.57% to 16.88 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |

### eu-at

No moved name without a sourced driver in this region.

### eu-pt

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:CTT` | CTT - Correios de Portugal SA | **+3.21%** | 4.764 EUR | 362,620 | $677.96M | none | Rose 3.21% to 4.764 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |

### eu-ie

No moved name without a sourced driver in this region.

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `OMXHEX:WRT1V` | Wartsila Oyj Abp | **+5.89%** | 24.97 EUR | 1,434,978 | $15.27B | none | Rose 5.89% to 24.97 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `OMXCOP:BETCO_DKK` | Better Collective A/S | **+7.23%** | 40.05 DKK | 337,431 | $322.05M | OTC | Rose 7.23% to 40.05 DKK with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |

### eu-gr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `ATHEX:PROF` | PROFILE Systems & Software S.A. | **+5.29%** | 9.75 EUR | 44,699 | $249.97M | none | Rose 5.29% to 9.75 EUR with no driver found - no company release or analyst action for 23 November could be sourced, and no named sector complex explains the move |

## Method, source health & caveats

### Method

- **Universe** - the TradingView per-country scanner, filtered on the ISSUER's own `country` (the endpoint takes it as `filter`; the `filters` key is silently ignored), one call per region and one for the America board. All 18 pulls were complete (`totalCount` == rows returned) on 23 November - 16 country boards, the America board and the 17 index tickers. 14,366 rows came back across the 16 regions and **2,841 names were published** in the 15 regions that traded; Japan was closed.
- **Floors (USD, applied AFTER conversion)** - au $300M + volume ≥ 100,000; jp $300M (not applied - the region did not trade); tw $200M; ca $200M; eu-de $300M + volume ≥ 50,000; eu-fr/eu-it/eu-es/eu-nl/eu-be/eu-at $100M; eu-ie $200M; eu-fi/eu-dk $100M; eu-pt/eu-gr $50M.
- **FX** - open.er-api.com, rate date **Mon, 23 Nov 2026 00:02:32 +0000**. The table is **local currency per 1 USD**, so the conversion is a **division**: `usd_cap = market_cap_basic / FX[listing_currency]`. The identity asserted on every published row is `usd_cap * FX_per_USD == market_cap_local`.
- **Venue collapse** - the issuer's PRIMARY listing venue wins (au ASX; jp TSE/NAG/FSE/SAPSE; tw TWSE/TPEX; ca TSX/TSXV/CSE/NEO; eu-de XETR/FWB/LSX/LS/GETTEX/DUS/MUN/SWB/TRADEGATE/HAM/HAN), and a line whose implied prior close (`close / (1 + change/100)`) does not reconcile with the prior session's published close for the same symbol within 5% is a `stale_venue_print` and is dropped. Off-official lines are counted in the Coverage table.
- **Cap carrier** - the cap is resolved to the issuer's PRIMARY (common) line, converted ONCE with the primary's currency, and every line of that issuer carries that one USD figure; `cap_source_symbol` names the line it came from. A group with no common line is dropped as `issuer_unresolved` rather than published with a borrowed cap.
- **Cross-venue cap check** - the America scanner is a second reading of the same company-level cap. **73 of the issuers with a US line disagree by more than 10%** after conversion (94 on the previous session); the primary venue's cap is the one published in every case, and the disagreements are a second-reading disagreement, not a defect in the published number.
- **Venue-official price rule** - where an exchange's own close is published it is the price and the row carries the conflict in `price_conflict`. **The ATHEX General is the one venue-official level in this artifact** - Euronext Athens' own index page gives the 23 November close as 2,562.36, +0.38%, high 2,570.53 and low 2,524.13 - because the ATHEX has no Yahoo symbol and no TradingView venue index. At row level the scanner close stood for every published row and every `price_conflict` cell is empty; the DAX is the Xetra official close of 17:50 (dpa-AFX) and the other European levels are the vendors' closing prints, each cross-checked against a press reading.
- **CSV columns** - **18**, unchanged from the previous session (`date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`). Prices are written to 4 decimals with trailing zeros stripped; `volume` and `market_cap` are integers.
- **Files written** - `international-eod/2026-11-23/`: 15 per-region CSVs (`au.csv` … `eu-gr.csv`, **no `jp.csv`**), `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView au scanner | scanner.tradingview.com/australia/scan, filter country = Australia, types = stock | ok | 2117 of 2117 rows, complete |
| TradingView tw scanner | scanner.tradingview.com/taiwan/scan, filter country = Taiwan, types = stock | ok | 2712 of 2712 rows, complete |
| TradingView ca scanner | scanner.tradingview.com/canada/scan, filter country = Canada, types = stock | ok | 8061 of 8061 rows, complete |
| TradingView eu-de scanner | scanner.tradingview.com/germany/scan, filter country = Germany, types = stock | ok | 4565 of 4565 rows, complete |
| TradingView eu-fr scanner | scanner.tradingview.com/france/scan, filter country = France, types = stock | ok | 694 of 694 rows, complete |
| TradingView eu-it scanner | scanner.tradingview.com/italy/scan, filter country = Italy, types = stock | ok | 383 of 383 rows, complete |
| TradingView eu-es scanner | scanner.tradingview.com/spain/scan, filter country = Spain, types = stock | ok | 233 of 233 rows, complete |
| TradingView eu-nl scanner | scanner.tradingview.com/netherlands/scan, filter country = Netherlands, types = stock | ok | 109 of 109 rows, complete |
| TradingView eu-be scanner | scanner.tradingview.com/belgium/scan, filter country = Belgium, types = stock | ok | 105 of 105 rows, complete |
| TradingView eu-at scanner | scanner.tradingview.com/austria/scan, filter country = Austria, types = stock | ok | 65 of 65 rows, complete |
| TradingView eu-pt scanner | scanner.tradingview.com/portugal/scan, filter country = Portugal, types = stock | ok | 31 of 31 rows, complete |
| TradingView eu-ie scanner | scanner.tradingview.com/ireland/scan, filter country = Ireland, types = stock | ok | 19 of 19 rows, complete |
| TradingView eu-fi scanner | scanner.tradingview.com/finland/scan, filter country = Finland, types = stock | ok | 190 of 190 rows, complete |
| TradingView eu-dk scanner | scanner.tradingview.com/denmark/scan, filter country = Denmark, types = stock | ok | 173 of 173 rows, complete |
| TradingView eu-gr scanner | scanner.tradingview.com/greece/scan, filter country = Greece, types = stock | ok | 128 of 128 rows, complete |
| TradingView america scanner | scanner.tradingview.com/america/scan, types = stock + dr | ok | 13581 of 13581 rows, complete - the source for `us_listing` and for the cross-venue cap check |
| TradingView global scanner | scanner.tradingview.com/global/scan, 17 index tickers | ok | 17 index closes (16 regions + the STOXX 600) |
| FX | open.er-api.com/v6/latest/USD | ok | rate date Mon, 23 Nov 2026 00:02:32 +0000 |
| Market session probe | market_session_probe.py --region <r> --date 2026-11-23, all 16 regions | ok | 15 regions `traded=yes`; **jp `traded=unknown`** - `after_last_session (last bar 2026-11-20)` - resolved to a CONFIRMED closure by the three checks below |
| Yahoo daily bars (Japan) | query1.finance.yahoo.com/v8/finance/chart/{^N225, 9984.T, 7203.T, 6758.T, 8306.T}?range=12d&interval=1d | ok | every one of the five series ends on 2026-11-20 - no 23 November bar exists for the index or for any TSE constituent |
| JPX market holidays | jpx.co.jp/english/corporate/about-jpx/calendar/ and the JPX derivatives notice of 20 Nov 2026 | ok | `Nov. 23 (Mon.) Labor Thanksgiving Day` - market holiday, with BCP testing from 21 to 23 November |
| Euronext Athens index page | athens.euronext.com/en/market-data/instruments/indices/GD | ok | the ATHEX Composite's own 23 Nov row: close 2,562.36, high 2,570.53, low 2,524.13, +0.38%, volume 53,506,686, turnover EUR413.18m - the venue-official level |
| Index levels - press and exchange pages | Reuters (global, TSX, STOXX), CNA/Focus Taiwan, TVBS, UURL, ABC live blog, dpa-AFX via vwd/tradegate, Tradegate, ideal-investisseur, Business Times, Il Sole 24 Ore Radiocor, Irish Times, samso, Investing.com, MarketScreener/MT, euro2day, 23 Nov 2026 | ok | every one of the 16 regional index levels published above was cross-checked against a second reading; the ATHEX is the only level carried without a vendor index and it comes from the venue's own page |
| Company releases and wires | ASX notices 1312.26.11 and 1334.26.11, CNMV relevant information, Sitka Gold's release, the Northern Miner, CIRO, market_session_probe.py | ok | the corporate-action and closure findings above |

### Caveats

- **Japan did not trade on this date, and the artifact does not pretend otherwise.** The Tokyo Stock Exchange was closed for **Labor Thanksgiving Day**, and the JPX also ran group-wide **BCP testing from 21 to 23 November**, which is why its derivatives notice marks the day `Not Open`. Three independent readings agree: Yahoo's daily bars for `^N225` and for four TSE constituents all stop at 20 November; the JPX calendar names the day; and the TradingView Japan pull repeated the 20 November session **verbatim**, including the -14.48% change on `TSE:9984` that the 20 November artifact published. Building that stale pull would have written 1,347 Japanese rows dated 23 November, 1,333 of them carrying the 20 November move, so the region is removed and the removal is recorded in `_manifest.json` under `closed_regions`. The next Tokyo session is Tuesday 24 November.
- **Taiwan's +10.00% prints are limit prices, not calculated moves, and the limit-up cluster was a policy event as much as a market one.** TWSE and TPEX cap a daily move at ±10%, so a +10.00% close is a limit print and the market was shut at that price. The Financial Supervisory Commission's **third wave** of stabilisation measures took effect on 23 November: short selling below the previous day's close was banned and the short-sale margin requirement was raised from 130% to 150%; the National Stabilization Fund confirmed it had entered the market - its 10th activation - and Premier Cho Jung-tai convened an emergency meeting with the technology and finance chiefs to discuss enlarging the fund beyond its NT$500bn. **68 listed and OTC stocks closed limit-up** (45 listed names gained more than 9%, 43 touched limit-up) after a 17.5% weekly fall, the worst week since January 1991 (CNA via Focus Taiwan, 23 Nov; TVBS, 23 Nov; UURL, 23 Nov; Taipei Times, 23 Nov; Bloomberg, 23 Nov).
- **Two rows are contract-adjustment artefacts and are kept out of every published table.** `ASX:ZIP` (Zip Co) printed **+363.50%** because a **1-for-5 share consolidation** took effect on 23 November (ASX Notice 1312.26.11 of 16 November; the ETO adjustment notice of 20 November) and the source measured the change against the **unadjusted** prior close - the implied prior of A$1.685 equals the 20 November close exactly, and the row opened at A$8.25 against that A$1.685. On the adjusted basis (A$1.685 × 5 = A$8.425) the real move is about **-7.3%**, which is what the ASX's own sharpest-decliners table shows. `EURONEXT:ALAGR` (AgroGeneration) printed **+11,119.51%** against a EUR0.041 prior close on a **210-share** print - the implied prior of EUR0.041 is the 20 November close exactly, so the change field is on the old price basis and the row's own market cap moved with it (EUR9.8m to EUR996m). Both rows stay in their CSVs with the source's own field, per the archive's convention, and are disclosed here.
- **Three Taiwanese OTC rows printed OUTSIDE Taiwan's ±10% daily limit band and are excluded from every published table.** `TPEX:3117` (Tecstar Technology) closed NT$17.10 against a NT$12.90 prior close (**+32.56%**) after opening at the prior close; `TPEX:7415` (BE Epitaxy Semiconductor) closed NT$227.50 against NT$187.00 (**+21.66%**), opening at the prior close; `TPEX:7959` (Full Chain Materials) closed NT$60.10 against NT$51.00 (**+17.84%**). Each reconciles arithmetically with the prior session's published close, so the venue-collapse test passes them, and no company release for 23 November could be sourced for any of them. A move beyond the venue's limit band cannot be read as an ordinary session move.
- **The Milan index is the one European board whose close is distorted by a technical effect.** The FTSE MIB's **+0.65%** is capped by the ex-dividend adjustment on nine major companies, worth about **-1.41%**; the underlying session was much stronger - the Stoxx technology sub-index was up 2.22% and STM closed 8.99% higher at EUR40.02. Reading the Milan close as a 0.65% session understates the Italian move (Il Sole 24 Ore Radiocor, 23 Nov; Reuters via MarketScreener, 23 Nov).
- **Glanbia's close carries a small two-source disagreement.** The scanner prints EUR17.92, -6.91%, while the Irish Times reports EUR18.09, -6.03%, at the close - a 0.95% difference on the same session. The scanner figure is the published one, and the row carries no `price_conflict` cell because no **venue-official** Euronext Dublin print was obtained; the disagreement is disclosed here and in the row's catalyst.
- **STMicroelectronics - the day's biggest single European AI name, up 8.96% to EUR40.01 - is NOT in this artifact, and the reason is the universe rule.** The scanner files its country as **Switzerland**, and the universe is the ISSUER's own country, so its Milan and Paris lines fall outside all sixteen boards; the same rule excludes any other issuer the vendor files under a country this skill does not cover. The session's Milan leader was therefore Technoprobe, not STM (TradingView global scanner, 23 Nov; Il Sole 24 Ore Radiocor, 23 Nov).
- **The Australian session was the laggard and its median name fell while the index barely moved.** The ASX 200 fell 0.26% to 8,570.60, an eighth straight decline, and it opened 0.6% lower before Wall Street's recovery was priced - the median published Australian name was **-0.42%** against the index's -0.26%, so the typical Australian name fell further than the index did. The day's one large single-name move was **ALS -12.23%**, and it was a results story, not a sector story.
- **A handful of published names are illiquid enough that the percentage is not the signal.** `MIL:ADV` (Adventure SpA) rose 17.24% on **10,875 shares** at Euronext Growth Milan; Borsa Italiana's own page shows that line as `Inaccessible` with a last contract of 17 November, and the company has been through an 8-for-1 share split and a capital reconstruction since 13 November. `EURONEXT:OXUR` printed +20.00% on a EUR0.0012 close. No driver could be sourced for either, so both sit in `## No catalyst` rather than in the mover table.
- **60 rows are carry-overs** - instruments that did not trade on this session, whose close is the prior session's print. They are kept in the CSVs as the source returned them, listed in `_carryover.json` with the date of each instrument's last actual trade (walked back through the prior files, never forward), and excluded from every table above. Canada (22) and Spain (17) hold most of them; the rest are spread across au (3), eu-fr (4), eu-it (4), eu-be (2), eu-at (4), tw (1), eu-pt (1), eu-dk (1) and eu-gr (1).
- **`us_listing` changed on 22 rows against the previous session.** 10 rows gained a US listing and 9 rows lost one. The matcher is unchanged from the previous session (the punctuation-clean issuer key with the trailing period stripped), so a change here is a change in the America scanner's own file, not a change in the rule.
- **73 cross-venue cap disagreements above 10%** were recorded, against 94 on the previous session. The published cap is always the primary venue's; the gap is a second-reading disagreement, not a defect in the published number.
- **Sector rotation** (over the written rows, mean and median `change_pct` per sector) - the rotation was the AI trade itself: the strongest sectors on the session were the semiconductor and semiconductor-equipment complexes in Taiwan and Germany and the technology sector in the Netherlands, while the weakest were the materials and specialty-chemical complexes in Canada and France (Eramet -5.25%) and the single-stock casualty of the session, ALS's Life Sciences division. The rotation is computed from the same rows as the breadth table; no cap-weighted sector aggregate is published, because this file's caps are company-level and deduplicate on `cap_source_symbol`.
