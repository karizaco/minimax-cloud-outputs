# Cron #05 eod-international-daily — Friday, 20 November 2026

## TL;DR

- **Global markets had a violent risk-off session as Anthropic's IPO failed to lift the AI trade**: the Nikkei fell **5.06%** to 56,436.65, a 3,007.56-point drop and its lowest close since 13 April, the TOPIX lost 3.88% and 93% of Prime Market issues fell; the TAIEX fell **6.23%** to 36,033.29 with **368 limit-downs** and the worst week since 1991; the STOXX 600 lost 2.00% to 625.65, the DAX fell 2.60% below 25,000 for a sixth straight loss day, the TSX lost 2.47% and the ASX 200 fell 1.58% for a seventh straight session; across the 16 boards **4,257 names** were published.
- **The one consequential move was the AI-hardware complex**: Anthropic priced at $83, opened 34% higher, closed 17.07% up at $97.17 and then fell in after-hours - a sell-the-news that left the AI trade unwinding rather than reviving it - so **SoftBank Group -14.48%**, **Kioxia -11.66%**, **Celestica -16.38%**, **ASML -9.33%**, **Infineon -7.91%**, **Delta Electronics -10.00%** (limit-down), **Fujikura -12.19%** and **ASM International -7.20%** led the rout. **The names a US trader can actually reach**: SoftBank Group (ADR), Fujikura (ADR), Kioxia (ADR), Infineon (ADR), ASML (ADR), ASM International (ADR), Sumitomo Metal Mining (ADR), Schaeffler (ADR), Prysmian (ADR), Celestica (NYSE) and Megaport (OTC).
- **The caveat that changes how to read it**: `market_cap` is in **USD** while `open`/`high`/`low`/`close` are in the **listing currency** (the `currency` column says which); Taiwan's -10.00% prints are **limit prices**, not calculated moves; three Taiwanese OTC rows printed **outside Taiwan's +/-10% band** with no sourceable company release and are excluded from every table below; and a second, older leg ran alongside the AI trade - **spot gold fell 3.95% to US$3,545.95/oz** on hawkish Fed commentary, which is what took the Australian and Canadian gold complexes down.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| au | 1 | 1544 | 1544 | 299 | $300M + vol >= 100,000 | 4 | 1225 | 15 | 1 | 0 | 1 | 0 |
| jp | 3 | 3892 | 3868 | 1357 | $300M | 6 | 2504 | 0 | 1 | 0 | 0 | 0 |
| tw | 2 | 2343 | 2343 | 814 | $200M | 67 | 1462 | 0 | 0 | 0 | 2 | 0 |
| ca | 3 | 4298 | 2699 | 604 | $200M | 69 | 1901 | 0 | 125 | 0 | 14 | 0 |
| eu-de | 1 | 4297 | 708 | 128 | $300M + vol >= 50,000 | 4 | 398 | 178 | 0 | 0 | 0 | 0 |
| eu-fr | 1 | 541 | 541 | 258 | $100M | 1 | 282 | 0 | 0 | 0 | 4 | 0 |
| eu-it | 1 | 377 | 377 | 178 | $100M | 2 | 197 | 0 | 0 | 0 | 6 | 0 |
| eu-es | 1 | 231 | 231 | 135 | $100M | 25 | 71 | 0 | 0 | 0 | 21 | 0 |
| eu-nl | 1 | 78 | 78 | 56 | $100M | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| eu-be | 1 | 101 | 101 | 76 | $100M | 1 | 24 | 0 | 0 | 0 | 0 | 0 |
| eu-at | 1 | 66 | 66 | 50 | $100M | 2 | 14 | 0 | 0 | 0 | 3 | 0 |
| eu-pt | 1 | 31 | 31 | 27 | $50M | 0 | 4 | 0 | 0 | 0 | 1 | 0 |
| eu-ie | 1 | 20 | 20 | 17 | $200M | 0 | 3 | 0 | 0 | 0 | 2 | 0 |
| eu-fi | 1 | 189 | 189 | 101 | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| eu-dk | 1 | 133 | 133 | 75 | $100M | 1 | 57 | 0 | 0 | 0 | 1 | 0 |
| eu-gr | 1 | 127 | 127 | 82 | $50M | 0 | 45 | 0 | 0 | 0 | 1 | 0 |
| **total** | | 18268 | 13056 | **4257** | | 186 | 8293 | 193 | 127 | 0 | 56 | 0 |

The exclusion counts are the per-reason counts in `_excluded.json`, not estimates. The reconciliation identity `unique_instruments == written + sum(excluded)` holds for every region.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 8,592.60 | -137.80 / -1.58% | 2026-11-20 | TradingView SP:XJO venue index; MarketIndex Evening Wrap and lithgowmercury, 20 Nov, both report 8,592.60, down 137.8 points or 1.58% - a seventh straight fall and a 490-point week |
| jp | Nikkei 225 | 56,436.65 | -3,007.56 / -5.06% | 2026-11-20 | TradingView TVC:NI225; Reuters and moomoo, 20 Nov, report the close and the 3,007.56-point fall, the fifth-largest on record and the lowest close since 13 April |
| jp | TOPIX | 3,674.22 | -3.88% | 2026-11-20 | TradingView TSE:TOPIX; Reuters, 20 Nov, reports the broader Topix down 3.88% to 3,674.22, with 93% of Prime Market issues falling |
| tw | TAIEX | 36,033.29 | -2,393.60 / -6.23% | 2026-11-20 | TradingView TWSE:IX0001; chipdispatch and 24/7 Wall St., 20 Nov, report 36,033.29, down 2,393.6 points or 6.2% - the third-largest closing point drop on record and the worst week since 1991 |
| ca | S&P/TSX Composite | 33,189.85 | -839.3 / -2.47% | 2026-11-20 | TradingView TSX:TSX; Reuters, 20 Nov, had it at 33,786.80 (-0.71%) by 10:43 ET and on track for its steepest weekly drop since June 2022, and Bloomberg reports it fell as much as 2.1% - the point change is computed from the published close and the published change |
| eu-de | DAX | 24,802.78 | -661.03 / -2.60% | 2026-11-20 | TradingView XETR:DAX and the Xetra official close of 20 Nov 17:50 (DOW JONES via vwd/tradegate): 24,802.78, down 661.03 or 2.60% - a sixth straight loss day and the first close below 25,000 |
| eu-fr | CAC 40 | 7,927.75 | -152.99 / -1.89% | 2026-11-20 | TradingView EURONEXT:PX1 and bankier's European index table, 20 Nov 17:38 |
| eu-it | FTSE MIB | 48,703.72 | -1,235.4 / -2.48% | 2026-11-20 | TradingView FTSE:FTSEMIB and Borsa Italiana's close report, 20 Nov - a fifth straight decline and a 5.6% week |
| eu-es | IBEX 35 | 18,873.09 | -313.11 / -1.63% | 2026-11-20 | TradingView BME:IBC; alertachart's European close table, 20 Nov, reports 18,873.09 against a 19,186.20 previous close, down 1.6% with the week at -5.7% |
| eu-nl | AEX | 1,066.15 | -25.79 / -2.36% | 2026-11-20 | TradingView EURONEXT:AEX and bankier, 20 Nov 17:38 - the AEX closed on its session low |
| eu-be | BEL 20 | 5,797.75 | -87.76 / -1.49% | 2026-11-20 | Euronext's own BEL 20 page, 20 Nov 18:05 CET: last level 5,797.75, since previous close -87.76 (-1.49%); TradingView agrees |
| eu-at | ATX | 6,204.21 | -174.89 / -2.74% | 2026-11-20 | TradingView VIE:ATX and bankier, 20 Nov 17:36 |
| eu-pt | PSI 20 | 9,279.88 | -130.41 / -1.39% | 2026-11-20 | TradingView EURONEXT:PSI20 and bankier, 20 Nov 17:37 |
| eu-ie | ISEQ | 14,378.74 | -317.46 / -2.16% | 2026-11-20 | TradingView EURONEXT:ISEQ and bankier, 20 Nov 17:35 |
| eu-fi | OMX Helsinki 25 | 5,905.12 | -185.1 / -3.04% | 2026-11-20 | TradingView OMXHEX:OMXH25; the 6,090.2 prior close is the level placera/direkt reported for 19 November - the point change is computed from the published close and the published change |
| eu-dk | OMX Copenhagen 20 | 1,594.23 | -19.80 / -1.23% | 2026-11-20 | TradingView OMXCOP:OMXC20 and bankier, 20 Nov 17:07 |
| eu-gr | ATHEX General | 2,552.70 | -48.53 / -1.87% | 2026-11-20 | bankier's European index table, 20 Nov 16:20 CET: ATHEXCOMP 2,552.70, down 48.53; euro2day reported the session opening at the prior close of 2,601.23 - the ATHEX has no Yahoo symbol and no TradingView venue index |
| *context* | STOXX 600 | 625.65 | -2.00% | 2026-11-20 | Reuters, 20 Nov: the pan-European STOXX 600 closed down 2% to 625.65, a fifth straight decline and a weekly loss of more than 5.7% |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 298 | -1.89% | 33 / 251 / 14 | -12.89% | +12.88% |
| jp | 1357 | -2.62% | 70 / 1273 / 14 | -16.87% | +6.89% |
| tw | 812 | -7.26% | 11 / 794 / 7 | -23.40% | +9.89% |
| ca | 590 | -1.64% | 85 / 486 / 19 | -20.21% | +9.00% |
| eu-de | 128 | -2.77% | 19 / 108 / 1 | -11.76% | +5.15% |
| eu-fr | 254 | -1.12% | 42 / 188 / 24 | -23.24% | +8.01% |
| eu-it | 172 | -2.00% | 24 / 136 / 12 | -9.31% | +5.71% |
| eu-es | 114 | -1.54% | 16 / 86 / 12 | -7.60% | +2.53% |
| eu-nl | 56 | -1.94% | 6 / 50 / 0 | -9.33% | +1.94% |
| eu-be | 76 | -1.55% | 4 / 64 / 8 | -8.57% | +1.73% |
| eu-at | 47 | -1.72% | 4 / 36 / 7 | -14.47% | +2.27% |
| eu-pt | 26 | -0.83% | 6 / 15 / 5 | -4.05% | +2.31% |
| eu-ie | 15 | -0.72% | 4 / 8 / 3 | -5.40% | +4.21% |
| eu-fi | 101 | -1.74% | 11 / 86 / 4 | -8.88% | +2.68% |
| eu-dk | 74 | -1.28% | 13 / 56 / 5 | -5.55% | +2.24% |
| eu-gr | 81 | -1.20% | 11 / 62 / 8 | -4.58% | +4.92% |

The breadth table is computed from the written rows, so an index move and the typical name can disagree. On this session they disagreed in **both** directions: the typical name fell harder than its index in Taiwan (index -6.23%, median published name **-7.26%**, because the market was limit-locked in the AI supply chain), in Australia (-1.58% against **-1.89%**), in Germany (-2.60% against **-2.77%**) and in Canada (-2.47% against -1.64% on the index's own weighting); but in **Japan the median published name fell less than the index** (median **-2.62%** against the TOPIX's -3.88% and the Nikkei's -5.06%), because the Nikkei is price-weighted and its losses came from a handful of very high-priced AI names - Advantest alone dragged it down 631 yen, SoftBank Group 428 yen and Tokyo Electron 302 yen (kabutan, 20 Nov; moomoo, 20 Nov).

## Top movers

Liquid names (volume ≥ 100,000, market cap at or above the region's floor) whose move cleared ±5%, with the driver that was actually sourced, largest absolute move first within the region. A row with no sourced driver is not here - it is under `## No catalyst`. Each region also publishes its single biggest liquid mover even when it did not clear ±5%, so no region is silent; a region with no name at all says so instead of publishing an unsourced row.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:MP1` | Megaport Ltd. | **-12.89%** | 14.94 AUD | 3,026,511 | $2.71B | OTC | Fell 12.89% to A$14.94 - shareholders gave the company its **first strike** on the remuneration report, with 58% of the votes cast against it at the AGM (MT Newswires, 20 Nov; NewsWire via perthnow, 20 Nov) |
| `ASX:PRN` | Perenti Limited | **-11.23%** | 1.66 AUD | 5,669,553 | $1.16B | none | Fell 11.23% to A$1.66 - the mining-services group was sold with the resources complex as copper slid to a seven-month low; it separately named Simon Franich as its next CFO (AWP Alliance News, 20 Nov; MarketIndex Evening Wrap, 20 Nov) |
| `ASX:TEA` | Tasmea Limited | **-9.62%** | 7.61 AUD | 2,025,877 | $1.58B | OTC | Fell 9.62% to A$7.61 with no company release found for 20 November - sold with the mining-services complex as the materials sector lost 2.15% (MarketIndex Evening Wrap, 20 Nov) |
| `ASX:ZIP` | Zip Co Ltd. | **-9.41%** | 1.685 AUD | 28,560,193 | $1.55B | none | Fell 9.41% to A$1.685 with no company release found for 20 November - sold with the information-technology sector, down 4.71% and the worst of the 11 (MarketIndex Evening Wrap, 20 Nov) |
| `ASX:SRL` | Sunrise Energy Metals Limited | **-7.52%** | 8.86 AUD | 917,472 | $1.10B | OTC | Fell 7.52% to A$8.86 - the redomiciliation to a US holding company with a Nasdaq primary listing still needs shareholder and court approval, and local holders would trade ASX CDIs rather than the shares directly; the stock is 42.9% lower over a month (ASX announcement, 19 Nov; AFR, 20 Nov; Investing.com, 19 Nov) |
| `ASX:NXT` | Nextdc Limited | **-7.11%** | 9.01 AUD | 4,216,675 | $4.92B | none | Fell 7.11% to A$9.01 - shareholders delivered a **second strike** on the remuneration report with just over 72% of the votes cast against it, even as the company raised its FY27 net-revenue guidance to A$485-500m and underlying EBITDA to A$260-275m (MT Newswires, 20 Nov; AWP Alliance News, 20 Nov) |
| `ASX:MI6` | Minerals 260 Limited | **-6.99%** | 0.665 AUD | 10,516,591 | $1.22B | OTC | Fell 6.99% to A$0.665 - held its AGM on 20 November with no company release found; sold with the critical-minerals complex (MarketIndex Evening Wrap, 20 Nov; fnarena, 20 Nov) |
| `ASX:MAH` | Macmahon Holdings Limited | **-6.75%** | 0.76 AUD | 8,333,275 | $1.14B | none | Fell 6.75% to A$0.76 with no company release found for 20 November - sold with the mining-services complex (MarketIndex Evening Wrap, 20 Nov) |
| `ASX:PDI` | PDI Gold Limited | **-6.05%** | 3.73 AUD | 6,017,576 | $2.62B | OTC | Fell 6.05% to A$3.73 - held its AGM on 20 November with no company release found; sold with the gold complex as spot gold fell 3.95% to US$3,545.95/oz (MarketIndex Evening Wrap, 20 Nov; Investing.com, 20 Nov) |
| `ASX:WGX` | Westgold Resources Ltd | **-5.81%** | 4.86 AUD | 5,276,940 | $3.23B | OTC | Fell 5.81% to A$4.86 with no company release found for 20 November - sold with the gold complex as the All Ords Gold index lost about 3% and bullion fell to a 14-month low (MarketIndex Evening Wrap, 20 Nov; MarketIndex live blog, 20 Nov) |
| `ASX:GMD` | Genesis Minerals Limited | **-5.81%** | 5.84 AUD | 14,372,167 | $4.86B | OTC | Fell 5.81% to A$5.84 - no announcement found; sold with the gold complex on 5.8 times its prior 20-session average volume (smallcaps.com.au Weekly Wrap, 20 Nov; MarketIndex Evening Wrap, 20 Nov) |
| `ASX:PDN` | Paladin Energy Ltd | **-5.49%** | 5.85 AUD | 12,203,964 | $2.13B | OTC | Fell 5.49% to A$5.85 with no company release found for 20 November - sold with the uranium complex (MarketIndex Evening Wrap, 20 Nov; Investing.com AU, 20 Nov) |
| `ASX:LOV` | Lovisa Holdings Ltd. | **-5.45%** | 24.44 AUD | 593,293 | $1.91B | none | Fell 5.45% to A$24.44 with no company release found for 20 November - oil services sold with the energy sector, down 1.30% (MarketIndex Evening Wrap, 20 Nov) |
| `ASX:SEK` | Seek Limited | **-5.33%** | 12.79 AUD | 1,963,244 | $3.22B | ADR | Fell 5.33% to A$12.79 with no company release found for 20 November - sold with the information-technology sector (MarketIndex live blog, 20 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:9984` | SoftBank Group Corp. | **-14.48%** | 3025 JPY | 109,918,800 | $126.39B | ADR | Fell 14.48% to Y3,025 - a 52-week low and -428 yen of the Nikkei's 3,007.56-point fall - after Anthropic's IPO failed to restore confidence in the AI trade; the stock is 67% below its 52-week high (Reuters, 20 Nov; moomoo [Stocks in Focus], 20 Nov; Tokyo Market Summary, 20 Nov) |
| `TSE:5706` | Mitsui Kinzoku Co., Ltd. | **-13.31%** | 1120 JPY | 27,316,700 | $4.64B | none | Fell 13.31% to Y1,120, hitting a year-to-date low, with no company release found for 20 November - sold with the metals and chip-equipment complex (moomoo, 20 Nov; RTTNews, 20 Nov) |
| `TSE:5801` | Furukawa Electric Co., Ltd. | **-12.67%** | 1620 JPY | 41,567,000 | $8.17B | ADR | Fell 12.67% to Y1,620 - a wire and cable name sold as aversion to AI-linked shares hit the AI power-infrastructure complex (Tokyo Market Summary, 20 Nov; RTTNews, 20 Nov) |
| `TSE:5803` | Fujikura Ltd | **-12.19%** | 2252 JPY | 61,153,400 | $28.17B | ADR | Fell 12.19% to Y2,252 to a new year-to-date low - a generative-AI-linked name hit by the AI-trade unwind (moomoo, 20 Nov; Tokyo Market Summary, 20 Nov) |
| `TSE:285A` | Kioxia Holdings Corporation | **-11.66%** | 7307 JPY | 141,192,200 | $85.23B | none | Fell 11.66% to Y7,307 - a memory-chip maker hit by the global AI-hardware rout, 78.4% below its 52-week high (Reuters, 20 Nov; Investing.com, 20 Nov) |
| `TSE:5838` | Rakuten Bank, Ltd. | **-11.65%** | 3915 JPY | 5,143,100 | $4.84B | none | Fell 11.35% to Y3,915 with no company release found for 20 November - sold with the Japanese growth complex as the Nikkei fell 3,007.56 points (moomoo, 20 Nov) |
| `TSE:5713` | Sumitomo Metal Mining Co., Ltd. | **-11.35%** | 5368 JPY | 4,286,600 | $10.34B | ADR | Fell 11.35% to Y5,368 with no company release found for 20 November - sold with the metals complex as copper fell to a seven-month low (RTTNews, 20 Nov; TradingEconomics, 20 Nov) |
| `TSE:4062` | IBIDEN CO., LTD. | **-11.18%** | 4672 JPY | 28,127,600 | $18.64B | ADR | Fell 11.18% to Y4,672 - a semiconductor-substrate and package name with the group's worst one-month drop (-44.3%), hit by the AI-hardware selloff (Investing.com, 20 Nov; TradingEconomics, 20 Nov) |
| `TSE:6871` | Micronics Japan Co., Ltd. | **-11.09%** | 8802 JPY | 2,396,100 | $2.38B | none | Fell 11.09% to Y8,802 with no company release found for 20 November - sold with the chip-equipment complex (moomoo, 20 Nov) |
| `TSE:6525` | Kokusai Electric Corporation | **-11.00%** | 4897 JPY | 8,065,800 | $8.18B | OTC | Fell 11.00% to Y4,897 - a wafer-fabrication-equipment name sold with the AI-exposed chip complex (RTTNews, 20 Nov) |
| `TSE:6752` | Panasonic Holdings Corporation | **-10.88%** | 2687 JPY | 19,902,900 | $44.06B | ADR | Fell 10.88% to Y2,687 - a hardware name down 23.5% over a month, sold with the AI-exposed technology complex (RTTNews, 20 Nov; Investing.com, 20 Nov) |
| `TSE:6323` | Rorze Corporation | **-10.76%** | 2754 JPY | 2,707,500 | $3.40B | none | Fell 10.76% to Y2,754 with no company release found for 20 November - a semiconductor-equipment maker sold with the chip complex (moomoo, 20 Nov) |
| `TSE:3110` | Nitto Boseki Co., Ltd. | **-10.65%** | 2098.5 JPY | 4,869,800 | $2.75B | OTC | Fell 10.65% to Y2,098.5 with no company release found for 20 November - sold with the chip-materials complex (moomoo, 20 Nov) |
| `TSE:6590` | Shibaura Mechatronics Corp. | **-10.52%** | 2338 JPY | 1,865,000 | $1.13B | none | Fell 10.52% to Y2,338 with no company release found for 20 November - a semiconductor-production-equipment maker sold with the chip complex (moomoo, 20 Nov) |

170 further liquid name(s) cleared ±5% in this region and are in `jp.csv`.

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TPEX:1815` | Fulltech Fiber Glass Corp. | **-10.00%** | 99 TWD | 13,690,094 | $2.05B | none | Fell 10.00% to NT$99, locked at its daily limit-down - a PCB materials name hit with the electronics complex (uurl news, 20 Nov) |
| `TPEX:3163` | Browave Corporation | **-10.00%** | 342 TWD | 362,120 | $1.09B | none | Fell 10.00% to NT$342, locked at its daily limit-down - an optical-communication name in the limit-down wave (uurl news, 20 Nov) |
| `TPEX:3374` | Xintec Inc. | **-10.00%** | 319.5 TWD | 4,586,247 | $2.92B | none | Fell 10.00% to NT$319.5, locked at its daily limit-down - an electronics-services name sold with the AI supply chain (uurl news, 20 Nov) |
| `TPEX:7734` | Ableprint Technology Co Ltd | **-10.00%** | 1260 TWD | 62,692 | $1.18B | none | Fell 10.00% to NT$1,260, locked at its daily limit-down - a high-priced PCB materials name hit in the rout (uurl news, 20 Nov) |
| `TWSE:2308` | Delta Electronics, Inc. | **-10.00%** | 900 TWD | 20,355,632 | $78.75B | none | Fell 10.00% to NT$900, locked at its daily limit-down, in a 368-name limit-down session - the AI power-supply bellwether (Gate News via Investing.com, 20 Nov; Taiwan News, 20 Nov) |
| `TWSE:2360` | Chroma Ate Inc. | **-10.00%** | 927 TWD | 1,703,998 | $13.22B | none | Fell 10.00% to NT$927, locked at its daily limit-down - a power-testing name hit with the electronics complex (Gate News, 20 Nov) |
| `TWSE:2368` | Gold Circuit Electronics Ltd | **-10.00%** | 711 TWD | 3,623,221 | $12.57B | none | Fell 10.00% to NT$711, locked at its daily limit-down - a copper-clad-laminate supplier at the front of the AI hardware chain (uurl news, 20 Nov; Gate News, 20 Nov) |
| `TWSE:2449` | King Yuan Electronics Co., Ltd. | **-10.00%** | 157.5 TWD | 15,122,609 | $6.81B | none | Fell 10.00% to NT$157.5, locked at its daily limit-down - a connector maker sold with the AI hardware chain (uurl news, 20 Nov) |
| `TWSE:3026` | Holy Stone Enterprise Co., Ltd. | **-10.00%** | 324 TWD | 2,576,654 | $1.81B | none | Fell 10.00% to NT$324, locked at its daily limit-down - an electronics-components name in the limit-down wave (uurl news, 20 Nov) |
| `TWSE:3406` | GeniuS Electronic Optical Co., Ltd. | **-10.00%** | 648 TWD | 2,587,443 | $2.58B | none | Fell 10.00% to NT$648, locked at its daily limit-down - an optics name hit in the high-priced-stock rout (uurl news, 20 Nov) |
| `TWSE:3443` | Global Unichip Corp. | **-10.00%** | 5400 TWD | 482,722 | $24.38B | none | Fell 10.00% to NT$5,400, locked at its daily limit-down - among the five highest-priced stocks on the market to hit its limit (Taiwan News, 20 Nov; uurl news, 20 Nov) |
| `TWSE:3661` | Alchip Technologies Ltd. | **-10.00%** | 3240 TWD | 3,142,227 | $9.38B | none | Fell 10.00% to NT$3,240, locked at its daily limit-down - an AI-chip designer sold with the semiconductor complex (uurl news, 20 Nov) |

162 further liquid name(s) cleared ±5% in this region and are in `tw.csv`.

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:CLS` | Celestica Inc. | **-16.38%** | 288 CAD | 1,000,710 | $30.32B | NYSE | Fell 16.38% to C$288 - the biggest decliner in the TSX, an AI-server and data-centre hardware maker sold with the technology sector, down 2.9% (Reuters, 20 Nov; RTTNews, 20 Nov; Bloomberg, 20 Nov) |
| `CSE:HG` | Hydrograph Clean Power Inc | **-14.77%** | 3.81 CAD | 922,140 | $1.13B | OTC | Fell 14.77% to C$3.81 with no company release found for 20 November - sold with the Canadian small-cap growth complex as the TSX headed for a seventh straight loss (Bloomberg, 20 Nov) |
| `TSX:ABRA` | AbraSilver Resource Corp. | **-11.46%** | 8.19 CAD | 6,235,467 | $1.04B | OTC | Fell 11.46% to C$8.19 with no company release found for 20 November - a silver-gold name sold with the metals sector as gold fell 3.7% and silver 7% (RTTNews, 20 Nov; Reuters, 20 Nov) |
| `TSX:VZLA` | Vizsla Silver Corp. | **-10.59%** | 3.63 CAD | 2,716,198 | $1.01B | NYSE | Fell 10.59% to C$3.63 - it pushed first production at its Panuco silver-gold project in Mexico back from the second half of 2027 to the second half of 2028 (Yahoo Finance / The Morning Bull, 19 Nov) |
| `TSX:MAU` | Montage Gold Corp. | **-10.04%** | 12.28 CAD | 1,092,137 | $3.88B | OTC | Fell 10.04% to C$12.28 with no company release found for 20 November - sold with the Canadian gold complex (RTTNews, 20 Nov; Reuters, 20 Nov) |
| `TSX:SKE` | Skeena Resources Limited | **-9.26%** | 33.71 CAD | 2,537,754 | $3.26B | NYSE | Fell 9.26% to C$33.71 with no company release found for 20 November - sold with the metals sector (RTTNews, 20 Nov) |
| `TSX:HPS.A` | Hammond Power Solutions Inc. Class A | **-9.17%** | 170.95 CAD | 198,847 | $1.56B | OTC | Fell 9.17% to C$170.95 - among the TSX's top percentage decliners; a transformer maker exposed to the data-centre build-out, sold with the technology sector (Bloomberg, 20 Nov; stockanalysis.com, 20 Nov) |
| `TSX:VNP` | 5N Plus Inc. | **-8.90%** | 28.96 CAD | 690,636 | $2.00B | OTC | Fell 8.90% to C$28.96 with no company release found for 20 November - a specialty semiconductor-materials name sold with the metals and technology complex (RTTNews, 20 Nov) |
| `TSX:SVM` | Silvercorp Metals Inc. | **-8.83%** | 9.5 CAD | 2,166,220 | $1.61B | NYSE | Fell 8.83% to C$9.50 - among the TSX's top percentage decliners, sold with the metals sector as precious-metal prices fell (Bloomberg, 20 Nov; Reuters, 20 Nov) |
| `TSX:TVK` | TerraVest Industries, Inc. | **-8.32%** | 101.9 CAD | 143,701 | $1.68B | OTC | Fell 8.32% to C$101.90 with no company release found for 20 November (Bloomberg, 20 Nov) |
| `TSX:ERO` | Ero Copper Corp. | **-8.29%** | 30.76 CAD | 941,530 | $2.44B | NYSE | Fell 8.29% to C$30.76 - copper slid to a seven-month low on a stronger US dollar and softer China data (Yahoo Finance / The Morning Bull, 19 Nov; RTTNews, 20 Nov) |
| `TSX:FVI` | Fortuna Mining Corp. | **-8.22%** | 10.5 CAD | 1,634,666 | $2.36B | NYSE | Fell 8.22% to C$10.50 with no company release found for 20 November - sold with the metals sector (RTTNews, 20 Nov) |
| `TSX:ELD` | Eldorado Gold Corporation | **-7.91%** | 35.5 CAD | 1,099,048 | $7.03B | NYSE | Fell 7.91% to C$35.50 with no company release found for 20 November - sold with the gold complex as gold fell to a more-than-one-year low (RTTNews, 20 Nov; Reuters, 20 Nov) |

30 further liquid name(s) cleared ±5% in this region and are in `ca.csv`.

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:JEN` | Jenoptik AG | **-11.76%** | 31.82 EUR | 417,604 | $2.27B | OTC | Fell 11.76% to EUR31.82 - an MDAX technology name in the 9.5-11.8% decline band, sold with the AI-exposed complex (BZ/dpa market report, 20 Nov) |
| `XETR:SMHN` | SUSS MicroTec SE | **-9.94%** | 43.86 EUR | 150,601 | $1.02B | OTC | Fell 9.94% to EUR43.86 - an MDAX technology name sold with the AI-exposed complex (dpa / Reuters, 20 Nov; DOW JONES, 20 Nov) |
| `XETR:AIXA` | AIXTRON SE | **-9.50%** | 29.42 EUR | 1,043,149 | $4.02B | ADR | Fell 9.50% to EUR29.42 - a semiconductor-equipment maker sold with the AI complex, with US efforts to curb Chinese firms' use of US chips adding pressure (Reuters, 20 Nov; DOW JONES, 20 Nov) |
| `XETR:PFS0` | PFISTERER Holding SE | **-9.02%** | 54.5 EUR | 79,013 | $1.20B | none | Fell 9.02% to EUR54.50 with no company release found for 20 November - sold with the German industrials (DOW JONES, 20 Nov) |
| `XETR:G24` | Scout24 SE | **-8.03%** | 80.75 EUR | 463,163 | $6.74B | ADR | Fell 8.03% to EUR80.75 - JPMorgan's Marcus Diebel cancelled his recommendation on AI-displacement fears for advertising revenue; the DAX's worst performer (DOW JONES, 20 Nov; dpa/AFX, 20 Nov) |
| `XETR:TKA` | thyssenkrupp AG | **-7.99%** | 10.31 EUR | 3,758,799 | $7.66B | ADR | Fell 7.99% to EUR10.31 - negative guidance from the steel-tube maker Vallourec plus general weakness in raw materials (DOW JONES, 20 Nov) |
| `XETR:IFX` | Infineon Technologies AG | **-7.91%** | 45.44 EUR | 7,794,531 | $70.51B | ADR | Fell 7.91% to EUR45.44 - a DAX technology heavyweight sold with the global AI-hardware rout (Il Sole 24 Ore Radiocor, 20 Nov; dpa, 20 Nov) |
| `XETR:SZG` | Salzgitter AG | **-7.40%** | 43.3 EUR | 250,957 | $3.09B | ADR | Fell 7.40% to EUR43.30 - sold with the European steel complex on weak raw-material prices (DOW JONES, 20 Nov) |
| `XETR:NCH2` | thyssenkrupp nucera AG & Co. KGaA | **-7.20%** | 7.15 EUR | 71,550 | $1.07B | none | Fell 7.20% to EUR7.15 with no company release found for 20 November - sold with the group (DOW JONES, 20 Nov) |
| `XETR:KGX` | KION GROUP AG | **-6.95%** | 29.2 EUR | 816,349 | $4.52B | ADR | Fell 6.95% to EUR29.20 with no company release found for 20 November - sold with the industrial complex (DOW JONES, 20 Nov) |
| `XETR:SHA0` | Schaeffler AG | **-6.94%** | 4.83 EUR | 1,735,225 | $5.38B | ADR | Fell 6.94% to EUR4.83 with no company release found for 20 November (DOW JONES, 20 Nov) |
| `XETR:WAF` | Siltronic AG | **-6.85%** | 51 EUR | 135,886 | $1.98B | ADR | Fell 6.85% to EUR51 with no company release found for 20 November - a wafer maker sold with the chip complex (DOW JONES, 20 Nov) |
| `XETR:ENR` | Siemens Energy AG | **-6.61%** | 118.32 EUR | 3,516,562 | $116.97B | ADR | Fell 6.61% to EUR118.32 - an AI data-centre infrastructure supplier; providers of energy infrastructure for data centres fell up to 6.6% (DOW JONES, 20 Nov; DOW JONES via marketscreener, 20 Nov) |
| `XETR:WCH` | Wacker Chemie AG | **-6.39%** | 75.4 EUR | 83,802 | $4.39B | OTC | Fell 6.39% to EUR75.40 with no company release found for 20 November - sold with the chemicals complex (DOW JONES, 20 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ABVX` | Abivax SA | **-17.21%** | 63 EUR | 842,420 | $7.32B | ADR | Fell 17.21% to EUR63 - **Scorpion Capital disclosed a short position** in the French biotech (Reuters, 20 Nov) |
| `EURONEXT:VK` | Vallourec SA | **-14.57%** | 15.475 EUR | 5,045,085 | $5.17B | ADR | Fell 14.57% to EUR15.48 - disappointing quarterly results with profit down as expected; market participants also blamed raw-material weakness and fears that data-centre construction is losing momentum (Il Sole 24 Ore Radiocor, 20 Nov; DOW JONES, 20 Nov) |
| `EURONEXT:ETL` | Eutelsat Communications SA | **-12.23%** | 1.4745 EUR | 3,090,725 | $2.17B | ADR | Fell 12.23% to EUR1.4745 with no company release found for 20 November - sold with the European technology complex (Reuters European close, 20 Nov) |
| `EURONEXT:SOI` | Soitec SA | **-11.85%** | 96.3 EUR | 570,227 | $4.30B | none | Fell 11.85% to EUR96.30 - the semiconductor-substrate maker gave back part of Thursday's +12.01% gain on results above expectations and raised AI-driven guidance (Il Sole 24 Ore Radiocor, 19 and 20 Nov; Investing.com, 20 Nov) |
| `EURONEXT:FRVIA` | Forvia SE | **-7.11%** | 7.494 EUR | 1,292,314 | $1.74B | none | Fell 7.11% to EUR7.494 with no company release found for 20 November - an automotive supplier sold with the European industrial complex (Reuters European close, 20 Nov) |
| `EURONEXT:NANO` | Nanobiotix SA | **-6.17%** | 24.34 EUR | 98,334 | $1.45B | ADR | Fell 6.17% to EUR24.34 with no company release found for 20 November (Reuters European close, 20 Nov) |
| `EURONEXT:ALO` | Alstom SA | **-5.84%** | 8.38 EUR | 3,631,629 | $4.52B | ADR | Fell 5.84% to EUR8.38 with no company release found for 20 November (Reuters European close, 20 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:TPRO` | Technoprobe SpA | **-9.31%** | 18.41 EUR | 3,585,329 | $14.27B | ADR | Fell 9.31% to EUR18.41 - the probe-card maker for AI chip testing, hit by the AI unwind and the week's sharpest MIB decliner, down about 16% (Il Sole 24 Ore Radiocor, 20 Nov; Alliance News, 20 Nov) |
| `MIL:MFEB` | MFE-MediaForEurope NV Class B | **-8.42%** | 2.59 EUR | 984,419 | $1.60B | none | Fell 8.42% to EUR2.59 - Equita cut its rating to hold and cut its advertising-revenue estimates on 19 November; the shares traded at lows not seen since November 2023 (Alliance News, 19 and 20 Nov) |
| `MIL:PRY` | Prysmian S.p.A. | **-6.29%** | 100.5 EUR | 1,911,308 | $35.24B | ADR | Fell 6.29% to EUR100.50 - a cable maker sold with the AI-exposed industrial complex (Alliance News, 20 Nov; Investing.com, 20 Nov) |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `BME:TRE` | Tecnicas Reunidas SA | **-5.07%** | 28.48 EUR | 173,849 | $2.57B | none | Fell 5.07% to EUR28.48 - the Spanish engineering group, with two-thirds of its revenue and order backlog in the Middle East, sold with the European risk-off session; it closed its buy-back programme on 19 November (Global Banking and Finance, 20 Nov; CNMV, 19 Nov) |

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ASML` | ASML Holding NV | **-9.33%** | 1168 EUR | 1,460,181 | $540.29B | ADR | Fell 9.33% to EUR1,168.00 - its lowest close since April; the semiconductor-equipment bellwether in the global AI unwind, with Jefferies noting that US efforts to curb Chinese firms' use of US chips particularly threaten ASML (Il Sole 24 Ore Radiocor, 20 Nov; DOW JONES, 20 Nov; Investing.com, 20 Nov) |
| `EURONEXT:ASM` | ASM International N.V. | **-7.20%** | 639.6 EUR | 272,735 | $36.82B | ADR | Fell 7.20% to EUR639.60 - a semiconductor-equipment name that rallied on Anthropic-IPO optimism on Thursday and then reversed (Il Sole 24 Ore Radiocor, 20 Nov; Investing.com, 20 Nov) |
| `EURONEXT:PRX` | Prosus N.V. Class N | **-5.94%** | 30.19 EUR | 6,339,659 | $70.19B | ADR | Fell 5.94% to EUR30.19 with no company release found for 20 November - a technology holding sold with the European complex (Reuters European close, 20 Nov) |
| `EURONEXT:BESI` | BE Semiconductor Industries N.V. | **-5.62%** | 142.7 EUR | 684,819 | $13.40B | ADR | Fell 5.62% to EUR142.70 - a semiconductor-equipment name sold with the chip complex (Investing.com, 20 Nov; DOW JONES, 20 Nov) |

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:VIO` | Viohalco SA/NV | **-8.57%** | 14.72 EUR | 4,273 | $4.58B | none | Fell 8.57% to EUR14.72 with no company release found for 20 November - outside the BEL 20, sold with the Belgian complex (24brussels, 20 Nov) |
| `EURONEXT:MELE` | Melexis NV | **-5.23%** | 52.5 EUR | 98,447 | $2.46B | none | Fell 5.23% to EUR52.50 - a BEL 20 constituent sold with the semiconductor complex (24brussels, 20 Nov) |

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | **-14.47%** | 97.5 EUR | 288,809 | $4.86B | OTC | Fell 14.47% to EUR97.50 with no company release found for 20 November - a PCB and AI-hardware name sold with the European technology complex (DOW JONES, 20 Nov) |
| `VIE:AMS2` | ams-OSRAM AG | **-8.11%** | 13.6 EUR | 16,952 | $1.62B | ADR | Fell 8.11% to EUR13.60 with no company release found for 20 November - a semiconductor name sold with the chip complex (DOW JONES, 20 Nov) |

### eu-pt

No liquid name cleared ±5% with a sourced driver in this region.

### eu-ie

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:KRX` | Kingspan Group PLC | **-5.40%** | 91.05 EUR | 487,746 | $19.33B | ADR | Fell 5.40% to EUR91.05 with no company release found for 20 November - a construction-insulation name sold with the Dublin risk-off session, the ISEQ down 2.16% (bankier European index table, 20 Nov) |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:NOKIA` | Nokia Oyj | **-8.88%** | 6.444 EUR | 25,082,196 | $43.94B | none | Fell 8.88% to EUR6.44 - the largest OMX Helsinki 25 decliner, a telecom and AI-exposed hardware name sold with the global rout (Investing.com, 20 Nov; Direkt/efn.se, 20 Nov) |
| `OMXHEX:IQMX` | IQM Quantum Computers Oyj Class A | **-8.54%** | 6 EUR | 154,199 | $1.34B | ADR | Fell 8.54% to EUR6.00 - a quantum-computing name sold with the AI-adjacent technology complex; it filed a 6-K with the SEC on 20 November (qubitsok.com daily edition, 20 Nov; Reuters European close, 20 Nov) |
| `OMXHEX:METSO` | Metso Corporation | **-6.48%** | 14.58 EUR | 2,374,800 | $14.17B | none | Fell 6.48% to EUR14.58 - sold with the Helsinki industrials (Investing.com, 20 Nov) |
| `OMXHEX:WRT1V` | Wartsila Oyj Abp | **-6.02%** | 23.58 EUR | 2,052,759 | $16.25B | none | Fell 6.02% to EUR23.58 - a marine and energy-technology name sold with the Nordic complex, well below its EUR40.75 April peak (Investing.com, 20 Nov; di.se, 20 Nov) |
| `OMXHEX:NESTE` | Neste Corporation | **-5.87%** | 24.68 EUR | 2,351,530 | $22.11B | none | Fell 5.87% to EUR24.68 - a Helsinki oil-and-gas name sold with the sector (Investing.com, 20 Nov) |
| `OMXHEX:OUT1V` | Outokumpu Oyj | **-5.03%** | 3.286 EUR | 1,944,934 | $1.78B | ADR | Fell 5.03% to EUR3.286 - a stainless-steel maker sold with the metals complex (Reuters European close, 20 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:NKT` | NKT A/S | **-5.55%** | 774.5 DKK | 450,227 | $6.47B | OTC | Fell 5.55% to DKK774.50 - a cable maker sold with the European industrials; its Q3 profit missed although 2026 EBITDA was guided to the top of the range (Yahoo Finance, 20 Nov) |
| `OMXCOP:FLS` | FLSmidth & Co. A/S | **-5.43%** | 467 DKK | 292,305 | $4.12B | ADR | Fell 5.43% to DKK467 with no company release found for 20 November - sold with the Copenhagen industrials (finans.dk, 19 Nov) |

### eu-gr

No liquid name cleared ±5% with a sourced driver in this region.

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a +100% or a -50% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:HE8 | Helios Energy Ltd | **+100.00%** | 666,037 | below the $300M cap floor |
| ASX:BIT | Biotron Limited | **+100.00%** | 1,019,027 | below the $300M cap floor |
| ASX:ARV | Artemis Resources Limited | **+50.00%** | 5,916,654 | below the $300M cap floor |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:4586 | Medrx Co., Ltd. | **+38.96%** | 48,351,100 | below the $300M cap floor |
| TSE:3624 | Axel Mark Inc. | **+33.09%** | 23,368,900 | below the $300M cap floor |
| TSE:2388 | Wedge Holdings CO., LTD. | **-20.00%** | 2,979,600 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:6827 | MegaPro Biomedical Co., Ltd. | **-18.72%** | 1,994,477 | below the $200M cap floor |
| TPEX:6820 | Acon Optics Communications, Inc. | **-15.67%** | 121,673 | below the $200M cap floor |
| TPEX:7888 | Libo Pharma Corp. | **-15.64%** | 245,464 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| CSE:MEC | Mustang Energy Corp | **+200.00%** | 203,000 | below the $200M cap floor |
| CSE:FNI | Fathom Nickel, Inc. | **+100.00%** | 284,500 | below the $200M cap floor |
| TSXV:EGR | EGR Exploration Ltd | **-60.00%** | 1,195,000 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| XETR:LPK | LPKF Laser & Electronics SE | **-16.83%** | 793,586 | below the $300M cap floor |
| XETR:TPG0 | Platform Group SE & Co. KGaA | **-15.65%** | 727,393 | below the $300M cap floor |
| XETR:SNG | SINGULUS TECHNOLOGIES AG | **-12.14%** | 113,650 | below the $300M cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALREE | REED | **-38.46%** | 6,179,982 | below the $100M cap floor |
| EURONEXT:ALTAI | LightOn S.A. | **-21.68%** | 239,448 | below the $100M cap floor |
| EURONEXT:ALTHO | Metavisio SA | **-12.50%** | 5,160,132 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:DATA | Datrix S.p.A. | **-20.84%** | 143,500 | below the $100M cap floor |
| MIL:ENY | Energy SpA | **+18.05%** | 289,500 | below the $100M cap floor |
| MIL:AEDES | Aedes Societa Anonima Ligure per Imprese e Costruzioni per azioni | **-10.38%** | 103,020 | below the $100M cap floor |

### eu-es

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-nl

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:NYXH | Nyxoah SA | **-6.38%** | 168,928 | below the $100M cap floor |

### eu-at

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-pt

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-ie

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:ESENSE | Enersense International Oyj | **-10.41%** | 154,073 | below the $100M cap floor |
| OMXHEX:BRETEC | Bioretec Ltd. | **-7.21%** | 1,759,557 | below the $100M cap floor |
| OMXHEX:NANOFH | Nanoform Finland Oyj | **-6.84%** | 130,559 | below the $100M cap floor |

### eu-dk

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-gr

No name below the cap floor cleared the volume gate and the move threshold in this region.

## No catalyst

The names that moved with **no sourced driver**: no company release, no filing, no analyst action, and no sector or macro move behind them that could be sourced. Separate, so they do not dilute the mover table.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `ASX:ALK` | Alkane Resources Ltd | **-5.30%** | 1.52 AUD | 9,454,547 | $1.46B | OTC | Fell 5.30% to 1.52 AUD with no driver found - no release for 20 November could be sourced |
| `ASX:L1G` | L1 Group Limited | **-5.24%** | 1.085 AUD | 2,982,654 | $1.94B | none | Fell 5.24% to 1.085 AUD with no driver found - no release for 20 November could be sourced |
| `ASX:CMM` | Capricorn Metals Ltd | **-5.12%** | 11.48 AUD | 2,392,733 | $3.69B | OTC | Fell 5.12% to 11.48 AUD with no driver found - no release for 20 November could be sourced |
| `ASX:BGL` | Bellevue Gold Limited | **-5.11%** | 1.3 AUD | 15,303,153 | $1.36B | ADR | Fell 5.11% to 1.3 AUD with no driver found - no release for 20 November could be sourced |
| `ASX:IGO` | IGO Limited | **-5.06%** | 4.5 AUD | 6,040,234 | $2.39B | ADR | Fell 5.06% to 4.5 AUD with no driver found - no release for 20 November could be sourced |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TSE:6857` | Advantest Corp. | **-10.32%** | 24255 JPY | 26,119,000 | $118.10B | ADR | Fell 10.32% to 24255 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:6890` | Ferrotec Corporation | **-10.15%** | 6185 JPY | 3,113,000 | $2.33B | OTC | Fell 10.15% to 6185 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:6324` | Harmonic Drive Systems Inc. | **-10.14%** | 3722 JPY | 2,213,700 | $2.50B | OTC | Fell 10.14% to 3722 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:3436` | SUMCO Corporation | **-10.12%** | 1829 JPY | 13,353,500 | $4.46B | ADR | Fell 10.12% to 1829 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:2914` | Japan Tobacco Inc. | **-10.11%** | 5265 JPY | 26,050,600 | $65.09B | ADR | Fell 10.11% to 5265 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:6508` | Meidensha Corporation | **-10.00%** | 6198 JPY | 339,700 | $1.96B | none | Fell 10.00% to 6198 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:3132` | MACNICA HOLDINGS INC. | **-9.97%** | 2776.5 JPY | 2,267,000 | $3.44B | none | Fell 9.97% to 2776.5 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:4186` | Tokyo Ohka Kogyo Co., Ltd. | **-9.96%** | 6416 JPY | 1,510,200 | $5.52B | OTC | Fell 9.96% to 6416 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:6834` | Seikoh Giken Co., Ltd. | **-9.76%** | 3420 JPY | 1,033,800 | $1.10B | none | Fell 9.76% to 3420 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:6055` | Japan Material Co., Ltd. | **-9.71%** | 1450 JPY | 755,600 | $1.03B | none | Fell 9.71% to 1450 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:6366` | Chiyoda Corp. | **-9.70%** | 596 JPY | 5,002,700 | $1.07B | ADR | Fell 9.70% to 596 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:5016` | JX Advanced Metals Corporation | **-9.54%** | 1820.5 JPY | 28,085,300 | $11.94B | ADR | Fell 9.54% to 1820.5 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:5631` | Japan Steel Works, Ltd. | **-9.51%** | 4432 JPY | 1,139,100 | $2.26B | none | Fell 9.51% to 4432 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:4004` | Resonac Holdings Corporation | **-9.47%** | 10995 JPY | 5,587,400 | $14.29B | ADR | Fell 9.47% to 10995 JPY with no driver found - no release for 20 November could be sourced |
| `TSE:4461` | DKS Co. Limited | **-16.87%** | 7340 JPY | 1,664,300 | $585M | none | Fell 16.87% to 7340 JPY with no driver found - no release for 20 November could be sourced |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TWSE:6213` | ITEQ Corporation | **-10.00%** | 355.5 TWD | 1,515,330 | $4.35B | none | Fell 10.00% to 355.5 TWD with no driver found - no release for 20 November could be sourced |
| `TPEX:6223` | MPI Corporation | **-9.99%** | 3560 TWD | 402,272 | $11.75B | none | Fell 9.99% to 3560 TWD with no driver found - no release for 20 November could be sourced |
| `TWSE:6515` | WinWay Technology Co., Ltd. | **-9.98%** | 2885 TWD | 268,587 | $3.54B | none | Fell 9.98% to 2885 TWD with no driver found - no release for 20 November could be sourced |
| `TPEX:6182` | Wafer Works Corp. | **-9.98%** | 56.8 TWD | 14,063,997 | $1.20B | none | Fell 9.98% to 56.8 TWD with no driver found - no release for 20 November could be sourced |
| `TPEX:4979` | Luxnet Corporation | **-9.98%** | 266 TWD | 865,441 | $1.27B | none | Fell 9.98% to 266 TWD with no driver found - no release for 20 November could be sourced |
| `TWSE:1560` | Kinik Co. | **-9.98%** | 523 TWD | 1,512,346 | $2.65B | none | Fell 9.98% to 523 TWD with no driver found - no release for 20 November could be sourced |
| `TWSE:3450` | Elite Advanced Laser Corporation | **-9.98%** | 257 TWD | 1,482,591 | $1.26B | none | Fell 9.98% to 257 TWD with no driver found - no release for 20 November could be sourced |
| `TWSE:6531` | AP Memory Technology Corp. | **-9.98%** | 482.5 TWD | 1,660,325 | $2.64B | none | Fell 9.98% to 482.5 TWD with no driver found - no release for 20 November could be sourced |
| `TWSE:8210` | Chenbro Micom Co., Ltd. | **-9.98%** | 424 TWD | 1,747,400 | $1.78B | none | Fell 9.98% to 424 TWD with no driver found - no release for 20 November could be sourced |
| `TPEX:3324` | AURAS Technology Co., Ltd. | **-9.98%** | 794 TWD | 648,332 | $2.43B | none | Fell 9.98% to 794 TWD with no driver found - no release for 20 November could be sourced |
| `TPEX:6274` | Taiwan Union Technology Corporation | **-9.97%** | 623 TWD | 2,099,861 | $6.28B | none | Fell 9.97% to 623 TWD with no driver found - no release for 20 November could be sourced |
| `TWSE:7769` | Hon. Precision, Inc. | **-9.97%** | 2890 TWD | 907,924 | $17.51B | none | Fell 9.97% to 2890 TWD with no driver found - no release for 20 November could be sourced |
| `TWSE:6472` | Bora Pharmaceuticals Co Ltd | **-9.97%** | 280 TWD | 1,660,081 | $1.21B | ADR | Fell 9.97% to 280 TWD with no driver found - no release for 20 November could be sourced |
| `TPEX:5274` | ASPEED Technology, Inc. | **-9.97%** | 7860 TWD | 369,796 | $10.99B | none | Fell 9.97% to 7860 TWD with no driver found - no release for 20 November could be sourced |
| `TPEX:3644` | Linco Technology Co., Ltd. | **-17.38%** | 252 TWD | 502,685 | $770M | none | Fell 17.38% to 252 TWD with no driver found - no release for 20 November could be sourced |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TSX:POW.PR.E` | Power Corporation of Canada Part.Pfd Shs | **+9.00%** | 94.83 CAD | 300 | $40.83B | none | Rose 9.00% to 94.83 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:AYA` | Aya Gold & Silver Inc. | **-7.82%** | 25 CAD | 3,974,544 | $2.73B | NASDAQ | Fell 7.82% to 25 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:DML` | Denison Mines Corp. | **-7.66%** | 2.41 CAD | 4,867,003 | $1.65B | NYSE | Fell 7.66% to 2.41 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:NXE` | NexGen Energy Ltd. | **-7.55%** | 9.19 CAD | 3,751,193 | $4.77B | NYSE | Fell 7.55% to 9.19 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:CS` | Capstone Copper Corp. | **-7.40%** | 8.01 CAD | 6,824,458 | $4.63B | ADR | Fell 7.40% to 8.01 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:SXGC` | Southern Cross Gold Consolidated Ltd. | **-7.27%** | 6.25 CAD | 1,020,562 | $1.27B | OTC | Fell 7.27% to 6.25 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:SGD` | Snowline Gold Corp. | **-7.22%** | 10.67 CAD | 390,236 | $1.51B | OTC | Fell 7.22% to 10.67 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:BB` | BlackBerry Limited | **-7.04%** | 11.1 CAD | 4,182,924 | $4.89B | NYSE | Fell 7.04% to 11.1 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:CG` | Centerra Gold Inc. | **-7.03%** | 23.94 CAD | 1,318,346 | $3.48B | NYSE | Fell 7.03% to 23.94 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:EDR` | Endeavour Silver Corp. | **-6.99%** | 8.12 CAD | 1,761,293 | $1.81B | NYSE | Fell 6.99% to 8.12 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:FTT` | Finning International Inc. | **-6.88%** | 77.66 CAD | 1,360,316 | $7.55B | OTC | Fell 6.88% to 77.66 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:BLCO` | Bausch + Lomb Corporation | **-6.84%** | 27.67 CAD | 14,542 | $7.41B | NYSE | Fell 6.84% to 27.67 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:FM` | First Quantum Minerals Ltd. | **-6.52%** | 26.1 CAD | 5,579,907 | $16.26B | OTC | Fell 6.52% to 26.1 CAD with no driver found - no release for 20 November could be sourced |
| `TSX:HBM` | Hudbay Minerals Inc | **-6.49%** | 23.19 CAD | 4,258,799 | $7.69B | NYSE | Fell 6.49% to 23.19 CAD with no driver found - no release for 20 November could be sourced |
| `TSXV:UCU` | Ucore Rare Metals Inc. | **-20.21%** | 1.5 CAD | 990,434 | $200M | OTC | Fell 20.21% to 1.5 CAD with no driver found - no release for 20 November could be sourced |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `XETR:DUE` | Durr AG | **-5.68%** | 15.28 EUR | 196,993 | $1.23B | ADR | Fell 5.68% to 15.28 EUR with no driver found - no release for 20 November could be sourced |
| `XETR:VH2` | Friedrich Vorwerk Group SE | **-5.60%** | 69.05 EUR | 107,652 | $1.61B | none | Fell 5.60% to 69.05 EUR with no driver found - no release for 20 November could be sourced |
| `XETR:NDX1` | Nordex SE | **-5.58%** | 36.9 EUR | 625,595 | $10.16B | ADR | Fell 5.58% to 36.9 EUR with no driver found - no release for 20 November could be sourced |
| `XETR:S92` | SMA Solar Technology AG | **-5.52%** | 43.1 EUR | 150,671 | $1.74B | ADR | Fell 5.52% to 43.1 EUR with no driver found - no release for 20 November could be sourced |
| `XETR:VBK` | Verbio SE | **-5.46%** | 20.42 EUR | 135,014 | $1.52B | none | Fell 5.46% to 20.42 EUR with no driver found - no release for 20 November could be sourced |
| `XETR:PUM` | PUMA SE | **-5.33%** | 23.43 EUR | 979,659 | $3.99B | ADR | Fell 5.33% to 23.43 EUR with no driver found - no release for 20 November could be sourced |
| `XETR:LXS` | LANXESS AG | **-5.24%** | 11.4 EUR | 694,891 | $1.14B | ADR | Fell 5.24% to 11.4 EUR with no driver found - no release for 20 November could be sourced |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:UBI` | UBISOFT Entertainment | **-23.24%** | 3.2 EUR | 3,621,314 | $636M | ADR | Fell 23.24% to 3.2 EUR with no driver found - no release for 20 November could be sourced |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `MIL:MFEA` | MFE-MediaForEurope NV Class A | **-6.58%** | 1.79 EUR | 7,560,755 | $1.60B | none | Fell 6.58% to 1.79 EUR with no driver found - no release for 20 November could be sourced |
| `MIL:BFG` | B.F. S.p.A. | **+5.71%** | 8.14 EUR | 69,891 | $2.21B | none | Rose 5.71% to 8.14 EUR with no driver found - no release for 20 November could be sourced |
| `MIL:LUVE` | LU-VE S.p.A. | **-5.48%** | 58.6 EUR | 33,429 | $1.51B | none | Fell 5.48% to 58.6 EUR with no driver found - no release for 20 November could be sourced |
| `MIL:CMB` | Cembre S.p.A. | **-5.07%** | 71.2 EUR | 9,560 | $1.38B | none | Fell 5.07% to 71.2 EUR with no driver found - no release for 20 November could be sourced |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `BME:GRE` | Grenergy Renovables S.A | **-7.45%** | 50.9 EUR | 136,981 | $1.65B | none | Fell 7.45% to 50.9 EUR with no driver found - no release for 20 November could be sourced |
| `BME:ART` | Arteche Lantegi Elkartea SA | **-6.03%** | 26.5 EUR | 38,076 | $1.80B | none | Fell 6.03% to 26.5 EUR with no driver found - no release for 20 November could be sourced |
| `BME:CBAV` | Clinica Baviera SA | **-5.36%** | 53 EUR | 2,367 | $1.00B | none | Fell 5.36% to 53 EUR with no driver found - no release for 20 November could be sourced |
| `BME:EDR` | eDreams ODIGEO | **-7.60%** | 4.44 EUR | 594,943 | $578M | OTC | Fell 7.60% to 4.44 EUR with no driver found - no release for 20 November could be sourced |

### eu-nl

No moved name without a sourced driver in this region.

### eu-be

No moved name without a sourced driver in this region.

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `VIE:MMK` | Mayr-Melnhof Karton AG | **-6.65%** | 68.8 EUR | 81,935 | $1.62B | OTC | Fell 6.65% to 68.8 EUR with no driver found - no release for 20 November could be sourced |
| `VIE:RHIM` | RHI Magnesita NV | **-6.13%** | 29.1 EUR | 2,392 | $1.61B | none | Fell 6.13% to 29.1 EUR with no driver found - no release for 20 November could be sourced |

### eu-pt

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:BCP` | Banco Comercial Portugues S.A. | **-4.05%** | 1.053 EUR | 52,410,194 | $17.84B | ADR | Fell 4.05% to 1.053 EUR with no driver found - no release for 20 November could be sourced |

### eu-ie

No moved name without a sourced driver in this region.

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `OMXHEX:KCR` | Konecranes Oyj | **-5.81%** | 26.6 EUR | 491,318 | $7.37B | none | Fell 5.81% to 26.6 EUR with no driver found - no release for 20 November could be sourced |
| `OMXHEX:SENSO` | Sensofusion Oyj | **-5.57%** | 19.33 EUR | 60,182 | $2.19B | none | Fell 5.57% to 19.33 EUR with no driver found - no release for 20 November could be sourced |

### eu-dk

No moved name without a sourced driver in this region.

### eu-gr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `ATHEX:EVROF` | Evropharma Milk Industry Anonyme Industrial & Commercial Company | **+4.92%** | 5.12 EUR | 37,482 | $73M | none | Rose 4.92% to 5.12 EUR with no driver found - no release for 20 November could be sourced |

## Method, source health & caveats

### Method

- **Universe** - the TradingView per-country scanner, filtered on the ISSUER's own `country` (the endpoint takes it as `filter`; the `filters` key is silently ignored), one call per region and one for the America board. All 17 pulls were complete (`totalCount` == rows returned) on 20 November. 18,268 rows came back across the 16 regions and 4,257 names were published.
- **Floors (USD, applied AFTER conversion)** - au $300M + volume ≥ 100,000; jp $300M; tw $200M; ca $200M; eu-de $300M + volume ≥ 50,000; eu-fr/eu-it/eu-es/eu-nl/eu-be/eu-at $100M; eu-ie $200M; eu-fi/eu-dk $100M; eu-pt/eu-gr $50M.
- **FX** - open.er-api.com, rate date **Fri, 20 Nov 2026 00:02:32 +0000**. The table is **local currency per 1 USD**, so the conversion is a **division**: `usd_cap = market_cap_basic / FX[listing_currency]`. The identity asserted on every published row is `usd_cap * FX_per_USD == market_cap_local`.
- **Venue collapse** - the issuer's PRIMARY listing venue wins (au ASX; jp TSE/NAG/FSE/SAPSE; tw TWSE/TPEX; ca TSX/TSXV/CSE/NEO; eu-de XETR/FWB/LSX/LS/GETTEX/DUS/MUN/SWB/TRADEGATE/HAM/HAN), and a line whose implied prior close (`close / (1 + change/100)`) does not reconcile with the prior session's published close for the same symbol within 5% is a `stale_venue_print` and is dropped. Off-official lines are counted in the Coverage table.
- **Cap carrier** - the cap is resolved to the issuer's PRIMARY (common) line, converted ONCE with the primary's currency, and every line of that issuer carries that one USD figure; `cap_source_symbol` names the line it came from. A group with no common line is dropped as `issuer_unresolved` rather than published with a borrowed cap.
- **Cross-venue cap check** - the America scanner is a second reading of the same company-level cap. **94 of 1352 issuers with a US line disagree by more than 10%** after conversion; the primary venue's cap is the one published in every case, and the disagreements are listed in the caveats below.
- **Venue-official price rule** - where an exchange's own auction/close is published it is the price and the row carries the conflict in `price_conflict`. **No row-level conflict was found today**: the scanner close stood for every published row and every `price_conflict` cell is empty. The venue-official prices in this artifact are at index level - the BEL 20 from Euronext's own page, the DAX from the Xetra official close and the ATHEX General from the Greek index table - because the ATHEX has no Yahoo symbol and no TradingView venue index.
- **CSV columns** - **18**, unchanged from the previous session (`date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`). Prices are written to 4 decimals with trailing zeros stripped; `volume` and `market_cap` are integers.
- **Files written** - `international-eod/2026-11-20/`: 16 per-region CSVs (`au.csv` … `eu-gr.csv`), `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView au scanner | scanner.tradingview.com/australia/scan, filter country = Australia, types = stock | ok | 2116 of 2116 rows, complete |
| TradingView jp scanner | scanner.tradingview.com/japan/scan, filter country = Japan, types = stock | ok | 4354 of 4354 rows, complete |
| TradingView tw scanner | scanner.tradingview.com/taiwan/scan, filter country = Taiwan, types = stock | ok | 2711 of 2711 rows, complete |
| TradingView ca scanner | scanner.tradingview.com/canada/scan, filter country = Canada, types = stock | ok | 8079 of 8079 rows, complete |
| TradingView eu-de scanner | scanner.tradingview.com/germany/scan, filter country = Germany, types = stock | ok | 4560 of 4560 rows, complete |
| TradingView eu-fr scanner | scanner.tradingview.com/france/scan, filter country = France, types = stock | ok | 693 of 693 rows, complete |
| TradingView eu-it scanner | scanner.tradingview.com/italy/scan, filter country = Italy, types = stock | ok | 383 of 383 rows, complete |
| TradingView eu-es scanner | scanner.tradingview.com/spain/scan, filter country = Spain, types = stock | ok | 234 of 234 rows, complete |
| TradingView eu-nl scanner | scanner.tradingview.com/netherlands/scan, filter country = Netherlands, types = stock | ok | 109 of 109 rows, complete |
| TradingView eu-be scanner | scanner.tradingview.com/belgium/scan, filter country = Belgium, types = stock | ok | 105 of 105 rows, complete |
| TradingView eu-at scanner | scanner.tradingview.com/austria/scan, filter country = Austria, types = stock | ok | 66 of 66 rows, complete |
| TradingView eu-pt scanner | scanner.tradingview.com/portugal/scan, filter country = Portugal, types = stock | ok | 32 of 32 rows, complete |
| TradingView eu-ie scanner | scanner.tradingview.com/ireland/scan, filter country = Ireland, types = stock | ok | 20 of 20 rows, complete |
| TradingView eu-fi scanner | scanner.tradingview.com/finland/scan, filter country = Finland, types = stock | ok | 190 of 190 rows, complete |
| TradingView eu-dk scanner | scanner.tradingview.com/denmark/scan, filter country = Denmark, types = stock | ok | 173 of 173 rows, complete |
| TradingView eu-gr scanner | scanner.tradingview.com/greece/scan, filter country = Greece, types = stock | ok | 128 of 128 rows, complete |
| TradingView america scanner | scanner.tradingview.com/america/scan, types = stock + dr | ok | 13602 of 13602 rows, complete - the source for `us_listing` and for the cross-venue cap check |
| TradingView global scanner | scanner.tradingview.com/global/scan, 17 index tickers | ok | 17 index closes (16 regions + the STOXX 600) |
| FX | open.er-api.com/v6/latest/USD | ok | rate date Fri, 20 Nov 2026 00:02:32 +0000 |
| Index levels - press and exchange pages | Reuters, MT Newswires, DOW JONES via vwd/tradegate, Il Sole 24 Ore Radiocor, dpa/AFX, Euronext's own BEL 20 page, bankier's European index table, alertachart's European close table, chipdispatch, 24/7 Wall St., MarketIndex, lithgowmercury, perthnow, euro2day, Investing.com, 20 Nov 2026 | ok | every one of the 16 regional index levels published above was cross-checked against a second reading; the ATHEX General is the only level with no venue page and is carried from the Greek index table |
| Yahoo news endpoint | query2.finance.yahoo.com/v1/finance/search | no data | **HTTP 429** from this egress - a rate limit, not an absence; every catalyst was sourced from the exchange, the company IR release, the press or the local financial press instead, so no artifact column depends on it |

### Caveats

- **Three Taiwanese OTC rows printed OUTSIDE Taiwan's ±10% daily limit band and are excluded from every published table.** **TPEX:6696** closed NT$119.50 against a NT$155.00 prior close (-22.90%) after opening at the prior close and printing a NT$110.00 low - a move far outside Taiwan's +/-10% daily limit band, with no company release for 20 November that could be sourced; **TPEX:7729** closed NT$203 against a NT$265.00 prior close (-23.40%), opening at the prior close and printing a NT$190 low - outside Taiwan's +/-10% daily limit band, with no company release for 20 November that could be sourced; **TPEX:7686** closed NT$619 against a NT$723.00 prior close (-14.38%) - outside Taiwan's +/-10% daily limit band, with no company release for 20 November that could be sourced. Each row stays in `tw.csv` with the source's own `change_pct`, and each one reconciles arithmetically with the prior session's published close (the implied prior equals the prior close exactly), so the venue-collapse test passes them - the open field is also equal to the prior close, so there is no contract-adjustment signature either. They are disclosed rather than silently published because a move beyond the venue's limit band cannot be read as an ordinary session move and no company release could be sourced for any of them.
- **Taiwan's -10.00% prints are limit prices, not calculated moves.** TWSE and TPEX cap a daily move at ±10%, so a -10.00% close is a limit print and the market was shut at that price. The session was violent: the TAIEX gapped down more than 780 points at the open, touched 35,738.68 intraday and closed down 2,393.60 points at 36,033.29, with **368 stocks at their limit-down** (179 TWSE, 189 OTC) and 1,896 falling against 66 rising; the three institutional investor groups net sold TWD 522.46bn (uurl news, 20 Nov; Gate News, 20 Nov; Taiwan News, 20 Nov).
- **The Nikkei fell more than 3,000 points for the fifth time in its history, and its weekly drop of 4,705.75 yen was the second-largest on record** - behind the 5,855.34-yen fall in the first week of November. The fall was concentrated in a handful of price-weighted names: Advantest alone dragged the index down 631 yen, SoftBank Group 428 yen and Tokyo Electron 302 yen (kabutan, 20 Nov; moomoo, 20 Nov; note.com/minkabu, 20 Nov).
- **The move was not only an AI story: gold was the second leg.** Spot gold fell 3.95% to US$3,545.95/oz - its lowest since September 2025 and on track for its worst week since March - on hawkish Fed commentary from Chicago Fed President Austan Goolsbee, who did not rule out a larger-than-usual December hike; silver fell about 13% on the week, copper fell 10.35% to a seven-month low, and the ASX All Ords Gold index lost about 20% since 10 November (Investing.com, 20 Nov; MarketIndex live blog, 20 Nov; smallcaps.com.au, 20 Nov). Gold and materials together accounted for more than half of the ASX 200's week (lithgowmercury, 20 Nov).
- **The Japanese market had a second, domestic driver: inflation.** Japan's October CPI accelerated to 2.3% from 2.1%, the highest since November 2025, reinforcing expectations of further Bank of Japan rate hikes and adding to the pressure on the Nikkei (gomarkets/fxstreet, 20 Nov).
- **The ATHEX General has no vendor index.** Its level (2,552.70, -1.87%) is carried from the Greek index table's 16:20 CET print, cross-checked against euro2day's report that the session opened at the prior close of 2,601.23 and against the report of 95 declines against 10 advances; two other readings of the same session (2,549.25 and a 2,642.07 print) are inconsistent with each other and are not used.
- **`us_listing` changed on 64 rows against the previous session.** 42 rows gained a US listing and 18 rows lost one. The matcher is unchanged from the previous session (the punctuation-clean issuer key with the trailing period stripped, which was the fix that landed on 19 November), so a change here is a change in the America scanner's own file, not a change in the rule.
- **94 cross-venue cap disagreements above 10%** were recorded, against 73 on the previous session. The published cap is always the primary venue's; the gap is a second-reading disagreement, not a defect in the published number. The largest cases on this session pair a local line with an **unrelated** same-named US company (ASX:WOW with OTC:WLWHY, ASX:CGF with OTC:CLLEF, ASX:PPT with NASDAQ:PDC) and are the matcher limitation named above, not cap findings; a genuine one is ASX:APA, a US operating subsidiary rather than the same issuer.
- **56 rows are carry-overs** - instruments that did not trade on this session, whose close is the prior session's print. They are kept in the CSVs as the source returned them, listed in `_carryover.json` with the date of each instrument's last actual trade (walked back through the prior files, never forward), and excluded from every table above.
- **Sector rotation** (over the written rows, mean and median `change_pct` per sector) - the weakest sectors on this session were semiconductors and semiconductor equipment on the TSE, electronic components and glass/ceramics on the TAIEX, and the materials and information-technology complexes on the ASX 200, where information technology closed down 4.71% and materials down 2.15% while utilities fell only 0.53% and consumer staples 0.84% (MarketIndex Evening Wrap, 20 Nov). The rotation is computed from the same rows as the breadth table; no cap-weighted sector aggregate is published, because this file's caps are company-level and deduplicate on `cap_source_symbol`.
