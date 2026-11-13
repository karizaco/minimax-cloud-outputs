# Cron #05 eod-international-daily — Friday, 13 November 2026

## TL;DR

- **Global markets closed the week mixed and thin.** Across the 16 regions 4,383 names were written, and of the 4,382 that printed a session change the median name moved +0.16%: 2,338 advanced, 1,756 fell and 288 were flat. The STOXX 600 was flat at 664.14, the TSX slipped 0.09%, the ASX 200 lost 0.71% to 9,082.20, the Nikkei added 0.53% to 61,142.35, the TAIEX jumped 1.35% to 43,675.12 and the ATHEX General fell 0.16% to 2,636.29 - the tape was digested, not directional, with the Fed-hike repricing and Nvidia's leadership change dominating.
- **The one move that mattered was Paladin Energy's -17.59%** (ASX:PDN, OTC): its A$525m equity raise priced the stock 8.1% below the offer on its first day back from a halt. The reachable names did the heavy lifting - **Stantec +13.79%** (NYSE) on a Q3 beat and raised targets, **Kelt Exploration +8.81%** (OTC) on a Q3 swing to profit, **Ambu +5.04%** (OTC) on two broker target hikes, **CES Energy Solutions +6.95%** (OTC) on record Q3 results, against **Celestica -5.42%** (NYSE) giving back two surge days.
- **Read the caps as USD and the prices as local.** `market_cap` is converted once per issuer from its primary line at Frankfurter's 13-Nov rates (JPY 160.0, EUR 0.90481, AUD 1.4738, CAD 1.4258, DKK 6.764, TWD 32.976), while open/high/low/close stay in the listing currency named in the `currency` column; 74 rows carry a close from an earlier session and are excluded from every mover table.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,547 | 1,547 | **293** | $300M + vol ≥ 100,000 | 5 | 1219 | 29 | 1 | 0 | 0 | 0 |
| `jp` | NAG, SAPSE, TSE | 3,896 | 3,867 | **1,382** | $300M | 2 | 2482 | 0 | 1 | 0 | 0 | 11 |
| `tw` | TPEX, TWSE | 2,338 | 2,338 | **872** | $200M | 56 | 1410 | 0 | 0 | 0 | 4 | 0 |
| `ca` | CSE, TSX, TSXV | 4,278 | 2,685 | **658** | $200M | 56 | 1894 | 0 | 77 | 0 | 28 | 13 |
| `eu-de` | XETR | 4,306 | 925 | **115** | $300M + vol ≥ 50,000 | 4 | 466 | 314 | 26 | 0 | 0 | 24 |
| `eu-fr` | EURONEXT | 537 | 537 | **260** | $100M | 1 | 276 | 0 | 0 | 0 | 6 | 0 |
| `eu-it` | MIL | 378 | 378 | **179** | $100M | 2 | 197 | 0 | 0 | 0 | 2 | 0 |
| `eu-es` | BME | 233 | 233 | **137** | $100M | 24 | 72 | 0 | 0 | 0 | 27 | 0 |
| `eu-nl` | EURONEXT | 78 | 78 | **56** | $100M | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| `eu-be` | EURONEXT | 101 | 101 | **76** | $100M | 1 | 24 | 0 | 0 | 0 | 2 | 0 |
| `eu-at` | VIE | 65 | 65 | **50** | $100M | 3 | 12 | 0 | 0 | 0 | 1 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **28** | $50M | 0 | 3 | 0 | 0 | 0 | 1 | 0 |
| `eu-ie` | EURONEXT | 20 | 20 | **17** | $200M | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `eu-fi` | OMXHEX | 189 | 189 | **101** | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 58 | 0 | 0 | 0 | 0 | 0 |
| `eu-gr` | ATHEX | 129 | 129 | **84** | $50M | 0 | 44 | 0 | 1 | 0 | 3 | 0 |
| **total** | | **18,260** | **13,257** | **4,383** | | **159** | **8266** | **343** | **106** | **0** | **74** | **48** |

`Universe` is every instrument the source returns for that country's own listings (the scanner's issuer-country filter, so a foreign company's local line is not counted); `Unique instruments` collapses the same line quoted on several venues down to one line per issuer and share class; `Written` applies the per-region USD market-cap floor plus the region's volume gate. Every excluded row carries a reason from the closed set in `_excluded.json`, and the counts above are read from that file rather than estimated.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 9,082.20 | -64.60 / -0.71% | 2026-11-13 | TradingView SP:XJO and Yahoo ^AXJO agree to the decimal; Samso Market Update and MT Newswires, 13 Nov, both report 9,082.2, down 64.6 points |
| jp | Nikkei 225 | 61,142.35 | +322.99 / +0.53% | 2026-11-13 | Yahoo ^N225 5-minute final bar (06:30 UTC) and Il Sole 24 Ore Radiocor, 13 Nov; the TradingView TVC:NI225 venue index read 61,142.13, 0.22 lower |
| jp | TOPIX | 3,941.57 | +4.24 / +0.11% | 2026-11-13 | TradingView TSE:TOPIX venue index; Kabutan and Yahoo Finance Japan (998405.T), 13 Nov, both report 3,941.57, +4.24; there is no Yahoo index symbol for the TOPIX |
| tw | TAIEX | 43,675.12 | +583.25 / +1.35% | 2026-11-13 | CNA and Taiwan News via CTEE, 13 Nov; the TradingView TWSE:IX0001 venue index and the Yahoo ^TWII 5-minute final bar agree to the decimal |
| ca | S&P/TSX Composite | 36,105.90 | -31.29 / -0.09% | 2026-11-13 | TradingView TSX:TSX venue index and Yahoo ^GSPTSE agree to the decimal; the prior session's 36,137.19 is the TMX/Reuters close of 12 November |
| eu-de | DAX (Xetra) | 26,749.95 | -21.93 / -0.08% | 2026-11-13 | TradingView XETR:DAX venue index and Yahoo ^GDAXI agree to the decimal; Sharecast and SquawkNews Europe close reports, 13 Nov |
| eu-fr | CAC 40 | 8,368.91 | +7.55 / +0.09% | 2026-11-13 | TradingView EURONEXT:PX1 venue index and Yahoo ^FCHI agree to the decimal; Sharecast Europe close, 13 Nov |
| eu-it | FTSE MIB | 51,858.51 | +49.84 / +0.10% | 2026-11-13 | TradingView FTSE:FTSEMIB venue index and Yahoo FTSEMIB.MI agree to the decimal; Boursee's European snapshot, 13 Nov, reports 51,859 |
| eu-es | IBEX 35 | 20,020.10 | +54.60 / +0.27% | 2026-11-13 | TradingView BME:IBC venue index and Yahoo ^IBEX agree to the decimal; Boursee's European snapshot, 13 Nov |
| eu-nl | AEX | 1,140.96 | +0.84 / +0.07% | 2026-11-13 | TradingView EURONEXT:AEX venue index and Yahoo ^AEX agree to the decimal; Boursee's European snapshot, 13 Nov |
| eu-be | BEL 20 | 6,119.66 | +4.57 / +0.07% | 2026-11-13 | TradingView EURONEXT:BEL20 venue index and Yahoo ^BFX agree to the decimal |
| eu-at | ATX | 6,654.83 | -31.06 / -0.46% | 2026-11-13 | TradingView VIE:ATX venue index and Yahoo ^ATX agree to the decimal; finanzen.at RTTNews European close, 13 Nov, reports ATX 6,655, -0.5% |
| eu-pt | PSI 20 | 9,697.64 | +101.27 / +1.06% | 2026-11-13 | TradingView EURONEXT:PSI20 venue index and Yahoo PSI20.LS agree to the decimal |
| eu-ie | ISEQ | 14,976.07 | -35.43 / -0.24% | 2026-11-13 | TradingView EURONEXT:ISEQ venue index and Yahoo ^ISEQ agree to the decimal |
| eu-fi | OMX Helsinki 25 | 6,332.69 | -9.02 / -0.14% | 2026-11-13 | TradingView OMXHEX:OMXH25 venue index and Yahoo ^OMXH25 agree to the decimal |
| eu-dk | OMX Copenhagen 20 | 1,674.23 | +4.67 / +0.28% | 2026-11-13 | TradingView OMXCOP:OMXC20 venue index and the Yahoo ^OMXC20 daily bar agree to the decimal |
| eu-gr | ATHEX General | 2,636.29 | -4.23 / -0.16% | 2026-11-13 | Euronext Athens' own daily list (DOL, 13 Nov 2026) gives the Composite Share Price Index 2,636.29, -4.23 points, -0.16%, day range 2,636.27-2,662.57; euro2day and xrimatistirio, 13 Nov, agree; the TradingEconomics CFD read of 2,649.02 is a third-party quote, not the official close |
| *context* | STOXX 600 | 664.14 | +0.13 / +0.02% | 2026-11-13 | TradingView STOXX:SXXP venue index and Yahoo ^STOXX agree to the decimal; Sharecast and Fidelity Europe close, 13 Nov |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 293 | -1.11% | 48 / 225 / 20 | -17.59% | +5.29% |
| jp | 1,382 | +0.31% | 805 / 535 / 42 | -19.72% | +14.34% |
| tw | 872 | +1.39% | 694 / 147 / 31 | -9.97% | +23.24% |
| ca | 658 | +0.00% | 297 / 300 / 61 | -33.87% | +16.94% |
| eu-de | 115 | -0.36% | 47 / 66 / 2 | -10.31% | +7.53% |
| eu-fr | 260 | +0.00% | 110 / 129 / 21 | -17.50% | +9.60% |
| eu-it | 179 | -0.18% | 71 / 93 / 15 | -12.18% | +7.12% |
| eu-es | 137 | +0.00% | 49 / 50 / 38 | -8.93% | +3.43% |
| eu-nl | 56 | +0.00% | 26 / 26 / 4 | -4.44% | +2.65% |
| eu-be | 76 | +0.00% | 36 / 31 / 9 | -5.00% | +2.98% |
| eu-at | 50 | -0.22% | 14 / 26 / 10 | -9.92% | +2.82% |
| eu-pt | 28 | +0.39% | 16 / 7 / 5 | -5.00% | +2.33% |
| eu-ie | 17 | -0.36% | 5 / 10 / 2 | -1.85% | +3.33% |
| eu-fi | 100 | +0.00% | 48 / 44 / 8 | -5.50% | +5.48% |
| eu-dk | 75 | +0.00% | 35 / 34 / 6 | -3.46% | +5.04% |
| eu-gr | 84 | +0.00% | 37 / 33 / 14 | -2.82% | +5.33% |

An index move and the typical name regularly disagree, so both are published: the ASX 200 fell 0.71% while the median Australian name fell 1.11% (225 of 293 down against 48 up), and the Nikkei rose 0.53% while the median Japanese name rose only 0.31% with 535 of 1,382 still falling; the TSX was flat (median +0.00%, 297 up against 300 down) even though the spread ran from -33.87% to +16.94%.

## Top movers

Liquid names (volume ≥ 100,000 **and** market cap ≥ $1B) whose move cleared ±5%, capped at the six largest absolute moves per region, with the driver that was actually sourced. A row with no sourced driver is not here - it is under `## No catalyst`. Regions where no name cleared the threshold with a sourced driver publish their largest liquid mover instead, marked *(fallback)*.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:PDN` | Paladin Energy Ltd | **-17.59%** | 7.17 AUD | 8,009,695 | $2.65B | OTC | Fell 17.59% to A$7.17 on its first day back from a trading halt after completing an A$525m fully underwritten equity raise - it closed 8.1% below the A$7.80 issue price; the ASX All Ordinaries Gold index fell 2.53% (ASX release, 12 Nov; Samso Market Update, 13 Nov; MT Newswires, 13 Nov) |
| `ASX:LLC` | Lendlease Group | **-8.43%** | 2.28 AUD | 5,838,318 | $1.16B | none | Fell 8.43% to A$2.28 on the bond-redemption announcement before the open: it began redeeming about A$1.22bn of outstanding bonds, funded from the A$1.25bn committed standby facility secured in June 2026, with about A$7m of early-repayment charges and about A$50m to close related interest-rate hedges, completing by 30 November (ASX announcement, 13 Nov; ABC News, 13 Nov; Samso, 13 Nov) |
| `ASX:SIQ` | Smartgroup Corporation Ltd | **-5.71%** | 10.73 AUD | 1,188,226 | $1.06B | none | Fell 5.71% to A$10.73 with no ASX announcement lodged since 4pm Thursday, sold alongside the other salary-packaging name McMillan Shakespeare (-8.29%) as the S&P/ASX Small Ordinaries dropped 1.75% (Samso Market Update, 13 Nov) |
| `ASX:GNC` | Graincorp Limited Class A | **+5.29%** | 7.37 AUD | 2,447,620 | $1.03B | OTC | Rose 5.29% to A$7.37 on the read-across from its FY2026 result (released 12 November: FY26 EBITDA A$223m and a full-year loss) - no further release was lodged on 13 November, and no sector driver was sourced for the move (Yahoo Finance earnings-call summary, 12 Nov; Yahoo Finance, 13 Nov) |
| `ASX:EQR` | EQ Resources Limited | **-5.17%** | 0.275 AUD | 16,262,076 | $1.02B | OTC | Fell 5.17% to A$0.275 with no company release on 13 November, sold with the listed-gold complex as the ASX All Ordinaries Gold index dropped 2.53% and spot gold recovered only 1% to about $3,915 after Thursday's 13-month low (Samso, 13 Nov; Yahoo Finance commodities, 13 Nov) |
| `ASX:EOS` | Electro Optic Systems Holdings Limited | **-5.05%** | 7.34 AUD | 2,604,090 | $1.16B | OTC | Fell 5.05% to A$7.34 with no company release on 13 November, sold with small caps as the S&P/ASX Small Ordinaries fell 1.75% and the ASX 200 lost 0.71% (Samso Market Update, 13 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:7936` | Asics Corporation | **-14.34%** | 4180 JPY | 24,046,800 | $20.54B | OTC | Fell 14.34% to Y4,180 (-Y700), the fourth-largest TSE Prime decliner of the session, after its results disappointed - the shares had ground sideways between Y4,843 and Y4,880 on 5-12 November and broke lower on the results day (Fisco via Kabutan, 13 Nov; Yahoo Finance Japan, 13 Nov) |
| `TSE:4041` | Nippon Soda Co., Ltd. | **+9.50%** | 3860 JPY | 428,000 | $1.20B | none | Rose 9.50% to Y3,860 after raising its FY3/2027 earnings and dividend forecasts, and made the TSE Prime top-ten gainers list (Kabutan, 13 Nov) |
| `TSE:6507` | Sinfonia Technology Co., Ltd. | **-9.49%** | 9060 JPY | 520,600 | $1.76B | none | Fell 9.49% to Y9,060, the ninth-largest TSE Prime decliner, as the market worked through its half-year result and share split reported on 12 November (Yahoo Finance Japan / Fisco via Kabutan, 12-13 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TWSE:2466` | Cosmo Electronics Corporation | **-9.97%** | 393 TWD | 7,900,686 | $2.30B | none | Fell 9.97% to NT$393 (-43.50), the worst performer on the Taiwan Weighted, with no company release found for 13 November - the electronics supply chain gave back ground even as the TAIEX closed up 1.35% (Investing.com, 13 Nov; CNA, 13 Nov) |
| `TPEX:3374` | Xintec Inc. | **+9.96%** | 519 TWD | 26,879,736 | $3.88B | none | Rose 9.96% to NT$519 with no company release found for 13 November, bid with the substrate/electronics complex as Nvidia's leadership change revived custom-chip order expectations (Taiwan News via CTEE, 13 Nov) |
| `TWSE:7610` | LIANYOU METALS CO.,LTD. | **-9.92%** | 1090 TWD | 1,229,346 | $2.14B | none | Fell 9.92% to NT$1,090 (-120), the second-worst Taiwan Weighted performer, with no company release found; the metals complex lagged the index's Nvidia-led chip rally (Investing.com, 13 Nov; Taiwan News, 13 Nov) |
| `TWSE:6949` | PELL Bio-Med Technology Co Ltd | **+9.89%** | 45 TWD | 5,593,738 | $1.63B | none | Rose 9.89% to NT$45 with no company release found for 13 November, in a broad risk-on tape for Taiwan's smaller boards (Taiwan News via CTEE, 13 Nov) |
| `TWSE:6526` | Airoha Technology Corp. | **+9.88%** | 756 TWD | 1,440,346 | $3.49B | none | Hit the daily limit-up with the chip designers - Airoha was named among the limit-up names as investors repositioned for who benefits from Nvidia's post-Huang leadership (Taiwan News via CTEE, 13 Nov) |
| `TPEX:3105` | Win Semiconductors Corp. | **+9.86%** | 568 TWD | 29,076,097 | $6.63B | none | Hit the daily limit-up with the low-Earth-orbit satellite group - Win Semiconductors led the limit-ups in the sector as SpaceX prepared for the 15th Starship flight (Taiwan News via CTEE, 13 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:STN` | Stantec Inc | **+13.79%** | 122.2 CAD | 880,046 | $8.47B | NYSE | Sprinted 13.79% to C$122.20 after reporting Q3 revenue and adjusted profit above estimates - adjusted EPS of C$1.89 - and raised its 2026 profitability targets; the shares traded as high as C$124.01 intraday (MT Newswires / Baystreet, 13 Nov) |
| `TSX:GMIN` | G Mining Ventures Corp | **+9.89%** | 46.21 CAD | 1,171,607 | $8.74B | OTC | Rose 9.89% to C$46.21 with no company release found for 13 November, bid with the gold-miner complex as spot gold recovered about 1% to $3,915 after Thursday's 13-month low (Yahoo Finance commodities, 13 Nov) |
| `TSX:KEL` | Kelt Exploration Ltd. | **+8.81%** | 11.49 CAD | 2,049,720 | $1.51B | OTC | Swung to a Q3 profit and raised its 2026 adjusted funds-from-operations forecast: Q3 petroleum and natural gas sales of $193.3m and adjusted FFO of $106.3m (C$0.51 per diluted share) against $44.6m (C$0.22) a year earlier (Baystreet, 13 Nov) |
| `TSX:CEU` | CES Energy Solutions Corp. | **+6.95%** | 21.54 CAD | 1,315,491 | $2.98B | OTC | Reported record Q3 2026 results and declared a cash dividend; the shares closed at a 52-week high (GlobeNewswire, 12 Nov; Baystreet, 13 Nov) |
| `TSX:NPI` | Northland Power Inc. | **+5.72%** | 23.86 CAD | 2,025,944 | $4.14B | OTC | Reported Q3 2026 results with value-accretive growth updates and reaffirmed its 2026 guidance (company release, 13 Nov) |
| `TSX:CLS` | Celestica Inc. | **-5.42%** | 342.32 CAD | 574,705 | $32.01B | NYSE | Fell 5.42% to C$342.32 with no company release on 13 November, giving back part of a two-session run that took it up 8.4% and then 4.8% on strong Q3 results and investor-day commentary (Trading Economics TSX recap, 12-13 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:S92` | SMA Solar Technology AG | **-8.23%** | 45.26 EUR | 207,921 | $1.89B | OTC | Fell 8.23% to EUR 45.26, a new 13-week low and the worst SDAX name of the session, with no company release found for 13 November (finanzen.at SDAX close, 13 Nov; finanzen.net chart signal, 13 Nov) |
| `XETR:VBK` | Verbio SE | **-7.35%** | 23.7 EUR | 208,420 | $1.81B | none | Fell 7.35% to EUR 23.70, the second-weakest SDAX name, giving back the reaction to its 12 November interim report (higher biofuel prices lifting profit) with no further release on 13 November (finanzen.at, 13 Nov; dpa-AFX, 12 Nov) |
| `XETR:EUZ` | Eckert & Ziegler SE | **+5.79%** | 15.34 EUR | 320,105 | $1.00B | OTC | Rose 5.79% to EUR 15.34 after its results showed good demand for radiopharmaceuticals and a higher earn (dpa-AFX, 12 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ERA` | Eramet SA | **-10.64%** | 32.92 EUR | 124,642 | $1.16B | OTC | Fell 10.64% to EUR 32.92 after launching a capital increase of about EUR 500m with preferential subscription rights - under which the French state is to become the group's largest shareholder (company release, 13 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:FCT` | Fincantieri S.p.A. | **-4.28%** | 11.405 EUR | 5,432,031 | $5.00B | OTC | Fell 4.28% to EUR 12.30 with no company release found for 13 November - the Italian market's largest liquid mover, published as the fallback (Yahoo Finance Italy, 13 Nov) |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `BME:ANA` | Acciona SA | **-7.98%** | 203 EUR | 132,104 | $13.32B | OTC | Fell 7.98% to EUR 203 with no company release found for 13 November, sold with the utilities as the IBEX 35 closed up 0.27% (BME close; Investing.com, 13 Nov) |

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ASM` | ASM International N.V. | **-4.09%** | 694.6 EUR | 228,821 | $38.95B | OTC | Fell 4.09% to EUR 1,338.80 with no release on 13 November, after the EUR 300m share buyback it started on 11 November - the Dutch market's largest liquid mover, published as the fallback (Simply Wall St, 11 Nov; Investing.com, 13 Nov) |

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:UMI` | Umicore SA | **-2.71%** | 17.62 EUR | 440,305 | $4.82B | OTC | Fell 2.71% to EUR 46.20 with no release on 13 November, after the 12 November announcement of a EUR 450m growth investment and reiterated FY 2026 guidance - the Belgian market's largest liquid mover, published as the fallback (Umicore release, 12 Nov) |

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:VOE` | voestalpine AG | **-3.28%** | 36.56 EUR | 298,800 | $7.46B | OTC | Fell 3.28% to EUR 25.60 with no company release found for 13 November - the Austrian market's largest liquid mover, published as the fallback (Wiener Börse close, 13 Nov) |

### eu-pt

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:RENE` | Redes Energeticas Nacionais SA | **+2.33%** | 3.74 EUR | 1,193,731 | $2.68B | none | Rose 2.33% to EUR 6.72 with no company release found for 13 November - the Portuguese market's largest liquid mover, published as the fallback (Euronext Lisbon close, 13 Nov) |

### eu-ie

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:GVR` | Glenveagh Properties PLC | **-1.85%** | 2.385 EUR | 615,607 | $1.30B | none | Fell 1.85% to EUR 1.58 with no company release found for 13 November - the Irish market's largest liquid mover, published as the fallback (Euronext Dublin close, 13 Nov) |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:IQMX` | IQM Quantum Computers Oyj Class A | **-5.50%** | 6.18 EUR | 147,644 | $1.35B | ADR | Fell 5.50% to EUR 6.18 with no company release found for 13 November; the last company event remains the Q3 report of 5 November - the region's largest liquid mover and published as the fallback (Yahoo Finance, 13 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:AMBU_B` | Ambu A/S Class B | **+5.04%** | 91.65 DKK | 1,082,164 | $3.42B | OTC | Rose 5.04% to DKK 91.65 after two brokers lifted targets - UBS to DKK 93 from 72 (neutral) and DNB Carnegie to DKK 110 from 105 (buy) (Finwire / Borskollen analyst list, 13 Nov) |

### eu-gr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ATHEX:MOH` | MOTOR OIL (HELLAS) CORINTH REFINERIES S.A. | **+2.56%** | 62.1 EUR | 102,388 | $7.39B | OTC | Rose 2.56% to EUR 62.10 with no company release found for 13 November, supported by the oil recovery (Brent around $96) - the refiners offset the pressure on the banks and the ATHEX General slipped 0.16% (xrimatistirio ATHEX movers, 13 Nov; euro2day, 13 Nov) |

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a +300% or a -80% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:RKB | Rokeby Resources Limited | **+100.00%** | 10,008,000 | below the $300M cap floor |
| ASX:VEN | Vintage Energy Ltd. | **+100.00%** | 1,202,590 | below the $300M cap floor |
| ASX:AYM | Australia United Mining Limited | **+50.00%** | 312,349 | below the $300M cap floor |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:3672 | AltPlus Holdings Inc. | **-33.33%** | 2,382,000 | below the $300M cap floor |
| TSE:336A | Dynamic Map Platform Co., Ltd. | **+21.88%** | 3,792,800 | below the $300M cap floor |
| TSE:5724 | Asaka Riken Co., Ltd. | **-20.91%** | 233,100 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:6827 | MegaPro Biomedical Co., Ltd. | **+18.13%** | 2,314,392 | below the $200M cap floor |
| TPEX:7759 | Sunhawk Vision Biotech, Inc. | **+17.89%** | 145,578 | below the $200M cap floor |
| TPEX:7850 | Protect Animal Health Incorporation | **+15.94%** | 359,194 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSXV:FUSE | Fuse Battery Metals Inc | **+133.33%** | 306,220 | below the $200M cap floor |
| TSXV:TNO.H | Terreno Resources Corp. | **+66.67%** | 106,210 | below the $200M cap floor |
| TSXV:AGH.H | Canadian Silver Hunter Inc. | **+60.00%** | 131,660 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| XETR:LUS1 | Lang & Schwarz AG | **-20.47%** | 114,395 | below the $300M cap floor |
| XETR:TPG0 | Platform Group SE & Co. KGaA | **+8.07%** | 171,390 | below the $300M cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALIBR | Calibre | **-25.00%** | 7,782,011 | below the $100M cap floor |
| EURONEXT:CO | Casino, Guichard-Perrachon SA | **-21.74%** | 3,086,234 | below the $100M cap floor |
| EURONEXT:ALTHO | Metavisio SA | **-12.50%** | 12,844,954 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:DATA | Datrix S.p.A. | **-8.98%** | 146,500 | below the $100M cap floor |
| MIL:SGC | SG Company Societa Benefit S.p.A. | **+6.75%** | 368,250 | below the $100M cap floor |

### eu-es

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| BME:SAI | Substrate Artificial Intelligence SA | **-11.11%** | 21,206,102 | below the $100M cap floor |
| BME:VANA | Vanadi Coffee SA | **-5.00%** | 1,930,715 | below the $100M cap floor |

### eu-nl

No name below the cap floor cleared the volume and move thresholds in this region.

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:OXUR | Oxurion NV | **-25.00%** | 5,333,812 | below the $100M cap floor |

### eu-at

No name below the cap floor cleared the volume and move thresholds in this region.

### eu-pt

No name below the cap floor cleared the volume and move thresholds in this region.

### eu-ie

No name below the cap floor cleared the volume and move thresholds in this region.

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:BRETEC | Bioretec Ltd. | **+8.85%** | 4,049,129 | below the $100M cap floor |
| OMXHEX:KAMUX | Kamux Oyj | **+6.76%** | 320,351 | below the $100M cap floor |
| OMXHEX:SBI | Sunborn International Plc | **+5.65%** | 364,182 | below the $100M cap floor |

### eu-dk

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXCOP:MOVINN | Movinn A/S | **+29.23%** | 110,173 | below the $100M cap floor |
| OMXCOP:ESG | Ennogie Solar Group A/S | **+12.46%** | 286,372 | below the $100M cap floor |
| OMXCOP:UNLGRP | Unlimit Group A/S | **-12.12%** | 610,500 | below the $100M cap floor |

### eu-gr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ATHEX:IKTIN | Iktinos Hellas S.A. | **+9.17%** | 348,440 | below the $50M cap floor |
| ATHEX:QUAL | Quality & Reliability S.A. | **+5.41%** | 185,550 | below the $50M cap floor |

## No catalyst

Names that moved with **no sourced driver** - no company release, no filing, no analyst action, and no sourced sector or macro move behind them. Kept separate, so they do not dilute the mover table.

### au

No liquid mover in this region lacked a sourced driver.

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | What was found |
|---|---|---|---|---|---|---|---|
| `TSE:6544` | Japan Elevator Service Holdings Co., Ltd. | **-14.33%** | 1246 JPY | 4,537,100 | $1.63B | OTC | No company-specific release was found for 13 November - it fell 14.33% to Y1,246 as the fifth-largest TSE Prime decliner, with no company release and no sourced sector driver behind it (Fisco via Kabutan, 13 Nov) |
| `TSE:6055` | Japan Material Co., Ltd. | **-9.54%** | 1668 JPY | 1,065,200 | $1.18B | OTC | No company-specific release was found for 13 November - it fell 9.54% to Y1,668 as the eighth-largest TSE Prime decliner, with no company release behind it (Fisco via Kabutan, 13 Nov) |
| `TSE:4588` | Oncolys BioPharma, Inc. | **+9.65%** | 8410 JPY | 2,120,700 | $1.42B | none | No company-specific release was found for 13 November - it rose 9.65% to Y8,410 with no company release behind it (Yahoo Finance Japan, 13 Nov) |
| `TSE:7552` | Happinet Corporation | **+9.30%** | 7050 JPY | 701,300 | $1.86B | none | No company-specific release was found for 13 November - it rose 9.30% to Y7,050, a TSE Prime top-ten gainer, with no company release behind it (Kabutan, 13 Nov) |
| `TSE:446A` | Northsand,Inc. | **+9.23%** | 2604 JPY | 1,698,100 | $1.03B | none | No company-specific release was found for 13 November - it rose 9.23% to Y2,604 with no company release behind it (Yahoo Finance Japan, 13 Nov) |

### tw

No liquid mover in this region lacked a sourced driver.

### ca

No liquid mover in this region lacked a sourced driver.

### eu-de

No liquid mover in this region lacked a sourced driver.

### eu-fr

No liquid mover in this region lacked a sourced driver.

### eu-it

No liquid mover in this region lacked a sourced driver.

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | What was found |
|---|---|---|---|---|---|---|---|
| `BME:ANE` | Corporacion Acciona Energias Renovables SA | **-6.89%** | 20.26 EUR | 878,180 | $7.81B | none | No company-specific release was found for 13 November - it fell 6.89% to EUR 20.26, sold with the Acciona group after the parent's decline, with no company release behind it (BME close, 13 Nov) |

### eu-nl

No liquid mover in this region lacked a sourced driver.

### eu-be

No liquid mover in this region lacked a sourced driver.

### eu-at

No liquid mover in this region lacked a sourced driver.

### eu-pt

No liquid mover in this region lacked a sourced driver.

### eu-ie

No liquid mover in this region lacked a sourced driver.

### eu-fi

No liquid mover in this region lacked a sourced driver.

### eu-dk

No liquid mover in this region lacked a sourced driver.

### eu-gr

No liquid mover in this region lacked a sourced driver.

## Method, source health & caveats

### Method

- **Universe** - the TradingView per-country scanner, `types=["stock"]`, filtered on the issuer's own country (`filter: [{left: country, equal, <country>}]`). One pull per region; the completeness test is a SET test (the pages' union equals `totalCount`), and every region pulled 100% of its names.
- **Venue collapse** - one line per symbol plus share class; the busiest venue with a reported cap wins, so the same issuer quoted on XETR, Frankfurt, Stuttgart and Tradegate is published once.
- **Cap carrier** - the cap is resolved to the issuer's PRIMARY (common) line and converted ONCE with that line's currency; every other line of the issuer publishes that same USD figure in `cap_source_symbol`, and a group with no common line is excluded as `issuer_unresolved` rather than published with a borrowed cap. The floor is applied to the group, so a published preferred never points at a cap source that is not in the file.
- **Floors (USD)** - au $300M + volume ≥ 100,000; jp $300M; tw $200M; ca $200M; eu-de $300M + volume ≥ 50,000; eu-fr/it/es/nl/be/at $100M; eu-pt/gr $50M; eu-ie $200M; eu-fi/dk $100M.
- **FX** - Frankfurter (ECB) base-USD table for 13 November 2026 (EUR 0.90481, JPY 160.0, AUD 1.4738, CAD 1.4258, DKK 6.764) plus open.er-api for TWD (32.976133, updated Fri 13 Nov 2026 00:02:31 UTC). These tables quote **local units per 1 USD**, so the conversion is a division: `usd_cap = market_cap_basic / FX_per_USD[currency]`. Share-count reconciliation confirms the direction (`market_cap_basic / close` returns each issuer's real share count).
- **Venue-official price rule** - where an exchange's own auction/close is published it is the price, and the row carries the conflict in `price_conflict`. **No row-level conflict was found today**: the scanner close stood for every published row. The one conflict found is at index level - the ATHEX General's official close 2,636.29 against the TradingEconomics CFD read of 2,649.02 - and it is published in the index table above.
- **CSV schema** - **18 columns** (`date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`), unchanged from the 2026-11-12 session.
- **Files written** - `international-eod/{DATE}/`: 16 region CSVs (`au.csv` … `eu-gr.csv`), `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView country scanner (16 regions) | scanner.tradingview.com/{au,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan, types=stock, filter country | ok | 17,965 rows across 16 regions; every pull's union equalled its totalCount |
| TradingView America scanner (us_listing + ADR second reading) | scanner.tradingview.com/america/scan, types=[stock,dr], paged on a stable name sort | ok | 13,561 rows, union = totalCount |
| TradingView venue indices | scanner.tradingview.com/global/scan, 17 index tickers | ok | 17 index closes, each cross-checked against Yahoo |
| Yahoo chart API | query1.finance.yahoo.com/v8/finance/chart, daily bars + 5-minute final bars for ^N225 and ^TWII | ok | 15 of 16 indices confirmed; the ATHEX has no Yahoo symbol |
| Frankfurter (ECB) | api.frankfurter.app/latest?base=USD&symbols=EUR,JPY,AUD,CAD,DKK | ok | 2026-11-13 table, 5 currencies |
| open.er-api | open.er-api.com/v6/latest/USD | ok | TWD 32.976133 |
| market_session_probe.py | 16 regions x 2026-11-13, Yahoo session bars | ok | 16/16 traded=yes, last_bar=2026-11-13 |
| Euronext Athens daily list | athens.euronext.com .../DOL-2026-216 (13 Nov).pdf | ok | official ATHEX Composite Share Price Index 2,636.29, -4.23, -0.16% |
| Yahoo Finance RSS headline feed | feeds.finance.yahoo.com/rss/2.0/headline?s=<symbol> | ok | dated headlines for 87 international symbols |
| Yahoo chart API for ^AXJO daily series | query1.finance.yahoo.com/v8/finance/chart/^AXJO | degraded | Yahoo serves no 2026-11-12 bar for ^AXJO; the session change was taken from the TradingView venue index (prior close 9,146.80) and confirmed by Samso and MT Newswires |
| Yahoo Finance / TV news search API | query2.finance.yahoo.com/v1/finance/search | degraded | returns quotes but an empty news array for non-US symbols; the RSS headline feed was used instead |

### Caveats

- **Carry-over rows** - 74 published rows carry a close from an earlier session (zero volume, or the scanner's stale change field beside an unchanged close). They stay in the CSVs because the schema is fixed, they are listed in `_carryover.json` with each instrument's last trade date, and they are excluded from every mover list.
- **The yen, the dollar and the bond market set the tone** - the 10-year Treasury yield topped 5.1%, the dollar index set a 19-month high and the market priced an 85-91% chance of a 25bp Fed hike in December, with the ANZ noting a 50bp hike is possible. Gold's 13-month low on Thursday ($3,876 close) and only a 1% Friday recovery is why the gold-miner complex split rather than moved together.
- **Off-official venue rows** - 48 secondary-venue lines carried a change field that did not reconcile with the prior session's close for the same instrument (a stale venue print). The issuer's PRIMARY venue line was published instead and the stale line was dropped by the venue collapse, so no published row carries a move that did not happen - the clearest case was the Cboe Canada line of Quebecor Class A, which read C$74 with a +105.56% change off a C$36 base while the primary TSX line closed at C$80, +2.83%.
- **Illiquid lines move in percent, not in money** - several below-the-gate rows are sub-cent or tiny-turnover lines (GETTEX:GRF with no print, LSX:A2QDNX on 75 shares, EURONEXT:CLEX on 5 shares, TSXV:HXC.H on 1,000 shares). Their percentages are real but their prices are not informative, and they are published for completeness, not as signals.
- **Thin cross-venue lines** - the Irish Euronext line of Hostelworld (EURONEXT:HSW, 71 shares) is not the venue where the stock trades, and the same name's main listing is in London; several German rows survive the collapse on thin Stuttgart or Gettex lines.
- **The Nikkei's and the TAIEX's daily bars lag** - Yahoo's ^N225 and ^TWII daily series still served the 12 November bar, so both index levels were confirmed on the 5-minute final bar (06:30 and 05:30 UTC) and against the venue index and the press.
- **Sector rotation** (mean and median `change_pct` per sector over the written rows) is not a section of its own; the per-region read is carried here and uses the same rows:

  - `au` - Gold and metals led the ASX down (miners -1.6%, real estate -1.3%); the listed-gold index fell 2.53% and small caps fell 1.75% against the ASX 200's -0.71%.
  - `jp` - Service, retail and transport led the TSE up (19 of 33 sectors rose) while non-ferrous metals, machinery, precision instruments and other products fell - the AI/semiconductor complex was bought back after the Nvidia shock.
  - `tw` - The tape was a chip-led reversal: MediaTek +7.01%, ASE +2.05% and a wave of limit-ups in chip design and low-Earth-orbit satellites, with the TAIEX adding a record 3,973.48 points (+10.01%) for the week.
  - `ca` - Energy and defensive names carried the TSX while the technology complex was sold off from Wall Street; the index was almost flat (-0.09%) and the median written name moved under 0.1%.
  - `eu-de` - Small caps were hit hardest (SDAX -1.08%, TecDAX -0.73%): Infineon lost more than 4% and the renewable complex (SMA Solar, Verbio) was sold.
  - `eu-fr` - The CAC 40 was almost flat (+0.09%) with the miners the main drag.
  - `eu-it` - A flat tape (FTSE MIB +0.10%); industrials and defence names lagged.
  - `eu-es` - Utilities and renewables were sold (Acciona -7.98%, Acciona Energia -6.89%) while the IBEX still closed up 0.27%.
  - `eu-nl` - A flat tape (AEX +0.07%); semiconductor equipment names were mixed.
  - `eu-be` - A flat tape (BEL 20 +0.07%) with the battery-materials complex under pressure.
  - `eu-at` - Banks and real estate pulled the ATX down 0.46% while energy held up.
  - `eu-pt` - Utilities led the PSI 20's 1.06% rise.
  - `eu-ie` - The ISEQ slipped 0.24% with property and travel names weak.
  - `eu-fi` - A flat tape (OMX Helsinki 25 -0.14%); technology and industrial machinery names were mixed.
  - `eu-dk` - Health care and industrial machinery carried the OMX Copenhagen 20 up 0.28%.
  - `eu-gr` - Energy was the strongest sector (median +1.39%) and basic materials the weakest (-1.38%); banks eased after three strong days and Allwyn was under pressure.
