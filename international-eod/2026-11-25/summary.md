# Cron #05 eod-international-daily — Wednesday, 25 November 2026

## TL;DR

- **The AI trade unwound on all 16 boards at once.** US October core PCE came in at **3.3% y/y, a tenth above consensus**, alongside a firm jobs print, and the Philadelphia Semiconductor Index fell **7.9%** overnight; the result was a single, synchronised risk-off session: the **TAIEX -4.80% at 38,195.43** (its sixth-largest point loss, and the second-largest intraday point loss on record at 36,681.90), the **Nikkei -2.78% at 57,011.62**, the **DAX -1.26% at 24,702.13**, the **FTSE MIB -1.81%**, the **ATX -3.10%** and the **ATHEX -2.77% at 2,454.94** (its steepest fall in 8.5 years), while the **ASX 200 slipped only 0.39% to 8,692.40** on hot Australian CPI and the **S&P/TSX actually closed +0.64% at 34,179.99** after the metals bounced off their lows into the bell. **4,243 names were published across all 16 boards**; every board traded and none was closed.
- **The one consequential move was the semiconductor unwind, and a US trader can reach both sides of it.** Japanese and Taiwanese hardware names led the world lower - **SoftBank -14.83%** (ADR), **Fujikura -14.70%** (ADR), **Taiyo Yuden -14.55%** (ADR), **IBIDEN -16.01%** (OTC), **Kokusai Electric -17.28%** - against **MediaTek -10.00%** (limit-down), **Winbond -10.00%**, **Transcend -10.00%**, **Macronix -10.00%** and **United Microelectronics -9.99%** in Taiwan, while Europe's equipment names fell again: **ASM International -7.81%** (ADR), **Infineon -6.49%** (ADR), **ASML -5.79%** (ADR) and **BE Semiconductor -5.56%** (ADR), with **ROCKWOOL -15.64%** (ADR) the worst European mover of the day on a guidance cut. The two stand-out non-tech names are **Rémy Cointreau +13.13%** (ADR, results and raised targets) and **Bureau Veritas +6.60%** (ADR, a reported Advent takeover approach).
- **The caveat that changes how to read it: `market_cap` is in USD while `open`/`high`/`low`/`close` are in the listing currency** (the `currency` column says which), and Taiwan's **-10.00% prints are limit prices, not calculated moves** - 392 Taiwanese stocks touched limit-down, so the TAIEX's -4.80% is a floor, not a valuation. Two further facts change the numbers themselves: **the TSX's +0.64% close is an intraday reversal**, not a session that was green (Reuters had it down 1.67% at 10:24 a.m. ET as gold hit a 14-month low), and **two rows, `TPEX:7861` -16.21% and `TPEX:7924` -11.25%, print outside Taiwan's +/-10% band** - the limit-band artefact the archive flagged on the first of them at +32.78% yesterday, kept out of the published tables.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| au | 1 | 1545 | 1545 | 294 | $300M + vol >= 100,000 | 4 | 1228 | 18 | 1 | 0 | 2 | 0 |
| jp | 3 | 3890 | 3868 | 1350 | $300M | 4 | 2513 | 0 | 1 | 0 | 0 | 0 |
| tw | 2 | 2347 | 2347 | 824 | $200M | 59 | 1464 | 0 | 0 | 0 | 2 | 0 |
| ca | 3 | 4299 | 2717 | 600 | $200M | 61 | 1930 | 0 | 126 | 0 | 19 | 0 |
| eu-de | 1 | 4296 | 710 | 123 | $300M + vol >= 50,000 | 4 | 402 | 181 | 0 | 0 | 0 | 0 |
| eu-fr | 1 | 543 | 543 | 259 | $100M | 1 | 283 | 0 | 0 | 0 | 6 | 0 |
| eu-it | 1 | 377 | 377 | 178 | $100M | 2 | 197 | 0 | 0 | 0 | 6 | 0 |
| eu-es | 1 | 230 | 230 | 134 | $100M | 24 | 72 | 0 | 0 | 0 | 23 | 0 |
| eu-nl | 1 | 78 | 78 | 56 | $100M | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| eu-be | 1 | 101 | 101 | 75 | $100M | 1 | 25 | 0 | 0 | 0 | 4 | 0 |
| eu-at | 1 | 66 | 66 | 50 | $100M | 2 | 14 | 0 | 0 | 0 | 4 | 0 |
| eu-pt | 1 | 30 | 30 | 26 | $50M | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| eu-ie | 1 | 19 | 19 | 16 | $200M | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| eu-fi | 1 | 189 | 189 | 101 | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| eu-dk | 1 | 133 | 133 | 75 | $100M | 1 | 57 | 0 | 0 | 0 | 0 | 0 |
| eu-gr | 1 | 127 | 127 | 82 | $50M | 0 | 45 | 0 | 0 | 0 | 0 | 0 |
| **total** | | 18270 | | **4243** | | 167 | 8343 | 199 | 128 | 0 | 66 | 0 |

The exclusion counts are the per-reason counts in `_excluded.json`, not estimates, and the reconciliation identity `unique_instruments == written + sum(excluded)` holds for every region. Written rows are 4243 against 4,202 on 24 November (+1.0%), and the boards that traded on both days are within a few tenths of a percent of the prior session's counts, which is the cheapest available proof that the FX conversion direction, the per-region floors and the cap-carrier rule all still hold.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 8,692.40 | -34.00 / -0.39% | 2026-11-25 | TradingView SP:XJO; samso Market Update (4:30pm AEDT), MarketIndex Evening Wrap and PerthNow all report 8,692.40, down 34.0 points or 0.39%, on the ABS's hotter-than-expected October inflation (4.9% y/y) and a 2.6% fall in the All Ordinaries Gold index |
| jp | Nikkei 225 | 57,011.62 | -1,633.01 / -2.78% | 2026-11-25 | TradingView TVC:NI225; Il Sole 24 Ore Radiocor, bbntimes and Trading Economics report the close at 57,011.62, down 1,633.01 points or 2.78%, after an intraday low of 56,936.38 - the TOPIX fell only 0.5% |
| jp | TOPIX | 3,746.20 | -18.68 / -0.50% | 2026-11-25 | TradingView TSE:TOPIX |
| tw | TAIEX | 38,195.43 | -1,926.92 / -4.80% | 2026-11-25 | TradingView TWSE:IX0001; CNA (Focus Taiwan), Taiwan News and the Taipei Times report the close at 38,195.43, down 1,926.92 points or 4.80% - the sixth-largest single-session point loss - after an intraday swing of 3,440.45 points to 36,681.90, the second-largest intraday point loss on record, with 392 stocks touching limit-down (note: Investing.com's close table prints the index down 4.94% on its own calculation) |
| ca | S&P/TSX Composite | 34,179.99 | +217.69 / +0.64% | 2026-11-25 | TradingView TSX:TSX, independently confirmed by the Yahoo chart API for ^GSPTSE (34,179.99, +217.688, +0.641%); Reuters had the index down 1.67% at 33,393.08 at 10:24 a.m. ET as gold hit a 14-month low, and it closed positive after the metals bounced off their lows into the bell |
| eu-de | DAX | 24,702.13 | -315.68 / -1.26% | 2026-11-25 | TradingView XETR:DAX; mlq.ai reports the close at 24,702.13, down 1.26%, as chipmakers slid with the AI rout |
| eu-fr | CAC 40 | 7,980.57 | -59.92 / -0.75% | 2026-11-25 | TradingView EURONEXT:PX1; mlq.ai reports the close at 7,980.57, down 0.75% |
| eu-it | FTSE MIB | 47,249.15 | -872.04 / -1.81% | 2026-11-25 | TradingView FTSE:FTSEMIB |
| eu-es | IBEX 35 | 18,635.80 | -380.00 / -2.00% | 2026-11-25 | TradingView BME:IBC |
| eu-nl | AEX | 1,063.44 | -13.97 / -1.30% | 2026-11-25 | TradingView EURONEXT:AEX |
| eu-be | BEL 20 | 5,837.71 | -46.41 / -0.79% | 2026-11-25 | TradingView EURONEXT:BEL20 |
| eu-at | ATX | 6,028.92 | -192.83 / -3.10% | 2026-11-25 | TradingView VIE:ATX - the worst of the 16 regional benchmarks on the day |
| eu-pt | PSI 20 | 9,254.08 | -79.46 / -0.85% | 2026-11-25 | TradingView EURONEXT:PSI20 |
| eu-ie | ISEQ | 14,120.63 | -300.52 / -2.08% | 2026-11-25 | TradingView EURONEXT:ISEQ |
| eu-fi | OMX Helsinki 25 | 5,866.56 | -88.26 / -1.48% | 2026-11-25 | TradingView OMXHEX:OMXH25 |
| eu-dk | OMX Copenhagen 20 | 1,613.32 | -13.08 / -0.80% | 2026-11-25 | TradingView OMXCOP:OMXC20 |
| eu-gr | ATHEX General | 2,454.94 | -69.94 / -2.77% | 2026-11-25 | **Euronext Athens' own print, via euro2day (25 Nov, 17:48) and xrimatistirio's close table**: close 2,454.94, down 69.94 points or 2.77% - the steepest fall in 8.5 years - on a range of 2,527.05 (+0.09%) to 2,444.63 (-3.14%), with 16 stocks rising against 104 falling, turnover EUR440.5m, and not one FTSE 25 stock in the green (the ATHEX has no Yahoo symbol and no TradingView venue index) |
| *context* | STOXX Europe 600 | 626.03 | -6.71 / -1.06% | 2026-11-25 | TradingView STOXX:SXXP; mlq.ai reports the 17:30 CET close at 626.03, down 1.06% against Tuesday's 632.74 |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 294 | -0.66% | 100 / 179 / 15 | -23.53% | +5.83% |
| jp | 1350 | +1.01% | 848 / 484 / 18 | -18.55% | +19.61% |
| tw | 824 | -5.60% | 30 / 784 / 10 | -21.18% | +9.89% |
| ca | 600 | +0.20% | 315 / 252 / 33 | -12.14% | +21.02% |
| eu-de | 123 | -0.40% | 51 / 72 / 0 | -7.48% | +5.30% |
| eu-fr | 259 | -0.13% | 93 / 134 / 32 | -6.92% | +13.13% |
| eu-it | 178 | -0.55% | 58 / 110 / 10 | -6.67% | +8.35% |
| eu-es | 134 | -0.03% | 35 / 67 / 32 | -5.88% | +3.81% |
| eu-nl | 56 | -0.53% | 19 / 34 / 3 | -16.54% | +3.21% |
| eu-be | 75 | +0.00% | 33 / 35 / 7 | -6.85% | +8.75% |
| eu-at | 50 | -1.31% | 8 / 37 / 5 | -7.66% | +7.98% |
| eu-pt | 26 | +0.20% | 14 / 9 / 3 | -3.60% | +7.46% |
| eu-ie | 16 | -0.77% | 3 / 9 / 4 | -4.38% | +1.12% |
| eu-fi | 101 | -0.87% | 27 / 71 / 3 | -7.78% | +6.95% |
| eu-dk | 75 | -1.12% | 16 / 54 / 5 | -16.05% | +3.24% |
| eu-gr | 82 | -1.29% | 8 / 65 / 9 | -7.13% | +5.71% |

The index level and the typical name disagree in both directions today, which is why both are published. **Japan's Nikkei fell 2.78% while 848 of its 1,350 published names ROSE and the median name was +1.01%** - the damage was concentrated in the AI-hardware complex, and the TOPIX fell only 0.50%. **Taiwan was a genuine broad rout** - 784 of 824 names down, median -5.60%, most of them locked at their limit-down. **Canada closed green (+0.64%) on a median of +0.20%,** which is the metals bounce, not a broad rally.

## Top movers

Liquid names (volume >= 100,000, market cap at or above the region's floor) whose move cleared +/-5%, with the driver that was actually sourced, largest absolute move first within the region. A row whose print falls outside its venue's daily price band is not a move and is kept out of every published table (two Taiwanese rows, disclosed in the caveats). A row with no sourced driver is not here - it is under `## No catalyst`. Each region also publishes its single biggest liquid mover even when it did not clear +/-5%, so no region is silent; a region with no name at all says so instead of publishing an unsourced row. Taiwan and Japan each had far more qualifying names than a table can carry: the tables publish the largest movers with a sourced driver, and the remainder stays in the CSVs.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:MI6` | Minerals 260 Limited | **-8.63%** | 0.635 AUD | 5,671,936 | $1.17B | OTC | Fell 8.63% to A$0.635 - no company driver beyond the market: its only release was the appointment of Paul Hegarty as chief financial officer, and it fell with the gold and copper complex (MarketIndex Evening Wrap, 25 Nov; samso Market Update, 25 Nov) |
| `ASX:LTR` | Liontown Limited | **-8.62%** | 0.53 AUD | 32,506,073 | $1.22B | OTC | Fell 8.62% to A$0.53 - no ASX announcement since the previous afternoon; it fell with the lithium complex after Develop Global said it would pause its Pioneer Dome mine (MarketIndex Evening Wrap, 25 Nov; samso Market Update, 25 Nov) |
| `ASX:TEA` | Tasmea Limited | **-7.62%** | 7.76 AUD | 1,426,907 | $1.55B | OTC | Fell 7.62% to A$7.76 - no company-specific release was found for 25 November; it fell with the Australian mining complex (MarketIndex Evening Wrap, 25 Nov) |
| `ASX:MP1` | Megaport Ltd. | **-7.18%** | 13.84 AUD | 2,157,388 | $2.32B | OTC | Fell 7.18% to A$13.84 - no company-specific release was found for 25 November; it fell with the Australian technology complex as the AI trade unwound (MarketIndex Evening Wrap, 25 Nov) |
| `ASX:OBM` | Ora Banda Mining Ltd. | **-6.94%** | 1.14 AUD | 7,330,140 | $1.56B | OTC | Fell 6.94% to A$1.14 - gold: the All Ordinaries Gold index lost 2.6% as COMEX gold fell 1.1% to US$3,522/oz in Asian trade after dropping 2.5% overnight (MarketIndex Evening Wrap, 25 Nov) |
| `ASX:MIN` | Mineral Resources Limited | **-6.24%** | 37.43 AUD | 1,637,480 | $5.17B | ADR | Fell 6.24% to A$37.43 - lithium: the lithium complex was smashed after Develop Global said it would pause its Pioneer Dome mine in December, citing the fall in the lithium price (MarketIndex Evening Wrap, 25 Nov; samso Market Update, 25 Nov) |
| `ASX:PLS` | PLS Group Limited | **-5.88%** | 2.56 AUD | 35,829,371 | $5.76B | OTC | Fell 5.88% to A$2.56 - lithium, in the same Develop Global-driven collapse of the lithium complex (MarketIndex Evening Wrap, 25 Nov) |
| `ASX:IGO` | IGO Limited | **-5.25%** | 4.51 AUD | 3,565,936 | $2.36B | ADR | Fell 5.25% to A$4.51 - lithium and gold, in the same complex selloff (MarketIndex Evening Wrap, 25 Nov; samso Market Update, 25 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:6777` | santec Holdings Corporation | **-18.55%** | 14140 JPY | 243,900 | $1.28B | none | Fell 18.55% to Y14,140 - no company-specific release was found for 25 November; it fell with the Japanese AI-hardware complex after the Philadelphia Semiconductor Index dropped 7.9% (Investing.com Japan top losers, 25 Nov; asiapresse, 25 Nov) |
| `TSE:6834` | Seikoh Giken Co., Ltd. | **-18.37%** | 3110 JPY | 1,258,200 | $1.11B | none | Fell 18.37% to Y3,110 - no company-specific release was found for 25 November; it fell with the Japanese precision-instrument complex (Investing.com Japan top losers, 25 Nov; RTTNews via finanzen.at, 25 Nov) |
| `TSE:6525` | Kokusai Electric Corporation | **-17.28%** | 4630 JPY | 9,689,400 | $8.35B | none | Fell 17.28% to Y4,630 - a semiconductor-equipment name in the Japanese AI-hardware rout, listed among the sharpest declines on the Nikkei (MarketScreener, 25 Nov; RTTNews via finanzen.at, 25 Nov) |
| `TSE:4062` | IBIDEN CO., LTD. | **-16.01%** | 4512 JPY | 29,425,700 | $19.09B | OTC | Fell 16.01% to Y4,512 - a named Ibiden in the AI-hardware rout, cited with Kioxia, Advantest, SoftBank and Fujikura as the day's worst performers (Il Sole 24 Ore Radiocor, 25 Nov; Trading Economics, 25 Nov) |
| `TSE:9984` | SoftBank Group Corp. | **-14.83%** | 2696.5 JPY | 93,966,400 | $113.44B | ADR | Fell 14.83% to Y2,696.5 - the biggest investor in OpenAI; it led the Japanese AI unwind after Wall Street's semiconductor selloff (Seoul Economic Daily via CNBC, 25 Nov; Trading Economics, 25 Nov) |
| `TSE:5803` | Fujikura Ltd | **-14.70%** | 2062.5 JPY | 51,111,200 | $26.64B | ADR | Fell 14.70% to Y2,062.5 - a named Fujikura in the AI-hardware rout (Il Sole 24 Ore Radiocor, 25 Nov; RTTNews via finanzen.at, 25 Nov) |
| `TSE:6976` | Taiyo Yuden Co., Ltd. | **-14.55%** | 5874 JPY | 16,490,600 | $5.74B | ADR | Fell 14.55% to Y5,874 - a capacitor maker named among the day's biggest Nikkei decliners (Trading Economics, 25 Nov; MarketScreener, 25 Nov) |
| `TSE:6323` | Rorze Corporation | **-14.48%** | 2639 JPY | 3,064,900 | $3.41B | none | Fell 14.48% to Y2,639 - a semiconductor-equipment name in the same complex (Investing.com Japan top losers, 25 Nov; MarketScreener, 25 Nov) |
| `TSE:6871` | Micronics Japan Co., Ltd. | **-14.33%** | 8179 JPY | 1,310,100 | $2.30B | none | Fell 14.33% to Y8,179 - no company-specific release was found for 25 November; it fell with the Japanese AI-hardware complex (Investing.com Japan top losers, 25 Nov) |
| `TSE:6981` | Murata Manufacturing Co., Ltd. | **-14.20%** | 4633 JPY | 26,678,800 | $62.51B | ADR | Fell 14.20% to Y4,633 - a named Murata Manufacturing in the AI-hardware rout, a close and a change the scanner and Investing.com's Japan table agree on exactly (Investing.com Japan top losers, 25 Nov; Trading Economics, 25 Nov) |
| `TSE:285A` | Kioxia Holdings Corporation | **-14.18%** | 6895 JPY | 121,196,900 | $83.03B | OTC | Fell 14.18% to Y6,895 - a named Kioxia, the memory name most often cited in the AI unwind (Investing.com Japan top losers, 25 Nov; Trading Economics, 25 Nov) |
| `TSE:5801` | Furukawa Electric Co., Ltd. | **-13.48%** | 1563.5 JPY | 27,041,600 | $7.98B | ADR | Fell 13.48% to Y1,563.5 - a named Furukawa Electric among the day's major Japanese losers (Investing.com Japan top losers, 25 Nov; RTTNews via finanzen.at, 25 Nov) |
| `TSE:3436` | SUMCO Corporation | **-13.34%** | 1760.5 JPY | 11,066,500 | $4.47B | OTC | Fell 13.34% to Y1,760.5 - a named SUMCO in the semiconductor-material complex (Investing.com Japan top losers, 25 Nov; RTTNews via finanzen.at, 25 Nov) |
| `TSE:6324` | Harmonic Drive Systems Inc. | **-13.07%** | 3665 JPY | 2,057,700 | $2.55B | OTC | Fell 13.07% to Y3,665 - a precision-motion name in the Japanese machinery complex (Investing.com Japan top losers, 25 Nov; RTTNews via finanzen.at, 25 Nov) |
| `TSE:6857` | Advantest Corp. | **-12.94%** | 23745 JPY | 20,990,800 | $119.42B | ADR | Fell 12.94% to Y23,745 - a named Advantest, the semiconductor test-equipment heavyweight in the AI unwind (Investing.com Japan top losers, 25 Nov; Il Sole 24 Ore Radiocor, 25 Nov) |
| `TSE:8035` | Tokyo Electron Ltd. | **-12.53%** | 7825 JPY | 22,102,900 | $130.65B | ADR | Fell 12.53% to Y7,825 - a named Tokyo Electron, the semiconductor-equipment heavyweight in the same unwind (Investing.com Japan top losers, 25 Nov; RTTNews via finanzen.at, 25 Nov) |
| `TSE:3110` | Nitto Boseki Co., Ltd. | **-12.47%** | 2099.5 JPY | 4,691,700 | $2.82B | OTC | Fell 12.47% to Y2,099.5 - a process-industry materials name in the same complex (Investing.com Japan top losers, 25 Nov; RTTNews via finanzen.at, 25 Nov) |
| `TSE:6278` | Union Tool Co. | **-12.27%** | 9220 JPY | 578,200 | $1.29B | none | Fell 12.27% to Y9,220 - a cutting-tool maker in the Japanese machinery complex (Investing.com Japan top losers, 25 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TWSE:2344` | Winbond Electronics Corp. | **-10.00%** | 94.5 TWD | 75,172,823 | $15.06B | none | Fell 10.00% to NT$94.50 - locked at its daily limit-down; TrendForce's 25 November DRAM bulletin flags Nanya and Winbond as filling the consumer DRAM gap while buyers turn cautious (Investing.com, 25 Nov; TrendForce DRAM Market Bulletin, 25 Nov) |
| `TWSE:2451` | Transcend Information, Inc. | **-10.00%** | 229.5 TWD | 3,544,494 | $3.34B | none | Fell 10.00% to NT$229.50 - locked at its daily limit-down with the memory complex (Investing.com, 25 Nov; CNA via Focus Taiwan, 25 Nov) |
| `TWSE:2454` | MediaTek Inc | **-10.00%** | 3645 TWD | 23,525,057 | $196.50B | none | Fell 10.00% to NT$3,645 - locked at its daily limit-down with the AI supply chain as the TAIEX lost 1,926.92 points (CNA via Focus Taiwan, 25 Nov; Taiwan News, 25 Nov) |
| `TWSE:2880` | Hua Nan Financial Holdings Co., Ltd. | **-10.00%** | 42.75 TWD | 26,000,800 | $20.28B | none | Fell 10.00% to NT$42.75 - locked at its daily limit-down (Taiwan News, 25 Nov) |
| `TWSE:2337` | Macronix International Co., Ltd. | **-10.00%** | 61.2 TWD | 43,607,577 | $4.08B | none | Fell 10.00% to NT$61.20 - the worst main-board performer of the session, locked at its daily limit-down (Investing.com, 25 Nov) |
| `TWSE:2303` | United Microelectronics Corp. | **-9.99%** | 87.4 TWD | 200,354,788 | $36.99B | ADR | Fell 9.99% - effectively the daily limit-down, a foundry name in the AI unwind (CNA via Focus Taiwan, 25 Nov; coinotag, 25 Nov) |
| `TPEX:5289` | Innodisk Corp. | **-9.96%** | 768 TWD | 2,353,413 | $2.55B | none | Fell 9.96% to NT$768 - a memory and industrial-storage name locked near its daily limit-down with the memory complex (Investing.com Taiwan close, 25 Nov; TrendForce DRAM Market Bulletin, 25 Nov) |
| `TPEX:3260` | ADATA Technology Co., Ltd. | **-9.96%** | 244 TWD | 7,048,848 | $2.93B | none | Fell 9.96% to NT$244 - a memory and storage name near its daily limit-down (Investing.com Taiwan close, 25 Nov; TrendForce DRAM Market Bulletin, 25 Nov) |
| `TWSE:3443` | Global Unichip Corp. | **-9.95%** | 5070 TWD | 897,200 | $22.92B | none | Fell 9.95% to NT$5,070 - an AI-chip designer near its daily limit-down with the AI complex (CNA via Focus Taiwan, 25 Nov; Taiwan News, 25 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:VNP` | 5N Plus Inc. | **+7.54%** | 31.93 CAD | 479,767 | $1.87B | OTC | Rose 7.54% to C$31.93 - a specialty-semiconductor and zinc producer that rose with the metals-and-materials complex; no company-specific release was found for 25 November (MarketScreener Canada, 25 Nov; Simply Wall St, 24 Nov) |
| `TSX:FM` | First Quantum Minerals Ltd. | **+6.51%** | 26.01 CAD | 4,863,735 | $14.29B | OTC | Rose 6.51% to C$26.01 - copper: Panama's government and First Quantum are negotiating over a new agreement for Cobre Panama, a process that began on 23 November and is still running (Reuters, 23 Nov; Mining Journal, 24 Nov) |
| `TSX:GMIN` | G Mining Ventures Corp | **+5.87%** | 42.19 CAD | 1,159,565 | $8.28B | OTC | Rose 5.87% to C$42.19 - gold, in the precious-metals bounce off a 14-month low into the close (Reuters via Marketscreener, 25 Nov; Yahoo Finance GC=F, 25 Nov) |
| `TSX:LNR` | Linamar Corporation | **+5.52%** | 90.83 CAD | 187,888 | $3.54B | OTC | Rose 5.52% to C$90.83 - no company-specific release was found for 25 November; it rose with the Canadian industrial complex (MarketScreener Canada, 25 Nov) |
| `TSX:DSV` | Discovery Mining Ltd. | **+5.50%** | 8.83 CAD | 2,636,824 | $4.78B | ADR | Rose 5.50% to C$8.83 - copper: it reported Q3 sales of US$371.4m and net income of US$58.4m and presented at the National Bank Mining Conference in London on 23 November (Simply Wall St, 24 Nov) |
| `TSX:LUNR` | LunR Royalties Corp | **+5.44%** | 13.56 CAD | 191,723 | $1.09B | OTC | Rose 5.44% to C$13.56 - a royalty company, in the precious-metals and mining bounce into the close (MarketScreener Canada, 25 Nov) |
| `TSX:AYA` | Aya Gold & Silver Inc. | **+5.22%** | 28.2 CAD | 1,194,215 | $2.71B | NASDAQ | Rose 5.22% to C$28.20 - gold and silver, in the metals bounce off the lows into the close (Reuters via Marketscreener, 25 Nov) |
| `TSX:EDR` | Endeavour Silver Corp. | **+5.20%** | 8.7 CAD | 1,258,461 | $1.72B | NYSE | Rose 5.20% to C$8.70 - a silver and gold miner, in the same precious-metals bounce (Reuters via Marketscreener, 25 Nov) |
| `TSX:SGD` | Snowline Gold Corp. | **+5.12%** | 11.5 CAD | 299,050 | $1.45B | OTC | Rose 5.12% to C$11.50 - gold, in the precious-metals bounce off a 14-month low into the close (Reuters via Marketscreener, 25 Nov; Yahoo Finance GC=F, 25 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:WAF` | Siltronic AG | **-6.61%** | 46.74 EUR | 186,344 | $1.81B | ADR | Fell 6.61% - a silicon-wafer supplier in the German semiconductor give-back as the AI rebound faded (mlq.ai, 25 Nov; Trading Economics, 25 Nov) |
| `XETR:IFX` | Infineon Technologies AG | **-6.49%** | 40.895 EUR | 7,498,977 | $62.24B | ADR | Fell 6.49% to EUR40.90 - a chip name giving back the prior session's relief rally as the tech rebound sparked by Jensen Huang's return faded (Il Sole 24 Ore Radiocor, 25 Nov; mlq.ai, 25 Nov) |
| `XETR:NDX1` | Nordex SE | **-6.49%** | 33.7 EUR | 936,288 | $9.34B | OTC | Fell 6.49% - a wind-turbine maker; no company-specific release was found for 25 November, and it fell with the European industrials (mlq.ai, 25 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:RCO` | Remy Cointreau SA | **+13.13%** | 58.15 EUR | 413,084 | $2.96B | ADR | Rose 13.13% - H1 2026/27 results: revenue EUR510.9m and current operating income EUR126.7m (+7.8% organic), with the FY26/27 outlook raised and new targets set through FY31/32 (ideal-investisseur, 25 Nov; Newsquawk via StockNow, 25 Nov) |
| `EURONEXT:SOI` | Soitec SA | **-6.92%** | 85.06 EUR | 541,547 | $3.58B | OTC | Fell 6.92% - a semiconductor-substrate supplier giving back the prior session's relief rally (mlq.ai, 25 Nov; Trading Economics, 25 Nov) |
| `EURONEXT:BVI` | Bureau Veritas SA | **+6.60%** | 31.8 EUR | 3,701,763 | $14.47B | ADR | Rose 6.60% - Bloomberg reported that Advent International is weighing a takeover bid; the company denied any discussions with Advent (Reuters, 25 Nov) |
| `EURONEXT:ABVX` | Abivax SA | **+6.01%** | 72.3 EUR | 210,269 | $6.53B | ADR | Rose 6.01% to EUR72.30 - it announced an additional investor meeting ahead of its US marketing-authorisation application for obefazimod (Euronext company releases, 24 Nov; ideal-investisseur, 25 Nov) |
| `EURONEXT:OVH` | OVH Groupe S.A. | **-5.74%** | 12.65 EUR | 207,331 | $2.23B | ADR | Fell 5.74% - a cloud provider in the European technology give-back; no company-specific release was found for 25 November (mlq.ai, 25 Nov) |
| `EURONEXT:EXENS` | Exosens SA | **-5.34%** | 48.7 EUR | 132,889 | $2.87B | none | Fell 5.34% - no company-specific release was found for 25 November; it fell with the European technology complex (mlq.ai, 25 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:PRY` | Prysmian S.p.A. | **-5.40%** | 93.12 EUR | 2,465,780 | $32.22B | ADR | Fell 5.40% - a cable and power-infrastructure name in the European industrials give-back (mlq.ai, 25 Nov; Reuters, 25 Nov) |

### eu-es

No name cleared the volume, cap and move gates in Spain with a sourced driver.

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ASM` | ASM International N.V. | **-7.81%** | 587.6 EUR | 349,826 | $33.92B | ADR | Fell 7.81% to EUR587.60 - a deposit-and-etch equipment maker in the European chip selloff (mlq.ai, 25 Nov) |
| `EURONEXT:ASML` | ASML Holding NV | **-5.79%** | 1131.6 EUR | 985,722 | $501.74B | ADR | Fell 5.79% to EUR1,131.60 - the lithography benchmark, cited with Infineon as the tech rebound faded (Il Sole 24 Ore Radiocor, 25 Nov; mlq.ai, 25 Nov) |
| `EURONEXT:BESI` | BE Semiconductor Industries N.V. | **-5.56%** | 134.3 EUR | 667,674 | $12.55B | ADR | Fell 5.56% to EUR134.30 - a chip-assembly-equipment maker in the same selloff (mlq.ai, 25 Nov) |

### eu-be

No name cleared the volume, cap and move gates in Belgium with a sourced driver.

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | **-7.66%** | 89.2 EUR | 264,307 | $4.10B | OTC | Fell 7.66% - the advanced-substrate and assembly name gave back more of its surge as European chip stocks fell on renewed doubts over AI infrastructure spending (mlq.ai, 25 Nov; Trading Economics, 25 Nov) |
| `VIE:RBI` | Raiffeisen Bank International AG | **-6.29%** | 54.4 EUR | 411,935 | $20.85B | ADR | Fell 6.29% - a bank, in the rate-hike-driven bank selloff that led Europe's declines (Reuters, 25 Nov) |

### eu-pt

No name cleared the volume, cap and move gates in Portugal with a sourced driver.

### eu-ie

No name cleared the volume, cap and move gates in Ireland with a sourced driver.

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:IQMX` | IQM Quantum Computers Oyj Class A | **+6.95%** | 6.23 EUR | 408,508 | $1.16B | ADR | Rose 6.95% - inside information: IQM Quantum Computers received a new order for an IQM Radiance 54-qubit quantum computer from QAI, a South Korean quantum-AI company (Nasdaq Nordic releases, 25 Nov 16:30) |
| `OMXHEX:NOKIA` | Nokia Oyj | **-5.13%** | 6.32 EUR | 15,758,744 | $41.22B | ADR | Fell 5.13% - no company-specific release was found for 25 November; it fell with the European technology complex (mlq.ai, 25 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:ROCK_B` | ROCKWOOL A/S Class B | **-15.64%** | 178 DKK | 2,106,836 | $6.56B | ADR | Fell 15.64% to DKK178.00 - its Q3 report and a cut full-year outlook: revenue growth lowered to about 5% (from 5-7%) and the EBIT margin to about 12% (from 13-14%) on higher-than-expected energy costs (ROCKWOOL release no. 24 via Nasdaq Copenhagen, 25 Nov 14:56; Reuters, 25 Nov) |
| `OMXCOP:NKT` | NKT A/S | **-5.77%** | 710.5 DKK | 394,930 | $5.93B | none | Fell 5.77% - a cable maker in the European industrials give-back; no company-specific release was found for 25 November (mlq.ai, 25 Nov) |

### eu-gr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ATHEX:GEKTERNA` | Gek Terna S.A. | **-6.18%** | 41.28 EUR | 421,529 | $4.65B | OTC | Fell 6.18% - a utility under pressure as the ATHEX posted its steepest fall in 8.5 years, with the banks hit hard (euro2day, 25 Nov 17:48; xrimatistirio, 25 Nov) |
| `ATHEX:OPTIMA` | Optima Bank SA | **-5.05%** | 14.1 EUR | 465,432 | $3.59B | none | Fell 5.05% - a bank, in the sell-off in the Greek systemic banks (euro2day, 25 Nov) |

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a -39% or a +200% move is not noise. Their tickers are printed **without** the backtick format used for CSV rows precisely because they are not CSV rows. **Most of them are sub-$0.05 micro-caps whose percentage carries little information** - their prices, not their percentages, are the signal.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| ASX:ENV | eNova Mining Ltd | **+3900.00%** | 0.04 | 455,967 | $45.5M | below the $300.0M Australia cap floor |
| ASX:ADN | Andromeda Metals Ltd | **+900.00%** | 0.05 | 298,610 | $19.0M | below the $300.0M Australia cap floor |
| ASX:BIT | Biotron Limited | **+100.00%** | 0.002 | 1,302,002 | $2.7M | below the $300.0M Australia cap floor |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| TSE:2388 | Wedge Holdings CO., LTD. | **+66.67%** | 20 | 16,689,500 | $3.2M | below the $300.0M Japan cap floor |
| TSE:4598 | Delta-Fly Pharma, Inc. | **+46.88%** | 94 | 17,771,100 | $8.7M | below the $300.0M Japan cap floor |
| TSE:5255 | Monstarlab Inc. | **-18.33%** | 49 | 2,577,300 | $24.4M | below the $300.0M Japan cap floor |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| TPEX:7595 | Pharmigene, Inc. | **+24.76%** | 13.1 | 2,116,091 | $16.1M | below the $200.0M Taiwan cap floor |
| TPEX:6820 | Acon Optics Communications, Inc. | **-20.00%** | 228 | 166,639 | $187.1M | below the $200.0M Taiwan cap floor |
| TPEX:3585 | Advance Materials Corporation | **-19.33%** | 42.35 | 1,871,320 | $168.8M | below the $200.0M Taiwan cap floor |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| TSXV:NBLC | Nobel Resources Corp | **+100.00%** | 0.01 | 1,167,925 | $734,320 | below the $200.0M Canada cap floor |
| CSE:STGX | Strategx Elements Corp. | **+100.00%** | 0.23 | 301,700 | $5.0M | below the $200.0M Canada cap floor |
| CSE:WIN | Windfall Geotek Inc. | **+100.00%** | 0.01 | 381,200 | $589,478 | below the $200.0M Canada cap floor |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| EURONEXT:ALIBR | Calibre | **+33.33%** | 0.0004 | 21,596,015 | $11.0M | below the $100.0M France cap floor |
| EURONEXT:ALNEV | Neovacs SA | **-20.98%** | 0.0403 | 1,883,355 | $101,592 | below the $100.0M France cap floor |
| EURONEXT:ALSRS | Sirius Media | **+20.79%** | 0.4102 | 252,058 | $878,437 | below the $100.0M France cap floor |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| MIL:ENY | Energy SpA | **+26.62%** | 0.39 | 262,500 | $19.5M | below the $100.0M Italy cap floor |
| MIL:NUS | Nusco SpA | **+8.50%** | 0.434 | 189,000 | $14.7M | below the $100.0M Italy cap floor |
| MIL:RN | Risanamento S.p.A. | **-7.22%** | 0.018 | 9,811,049 | $38.2M | below the $100.0M Italy cap floor |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| BME:VANA | Vanadi Coffee SA | **-11.82%** | 0.0097 | 2,241,585 | $3.0M | below the $100.0M Spain cap floor |
| BME:SAI | Substrate Artificial Intelligence SA | **-6.36%** | 0.0265 | 11,528,671 | $25.3M | below the $100.0M Spain cap floor |
| BME:EZE | Grupo Ezentis SA | **-5.33%** | 0.0515 | 3,342,885 | $47.7M | below the $100.0M Spain cap floor |

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| EURONEXT:NYXH | Nyxoah SA | **-8.05%** | 0.651 | 303,660 | $78.8M | below the $100.0M Belgium cap floor |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| OMXHEX:MODU | Modulight Oyj | **+41.83%** | 1.475 | 1,312,009 | $48.4M | below the $100.0M Finland cap floor |
| OMXHEX:WETTERI | Wetteri Oyj | **-26.90%** | 0.0826 | 617,060 | $20.0M | below the $100.0M Finland cap floor |
| OMXHEX:EEZY | Eezy Oyj | **-8.19%** | 0.129 | 234,941 | $19.2M | below the $100.0M Finland cap floor |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| OMXCOP:UNLGRP | Unlimit Group A/S | **+8.70%** | 0.005 | 3,527,878 | $3.0M | below the $100.0M Denmark cap floor |

## No catalyst

Names that moved with no sourced driver - no company release, no filing, no analyst action, and no sourced sector or macro move behind them - kept separate so they do not dilute the mover table.

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) |
|---|---|---|---|---|---|
| `TSE:6890` | Ferrotec Corporation | **-11.87%** | 5863 JPY | 3,256,900 | $2.25B |
| `TSE:6920` | Lasertec Corp. | **-11.67%** | 29325 JPY | 4,515,400 | $18.68B |
| `TSE:6590` | Shibaura Mechatronics Corp. | **-11.50%** | 2255 JPY | 1,140,600 | $1.10B |
| `TSE:7729` | Tokyo Seimitsu Co., Ltd | **-11.38%** | 10750 JPY | 662,300 | $3.13B |
| `TSE:6787` | Meiko Electronics Co., Ltd. | **-11.34%** | 7740 JPY | 2,642,500 | $2.88B |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) |
|---|---|---|---|---|---|
| `TWSE:6949` | PELL Bio-Med Technology Co Ltd | **-9.98%** | 36.55 TWD | 6,022,498 | $1.62B |
| `TWSE:2441` | Greatek Electronics, Inc. | **-9.95%** | 92.3 TWD | 3,881,548 | $1.77B |
| `TWSE:8021` | Topoint Technology Co., Ltd. | **-9.94%** | 244.5 TWD | 2,235,890 | $1.22B |
| `TWSE:6770` | Powerchip Semiconductor Manufacturing Corp. | **-9.94%** | 48 TWD | 95,163,169 | $7.63B |
| `TWSE:3030` | Test Research, Inc. | **-9.94%** | 208.5 TWD | 2,135,883 | $1.66B |

## Method, source health & caveats

### Method

- **Universe.** The TradingView per-country scanner for each of the 16 boards, pulled with `symbols.query.types = ["stock"]` and the endpoint's `filter` on the scanner's **`country` column - the issuer's own country, not the venue's**. That is what makes a region file hold that country's own issuers; a venue pull would file Apple as a German and a Japanese name. Every pull was set-asserted: the pages were disjoint and their union equalled `totalCount` (au 1,545; jp 3,890; tw 2,347; ca 4,299; eu-de 4,296; eu-fr 543; eu-it 377; eu-es 230; eu-nl 78; eu-be 101; eu-at 66; eu-pt 30; eu-ie 19; eu-fi 189; eu-dk 133; eu-gr 127 - all complete). The America scanner (types `stock` + `dr`, 13,610 rows, set-asserted the same way) is the source for `us_listing` and for the cross-venue cap check.
- **Floors.** Per-region USD floors applied **after** conversion: au $300M + volume >= 100,000; jp $300M; tw $200M; ca $200M; eu-de $300M + volume >= 50,000; eu-fr/it/es/nl/be/at $100M; eu-ie $200M; eu-fi/dk $100M; eu-pt/gr $50M. **The CSV carries 18 columns** - the same 18-column schema as the previous session, so no positional break for a consumer reading the archive.
- **FX.** `usd_cap = market_cap_basic / FX_per_USD[listing_currency]`, i.e. a **division**, because every FX table here is *local currency per 1 USD*. Provider: **frankfurter.app (base USD), rate date 2026-11-25**, plus **open.er-api.com/v6/latest/USD** for TWD (32.918193 per USD), which Frankfurter does not publish. The direction was settled by share-count reconciliation, not by a spot check: `market_cap_basic / close` returns 11.85bn shares for Toyota, 5.67bn for Kioxia, 405.5m for ASML and 1.164bn for SAP - the issuers' real share counts.
- **Cap carrier.** The cap belongs to the issuer and is resolved to the issuer's **primary (common) line**, converted **once** on the primary's currency, and carried to every line of that issuer; `cap_source_symbol` records which line it came from. The primary is the common line whose own `market_cap_basic` carries the source's per-line cap (a fractional part), with the most liquid common line as the tie-break. A group with no common line has no primary and is dropped as `issuer_unresolved`; a carry that fails the same-issuer assertion drops the group as `cap_issuer_mismatch`.
- **Venue collapse.** The issuer's **primary venue's** line wins, not the busiest venue's, and a line whose implied prior close (`close / (1 + change/100)`) misses the prior session's published close by more than 5% is dropped as a stale print and counted in `off_official_rows`. The lookup is per symbol including its share-class suffix, so a Canadian preferred is not compared with its common line. **No off-official rows were found on this session** - every board's lines reconciled against the prior session.
- **Venue-official price.** Where a venue's own print is obtained it is published and the third-party quote is recorded beside it; **no row-level venue print was obtained this session**, so every `price_conflict` cell is empty and the scanner's settle stands as the price. The one venue-official number published is the **ATHEX General index level**, taken from Euronext Athens' own print via the Greek press (euro2day, 25 Nov 17:48).
- **Cross-venue cap check.** The ADR/OTC line is a second reading of the same company-level cap and must agree within 10%. **1,440 comparisons ran and 67 disagreed by more than 10%.** Most of those are the ADR **ratio** rather than a data error - an ADR line carries a different number of underlying shares, so its converted cap differs by design - but the three largest gaps are the matcher's known name-key collisions (`TPEX:5425` against `NYSE:TSM`, `TSE:9716` against `NYSE:NMR`, `TWSE:3703` against `OTC:CTTAY`), which are disclosed below rather than published as cap findings. Every published cap therefore has a second reading behind it, and the local line's cap is what is published.
- **Carry-over.** A row whose close equals the prior session's published close **exactly** (string equality on the written value, never a tolerance) while its volume is zero or its change field is a non-zero leftover is a carry-over; it stays in the CSV with the source's own field, is listed in `_carryover.json` with its `last_trade_date` walked backwards, and is excluded from every mover list.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView per-country scanner | `scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan`, `filter=[{country equal <issuer country>}]`, `types=[stock]` | ok | 16/16 pulls complete; every pull set-asserted (disjoint pages, union == totalCount) |
| TradingView America scanner | `scanner.tradingview.com/america/scan`, `types=[stock, dr]` | ok | 13,610 rows, set-asserted; the source for `us_listing` and the cross-venue cap check |
| TradingView index scanner | `scanner.tradingview.com/global/scan`, `tickers=[SP:XJO, TVC:NI225, TSE:TOPIX, TWSE:IX0001, TSX:TSX, XETR:DAX, EURONEXT:PX1, FTSE:FTSEMIB, BME:IBC, EURONEXT:AEX, EURONEXT:BEL20, VIE:ATX, EURONEXT:PSI20, EURONEXT:ISEQ, OMXHEX:OMXH25, OMXCOP:OMXC20, STOXX:SXXP]` | ok | 16 region index levels plus the STOXX 600 context row |
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/{%5EGSPTSE,GC%3DF}` | ok | used as an independent second reading of the TSX close (34,179.99, +217.688, +0.641%) and of the gold futures path (a 3,453.80 low, back to ~3,596.80 by the US close) |
| Frankfurter FX | `api.frankfurter.app/latest?base=USD` | ok | rate date 2026-11-25; no TWD quote, so TWD came from open.er-api.com |
| open.er-api FX | `open.er-api.com/v6/latest/USD` | ok | used only for TWD (32.918193 per USD), updated Wed, 25 Nov 2026 00:02:31 +0000 |
| Yahoo daily bars (session probe) | `market_session_probe.py --audit --from 2026-11-24 --to 2026-11-25` over all 16 regions | ok | every region reports a session dated 2026-11-25 - **no market was closed** |
| Euronext Athens index / Greek press | `euro2day.gr` (25 Nov, 17:48), `xrimatistirio.com` close table | ok | ATHEX General 2,454.94, -69.94 (-2.77%) - the venue's own print (no Yahoo symbol, no TradingView venue index) |
| Wire services and company releases | per-name news via web_search (Reuters, CNA/Focus Taiwan, Taiwan News, RTTNews, Trading Economics, MarketIndex/samso, ideal-investisseur, Euronext company releases, Nasdaq Nordic releases, GlobeNewswire) | ok | catalysts for every name published in `## Top movers` |
| TSX daily record PDF | `tsx.com/files/alpha/daily-record/AlphaDailyRecord11252026.pdf` | failed | the venue's PDF returned an HTML page instead of the record, so the TSX close was cross-checked against the Yahoo chart API instead |
| MCP finance tools | - | not registered | the `mcp__*` finance tools are absent from this runtime by design; the MCP-over-HTTP bridge was not needed because the scanner and press sources answered |

### Caveats

- **The unit convention.** `market_cap` is **USD**; `open`/`high`/`low`/`close` are in the **listing currency** named in the `currency` column. A cap and a price in one row are therefore in two different currencies, by contract.
- **Taiwan's limit prices are not calculated moves.** 392 Taiwanese stocks touched their daily limit-down on 25 November, and the -10.00% prints in the TAIEX tables are **the floor of the band**, not a valuation. The TAIEX's -4.80% is therefore partly a floor, not a measured decline.
- **The limit-band class is live on two rows, and both are kept out of every published table.** `TPEX:7861` (Bellwether Electronic) prints **-16.21%** - outside Taiwan's +/-10% band - and it printed **+32.78%** yesterday; `TPEX:7924` (TLC BioSciences) prints **-11.25%**, also outside the band. The first one's implied prior (NT$802.0) reconciles exactly with its 24 November close of NT$802, so it is not a stale print, but no price-basis explanation was found and no company-specific release was located for either. Both stay in the CSVs with the source's own field and are disclosed here rather than published as moves.
- **The TSX's +0.64% close is an intraday reversal, not a green session.** Reuters had the index **down 1.67% at 33,393.08 at 10:24 a.m. ET** as spot gold broke below $3,500 to a 14-month low and silver slid 6.2%; it closed **up 217.69 points at 34,179.99** after the metals bounced off their lows into the bell. A reader who takes the Canadian session as “risk-on” will misread the gold and silver miners’ +5% to +7% closes, which are a bounce from a 14-month low, not a new bid.
- **The macro driver was a hot US inflation print, not a company event.** US October core PCE came in at **3.3% y/y against a 3.2% consensus** (up from 3.1%), alongside a firm jobs print, and the Philadelphia Semiconductor Index fell **7.9%** overnight. US markets were closed on Thursday for Thanksgiving, so the US session on this date was still running when the Asian and European boards closed - the US session's own close is not in this artifact.
- **Europe opened higher and closed lower.** The STOXX 600 was up about 0.4% at midday and ended down 1.06% as the US AI rout deepened through the afternoon, so a reader who takes an intraday European quote will get the sign wrong.
- **Greece's index has no machine-readable vendor feed.** The ATHEX General is published from the venue's own print via the Greek press (euro2day, 17:48; xrimatistirio's close table) because the ATHEX has neither a Yahoo index symbol nor a TradingView venue index; the 82 Greek rows themselves come from the scanner like every other board.
- **The US-listing matcher can pair two different companies that share a name.** The `us_listing` column comes from the archive's shipped issuer-name matcher, which is prefix-based; the known false pairs (APA Group with APA Corporation, Perpetual with Perpetuals.com, Endeavour Group with Endeavour Silver) were not adopted as facts, and the cross-venue cap check uses a stricter same-issuer test because a false pair there would manufacture a cap finding.
- **Carry-over rows.** 66 rows across the 16 boards did not trade on 25 November and keep an earlier session's close and change field. They stay in the CSVs with the source's own field, are listed in `_carryover.json` with the date each one last traded, and are excluded from every movers list.
- **Three cross-venue cap gaps are name-key collisions, not cap findings.** `TPEX:5425` (local $0.52bn against `NYSE:TSM` at $1,753.8bn), `TSE:9716` (local $0.87bn against `NYSE:NMR` at $25.9bn) and `TWSE:3703` (local $0.54bn against `OTC:CTTAY` at $15.1bn) are the matcher pairing a small local line with a large unrelated US issuer. None of them is published as a cap finding.
- **No region was closed.** The session probe reports a session dated 2026-11-25 for all 16 boards, and each board's pull was checked against the prior session's file - the venue-collapse test found **zero** off-official rows.

### Sector rotation

Mean and median `change_pct` per sector over the liquid subset (volume >= 100,000), across all 16 boards. The scanner's sector taxonomy puts semiconductors and hardware in `Electronic Technology` and the equipment makers in `Producer Manufacturing`, so both appear below.

**The worst eight sectors:**

| Sector | Names | Mean | Median |
|---|---|---|---|
| Consumer Non-Durables | 107 | +1.71% | +1.89% |
| Retail Trade | 108 | +1.15% | +1.08% |
| Miscellaneous | 11 | +0.73% | +0.81% |
| Consumer Services | 105 | +0.61% | +1.06% |
| Energy Minerals | 61 | +0.47% | +0.37% |
| Non-Energy Minerals | 264 | +0.44% | +0.54% |
| Health Services | 19 | +0.33% | +0.00% |
| Technology Services | 146 | -0.03% | +0.26% |

**The best six sectors:**

| Sector | Names | Mean | Median |
|---|---|---|---|
| Consumer Durables | 130 | -1.31% | -0.56% |
| Communications | 32 | -1.32% | -0.39% |
| Finance | 383 | -1.34% | -1.06% |
| Process Industries | 206 | -2.26% | -1.38% |
| Producer Manufacturing | 328 | -3.88% | -3.72% |
| Electronic Technology | 415 | -6.17% | -6.93% |

The rotation has one theme and no counter-theme: **Electronic Technology - the scanner's sector for semiconductors and hardware - is the worst sector of the day at a mean of -6.17% and a median of -6.93% across 415 liquid names**, with `Producer Manufacturing` (-3.88%) and `Process Industries` (-2.26%) behind it, while consumer-facing sectors held up (`Consumer Non-Durables` +1.71%, `Retail Trade` +1.15%). The damage is not geographic this time - Japanese, Taiwanese, German, Dutch, French, Austrian and Danish hardware names all fell together on the same driver, the hot US core PCE print and the 7.9% drop in the Philadelphia Semiconductor Index. What is NOT one-way is the index-versus-breadth split: Japan's typical name rose while its index fell, and Taiwan's typical name fell harder than its index.

