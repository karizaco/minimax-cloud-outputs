# Cron #05 eod-international-daily — Thursday, 19 November 2026

## TL;DR

- **Europe, Canada and Taiwan sold off while Japan and Greece rose**: the TAIEX fell **4.40%** to 38,426.89, its seventh-largest one-day point decline on record, with 128 limit-downs in a rout of Nvidia's AI supply chain; the STOXX 600 lost 0.88%, the DAX 1.06%, the IBEX 35 0.97%, the TSX 1.59% and the ASX 200 1.04% (a sixth straight fall), while the Nikkei rose 419.93 points on Anthropic's IPO price and the ATHEX General gained 0.65%; across the 16 boards **4,304 names** were published.
- **The one consequential move was Taiwan's AI supply chain**: Nvidia fell 2.9% despite a revenue beat, US export controls on advanced chips took effect and TSMC paused some advanced China orders, and the PCB, substrate, memory and optical-testing complex was limit-locked - **Global Unichip -9.98%**, **Unimicron -9.97%**, **Tripod -9.97%**, **Taiwan Glass -9.97%**, **Elite Material -9.96%**; the reachable names outside Taiwan are **Evonik -16.21% (OTC)** after BASF walked away, **TELUS +13.72% (NYSE)** on Quebecor's US$31bn approach, **Soitec +12.01%**, **Shopify -5.22% (NASDAQ)**, **Evoltion Mining -7.33% (ADR)** and **Sonic Healthcare +6.28% (ADR)**.
- **The caveat that changes how to read it**: `market_cap` is in **USD** while `open`/`high`/`low`/`close` are in the **listing currency** (the `currency` column says which), Taiwan's -10% prints are **limit prices** rather than calculated moves, and Cromwell Property Group's **+422.86% is a 5-for-1 share consolidation, not a move** - it is kept in the CSV with the source's field and is excluded from every table below.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| au | 1 | 1548 | 1548 | 297 | $300M + vol >= 100,000 | 4 | 1228 | 18 | 1 | 0 | 1 | 0 |
| jp | 3 | 3897 | 3867 | 1368 | $300M | 3 | 2495 | 0 | 1 | 0 | 1 | 1 |
| tw | 2 | 2342 | 2342 | 849 | $200M | 57 | 1436 | 0 | 0 | 0 | 1 | 0 |
| ca | 3 | 4300 | 2696 | 610 | $200M | 61 | 1900 | 0 | 125 | 0 | 21 | 0 |
| eu-de | 1 | 4297 | 708 | 122 | $300M + vol >= 50,000 | 4 | 398 | 184 | 0 | 0 | 0 | 0 |
| eu-fr | 1 | 539 | 539 | 260 | $100M | 1 | 278 | 0 | 0 | 0 | 5 | 0 |
| eu-it | 1 | 377 | 377 | 178 | $100M | 2 | 197 | 0 | 0 | 0 | 2 | 0 |
| eu-es | 1 | 231 | 231 | 135 | $100M | 23 | 73 | 0 | 0 | 0 | 22 | 0 |
| eu-nl | 1 | 78 | 78 | 56 | $100M | 0 | 22 | 0 | 0 | 0 | 1 | 0 |
| eu-be | 1 | 101 | 101 | 76 | $100M | 1 | 24 | 0 | 0 | 0 | 0 | 0 |
| eu-at | 1 | 66 | 66 | 50 | $100M | 2 | 14 | 0 | 0 | 0 | 4 | 0 |
| eu-pt | 1 | 31 | 31 | 27 | $50M | 0 | 4 | 0 | 0 | 0 | 2 | 0 |
| eu-ie | 1 | 20 | 20 | 17 | $200M | 0 | 3 | 0 | 0 | 0 | 1 | 0 |
| eu-fi | 1 | 189 | 189 | 101 | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| eu-dk | 1 | 133 | 133 | 75 | $100M | 1 | 57 | 0 | 0 | 0 | 1 | 0 |
| eu-gr | 1 | 128 | 128 | 83 | $50M | 0 | 45 | 0 | 0 | 0 | 0 | 0 |
| **total** | | 18277 | 13054 | **4304** | | 163 | 8258 | 202 | 127 | 0 | 62 | 1 |

The exclusion counts are the per-reason counts in `_excluded.json`, not estimates. The reconciliation identity `unique_instruments == written + sum(excluded)` holds for every region.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 8,730.40 | -91.40 / -1.04% | 2026-11-19 | TradingView SP:XJO; NewsWire via news.com.au, 19 Nov, reports 8,730.40, down 91.40 points - a sixth straight fall, with the materials sector down 3.80% |
| jp | Nikkei 225 | 59,443.99 | +419.93 / +0.71% | 2026-11-19 | TradingView TVC:NI225 venue index read 59,443.99; minkabu, kabutan and gentosha-go, 19 Nov, report the official close at 59,444.21, up 419.93 points - a 0.22-point difference against the vendor index |
| jp | TOPIX | 3,822.47 | -1.53 / -0.04% | 2026-11-19 | TradingView TSE:TOPIX venue index; jiji and kabutan, 19 Nov, report 3,822.47, down 1.53 points - a fourth straight fall |
| tw | TAIEX | 38,426.89 | -1,768.02 / -4.40% | 2026-11-19 | TradingView TWSE:IX0001; CNA via Focus Taiwan and Taiwan News, 19 Nov, report the same close - the seventh-largest one-day point decline on record, below the 240-day moving average |
| ca | S&P/TSX Composite | 34,028.73 | -549.32 / -1.59% | 2026-11-19 | TradingView TSX:TSX venue index; Reuters, 19 Nov, had it at 34,334.01 (-0.71%) at 10:28 ET and Baystreet at 34,268.55 intraday - a more-than-four-month low |
| eu-de | DAX (Xetra) | 25,463.81 | -306.43 / -1.06% | 2026-11-19 | TradingView XETR:DAX venue index; n-tv and elfolio, 19 Nov, both report 25,463.81 (-1.06%) - a fifth straight fall and the session low |
| eu-fr | CAC 40 | 8,080.74 | -66.09 / -0.81% | 2026-11-19 | TradingView EURONEXT:PX1; elfolio, 19 Nov, reports 8,080.74 (-0.81%) |
| eu-it | FTSE MIB | 49,941.25 | -232.42 / -0.46% | 2026-11-19 | TradingView FTSE:FTSEMIB venue index; elfolio, 19 Nov, reports 49,941.25 (-0.46%) |
| eu-es | IBEX 35 | 19,186.20 | -187.10 / -0.97% | 2026-11-19 | TradingView BME:IBC; elfolio, 19 Nov, reports 19,186.20 (-0.97%) - a fourth straight fall below 19,200 |
| eu-nl | AEX | 1,091.94 | -6.79 / -0.62% | 2026-11-19 | TradingView EURONEXT:AEX venue index; the Dow Jones close table, 19 Nov, agrees on the -0.6% change, but its level column carries the previous session's close |
| eu-be | BEL 20 | 5,885.51 | -67.00 / -1.13% | 2026-11-19 | TradingView EURONEXT:BEL20 venue index; the Dow Jones close table, 19 Nov, agrees on the -1.1% change, but its level column carries the previous session's close |
| eu-at | ATX | 6,379.10 | -15.62 / -0.24% | 2026-11-19 | TradingView VIE:ATX venue index; the Dow Jones close table, 19 Nov, agrees on the -0.2% change, but its level column carries the previous session's close |
| eu-pt | PSI 20 | 9,410.29 | -89.36 / -0.94% | 2026-11-19 | TradingView EURONEXT:PSI20 venue index; the Dow Jones close table, 19 Nov, agrees on the -0.9% change, but its level column carries the previous session's close |
| eu-ie | ISEQ | 14,696.20 | -81.40 / -0.55% | 2026-11-19 | TradingView EURONEXT:ISEQ venue index; the Dow Jones close table, 19 Nov, agrees on the -0.6% change, but its level column carries the previous session's close |
| eu-fi | OMX Helsinki 25 | 6,090.06 | -18.53 / -0.30% | 2026-11-19 | TradingView OMXHEX:OMXH25 venue index; the Dow Jones close table, 19 Nov, agrees on the -0.3% change, but its level column carries the previous session's close |
| eu-dk | OMX Copenhagen 20 | 1,614.03 | -23.21 / -1.42% | 2026-11-19 | TradingView OMXCOP:OMXC20 venue index; the Dow Jones close table, 19 Nov, agrees on the -1.4% change, but its level column carries the previous session's close |
| eu-gr | ATHEX General | 2,601.23 | +16.72 / +0.65% | 2026-11-19 | capital.gr, insider.gr, euro2day and pelop.gr, 19 Nov 17:19, report the General Index closing at 2,601.23, up 16.72 points or 0.65%, in a 2,592.16-2,619.82 range, with the bank index up 1.53%; the ATHEX has no Yahoo symbol and no TradingView venue index |
| *context* | STOXX 600 | 638.41 | -5.64 / -0.88% | 2026-11-19 | TradingView STOXX:SXXP; elfolio, 19 Nov, reports 638.41 (-0.88%) |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 296 | -0.82% | 83 / 196 / 17 | -10.39% | +422.86% |
| jp | 1367 | -0.24% | 570 / 758 / 39 | -9.53% | +8.92% |
| tw | 848 | -5.57% | 40 / 789 / 19 | -17.39% | +9.01% |
| ca | 589 | -1.14% | 77 / 483 / 29 | -29.26% | +20.88% |
| eu-de | 122 | -0.95% | 32 / 89 / 1 | -16.21% | +4.57% |
| eu-fr | 255 | -0.61% | 63 / 154 / 38 | -9.41% | +12.01% |
| eu-it | 176 | -0.45% | 57 / 105 / 14 | -15.01% | +5.84% |
| eu-es | 113 | -0.79% | 26 / 80 / 7 | -9.39% | +6.82% |
| eu-nl | 55 | -1.05% | 14 / 41 / 0 | -3.59% | +2.87% |
| eu-be | 76 | -0.80% | 15 / 53 / 8 | -3.45% | +3.53% |
| eu-at | 46 | -0.54% | 12 / 27 / 7 | -8.91% | +4.95% |
| eu-pt | 25 | -0.77% | 4 / 16 / 5 | -2.16% | +2.49% |
| eu-ie | 16 | -0.50% | 5 / 9 / 2 | -2.92% | +2.22% |
| eu-fi | 101 | -0.51% | 31 / 66 / 4 | -7.37% | +7.55% |
| eu-dk | 74 | -0.66% | 17 / 55 / 2 | -8.38% | +5.61% |
| eu-gr | 83 | +0.00% | 32 / 30 / 21 | -3.00% | +13.49% |

The breadth table is computed from the written rows, so an index move and the typical name can disagree. On this session they did, in both directions: the TAIEX fell 4.40% while the median published Taiwanese name fell 9.59% (the market was limit-locked in the AI supply chain), and the ATHEX General rose 0.65% while the median published Greek name fell 2.70%.

## Top movers

Liquid names (volume ≥ 100,000, market cap at or above the region's floor) whose move cleared ±5%, with the driver that was actually sourced, largest absolute move first within the region. A row with no sourced driver is not here - it is under `## No catalyst`. Each region also publishes its single biggest liquid mover even when it did not clear ±5%, so no region is silent; a region with no name at all says so instead of publishing an unsourced row.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:EMR` | Emerald Resources NL | **-8.17%** | 6.07 AUD | 5,176,843 | $2.95B | none | Fell 8.17% to A$6.07 with no company release for 19 November - it was sold with the resources complex as the ASX materials sector lost 3.80%, copper plunged as much as 5% on AI-capex doubts and spot gold fell 3.2% to a 14-month low near US$3,725/oz, with weak Australian jobs data reviving RBA rate-hike and recession fears (NewsWire via news.com.au, 19 Nov; MarketIndex Evening Wrap, 19 Nov) |
| `ASX:PDN` | Paladin Energy Ltd | **-8.16%** | 6.19 AUD | 12,742,429 | $2.03B | OTC | Fell 8.16% to A$6.19 with no company release for 19 November - sold with the gold complex as the precious metal fell 3.2% to a 14-month low near US$3,725/oz on US-dollar strength (MarketIndex Evening Wrap, 19 Nov; Veye, 19 Nov) |
| `ASX:EVN` | Evolution Mining Limited | **-7.33%** | 10.88 AUD | 14,589,829 | $16.27B | ADR | Fell 7.33% to A$10.88 as gold fell more than 3% to a 14-month low, with the materials sector down 3.80% and the ASX 200 in a sixth straight falling session (NewsWire via news.com.au, 19 Nov; Veye, 19 Nov) |
| `ASX:RSG` | Resolute Mining Limited | **-7.14%** | 1.04 AUD | 9,027,690 | $1.61B | ADR | Fell 7.14% to A$1.04 with no company release for 19 November - sold with the gold complex as spot gold broke below US$3,800/oz and the All Ordinaries Gold index swung from an early 1.7% gain to a 2.79% loss (MarketIndex Evening Wrap, 19 Nov; Veye, 19 Nov) |
| `ASX:GGP` | Greatland Resources Limited | **-6.33%** | 9.02 AUD | 1,688,867 | $4.16B | none | Fell 6.33% to A$9.02 with no company release for 19 November - sold with the base-metals complex as copper fell as much as 5% on AI-linked de-risking (MarketIndex Evening Wrap, 19 Nov) |
| `ASX:MAH` | Macmahon Holdings Limited | **-6.32%** | 0.815 AUD | 13,033,606 | $1.23B | none | Fell 6.32% to A$0.815 with no company release for 19 November - sold with the mining sector, which lost 3.80% as copper and gold fell together (NewsWire via news.com.au, 19 Nov; MarketIndex Evening Wrap, 19 Nov) |
| `ASX:RMS` | Ramelius Resources Limited | **-6.32%** | 3.26 AUD | 10,142,467 | $4.40B | OTC | Fell 6.32% to A$3.26 with no company release for 19 November - sold with the gold complex on the 14-month low in spot gold (MarketIndex Evening Wrap, 19 Nov) |
| `ASX:SHL` | Sonic Healthcare Limited | **+6.28%** | 21.33 AUD | 2,547,565 | $6.66B | ADR | Rose 6.28% to A$21.33, defying a sinking ASX 200, after its 2026 AGM - all resolutions carried, the FY2027 EBITDA guidance was maintained unchanged at A$1.95-2.03bn and the CEO reaffirmed it; FY2026 revenue was A$10.87bn (+13%), underlying EBITDA A$1.93bn (+11%), underlying net profit A$621m (+17%) and the final dividend 63c (Sonic Healthcare ASX announcement, 19 Nov; IBTimes, 19 Nov; AFR, 19 Nov) |
| `ASX:PYC` | PYC Therapeutics Limited | **-6.05%** | 1.63 AUD | 2,800,429 | $1.15B | OTC | Fell 6.05% to A$1.63 with no company release for 19 November - sold with the broader market (MarketIndex Evening Wrap, 19 Nov) |
| `ASX:S32` | South32 Ltd. | **-5.87%** | 4.01 AUD | 21,610,085 | $12.78B | ADR | Fell 5.87% to A$4.01 with no company release for 19 November - sold with the base-metals complex as copper fell as much as 5% on AI jitters and iron ore fell with it (NewsWire via news.com.au, 19 Nov) |
| `ASX:ALK` | Alkane Resources Ltd | **-5.87%** | 1.605 AUD | 3,508,966 | $1.57B | OTC | Fell 5.87% to A$1.605 with no company release for 19 November - sold with the energy sector, down 1.5% after US crude inventories surprised on the upside (MarketIndex Evening Wrap, 19 Nov) |
| `ASX:WGX` | Westgold Resources Ltd | **-5.84%** | 5.16 AUD | 5,787,232 | $3.46B | OTC | Fell 5.84% to A$5.16 with no company release for 19 November - sold with the gold complex at the 14-month low in spot gold (MarketIndex Evening Wrap, 19 Nov) |
| `ASX:OBM` | Ora Banda Mining Ltd. | **-5.73%** | 1.235 AUD | 16,849,440 | $1.71B | OTC | Fell 5.73% to A$1.235 with no company release for 19 November - sold with the gold complex (MarketIndex Evening Wrap, 19 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:1515` | Nittetsu Mining Co., Ltd. | **-8.97%** | 2305 JPY | 792,400 | $1.27B | none | Fell 8.97% to Y2,305, the worst decliner in the TSE Prime market (-227 yen), with no company release for 19 November - it was sold with the mining and non-ferrous-metals sectors, the weakest of the 33 TSE sectors, as metals sold off globally (kabutan / minkabu, 19 Nov) |
| `TSE:6315` | Towa Corporation | **+8.92%** | 2394 JPY | 7,560,700 | $1.04B | OTC | Rose 8.92% to Y2,394, the number-one TSE Prime gainer (+196 yen), bought with the AI and semiconductor complex after Anthropic's IPO price was set above its range - the same bid that lifted SoftBank Group and Tokyo Electron (kabutan / minkabu, 19 Nov; gentosha-go, 19 Nov) |
| `TSE:6787` | Meiko Electronics Co., Ltd. | **+6.76%** | 8370 JPY | 2,544,400 | $2.58B | none | Rose 6.76% to Y8,370, the third-largest TSE Prime gainer (+530 yen), bought with the semiconductor-equipment complex in the Anthropic-IPO bid (kabutan / minkabu, 19 Nov; gentosha-go, 19 Nov) |
| `TSE:4588` | Oncolys BioPharma, Inc. | **-6.23%** | 7070 JPY | 1,460,500 | $1.40B | none | Fell 6.23% to Y7,070 with no company release for 19 November (kabutan / minkabu, 19 Nov) |
| `TSE:5016` | JX Advanced Metals Corporation | **-6.20%** | 2012.5 JPY | 33,995,700 | $12.76B | ADR | Fell 6.20% to Y2,012.5 - JX Advanced Metals was among the largest TSE Prime decliners, sold with the non-ferrous-metals sector as metals prices fell (kabutan / minkabu, 19 Nov) |
| `TSE:4680` | ROUND ONE Corporation | **+5.83%** | 1469.5 JPY | 2,348,500 | $2.52B | OTC | Rose 5.83% to Y1,469.5 - ROUND ONE was among the ten biggest TSE Prime gainers (kabutan / minkabu, 19 Nov) |
| `TSE:4704` | Trend Micro Incorporated | **+5.72%** | 7506 JPY | 2,055,100 | $5.85B | ADR | Rose 5.72% to Y7,506 - Trend Micro was among the ten biggest TSE Prime gainers, on continued inflows into the cybersecurity sector (kabutan / minkabu, 19 Nov) |
| `TSE:4980` | Dexerials Corp. | **+5.48%** | 2031 JPY | 4,762,400 | $2.07B | none | Rose 5.48% to Y2,031 - Dexerials was among the ten biggest TSE Prime gainers (kabutan / minkabu, 19 Nov) |
| `TSE:8022` | Mizuno Corporation | **+5.27%** | 4295 JPY | 816,300 | $2.02B | none | Rose 5.27% to Y4,295 - Mizuno was among the ten biggest TSE Prime gainers (kabutan / minkabu, 19 Nov) |
| `TSE:5713` | Sumitomo Metal Mining Co., Ltd. | **-5.24%** | 6055 JPY | 5,124,600 | $10.93B | ADR | Fell 5.24% to Y6,055 - Sumitomo Metal Mining was among the ten biggest TSE Prime decliners, sold with the mining sector (kabutan / minkabu, 19 Nov) |
| `TSE:6946` | Nippon Avionics Co., Ltd. | **-9.53%** | 3940 JPY | 764,600 | $458M | none | Fell 9.53% to Y3,940 - the largest move in the Japanese file - with no company release found for 19 November and no sector move that reaches it (kabutan / minkabu, 19 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TPEX:3105` | Win Semiconductors Corp. | **-10.00%** | 423 TWD | 27,837,084 | $6.02B | none | Fell 10.00% to NT$423, locked at its daily lower limit, with no company release for 19 November - Win Semiconductors was among the limit-down semiconductor names (CNA via Focus Taiwan, 19 Nov; gate.com, 19 Nov) |
| `TPEX:5274` | ASPEED Technology, Inc. | **-10.00%** | 8730 TWD | 330,602 | $12.21B | none | Fell 10.00% to NT$8,730, locked at its daily lower limit - Aspeed, Taiwan's highest-priced stock, was one of 20 limit-down names priced above NT$1,000, sold with the AI supply chain after Nvidia fell 2.9% despite its strong results (CNA via Focus Taiwan, 19 Nov; Taiwan News, 19 Nov) |
| `TWSE:3406` | GeniuS Electronic Optical Co., Ltd. | **-10.00%** | 720 TWD | 3,488,396 | $2.87B | none | Fell 10.00% to NT$720, locked at its daily lower limit, with no company release for 19 November - Genius Electronic Optical was among the electronics names limit-locked (CNA via Focus Taiwan, 19 Nov) |
| `TWSE:3443` | Global Unichip Corp. | **-9.98%** | 6000 TWD | 1,229,636 | $27.09B | none | Fell 9.98% to NT$6,000, hitting its daily lower limit, with no company release for 19 November - Global Unichip was named among the semiconductor names hit by the rout (Investing.com via sg.finance.yahoo, 19 Nov) |
| `TWSE:3037` | Unimicron Technology Corp. | **-9.97%** | 596 TWD | 19,543,015 | $32.36B | none | Fell 9.97% to NT$596, locked at its daily limit-down - Unimicron, a PCB substrate maker, was one of the names hit as the PCB sector sold off wholesale (Taiwan News, 19 Nov) |
| `TWSE:1802` | Taiwan Glass Industry Corp. | **-9.97%** | 58.7 TWD | 121,128,413 | $5.75B | none | Fell 9.97% to NT$58.7, locked at its daily limit-down - Taiwan Glass was among the fiberglass and copper-clad-laminate suppliers hit at the upstream end of the PCB chain (Taiwan News, 19 Nov) |
| `TWSE:3044` | Tripod Technology Corporation | **-9.97%** | 433.5 TWD | 8,319,278 | $7.68B | none | Fell 9.97% to NT$433.5 - Tripod, a PCB maker, fell more than 8% and the PCB names hit their daily lower limits (Investing.com via sg.finance.yahoo, 19 Nov; Taiwan News, 19 Nov) |
| `TPEX:3363` | FOCI Fiber Optic Communications, Inc. | **-9.97%** | 284.5 TWD | 2,632,571 | $1.09B | none | Fell 9.97% to NT$284.5 with no company release for 19 November - sold with the optical-communication and semiconductor-testing complex (CNA via Focus Taiwan, 19 Nov) |
| `TWSE:2383` | Elite Material Co., Ltd. | **-9.96%** | 3120 TWD | 3,393,302 | $37.65B | none | Fell 9.96% to NT$3,120, locked at its daily limit-down - Elite Material was among the copper-clad-laminate suppliers hit at the upstream end of the PCB chain (Taiwan News, 19 Nov) |
| `TWSE:2492` | Walsin Technology Corporation | **-9.96%** | 208 TWD | 25,399,448 | $3.39B | none | Fell 9.96% to NT$208, locked at its daily limit-down - Walsin Technology was among the passive-component makers hit (Taiwan News, 19 Nov) |
| `TWSE:3653` | Jentech Precision Industrial Co., Ltd | **-9.96%** | 4115 TWD | 2,836,596 | $20.24B | none | Fell 9.96% to NT$4,115 with no company release for 19 November - sold with the AI supply chain (CNA via Focus Taiwan, 19 Nov) |
| `TWSE:6442` | EZconn Corp. | **-9.95%** | 959 TWD | 2,535,724 | $2.55B | none | Fell 9.95% to NT$959 - EZconn, an optical-communication products maker, fell below the NT$1,000 threshold (CNA via Focus Taiwan, 19 Nov) |
| `TPEX:3163` | Browave Corporation | **-9.95%** | 380 TWD | 1,449,732 | $1.21B | none | Fell 9.95% to NT$380 with no company release for 19 November - Browave was named among the optical and semiconductor-testing stocks that plunged (Investing.com via sg.finance.yahoo, 19 Nov) |
| `TPEX:6510` | Chunghwa Precision Test Tech Co., Ltd. | **-9.95%** | 2625 TWD | 321,440 | $2.91B | none | Fell 9.95% to NT$2,625 with no company release for 19 November (CNA via Focus Taiwan, 19 Nov) |

116 further liquid name(s) cleared ±5% in this region and are in `tw.csv`.

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:SEA` | Seabridge Gold Inc | **-29.26%** | 25.92 CAD | 926,052 | $2.76B | NYSE | Fell 29.26% to C$25.92 - Seabridge Gold tumbled as much as 27.9% to its lowest level since November 2025, with no company-specific release for 19 November; it was sold with the gold complex as the metal fell to a 14-month low on US-dollar strength (Reuters, 19 Nov; Baystreet, 19 Nov) |
| `TSX:T` | TELUS Corporation | **+13.72%** | 15.5 CAD | 26,606,119 | $15.15B | NYSE | Rose 13.72% to C$15.50 - TELUS was the TSX's top gainer, up 12.4% intraday, on Quebecor's proposed combination with the telecom operator, reported as a US$31bn deal (Reuters, 19 Nov) |
| `TSX:QBR.B` | Quebecor Inc. Class B | **+7.53%** | 58.4 CAD | 4,329,904 | $8.60B | OTC | Rose 7.53% to C$58.40 - the other side of Quebecor's proposed combination with TELUS, reported as a US$31bn deal (Reuters, 19 Nov) |
| `TSX:EDR` | Endeavour Silver Corp. | **-7.13%** | 8.73 CAD | 1,376,144 | $1.94B | NYSE | Fell 7.13% to C$8.73 with no company release for 19 November - sold with the gold complex as the precious metal slipped on US-dollar strength (Reuters, 19 Nov) |
| `TSX:MAU` | Montage Gold Corp. | **-7.08%** | 13.65 CAD | 1,409,417 | $4.18B | OTC | Fell 7.08% to C$13.65 with no company release for 19 November - sold with the gold complex (Reuters, 19 Nov) |
| `TSX:SGD` | Snowline Gold Corp. | **-6.81%** | 11.5 CAD | 329,193 | $1.62B | OTC | Fell 6.81% to C$11.50 with no company release for 19 November - sold with the gold complex (Reuters, 19 Nov) |
| `TSX:GMIN` | G Mining Ventures Corp | **-6.63%** | 39.55 CAD | 959,409 | $8.76B | OTC | Fell 6.63% to C$39.55 with no company release for 19 November - sold with the gold complex (Reuters, 19 Nov) |
| `TSX:AYA` | Aya Gold & Silver Inc. | **-6.51%** | 27.12 CAD | 1,102,019 | $2.92B | NASDAQ | Fell 6.51% to C$27.12 with no company release for 19 November - sold with the gold complex (Reuters, 19 Nov) |
| `TSX:ABRA` | AbraSilver Resource Corp. | **-6.28%** | 9.25 CAD | 2,187,648 | $1.11B | OTC | Fell 6.28% to C$9.25 with no company release for 19 November - sold with the gold complex (Reuters, 19 Nov) |
| `TSX:AAUC` | Allied Gold Corporation | **-5.72%** | 26.7 CAD | 707,700 | $2.78B | NYSE | Fell 5.72% to C$26.70 - Allied Gold was among the TSX's largest decliners intraday, shedding more than 3% as gold slipped on US-dollar strength (Reuters, 19 Nov) |
| `TSX:SXGC` | Southern Cross Gold Consolidated Ltd. | **-5.34%** | 6.74 CAD | 676,717 | $1.34B | OTC | Fell 5.34% to C$6.74 with no company release for 19 November - sold with the gold complex (Reuters, 19 Nov) |
| `TSX:SHOP` | Shopify, Inc. Class A | **-5.22%** | 189.35 CAD | 1,564,899 | $179.46B | NASDAQ | Fell 5.22% to C$189.35 with no company release for 19 November - sold with the technology complex as investors awaited Anthropic's market debut (Reuters, 19 Nov) |
| `TSX:ELD` | Eldorado Gold Corporation | **-5.19%** | 38.55 CAD | 648,692 | $7.42B | NYSE | Fell 5.19% to C$38.55 with no company release for 19 November - sold with the gold complex (Reuters, 19 Nov) |
| `TSX:ORE` | Orezone Gold Corporation | **-5.02%** | 2.08 CAD | 1,371,808 | $1.10B | OTC | Fell 5.02% to C$2.08 with no company release for 19 November - sold with the gold complex (Reuters, 19 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:EVK` | Evonik Industries AG | **-16.21%** | 18.25 EUR | 4,933,683 | $11.14B | ADR | Fell 16.21% to EUR18.25 - BASF abandoned its takeover approach after Evonik rejected two non-binding offers (around EUR22.15 and then EUR24.00 a share, valuing Evonik above EUR11bn); the shares fell as much as 23% intraday to a four-month low and closed around 16% lower, their biggest one-day fall on record, while BASF gave back about 1% (dpa-AFX, 19 Nov; Bloomberg via de.finance.yahoo, 19 Nov; onvista, 19 Nov; n-tv, 19 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:SOI` | Soitec SA | **+12.01%** | 109.25 EUR | 804,416 | $3.83B | none | Rose 12.01% to EUR109.25, the best SBF 120 performer, after its H1 FY2027 results - revenue EUR316.7m (+37%), gross margin up 8.2 points to 33.3% and a EUR45m net loss - with the FY2026-27 outlook extended to EUR829.2m on AI demand, alongside two target raises (J.P. Morgan to EUR195, CIC to EUR200) (Il Sole 24 Ore Radiocor, 19 Nov; Ideal Investisseur, 19 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:OROX` | Gens Aurea S.p.A. | **-15.01%** | 9.4 EUR | 456,077 | $1.23B | none | Fell 15.01% to EUR9.40 - the largest move on the Milan board - with no driver found; no release for 19 November could be sourced (Reuters via Il Sole 24 Ore Radiocor, 19 Nov) |
| `MIL:MFEA` | MFE-MediaForEurope NV Class A | **-5.34%** | 1.916 EUR | 5,971,854 | $1.67B | none | Fell 5.34% to EUR1.916 with no company release for 19 November - sold with the European media complex (Il Sole 24 Ore Radiocor, 19 Nov) |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `BME:GRE` | Grenergy Renovables S.A | **-9.39%** | 55 EUR | 492,750 | $1.82B | none | Fell 9.39% to EUR55.00, breaking its annual low of EUR60.60, with no company-specific release for 19 November - it was sold with the Spanish renewable complex, where Acciona Energia lost 3.25% and Acciona 2.94% (Dow Jones Newswires via es.marketscreener, 19 Nov; elfolio, 19 Nov) |
| `BME:SLR` | Solaria Energia y Medio Ambiente, S.A. | **-5.41%** | 14.16 EUR | 3,904,831 | $2.18B | none | Fell 5.41% to EUR14.16, the IBEX 35's worst performer, after its nine-month accounts and its 2029 roadmap at a Capital Markets Day in London - EBITDA of EUR540-560m targeted for 2029, EUR1.2bn of capex for 2027-29 and a buyback taking treasury shares to 10%; nine-month net profit was EUR177.94m (+26%) on record production of 3,143GWh (+56%), and the shares traded about 7% lower intraday (Democrata, 19 Nov; Press Digital, 19 Nov; elfolio, 19 Nov) |

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ADYEN` | Adyen NV | **-3.59%** | 806.4 EUR | 181,455 | $29.09B | ADR | Fell 3.59% to EUR806.40 - the largest liquid mover on the AEX - with no driver found; no release for 19 November could be sourced (Dow Jones Newswires close table, 19 Nov) |

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:IMMO` | Immobel SA | **+3.53%** | 17.6 EUR | 4,246 | $191M | none | Rose 3.53% to EUR17.60 - the largest move on the BEL 20 - with no driver found; no release for 19 November could be sourced (Dow Jones Newswires close table, 19 Nov) |

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:1AST` | Asta Energy Solutions AG | **-8.91%** | 41.9 EUR | 4,953 | $702M | OTC | Fell 8.91% to EUR41.90 - the largest move on the ATX - with no driver found; no release for 19 November could be sourced (Dow Jones Newswires close table, 19 Nov) |

### eu-pt

No liquid name cleared ±5% with a sourced driver in this region.

### eu-ie

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:OIZ` | Origin Enterprises PLC | **-2.92%** | 4.155 EUR | 158,888 | $507M | none | Fell 2.92% to EUR4.155 - the largest liquid mover on the ISEQ - with no driver found; no release for 19 November could be sourced (Dow Jones Newswires close table, 19 Nov) |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:IQMX` | IQM Quantum Computers Oyj Class A | **+6.75%** | 6.56 EUR | 117,314 | $1.29B | ADR | Rose 6.75% to EUR6.56 - the largest liquid mover on OMX Helsinki - with no driver found; no release for 19 November could be sourced (Dow Jones Newswires close table, 19 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:BETCO_DKK` | Better Collective A/S | **-8.38%** | 38.8 DKK | 263,633 | $367M | none | Fell 8.38% to DKK38.80 - the largest move on OMX Copenhagen - with no driver found; no release for 19 November could be sourced (Dow Jones Newswires close table, 19 Nov) |

### eu-gr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ATHEX:EVROF` | Evropharma Milk Industry Anonyme Industrial & Commercial Company | **+13.49%** | 4.88 EUR | 24,576 | $65M | none | Rose 13.49% to EUR4.88 - the largest move on the ATHEX - with no driver found; no release for 19 November could be sourced (insider.gr, 19 Nov) |

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a +100% or a -50% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:MMR | MEC Resources Ltd | **+100.00%** | 963,428 | below the $300M cap floor |
| ASX:ENV | Enova Mining Limited | **+100.00%** | 782,350 | below the $300M cap floor |
| ASX:ACW | Actinogen Medical Limited | **-82.22%** | 213,989,929 | below the $300M cap floor |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:4586 | Medrx Co., Ltd. | **+63.83%** | 24,380,400 | below the $300M cap floor |
| TSE:3624 | Axel Mark Inc. | **+39.00%** | 22,323,200 | below the $300M cap floor |
| TSE:130A | Veritas In Silico Inc. | **+28.07%** | 2,172,100 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:7929 | CerTone Heat Solution Co Ltd | **-20.00%** | 127,518 | below the $200M cap floor |
| TPEX:6977 | United Purification Technology Co Ltd | **-17.25%** | 275,605 | below the $200M cap floor |
| TPEX:7707 | CMSC, Inc. | **-15.23%** | 153,554 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSXV:WAV.H | Pepcap Resources, Inc. | **+200.00%** | 119,350 | below the $200M cap floor |
| TSXV:EGR | EGR Exploration Ltd | **-60.00%** | 1,195,000 | below the $200M cap floor |
| CSE:TGIF | 1933 Industries, Inc. | **-50.00%** | 110,700 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| XETR:BEZ | Berentzen-Gruppe AG | **+18.44%** | 234,138 | below the $300M cap floor |
| XETR:TPG0 | Platform Group SE & Co. KGaA | **-11.18%** | 499,251 | below the $300M cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALTAI | LightOn S.A. | **+24.39%** | 344,145 | below the $100M cap floor |
| EURONEXT:ALTHO | Metavisio SA | **+14.29%** | 1,147,871 | below the $100M cap floor |
| EURONEXT:ALREE | REED | **-13.33%** | 1,167,645 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:ENY | Energy SpA | **+26.15%** | 501,500 | below the $100M cap floor |
| MIL:DATA | Datrix S.p.A. | **-17.18%** | 115,500 | below the $100M cap floor |
| MIL:MTV | Mondo TV S.p.A. | **-10.53%** | 2,151,258 | below the $100M cap floor |

### eu-es

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| BME:CITY | Club De Futbol Intercity SAD | **-5.26%** | 15,290,899 | below the $100M cap floor |

### eu-nl

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:EBUS | Ebusco Holding N.V. | **-8.47%** | 952,285 | below the $100M cap floor |

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:OXUR | Oxurion NV | **+25.00%** | 12,461,813 | below the $100M cap floor |

### eu-at

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-pt

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-ie

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:ESENSE | Enersense International Oyj | **-16.14%** | 274,918 | below the $100M cap floor |
| OMXHEX:CTH1V | Componenta Oyj | **+11.14%** | 117,325 | below the $100M cap floor |
| OMXHEX:SBI | Sunborn International Plc | **-6.10%** | 103,564 | below the $100M cap floor |

### eu-dk

No name below the cap floor cleared the volume gate and the move threshold in this region.

### eu-gr

No name below the cap floor cleared the volume gate and the move threshold in this region.

## No catalyst

The names that moved with **no sourced driver**: no company release, no filing, no analyst action, and no sector or macro move behind them that could be sourced. Separate, so they do not dilute the mover table.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `ASX:NST` | Northern Star Resources Ltd | **-5.71%** | 22.8 AUD | 5,646,879 | $23.14B | OTC | Fell 5.71% to 22.8 AUD with no driver found - no release for 19 November could be sourced |
| `ASX:CMM` | Capricorn Metals Ltd | **-5.69%** | 12.1 AUD | 2,605,851 | $3.94B | OTC | Fell 5.69% to 12.1 AUD with no driver found - no release for 19 November could be sourced |
| `ASX:GMD` | Genesis Minerals Limited | **-5.63%** | 6.2 AUD | 14,695,689 | $5.19B | OTC | Fell 5.63% to 6.2 AUD with no driver found - no release for 19 November could be sourced |
| `ASX:RRL` | Regis Resources Limited | **-5.48%** | 6.04 AUD | 3,649,424 | $3.26B | OTC | Fell 5.48% to 6.04 AUD with no driver found - no release for 19 November could be sourced |
| `ASX:SRL` | Sunrise Energy Metals Limited | **-5.34%** | 9.58 AUD | 1,758,405 | $1.17B | OTC | Fell 5.34% to 9.58 AUD with no driver found - no release for 19 November could be sourced |
| `ASX:TEA` | Tasmea Limited | **-5.07%** | 8.42 AUD | 1,438,972 | $1.68B | OTC | Fell 5.07% to 8.42 AUD with no driver found - no release for 19 November could be sourced |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TSE:319A` | Next Generation Technology Group, Inc. | **-6.79%** | 20040 JPY | 98,100 | $1.19B | none | Fell 6.79% to 20040 JPY with no driver found - no release for 19 November could be sourced |
| `TSE:6736` | Suncorporation | **+6.44%** | 10580 JPY | 45,000 | $1.39B | none | Rose 6.44% to 10580 JPY with no driver found - no release for 19 November could be sourced |
| `TSE:5273` | Mitani Sekisan Co., Ltd. | **+5.58%** | 2250 JPY | 88,100 | $1.03B | none | Rose 5.58% to 2250 JPY with no driver found - no release for 19 November could be sourced |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TWSE:3715` | Dynamic Holding Co Ltd | **-10.00%** | 126 TWD | 16,054,886 | $1.20B | none | Fell 10.00% to 126 TWD with no driver found - no release for 19 November could be sourced |
| `TWSE:8021` | Topoint Technology Co., Ltd. | **-10.00%** | 274.5 TWD | 3,363,401 | $1.36B | none | Fell 10.00% to 274.5 TWD with no driver found - no release for 19 November could be sourced |
| `TWSE:7711` | ASrock Rack, Inc. | **-9.99%** | 419 TWD | 1,361,250 | $1.01B | none | Fell 9.99% to 419 TWD with no driver found - no release for 19 November could be sourced |
| `TPEX:6187` | All Ring Tech Co., Ltd. | **-9.99%** | 694 TWD | 2,636,286 | $2.25B | none | Fell 9.99% to 694 TWD with no driver found - no release for 19 November could be sourced |
| `TPEX:6182` | Wafer Works Corp. | **-9.99%** | 63.1 TWD | 29,897,206 | $1.33B | none | Fell 9.99% to 63.1 TWD with no driver found - no release for 19 November could be sourced |
| `TWSE:6515` | WinWay Technology Co., Ltd. | **-9.97%** | 3205 TWD | 299,363 | $3.93B | none | Fell 9.97% to 3205 TWD with no driver found - no release for 19 November could be sourced |
| `TPEX:7734` | Ableprint Technology Co Ltd | **-9.97%** | 1400 TWD | 115,474 | $1.31B | none | Fell 9.97% to 1400 TWD with no driver found - no release for 19 November could be sourced |
| `TWSE:7769` | Hon. Precision, Inc. | **-9.96%** | 3210 TWD | 1,063,285 | $19.45B | none | Fell 9.96% to 3210 TWD with no driver found - no release for 19 November could be sourced |
| `TWSE:6526` | Airoha Technology Corp. | **-9.96%** | 606 TWD | 1,352,731 | $3.42B | none | Fell 9.96% to 606 TWD with no driver found - no release for 19 November could be sourced |
| `TWSE:7610` | LIANYOU METALS CO.,LTD. | **-9.96%** | 805 TWD | 945,070 | $1.58B | none | Fell 9.96% to 805 TWD with no driver found - no release for 19 November could be sourced |
| `TWSE:2455` | Visual Photonics Epitaxy Co., Ltd. | **-9.95%** | 294 TWD | 3,365,204 | $1.85B | none | Fell 9.95% to 294 TWD with no driver found - no release for 19 November could be sourced |
| `TWSE:4958` | Zhen Ding Technology Holding Limited | **-9.95%** | 344 TWD | 25,232,794 | $13.13B | none | Fell 9.95% to 344 TWD with no driver found - no release for 19 November could be sourced |
| `TWSE:3017` | Asia Vital Components Co., Ltd. | **-9.94%** | 2445 TWD | 4,658,467 | $32.33B | none | Fell 9.94% to 2445 TWD with no driver found - no release for 19 November could be sourced |
| `TWSE:6805` | Fositek Corp. | **-9.94%** | 1585 TWD | 542,895 | $3.66B | none | Fell 9.94% to 1585 TWD with no driver found - no release for 19 November could be sourced |
| `TPEX:7415` | BE Epitaxy Semiconductor Technology Co Ltd | **-17.39%** | 190 TWD | 331,343 | $209M | none | Fell 17.39% to 190 TWD with no driver found - no release for 19 November could be sourced |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TSX:TPX.A` | Molson Coors Canada Inc. Class A | **-10.94%** | 57 CAD | 700 | $7.62B | none | Fell 10.94% to 57 CAD with no driver found - no release for 19 November could be sourced |
| `TSX:TPX.B` | Molson Coors Canada Inc. Class B | **-5.32%** | 57 CAD | 3,802 | $7.62B | none | Fell 5.32% to 57 CAD with no driver found - no release for 19 November could be sourced |

### eu-de

No moved name without a sourced driver in this region.

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:NANO` | Nanobiotix SA | **+7.72%** | 25.94 EUR | 92,747 | $1.35B | ADR | Rose 7.72% to 25.94 EUR with no driver found - no release for 19 November could be sourced |

### eu-it

No moved name without a sourced driver in this region.

### eu-es

No moved name without a sourced driver in this region.

### eu-nl

No moved name without a sourced driver in this region.

### eu-be

No moved name without a sourced driver in this region.

### eu-at

No moved name without a sourced driver in this region.

### eu-pt

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:PHR` | Pharol, SA | **+2.49%** | 0.0945 EUR | 2,439,267 | $83M | none | Rose 2.49% to 0.0945 EUR with no driver found - no release for 19 November could be sourced |

### eu-ie

No moved name without a sourced driver in this region.

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `OMXHEX:AUROORA` | Auroora Group Plc | **+7.55%** | 10.54 EUR | 117,759 | $322M | none | Rose 7.55% to 10.54 EUR with no driver found - no release for 19 November could be sourced |

### eu-dk

No moved name without a sourced driver in this region.

### eu-gr

No moved name without a sourced driver in this region.

## Method, source health & caveats

### Method

- **Universe** - the TradingView per-country scanner, filtered on the ISSUER's own `country` (the endpoint takes it as `filter`; the `filters` key is silently ignored), one call per region and one for the America board. All 17 pulls were complete (`totalCount` == rows returned) on 19 November. 18,277 rows came back across the 16 regions and 4,304 names were published.
- **Floors (USD, applied AFTER conversion)** - au $300M + volume ≥ 100,000; jp $300M; tw $200M; ca $200M; eu-de $300M + volume ≥ 50,000; eu-fr/eu-it/eu-es/eu-nl/eu-be/eu-at $100M; eu-ie $200M; eu-fi/eu-dk $100M; eu-pt/eu-gr $50M.
- **FX** - open.er-api.com, rate date **Thu, 19 Nov 2026 00:02:31 +0000**. The table is **local currency per 1 USD**, so the conversion is a **division**: `usd_cap = market_cap_basic / FX[listing_currency]`. The identity asserted on every published row is `usd_cap * FX_per_USD == market_cap_local`.
- **Venue collapse** - the issuer's PRIMARY listing venue wins (au ASX; jp TSE/NAG/FSE/SAPSE; tw TWSE/TPEX; ca TSX/TSXV/CSE/NEO; eu-de XETR/FWB/LSX/LS/GETTEX/DUS/MUN/SWB/TRADEGATE/HAM/HAN), and a line whose implied prior close (`close / (1 + change/100)`) does not reconcile with the prior session's published close for the same symbol within 5% is a `stale_venue_print` and is dropped. Off-official lines are counted in the Coverage table.
- **Cap carrier** - the cap is resolved to the issuer's PRIMARY (common) line, converted ONCE with the primary's currency, and every line of that issuer carries that one USD figure; `cap_source_symbol` names the line it came from. A group with no common line is dropped as `issuer_unresolved` rather than published with a borrowed cap.
- **Cross-venue cap check** - the America scanner is a second reading of the same company-level cap. **73 of 1330 issuers with a US line disagree by more than 10%** after conversion; the primary venue's cap is the one published in every case, and the disagreements are listed in the caveats below.
- **Venue-official price rule** - where an exchange's own auction/close is published it is the price and the row carries the conflict in `price_conflict`. **No row-level conflict was found today**: the scanner close stood for every published row and every `price_conflict` cell is empty. The one venue-official price in this artifact is at index level - the ATHEX General's official close 2,601.23 (capital.gr, insider.gr, 19 Nov) - because the ATHEX has no Yahoo symbol and no TradingView venue index.
- **CSV columns** - **18**, unchanged from the previous session (`date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`). Prices are written to 4 decimals with trailing zeros stripped; `volume` and `market_cap` are integers.
- **Files written** - `international-eod/2026-11-19/`: 16 per-region CSVs (`au.csv` … `eu-gr.csv`), `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView au scanner | scanner.tradingview.com/au/scan, filter country = Australia, types = stock | ok | 2119 of 2119 rows, complete |
| TradingView jp scanner | scanner.tradingview.com/jp/scan, filter country = Japan, types = stock | ok | 4360 of 4360 rows, complete |
| TradingView tw scanner | scanner.tradingview.com/tw/scan, filter country = Taiwan, types = stock | ok | 2709 of 2709 rows, complete |
| TradingView ca scanner | scanner.tradingview.com/ca/scan, filter country = Canada, types = stock | ok | 8062 of 8062 rows, complete |
| TradingView eu-de scanner | scanner.tradingview.com/eu-de/scan, filter country = Germany, types = stock | ok | 4560 of 4560 rows, complete |
| TradingView eu-fr scanner | scanner.tradingview.com/eu-fr/scan, filter country = France, types = stock | ok | 691 of 691 rows, complete |
| TradingView eu-it scanner | scanner.tradingview.com/eu-it/scan, filter country = Italy, types = stock | ok | 383 of 383 rows, complete |
| TradingView eu-es scanner | scanner.tradingview.com/eu-es/scan, filter country = Spain, types = stock | ok | 234 of 234 rows, complete |
| TradingView eu-nl scanner | scanner.tradingview.com/eu-nl/scan, filter country = Netherlands, types = stock | ok | 109 of 109 rows, complete |
| TradingView eu-be scanner | scanner.tradingview.com/eu-be/scan, filter country = Belgium, types = stock | ok | 105 of 105 rows, complete |
| TradingView eu-at scanner | scanner.tradingview.com/eu-at/scan, filter country = Austria, types = stock | ok | 66 of 66 rows, complete |
| TradingView eu-pt scanner | scanner.tradingview.com/eu-pt/scan, filter country = Portugal, types = stock | ok | 32 of 32 rows, complete |
| TradingView eu-ie scanner | scanner.tradingview.com/eu-ie/scan, filter country = Ireland, types = stock | ok | 20 of 20 rows, complete |
| TradingView eu-fi scanner | scanner.tradingview.com/eu-fi/scan, filter country = Finland, types = stock | ok | 190 of 190 rows, complete |
| TradingView eu-dk scanner | scanner.tradingview.com/eu-dk/scan, filter country = Denmark, types = stock | ok | 173 of 173 rows, complete |
| TradingView eu-gr scanner | scanner.tradingview.com/eu-gr/scan, filter country = Greece, types = stock | ok | 129 of 129 rows, complete |
| TradingView america scanner | scanner.tradingview.com/america/scan, types = stock + dr | ok | 13546 of 13546 rows, complete - the source for `us_listing` and for the cross-venue cap check |
| TradingView global scanner | scanner.tradingview.com/global/scan, 17 index tickers | ok | 17 index closes (16 regions + the STOXX 600) |
| FX | open.er-api.com/v6/latest/USD | ok | rate date Thu, 19 Nov 2026 00:02:31 +0000 |
| ATHEX official close | capital.gr / insider.gr / euro2day, 19 Nov 2026 17:19 | ok | the General Index closed at 2,601.23, up 16.72 points or 0.65% - no vendor index covers it |
| Yahoo news endpoint | query2.finance.yahoo.com/v1/finance/search | no data | HTTP 200 with a quotes-only payload and **no `news` array** for the international tickers - a no-data answer, not a source failure; every catalyst was sourced from the exchange, the company IR release or the press instead, so no artifact column depends on it |

### Caveats

- **Cromwell Property Group's +422.86% is a corporate action, not a move.** Securityholders approved a **5-for-1 consolidation of the stapled securities** at the AGM on 17 November (99.71% of votes cast), effective 17 November; pre-consolidation securities last traded on 18 November and post-consolidation trading opened on a deferred-settlement basis on 19 November. Securities on issue go from 2,618,866,699 to 523,773,340. The row stays in `au.csv` with the source's own `change_pct`, but the adjusted prior close is A$1.75 (A$0.35 × 5) against an A$1.83 close - about **+4.6%**, not +422.86% - so the row is excluded from every published table (Cromwell Property Group ASX announcement 17 Nov; MarketIndex announcement 2A1711017, 17 Nov; grafa, 17 Nov).
- **`us_listing` changed on 228 rows against the previous session, and the change is a fix.** The America scanner appends " Ltd." **with a trailing period** ("Accor SA Ltd."), and the matcher did not strip the period, so the issuer key came out as `accorsaltd` and never matched the local `accor`. Every issuer with a " Ltd." US line was therefore published as `us_listing=none` even though a US line exists for it. The period is now stripped and the tokeniser splits on all punctuation ("Co.Ltd." -> `Co`, `Ltd`), which **adds** 186 US listings. 12 rows lost a listing: in each case the matcher had paired the local line with a **different company of a similar name** (Aegean Airlines SA with Aegon, Challenger Limited with Challenger Gold, Endeavour Group with Endeavour Silver, Perpetual Limited with Perpetuals.com, Banco Santander with Banco Santander-Chile, Capital B with Capital Bancorp, Iren with IREN, Mitsubishi Corporation with Mitsubishi Chemical, Sumitomo Corporation with Sumitomo Chemical, Black Diamond Group with Black Diamond Therapeutics, Integral Group with Integra LifeSciences, Navigator with Navigator Holdings) - and no US line exists for any of them, so `none` is the correct answer. **A known limitation remains**: the matcher can still pair two same-named issuers in the same country, and the cross-venue cap check below is where that shows up.
- **73 cross-venue cap disagreements above 10%** were recorded. The published cap is always the primary venue's; the gap is a second-reading disagreement, not a defect in the published number. The largest genuine cases are Seabridge Gold (C$2.76bn primary against US$1.95bn on its NYSE American line, -29.4%), Deutz (EUR2.01bn against US$2.71bn, +34.4%), GMO Internet (US$0.74bn against US$1.89bn, +154.8%), freee (US$1.23bn against US$1.81bn, +47.4%) and APA Group (US$10.23bn against the US$14.98bn NASDAQ:APA line, +46.5% - a US operating subsidiary, not the same issuer). The remaining flags pair a local line with an **unrelated** same-named US company and are the matcher limitation named above, not cap findings.
- **Taiwan's -10% prints are limit prices, not calculated moves.** TWSE and TPEX cap a daily move at ±10%, so a -10.00% close is a limit print and the market was shut at that price. The session was violent in both directions: the TAIEX peaked at 40,315.53, fell to an intraday low of 38,259.70 - a 1,935.21-point swing, the ninth largest intraday on record - and closed down 1,768.02 points. Of the TAIEX-listed names, 1,095 fell against 71 that rose and 128 hit their daily limit-down (CNA via Focus Taiwan, 19 Nov; Taiwan News, 19 Nov).
- **62 rows are carry-overs** - instruments that did not trade on this session, whose close is the prior session's print. They are kept in the CSVs as the source returned them, listed in `_carryover.json` with the date of each instrument's last actual trade (walked back through the prior files, never forward), and excluded from every table above.
- **The Nikkei close differs by 0.22 points from the vendor index** (59,444.21 on the exchange against 59,443.99 on the TradingView venue index). The exchange figure is the close of record; the index table carries the vendor figure with the difference stated.
- **The Dow Jones European close table carries the previous session's level** for the AEX, BEL 20, ATX, PSI 20, ISEQ, OMX Helsinki and OMX Copenhagen rows, while its change column agrees with the venue index; the index table therefore publishes the TradingView venue level and notes the disagreement rather than mixing the two.
- **Sector rotation** (over the written rows, mean and median `change_pct` per sector) - materials was the weakest sector on the ASX (-3.80%) and across the Canadian gold complex, semiconductors and PCB were the weakest on the TAIEX, while information technology, semiconductor equipment and services led the TSE and the SBF 120. The rotation is computed from the same rows as the breadth table; no cap-weighted sector aggregate is published, because this file's caps are company-level and deduplicate on `cap_source_symbol`.
