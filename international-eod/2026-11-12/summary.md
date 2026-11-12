# Cron #05 eod-international-daily — Thursday, 12 November 2026

## TL;DR

- **One story ran through the whole world on 12 November: Nvidia's leadership crisis.** The Wall Street Journal reported that Nvidia's board was preparing to remove CEO Jensen Huang; the shares fell ~8% after hours and 7.4% in Frankfurt, and the AI complex sold off from Taipei to Toronto. **Taipei took the hit — the TAIEX fell 1,165.28 points (-2.63%) to 43,091.87, its sharpest fall in weeks, with TSMC -2.30% and ASE -5.02%** — while Europe went the other way and closed at a record: the **STOXX 600 +0.14% to a record 664.01** on strong earnings, the **DAX +0.41% to 26,771.88** and the **CAC 40 +0.34% to 8,361.36**. Japan closed mixed (**Nikkei -0.70% to 60,819.36**, TOPIX +0.20%), Australia was flat (**-0.07% to 9,146.80**) and Canada fell (**TSX -0.75% to 36,137.19**). **4,380 instruments printed across the 16 regions.**
- **The most consequential move was the AI-hardware de-risking, and the foreign names a US trader can actually reach are the US lines: Domino's Pizza +12.93% (ASX:DMP, OTC) to a 52-week high, Cargojet +10.29% (TSX:CJT, OTC) on a Q3 beat, freee -14.52% (TSE:4478, OTC) to the daily limit low, Resonac +12.48% (TSE:4004, OTC) on a profit upgrade, Aya Gold -6.91% (TSX:AYA, NASDAQ) despite record production, and PLS -8.06% (ASX:PLS, OTC) on its MSCI index removal.** The largest single-name moves were in the chip complex: Dexerials -16.57% (TSE:4980) on an H1 profit fall, Nan Ya PCB -10.00% and ITEQ -10.00% (both limit down, TW), Kinsus -9.99% and Holy Stone -9.98% (TW), and Rakuten Bank -14.87% (TSE:5838) on a forecast that missed. The one genuinely company-specific story in Europe was **Ottobock -16.60% (XETR:OBCK)** — a Q3 beat with guidance confirmed, sold because management warned that reimbursement in several core markets is getting harder.
- **Read the numbers with the unit convention in mind: `market_cap` is USD while every price is in the listing currency** (the `currency` column says which) — a Y2,167.50 close and a C$108.77 close are not comparable, the caps are. **And read the tape with three caveats: it is a narrow de-risking, not a broad one** (Europe closed higher on the same day the chip complex was sold; the average name in Taipei fell 1.59% while the average Japanese name rose 0.56%), **every close here is the scanner's venue close with carry-over rows included as the source returned them**, and **the 18-column schema is unchanged from the 11 November session**.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,543 | 1,543 | **303** | $300M + vol ≥ 100,000 | 4 | 1216 | 19 | 1 | 0 | 1 | 0 |
| `jp` | FSE, NAG, SAPSE, TSE | 3,899 | 3,868 | **1,380** | $300M | 2 | 2483 | 0 | 3 | 0 | 0 | 0 |
| `tw` | TPEX, TWSE | 2,337 | 2,337 | **882** | $200M | 55 | 1398 | 0 | 2 | 0 | 2 | 0 |
| `ca` | CSE, NEO, TSX, TSXV | 4,293 | 2,679 | **631** | $200M | 33 | 1859 | 0 | 156 | 0 | 40 | 0 |
| `eu-de` | FWB, GETTEX, LS, LSX, XETR | 4,300 | 925 | **122** | $300M + vol ≥ 50,000 | 4 | 464 | 309 | 26 | 0 | 0 | 0 |
| `eu-fr` | EURONEXT | 542 | 542 | **259** | $100M | 1 | 282 | 0 | 0 | 0 | 3 | 0 |
| `eu-it` | MIL | 378 | 378 | **178** | $100M | 2 | 198 | 0 | 0 | 0 | 5 | 0 |
| `eu-es` | BME | 233 | 233 | **137** | $100M | 24 | 72 | 0 | 0 | 0 | 28 | 0 |
| `eu-nl` | EURONEXT | 78 | 78 | **56** | $100M | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| `eu-be` | EURONEXT | 101 | 101 | **76** | $100M | 1 | 24 | 0 | 0 | 0 | 1 | 0 |
| `eu-at` | VIE | 65 | 65 | **51** | $100M | 3 | 11 | 0 | 0 | 0 | 1 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **28** | $50M | 0 | 3 | 0 | 0 | 0 | 1 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| `eu-fi` | OMXHEX | 188 | 188 | **100** | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 58 | 0 | 0 | 0 | 0 | 0 |
| `eu-gr` | ATHEX | 130 | 130 | **85** | $50M | 0 | 43 | 0 | 2 | 0 | 2 | 0 |
| **total** | | **18,271** | **13,251** | **4,380** | | **134** | **8219** | **328** | **190** | **0** | **84** | **0** |

`Universe` is every instrument the source returns for that country's own listings (the scanner's issuer-country filter, so a foreign company's local line is not counted); `Unique instruments` collapses the same line quoted on several venues down to one line per issuer and share class; `Written` applies the per-region USD market-cap floor plus the region's volume gate. Every excluded row carries a reason from the closed set in `_excluded.json`, and the counts above are read from that file rather than estimated.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 9,146.80 | -6.40 / -0.07% | 2026-11-12 | Samso Market Update, 12 Nov (4:30pm AEDT): 9,146.8, down 6.4 points; the TradingView SP:XJO venue index agrees to the decimal |
| jp | Nikkei 225 | 60,819.36 | -429.23 / -0.70% | 2026-11-12 | Kyodo News (TSE close 60,819.36, down 429.23) and Yahoo ^N225 1-hour final bar; the TradingView TVC:NI225 venue index read 60,819.14, 0.22 lower |
| jp | TOPIX | 3,937.33 | +7.94 / +0.20% | 2026-11-12 | TradingView TSE:TOPIX venue index, 12 Nov; Reuters and QNA both report 3,937.33 |
| tw | TAIEX | 43,091.87 | -1,165.28 / -2.63% | 2026-11-12 | CNA and the TWSE daily board, 12 Nov: -1,165.28 points to 43,091.87, session range 42,943.50-44,525.24; the TradingView TWSE:IX0001 index and Yahoo ^TWII intraday agree |
| ca | S&P/TSX Composite | 36,137.19 | -274.53 / -0.75% | 2026-11-12 | TradingView TSX:TSX venue index and Yahoo ^GSPTSE agree to the decimal; Reuters' 36,256.06 was a 10:54 ET midday reading, not the close |
| eu-de | DAX (Xetra) | 26,771.88 | +109.11 / +0.41% | 2026-11-12 | Edge Consultancy Europe wrap, 12 Nov (Xetra closing price) and Yahoo ^GDAXI; the TradingView XETR:DAX venue index agrees to the decimal |
| eu-fr | CAC 40 | 8,361.36 | +28.49 / +0.34% | 2026-11-12 | Edge Consultancy Europe wrap, 12 Nov and Yahoo ^FCHI; the TradingView EURONEXT:PX1 venue index agrees to the decimal |
| eu-it | FTSE MIB | 51,808.67 | -137.87 / -0.27% | 2026-11-12 | Edge Consultancy Europe wrap, 12 Nov and Yahoo FTSEMIB.MI; the TradingView FTSE:FTSEMIB venue index agrees to the decimal |
| eu-es | IBEX 35 | 19,965.50 | -62.40 / -0.31% | 2026-11-12 | Edge Consultancy Europe wrap, 12 Nov and Yahoo ^IBEX; the TradingView BME:IBC venue index agrees to the decimal |
| eu-nl | AEX | 1,140.12 | -5.02 / -0.44% | 2026-11-12 | Edge Consultancy Europe wrap, 12 Nov and Yahoo ^AEX; the TradingView EURONEXT:AEX venue index agrees to the decimal |
| eu-be | BEL 20 | 6,115.09 | +14.61 / +0.24% | 2026-11-12 | Yahoo ^BFX; the TradingView EURONEXT:BEL20 venue index agrees to the decimal |
| eu-at | ATX | 6,685.89 | -52.96 / -0.79% | 2026-11-12 | finanzen.at RTTNews European close, 12 Nov (ATX 6,686, -0.8%); the TradingView VIE:ATX venue index agrees to the decimal |
| eu-pt | PSI 20 | 9,596.37 | +1.86 / +0.02% | 2026-11-12 | Yahoo PSI20.LS; the TradingView EURONEXT:PSI20 venue index agrees to the decimal |
| eu-ie | ISEQ | 15,011.50 | -23.58 / -0.16% | 2026-11-12 | Yahoo ^ISEQ; the TradingView EURONEXT:ISEQ venue index agrees to the decimal |
| eu-fi | OMX Helsinki 25 | 6,341.71 | +13.73 / +0.22% | 2026-11-12 | Yahoo ^OMXH25; the TradingView OMXHEX:OMXH25 venue index agrees to the decimal |
| eu-dk | OMX Copenhagen 20 | 1,669.56 | +9.26 / +0.56% | 2026-11-12 | Yahoo ^OMXC20; the TradingView OMXCOP:OMXC20 venue index agrees to the decimal |
| eu-gr | ATHEX General | 2,640.52 | -15.61 / -0.59% | 2026-11-12 | Euronext Athens' own index page (2,640.52, high 2,664.10, low 2,633.44) and euro2day's 17:37 close report; there is no Yahoo symbol for the ATHEX and the TradingEconomics CFD read of 2,652.81 is a third-party quote, not the official close |
| *context* | STOXX 600 | 664.01 | +0.96 / +0.14% | 2026-11-12 | Stoxx administrator's 17:00 GMT final value via the Edge Consultancy Europe wrap, 12 Nov; the TradingView STOXX:SXXP venue index agrees to the decimal |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 302 | -0.57% | 111 / 173 / 18 | -9.39% | +23.49% |
| jp | 1,380 | +0.56% | 849 / 502 / 29 | -16.87% | +18.55% |
| tw | 880 | -1.59% | 194 / 637 / 49 | -12.21% | +15.07% |
| ca | 591 | -0.46% | 166 / 393 / 32 | -21.75% | +19.96% |
| eu-de | 122 | -0.22% | 52 / 69 / 1 | -17.09% | +23.17% |
| eu-fr | 256 | -0.11% | 99 / 137 / 20 | -6.07% | +10.56% |
| eu-it | 173 | +0.00% | 84 / 81 / 8 | -11.44% | +6.54% |
| eu-es | 109 | +0.00% | 45 / 51 / 13 | -3.80% | +4.12% |
| eu-nl | 56 | -0.01% | 24 / 28 / 4 | -4.88% | +3.72% |
| eu-be | 75 | +0.00% | 36 / 33 / 6 | -6.04% | +3.51% |
| eu-at | 50 | -0.61% | 16 / 29 / 5 | -5.99% | +4.00% |
| eu-pt | 27 | +0.00% | 12 / 10 / 5 | -4.11% | +7.75% |
| eu-ie | 17 | +0.15% | 9 / 6 / 2 | -1.42% | +1.56% |
| eu-fi | 100 | +0.23% | 57 / 37 / 6 | -10.71% | +5.43% |
| eu-dk | 75 | +0.44% | 49 / 23 / 3 | -8.32% | +13.73% |
| eu-gr | 83 | +0.00% | 36 / 34 / 13 | -4.46% | +4.77% |

**The index and the average name disagreed all day, and the disagreement is the story.** Taipei is the clearest case: the TAIEX fell 2.63% and the median written Taiwanese name fell **1.59%**, with 637 of 880 names down. But Tokyo went the other way — the Nikkei fell 0.70% while the median Japanese name **rose 0.56%** and 849 of 1,380 names advanced, because the losses were concentrated in the chip complex while tobacco, construction and shipping rallied. Europe split the same way: the STOXX 600 at a record +0.14% sat on a Frankfurt market where the median name was -0.22% and the DAX's own gain came from insurers and earnings, while autos (-1.43%) and basic resources (-1.32%) lagged. In Australia the index was flat but the median name fell 0.57%, with the banks up 1.10% and materials down 2.08%.

**Sector rotation on the liquid subset** (mean change by sector, names with volume ≥ 100,000 and cap ≥ $1B): the leadership flipped from yesterday's AI complex to defensives and materials-linked names. Best sectors were Australian process industries (+1.49%, 3 names), Japanese transportation (+1.96%, 37 names) and health services (+2.86%), Canadian retail trade (+1.07%, 9 names) and Italian transportation (+2.92%); the worst were Australian non-energy minerals (**-3.58%**, 36 names), Canadian non-energy minerals (**-3.73%**, 61 names), Taiwanese producer manufacturing (**-3.75%**, 36 names) and Japanese electronic technology (**-1.86%**, 45 names). The macro backdrop behind it: gold fell ~2.6-2.9% to roughly $3,879-3,970/oz on a more-than-one-year low, oil recovered mid-session after Trump's comment that the US "does not need a deal with Iran", and US yields near 5% pushed money out of resources and into banks.

## Top movers

Liquid names (volume ≥ 100,000 **and** market cap ≥ $1B) whose move cleared ±5%, capped at the six largest absolute moves per region, with the driver that was actually sourced. A row with no sourced driver is not here — it is under `## No catalyst`. Regions where no name cleared the threshold with a sourced driver publish their largest liquid mover instead, marked.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:DMP` | Domino's Pizza Enterprises Limited | **+12.93%** | 25.06 AUD | 1,836,765 | $1.43B | OTC | AGM address lodged at 3:56pm Wednesday: FY26 record free cash flow of A$164.1m, final dividend +51.2% to 32.5c, net leverage cut to 1.86x, and October same-store sales positive in Australia, New Zealand and the Netherlands - closed at a 52-week high of A$25.06 on ~4x average volume (Samso Market Update, 12 Nov; The Bull, 12 Nov) |
| `ASX:MI6` | Minerals 260 Limited | **-8.52%** | 0.805 AUD | 9,184,796 | $1.54B | OTC | Fell 8.52% to A$0.805 on the day the Western Australian government granted works approval for its Bullabulling gold project (processing plant, power and tailings storage) - the positive project milestone did not lift the stock while the gold-miner complex fell (ASX All Ordinaries Gold index -3.59%) (Samso Market Update, 12 Nov) |
| `ASX:PLS` | PLS Group Limited | **-8.06%** | 2.85 AUD | 34,850,646 | $6.82B | OTC | Fell 8.06% to A$2.85 on A$97.6m turnover after index provider MSCI said it would remove PLS from the MSCI Australia Index, and Citi cut its target to A$4.10 from A$5.70 (Buy kept); the only ASX filings since Wednesday afternoon were substantial-holding notices (Market Index via IBTimes Australia, 12 Nov; Stockwirex, 12 Nov; Samso, 12 Nov) |
| `ASX:LTR` | Liontown Limited | **-6.99%** | 0.665 AUD | 43,232,252 | $1.56B | OTC | Closed down 6.99% at A$0.665 on 43m+ shares as lithium names were sold off on sentiment rather than price (lithium carbonate only -0.2%): PLS -8.1%, Elevra -8.4%, Vulcan -7.0%; JPMorgan had cut its target to 80c from A$1.10 on Monday, and the stock is down ~57% year-to-date (IBTimes Australia, 12 Nov; Stockwirex, 12 Nov) |
| `ASX:SRL` | Sunrise Energy Metals Limited | **-6.93%** | 13.03 AUD | 344,379 | $1.65B | OTC | Fell 6.93% to A$13.03 on the day of its AGM (CEO presentation 10:58am, meeting results 2:58pm) and with the battery-materials complex; its last release before that was the Agni Semiconductor investment progress report on 10 November (Samso, 12 Nov; Intelligent Investor announcement feed, 12 Nov) |
| `ASX:PDI` | PDI Gold Limited | **-6.46%** | 4.63 AUD | 1,912,933 | $3.34B | OTC | Fell 6.46% to A$4.63 with no ASX announcement since 4pm Wednesday, as the gold-miner complex was sold off (ASX All Ordinaries Gold index -3.59%, spot gold -2.6%) (Samso Market Update, 12 Nov; FN Arena ASX winners/losers, 12 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:4980` | Dexerials Corp. | **-16.57%** | 2167.5 JPY | 7,422,500 | $2.79B | none | H1 FY3/27 profit fell on weak display and ARF volumes and higher growth-investment costs, although full-year guidance was left unchanged at Y123.0bn sales and Y40.0bn business profit; the stock had already fallen 19% the prior week (Dexerials H1 slides summary via TradingView News, 12 Nov; Simply Wall St, 12 Nov) |
| `TSE:3107` | Daiwabo Holdings Co., Ltd. | **+15.27%** | 3857 JPY | 1,426,500 | $1.77B | none | Raised its FY3/2027 forecast after Wednesday's close: operating profit to Y43.0bn from Y36.5bn and sales to Y1.369tn from Y1.189tn, citing continued strong corporate IT demand (Kabutan, 12 Nov) |
| `TSE:5838` | Rakuten Bank, Ltd. | **-14.87%** | 5466 JPY | 5,689,500 | $7.02B | none | H1 results (11 Nov) showed net profit of Y43.2bn, +27.0% y/y, and an upwardly revised forecast reflecting post-restructuring figures - but the revision fell short of market expectations, and the shares were sharply lower (Fisco Japan via moomoo, 12 Nov; Wealthpath market brief, 12 Nov) |
| `TSE:4478` | freee K.K. | **-14.52%** | 4120 JPY | 810,900 | $1.80B | OTC | Fell 14.52% to the daily limit low, among the names sold off for poor earnings or results that missed expectations; no separate company release was found for 12 November (Wealthpath market brief, 12 Nov) |
| `TSE:4004` | Resonac Holdings Corporation | **+12.48%** | 14150 JPY | 7,121,800 | $14.81B | OTC | Raised FY2026 core operating profit to Y250.0bn from Y196.0bn and sales to Y1.235tn from Y1.165tn on strong advanced-semiconductor demand, and announced the sale of its graphite-electrode business and its exit from Li-ion anode material; Jan-Sep net profit was Y94.64bn, ~16x the prior year (Kabutan, 12 Nov) |
| `TSE:5714` | DOWA HOLDINGS CO., LTD. | **+10.92%** | 8613 JPY | 2,107,900 | $2.89B | none | Gapped up after raising its full-year forecast with H2 results: sales to Y1.0tn from Y941.0bn, operating profit to Y71.5bn from Y53.0bn, net profit to Y70.0bn from Y57.0bn and the year-end dividend +Y77 to Y415, plus a buyback of up to 2.4m shares (Y16.0bn) (Kabutan, 12 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TPEX:7686` | A-Top Health Biotech Co., Ltd. | **-12.21%** | 640 TWD | 163,176 | $1.11B | none | No company-specific release was found for 12 November; it fell with the broader OTC board as the TAIEX lost 1,165 points on the Nvidia-led risk-off (CNA, 12 Nov) |
| `TPEX:3324` | AURAS Technology Co., Ltd. | **-10.00%** | 1170 TWD | 5,586,204 | $3.59B | none | Limit-down with the electronics/PCB supply chain in the Nvidia-driven selloff; the electronic-components sector closed -5.97% and plastics -5.30% (CNA, 12 Nov; Gate News, 12 Nov) |
| `TWSE:6213` | ITEQ Corporation | **-10.00%** | 522 TWD | 41,880,559 | $6.41B | none | Limit-down with the PCB/electronics complex as investors feared a Wall Street spillover from Nvidia's ~8% after-hours fall and its board's discussion of removing CEO Jensen Huang; TSMC -2.30% and ASE Technology -5.02% (CNA, 12 Nov; The Edge Asia market wrap, 12 Nov) |
| `TWSE:8046` | Nan Ya Printed Circuit Board Corporation | **-10.00%** | 972 TWD | 12,539,521 | $21.22B | none | Limit-down PCB line in the AI-hardware de-risking after the Nvidia CEO turmoil - Nanya PCB and Hermes-Epitek both hit the daily limit down, with electronic components -5.97% and computers/peripherals -4.93% (CNA, 12 Nov; Gate News, 12 Nov) |
| `TWSE:3189` | Kinsus Interconnect Technology Corp. | **-9.99%** | 667 TWD | 9,295,694 | $11.87B | none | Fell 9.99% with the IC-substrate/PCB complex (Unimicron and Taiwan Union Tech both more than 8% down) as TSMC -2.30% and ASE Technology -5.02% dragged the TAIEX (CNA, 12 Nov; Gate News, 12 Nov) |
| `TWSE:3026` | Holy Stone Enterprise Co., Ltd. | **-9.98%** | 505 TWD | 17,015,831 | $2.83B | none | Fell 9.98% with the electronics complex as the TAIEX lost 1,165.28 points (-2.63%) and defensive food and telecom names were bid (CNA, 12 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:CJT` | Cargojet Inc. | **+10.29%** | 108.77 CAD | 656,426 | $1.02B | OTC | Q3 revenue and adjusted profit beat analyst estimates, and the shares hit a 52-week high of C$108.28; on Wednesday the air-cargo carrier also announced the expansion of its Hamilton (YHM)-Miami service to three weekly rotations from 2 December (Reuters via Baystreet, 12 Nov; Baystreet, 12 Nov) |
| `TSX:CTC.A` | Canadian Tire Corporation, Limited Class A | **+7.22%** | 219.77 CAD | 339,499 | $7.46B | OTC | Q3 results (quarter ended 3 October) delivered diluted EPS from continuing operations of $4.27, up $1.14 or 36.4% y/y and 13.0% on a normalised basis; the shares hit a 52-week high of $219.19 (Baystreet, 12 Nov) |
| `TSX:AYA` | Aya Gold & Silver Inc. | **-6.91%** | 32.48 CAD | 974,199 | $3.53B | NASDAQ | Reported strong Q3-2026 results on record production and lower cash costs (12 Nov), yet the shares fell as spot gold dropped almost 3% to a more-than-one-year low; CIBC maintained Outperform with a C$55.00 target (GlobeNewswire via Yahoo Finance, 12 Nov; Reuters, 12 Nov) |
| `TSX:APTX` | Apotex Health Corp. | **+6.83%** | 38.46 CAD | 1,212,013 | $5.77B | none | Reported strong Q2 fiscal 2027 results and raised its FY2027 guidance (release before the open, 12 Nov); CIBC maintained Outperform with a C$40.00 target (GlobeNewswire via Yahoo Finance, 12 Nov; Globe and Mail analyst notes, 12 Nov) |
| `TSX:DSV` | Discovery Mining Ltd. | **-6.59%** | 9.93 CAD | 2,210,777 | $6.07B | OTC | No company-specific release was found for 12 November; it fell with the Canadian gold and copper explorers as spot gold dropped almost 3% to a more-than-one-year low (Reuters, 12 Nov) |
| `TSX:CS` | Capstone Copper Corp. | **-6.53%** | 10.74 CAD | 6,168,368 | $6.18B | OTC | Fell with the Canadian materials sector (-1.8%) as gold dropped almost 3% and copper weakened; the company published an operations update before the open on 12 November (Reuters, 12 Nov; Stockwatch news feed, 12 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:OBCK` | Ottobock SE & Co. KGaA | **-16.60%** | 39.2 EUR | 491,957 | $3.33B | none | Q3 beat on the numbers - core revenue +9% to EUR 433m, adjusted EBITDA +~14% to EUR 120.1m (margin 27.7%), net profit EUR 47.8m, +80% y/y, FY guidance confirmed - but management warned that reimbursement conditions in several core markets are tougher and expected that to continue into Q4; the shares hit a record low of EUR 39.20 (dpa-AFX, 12 Nov) |
| `XETR:WAC` | Wacker Neuson SE | **-10.04%** | 20.6 EUR | 147,219 | $1.74B | OTC | Q3 revenue EUR 589.7m (+7%) and EBIT EUR 45.6m (margin 7.7%), but the full-year EBIT-margin target was cut to 7.0-7.5% from 7.0-8.0% on a subdued market and Q3 one-offs; the shares fell to a three-month low (dpa-AFX, 12 Nov; Investing.com earnings-call transcript, 12 Nov) |
| `XETR:DMP` | Dermapharm Holding SE | **-9.46%** | 34.95 EUR | 116,463 | $2.12B | none | Published its nine-month/Q3 results on 12 November - strong branded-pharmaceuticals growth, but an earnings dip (Dermapharm EQS release, 12 Nov) - and the shares fell 9.46% (Investing.com, 12 Nov) |

### eu-fr

No name cleared the ±5% threshold with a sourced driver in this region; its largest liquid mover is published under `## No catalyst`.

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:ENAV` | ENAV S.p.A. | **+5.37%** | 5.59 EUR | 1,650,330 | $3.18B | none | 9M 2026 results: traffic growth drove EBITDA +18% and the company upgraded its full-year guidance; the shares traded near their 52-week high of EUR 5.64 (Investing.com, 12 Nov) |

### eu-es

No name cleared the ±5% threshold with a sourced driver in this region; its largest liquid mover is published under `## No catalyst`.

### eu-nl

No name cleared the ±5% threshold with a sourced driver in this region; its largest liquid mover is published under `## No catalyst`.

### eu-be

No name cleared the ±5% threshold with a sourced driver in this region; its largest liquid mover is published under `## No catalyst`.

### eu-at

No name cleared the ±5% threshold with a sourced driver in this region; its largest liquid mover is published under `## No catalyst`.

### eu-pt

No name cleared the ±5% threshold with a sourced driver in this region; its largest liquid mover is published under `## No catalyst`.

### eu-ie

No name cleared the ±5% threshold with a sourced driver in this region; its largest liquid mover is published under `## No catalyst`.

### eu-fi

No name cleared the ±5% threshold with a sourced driver in this region; its largest liquid mover is published under `## No catalyst`.

### eu-dk

No name cleared the ±5% threshold with a sourced driver in this region; its largest liquid mover is published under `## No catalyst`.

### eu-gr

No name cleared the ±5% threshold with a sourced driver in this region; its largest liquid mover is published under `## No catalyst`.

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) — published, because a +300% or a -80% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:HE8 | Helios Energy Ltd | **+100.00%** | 2,048,500 | below the $300M cap floor |
| ASX:VEN | Vintage Energy Ltd. | **+100.00%** | 1,202,590 | below the $300M cap floor |
| ASX:GEM | G8 Education Limited | **+90.00%** | 20,945,635 | below the $300M cap floor |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:264A | Schoo,inc. | **+38.28%** | 2,656,300 | below the $300M cap floor |
| TSE:7603 | Gyet Co.Ltd. | **-29.27%** | 9,648,500 | below the $300M cap floor |
| TSE:2693 | YKT Corporation | **+28.51%** | 1,640,200 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:6555 | Long Time Technology Co., Ltd. | **-14.24%** | 816,544 | below the $200M cap floor |
| TPEX:2741 | Renjie Oldsichuan Catering Management Consultant Co., Ltd. | **+14.06%** | 605,777 | below the $200M cap floor |
| TPEX:6827 | MegaPro Biomedical Co., Ltd. | **+11.76%** | 1,611,139 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSXV:HXC.H | HFX Holding Corp. | **+300.00%** | 1,000 | below the $200M cap floor |
| CSE:VLAB | VESALIUS LONGEVITY LABS INC | **+262.75%** | 134,500 | below the $200M cap floor |
| NEO:CISC | Ciscom Corp. | **+180.00%** | 38,000 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| LSX:A1A6WB | Path2 Hydrogen AG | **+337.50%** | 300 | below the $300M cap floor |
| GETTEX:GGS | Gigaset AG | **+114.29%** | 20,991 | below the $300M cap floor |
| LSX:A2QDNX | CCS Abwicklungs AG | **-80.00%** | 75 | below the $300M cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALALO | Acheter-Louer.fr SA | **-99.99%** | 28 | below the $100M cap floor |
| EURONEXT:MLAEM | Ashler et Manson SA | **+21.26%** | 120 | below the $100M cap floor |
| EURONEXT:JBOG | Jacques Bogart SA | **+18.86%** | 16,079 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:ENY | Energy SpA | **+19.05%** | 254,500 | below the $100M cap floor |
| MIL:BWZ | Beewize S.p.A. | **-15.38%** | 2,782 | below the $100M cap floor |
| MIL:GML | G.M. Leather S.P.A. | **-14.29%** | 133,000 | below the $100M cap floor |

### eu-es

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| BME:VANA | Vanadi Coffee SA | **-9.68%** | 2,809,238 | below the $100M cap floor |
| BME:CITY | Club De Futbol Intercity SAD | **-6.57%** | 10,481,199 | below the $100M cap floor |
| BME:LLYC | Llorente & Cuenca SA | **-6.36%** | 6,642 | below the $100M cap floor |

### eu-nl

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:NEDSE | MKB NedSense N.V. | **+10.00%** | 81,656 | below the $100M cap floor |
| EURONEXT:BEVER | N.V. Bever Holding | **-7.14%** | 100 | below the $100M cap floor |

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:CLEX | Cumulex N.V. | **+27.27%** | 5 | below the $100M cap floor |
| EURONEXT:MLTV | CHOICE NV | **-16.03%** | 4,912 | below the $100M cap floor |
| EURONEXT:MONNI | MONNI | **+9.93%** | 70 | below the $100M cap floor |

### eu-at

No below-floor name moved more than 5% in this region.

### eu-pt

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ESON | ESTORIL-SOL, SGPS, S.A. | **+19.85%** | 30 | below the $50M cap floor |

### eu-ie

No below-floor name moved more than 5% in this region.

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:EAGLE | Eagle Filters Group Plc Class A | **-14.73%** | 689,237 | below the $100M cap floor |
| OMXHEX:NETUM | Netum Group Oyj | **+12.25%** | 10 | below the $100M cap floor |
| OMXHEX:SIILI | Siili Solutions Oy | **+11.76%** | 19,782 | below the $100M cap floor |

### eu-dk

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXCOP:ESG | Ennogie Solar Group A/S | **+25.11%** | 228,426 | below the $100M cap floor |
| OMXCOP:UNLGRP | Unlimit Group A/S | **+13.79%** | 820,000 | below the $100M cap floor |
| OMXCOP:FASTPC | FastPassCorp A/S | **-9.50%** | 54 | below the $100M cap floor |

### eu-gr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ATHEX:REVOIL | REVOIL Petroleum Company SA | **+7.39%** | 93,835 | below the $50M cap floor |
| ATHEX:ELBE | ELVE S.A. | **+6.20%** | 414 | below the $50M cap floor |

## No catalyst

Names that moved with **no sourced driver** — no company release, no filing, no analyst action, and no sourced sector or macro move behind them. Kept separate so they do not dilute the mover table. Regions marked *fallback* had no name that cleared the ±5% threshold with a sourced driver, so their largest liquid mover is published here instead.

### au

No liquid mover in this region lacked a sourced driver.

### jp

No liquid mover in this region lacked a sourced driver.

### tw

No liquid mover in this region lacked a sourced driver.

### ca

No liquid mover in this region lacked a sourced driver.

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `XETR:TKMS` | TKMS AG & Co. KGaA | **-5.08%** | 76.6 EUR | 191,682 | $5.68B | OTC | No company-specific release was found for 12 November; the stock fell with the German de-risking (Dax +0.41% on strong earnings) while the healthcare and distribution complex lagged  |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:RNO` | Renault SA | **-3.68%** | 28.23 EUR | 2,551,777 | $9.41B | none | No company-specific release was found for 12 November; the largest liquid mover in France on a session where the CAC 40 added 0.34% on easing oil prices fallback — largest liquid mover |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `MIL:REY` | Reply S.p.A. | **+5.54%** | 139.1 EUR | 196,342 | $5.44B | none | No company-specific release was found for 12 November; the largest liquid mover in Italy on a session where the FTSE MIB closed -0.27%  |
| `MIL:AMP` | Amplifon SpA | **-5.29%** | 11.54 EUR | 2,837,505 | $3.65B | OTC | No price-sensitive release before the Milan close - the EUR 600m five-year bond placement was announced at 19:00 CET, after the close; the stock fell with the Italian healthcare complex  |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `BME:ENO` | Elecnor S.A. | **+3.19%** | 32.3 EUR | 243,556 | $2.94B | none | No company-specific release was found for 12 November; the largest liquid mover in Spain on a session where the IBEX 35 slipped 0.31% and autos and basic resources lagged fallback — largest liquid mover |

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:RAND` | Randstad NV | **+3.72%** | 42.67 EUR | 422,361 | $8.02B | OTC | No company-specific release was found for 12 November; the largest liquid mover in the Netherlands on a session where the AEX fell 0.44% fallback — largest liquid mover |

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:KBC` | KBC Group N.V. | **-4.34%** | 115.6 EUR | 932,150 | $55.93B | OTC | No company-specific release was found for 12 November; the largest liquid mover in Belgium, where the BEL 20 added 0.24% fallback — largest liquid mover |

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `VIE:WIE` | Wienerberger AG | **-4.77%** | 16.38 EUR | 789,305 | $2.08B | OTC | No company-specific release was found for 12 November; the largest liquid mover in Austria, where the ATX fell 0.79% fallback — largest liquid mover |

### eu-pt

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:SON` | Sonae SGPS SA | **+0.88%** | 2.285 EUR | 3,053,960 | $5.02B | OTC | No company-specific release was found for 12 November; the largest liquid mover in Portugal, where the PSI 20 was flat at +0.02% fallback — largest liquid mover |

### eu-ie

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:KRZ` | Kerry Group PLC | **+1.46%** | 100.7 EUR | 416,659 | $17.32B | OTC | No company-specific release was found for 12 November; the largest liquid mover in Ireland, where the ISEQ slipped 0.16% fallback — largest liquid mover |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `OMXHEX:IQMX` | IQM Quantum Computers Oyj Class A | **-2.97%** | 6.54 EUR | 129,232 | $1.42B | ADR | No company-specific release was found for 12 November; the largest liquid mover in Finland, where the OMX Helsinki 25 added 0.22% fallback — largest liquid mover |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `OMXCOP:DEMANT` | Demant A/S | **-8.32%** | 339.4 DKK | 1,140,177 | $11.25B | none | No company-specific release was found for 12 November; the stock gave back ground after Wednesday's strong Q3 (revenue +21% to DKK 6.62bn, FY guidance 7-8% organic growth and DKK 4.7-5.0bn EBIT raised on 9 October) and drifted from DKK 351.20 at 14:35 CET to close at DKK 339.40  |
| `OMXCOP:FLS` | FLSmidth & Co. A/S | **-5.55%** | 570.5 DKK | 517,909 | $5.09B | OTC | No company-specific release was found for 12 November; it gave back the 3.39% it gained on Wednesday's strong Q3 (order intake +36% to DKK 4.5bn, revenue +10% to DKK 3.8bn, 2026 organic revenue guidance narrowed to 1-3%)  |

### eu-gr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `ATHEX:ELHA` | ELVALHALCOR Hellenic Copper and Aluminium Industry S.A. | **+4.77%** | 3.625 EUR | 1,405,416 | $1.66B | none | No company-specific release was found for 12 November; the largest liquid mover in Athens, where the ATHEX General fell 0.59% and sellers were in control from 11:55 to the close fallback — largest liquid mover |

## Method, source health & caveats

### Method

- **Universe** — one TradingView per-country scanner pull per region (`POST https://scanner.tradingview.com/{country}/scan`), filtered on the scanner's `country` column (the ISSUER's country, not the venue) with `symbols.query.types = ["stock"]`. Every pull is set-verified: the distinct symbols returned equal `totalCount`, and pages are pulled sorted by `name` so a page can never overlap another. No pull was truncated; no region was skipped.
- **Venue collapse** — the same line quoted on several venues (a German name on XETR, FWB, GETTEX, LSX and LS; a Canadian name on TSX, TSXV, NEO and CSE) is collapsed to one line per issuer and share class, keeping the highest-priority venue (XETR > FWB > GETTEX > LSX > LS; TSX > TSXV > NEO > CSE; TSE > SAPSE > NAG > FSE; TWSE > TPEX).
- **Floors** — USD floors applied after conversion: au $300M + volume ≥ 100,000; jp $300M; tw $200M; ca $200M; eu-de $300M + volume ≥ 50,000; eu-fr/eu-it/eu-es/eu-nl/eu-be/eu-at $100M; eu-ie $200M; eu-fi/eu-dk $100M; eu-pt/eu-gr $50M.
- **FX and the conversion direction** — FX is **local units per 1 USD**, so the conversion is a **division**: `usd_cap = market_cap_basic / FX[listing_currency]`. Frankfurter (ECB) for EUR, JPY, AUD, CAD and DKK, dated 2026-11-12; open.er-api for TWD, dated Thu, 12 Nov 2026 00:02:31 +0000. Rates used: EUR 0.90245, JPY 159.7, AUD 1.4661, CAD 1.4249, DKK 6.7461, TWD 32.880042. TradingView's `market_cap_basic` is in the LISTING currency, so it is divided, not multiplied.
- **Cap carrier rule** — the cap belongs to the issuer. Rows are grouped by (venue, ticker root); the group's primary line is its `common` line, the conversion is applied ONCE to the primary's `market_cap_basic` using the PRIMARY's currency, and every line of that issuer publishes that one USD figure with `cap_source_symbol` set to the primary's ticker. A group with no `common` line has no primary and is excluded with reason `issuer_unresolved` (190 rows); a carried cap is asserted to land on the same issuer, and a mismatch would drop the group as `cap_issuer_mismatch` (0 rows this session). The floor is applied to the group, so a published row never points at a `cap_source_symbol` that is not in the file.
- **Share class** — derived from the ticker suffix and the description, never from the scanner's `type` column (which reads `stock` for common and preferred lines alike): `.PR`/`.PF`/`.P` and 'pfd'/'preferred' descriptions are `preferred`, `.UN`/`.U` and trust-unit descriptions are `unit`, everything else is `common`. A preferred line carries the issuer's company-level cap and never outranks the common line.
- **Venue-official price rule** — where a venue's own close is available it wins and the third-party reading is published beside it with the delta. Four index rows carry a third-party difference: the Nikkei (official 60,819.36 per Kyodo News and Yahoo's 1-hour final bar; the TradingView venue index read 60,819.14) and the ATHEX (official 2,640.52 per Euronext Athens' own index page and euro2day's 17:37 close report; the TradingEconomics CFD read of 2,652.81 is a third-party quote). The remaining 15 index rows are the TradingView venue index cross-checked against Yahoo's chart API, and agree to the decimal. No single-stock row carries a `price_conflict`: the scanner's venue close was not cross-checked against a second per-stock source, so no conflict is claimed.
- **Schema** — **18 columns**, unchanged from the 2026-11-11 session: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`. `market_cap` is USD on every row; `open`/`high`/`low`/`close` are in the listing currency named by the `currency` column. Numeric formatting is unchanged from the 11 November session (6 significant figures, integers for volume and cap).
- **Files written** — 16 region CSVs (`<region>.csv`), `summary.md`, `_manifest.json`, `_excluded.json` and `_carryover.json`, all under `international-eod/2026-11-12/`. **4,380 rows written**, 8,871 excluded with a reason, 84 carry-over rows.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView country scanners (16) | `POST https://scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan`, filter `country == <issuer country>`, types `stock`, sorted by `name` | ok | 16/16 set-verified: distinct symbols = `totalCount` in every region (au 1,543; jp 3,899; tw 2,337; ca 4,293; de 4,300; fr 542; it 378; es 233; nl 78; be 101; at 65; pt 31; ie 19; fi 188; dk 134; gr 130) |
| TradingView America scanner | `POST https://scanner.tradingview.com/america/scan`, types `stock` + `dr` | ok | 13,573 rows, 13,573 distinct — used for `us_listing` (1,210 OTC, 231 NYSE, 32 NASDAQ, 45 ADR) and for the cross-venue cap second reading |
| TradingView symbol endpoint (18 index symbols) | `GET https://scanner.tradingview.com/symbol?symbol=<VENUE:INDEX>&fields=close,change,change_abs` | ok | 17 of 18 returned a level; `TWSE:TWII` returns null, so Taiwan was taken from `TWSE:IX0001` (the TSEC capitalisation-weighted index, which is the TAIEX) |
| Yahoo chart API (index cross-check) | `GET https://query1.finance.yahoo.com/v8/finance/chart/{^AXJO,^N225,^TWII,^GSPTSE,^GDAXI,^FCHI,FTSEMIB.MI,^IBEX,^AEX,^BFX,^ATX,PSI20.LS,^ISEQ,^OMXH25,^OMXC20,^STOXX}` | ok | 15 symbols returned a 12 Nov bar and agree with the venue index to the decimal; `^OMXC20` needed a 1-hour interval (its daily bar had not settled) and `^N225`/`^TWII` resolved through the 1-hour series because their daily bars had not yet published |
| Frankfurter (ECB) | `GET https://api.frankfurter.app/latest?from=USD&to=EUR,JPY,AUD,CAD,DKK` | ok | dated 2026-11-12; EUR 0.90245, JPY 159.7, AUD 1.4661, CAD 1.4249, DKK 6.7461 (local per USD) |
| open.er-api | `GET https://open.er-api.com/v6/latest/USD` | ok | TWD 32.880042 (local per USD), updated 12 Nov 2026 00:02:31 UTC |
| Yahoo daily bar for ^TWII | `GET .../v8/finance/chart/%5ETWII?range=5d&interval=1d` | degraded | the daily series still carried the 11 Nov bar (44,257.15) at run time; the session close was taken from the 1-hour series (43,091.87), which matches the TradingView venue index to the decimal |
| Catalyst research | `web_search` on the wire and IR record for each mover (CNA, Reuters, RTTNews, dpa-AFX, Kabutan, Fisco Japan, Euro2day, Euronext Athens, Samso, Baystreet, GlobeNewswire, dpa/AFX round-ups, company IR) | ok | every Top-movers row carries a dated, sourced driver; 14 rows found no driver and are published under `## No catalyst` |

### Caveats

- **Carry-over rows: 84 rows did not trade today** (ca 40, es 28, it 5, fr 3, gr 2, tw 2, au 1, at 1, be 1, pt 1). They are written as the source returned them — the scanner's last close and change — and are flagged in `_carryover.json` with each instrument's `last_trade_date`, which walks back through the prior files and never forward. They are excluded from every movers list and from the breadth table.
- **The Spain universe shrank by 44 lines since the 11 November session** (277 → 233): the BME `SC*` series (rights, warrants and similar lines such as `BME:SCALF`, `BME:SCAP7`, `BME:SCHLR`, `BME:YIRG`) and `BME:EEP`/`BME:ISE` are no longer returned by the scanner under `types = ["stock"]`, and they are not present in the scanner at all under any instrument type. This is a source-side reclassification, not a market event, and it is why Spain's written row count is 137 today against 146 on 11 November.
- **Three lines that were published on 11 November are absent from today's scanner pull** — `EURONEXT:ALPG`, `EURONEXT:BLEE` (France) and `MIL:BF` (Italy) — and three of the eight names dropped from the published Spanish file were `SC*`/`Y*` lines. No close, cap or catalyst is published for them.
- **Every close in the CSVs is the TradingView scanner's venue close**, not a venue-auction print cross-checked per stock. Only the 16 index rows were cross-checked against a second source. A row's `price_conflict` cell is therefore empty throughout: an unverified conflict is not a conflict.
- **`market_cap` is the scanner's company-level figure carried to the issuer's primary line and converted once.** It is a *vendor* cap: `market_cap_basic / close` returns the issuer's share count on the published price basis, but the vendor's caps are coarse, so the file does not support cap-weighted sector aggregates without deduplicating on `cap_source_symbol` first.
- **Volume gates are applied per line, and a group's volume failure removes the whole group**, so a preferred line is never published on a cap whose primary line failed the region's volume gate. The 328 below-volume exclusions are concentrated in Germany (309), where the Xetra line's volume is the binding field.
- **`pe_ratio` and `sector` come from the scanner's own columns** and are blank where the source does not carry them; no third-party enrichment was merged into these files.
- **Catalyst attribution is a research product, not a feed.** Every Top-movers row names its source and date, but a sourced driver is not proof of causation: where the driver is a sector or macro move rather than a company release, the row says so explicitly.
