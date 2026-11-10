# Cron #05 eod-international-daily — Tuesday, 10 November 2026

## TL;DR

- **Thirteen of the sixteen regions closed higher and the session was a relief rally on lower oil, not a new advance: 4,386 instruments printed across the 16 regions.** Wall Street's Monday rebound (S&P 500 +2.3%) carried Asia - **Tokyo +2.87%** (Nikkei 60,459.58), **Taipei +2.52%** (42,711.92), **Sydney +1.10%** (9,129.0) - and Europe finished higher but off its morning highs (**Frankfurt +0.31%**, **Paris +0.55%**, **Milan +0.69%**) once the US CPI print landed. **Canada (-0.76%) and Copenhagen (-0.83%) were the day's losers**: materials fell about 3% as December gold dropped US$62-80 to about $4,034/oz after a Fed governor warned that more aggressive policy could be needed, and **Copenhagen closed -0.83%**.
- **The most consequential move was the AI-equipment complex, and the names a US trader can actually reach are the ADRs: santec Holdings +23.84% (TSE:6777, optical metrology for data-centre optical inspection), Kokusai Electric +14.36% (TSE:6525, the Nikkei's top gainer), SoftBank Group +13.88% ahead of its own earnings release (TSE:9984, OTC), ASE Technology +7.84% (TWSE:3711, ADR), Taiwan's Delta Electronics +9.91% and MediaTek +2.82%, with **TSMC +2.24% (TWSE:2330, ADR)** adding ~400 points to the TAIEX and **Toyota -2.21% (TSE:7203, ADR)** the counterweight in the same tape.** On the company-specific side the standout was **Monadelphous +15.30%** (ASX:MND) on its first-half FY27 guidance - A$1.7bn of revenue and A$80-85m of net profit after tax.
- **Read the numbers with the unit convention in mind: `market_cap` is USD while every price is in the listing currency** (the `currency` column says which) - a ¥20,050 close and a C$23.15 close are not comparable, the caps are. **And read the tape with the CPI caveat: the rally was an oil-and-tech relief bid that faded into the close** (US CPI +0.4% m/m in October against a +0.3% consensus, 3.9% y/y), which is why Europe's gains shrank from about +1.3% in the morning to +0.3-0.7% at the close and why gold miners were sold. This file carries **18 columns**, the same schema as the 9 November session.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,545 | 1,545 | **303** | $300M + vol ≥ 100,000 | 3 | 1218 | 20 | 1 | 0 | 0 | 0 |
| `jp` | TSE, NAG, FSE, SAPSE | 3,902 | 3,870 | **1,376** | $300M | 3 | 2488 | 0 | 3 | 0 | 1 | 0 |
| `tw` | TWSE, TPEX | 2,336 | 2,336 | **874** | $200M | 55 | 1405 | 0 | 2 | 0 | 2 | 0 |
| `ca` | TSX, TSXV, CSE, NEO | 4,300 | 2,686 | **633** | $200M | 130 | 1858 | 0 | 65 | 0 | 25 | 0 |
| `eu-de` | XETR, FWB, LSX, LS, GETTEX, SWB, DUS, MUN, TRADEGATE, HAM, HAN | 4,298 | 926 | **123** | $300M + vol ≥ 50,000 | 4 | 468 | 331 | 0 | 0 | 0 | 0 |
| `eu-fr` | EURONEXT | 544 | 544 | **260** | $100M | 1 | 283 | 0 | 0 | 0 | 6 | 0 |
| `eu-it` | MIL | 391 | 391 | **181** | $100M | 2 | 208 | 0 | 0 | 0 | 3 | 0 |
| `eu-es` | BME | 273 | 273 | **147** | $100M | 34 | 92 | 0 | 0 | 0 | 34 | 0 |
| `eu-nl` | EURONEXT | 78 | 78 | **56** | $100M | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| `eu-be` | EURONEXT | 101 | 101 | **77** | $100M | 1 | 23 | 0 | 0 | 0 | 3 | 0 |
| `eu-at` | VIE | 65 | 65 | **51** | $100M | 3 | 11 | 0 | 0 | 0 | 2 | 0 |
| `eu-pt` | EURONEXT | 32 | 32 | **28** | $50M | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| `eu-fi` | OMXHEX | 188 | 188 | **101** | $100M | 4 | 83 | 0 | 0 | 0 | 0 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 58 | 0 | 0 | 0 | 0 | 0 |
| `eu-gr` | ATHEX | 130 | 130 | **84** | $50M | 0 | 46 | 0 | 0 | 0 | 1 | 0 |
| **total** | | **18,336** | **13,318** | **4,386** | | **241** | **8269** | **351** | **71** | **0** | **77** | **0** |

`Universe` is every instrument the source returns for that country's own listings (the scanner's issuer-country filter, so a foreign company's local line is not counted); `Unique instruments` collapses the same line quoted on several venues down to one line per issuer and share class; `Written` applies the per-region USD market-cap floor plus the region's volume gate. Every excluded row carries a reason from the closed set in `_excluded.json`, and the counts above are read from that file rather than estimated.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 9,129.00 | +99.30 / +1.10% | 2026-11-10 | AP (10 Nov) and the Samso market update, 4:30pm AEDT: 9,129.0, +99.3 points; TradingView SP:XJO agrees |
| jp | Nikkei 225 | 60,459.58 | +1,684.08 / +2.87% | 2026-11-10 | AP and Odaily (10 Nov): +1,684.08 points to 60,459.58; Tokyo Market Summary (Trader's Web) agrees. The prior close is the 9 Nov published close |
| jp | TOPIX | 3,893.71 | +75.55 / +1.98% | 2026-11-10 | TradingView TSE:TOPIX venue index (10 Nov); the prior close is the 9 Nov published close |
| tw | TAIEX | 42,711.92 | +1,050.22 / +2.52% | 2026-11-10 | CNA / Focus Taiwan and the TWSE daily board (10 Nov): +1,050.22 points to 42,711.92. Investing.com's +2.23% is a third-party figure and is not published |
| ca | S&P/TSX Composite | 36,170.45 | -275.81 / -0.76% | 2026-11-10 | TradingView TSX:TSX venue index (10 Nov); RTTNews had it at 36,172.76 (-0.8%) mid-session. Reuters: materials -3% as gold fell |
| eu-de | DAX (Xetra) | 26,347.45 | +80.26 / +0.31% | 2026-11-10 | Anadolu/AA European close (10 Nov) and Il Sole 24 Ore Radiocor: 26,347.45 +0.31%; TradingView XETR:DAX agrees |
| eu-fr | CAC 40 | 8,278.59 | +45.29 / +0.55% | 2026-11-10 | Anadolu/AA European close (10 Nov) and ANSA: 8,278.59 +0.55%; TradingView EURONEXT:PX1 agrees |
| eu-it | FTSE MIB | 51,755.08 | +355.20 / +0.69% | 2026-11-10 | ANSA (10 Nov): 51,755 points, +0.69%; TradingView FTSE:FTSEMIB agrees |
| eu-es | IBEX 35 | 19,936.40 | +193.90 / +0.98% | 2026-11-10 | TradingView BME:IBC venue index (10 Nov); the earlier ~+1.3% figure in intraday European wraps was before the US CPI print |
| eu-nl | AEX | 1,132.44 | +2.47 / +0.22% | 2026-11-10 | TradingView EURONEXT:AEX venue index (10 Nov) |
| eu-be | BEL 20 | 6,105.03 | +6.94 / +0.11% | 2026-11-10 | TradingView EURONEXT:BEL20 venue index (10 Nov) |
| eu-at | ATX | 6,650.55 | +88.09 / +1.34% | 2026-11-10 | TradingView VIE:ATX venue index (10 Nov) |
| eu-pt | PSI 20 | 9,548.46 | -6.42 / -0.07% | 2026-11-10 | TradingView EURONEXT:PSI20 venue index (10 Nov) |
| eu-ie | ISEQ | 15,025.86 | +150.53 / +1.01% | 2026-11-10 | TradingView EURONEXT:ISEQ venue index (10 Nov) |
| eu-fi | OMX Helsinki 25 | 6,282.48 | +3.53 / +0.06% | 2026-11-10 | TradingView OMXHEX:OMXH25 venue index (10 Nov) |
| eu-dk | OMX Copenhagen 20 | 1,654.80 | -13.89 / -0.83% | 2026-11-10 | TradingView OMXCOP:OMXC20 venue index (10 Nov) |
| eu-gr | ATHEX General | 2,642.07 | +32.44 / +1.24% | 2026-11-10 | TradingView ATHEX:GD venue index (10 Nov); there is no Yahoo symbol for the ATHEX |
| *context* | STOXX 600 | 658.32 | +1.80 / +0.27% | 2026-11-10 | Anadolu/AA European close (10 Nov): 658.32, +0.27% |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 303 | +1.55% | 252 / 40 / 11 | -10.29% | +17.11% |
| jp | 1,376 | +1.55% | 1016 / 343 / 17 | -20.00% | +28.49% |
| tw | 874 | +0.51% | 502 / 328 / 44 | -10.81% | +17.38% |
| ca | 633 | -0.12% | 237 / 343 / 53 | -15.67% | +8.82% |
| eu-de | 123 | +0.22% | 68 / 55 / 0 | -6.30% | +13.16% |
| eu-fr | 260 | +0.21% | 140 / 101 / 19 | -5.07% | +11.76% |
| eu-it | 181 | +0.38% | 104 / 66 / 11 | -9.33% | +10.09% |
| eu-es | 147 | +0.00% | 68 / 31 / 48 | -6.25% | +4.91% |
| eu-nl | 56 | +0.29% | 31 / 22 / 3 | -10.08% | +6.96% |
| eu-be | 77 | +0.00% | 36 / 32 / 9 | -4.25% | +3.47% |
| eu-at | 51 | +0.11% | 26 / 19 / 6 | -3.76% | +9.25% |
| eu-pt | 28 | +0.49% | 18 / 7 / 3 | -1.91% | +4.40% |
| eu-ie | 17 | +0.05% | 9 / 6 / 2 | -2.07% | +1.94% |
| eu-fi | 101 | -0.16% | 44 / 53 / 4 | -7.08% | +6.13% |
| eu-dk | 75 | +0.00% | 34 / 35 / 6 | -6.09% | +7.56% |
| eu-gr | 84 | +0.36% | 53 / 18 / 13 | -2.03% | +4.80% |

**One story, one catalyst.** The buyer of the day was oil down and technology up: Brent fell below $91 a barrel - its lowest since early September - after President Trump said the Iran conflict was "militarily effectively over", and Wall Street's AI complex rebounded (the Nasdaq +2.7% on Monday, the Philadelphia Semiconductor Index +6.9%). That combination produced an **Asian close-up session** (Taipei's electronics +3.06%, Seoul's Kospi +4.39% with SK hynix +6.7% and Samsung +4.7%, Tokyo's Kioxia +7.5% and Advantest +4.6%) and a **broad European open** (STOXX 600 +0.72% at 08:20 GMT, banks +2.6% intraday, defence +4.2%, airlines bid on cheaper fuel). Then **US October CPI printed +0.4% m/m against a +0.3% consensus** and the late-session gains came off: London closed -0.29%, Frankfurt pared +1.29% to +0.31%, Toronto gave back a 1.8% Monday gain, and gold - already sliding on the Fed governor's hawkishness - took another US$62-80 an ounce to about $4,034, which is why the Canadian precious-metals complex was the day's worst sector. The one late mover worth watching is **Infineon**: it opened +4.6% and peaked at EUR 52.06 after raising its data-centre sales outlook, and then closed +0.87% at EUR 49.05 - a textbook CPI fade.

## Top movers

Liquid names (volume ≥ 100,000 **and** market cap ≥ $1B) whose move cleared ±5%, capped at the six largest absolute moves per region, with the driver that was actually sourced. Where a region had no such name, its largest liquid mover is published instead and marked. A row with no sourced driver is not here - it is under `## No catalyst`.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:MND` | Monadelphous Group Limited | **+15.30%** | 32.63 AUD | 704,619 | $1.97B | none | H1 FY27 business update (10 Nov, 8:19am AEDT): revenue ~A$1.7bn and net profit after tax of A$80-85m for the half to 31 Dec 2026, after A$830m of new contracts since 1 July; management flags moderating activity in H2 (ASX release via stocklight; Samso market update, 10 Nov; The West Australian, 10 Nov) |
| `ASX:OBM` | Ora Banda Mining Ltd. | **+7.19%** | 1.64 AUD | 13,786,572 | $2.05B | none | No company-specific release found - the gold complex rose with mining (+1.5%) and gold stocks (+2.3%) on cheaper diesel and cost relief even as spot gold slipped below $4,100/oz (Business Recorder / Reuters market wrap, 10 Nov; thebull.com.au, 10 Nov) |
| `ASX:MP1` | Megaport Ltd. | **+6.40%** | 18.45 AUD | 1,181,727 | $2.84B | OTC | No company-specific release found - the ASX's mid-cap growth names rose with the broad, oil-led rally; Megaport was among the day's top risers (Samso market update, 10 Nov) |
| `ASX:SRG` | SRG Global Limited | **+6.36%** | 3.51 AUD | 2,773,779 | $1.44B | none | Sector read-through from Monadelphous' H1 guidance - SRG Global, a fellow WA engineering and mining-services contractor, was lifted with it (thebull.com.au, 10 Nov) |
| `ASX:QAN` | Qantas Airways Limited | **+6.34%** | 9.9 AUD | 12,024,635 | $9.61B | OTC | Qantas plans to cut 850 corporate roles from mid-2027 and move the work to Accenture; the market took the cost-out positively, and cheaper Brent (settling near $91) helped the fuel bill (ABC News live markets, 10 Nov; Samso market update, 10 Nov; Business Recorder, 10 Nov). No ASX announcement was lodged between 4pm Monday and the close |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:6777` | santec Holdings Corporation | **+23.84%** | 20050 JPY | 621,700 | $1.20B | none | AI-driven optical-metrology demand: H1 net sales +65.6% and operating profit +87.5%, with FY March-2027 operating profit guidance raised from Y12bn to Y18bn and the dividend raised Y100 (results and revised guidance, 6 Nov; continued buying on the AI bounce, 10 Nov - Tokyo Market Summary and the TSE top-gainer ranking) |
| `TSE:6834` | Seikoh Giken Co., Ltd. | **+16.24%** | 5010 JPY | 1,262,600 | $1.27B | none | No company-specific release found - Seikoh Giken, an optical-component and optical-communication supplier, rose with the Tokyo AI/optics complex (TSE top-gainer ranking, 10 Nov; Yahoo Finance quote, 10 Nov) |
| `TSE:6269` | Modec, Inc. | **+15.86%** | 8365 JPY | 2,951,700 | $3.12B | none | Upward revision of the earnings and dividend forecasts together with a share buyback/cancellation announcement; Modec surged in the afternoon session (Tokyo Market Summary, Trader's Web, 10 Nov) |
| `TSE:6525` | Kokusai Electric Corporation | **+14.36%** | 5576 JPY | 12,394,200 | $7.32B | OTC | No company-specific release found - Kokusai Electric topped the Nikkei/TOPIX gainer list as semiconductor-equipment shares followed the global AI-equipment rebound (Tokyo Market Summary and Investing.com TOPX1000 gainers, 10 Nov) |
| `TSE:9984` | SoftBank Group Corp. | **+13.88%** | 3872 JPY | 64,833,500 | $122.70B | OTC | SoftBank Group jumped 13.9% ahead of its own earnings release later on 10 November (Euronews, 10 Nov; AP, 10 Nov) |
| `TSE:5233` | Taiheiyo Cement Corporation | **-12.34%** | 3859 JPY | 1,424,900 | $3.14B | none | Downward revision of the earnings forecast; Taiheiyo Cement was the top decliner of the session (Tokyo Market Summary, Trader's Web, 10 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TWSE:5269` | Asmedia Technology Inc. | **-10.00%** | 1125 TWD | 1,077,559 | $2.83B | none | Q3 2026 results (earnings call on the afternoon of 10 Nov): the stock was up 6.9% in early trading and then closed limit-down at NT$1,125 (Yahoo Finance 5269.TW, 10 Nov) |
| `TWSE:6271` | Tong Hsing Electronic Industries ,Ltd. | **+10.00%** | 203.5 TWD | 4,633,217 | $1.18B | none | Limit-up at NT$203.50 with the electronic-component makers - analysts at Moore Securities noted rotational buying into AI-linked electronics (CNA / Focus Taiwan, 10 Nov; Investing.com Taiwan close report, 10 Nov) |
| `TPEX:6223` | MPI Corporation | **+9.99%** | 4075 TWD | 760,610 | $11.07B | none | No company-specific release found - MPI Corporation rose with the rotational buying into AI-linked electronics (CNA / Focus Taiwan, 10 Nov) |
| `TWSE:3661` | Alchip Technologies Ltd. | **+9.97%** | 3420 TWD | 4,645,742 | $8.16B | none | AI chip-design services: the AI-linked local names continued to steam ahead and Alchip was named in a same-day KGISI sector note on split sourcing and volume upside (CNA / Focus Taiwan, 10 Nov; KGISI research, 10 Nov) |
| `TWSE:2345` | Accton Technology Corp. | **+9.96%** | 1545 TWD | 6,572,382 | $23.95B | none | AI server and networking chain: Accton sits in the five-US-CSP capex chain covered by a same-day KGISI sector note (KGISI research, 10 Nov; CNA / Focus Taiwan, 10 Nov) |
| `TWSE:2368` | Gold Circuit Electronics Ltd | **+9.96%** | 983 TWD | 11,402,302 | $14.31B | none | Printed circuit boards: Gold Circuit Electronics jumped 10% to NT$983 in the rotational buying into PCB and component makers (CNA / Focus Taiwan, 10 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:USA` | Americas Gold and Silver Corporation | **-8.58%** | 4.26 CAD | 1,151,464 | $1.11B | NYSE | Gold-price shock: December gold fell US$62-80 to ~$4,034/oz after a Fed governor said more aggressive policy could be needed if inflation keeps rising, and TSX materials fell about 3% (Reuters, 10 Nov; Baystreet.ca, 10 Nov) |
| `TSX:NUAG` | New Pacific Metals Corp | **-8.56%** | 7.9 CAD | 121,391 | $1.13B | NYSE | Same gold-price shock - New Pacific is a developer/explorer and fell with the precious-metals complex (Reuters, 10 Nov; Baystreet.ca, 10 Nov) |
| `TSX:PET` | Pet Valu Holdings Ltd. | **+7.57%** | 23.15 CAD | 730,429 | $1.02B | none | Q3 2026 results: revenue C$299.5m (+3.5%), system-wide sales C$388.6m (+3.9%), same-store sales +1.5%, adjusted EBITDA C$66.6m (+4.8%), adjusted EPS C$0.44 (+10%), and the 2026 revenue-growth outlook was set at 2.5-3.5% (Pet Valu / GlobeNewswire release, 10 Nov) |
| `TSX:VMET` | Versamet Royalties Corp. | **-6.87%** | 12.33 CAD | 102,076 | $1.02B | NASDAQ | Same gold-price shock - Versamet is a precious-metals royalty company (Reuters, 10 Nov) |
| `TSX:DPM` | DPM Metals Inc. | **-6.80%** | 53.9 CAD | 1,369,527 | $8.97B | OTC | Same gold-price shock - DPM Metals fell with the base/precious-metals complex (Reuters, 10 Nov; Baystreet.ca, 10 Nov) |
| `TSX:GGD` | Gogold Resources, Inc. | **-6.79%** | 3.43 CAD | 1,276,814 | $1.13B | OTC | Same gold-price shock - Gogold Resources fell with the precious-metals complex (Reuters, 10 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:AG1` | AUTO1 Group SE | **-4.94%** (the region's largest liquid mover; it did not clear ±5%) | 16.35 EUR | 501,206 | $4.28B | OTC | AUTO1 appointed Jörg Pietzner as CFO on 10 November (07:30 CET), after the surprise departure of its previous CFO; the shares were already under pressure from the Q3 revenue miss (EQS company news, 10 Nov; simplywall.st, 7 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:EDEN` | Edenred SA | **+6.37%** | 25.89 EUR | 969,717 | $6.45B | none | A Brazilian court suspended part of the country's new meal-voucher rules, a positive for both employee-benefits providers - Edenred and Pluxee (Il Sole 24 Ore Radiocor, 10 Nov, midday; the stock closed +6.37% at EUR 25.89 after being +3.2% in midday trading) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:NWL` | NewPrinces S.p.A. | **-7.61%** | 24.3 EUR | 316,804 | $1.26B | none | Q3 2026 results day - NewPrinces closed 7.6% lower at EUR 24.30 on the release (Yahoo Finance NWL.MI, 10 Nov, earnings date 10 Nov) |

### eu-es

No liquid name cleared ±5% on the day.

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:BESI` | BE Semiconductor Industries N.V. | **+2.58%** (the region's largest liquid mover; it did not clear ±5%) | 150.8 EUR | 525,037 | $13.31B | OTC | Chip-related stocks led the European open - BE Semiconductor, Infineon and Soitec all made gains as the AI trade stabilised (Hargreaves Lansdown market report, 10 Nov; Il Sole 24 Ore Radiocor, 10 Nov) |

### eu-be

No liquid name cleared ±5% on the day.

### eu-at

No liquid name cleared ±5% on the day.

### eu-pt

No liquid name cleared ±5% on the day.

### eu-ie

No liquid name cleared ±5% on the day.

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:IQMX` | IQM Quantum Computers Oyj Class A | **-7.08%** | 6.76 EUR | 126,864 | $1.57B | ADR | Q3 2026 interim report published at 01:19 CET on 10 November; the shares fell through the session (company interim report, 10 Nov) |
| `OMXHEX:FIA1S` | Finnair Oyj | **+5.01%** | 5.655 EUR | 1,147,563 | $1.23B | OTC | No company-specific release found - airline shares were lifted across Europe by cheaper fuel as Brent fell back below $91 (Reuters, 10 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:HLUN_A` | H. Lundbeck A/S Class A | **+7.56%** | 56.9 DKK | 223,267 | $8.27B | OTC | 9M 2026 results and a guidance raise: revenue DKK 20,191m (+13% CER), adjusted EBITDA DKK 7,026m (+19% CER) led by Vyepti (+45%), and FY2026 revenue-growth guidance lifted to 11-12% CER from 7-9% with adjusted EBITDA growth raised to 15-19% from 8-14% (Lundbeck company announcement, 10 Nov 11:40 CET; Quartr summary, 10 Nov; Euroinvestor via Nordic Financial News, 10 Nov) |
| `OMXCOP:HLUN_B` | H. Lundbeck A/S Class B | **+6.14%** | 59.65 DKK | 2,852,170 | $8.27B | OTC | Same release - the Class B line followed the guidance raise (Lundbeck company announcement, 10 Nov) |
| `OMXCOP:NTG` | NTG Nordic Transport Group A/S | **-6.09%** | 308.5 DKK | 118,172 | $1.10B | none | Q3 2026 interim results released on the evening of 9 November, with the results call held on the morning of 10 November; the shares fell (NTG investor relations, 10 Nov) |

### eu-gr

No liquid name cleared ±5% on the day.

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a +100% or a -50% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:SMG | SEVENMEDIA FPO | **+9400.00%** | 103,476 | below the $300M cap floor |
| ASX:NAE | New Age Exploration Ltd | **+2400.00%** | 484,790 | below the $300M cap floor |
| ASX:MRQ | MRG Metals Limited | **+100.00%** | 119,468 | below the $300M cap floor |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:198A | PostPrime Inc. | **+33.33%** | 5,603,100 | below the $300M cap floor |
| TSE:4286 | CL Holdings Inc. | **+24.63%** | 372,900 | below the $300M cap floor |
| TSE:4064 | Nippon Carbide Industries Company,Incorporated | **+21.94%** | 237,900 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:7737 | KDAN Mobile Software Ltd | **-16.50%** | 260,978 | below the $200M cap floor |
| TPEX:5248 | Pixon Technologies Corporation | **-15.28%** | 522,499 | below the $200M cap floor |
| TPEX:7507 | Enrestec, Inc. | **+12.28%** | 162,277 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSXV:ESPN | Hispania Resources Inc | **+300.00%** | 200,398 | below the $200M cap floor |
| TSXV:HXC.H | HFX Holding Corp. | **+300.00%** | 1,000 | below the $200M cap floor |
| TSXV:KEON | Keon Capital Inc | **+173.70%** | 411,339 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| XETR:SNG | SINGULUS TECHNOLOGIES AG | **+10.43%** | 147,033 | below the $300M cap floor |
| XETR:LEOW | Leo International Precision Health Aktiengesellschaft | **+6.78%** | 117,631 | below the $300M cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALALO | ACHETER-LOUER.FR | **+999900.00%** | 28 | below the $100M cap floor |
| EURONEXT:ALTOO | Toosla Societe Anonyme | **-50.00%** | 7,201,809 | below the $100M cap floor |
| EURONEXT:ADOC | Adocia SA | **+25.00%** | 1,627,757 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:BWZ | Beewize S.p.A. | **+19.27%** | 10,000 | below the $100M cap floor |
| MIL:VNE | VNE S.p.A. | **+14.08%** | 19,950 | below the $100M cap floor |
| MIL:ENA | ENA S.P.A. | **-10.00%** | 38,000 | below the $100M cap floor |

### eu-es

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| BME:CITY | Club De Futbol Intercity SAD | **-14.46%** | 14,498,153 | below the $100M cap floor |

### eu-nl

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:HOLCO | Holland Colours NV | **-7.63%** | 3,496 | below the $100M cap floor |
| EURONEXT:BEVER | N.V. Bever Holding | **-7.14%** | 100 | below the $100M cap floor |
| EURONEXT:CTAC | Ctac NV | **-6.64%** | 73 | below the $100M cap floor |

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:CLEX | Cumulex N.V. | **+27.27%** | 5 | below the $100M cap floor |
| EURONEXT:OPTI | OPTION | **+22.14%** | 12,741 | below the $100M cap floor |
| EURONEXT:MONNI | MONNI | **+9.93%** | 70 | below the $100M cap floor |

### eu-pt

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ESON | ESTORIL-SOL, SGPS, S.A. | **+19.85%** | 30 | below the $50M cap floor |

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:EAGLE | Eagle Filters Group Plc Class A | **+17.38%** | 285,250 | below the $100M cap floor |
| OMXHEX:NANOFH | Nanoform Finland Oyj | **-6.59%** | 56,419 | below the $100M cap floor |
| OMXHEX:HRTIS | Herantis Pharma Plc | **-6.39%** | 61,716 | below the $100M cap floor |

### eu-dk

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXCOP:QINTER | Q-Interline A/S | **+19.15%** | 44,298 | below the $100M cap floor |
| OMXCOP:VIRO | ViroGates A/S | **-15.15%** | 2,342 | below the $100M cap floor |
| OMXCOP:FASTPC | FastPassCorp A/S | **+13.64%** | 70 | below the $100M cap floor |

### eu-gr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ATHEX:VOSYS | VOYATZOGLOU S.A. | **+6.42%** | 101 | below the $50M cap floor |
| ATHEX:ELBE | ELVE S.A. | **+6.20%** | 414 | below the $50M cap floor |
| ATHEX:XYLEP | Interwood-Xylemporia A.T.E.N.E. Pref.Reg. | **+5.37%** | 92 | below the $50M cap floor |

## No catalyst

Names that moved with **no sourced driver** - no company release, no filing, no analyst action and no sourced sector or macro move behind them. Kept separate so they do not dilute the mover table.

### au

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `ASX:IMD` | Imdex Ltd | **+6.10%** | 3.48 AUD | $1.18B |

### eu-es

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `BME:ACX` | Acerinox SA | **+3.33%** | 15.81 EUR | $4.09B |

### eu-be

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `EURONEXT:UMI` | Umicore SA | **-1.90%** | 18.55 EUR | $5.10B |

### eu-at

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `VIE:MMK` | Mayr-Melnhof Karton AG | **+9.25%** | 73.2 EUR | $1.50B |

### eu-pt

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `EURONEXT:NOS` | NOS SGPS SA | **+2.56%** | 5.61 EUR | $3.16B |

### eu-ie

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `EURONEXT:A5G` | AIB Group PLC | **+1.94%** | 11.58 EUR | $26.15B |

### eu-gr

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `ATHEX:OPTIMA` | Optima Bank SA | **+4.53%** | 14.77 EUR | $3.51B |

The drivers that could not be sourced, per name:

- `ASX:IMD` — No company-specific release found, and no sourced sector or macro move explains the move - Imdex is a small-cap mining-services name on a day when the ASX's own reporting lists it among the risers without a driver (FN Arena ASX winners/losers, 10 Nov; Samso market update, 10 Nov)
- `BME:ACX` — No company-specific release found; Acerinox rose with the European industrials on the broad rally and the day's lower input costs (ANSA European close, 10 Nov)
- `EURONEXT:UMI` — No company-specific release found; Umicore is a metals and materials name on a day when the precious-metals complex fell hard on the gold-price drop (Reuters, 10 Nov)
- `VIE:MMK` — No company-specific release found - Mayr-Melnhof's +9.25% could not be tied to a release, a filing or an analyst action, and no sourced sector move of that size was found for Austrian packaging (ATX close via the TradingView venue index, 10 Nov)
- `EURONEXT:NOS` — No company-specific release found; NOS rose with the broad European tape (Anadolu/AA European close, 10 Nov)
- `EURONEXT:A5G` — No company-specific release found; AIB Group traded with the European banks, which led the STOXX 600 sectorally (+2.6% intraday per Reuters, 10 Nov)
- `ATHEX:OPTIMA` — No company-specific release found; the ATHEX financials sector index closed +1.85% (TradingView ATHEX:FTSE_FS, 10 Nov)

## Method, source health & caveats

### Method

- **Universe** — the TradingView per-country scanner (`POST scanner.tradingview.com/<country>/scan`), issuer-country filtered. The filter is the **top-level** `filter` key (`[{"left":"country","operation":"equal","right":"Germany"}]`): the key inside `symbols` is silently ignored and returns the unfiltered totalCount with no error. The 16 regions pulled 18,336 rows in total, collapsing to 13,318 unique instruments after the same line quoted on several venues is merged (a preferred SERIES stays its own instrument).
- **Per-region USD floors**, applied **after** converting the listing-currency cap: au $300M (+ volume ≥ 100,000), jp $300M, tw $200M, ca $200M, eu-de $300M (+ volume ≥ 50,000), eu-fr/it/es/nl/be/at $100M, eu-ie $200M, eu-fi/dk $100M, eu-pt/gr $50M. A row the source reports no cap for is **excluded**, not written blank.
- **FX** — Frankfurter (ECB reference rates, table dated 2026-11-10) with open.er-api for TWD: EUR 0.89174, JPY 158.18, AUD 1.4485, CAD 1.4136, DKK 6.6661, TWD 32.780875 - all **local units per 1 USD**, so `usd_cap = market_cap_basic / FX`. The conversion direction was verified by share-count reconciliation (`market_cap_basic / close` returns the issuer's real share count) and by the per-region row counts landing within 1-14% of the 9 November archive. open.er-api's table agrees with Frankfurter to within 0.2% on the five currencies they share.
- **Venue-collapse rule** — one row per issuer and share class; where the same issuer is quoted on several venues, the main-venue line (XETR, TSX, TWSE, TSE…) is published and the others are collapsed into it.
- **Cap carrier rule** — the cap belongs to the issuer: it is read from the issuer's **primary (common) line**, converted **once** on that line's own currency, and carried to every other line of the same issuer, which publishes `cap_source_symbol` and `share_class`. Issuer groups are resolved **before** the floor, so an issuer survives or fails as a whole and a published row never points at a `cap_source_symbol` that is not in the file. `share_class` comes from the ticker suffix and the description, never from the scanner's `type` column (which reads `stock` for common and preferred lines alike).
- **Cross-venue cap check** — the issuer's US line is an independent second reading of the same company-level cap. It was run against the **US depositary receipts** - the only US line that is the same issuer by definition: the foreign cap and the ADR's own cap agree within 10% for 35 of 35 issuers that have one, and the widest gap of all of them is -0.32%. The US lines are also the source for `us_listing` (`NYSE`/`NASDAQ`/`ADR`/`OTC`/`none`), matched on the issuer rather than on the ticker.
- **Venue-official price rule** — where an exchange's own close could be obtained it is the price that is published; a third-party quote that differs is recorded, not averaged. No row in this artifact carries a `price_conflict` cell: every close in it is the scanner's venue close, and the index table publishes the exchange's own close where one was reported (the TAIEX is published at CNA's official 42,711.92 +2.52%, not Investing.com's +2.23%).
- **Carry-over detection** — a row is a carry-over when its close is **exactly** equal to the prior session's stored close **and** either its volume is zero or its `change_pct` is non-zero (the scanner's stale leftover). The comparison is against the **immediate** prior session only (9 November); the walk back through older files is used only to stamp `last_trade_date`.
- **CSV column count** — **18** (`date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`), unchanged from the 9 November session, so the archive's width has not moved since 5 November.
- **Files written** — 16 `<region>.csv` files (4,386 rows in total), `summary.md`, `_manifest.json`, `_excluded.json` and `_carryover.json` in `international-eod/2026-11-10/`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView per-country scanner | `POST scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan` with the top-level country filter | ok | {tot['universe_rows']:,} rows, {tot['unique_instruments']:,} unique instruments |
| TradingView America scanner | `POST scanner.tradingview.com/america/scan`, types `["stock","dr"]`, sorted by market cap, 3 pages | ok | 13,483 US lines used for `us_listing` and the cross-venue cap check |
| TradingView index scanner | `POST scanner.tradingview.com/global/scan`, types `["index"]` (SP:XJO, TSE:TOPIX, TSX:TSX, XETR:DAX, EURONEXT:PX1, FTSE:FTSEMIB, BME:IBC, OMXHEX:OMXH25, OMXCOP:OMXC20, ATHEX:GD …) | ok | 16 venue index levels; each one reconciles with the 9 November published close in the prior session's artifact |
| Frankfurter | `https://api.frankfurter.dev/v1/latest?base=USD` | ok | table dated 2026-11-10: EUR 0.89174, JPY 158.18, AUD 1.4485, CAD 1.4136, DKK 6.6661 |
| open.er-api | `https://open.er-api.com/v6/latest/USD` | ok | TWD 32.780875 (table updated Tue, 10 Nov 2026 00:02:31 UTC); agrees with Frankfurter to within 0.2% |
| Yahoo Finance JSON | `query1/query2.finance.yahoo.com/v8/finance/chart/...` | **429 rate-limited** | Not used for any published number; index levels come from the exchanges' own closes as reported on 10 Nov plus the TradingView venue index symbols |
| Market close reporting | AP, CNA / Focus Taiwan, ANSA, Anadolu / AA, Il Sole 24 Ore Radiocor, Reuters, Baystreet.ca, ABC News, Euronews, Samso, TradingView | ok | Used for the index levels, the session narrative and every catalyst in the movers table |

### Caveats

- **Unit caveat** — `market_cap` is USD; `open`/`high`/`low`/`close` are in the listing currency named in the `currency` column. The two are not comparable within a row.
- **Carry-over rows** — 77 published rows across the 16 regions did not trade today (the scanner returned the prior session's close). They are written as the source returned them, listed in `_carryover.json` with their `last_trade_date`, and excluded from every movers list. Canada accounts for 25 of them and Spain for 34.
- **The cross-venue cap check was run against the US depositary receipts only** - the source's OTC caps are not company-level (a US OTC line for an Australian issuer reads a few hundred dollars), and an ordinary US listing is not automatically the same issuer, so neither is a second reading of the cap.
- **A cap claim without a second reading is not publishable** — every published cap is either the issuer's own primary line or a carry from it, and the cross-venue check against the issuer's US line was run for every name that has one.
- **Widest cross-venue cap gaps** (the published cap is the primary line's; the US depositary receipt is the second reading - every one of them is inside 0.4%):
  - `ASX:RIO` (Rio Tinto Limited) — published $146.94B vs the US line `NYSE:RIO` at $147.41B (-0.32%)
  - `ASX:BHP` (BHP Group Ltd) — published $207.76B vs the US line `NYSE:BHP` at $208.41B (-0.31%)
  - `ASX:WDS` (Woodside Energy Group Ltd) — published $40.25B vs the US line `NYSE:WDS` at $40.37B (-0.31%)
  - `ASX:MSB` (Mesoblast Limited) — published $1.83B vs the US line `NASDAQ:MESO` at $1.84B (-0.31%)
  - `ASX:TLX` (Telix Pharmaceuticals Limited) — published $3.27B vs the US line `NASDAQ:TLX` at $3.28B (-0.31%)
  - `ASX:ELV` (Elevra Lithium Limited) — published $475M vs the US line `NASDAQ:ELVR` at $477M (-0.31%)
- **Issuer-country filter** — the universe is the scanner's **issuer** country, so a name TradingView files under another country is not in this file even when it trades there. GFL Environmental (TSX:GFL, -7.19% today) is tagged a United States issuer and is therefore absent from the Canada file, exactly as on 9 November.
- **The scanner is the close of record here** — every close in the CSVs is the scanner's venue close for 10 November. Where a wire reported an intraday level (Infineon at EUR 51.21 mid-day, Edenred at +3.2% in mid-morning trading) the close is published and the intraday figure is named in the catalyst instead of the other way round.
- **No company-specific driver was found for the names in `## No catalyst`**, and none is claimed for them; they are published separately rather than dropped, because a move without a source is still a move.
- **Sector rotation** (mean and median `change_pct` per sector over the published rows): technology/semiconductors led (Tokyo's Kokusai +14.36%, Taiwan's ASE +7.84%, Delta +9.91%, Paris's Edenred +6.37% on the Brazilian meal-voucher ruling), pharmaceuticals were the standout positive sector (Lundbeck +7.56%/+6.14% on the guidance raise), and precious metals were the clear negative (the Canadian gold cohort, -6.8% to -8.6%).

