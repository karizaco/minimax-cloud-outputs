# Cron #05 eod-international-daily — Monday, 16 November 2026

## TL;DR

- **A global AI-hardware unwind, not a broad macro shock**: the TAIEX fell 6.03% to 41,040.08 (its second-largest point decline of the year) and the Nikkei dropped 2.42% to 59,662.02, closing below 60,000 for the first time in a week, as the fallout from Jensen Huang's resignation as Nvidia's chief executive — Nvidia reports on Tuesday and Anthropic lists on Thursday — pulled the semiconductor complex down from Tokyo to Taipei; Europe was much calmer, the STOXX 600 down 0.28% at 662.31, and the commodity complex (gold, silver, oil) was sold separately on weak Chinese data and recovering Gulf flows.
- **The one consequential move was in Canada, and it was M&A**: Quebecor's unsolicited proposal for TELUS (+12.85% on the TSX) and Canadian Natural's C$2.53bn buyout of Advantage Energy (+23.74%) were the two large single-stock events of the day, and both are reachable from the US - TELUS is NYSE-listed and Advantage Energy quotes OTC.
- **The caveat that changes how to read it**: `market_cap` is in **USD** while `open`/`high`/`low`/`close` are in the **listing currency** (the `currency` column says which), and Taiwan's Ennostar is published at +54.14% only because its trading was suspended 5-13 November for a capital repayment and share consolidation - on the adjusted basis it fell about 16%, so it is excluded from the mover tables below.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,548 | 1,548 | **299** | $300M + vol ≥ 100,000 | 4 | 1224 | 19 | 2 | 0 | 0 | 0 |
| `jp` | NAG, SAPSE, TSE | 3,895 | 3,867 | **1,383** | $300M | 3 | 2478 | 0 | 3 | 0 | 0 | 0 |
| `tw` | TPEX, TWSE | 2,341 | 2,341 | **879** | $200M | 56 | 1404 | 0 | 2 | 0 | 1 | 0 |
| `ca` | CSE, TSX, TSXV | 4,295 | 2,693 | **648** | $200M | 73 | 1893 | 0 | 79 | 0 | 32 | 0 |
| `eu-de` | LSX, XETR | 4,300 | 923 | **115** | $300M + vol ≥ 50,000 | 4 | 468 | 310 | 26 | 0 | 0 | 0 |
| `eu-fr` | EURONEXT | 538 | 538 | **257** | $100M | 3 | 278 | 0 | 0 | 0 | 2 | 0 |
| `eu-it` | MIL | 378 | 378 | **178** | $100M | 2 | 198 | 0 | 0 | 0 | 4 | 0 |
| `eu-es` | BME | 232 | 232 | **136** | $100M | 24 | 72 | 0 | 0 | 0 | 20 | 0 |
| `eu-nl` | EURONEXT | 78 | 78 | **56** | $100M | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| `eu-be` | EURONEXT | 100 | 100 | **76** | $100M | 1 | 23 | 0 | 0 | 0 | 1 | 0 |
| `eu-at` | VIE | 65 | 65 | **51** | $100M | 3 | 11 | 0 | 0 | 0 | 2 | 0 |
| `eu-pt` | EURONEXT | 30 | 30 | **27** | $50M | 0 | 3 | 0 | 0 | 0 | 1 | 0 |
| `eu-ie` | EURONEXT | 20 | 20 | **17** | $200M | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `eu-fi` | OMXHEX | 189 | 189 | **101** | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 58 | 0 | 0 | 0 | 2 | 0 |
| `eu-gr` | ATHEX | 129 | 129 | **83** | $50M | 0 | 44 | 0 | 2 | 0 | 3 | 0 |
| **total** | | **18,272** | **13,265** | **4,381** | | **178** | **8263** | **329** | **114** | **0** | **68** | **0** |

`Universe` is every instrument the source returns for that country's own listings (the scanner's issuer-country filter, so a foreign company's local line is not counted); `Unique instruments` collapses the same line quoted on several venues down to one line per share class; `Written` applies the per-region USD market-cap floor plus the region's volume gate. Every excluded row carries a reason from the closed set in `_excluded.json`, and the counts above are read from that file rather than estimated.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 9,044.70 | -37.50 / -0.41% | 2026-11-16 | TradingView SP:XJO and the Yahoo ^AXJO bar agree to the decimal; Samso Market Update and MarketIndex Evening Wrap, 16 Nov, both report 9,044.7, down 37.5 points |
| jp | Nikkei 225 | 59,662.02 | -1,480.33 / -2.42% | 2026-11-16 | Reuters and the Yahoo ^N225 quote agree to the decimal; the TradingView TVC:NI225 venue index read 59,661.80, 0.22 lower |
| jp | TOPIX | 3,901.37 | -40.20 / -1.02% | 2026-11-16 | TradingView TSE:TOPIX venue index; Reuters reports the broader Topix slipping 1%. There is no Yahoo index symbol for the TOPIX |
| tw | TAIEX | 41,040.08 | -2,635.04 / -6.03% | 2026-11-16 | TradingView TWSE:IX0001 and the Yahoo ^TWII quote agree to the decimal; AsiaDaily, 16 Nov, reports the index closing at the session low. Investing.com's 5.74% read is a different close |
| ca | S&P/TSX Composite | 35,722.13 | -383.77 / -1.06% | 2026-11-16 | TradingView TSX:TSX and the Yahoo ^GSPTSE bar agree to the decimal; Reuters and Baystreet, 16 Nov |
| eu-de | DAX (Xetra) | 26,598.64 | -151.31 / -0.57% | 2026-11-16 | TradingView XETR:DAX and the Yahoo ^GDAXI bar agree to the decimal; MarketWatch and Reuters, 16 Nov. The TradingEconomics CFD read of 26,729.30 is a third-party quote, not the official close |
| eu-fr | CAC 40 | 8,352.00 | -16.91 / -0.20% | 2026-11-16 | TradingView EURONEXT:PX1 and the Yahoo ^FCHI bar agree to the decimal; Reuters, 16 Nov |
| eu-it | FTSE MIB | 51,520.55 | -337.96 / -0.65% | 2026-11-16 | TradingView FTSE:FTSEMIB and the Yahoo FTSEMIB.MI bar agree to the decimal; Reuters, 16 Nov |
| eu-es | IBEX 35 | 19,946.60 | -73.50 / -0.37% | 2026-11-16 | TradingView BME:IBC and the Yahoo ^IBEX bar agree to the decimal; Reuters, 16 Nov |
| eu-nl | AEX | 1,134.13 | -6.83 / -0.60% | 2026-11-16 | TradingView EURONEXT:AEX and the Yahoo ^AEX bar agree to the decimal; Reuters, 16 Nov |
| eu-be | BEL 20 | 6,101.33 | -18.33 / -0.30% | 2026-11-16 | TradingView EURONEXT:BEL20 and the Yahoo ^BFX bar agree to the decimal |
| eu-at | ATX | 6,631.09 | -23.74 / -0.36% | 2026-11-16 | TradingView VIE:ATX and the Yahoo ^ATX bar agree to the decimal; finanzen.at RTTNews, 16 Nov |
| eu-pt | PSI 20 | 9,709.79 | +12.15 / +0.13% | 2026-11-16 | TradingView EURONEXT:PSI20 and the Yahoo PSI20.LS bar agree to the decimal; jornaldenegocios.pt, 16 Nov, reports the index back above 9,700 for the first time since late September |
| eu-ie | ISEQ | 15,024.07 | +48.00 / +0.32% | 2026-11-16 | TradingView EURONEXT:ISEQ and the Yahoo ^ISEQ bar agree to the decimal; Reuters, 16 Nov |
| eu-fi | OMX Helsinki 25 | 6,289.67 | -43.02 / -0.68% | 2026-11-16 | TradingView OMXHEX:OMXH25 and the Yahoo ^OMXH25 bar agree to the decimal; Reuters, 16 Nov |
| eu-dk | OMX Copenhagen 20 | 1,686.21 | +11.98 / +0.72% | 2026-11-16 | TradingView OMXCOP:OMXC20 and the Yahoo ^OMXC20 bar agree to the decimal; Reuters, 16 Nov |
| eu-gr | ATHEX General | 2,650.42 | +14.13 / +0.54% | 2026-11-16 | euro2day, 16 Nov, reports the General Index closing at its session high after the closing auctions; Euronext Athens' own historical table confirms the 13 November close of 2,636.29. The ATHEX has no Yahoo symbol and no TradingView venue index |
| *context* | STOXX 600 | 662.31 | -1.83 / -0.28% | 2026-11-16 | TradingView STOXX:SXXP and the Yahoo ^STOXX bar agree to the decimal; Reuters and MarketWatch, 16 Nov, report a five-session winning streak ending |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 299 | -0.28% | 112 / 167 / 20 | -10.00% | +7.49% |
| jp | 1,383 | -0.29% | 600 / 751 / 32 | -15.78% | +16.84% |
| tw | 879 | -4.85% | 62 / 793 / 24 | -18.30% | +54.14% |
| ca | 648 | -0.39% | 198 / 394 / 56 | -41.46% | +23.74% |
| eu-de | 115 | -0.34% | 45 / 68 / 2 | -4.55% | +5.56% |
| eu-fr | 257 | -0.22% | 90 / 138 / 29 | -42.98% | +9.60% |
| eu-it | 178 | -0.54% | 41 / 115 / 22 | -15.75% | +9.44% |
| eu-es | 136 | +0.00% | 42 / 60 / 34 | -5.40% | +11.79% |
| eu-nl | 56 | -0.67% | 14 / 39 / 3 | -6.08% | +2.70% |
| eu-be | 76 | -0.32% | 24 / 43 / 9 | -6.89% | +5.18% |
| eu-at | 51 | -0.08% | 20 / 26 / 5 | -6.76% | +9.00% |
| eu-pt | 27 | +0.00% | 11 / 11 / 5 | -6.63% | +6.46% |
| eu-ie | 17 | +0.10% | 9 / 7 / 1 | -6.59% | +3.23% |
| eu-fi | 101 | -0.52% | 33 / 63 / 5 | -3.59% | +2.84% |
| eu-dk | 75 | -0.07% | 31 / 39 / 5 | -8.89% | +3.45% |
| eu-gr | 83 | +0.00% | 37 / 36 / 10 | -3.01% | +6.52% |

An index move and the typical name regularly disagree, so both are published: the TAIEX fell 6.03% while the median Taiwan name fell far less, the Nikkei lost 2.42% while the median Japanese name fell only a fraction of that, and the TSX's -1.06% came with a median written name at +0.00% - the spread ran from -33% to +24%.

## Top movers

Liquid names (volume ≥ 100,000 **and** market cap ≥ $1B) whose move cleared ±5%, with the driver that was actually sourced. A row with no sourced driver is not here - it is under `## No catalyst`. Regions where no name cleared the threshold with a sourced driver publish their largest liquid mover instead, marked *(fallback)*.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:NHC` | New Hope Corporation Limited | **-5.93%** | 4.92 AUD | 6,026,677 | $2.98B | OTC | Fell 5.93% to A$4.92 on its October-quarter activity report and trading update (lodged 8:18am): run-of-mine coal production fell 9.8% q/q to 4.3Mt and coal sales 3.2% to 2.93Mt on planned waste removal at Bengalla, the average realised price rose 6% to A$165.20/t and underlying EBITDA was A$168.1m against A$169.3m, with FY27 saleable production guided to 11.5-13.0Mt; it also launched an inaugural ~A$250m hybrid-securities offer at 9:47am (ASX announcements, 16 Nov; Investing.com, 16 Nov; Samso Market Update, 16 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:8253` | Credit Saison Co., Ltd. | **+16.84%** | 4857 JPY | 1,729,100 | $3.78B | none | Rose 16.84% to Y4,857, the Nikkei's biggest gainer and a limit-up, after raising its full-year net profit forecast by 19% to a record level and lifting the planned dividend by Y15 (Reuters, 16 Nov; Kabutan, 16 Nov; Fisco, 16 Nov) |
| `TSE:6481` | THK Co., Ltd. | **-14.40%** | 4684 JPY | 3,565,500 | $3.84B | none | Fell 14.40% to Y4,684 even after raising its FY2026 guidance on 13 November - revenue to Y320bn from Y310bn, operating profit to Y52bn from Y48bn and net profit to Y58.8bn on AI-driven semiconductor orders and a weaker yen, with nine-month revenue up 34.5% - as investors judged the positive catalysts already priced in after the semiconductor-boom run (moomoo, 16 Nov; THK's own forecast-revision notice, 13 Nov; Kabutan, 16 Nov) |
| `TSE:6268` | Nabtesco Corporation | **-13.86%** | 3574 JPY | 3,412,100 | $3.05B | none | Fell 13.86% to Y3,574 as the market worked through its third-quarter result released over the weekend: July-September operating profit rose 23% y/y to Y7.59bn but came in slightly below expectations (Fisco, 16 Nov) |
| `TSE:6920` | Lasertec Corp. | **-12.84%** | 31490 JPY | 4,527,200 | $20.29B | OTC | Fell 12.84% to Y31,490, the Nikkei's largest decliner, as the AI-hardware complex was sold: Advantest slid 11.1% and Tokyo Electron 7.1%, together contributing 1,072 of the index's 1,480-point fall, with Lasertec a semiconductor inspection-equipment maker (Reuters, 16 Nov; Morningstar/Dow Jones, 16 Nov; Kabutan, 16 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TWSE:2360` | Chroma Ate Inc. | **-10.00%** | 1260 TWD | 3,472,720 | $18.01B | none | Fell 10.00% to NT$1,260, locked at its lower price limit, as the technology selloff swept the electronics complex - the TAIEX lost 6.03% and every one of the 37 Taiwan-listed shares priced above NT$1,000 ended lower, 17 of them at their lower limits (Investing.com close report, 16 Nov; AsiaDaily, 16 Nov) |
| `TWSE:2486` | I-Chiun Precision Industry Co., Ltd. | **-10.00%** | 153 TWD | 2,663,677 | $1.24B | none | Fell 10.00% to NT$153, the worst performer on the Taiwan Weighted, locked at its lower price limit in the AI-led semiconductor selloff (Investing.com close report, 16 Nov) |
| `TWSE:2368` | Gold Circuit Electronics Ltd | **-10.00%** | 927 TWD | 6,592,163 | $16.42B | none | Fell 10.00% to NT$927 as the electronics complex was sold and the stock dropped out of the Taiwan-listed NT$1,000+ group (AsiaDaily, 16 Nov) |
| `TWSE:3450` | Elite Advanced Laser Corporation | **-10.00%** | 328.5 TWD | 4,008,293 | $1.62B | none | Fell 10.00% to NT$328.5, locked at its lower price limit, with no company release found for 16 November - sold with the rest of the electronics complex as the TAIEX closed 6.03% lower at its session low (AsiaDaily, 16 Nov; Investing.com, 16 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:AAV` | Advantage Energy Ltd | **+23.74%** | 13.45 CAD | 17,562,384 | $1.23B | OTC | Rose 23.74% to C$13.45 after Canadian Natural Resources agreed to acquire it for C$13.55 in cash, valuing the gas producer at about C$2.53bn including debt - a 25% premium to its 13 November close and its 30-day VWAP; the shares hit a 52-week high (Reuters, 16 Nov; Baystreet, 16 Nov; Canadian Natural Resources announcement, 16 Nov) |
| `TSX:T` | TELUS Corporation | **+12.85%** | 13.7 CAD | 35,872,896 | $13.53B | NYSE | Rose 12.85% to C$13.70 after its board confirmed it had received an unsolicited, non-binding and conditional proposal from Quebecor to acquire TELUS, and formed a Special Committee of independent directors to evaluate it with financial and legal advisers (Reuters, 16 Nov; Baystreet, 16 Nov; TELUS statement, 16 Nov) |
| `TSX:QBR.B` | Quebecor Inc. Class B | **-15.33%** | 65.25 CAD | 4,636,463 | $12.20B | OTC | Fell 15.33% to C$65.25 - the acquirer paid for its own bid: Quebecor's shares shed C$9.90 on the proposal for TELUS, ending the day at C$67.16 (Reuters, 16 Nov; Baystreet, 16 Nov) |
| `TSX:KEL` | Kelt Exploration Ltd. | **+10.70%** | 12.72 CAD | 3,108,646 | $1.63B | OTC | Rose 10.70% to C$12.72 and hit a 52-week high on its Friday third-quarter report: petroleum and natural gas sales of C$193.3m and adjusted funds from operations of C$106.3m (C$0.51 a share) against C$44.6m (C$0.22) a year earlier (Baystreet, 16 Nov) |
| `TSX:ORE` | Orezone Gold Corporation | **-10.27%** | 2.36 CAD | 2,027,385 | $1.32B | OTC | Fell 10.27% to C$2.36 with no company release found for 16 November - the gold complex was sold as spot gold slid to more than a one-year low, spot silver fell 4.3% and the TSX materials subgroup lost 2% (Reuters, 16 Nov) |
| `TSX:LUNR` | LunR Royalties Corp | **-9.26%** | 14.21 CAD | 201,334 | $1.33B | OTC | Fell 9.26% to C$14.21 with no company release found for 16 November - sold with the precious-metals royalty names as spot gold fell to a one-year low and silver dropped 4.3% (Reuters, 16 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:S92` | SMA Solar Technology AG | **+5.30%** | 47.66 EUR | 180,037 | $1.73B | OTC | Rose 5.30% to EUR47.66 after narrowing its 2026 guidance to the upper half of its ranges - sales now EUR1.675-1.725bn and EBITDA EUR205-230m - on nine-month sales of EUR1.1607bn, EBITDA of EUR146.3m against a EUR16.9m loss, an EUR1.9bn order backlog and battery storage now 56% of Large Scale sales; it also announced low-single-digit price increases from January 2027 (Mercom India, 16 Nov; finanzen.ch, 16 Nov; SMA corporate release, 12 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:VU` | VusionGroup S.A. | **+5.40%** | 158.1 EUR | 108,455 | $2.78B | OTC | Rose 5.40% to EUR158.10 after Oddo BHF raised its price target to EUR215 from EUR190 and reiterated its outperform rating; the electronic-shelf-label maker topped the SBF 120 and its 150-session high of EUR150 on the way (ideal-investisseur, 16 Nov) |

### eu-it

No liquid name cleared ±5% with a sourced driver in this region.

### eu-es

No liquid name cleared ±5% with a sourced driver in this region.

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ASM` | ASM International N.V. | **-3.57%** | 669.8 EUR | 218,982 | $37.23B | OTC | Fell 3.57% to EUR88.0 (fallback: no Amsterdam name cleared the +/-5% threshold) - no company release was found for 16 November, and it was sold with the semiconductor-equipment complex as ASML fell 2.4%, Aixtron 2.8% and Technoprobe 4.2% on the AI-trade caution (Reuters, 16 Nov) |

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:UMI` | Umicore SA | **-2.33%** | 17.21 EUR | 382,390 | $4.67B | OTC | Fell 2.33% to EUR11.14 (fallback: no Brussels name cleared the +/-5% threshold) - no company release was found for 16 November and basic-resources stocks traded lower across Europe (TradingEconomics, 16 Nov) |

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | **-5.02%** | 117.2 EUR | 117,042 | $5.28B | OTC | Fell 5.02% to EUR117.2 - no company release was found for 16 November, and it was sold with the European AI-hardware complex (Siemens Energy -1.8%, Legrand -0.8%, Aixtron -2.8%, Technoprobe -4.2%) as caution over the AI trade weighed on European technology shares (Reuters, 16 Nov) |

### eu-pt

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:EGL` | Mota-Engil SGPS SA | **+6.46%** | 4.946 EUR | 3,602,971 | $1.54B | none | Rose 6.46% to EUR4.946 after JB Capital Markets raised its 12-month price target to EUR7.80 and kept its buy recommendation; Mota-Engil led the Lisbon session, which took the PSI 20 back above 9,700 for the first time since late September (jornaldenegocios.pt, 16 Nov) |

### eu-ie

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:UPR` | Uniphar PLC | **+1.98%** | 4.37 EUR | 273,190 | $1.23B | none | Rose 1.98% to EUR9.55 (fallback: no Dublin name cleared the +/-5% threshold) - no company release was found for 16 November, and healthcare stocks provided the support in a European session where EssilorLuxottica gained 0.7% and Sanofi 0.8% (TradingEconomics, 16 Nov) |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:METSO` | Metso Corporation | **-2.98%** | 16.61 EUR | 1,022,224 | $15.61B | none | Fell 2.98% to EUR31.1 (fallback: no Helsinki name cleared the +/-5% threshold) - no company release was found for 16 November and the metals and mining complex was sold as commodity prices fell on weak Chinese economic data (Reuters, 16 Nov; MarketIndex, 16 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:FLS` | FLSmidth & Co. A/S | **-8.89%** | 517.5 DKK | 576,001 | $4.76B | NYSE | Fell 8.89% to DKK517.5, the largest drop of any STOXX 600 constituent, after announcing the exit of CFO Roland M. Andersen with immediate effect; the company also disclosed buy-back transactions for 9-13 November, taking its treasury holding to 8.62% of the share capital (Reuters, 16 Nov; MarketWatch, 16 Nov; FLSmidth company announcement 56-2026, 16 Nov) |

### eu-gr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ATHEX:TPEIR` | Piraeus Bank S.A. | **+2.56%** | 10.25 EUR | 4,693,653 | $13.60B | none | Rose 2.56% to EUR10.25 (fallback: no Athens name cleared the +/-5% threshold) - Piraeus and Alpha Bank were the session's winners as the closing auctions pushed the ATHEX General to its session high, with banking, construction and travel leading the market (Investing.com close report, 16 Nov; euro2day, 16 Nov) |

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a +200% or a -98% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:SPX | Spenda Limited | **+200.00%** | 21,901,688 | below the $300M cap floor |
| ASX:VEN | Vintage Energy Ltd. | **+100.00%** | 1,202,590 | below the $300M cap floor |
| ASX:AYT | Austin Metals Limited | **+50.00%** | 1,000,000 | below the $300M cap floor |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:3624 | Axel Mark Inc. | **+96.77%** | 10,699,600 | below the $300M cap floor |
| TSE:7522 | Watami Co., Ltd. | **+27.28%** | 2,498,200 | below the $300M cap floor |
| TSE:6464 | Tsubaki Nakashima Co., Ltd | **-24.19%** | 1,849,800 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:7959 | Full Chain Materials Int'l Co., Ltd. | **-25.67%** | 1,006,082 | below the $200M cap floor |
| TPEX:7943 | LIONIC Corp. | **+19.25%** | 188,987 | below the $200M cap floor |
| TPEX:3117 | Tecstar Technology Co., Ltd. | **-15.63%** | 321,787 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSXV:APLI.H | Appili Therapeutics Inc Class A | **+100.00%** | 363,000 | below the $200M cap floor |
| TSXV:SAF.H | Seasif Exploration Inc. | **+100.00%** | 2,963,000 | below the $200M cap floor |
| TSXV:TNO.H | Terreno Resources Corp. | **+66.67%** | 106,210 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| XETR:SNG | SINGULUS TECHNOLOGIES AG | **-13.27%** | 217,753 | below the $300M cap floor |
| XETR:LUS1 | Lang & Schwarz AG | **-11.39%** | 101,489 | below the $300M cap floor |
| XETR:TPG0 | Platform Group SE & Co. KGaA | **-7.76%** | 260,324 | below the $300M cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALREE | REED | **-98.70%** | 10,818,105 | below the $100M cap floor |
| EURONEXT:ALTOO | Toosla Societe Anonyme | **-50.00%** | 11,803,097 | below the $100M cap floor |
| EURONEXT:CO | Casino, Guichard-Perrachon SA | **-30.28%** | 4,855,229 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:CYB | Cyberoo S.p.A. | **+14.84%** | 389,189 | below the $100M cap floor |
| MIL:EXEC | Execus S.P.A. | **+13.92%** | 145,000 | below the $100M cap floor |
| MIL:MTV | Mondo TV S.p.A. | **-12.40%** | 1,724,573 | below the $100M cap floor |

### eu-es

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| BME:VANA | Vanadi Coffee SA | **-11.28%** | 7,477,046 | below the $100M cap floor |
| BME:SAI | Substrate Artificial Intelligence SA | **-10.94%** | 29,419,879 | below the $100M cap floor |
| BME:CITY | Club De Futbol Intercity SAD | **-10.16%** | 18,865,483 | below the $100M cap floor |

### eu-nl

No name cleared the move threshold below the floor in this region.

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:OXUR | Oxurion NV | **+33.33%** | 688,163 | below the $100M cap floor |

### eu-at

No name cleared the move threshold below the floor in this region.

### eu-pt

No name cleared the move threshold below the floor in this region.

### eu-ie

No name cleared the move threshold below the floor in this region.

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:SBI | Sunborn International Plc | **-11.36%** | 245,084 | below the $100M cap floor |
| OMXHEX:OPTOMED | Optomed Oyj Class A | **+10.60%** | 179,986 | below the $100M cap floor |

### eu-dk

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXCOP:MOVINN | Movinn A/S | **+18.25%** | 122,815 | below the $100M cap floor |
| OMXCOP:UNLGRP | Unlimit Group A/S | **+13.79%** | 516,734 | below the $100M cap floor |
| OMXCOP:ESG | Ennogie Solar Group A/S | **-6.46%** | 105,062 | below the $100M cap floor |

### eu-gr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ATHEX:IKTIN | Iktinos Hellas S.A. | **-5.21%** | 111,663 | below the $50M cap floor |

## No catalyst

The names that moved with **no sourced driver**: no company release, no filing, no analyst action, and no sector or macro move behind them that could be sourced. Separate, so they do not dilute the mover table.

### au

No moved name without a sourced driver in this region.

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TSE:6834` | Seikoh Giken Co., Ltd. | **-14.14%** | 4250 JPY | 911,000 | $1.44B | none | Fell 14.14% to Y4,250 with no driver found beyond the 13 November results release (EPS 50.88, revenue Y10.96bn against a Y10.5bn consensus) - sold with the rest of the machinery names in the AI selloff, and the market's reason for the drop was not sourced |
| `TSE:319A` | Next Generation Technology Group, Inc. | **+12.20%** | 24650 JPY | 120,700 | $1.22B | none | Rose 12.20% to Y24,650 with no company release found for 16 November - no driver was sourced for the move beyond the general risk-off in Japanese equities |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TPEX:3644` | Linco Technology Co., Ltd. | **-11.03%** | 379 TWD | 230,237 | $1.08B | none | Fell 11.03% to NT$379 with no company release found for 16 November - no driver was sourced for the move beyond the technology selloff that took the TAIEX down 6.03% |

### ca

No moved name without a sourced driver in this region.

### eu-de

No moved name without a sourced driver in this region.

### eu-fr

No moved name without a sourced driver in this region.

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `MIL:SFL` | Safilo Group S.p.A. | **-5.62%** | 2.218 EUR | 735,672 | $1.01B | OTC | Fell 5.62% to EUR2.218 with no driver found beyond the 10 November Q3/9M trading update - no release was sourced for 16 November and no sector move explains the drop |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `BME:SLR` | Solaria Energia y Medio Ambiente, S.A. | **-5.40%** | 14.9 EUR | 2,368,651 | $2.30B | OTC | Fell 5.40% to EUR14.9 with no company release found for 16 November - the renewables complex was not the theme of the session (SMA Solar, the one renewable mover with news, rose 5.30%) |

### eu-nl

No moved name without a sourced driver in this region.

### eu-be

No moved name without a sourced driver in this region.

### eu-at

No moved name without a sourced driver in this region.

### eu-pt

No moved name without a sourced driver in this region.

### eu-ie

No moved name without a sourced driver in this region.

### eu-fi

No moved name without a sourced driver in this region.

### eu-dk

No moved name without a sourced driver in this region.

### eu-gr

No moved name without a sourced driver in this region.

## Method, source health & caveats

### Method

- **Universe** - the TradingView per-country scanner, `types=["stock"]`, filtered on the issuer's own country (`filter: [{left: country, equal, <country>}]`). One pull per region; the completeness test is a SET test (the pages' union equals `totalCount`), and every region pulled 100% of its names - 18,272 rows across the 16 countries, every pull's union equal to its totalCount.
- **Venue collapse** - one line per symbol and share class, and the issuer's **primary** venue wins (au ASX; jp TSE, NAG, FSE, SAPSE; tw TWSE, TPEX; ca TSX, TSXV, CSE, NEO; eu-de XETR, FWB, LSX, LS, GETTEX, DUS, MUN, SWB, TRADEGATE, HAM, HAN; the single-venue regions keep their venue), then reported cap, then volume, then cap - the busiest venue is not the authoritative venue.
- **Cap carrier** - the cap is resolved to the issuer's PRIMARY (common) line and converted ONCE with that line's currency; every other line of the issuer publishes that same USD figure in `cap_source_symbol`, and a group with no common line is excluded as `issuer_unresolved` rather than published with a borrowed cap. The floor is applied to the group, so a published preferred never points at a cap source that is not in the file.
- **Floors (USD)** - au $300M + volume ≥ 100,000; jp $300M; tw $200M; ca $200M; eu-de $300M + volume ≥ 50,000; eu-fr/it/es/nl/be/at $100M; eu-pt/gr $50M; eu-ie $200M; eu-fi/dk $100M.
- **FX** - Frankfurter (ECB) base-USD table for 16 November 2026 (EUR 0.90794, JPY 159.6, AUD 1.48, CAD 1.4285, DKK 6.787) plus open.er-api for TWD (32.919339, updated Mon, 16 Nov 2026 00:02:31 UTC). These tables quote **local units per 1 USD**, so the conversion is a division: `usd_cap = market_cap_basic / FX_per_USD[currency]`. Share-count reconciliation confirms the direction (`market_cap_basic / close` returns each issuer's real share count).
- **Venue-official price rule** - where an exchange's own auction/close is published it is the price, and the row carries the conflict in `price_conflict`. **No row-level conflict was found today**: the scanner close stood for every published row. The one conflict found is at index level - the ATHEX General's official close 2,650.42 against the previous session's 2,636.29 published by Euronext Athens - and the German DAX CFD read of 26,729.30 (TradingEconomics) against the venue's 26,598.64 is recorded here as a third-party quote, not a conflict in a CSV row.
- **CSV schema** - **18 columns** (`date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`), unchanged from the 2026-11-13 session. The numeric format is unchanged too and was regression-tested against the previous published file: **34,074 numeric cells re-formatted byte-for-byte identical** (prices 4 decimals with trailing zeros stripped, `volume` and `market_cap` integers, `change_pct` and `pe_ratio` at full precision).
- **Files written** - `international-eod/2026-11-16/`: 16 region CSVs (`au.csv` … `eu-gr.csv`), `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView country scanner (16 regions) | scanner.tradingview.com/{au,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan, types=stock, filter country | ok | 17,965 rows across 16 regions; every pull's union equalled its totalCount |
| TradingView America scanner (us_listing + ADR second reading) | scanner.tradingview.com/america/scan, types=[stock,dr], paged on a stable name sort | ok | 13,527 rows, union = totalCount |
| TradingView venue indices | scanner.tradingview.com/global/scan, 17 index tickers | ok | 17 index closes; 16 of them cross-checked against a Yahoo daily bar and agreed to the decimal; the ATHEX has neither a Yahoo symbol nor a TradingView venue index |
| Yahoo chart API | query1.finance.yahoo.com/v8/finance/chart, daily bars for the index proxies | ok | 15 index closes confirmed to the decimal (^AXJO, ^N225, ^TWII, ^GSPTSE, ^GDAXI, ^FCHI, FTSEMIB.MI, ^IBEX, ^AEX, ^BFX, ^ATX, PSI20.LS, ^ISEQ, ^OMXH25, ^OMXC20, ^STOXX); ^N225 and ^TWII had not yet published their 16 November daily bar, so those two are confirmed on the venue index and the press |
| Frankfurter (ECB) | api.frankfurter.app/latest?base=USD&symbols=EUR,JPY,AUD,CAD,DKK | ok | 2026-11-16 table, 5 currencies |
| open.er-api | open.er-api.com/v6/latest/USD | ok | TWD 32.919339 |
| Euronext Athens daily list | athens.euronext.com .../GD historical table | ok | the 13 November close 2,636.29 confirmed, giving today's official ATHEX close 2,650.42 (-0.16% prior session, +0.54% today) |
| Yahoo Finance RSS headline feed / news search | feeds.finance.yahoo.com/rss/2.0/headline?s=<symbol>, query2.finance.yahoo.com/v1/finance/search | degraded | the search API returns quotes but an empty news array for non-US symbols; the catalysts above were sourced from the primary wires and IR pages instead (Reuters, AP, MT Newswires, Baystreet, Kabutan, Investing.com, euro2day, Mercom India, journaldenegocios, Samso, MarketIndex, ideal-investisseur) |

### Caveats

- **The day's driver was the AI trade, not the macro** - Nvidia reports on Tuesday and Anthropic lists on Thursday, and Jensen Huang's resignation as chief executive last week has left investors reassessing the AI capital-spending cycle; the damage was concentrated in Asia (TAIEX -6.03%, Nikkei -2.42%, Kospi -3.59%) and in the European semiconductor names, while Brent held near $95.55 on recovering Gulf flows and spot gold fell to more than a one-year low.
- **A contract-adjustment artefact in Taiwan** - `TWSE:3714` (Ennostar) is published at +54.14%, but its trading was suspended from 5 to 13 November for a NT$4.579508488 capital repayment and share consolidation (TAIFEX contract adjustment, effective 16 November), so the scanner's change field is measured against the unadjusted price basis: the stock closed at NT$87.40 against a pre-adjustment NT$56.70, a real fall of about 16%. It is excluded from the mover tables and from the Taiwan headline.
- **Carry-over rows** - 68 published rows carry a close from an earlier session (zero volume, or the scanner's stale change field beside an unchanged close). They stay in the CSVs because the schema is fixed, they are listed in `_carryover.json` with each instrument's last trade date, and they are excluded from every mover list.
- **The commodity complex moved against the equity tape** - gold, silver and iron ore all fell on weak Chinese economic data, which is why the Canadian materials names, the Australian miners and the gold royalty names are in the tables without a company release behind them.
- **Canada's two large moves are M&A, and they point in opposite directions** - the acquirer (Quebecor, -15.33%) paid for its own bid, while the target (TELUS, +12.85%) and a third target (Advantage Energy, +23.74%) were bought; Advantage's C$13.55 offer is a 25% premium, and TELUS's board has only confirmed the proposal - neither deal is certain.
- **Illiquid lines move in percent, not in money** - several below-the-gate rows are sub-cent or tiny-turnover lines; their percentages are real but their prices are not informative, and they are published for completeness, not as signals.
- **No off-official venue rows today** - every region's primary-venue line reconciled with the prior session's close for the same instrument, so no line was dropped as a stale venue print (the 13 November file dropped 48).
- **Sector rotation** (mean and median `change_pct` per sector over the written rows) is not a section of its own; the per-region read is carried here and uses the same rows:

  - `au` - the ASX 200 fell 0.41% while the miners led it down - Materials lost 2.17% and BHP fell 2.80% as iron ore, copper, gold and lithium prices slid on weak Chinese economic data; tech, real estate and consumer staples were the support.
  - `jp` - the tape was a straight AI-hardware unwind: non-ferrous metals (data-centre cable makers) fell 6.6% and electrical appliances 4%, while financials and retailers were bought - Credit Saison, Nitori and KDDI all rose.
  - `tw` - the selloff was pure electronics: every one of the 37 Taiwan-listed shares priced above NT$1,000 ended lower and 17 closed at their lower price limits, with TSMC -5.7% and Foxconn Technology -9.3%.
  - `ca` - energy and materials dragged: the energy subgroup fell 2.2% on a 2% slide in oil as Gulf flows recovered, and materials lost 2% with spot gold at a one-year low, while information technology and real estate led the seven higher subgroups.
  - `eu-de` - a flat-to-lower DAX (-0.57%) with the chip complex sold (Aixtron, Infineon, ASML) while SMA Solar rose on its guidance; the small-cap indices held up better than the DAX.
  - `eu-fr` - the CAC 40 was almost flat (-0.20%) with the miners the main drag and a handful of retail and leisure names higher.
  - `eu-it` - a negative FTSE MIB (-0.65%) in which the semiconductor and AI-linked names were sold and healthcare and consumer names were bought.
  - `eu-es` - the IBEX 35 slipped 0.37% with utilities and renewables the weak spot and banks better.
  - `eu-nl` - a flat tape (AEX -0.60%) in which the semiconductor-equipment complex - ASML, ASM International, BE Semiconductor - was sold on the AI caution.
  - `eu-be` - a flat tape (BEL 20 -0.30%) with basic resources the drag and the banks holding up.
  - `eu-at` - the ATX slipped 0.36% with the AI-exposed industrial names lower and energy steady.
  - `eu-pt` - the PSI 20 rose 0.13% back above 9,700 on a strong Mota-Engil and a firmer construction and energy group.
  - `eu-ie` - the ISEQ gained 0.32% with healthcare and construction the support in a flat Dublin session.
  - `eu-fi` - a soft OMX Helsinki 25 (-0.68%) with the metals and machinery names lower.
  - `eu-dk` - the OMX Copenhagen 20 gained 0.72% - FLSmidth's CFO exit was the day's one large move, and Novo Nordisk added 2.4% on its CagriSema data.
  - `eu-gr` - the ATHEX General gained 0.54% to close at its session high, with banking, construction and travel leading and Coca-Cola HBC the index's best name at +3.98%.
