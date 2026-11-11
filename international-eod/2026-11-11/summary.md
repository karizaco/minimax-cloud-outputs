# Cron #05 eod-international-daily — Wednesday, 11 November 2026

## TL;DR

- **Fifteen of the sixteen regions closed higher, and the tape was one story: CoreWeave's post-close AI numbers revived the AI complex overnight, so every market that carries chip or equipment names bid, and the ones that do not merely followed.** **4,380 instruments printed across the 16 regions** - Taiwan led the world (**TAIEX +3.62%** to 44,257.15, its sixth-largest point gain ever, on TSMC +4.81%), Tokyo followed (**Nikkei +1.31%** to 61,248.52, a third straight gain), and Europe closed near a record (**STOXX 600 +0.72%** to 663.05, **DAX +1.20%**, **CAC 40 +0.66%**); Australia (+0.27%) and Canada (+0.67%) were the laggards, and Belgium (-0.07%) was the only index lower.
- **The most consequential move was the AI-equipment complex, and the names a US trader can actually reach are the US depositary receipts: Soitec +11.93% (EURONEXT:SOI), Siemens Energy +10.78% (XETR:ENR, OTC), Hamamatsu Photonics +14.66% (TSE:6965, OTC), AIXTRON +8.00% (XETR:AIXA, OTC), ASM International +6.97% and BE Semiconductor +5.94% (both OTC), AT&S +11.88% (VIE:ATS, OTC), Global Unichip +9.97% (TWSE:3443) and ChipMOS +9.98% (TWSE:8150, ADR) - with TSMC +4.81% adding about 880 points to the Taiex on its record NT$9 dividend and October sales up almost 60% y/y.** The one genuinely company-specific story was **Seiko Group -11.00% (TSE:8050)**: operating profit +86.5% and guidance raised to Y47.0bn, but below the market's Y50bn consensus.
- **Read the numbers with the unit convention in mind: `market_cap` is USD while every price is in the listing currency** (the `currency` column says which) - a Y3,075 close and a C$38.67 close are not comparable, the caps are. **And read the tape with two caveats: the rally is an AI-narrow bid rather than a broad one** (Belgium closed lower, the Milan banks fell and European defence names stayed under pressure - Rheinmetall -6.94%), **and every close here is the scanner's venue close, with carry-over rows included as the source returned them.** This file carries **18 columns**, unchanged from the 10 November session.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,543 | 1,543 | **301** | $300M + vol ≥ 100,000 | 3 | 1217 | 20 | 2 | 0 | 1 | 0 |
| `jp` | FSE, NAG, SAPSE, TSE | 3,900 | 3,868 | **1,380** | $300M | 2 | 2483 | 0 | 3 | 0 | 1 | 0 |
| `tw` | TPEX, TWSE | 2,336 | 2,336 | **879** | $200M | 55 | 1400 | 0 | 2 | 0 | 3 | 0 |
| `ca` | CSE, NEO, TSX, TSXV | 4,298 | 2,683 | **631** | $200M | 33 | 1860 | 0 | 159 | 0 | 31 | 0 |
| `eu-de` | FWB, GETTEX, LS, LSX, XETR | 4,298 | 927 | **116** | $300M + vol ≥ 50,000 | 4 | 466 | 315 | 26 | 0 | 0 | 0 |
| `eu-fr` | EURONEXT | 545 | 545 | **259** | $100M | 1 | 285 | 0 | 0 | 0 | 6 | 0 |
| `eu-it` | MIL | 392 | 392 | **182** | $100M | 2 | 208 | 0 | 0 | 0 | 5 | 0 |
| `eu-es` | BME | 277 | 277 | **146** | $100M | 36 | 95 | 0 | 0 | 0 | 35 | 0 |
| `eu-nl` | EURONEXT | 78 | 78 | **56** | $100M | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| `eu-be` | EURONEXT | 101 | 101 | **76** | $100M | 1 | 24 | 0 | 0 | 0 | 2 | 0 |
| `eu-at` | VIE | 65 | 65 | **50** | $100M | 3 | 12 | 0 | 0 | 0 | 2 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **28** | $50M | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| `eu-fi` | OMXHEX | 188 | 188 | **101** | $100M | 4 | 83 | 0 | 0 | 0 | 0 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 58 | 0 | 0 | 0 | 0 | 0 |
| `eu-gr` | ATHEX | 130 | 130 | **83** | $50M | 0 | 45 | 0 | 2 | 0 | 2 | 0 |
| **total** | | **18,335** | **13,317** | **4,380** | | **145** | **8263** | **335** | **194** | **0** | **88** | **0** |

`Universe` is every instrument the source returns for that country's own listings (the scanner's issuer-country filter, so a foreign company's local line is not counted); `Unique instruments` collapses the same line quoted on several venues down to one line per issuer and share class; `Written` applies the per-region USD market-cap floor plus the region's volume gate. Every excluded row carries a reason from the closed set in `_excluded.json`, and the counts above are read from that file rather than estimated.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 9,153.20 | +24.20 / +0.27% | 2026-11-11 | Samso market update, 11 Nov (4:30pm AEDT): 9,153.2, up 24.2 points; the TradingView SP:XJO venue index agrees to the decimal |
| jp | Nikkei 225 | 61,248.52 | +789.16 / +1.31% | 2026-11-11 | Reuters Japan market wrap and the Tokyo Market Summary, 11 Nov: up 789 yen to 61,248; the TradingView TVC:NI225 venue index agrees |
| jp | TOPIX | 3,929.39 | +35.68 / +0.92% | 2026-11-11 | TradingView TSE:TOPIX venue index, 11 Nov |
| tw | TAIEX | 44,257.15 | +1,545.23 / +3.62% | 2026-11-11 | CNA / Focus Taiwan and the TWSE daily board, 11 Nov: +1,545.23 points to 44,257.15, the day's high and the sixth-largest point gain in index history; Taiwan News, 11 Nov |
| ca | S&P/TSX Composite | 36,411.72 | +241.27 / +0.67% | 2026-11-11 | TradingView TSX:TSX venue index, 11 Nov; Reuters had it at 36,363.05 (+0.53%) at 10:44 ET, so the published level is the venue close |
| eu-de | DAX (Xetra) | 26,662.77 | +315.32 / +1.20% | 2026-11-11 | RTTNews European close, 11 Nov: +315.32 points or 1.20% to 26,662.77; the TradingView XETR:DAX venue index agrees |
| eu-fr | CAC 40 | 8,332.87 | +54.28 / +0.66% | 2026-11-11 | RTTNews European close, 11 Nov: +54.28 points or 0.66%; Sharecast and the TradingView EURONEXT:PX1 venue index agree |
| eu-it | FTSE MIB | 51,946.54 | +191.46 / +0.37% | 2026-11-11 | Il Sole 24 Ore Radiocor European close, 11 Nov: Milan +0.4% at the close; the TradingView FTSE:FTSEMIB venue index agrees |
| eu-es | IBEX 35 | 20,027.90 | +91.50 / +0.46% | 2026-11-11 | TradingView BME:IBC venue index, 11 Nov; no wire close was available for the session |
| eu-nl | AEX | 1,145.14 | +12.70 / +1.12% | 2026-11-11 | TradingView EURONEXT:AEX venue index, 11 Nov |
| eu-be | BEL 20 | 6,100.48 | -4.55 / -0.07% | 2026-11-11 | TradingView EURONEXT:BEL20 venue index, 11 Nov |
| eu-at | ATX | 6,738.85 | +88.30 / +1.33% | 2026-11-11 | TradingView VIE:ATX venue index, 11 Nov |
| eu-pt | PSI 20 | 9,594.51 | +46.05 / +0.48% | 2026-11-11 | TradingView EURONEXT:PSI20 venue index, 11 Nov |
| eu-ie | ISEQ | 15,035.08 | +9.22 / +0.06% | 2026-11-11 | TradingView EURONEXT:ISEQ venue index, 11 Nov |
| eu-fi | OMX Helsinki 25 | 6,327.98 | +45.50 / +0.72% | 2026-11-11 | TradingView OMXHEX:OMXH25 venue index, 11 Nov |
| eu-dk | OMX Copenhagen 20 | 1,660.29 | +5.49 / +0.33% | 2026-11-11 | TradingView OMXCOP:OMXC20 venue index, 11 Nov |
| eu-gr | ATHEX General | 2,656.13 | +14.06 / +0.53% | 2026-11-11 | TradingView ATHEX:GD venue index, 11 Nov; there is no Yahoo symbol for the ATHEX |
| *context* | STOXX 600 | 663.05 | +4.73 / +0.72% | 2026-11-11 | Sharecast and FourWeekMBA, 11 Nov: 663.05, +0.7%, a 12-month closing high; the TradingView STOXX:SXXP venue index agrees to the decimal |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 300 | +0.41% | 176 / 103 / 21 | -5.04% | +16.29% |
| jp | 1,379 | +0.17% | 725 / 628 / 26 | -13.25% | +21.77% |
| tw | 876 | +0.95% | 566 / 256 / 54 | -10.00% | +31.35% |
| ca | 600 | +0.08% | 314 / 257 / 29 | -16.35% | +13.00% |
| eu-de | 116 | +0.24% | 64 / 50 / 2 | -8.08% | +17.93% |
| eu-fr | 253 | +0.22% | 142 / 83 / 28 | -10.40% | +11.93% |
| eu-it | 177 | +0.13% | 92 / 73 / 12 | -22.27% | +7.73% |
| eu-es | 111 | +0.00% | 53 / 47 / 11 | -11.87% | +5.26% |
| eu-nl | 56 | +0.24% | 32 / 21 / 3 | -8.96% | +6.97% |
| eu-be | 74 | +0.00% | 35 / 25 / 14 | -1.97% | +5.24% |
| eu-at | 48 | +0.40% | 28 / 13 / 7 | -7.65% | +11.88% |
| eu-pt | 28 | -0.13% | 7 / 15 / 6 | -6.52% | +9.77% |
| eu-ie | 17 | +0.10% | 9 / 6 / 2 | -2.29% | +2.37% |
| eu-fi | 101 | +0.54% | 63 / 34 / 4 | -4.23% | +11.19% |
| eu-dk | 75 | +0.22% | 41 / 28 / 6 | -3.80% | +6.00% |
| eu-gr | 81 | +0.00% | 40 / 26 / 15 | -3.26% | +6.62% |

**One story, one catalyst.** CoreWeave reported a 168% jump in quarterly revenue after Tuesday's close and said it would be adjusted-profitable in the first half of 2028, and the AI complex bid everywhere: Europe's chip and equipment names closed a median +5.9% against the STOXX 600's +0.7% (roughly eight times the index), Taiwan's electronics index rose 3.98% on TSMC's record NT$9 dividend and October sales up almost 60% y/y, and Tokyo's AI-linked names led the Nikkei to a third straight gain. The second force was **macro**: German October inflation slowed to 2.8% y/y from 3.3%, below consensus, while Tuesday's hotter US CPI cemented a December Fed hike, sent the dollar to a four-week high and lifted Brent about 1% to around $92.5 on fresh Strait of Hormuz shipping attacks; gold bounced 0.4% to $4,047/oz after a 2.6% slide. The two exceptions were sharp: **Seiko Group -11.00%** on a guidance raise that missed consensus, and **voestalpine -7.65%** on an EBITDA guidance trim despite a 46% jump in first-half profit.

## Top movers

Liquid names (volume ≥ 100,000 **and** market cap ≥ $1B) whose move cleared ±5%, capped at the six largest absolute moves per region, with the driver that was actually sourced. Where a region had no such name, its largest liquid mover is published instead and marked. A row with no sourced driver is not here - it is under `## No catalyst`.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:SRL` | Sunrise Energy Metals Limited | **+7.69%** | 14 AUD | 476,087 | $1.54B | OTC | No company-specific release found - Sunrise Energy Metals has lodged no ASX announcement since 10 November (its latest is the Agni Semiconductor investment progress report) and it rose with the battery-materials and resources complex on the ASX's third straight gain (Samso market update, 11 Nov; FN Arena ASX winners/losers, 11 Nov) |
| `ASX:MND` | Monadelphous Group Limited | **+7.23%** | 34.99 AUD | 544,855 | $2.25B | none | Monadelphous continued Tuesday's move on its H1 FY27 guidance (revenue of about A$1.7bn and net profit after tax of A$80-85m) - the shares rose 15.30% on that release on 10 November and added 7.23% today with no new ASX announcement lodged (Samso market update, 11 Nov; The West Australian, 10 Nov) |
| `ASX:PLS` | PLS Group Limited | **+6.53%** | 3.1 AUD | 32,327,566 | $6.44B | none | No company-specific release found - the only ASX announcement since Tuesday afternoon was a change in substantial holding notice; PLS rose with the lithium and resources complex as the ASX 200 closed a third session higher (Samso market update, 11 Nov) |
| `ASX:NWH` | NRW Holdings Limited | **+6.47%** | 6.91 AUD | 2,012,239 | $2.05B | none | NRW's subsidiary Fredon was awarded an electrical-services contract worth about A$240m by Shape for a data-centre project, announced before the open (Samso market update, 11 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:1980` | DAI-DAN Co., Ltd. | **+15.13%** | 3075 JPY | 2,415,600 | $2.29B | none | H1 FY3/27 profit up: net income Y16.362bn (from Y12.520bn), EPS Y126.39, revenue Y126.844bn +7.2%, FY guidance EPS Y231.73 and revenue Y265.0bn; the board also approved a Y10bn buyback of up to 6,000,000 shares (4.63% of capital) (RTTNews, 11 Nov; Simply Wall St, 11 Nov) |
| `TSE:6965` | Hamamatsu Photonics K.K. | **+14.66%** | 2357.5 JPY | 7,711,700 | $3.99B | OTC | FY9/2027 operating-profit guidance of Y320.0bn (+17.7% y/y) with the annual dividend forecast raised to Y40; H1 operating profit came in at Y271.8bn, +68.2% y/y (Trader's Web / Minkabu, 11 Nov; Investing.com TOPX1000 gainers, 11 Nov) |
| `TSE:6890` | Ferrotec Corporation | **+11.49%** | 7617 JPY | 2,681,600 | $2.32B | none | No company-specific release found - Ferrotec rose with the Tokyo semiconductor and AI complex, opening up 460 yen before paring back the gain (Investing.com TOPX1000 gainers, 11 Nov; moomoo Ferrotec news flow, 11 Nov) |
| `TSE:8050` | SEIKO GROUP CORPORATION | **-11.00%** | 8759 JPY | 2,450,800 | $5.11B | none | Sell-the-news on the H1 print: operating profit Y31.429bn (+86.5% y/y) and FY guidance raised to Y47.0bn, but below the market's Y50bn consensus, with weak overseas wholesale cited as the main cause; the shares hit the daily lower limit (Jiji Press, 11 Nov; Shikiho Toyo Keizai, 11 Nov; Seiko Group IR, 10-11 Nov) |
| `TSE:4680` | ROUND ONE Corporation | **+10.89%** | 1466 JPY | 6,205,800 | $2.40B | OTC | No company-specific release found - Round One rose with the Tokyo growth and AI complex on the Nikkei's third straight gain (Investing.com TOPX1000 gainers, 11 Nov; Reuters Japan market wrap, 11 Nov) |
| `TSE:3569` | Seiren Co., Ltd. | **+10.36%** | 3515 JPY | 417,300 | $1.07B | none | No company-specific release found - Seiren rose with the Tokyo AI-linked complex; the day's top-gainer ranking was led by the AI/electronics names (Investing.com TOPX1000 gainers, 11 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TWSE:3026` | Holy Stone Enterprise Co., Ltd. | **+10.00%** | 561 TWD | 20,244,200 | $2.57B | none | Limit-up with the passive-component makers - Holy Stone and Viking Tech both closed at the daily limit in the electronics rally (Taiwan News, 11 Nov) |
| `TWSE:3167` | Ta Liang Technology Co., Ltd. | **+9.99%** | 881 TWD | 7,577,751 | $2.18B | none | No company-specific release found - Ta Liang Technology closed at the daily limit with the electronics and robotics complex (Taiwan News, 11 Nov) |
| `TPEX:7856` | Hermes Testing Solutions Inc. | **+9.98%** | 2755 TWD | 567,372 | $2.51B | none | No company-specific release found - robotics and electronics names were bought after Apple unveiled HALO, its system for humanoid robots; Taiwan Benefit, Usun, Ying Han and Taiwan Takisawa closed at their limits (Taiwan News, 11 Nov) |
| `TWSE:8150` | ChipMOS Technologies, Inc. | **+9.98%** | 88.2 TWD | 28,436,351 | $1.72B | ADR | ChipMOS rose with the semiconductor complex on TSMC's record NT$9 cash dividend and October sales up almost 60% y/y, which lifted the electronics index 3.98% (CNA / Focus Taiwan, 11 Nov) |
| `TWSE:2466` | Cosmo Electronics Corporation | **+9.97%** | 397 TWD | 3,710,046 | $1.90B | none | No company-specific release found - Cosmo Electronics closed at its daily limit with the electronics group (Taiwan News, 11 Nov) |
| `TWSE:3443` | Global Unichip Corp. | **+9.97%** | 7885 TWD | 2,283,682 | $29.17B | none | Global Unichip rose with the AI ASIC designers - TSMC, more than 40% of the Taiex's market value, gained 4.81% to NT$2,395 and added about 880 points to the index (CNA / Focus Taiwan, 11 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:MAL` | Magellan Aerospace Corporation | **+13.00%** | 38.67 CAD | 287,050 | $1.37B | OTC | TD Securities kept its Buy rating and raised its price target to C$46 from C$45 on Magellan Aerospace (Globe and Mail Canadian analyst updates, 11 Nov) |
| `TSX:BYD` | Boyd Group Services Inc | **-12.22%** | 109.7 CAD | 575,418 | $2.44B | NYSE | Boyd Group missed its third-quarter adjusted profit estimate and the collision-repair operator tumbled (Reuters Canada stocks, 11 Nov) |
| `TSX:CLS` | Celestica Inc. | **+8.38%** | 345.43 CAD | 670,423 | $28.24B | NYSE | CoreWeave-led AI rally - Canadian technology stocks rose 1.8%, with Celestica up 7.5% in early trading (Reuters Canada stocks, 11 Nov) |
| `TSX:KXS` | Kinaxis, Inc. | **+6.37%** | 229.37 CAD | 297,568 | $4.12B | OTC | The TSX accepted Kinaxis' normal course issuer bid for up to 2,698,037 shares, about 10% of the public float, running from 13 Nov 2026 to 12 Nov 2027 (Kinaxis release via Business Wire, 11 Nov; MT Newswires, 11 Nov) |
| `TSX:BDT` | Bird Construction Inc. | **+5.62%** | 76.89 CAD | 482,600 | $2.83B | OTC | Bird Construction reported quarterly results on the day of the move (Motley Fool TSX Today, 11 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:ENR` | Siemens Energy AG | **+10.78%** | 132.76 EUR | 4,476,591 | $112.12B | OTC | Siemens Energy reported record results, raised its 2027 profitability outlook and announced plans to more than triple its dividend (Il Sole 24 Ore Radiocor, 11 Nov; Sharecast Europe close, 11 Nov) |
| `XETR:SMHN` | SUSS MicroTec SE | **+8.79%** | 52 EUR | 124,039 | $1.02B | OTC | No company-specific release found - SUSS MicroTec rose with the semiconductor-equipment complex that followed CoreWeave's results (FourWeekMBA Europe AI names, 11 Nov) |
| `XETR:V1NC` | VINCORION SE | **-8.08%** | 16.72 EUR | 182,515 | $1.01B | none | 9M 2026 results: revenue +41.4% to EUR 237.7m and FY guidance raised to EUR 323-333m, but the adjusted EBIT margin slipped to 19.5% from 20.5% and 9M free cash flow was -EUR 5.5m, and the shares fell on the presentation (EQS ad-hoc, 11 Nov; Investing.com, 11 Nov) |
| `XETR:AIXA` | AIXTRON SE | **+8.00%** | 34.29 EUR | 723,279 | $3.98B | OTC | AI rally read-across from CoreWeave's results - Aixtron rose with the European chip and equipment names (Sharecast Europe close, 11 Nov; Reuters Europe open, 11 Nov) |
| `XETR:WAF` | Siltronic AG | **+7.46%** | 57.65 EUR | 154,872 | $1.97B | OTC | No company-specific release found - Siltronic rose with the wafer and semiconductor complex (STMicroelectronics +4.16%, ASML +3.14% on the day) (FourWeekMBA Europe AI names, 11 Nov; Reuters Europe open, 11 Nov) |
| `XETR:RHM` | Rheinmetall AG | **-6.94%** | 794.1 EUR | 412,223 | $44.30B | OTC | No new company release - Rheinmetall's derating after the 5 November guidance cut continued, with European defence names lower again (Avio and Leonardo more than 1.5% down in Milan) and BofA still at neutral with a EUR 900 target (Il Sole 24 Ore Radiocor, 11 Nov; Reuters, 5 Nov; Investing.com, 9 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:SOI` | Soitec SA | **+11.93%** | 108.35 EUR | 427,383 | $3.86B | none | Soitec rebounded 11.93% to EUR 108.35 on the CoreWeave-led AI rally after a month of heavy liquidation, with BofA turning bullish on silicon-photonics demand and T2 FY27 revenue guided more than 30% higher y/y (ideal-investisseur, 11 Nov; Reuters Europe open, 11 Nov; FourWeekMBA, 11 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:TPRO` | Technoprobe SpA | **+7.73%** | 23.7 EUR | 2,797,026 | $15.67B | OTC | Technoprobe rallied 7.73% to EUR 23.70 on the day of its quarterly results, led the Milan tech rally with STMicroelectronics and Prysmian, and its CEO has been vocal on the AI opportunity (Il Sole 24 Ore Radiocor, 11 Nov; Investing.com, 11 Nov) |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `BME:CAF` | Construcciones y Auxiliar de Ferrocarriles, S.A. | **-11.87%** | 68.3 EUR | 220,654 | $2.96B | none | Q3 2026 results and the board's approval of the 2027-2030 Strategic Plan (to be presented to analysts on 22 December 2026) - the shares sold off about 12% on the read (CNMV relevant information, 10 Nov; company Q3 2026 results release, 10 Nov) |

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ASM` | ASM International N.V. | **+6.97%** | 727.6 EUR | 258,993 | $36.83B | OTC | AI read-across from CoreWeave - ASM International and BE Semiconductor were named among Europe's AI-equipment leaders on the day (Reuters Europe open, 11 Nov; Investing.com, 11 Nov) |
| `EURONEXT:BESI` | BE Semiconductor Industries N.V. | **+5.94%** | 159.75 EUR | 568,630 | $13.55B | OTC | AI read-across from CoreWeave - BE Semiconductor and ASM International both jumped in early European trading (Reuters Europe open, 11 Nov; FourWeekMBA, 11 Nov) |

### eu-be

No liquid name cleared ±5% on the day.

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | **+11.88%** | 126.2 EUR | 155,720 | $4.88B | OTC | AT&S was named among the session's European tech leaders with Soitec, Infineon, ASM International and BE Semiconductor on the CoreWeave AI rally (Sharecast Europe close, 11 Nov; HL, 11 Nov) |
| `VIE:VOE` | voestalpine AG | **-7.65%** | 38.38 EUR | 657,414 | $8.26B | OTC | H1 2026/27: revenue EUR 7.7bn, EBITDA EUR 846m (+17.1%), EBIT EUR 470m (+36%) and net profit EUR 290m (+46%), but the FY EBITDA forecast was cut to EUR 1.60-1.70bn from EUR 1.60-1.85bn on Middle East energy and logistics costs and extra US tariffs (voestalpine ad-hoc, 11 Nov) |

### eu-pt

No liquid name cleared ±5% on the day.

### eu-ie

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:RYA` | Ryanair Holdings PLC | **-2.29%** (the region's largest liquid mover; it did not clear ±5%) | 26 EUR | 1,706,896 | $30.67B | ADR | Ryanair closed at EUR 26.00, down 2.29%, still paying for the 2 November H1 profit fall of 15% to EUR 2.15bn and a EUR 2bn rise in the coming year's fuel bill (Irish Times, 11 Nov; Ryanair H1 release, 2 Nov) |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:NOKIA` | Nokia Oyj | **+4.14%** (the region's largest liquid mover; it did not clear ±5%) | 7.746 EUR | 12,379,955 | $46.84B | OTC | Nokia and NVIDIA announced a strategic partnership (Nokia and NVIDIA announce strategic partnership, 11 Nov); Nokia closed at EUR 7.75, +4.14% |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:FLS` | FLSmidth & Co. A/S | **+5.59%** | 604 DKK | 258,688 | $4.84B | OTC | FLSmidth published its Q3 2026 report on 11 November and closed at DKK 604.00, +5.59% (FLSmidth quarterly report, 11 Nov; FT Markets, 11 Nov) |

### eu-gr

No liquid name cleared ±5% on the day.

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a +300% or a -82% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:MRQ | MRG Metals Limited | **+100.00%** | 119,468 | below the $300M cap floor |
| ASX:ARV | Artemis Resources Limited | **+50.00%** | 547,695 | below the $300M cap floor |
| ASX:ATC | Altech Batteries Limited | **-50.00%** | 1,488,722 | below the $300M cap floor |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:7603 | Gyet Co.Ltd. | **+57.69%** | 39,043,200 | below the $300M cap floor |
| TSE:5129 | FIXER Inc. | **+38.83%** | 6,739,500 | below the $300M cap floor |
| TSE:1810 | Matsui Construction Co., Ltd. | **+21.35%** | 97,900 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:7866 | DLI Memory, Inc. | **+25.00%** | 459,331 | below the $200M cap floor |
| TPEX:7796 | Microip, Inc. | **+20.76%** | 110,080 | below the $200M cap floor |
| TPEX:3473 | Fiber Logic Communications Inc | **+18.88%** | 95,486 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSXV:HXC.H | HFX Holding Corp. | **+300.00%** | 1,000 | below the $200M cap floor |
| CSE:TEMP | Tempus Capital, Inc. | **+114.29%** | 8,150 | below the $200M cap floor |
| CSE:NWI | Nuinsco Resources Limited | **+100.00%** | 4,000 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| GETTEX:ADC | AdCapital AG | **+5900.00%** | 1 | below the $300M cap floor |
| XETR:SNG | SINGULUS TECHNOLOGIES AG | **+108.66%** | 802,706 | below the $300M cap floor |
| XETR:AB9 | ABO Energy GmbH & Co. KGaA | **-81.95%** | 272,207 | below the $300M cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALALO | Acheter-Louer.fr SA | **+999900.00%** | 28 | below the $100M cap floor |
| EURONEXT:ALTOO | Toosla Societe Anonyme | **+100.00%** | 45,073,057 | below the $100M cap floor |
| EURONEXT:ALCLS | Cellectis S.A. | **+28.79%** | 1,607,758 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:GML | G.M. Leather S.P.A. | **-19.23%** | 94,000 | below the $100M cap floor |
| MIL:TMP | Tmp Group S.P.A. | **-11.43%** | 15,800 | below the $100M cap floor |
| MIL:FAE | Fae Technology S.P.A | **+8.23%** | 13,408 | below the $100M cap floor |

### eu-es

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| BME:VANA | Vanadi Coffee SA | **+23.02%** | 16,631,162 | below the $100M cap floor |
| BME:ETC | Energy Solar Tech, S.A. | **-6.67%** | 1,140 | below the $100M cap floor |
| BME:END | Endurance Motive SA | **+5.67%** | 65,060 | below the $100M cap floor |

### eu-nl

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:SIFG | Sif Holding N.V. | **+8.89%** | 235,481 | below the $100M cap floor |
| EURONEXT:BEVER | N.V. Bever Holding | **-7.14%** | 100 | below the $100M cap floor |
| EURONEXT:LVIDE | Lavide Holding N.V. | **+6.67%** | 234 | below the $100M cap floor |

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:CLEX | Cumulex N.V. | **+27.27%** | 5 | below the $100M cap floor |
| EURONEXT:MONNI | MONNI | **+9.93%** | 70 | below the $100M cap floor |
| EURONEXT:MLTV | CHOICE NV | **-9.66%** | 13,737 | below the $100M cap floor |

### eu-at

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| VIE:PYT | POLYTEC HOLDING AG | **+6.97%** | 109,830 | below the $100M cap floor |

### eu-pt

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ESON | ESTORIL-SOL, SGPS, S.A. | **+19.85%** | 30 | below the $50M cap floor |

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:HRTIS | Herantis Pharma Plc | **+15.80%** | 127,908 | below the $100M cap floor |
| OMXHEX:PALLAS | Pallas Air Plc | **-15.66%** | 242 | below the $100M cap floor |
| OMXHEX:MARAS | Martela Oyj Class A | **-9.97%** | 34,093 | below the $100M cap floor |

### eu-dk

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXCOP:MOVINN | Movinn A/S | **+25.00%** | 30,102 | below the $100M cap floor |
| OMXCOP:UNLGRP | Unlimit Group A/S | **-17.14%** | 1,145,000 | below the $100M cap floor |
| OMXCOP:FASTPC | FastPassCorp A/S | **+13.64%** | 70 | below the $100M cap floor |

### eu-gr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ATHEX:ELBE | ELVE S.A. | **+6.20%** | 414 | below the $50M cap floor |

## No catalyst

Names that moved with **no sourced driver** - no company release, no filing, no analyst action and no sourced sector or macro move behind them. Kept separate so they do not dilute the mover table.

### au

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `ASX:AGL` | AGL Energy Limited | **+2.32%** | 9.25 AUD | $4.17B |

### ca

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `CSE:HG` | Hydrograph Clean Power Inc | **+5.53%** | 4.96 CAD | $1.20B |

### eu-be

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `EURONEXT:SYENS` | Syensqo SA/NV | **+3.43%** | 80 EUR | $8.72B |

### eu-pt

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `EURONEXT:EDP` | EDP S.A. | **+1.71%** | 5.058 EUR | $22.87B |

### eu-gr

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `ATHEX:ADMIE` | Admie Holdings SA | **+3.06%** | 4.72 EUR | $1.85B |

The drivers that could not be sourced, per name:

- `ASX:AGL` — No company-specific release found, and no sourced sector or macro move explains the move - AGL Energy is a power and utilities name on a day when the ASX's own sector leaders were technology and resources (Samso market update, 11 Nov; FN Arena ASX winners/losers, 11 Nov)
- `CSE:HG` — No company-specific release found - Hydrograph Clean Power rose with the Canadian growth complex on a day when the TSX's own movers list was dominated by AI-linked technology (Reuters Canada stocks, 11 Nov)
- `EURONEXT:SYENS` — No company-specific release found; Syensqo traded with the Belgian mid-caps on a day when no Belgian name cleared 5% (Il Sole 24 Ore Radiocor European close, 11 Nov)
- `EURONEXT:EDP` — No company-specific release found; EDP traded with the Portuguese large caps as the PSI 20 closed 0.48% higher (Il Sole 24 Ore Radiocor European close, 11 Nov)
- `ATHEX:ADMIE` — No company-specific release found - Admie Holdings traded with the ATHEX energy names as the ATHEX General index closed 0.53% higher (TradingView ATHEX:GD venue index, 11 Nov)

## Method, source health & caveats

### Method

- **Universe** — the TradingView per-country scanner (`POST scanner.tradingview.com/<country>/scan`), issuer-country filtered. The filter is the **top-level** `filter` key (`[{"left":"country","operation":"equal","right":"Germany"}]`): the key inside `symbols` is silently ignored and returns the unfiltered totalCount with no error. The 16 regions pulled 18,335 rows in total, collapsing to 13,317 unique instruments after the same line quoted on several venues is merged (a preferred SERIES stays its own instrument, and Germany's numeric-code venues are separate symbols that carry the same issuer's cap).
- **Per-region USD floors**, applied **after** converting the listing-currency cap: au $300M (+ volume ≥ 100,000), jp $300M, tw $200M, ca $200M, eu-de $300M (+ volume ≥ 50,000), eu-fr/it/es/nl/be/at $100M, eu-ie $200M, eu-fi/dk $100M, eu-pt/gr $50M. A row the source reports no cap for is **excluded**, not written blank.
- **FX** — Frankfurter (ECB) + open.er-api, table dated Frankfurter (ECB): 2026-11-11; open.er-api: Wed, 11 Nov 2026 00:02:32 +0000: EUR 0.89871, JPY 159.23, AUD 1.4579, CAD 1.4235, DKK 6.7183, TWD 32.944401 - all **local units per 1 USD**, so `usd_cap = market_cap_basic / FX`. The conversion direction was verified by share-count reconciliation (`market_cap_basic / close` returns the issuer's real share count) and by the per-region row counts landing within 6% of the 10 November archive.
- **Venue-collapse rule** — one row per issuer and share class; where the same issuer is quoted on several venues, the main-venue line (XETR, TSX, TWSE, TSE…) is published and the others are collapsed into it.
- **Cap carrier rule** — the cap belongs to the issuer: it is read from the issuer's **primary (common) line**, converted **once** on that line's own currency, and carried to every other line of the same issuer, which publishes `cap_source_symbol` and `share_class`. Issuer groups are resolved **before** the floor, so an issuer survives or fails as a whole and a published row never points at a `cap_source_symbol` that is not in the file. `share_class` comes from the ticker suffix and the description, never from the scanner's `type` column (which reads `stock` for common and preferred lines alike). A line whose issuer group holds no common line is excluded with reason `issuer_unresolved` rather than published with a borrowed cap.
- **Cross-venue cap check** — the issuer's US depositary receipt is an independent second reading of the same company-level cap. It was run against the **US depositary receipts** - the only US line that is the same issuer by definition: the foreign cap and the ADR's own cap agree within 10% for every issuer that has one. The US lines are also the source for `us_listing` (`NYSE`/`NASDAQ`/`ADR`/`OTC`/`none`), matched on the issuer (name-token similarity plus the issuer-country tag) rather than on the ticker; an OTC quotation is published as `OTC` even when the source types it as a depositary receipt.
- **Venue-official price rule** — where an exchange's own close could be obtained it is the price that is published; a third-party quote that differs is recorded, not averaged. No row in this artifact carries a `price_conflict` cell: every close in it is the scanner's venue close for 11 November, and the index table publishes the exchange's own close where one was reported (the TAIEX is published at CNA's official 44,257.15 +3.62%, the DAX at the wire's 26,662.77 +1.20%, the CAC 40 at 8,332.87 +0.66%).
- **Carry-over detection** — a row is a carry-over when its close is **exactly** equal to the prior session's stored close **and** either its volume is zero or its `change_pct` is non-zero (the scanner's stale leftover). The comparison is against the **immediate** prior session only (10 November); the walk back through older files is used only to stamp `last_trade_date`.
- **CSV column count** — **18** (`date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`), unchanged from the 10 November session, so the archive's width has not moved since 5 November.
- **Files written** — 16 `<region>.csv` files (4,380 rows in total), `summary.md`, `_manifest.json`, `_excluded.json` and `_carryover.json` in `international-eod/2026-11-11/`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView per-country scanner | `POST scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan` with the top-level country filter | ok | 18,335 rows, 13,317 unique instruments |
| TradingView America scanner | `POST scanner.tradingview.com/america/scan`, types `["stock","dr"]`, sorted by market cap, 3 pages | ok | 13,559 US lines used for `us_listing` and the cross-venue cap check |
| TradingView index scanner | `POST scanner.tradingview.com/global/scan` (SP:XJO, TVC:NI225, TSE:TOPIX, TSX:TSX, XETR:DAX, EURONEXT:PX1, FTSE:FTSEMIB, BME:IBC, EURONEXT:AEX, EURONEXT:BEL20, VIE:ATX, EURONEXT:PSI20, EURONEXT:ISEQ, OMXHEX:OMXH25, OMXCOP:OMXC20, ATHEX:GD, STOXX:SXXP) | ok | 17 venue index levels; each reconciles with the wire's own close where one was published |
| Frankfurter (ECB) | `https://api.frankfurter.dev/v1/latest?base=USD` | ok | table dated 32 +0000: EUR 0.89871, JPY 159.23, AUD 1.4579, CAD 1.4235, DKK 6.7183 |
| open.er-api | `https://open.er-api.com/v6/latest/USD` | ok | TWD 32.944401; agrees with Frankfurter to within 0.2% on the currencies they share |
| Market close reporting | Reuters, AP, CNA / Focus Taiwan, Taiwan News, RTTNews, Il Sole 24 Ore Radiocor, Sharecast, HL, Samso, FN Arena, Trading Economics, Investing.com, FT Markets, Irish Times, voestalpine and Vincorion company releases, Nokia release, Kinaxis release, EQS ad-hoc | ok | Used for the index levels, the session narrative and every catalyst in the movers table |

### Caveats

- **Unit caveat** — `market_cap` is USD; `open`/`high`/`low`/`close` are in the listing currency named in the `currency` column. The two are not comparable within a row.
- **Carry-over rows** — 88 published rows across the 16 regions did not trade today (the scanner returned the prior session's close). They are written as the source returned them, listed in `_carryover.json` with their `last_trade_date`, and excluded from every movers list. Spain accounts for 35 of them and Canada for 31.
- **The cross-venue cap check was run against the US depositary receipts only** - the source's OTC caps are not company-level (a US OTC line for an Australian issuer reads a few hundred dollars), and an ordinary US listing is not automatically the same issuer, so neither is a second reading of the cap.
- **A cap claim without a second reading is not publishable** — every published cap is either the issuer's own primary line or a carry from it.
- **Issuer-country filter** — the universe is the scanner's **issuer** country, so a name TradingView files under another country is not in this file even when it trades there. The Canadian file, for example, holds only issuers the source tags as Canadian.
- **Issuer groups are venue-scoped, so a preferred line can be unresolved** — the cap-carry assertion requires the carrier and the carried line to share a ticker root, and a root carries its venue. Germany's numeric-code venues (LSX, LS) quote an issuer's line under a different symbol from its XETR line, so those lines are separate instruments. Where a group's only line is a preferred or unit line, there is no primary to carry a cap from and the row is excluded with reason `issuer_unresolved` rather than published with a borrowed cap.
- **The Canadian preferred block is thinner than on 10 November** — the source's Canada pull no longer returns several issuers' common lines (Brookfield Office, for example), so their preferred series have no primary to carry a cap from and are excluded as `issuer_unresolved`. This is a source-side gap, visible in the per-reason exclusion counts, not a change to the universe rule.
- **The scanner is the close of record here** — every close in the CSVs is the scanner's venue close for 11 November. Where a wire reported an intraday level (Celestica at +9.19% in early trading, the TSX at +0.53% at 10:44 ET) the close is published and the intraday figure is named in the catalyst instead of the other way round.
- **No company-specific driver was found for the names in `## No catalyst`**, and none is claimed for them; they are published separately rather than dropped, because a move without a source is still a move.
- **Sector rotation** (mean and median `change_pct` per sector over the published rows, sectors with 25+ names): Electronic Technology +2.49% mean / +2.00% median (n=489); Energy Minerals +1.65% mean / +1.78% median (n=72); Producer Manufacturing +1.49% mean / +0.97% median (n=449); Distribution Services +1.00% mean / +0.73% median (n=150) — while Non-Energy Minerals -0.77% mean (n=330); Consumer Non-Durables -0.73% mean (n=171); Retail Trade -0.44% mean (n=165).
