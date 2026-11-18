# Cron #05 eod-international-daily — Wednesday, 18 November 2026

## TL;DR

- **Europe fell hardest and Asia rebounded**: the STOXX 600 lost 1.03%, the DAX 1.19%, the ATX 1.95% and the IBEX 35 1.28% on weak commodities and hot euro-area/UK inflation data, Canada sank 2.09% to a more-than-four-month low on the metals crash and the ASX 200 lost 0.69% (a fifth straight fall), while Nvidia's beat lifted Asia - the Nikkei +0.28%, the TAIEX +0.26% after a 1,677-point intraday swing and the Kospi +1.99%; across the 16 boards **4,323 names** were published.
- **The one consequential move was the metals complex**: LME three-month copper plunged 3.5-5.4% to a seven-month low near US$12,700/t and spot gold broke below US$3,800/oz at a one-year low, taking Canada's base metals with it - and the US-reachable names are **Ero Copper (-11.34%, NYSE), Hudbay Minerals (-8.16%, NYSE), First Quantum (-7.99%, OTC), Repsol (-6.42%, ADR), Innate Pharma (-18.08%, ADR) and DEUTZ (-16.56%, OTC)**; the single largest name move was Nuix, +45.28%, on a A$2.75/share private-equity proposal.
- **The caveat that changes how to read it**: `market_cap` is in **USD** while `open`/`high`/`low`/`close` are in the **listing currency** (the `currency` column says which), Taiwan's +9.9% prints are **limit prices** rather than calculated moves, and the ATHEX General's official close (2,584.51) came from the press because no vendor index covers it.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,546 | 1,546 | **298** | $300M + vol ≥ 100,000 | 4 | 1224 | 19 | 1 | 0 | 1 | 0 |
| `jp` | NAG, SAPSE, TSE | 3,897 | 3,867 | **1,375** | $300M | 3 | 2488 | 0 | 1 | 0 | 1 | 0 |
| `tw` | TPEX, TWSE | 2,342 | 2,342 | **853** | $200M | 57 | 1432 | 0 | 0 | 0 | 2 | 0 |
| `ca` | CSE, TSX, TSXV | 4,299 | 2,697 | **613** | $200M | 61 | 1898 | 0 | 125 | 0 | 34 | 0 |
| `eu-de` | XETR | 4,297 | 707 | **123** | $300M + vol ≥ 50,000 | 4 | 397 | 183 | 0 | 0 | 0 | 0 |
| `eu-fr` | EURONEXT | 538 | 537 | **260** | $100M | 1 | 276 | 0 | 0 | 0 | 3 | 1 |
| `eu-it` | MIL | 378 | 378 | **179** | $100M | 2 | 197 | 0 | 0 | 0 | 7 | 0 |
| `eu-es` | BME | 232 | 232 | **136** | $100M | 23 | 73 | 0 | 0 | 0 | 23 | 0 |
| `eu-nl` | EURONEXT | 77 | 77 | **56** | $100M | 0 | 21 | 0 | 0 | 0 | 1 | 0 |
| `eu-be` | EURONEXT | 100 | 100 | **76** | $100M | 1 | 23 | 0 | 0 | 0 | 0 | 0 |
| `eu-at` | VIE | 66 | 66 | **51** | $100M | 3 | 12 | 0 | 0 | 0 | 3 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **27** | $50M | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| `eu-ie` | EURONEXT | 20 | 20 | **17** | $200M | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `eu-fi` | OMXHEX | 189 | 189 | **101** | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| `eu-dk` | OMXCOP | 133 | 133 | **75** | $100M | 1 | 57 | 0 | 0 | 0 | 2 | 0 |
| `eu-gr` | ATHEX | 128 | 128 | **83** | $50M | 0 | 45 | 0 | 0 | 0 | 0 | 0 |
| **total** | | **18,273** | **13,050** | **4,323** | | **164** | **8234** | **202** | **127** | **0** | **77** | **1** |

`Universe` is every instrument the source returns for that country's own listings (the scanner's issuer-country filter, `type=stock`, so a foreign company's local line is not counted); `Unique instruments` collapses the same line quoted on several venues down to one line per share class; `Written` applies the per-region USD market-cap floor plus the region's volume gate. Every excluded row carries a reason from the closed set in `_excluded.json`, and the counts above are read from that file rather than estimated.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 8,821.80 | -61.40 / -0.69% | 2026-11-18 | TradingView SP:XJO; NewsWire via PerthNow and MarketIndex Evening Wrap, 18 Nov, both report 8,821.8, down 61.4 points, a fifth straight fall with nine of eleven sectors lower |
| jp | Nikkei 225 | 59,024.06 | +163.85 / +0.28% | 2026-11-18 | TradingView TVC:NI225 venue index read 59,024.06; Newson Japan and kabutan, 18 Nov, report 59,024.28, up 163.85 points - a 0.22-point difference against the venue index |
| jp | TOPIX | 3,824.00 | -16.02 / -0.42% | 2026-11-18 | TradingView TSE:TOPIX venue index, which agrees with Newson Japan and kabutan, 18 Nov, on the third consecutive decline; there is no Yahoo index symbol for the TOPIX |
| tw | TAIEX | 40,194.91 | +102.80 / +0.26% | 2026-11-18 | TradingView TWSE:IX0001; Economic Daily News and uurl, 18 Nov, report the same close after an intraday swing of 1,677.21 points from 40,938.20 to 39,260.99, with 21 limit-up and 4 limit-down stocks |
| ca | S&P/TSX Composite | 34,578.05 | -737.25 / -2.09% | 2026-11-18 | TradingView TSX:TSX venue index; Reuters, 18 Nov, had it at 34,737.31 (-1.64%) at 10:35 ET and BNN Bloomberg at 34,663.61 intraday - a more-than-four-month low |
| eu-de | DAX (Xetra) | 25,736.24 | -309.13 / -1.19% | 2026-11-18 | TradingView XETR:DAX venue index; DPA, 18 Nov, reports the DAX down 1.19%, while Investing.com's close-of-session note says 1.11% - a third-party read |
| eu-fr | CAC 40 | 8,146.83 | -69.95 / -0.85% | 2026-11-18 | TradingView EURONEXT:PX1; Investing.com, 18 Nov, reports the CAC down 0.85% at the close, with losses in oil & gas, financials and consumer services |
| eu-it | FTSE MIB | 50,173.67 | -672.14 / -1.32% | 2026-11-18 | TradingView FTSE:FTSEMIB venue index |
| eu-es | IBEX 35 | 19,373.30 | -252.00 / -1.28% | 2026-11-18 | TradingView BME:IBC; FolioBots Newsroom, 18 Nov, reports the same close on a third straight fall, with Repsol the worst performer; Investing.com says -1.26% |
| eu-nl | AEX | 1,098.73 | -11.16 / -1.01% | 2026-11-18 | TradingView EURONEXT:AEX; ANP via rd.nl and iex.nl, 18 Nov, both report 1,098.73, down 1% |
| eu-be | BEL 20 | 5,952.51 | -34.47 / -0.58% | 2026-11-18 | TradingView EURONEXT:BEL20 venue index |
| eu-at | ATX | 6,394.72 | -127.16 / -1.95% | 2026-11-18 | TradingView VIE:ATX venue index |
| eu-pt | PSI 20 | 9,499.65 | -94.07 / -0.98% | 2026-11-18 | TradingView EURONEXT:PSI20 venue index |
| eu-ie | ISEQ | 14,777.60 | -18.72 / -0.13% | 2026-11-18 | TradingView EURONEXT:ISEQ venue index |
| eu-fi | OMX Helsinki 25 | 6,108.59 | -65.46 / -1.06% | 2026-11-18 | TradingView OMXHEX:OMXH25 venue index |
| eu-dk | OMX Copenhagen 20 | 1,637.24 | -19.18 / -1.16% | 2026-11-18 | TradingView OMXCOP:OMXC20 venue index |
| eu-gr | ATHEX General | 2,584.51 | -53.18 / -2.02% | 2026-11-18 | protothema, 18 Nov 17:29, reports the General Index closing at 2,584.51, down 53.18 points or 2.02%, at the day's low, with bank shares down more than 3%; the ATHEX has no Yahoo symbol and no TradingView venue index |
| *context* | STOXX 600 | 644.05 | -6.67 / -1.03% | 2026-11-18 | TradingView STOXX:SXXP; DPA, 18 Nov, reports the pan-European index down 1.03% on weak commodities and hot euro-area and UK inflation data |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| `au` | 298 | -0.86% | 58 / 214 / 26 | -16.91% | +45.28% |
| `jp` | 1,375 | -0.76% | 369 / 974 / 32 | -15.16% | +13.03% |
| `tw` | 853 | +0.00% | 413 / 400 / 40 | -23.59% | +10.69% |
| `ca` | 613 | -0.38% | 159 / 390 / 64 | -12.35% | +13.73% |
| `eu-de` | 123 | -0.83% | 40 / 82 / 1 | -16.56% | +4.95% |
| `eu-fr` | 260 | -0.45% | 74 / 160 / 26 | -18.08% | +9.60% |
| `eu-it` | 179 | -0.42% | 59 / 107 / 13 | -4.72% | +5.68% |
| `eu-es` | 136 | -0.39% | 30 / 73 / 33 | -6.90% | +8.66% |
| `eu-nl` | 56 | -0.43% | 17 / 35 / 4 | -6.08% | +3.21% |
| `eu-be` | 76 | -0.17% | 25 / 43 / 8 | -8.80% | +2.74% |
| `eu-at` | 51 | -0.51% | 16 / 29 / 6 | -6.88% | +3.91% |
| `eu-pt` | 27 | -0.86% | 4 / 18 / 5 | -8.22% | +3.15% |
| `eu-ie` | 17 | +0.25% | 10 / 6 / 1 | -2.43% | +4.05% |
| `eu-fi` | 101 | -0.60% | 25 / 70 / 6 | -5.33% | +4.86% |
| `eu-dk` | 75 | -0.44% | 21 / 46 / 8 | -6.64% | +4.50% |
| `eu-gr` | 83 | -0.34% | 21 / 48 / 14 | -4.70% | +2.43% |

## Top movers

Liquid names (volume ≥ 100,000 and market cap at or above the region's floor) whose move cleared ±5%, with the driver that was actually sourced. A row with no sourced driver is not here - it is under `## No catalyst`. Regions where no name cleared the threshold with a sourced driver say so instead of publishing an unsourced row.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:NXL` | Nuix Ltd. | **+45.28%** | 2.31 AUD | 5,364,928 | $368M | none | Rose 45.28% to A$2.31 after Nuix signed a process and exclusivity deed with US private equity firm Haveli Investments over a non-binding indicative proposal of A$2.75 a share in cash - a 73.0% premium to Tuesday's A$1.59 close - with five weeks of exclusivity, no break fee payable, and Macquarie Corporate Holdings (~28%) supporting the process (MT Newswires via au.finance.yahoo, 18 Nov; acquisitionsnews, 18 Nov; Samso Market Update, 18 Nov; ShareCafe, 18 Nov) |
| `ASX:LLC` | Lendlease Group | **-16.91%** | 1.72 AUD | 11,165,447 | $956M | ADR | Fell 16.91% to A$1.72, the biggest faller among ASX companies worth more than A$1bn, as Morgan Stanley downgraded it to Underweight from Equal Weight and cut its target to A$2.24 from A$3.21 (Samso Market Update, 18 Nov; MarketIndex Evening Wrap, 18 Nov) |
| `ASX:OBM` | Ora Banda Mining Ltd. | **-9.66%** | 1.31 AUD | 9,205,702 | $1.89B | OTC | Fell 9.66% to A$1.31 with no company release for 18 November - it was sold with the resources complex as the ASX materials sector fell 1.08%, LME copper dropped 3.5-5.4% to a seven-month low near US$12,700/t and spot gold broke below US$3,800/oz at a one-year low (MarketIndex Evening Wrap, 18 Nov; Reuters via au.finance.yahoo, 18 Nov; CNBC, 18 Nov) |
| `ASX:TEA` | Tasmea Limited | **-9.49%** | 8.87 AUD | 1,130,205 | $1.86B | none | Fell 9.49% to A$8.87 with no company release for 18 November - sold with the mining sector as gold and copper fell together and the ASX materials sector dropped 1.08% (MarketIndex Evening Wrap, 18 Nov; The Edge Singapore, 18 Nov) |
| `ASX:IPH` | IPH Ltd. | **-7.60%** | 3.16 AUD | 4,013,541 | $590M | none | Fell 7.60% to A$3.16 with no company release for 18 November - sold with the gold complex, and Macquarie cut its target to A$3.37 from A$3.65 while retaining Neutral (MarketIndex Evening Wrap, 18 Nov) |
| `ASX:PRN` | Perenti Limited | **-7.11%** | 1.96 AUD | 3,511,653 | $1.33B | none | Fell 7.11% to A$1.96 with no company release for 18 November - sold with the mining and gold complex as spot gold fell about 2% to a one-year low (MarketIndex Evening Wrap, 18 Nov) |
| `ASX:PDI` | PDI Gold Limited | **-7.05%** | 4.09 AUD | 3,844,703 | $2.93B | none | Fell 7.05% to A$4.09 with no company release for 18 November - sold with the gold complex as spot gold broke below US$3,800/oz; Barrenjoey retained Overweight with a A$6.25 target (MarketIndex Evening Wrap, 18 Nov) |
| `ASX:TNE` | Technology One Limited | **-6.12%** | 33 AUD | 2,335,923 | $7.75B | OTC | Fell 6.12% to A$33.00, leading the ASX 200's information-technology sector down 2.31% and handing back Monday's 8.86% surge - no ASX announcement since Tuesday afternoon, with broker action in the session (Macquarie retained Outperform and raised its target to A$38.70 from A$30.50; UBS retained Neutral at A$35.80) and debt concerns cited (MarketIndex Evening Wrap, 18 Nov; ShareTrader, 18 Nov; Samso Market Update, 18 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:5838` | Rakuten Bank, Ltd. | **-15.16%** | 4489 JPY | 13,995,300 | $5.79B | none | Fell 15.16% to Y4,489, touching its daily lower limit at one point, after Rakuten Securities disclosed unauthorised access to a testing system that may have exposed login IDs and client codes for up to 11.25m accounts and personal information for 4.47m accounts - the biggest intraday drop since its 2023 listing - with the parent Rakuten Group sliding to a three-year low (Bloomberg, 18 Nov; The Edge Singapore, 18 Nov; Reuters via Fidelity, 18 Nov; Global Banking & Finance, 18 Nov) |
| `TSE:6027` | Bengo4.com, Inc. | **-8.71%** | 4090 JPY | 300,200 | $643M | none | Fell 8.71% to Y4,090, the second-largest decliner in the TSE Prime market, with no company release for 18 November - sold with the Japanese software and services complex in a session where 1,110 Prime names fell against 401 that rose (kabutan / minkabu, 18 Nov) |
| `TSE:4972` | Soken Chemical & Engineering Co., Ltd. | **+13.03%** | 5160 JPY | 281,500 | $474M | none | Rose 13.03% to Y5,160 after raising its FY2027/3 earnings forecast (kabutan / minkabu, 18 Nov) |
| `TSE:6490` | PILLAR Corporation | **+9.43%** | 9400 JPY | 455,900 | $1.27B | none | Rose 9.43% to Y9,400, the top gainer in the TSE Prime market, on buying in the AI and semiconductor complex after Nvidia's beat - its fluororesin fluid-control parts and semiconductor cleaning equipment sit in that chain - with the standing company news being the three-for-one stock split effective 1 January 2027 and a raised dividend forecast, announced on 12 November (kabutan / minkabu, 18 Nov; moomoo, 18 Nov; MarketScreener, 18 Nov) |
| `TSE:6855` | Japan Electronic Materials Corporation | **+7.98%** | 5820 JPY | 1,256,400 | $496M | none | Rose 7.98% to Y5,820 on speculation that an investor had lifted its stake further (kabutan / minkabu, 18 Nov) |
| `TSE:3923` | RAKUS Co., Ltd. | **-7.65%** | 1019.5 JPY | 3,612,500 | $2.45B | none | Fell 7.65% to Y1,019.50 with no company release for 18 November - sold with the Japanese software names, with services the weakest of the 33 TSE sectors and the TSE Growth 250 index down 9.98 points (kabutan / minkabu, 18 Nov; MarketScreener, 18 Nov) |
| `TSE:4478` | freee K.K. | **-7.50%** | 3270 JPY | 702,100 | $1.33B | OTC | Fell 7.50% to Y3,270 with no company release for 18 November - sold with the Japanese software complex (kabutan / minkabu, 18 Nov) |
| `TSE:4483` | JMDC Inc. | **-7.46%** | 3410 JPY | 423,000 | $1.51B | none | Fell 7.46% to Y3,410 with no company release for 18 November - sold with the Japanese software complex; JMDC was among the ten largest decliners in the TSE Prime market (kabutan / minkabu, 18 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TWSE:3665` | BizLink Holding Inc. | **+9.93%** | 1550 TWD | 4,513,379 | $8.54B | none | Rose 9.93% to NT$1,550 on record Q3 results - EPS of NT$21.93, an operating margin of 20.78% and a net margin of 15.4%, all company records (Zero One Investment Research daily brief, 18 Nov, citing Liberty Times) |
| `TWSE:3044` | Tripod Technology Corporation | **+9.93%** | 481.5 TWD | 6,248,545 | $6.98B | none | Rose 9.93% to NT$481.5, a day after falling nearly 9%, with domestic investment trusts reported to be buying at about 9.3 times earnings (Zero One daily brief, 18 Nov, citing cnYES) |
| `TWSE:3017` | Asia Vital Components Co., Ltd. | **+9.92%** | 2715 TWD | 5,829,610 | $29.42B | none | Rose 9.92% to NT$2,715, locked at the +10% limit, as a cooling-solution supplier in Nvidia's supply chain - one of three Taiwanese cooling makers that hit their daily limit-up by midday on Nvidia's results (Gate.com, 18 Nov; Taipei Times editorial, 18 Nov) |
| `TWSE:2449` | King Yuan Electronics Co., Ltd. | **+9.92%** | 194 TWD | 43,681,189 | $6.87B | none | Rose 9.92% to NT$194, locked at the +10% limit, with no company release found - bought with the AI supply chain after Nvidia's beat, in a session with 21 limit-up and 4 limit-down stocks (Economic Daily News via dealcanada, 18 Nov) |
| `TWSE:3661` | Alchip Technologies Ltd. | **+9.87%** | 3950 TWD | 4,837,126 | $9.37B | none | Rose 9.87% to NT$3,950, locked at the +10% limit, as Alchip - a designer of custom AI chips for cloud providers - is seen as among the Taiwanese names least exposed to a slowdown in Nvidia's own roadmap (Taipei Times editorial, 18 Nov; Economic Daily News, 18 Nov) |
| `TWSE:3189` | Kinsus Interconnect Technology Corp. | **+6.83%** | 579 TWD | 79,453,401 | $8.66B | none | Rose 6.83% to NT$579 after touching its +10% limit intraday, as Nvidia put more than US$1bn of cash into Kinsus to expand the ABF substrate capacity dedicated to Nvidia by more than 3.5x, with production from 2H27 (Zero One daily brief, 18 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:ARG` | Amerigo Resources Ltd | **-12.35%** | 6.53 CAD | 1,425,463 | $843M | OTC | Fell 12.35% to C$6.53 with no company release for 18 November - sold with the gold subgroup, which fell 6.8% as spot gold broke below US$3,800/oz at a one-year low (Reuters via ca.marketscreener, 18 Nov; Yahoo Finance TSX wrap, 18 Nov) |
| `TSX:ERO` | Ero Copper Corp. | **-11.34%** | 34.24 CAD | 870,510 | $2.82B | NYSE | Fell 11.34% to C$34.24 as LME three-month copper plunged 3.5-5.4% to a seven-month low near US$12,700/t on AI-capex doubts, a 19-month-high dollar and hawkish Fed expectations (Reuters via au.finance.yahoo, 18 Nov; Morningstar/Dow Jones, 18 Nov) |
| `TSX:TKO` | Trekor Metals Limited | **-10.03%** | 7.98 CAD | 1,720,512 | $2.28B | NYSE | Fell 10.03% to C$7.98 with no company release for 18 November - sold with the base-metals complex as copper hit its lowest level since April (Reuters, 18 Nov) |
| `TSX:LUN` | Lundin Mining Corporation | **-9.90%** | 24.65 CAD | 7,405,204 | $16.38B | ADR | Fell 9.90% to C$24.65 with no company release for 18 November - sold with the copper complex (Reuters via au.finance.yahoo, 18 Nov) |
| `TSX:HBM` | Hudbay Minerals Inc | **-8.16%** | 25.87 CAD | 3,093,042 | $8.75B | NYSE | Fell 8.16% to C$25.87 as copper stocks sold off with LME copper at a seven-month low (Reuters via au.finance.yahoo, 18 Nov) |
| `TSX:FM` | First Quantum Minerals Ltd. | **-7.99%** | 28.43 CAD | 5,237,498 | $18.03B | OTC | Fell 7.99% to C$28.43 with no company release for 18 November - sold with the base-metals complex (Reuters, 18 Nov) |
| `TSX:EDR` | Endeavour Silver Corp. | **-7.84%** | 9.4 CAD | 2,439,759 | $2.11B | none | Fell 7.84% to C$9.40 with no company release for 18 November - sold with the silver complex, silver losing 4.7% in a session when the TSX materials subgroup fell 5.7% to a four-month low (Reuters via ca.marketscreener, 18 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:DEZ` | DEUTZ AG | **-16.56%** | 7.66 EUR | 7,969,431 | $2.42B | OTC | Fell 16.56% to EUR7.66, the worst DAX constituent and its lowest level since November 2025, after US short-seller Ningi Research published a negative report on the EUR1.6bn acquisition of Flensburger Fahrzeugbau - it says a 45% minority holder in FFG Industries would take that share of future profits while Deutz carries the acquisition debt, and that management did not disclose everything; Deutz said it will examine the allegations carefully (dpa-AFX via finanzen.at, 18 Nov; Boersen-Zeitung, 18 Nov; n-tv, 18 Nov; Investing.com, 18 Nov) |
| `XETR:NEM` | Nemetschek SE | **-5.82%** | 57.4 EUR | 365,572 | $7.74B | ADR | Fell 5.82% to EUR57.40 with no company release for 18 November - sold with the German software and construction complex, the sectors that led the DAX's 1.19% fall (Investing.com, 18 Nov; ad-hoc-news.de, 18 Nov) |
| `XETR:NDA` | Aurubis AG | **-5.31%** | 126.6 EUR | 149,704 | $6.42B | ADR | Fell 5.31% to EUR126.60 as copper plunged about 5% - the DAX copper producer fell less than Freeport-McMoran (-7.3%) and Glencore (-6.1%) (Investing.com, 18 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:IPH` | Innate Pharma SA Class A | **-18.08%** | 0.988 EUR | 1,895,904 | $148M | ADR | Fell 18.08% to EUR0.988 after the initial Phase 1 data for IPH4502, its Nectin-4 antibody-drug conjugate, presented at ENA 2026 came in below expectations: the maximum tolerated dose of 3.6 mg/kg was limited by stomatitis, 43.4% of patients had grade 3+ treatment-emergent events, and the urothelial-cancer cohort - the drug's commercial target - produced only three partial responses at intermediate doses in patients who had all been treated with enfortumab vedotin; the Nasdaq line touched a 52-week low of US$1.01 (Investing.com, 18 Nov; Stock Titan, 18 Nov) |
| `EURONEXT:ETL` | Eutelsat Communications SA | **+7.65%** | 1.738 EUR | 1,331,242 | $2.09B | ADR | Rose 7.65% to EUR1.738, the best SBF 120 performer, after the satellite operator's refinancing (Ideal Investisseur, 18 Nov; Investing.com, 18 Nov) |
| `EURONEXT:ALO` | Alstom SA | **-7.15%** | 9.304 EUR | 7,745,227 | $5.10B | ADR | Fell 7.15% to EUR9.304, a five-year low, after the train maker said it is reviewing an equity and equity-like raise and asset sales to meet its EUR2bn debt-reduction target for September 2027; first-half sales rose 3% but it posted a EUR954m net loss (MarketWatch, 18 Nov; Investing.com, 18 Nov; Ideal Investisseur, 18 Nov) |
| `EURONEXT:VU` | VusionGroup S.A. | **-5.86%** | 142.9 EUR | 200,482 | $2.81B | none | Fell 5.86% to EUR142.90 with no company release for 18 November - sold with the CAC's consumer and technology names (Investing.com, 18 Nov) |

### eu-it

No name in Italy cleared the ±5% threshold with a sourced driver; the largest liquid mover is published under `## No catalyst`.

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `BME:REP` | Repsol SA | **-6.42%** | 28.71 EUR | 4,461,031 | $36.40B | ADR | Fell 6.42% to EUR28.71, the IBEX 35's worst performer, as Brent fell 2.46% to about US$90.9/bbl and WTI 3.64% to US$81.6 on a build in US crude and fuel inventories (FolioBots Newsroom, 18 Nov; Reuters via ca.marketscreener, 18 Nov; Investing.com, 18 Nov) |

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:PRX` | Prosus N.V. Class N | **-5.05%** | 32.525 EUR | 9,510,287 | $75.04B | ADR | Fell 5.05% to EUR32.525 after Tencent, in which Prosus holds a large stake, missed Q3 revenue consensus (CNY207.34bn against CNY210.77bn), saw operating profit fall 7% and posted negative free cash flow for a second quarter as AI capex rose roughly sixfold; Tencent is about 73% of Prosus's gross asset value (ANP via rd.nl, 18 Nov; iex.nl, 18 Nov; Investing.com, 18 Nov) |

### eu-be

No name in Belgium cleared the ±5% threshold with a sourced driver; the largest liquid mover is published under `## No catalyst`.

### eu-at

No name in Austria cleared the ±5% threshold with a sourced driver; the largest liquid mover is published under `## No catalyst`.

### eu-pt

No name in Portugal cleared the ±5% threshold with a sourced driver; the largest liquid mover is published under `## No catalyst`.

### eu-ie

No name in Ireland cleared the ±5% threshold with a sourced driver; the largest liquid mover is published under `## No catalyst`.

### eu-fi

No name in Finland cleared the ±5% threshold with a sourced driver; the largest liquid mover is published under `## No catalyst`.

### eu-dk

No name in Denmark cleared the ±5% threshold with a sourced driver; the largest liquid mover is published under `## No catalyst`.

### eu-gr

No name in Greece cleared the ±5% threshold with a sourced driver; the largest liquid mover is published under `## No catalyst`.

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a +100% or a -50% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:MMR | MEC Resources Ltd | **+100.00%** | 963,428 | below the $300M cap floor |
| ASX:BUY | Bounty Oil & Gas NL | **+60.00%** | 29,513,062 | below the $300M cap floor |
| ASX:HE8 | Helios Energy Ltd | **-50.00%** | 1,000,000 | below the $300M cap floor |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:130A | Veritas In Silico Inc. | **+26.67%** | 3,690,800 | below the $300M cap floor |
| TSE:9213 | Seyfert Ltd. | **+20.46%** | 111,800 | below the $300M cap floor |
| TSE:2388 | Wedge Holdings CO., LTD. | **+18.75%** | 12,058,800 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:6827 | MegaPro Biomedical Co., Ltd. | **+12.53%** | 1,597,603 | below the $200M cap floor |
| TPEX:6980 | Rapidtek Technologies Inc. | **+11.63%** | 122,269 | below the $200M cap floor |
| TPEX:7816 | RiTWIN Corporation | **-11.52%** | 120,338 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| CSE:NDAT | nDatalyze Corp | **+233.33%** | 154,500 | below the $200M cap floor |
| TSXV:LTV | LeoNovus Inc. | **+66.67%** | 126,441 | below the $200M cap floor |
| TSXV:EGR | EGR Exploration Ltd | **-60.00%** | 1,195,000 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| XETR:JDC | JDC Group AG | **-20.00%** | 153,855 | below the $300M cap floor |
| XETR:TPG0 | Platform Group SE & Co. KGaA | **-7.54%** | 1,272,906 | below the $300M cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALREE | REED | **-40.00%** | 2,313,610 | below the $100M cap floor |
| EURONEXT:ALNEV | Neovacs SA | **-20.00%** | 560,602 | below the $100M cap floor |
| EURONEXT:ALTAI | LightOn S.A. | **+18.32%** | 277,253 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:AGP | Altea Green Power S.p.A. | **-16.19%** | 352,780 | below the $100M cap floor |
| MIL:ENY | Energy SpA | **+11.68%** | 589,500 | below the $100M cap floor |

### eu-es

No name moved hard enough to clear the below-the-floor test in this region.

### eu-nl

No name moved hard enough to clear the below-the-floor test in this region.

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:OXUR | Oxurion NV | **+33.33%** | 3,475,558 | below the $100M cap floor |

### eu-at

No name moved hard enough to clear the below-the-floor test in this region.

### eu-pt

No name moved hard enough to clear the below-the-floor test in this region.

### eu-ie

No name moved hard enough to clear the below-the-floor test in this region.

### eu-fi

No name moved hard enough to clear the below-the-floor test in this region.

### eu-dk

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXCOP:UNLGRP | Unlimit Group A/S | **-20.59%** | 2,536,665 | below the $100M cap floor |
| OMXCOP:STENO | StenoCare A/S | **-5.96%** | 183,845 | below the $100M cap floor |

### eu-gr

No name moved hard enough to clear the below-the-floor test in this region.

## No catalyst

The names that moved with **no sourced driver**: no company release, no filing, no analyst action, and no sector or macro move behind them that could be sourced. Separate, so they do not dilute the mover table.

### au

No moved name without a sourced driver in this region.

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TSE:3491` | GA technologies Co., Ltd. | **-6.97%** | 1321 JPY | 592,500 | $366M | none | Fell 6.97% to Y1,321 with no driver found - no release for 18 November could be sourced and no sector move explains it |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TPEX:7415` | BE Epitaxy Semiconductor Technology Co Ltd | **-23.59%** | 230 TWD | 673,987 | $274M | none | Fell 23.59% to NT$230 - the largest move in Taiwan's published file - with no driver found; no release for 18 November could be sourced, and TPEX carries no daily price band, so the percentage is a real print rather than a limit price |
| `TWSE:2884` | E.SUN Financial Holding Co., Ltd. | **-9.65%** | 42.15 TWD | 96,808,265 | $25.08B | none | Fell 9.65% to NT$42.15, locked at its daily limit-down, with no driver found - no release for 18 November could be sourced |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TSXV:RML` | Rusoro Mining Ltd. | **+13.73%** | 1.16 CAD | 8,371,804 | $457M | OTC | Rose 13.73% to C$1.16 on 8.4m shares with no driver found - no release for 18 November could be sourced, and the move runs against the gold tape, so no driver is named here |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `XETR:AFX` | Carl Zeiss Meditec AG | **-6.22%** | 32.26 EUR | 238,584 | $3.38B | ADR | Fell 6.22% to EUR32.26, the worst DAX constituent, with no driver found - no release for 18 November could be sourced and the sector move does not reach it |
| `XETR:STM` | Stabilus SE | **-6.10%** | 12.92 EUR | 109,811 | $374M | OTC | Fell 6.10% to EUR12.92 with no driver found - no release for 18 November could be sourced |

### eu-fr

No moved name without a sourced driver in this region.

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `MIL:CY4` | CY4Gate SpA | **+5.68%** | 11.9 EUR | 241,611 | $292M | none | Rose 5.68% to EUR11.90 with no driver found - no release for 18 November could be sourced |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `BME:GGR` | Greening Group Global S.A. | **+8.66%** | 1.38 EUR | 88,492 | $112M | none | Rose 8.66% to EUR1.38 on 88,492 shares with no driver found - no release for 18 November could be sourced |

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ENVI` | Envipco Holding N.V. | **-6.08%** | 3.4 EUR | 113,569 | $266M | none | Fell 6.08% to EUR3.40 with no driver found - no release for 18 November could be sourced |

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:EVS` | EVS SA | **-8.80%** | 15.54 EUR | 210,229 | $251M | none | Fell 8.80% to EUR15.54 with no driver found - no release for 18 November could be sourced |
| `EURONEXT:ONTEX` | Ontex Group N.V. | **-8.02%** | 1.17 EUR | 818,197 | $113M | ADR | Fell 8.02% to EUR1.17 with no driver found - no release for 18 November could be sourced |

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `VIE:FACC` | FACC AG | **+3.91%** | 14.36 EUR | 70,441 | $696M | none | Rose 3.91% to EUR14.36 - the largest liquid mover on the ATX - with no driver found; no release for 18 November could be sourced |

### eu-pt

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:RENE` | Redes Energeticas Nacionais SA | **+3.15%** | 3.93 EUR | 1,707,943 | $2.78B | none | Rose 3.15% to EUR3.93 - the largest liquid mover on the PSI - with no driver found; no release for 18 November could be sourced |

### eu-ie

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:MIO` | Mincon Group PLC | **+4.05%** | 0.9 EUR | 196,528 | $202M | none | Rose 4.05% to EUR0.90 - the largest liquid mover on the ISEQ - with no driver found; no release for 18 November could be sourced |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `OMXHEX:IQMX` | IQM Quantum Computers Oyj Class A | **+4.86%** | 6.145 EUR | 145,120 | $1.23B | ADR | Rose 4.86% to EUR6.145 - the largest liquid mover on OMX Helsinki - with no driver found; no release for 18 November could be sourced |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `OMXCOP:GUBRA` | Gubra A/S | **-6.64%** | 269.8 DKK | 72,667 | $698M | none | Fell 6.64% to DKK269.80 - the largest liquid mover on OMX Copenhagen - with no driver found; no release for 18 November could be sourced |

### eu-gr

No moved name without a sourced driver in this region.

## Method, source health & caveats

### Method

- **Universe** - the TradingView per-country scanner, `types=["stock"]`, filtered on the issuer's own country (`filter: [{left: country, equal, <country>}]`). One pull per region; the completeness test is a SET test (the rows returned equal the pull's `totalCount`), and every region returned 100% of its names - **18,273 stock rows across the 16 countries**, every pull equal to its totalCount. The `type` filter matters: the same country endpoints also carry funds and structured products, which would have added rows that are not equities.
- **Venue collapse** - one line per symbol and share class, and the issuer's **primary** venue wins (au ASX; jp TSE, NAG, FSE, SAPSE; tw TWSE, TPEX; ca TSX, TSXV, CSE, NEO; eu-de XETR, FWB, LSX, LS, GETTEX, DUS, MUN, SWB, TRADEGATE, HAM, HAN; the single-venue regions keep their venue), then reported cap, then volume, then cap - the busiest venue is not the authoritative venue. A line whose implied prior close (`close / (1 + change/100)`) fails to reconcile with the **prior session's published close for the same symbol** by more than 5% is a stale venue print and is dropped; **1 line(s) were dropped** as off-official prints today (eu-fr 1), and a row whose close is unchanged is a carry-over, not a stale print.
- **Cap carrier** - the cap is resolved to the issuer's PRIMARY (common) line and converted ONCE with that line's currency; every other line of the issuer publishes that same USD figure in `cap_source_symbol`, and a group with no common line is excluded as `issuer_unresolved` rather than published with a borrowed cap. The floor is applied to the group, so a published preferred never points at a cap source that is not in the file. Canada shows the rule working: **125 rows are excluded as `issuer_unresolved`** because their issuer's common line sits on another venue, and their cap could not be carried without borrowing it.
- **Floors (USD)** - au $300M + volume ≥ 100,000; jp $300M; tw $200M; ca $200M; eu-de $300M + volume ≥ 50,000; eu-fr/it/es/nl/be/at $100M; eu-pt/gr $50M; eu-ie $200M; eu-fi/dk $100M. The floor is applied AFTER the conversion, never as a server-side screener filter (`market_cap_basic` on a per-country endpoint is in the listing currency).
- **FX** - open.er-api's base-USD table for 18 November 2026 (updated Wed, 18 Nov 2026 00:02:31 +0000: EUR 0.909215, JPY 159.393063, AUD 1.48436, CAD 1.429407, DKK 6.800425, TWD 32.967382). The table quotes **local units per 1 USD**, so the conversion is a division: `usd_cap = market_cap_basic / FX_per_USD[currency]`.
- **`us_listing`** - the America scanner, matched on the ISSUER (the US line's depositary-receipt wording is cut, the corporate-form words are normalised, and a US line whose name is SHORTER than the local line is a different issuer and does not match). A depositary receipt is published as `ADR` wherever it sits, an issuer's own US listing as `NYSE`/`NASDAQ`, and an OTC quotation as `OTC`.
- **Venue-official price rule** - where an exchange's own auction/close is published it is the price, and the row carries the conflict in `price_conflict`. **No row-level conflict was found today**: the scanner close stood for every published row and every `price_conflict` cell is empty. The German and French closes are corroborated to the cent by the exchange's own close-of-session table (DEUTZ EUR7.66, Carl Zeiss EUR32.26, Nemetschek EUR57.40, Aurubis EUR126.60, Alstom EUR9.304, VusionGroup EUR142.90, Eutelsat EUR1.738). The one venue-official price in this artifact is at index level - the ATHEX General's official close 2,584.51 (protothema, 18 Nov), which no vendor index covers.
- **CSV schema** - **18 columns** (`date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`), unchanged from the 2026-11-17 session. The numeric format is unchanged too (prices 4 decimals with trailing zeros stripped, `volume` and `market_cap` integers, `change_pct` and `pe_ratio` at full precision).
- **Files written** - `international-eod/2026-11-18/`: 16 region CSVs (`au.csv` … `eu-gr.csv`), `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView country scanner (16 regions) | scanner.tradingview.com/{au,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan, types=stock, filter country | ok | 18,273 stock rows across the 16 regions; every pull returned exactly its `totalCount` |
| TradingView America scanner (`us_listing` + ADR cap reading) | scanner.tradingview.com/america/scan, types=[stock,dr], sorted on a stable name sort | ok | 13,576 rows, union = totalCount |
| TradingView venue indices | scanner.tradingview.com/global/scan, 18 index tickers | ok | 17 index closes (16 regions + the STOXX 600); the ASX index is `SP:XJO` and the Nikkei `TVC:NI225` |
| ATHEX official close | protothema.gr, 18 Nov 2026 17:29 | ok | the General Index closed at 2,584.51, down 53.18 points or 2.02%, at the day's low - the ATHEX has no Yahoo symbol and no TradingView venue index |
| open.er-api | open.er-api.com/v6/latest/USD | ok | the Wed, 18 Nov 2026 00:02:31 +0000 table, 6 currencies |
| Prior published sessions (2026-11-17 … 2026-11-09) | karizaco/minimax-cloud-outputs, international-eod/<date>/<region>.csv | ok | 7 sessions per region, used for the stale-print reconciliation and the carry-over walk-back |
| Web search (catalyst research) | the web search tool, clustered by sector and by name | ok | every catalyst above carries a source and a date; names with no driver located are listed under `## No catalyst` |

### Caveats

- **The day's driver was the metals complex, and the AI beat did not stop it**: LME three-month copper fell 3.5-5.4% to a seven-month low near US$12,700/t on doubts about AI data-centre capital spending, a dollar at a 19-month high and Fed pricing near a 96% probability of a December hike, and spot gold broke below US$3,800/oz at a one-year low - on the year gold is heading for its worst performance since 2015. **Nvidia beat (Q3 revenue US$115.84bn, +103% y/y, 4Q guidance ~US$130bn with no China data-centre compute assumed) and still the metals sold off**; Nvidia's own market value had already fallen about US$1.9trn from early October. The TSX materials subgroup fell 5.7% to a four-month low, and the ASX's materials sector fell 1.08%.
- **The unit convention is the standing caveat**: `market_cap` is in **USD**, while `open`/`high`/`low`/`close` are in the **listing currency** - the `currency` column says which, and the cap is the only USD number in the row.
- **Taiwan's +9.9% prints are limit prices, not calculated moves** - TWSE and TPEX cap a daily move at ±10%, so a +9.92% close is a limit print and the market was shut at that price; the same applies to the ASX's and the Nordic boards' smaller bands. Taiwan's index was also volatile: it opened at 40,720.09, reached 40,938.20 and fell to 39,260.99 before closing at 40,194.91, with 21 limit-up and 4 limit-down stocks.
- **Carry-over rows** - 77 published rows carry a close from an earlier session (zero volume, or the scanner's stale change field beside an unchanged close): 33 last traded on 2026-11-17, 17 last traded on before 2026-11-09, 14 last traded on 2026-11-16, 7 last traded on 2026-11-13, 2 last traded on 2026-11-11, 2 last traded on 2026-11-10. They stay in the CSVs because the schema is fixed, each one is listed in `_carryover.json` with its last trade date, and they are excluded from every mover list.
- **The below-the-floor names cannot be reconciled against the archive** - a row that falls below the cap floor is not in yesterday's CSV either, so its prior close cannot be checked and its percentage is published as the source returned it. At the sub-cent prices in that table a ±50% or ±100% print is often a consolidation or a recapitalisation rather than a move; each row's `open` was checked against its implied prior close and none of them shows the open/close discontinuity a consolidation produces, but they are sub-$10m shells and are not signals.
- **Illiquid lines move in percent, not in money** - their percentages are real but their prices carry no information, and they are published for completeness rather than as signals.
- **No off-official venue rows today** - every region's primary-venue line reconciled with the prior session's close for the same instrument, so 1 line(s) were dropped as a stale venue print and the rest stood.
- **Sector rotation** (mean `change_pct` per sector over the written rows) is not a section of its own; the per-region read is carried here and uses the same rows:

  - `au` - the best sector was Technology Services (+1.40% mean over 15 names) and the worst Industrial Services (-2.33% over 16); the median written name closed -0.86%.
  - `jp` - the best sector was Electronic Technology (+1.05% mean over 90 names) and the worst Commercial Services (-1.83% over 58); the median written name closed -0.76%.
  - `tw` - the best sector was Commercial Services (+1.28% mean over 16 names) and the worst Utilities (-1.57% over 10); the median written name closed +0.00%.
  - `ca` - the best sector was Consumer Durables (+0.32% mean over 5 names) and the worst Non-Energy Minerals (-4.30% over 146); the median written name closed -0.38%.
  - `eu-de` - the best sector was Industrial Services (+0.42% mean over 1 names) and the worst Non-Energy Minerals (-2.75% over 4); the median written name closed -0.83%.
  - `eu-fr` - the best sector was Communications (+2.28% mean over 3 names) and the worst Non-Energy Minerals (-2.26% over 5); the median written name closed -0.45%.
  - `eu-it` - the best sector was Electronic Technology (+0.79% mean over 9 names) and the worst Energy Minerals (-2.38% over 2); the median written name closed -0.42%.
  - `eu-es` - the best sector was Electronic Technology (+4.11% mean over 2 names) and the worst Energy Minerals (-6.42% over 1); the median written name closed -0.39%.
  - `eu-nl` - the best sector was Electronic Technology (+0.70% mean over 2 names) and the worst Non-Energy Minerals (-2.70% over 1); the median written name closed -0.43%.
  - `eu-be` - the best sector was Technology Services (+2.25% mean over 2 names) and the worst Consumer Durables (-8.80% over 1); the median written name closed -0.17%.
  - `eu-at` - the best sector was Technology Services (+3.14% mean over 2 names) and the worst Distribution Services (-3.44% over 2); the median written name closed -0.51%.
  - `eu-pt` - the best sector was Utilities (+1.23% mean over 2 names) and the worst Retail Trade (-4.19% over 2); the median written name closed -0.86%.
  - `eu-ie` - the best sector was Producer Manufacturing (+4.05% mean over 1 names) and the worst Finance (-0.83% over 5); the median written name closed +0.25%.
  - `eu-fi` - the best sector was Electronic Technology (+1.70% mean over 8 names) and the worst Communications (-2.28% over 1); the median written name closed -0.60%.
  - `eu-dk` - the best sector was Consumer Non-Durables (+0.76% mean over 4 names) and the worst Commercial Services (-2.36% over 3); the median written name closed -0.44%.
  - `eu-gr` - the best sector was Commercial Services (+2.43% mean over 1 names) and the worst Energy Minerals (-3.39% over 2); the median written name closed -0.34%.

