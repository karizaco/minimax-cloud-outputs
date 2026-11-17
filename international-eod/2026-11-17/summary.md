# Cron #05 eod-international-daily — Tuesday, 17 November 2026

## TL;DR

- **A second, AI-led global selloff took every major board lower**: the STOXX 600 fell 1.75%, the DAX 2.08%, the AEX 2.14%, the TAIEX 2.31% and the Nikkei 1.34%, with the S&P/ASX 200 down 1.79% and the S&P/TSX Composite down 1.14% - Washington had tightened restrictions on AI-chip sales to China, Nvidia reports after the close for the first time without Jensen Huang at the helm, and Anthropic lists on Thursday; across the 16 boards 4,343 names were published and roughly three in four of them closed lower.
- **The one consequential single-name move was Deutsche Bank, down 6.00% to EUR30.94 after media reports based on leaked documents tied the bank to clients including Russian oligarchs, US President Donald Trump and the late financier Jeffrey Epstein - and it is not US-listed**: the moves a US trader can actually reach are SAP (-5.58%, ADR), ASML (-5.34%, ADR), BlackBerry (-7.33%, NYSE), Waste Connections (-8.12%, NYSE), Santacruz Silver (+14.91%, NASDAQ) and Avio (+14.90%, ADR, on ICEYE's EUR2.05bn bid).
- **The caveat that changes how to read it**: `market_cap` is in **USD** while `open`/`high`/`low`/`close` are in the **listing currency** (the `currency` column says which), Taiwan's -10% prints are **limit-downs** rather than calculated moves, and the ATHEX General's official close (2,637.69) came from the press because no vendor index exists for it.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,547 | 1,547 | **295** | $300M + vol ≥ 100,000 | 4 | 1222 | 25 | 1 | 0 | 0 | 0 |
| `jp` | NAG, SAPSE, TSE | 3,898 | 3,867 | **1,384** | $300M | 3 | 2479 | 0 | 1 | 0 | 2 | 0 |
| `tw` | TPEX, TWSE | 2,342 | 2,342 | **863** | $200M | 57 | 1422 | 0 | 0 | 0 | 3 | 0 |
| `ca` | CSE, TSX, TSXV | 4,297 | 2,703 | **618** | $200M | 60 | 1900 | 0 | 125 | 0 | 46 | 0 |
| `eu-de` | XETR | 4,305 | 709 | **123** | $300M + vol ≥ 50,000 | 4 | 396 | 186 | 0 | 0 | 0 | 0 |
| `eu-fr` | EURONEXT | 538 | 538 | **262** | $100M | 1 | 275 | 0 | 0 | 0 | 3 | 0 |
| `eu-it` | MIL | 378 | 378 | **179** | $100M | 2 | 197 | 0 | 0 | 0 | 5 | 0 |
| `eu-es` | BME | 231 | 231 | **136** | $100M | 23 | 72 | 0 | 0 | 0 | 28 | 0 |
| `eu-nl` | EURONEXT | 78 | 78 | **56** | $100M | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| `eu-be` | EURONEXT | 99 | 99 | **76** | $100M | 1 | 22 | 0 | 0 | 0 | 0 | 0 |
| `eu-at` | VIE | 65 | 65 | **51** | $100M | 3 | 11 | 0 | 0 | 0 | 4 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **27** | $50M | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| `eu-ie` | EURONEXT | 21 | 21 | **16** | $200M | 0 | 5 | 0 | 0 | 0 | 0 | 0 |
| `eu-fi` | OMXHEX | 189 | 189 | **101** | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| `eu-dk` | OMXCOP | 133 | 133 | **75** | $100M | 1 | 57 | 0 | 0 | 0 | 0 | 0 |
| `eu-gr` | ATHEX | 129 | 129 | **83** | $50M | 0 | 46 | 0 | 0 | 0 | 2 | 0 |
| **total** | | **18,281** | **13,060** | **4,345** | | **163** | **8214** | **211** | **127** | **0** | **93** | **0** |

`Universe` is every instrument the source returns for that country's own listings (the scanner's issuer-country filter, `type=stock`, so a foreign company's local line is not counted); `Unique instruments` collapses the same line quoted on several venues down to one line per share class; `Written` applies the per-region USD market-cap floor plus the region's volume gate. Every excluded row carries a reason from the closed set in `_excluded.json`, and the counts above are read from that file rather than estimated.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 8,883.20 | -161.50 / -1.79% | 2026-11-17 | TradingView SP:XJO; NewsWire (via PerthNow) and Samso Market Update, 17 Nov, both report 8,883.2, down 161.5 points, with ten of eleven sectors lower |
| jp | Nikkei 225 | 58,860.43 | -801.59 / -1.34% | 2026-11-17 | TradingView TVC:NI225 venue index read 58,860.21; Newson Japan and kabutaro777, 17 Nov, report 58,860.43, down 801.59 points |
| jp | TOPIX | 3,840.02 | -61.35 / -1.57% | 2026-11-17 | TradingView TSE:TOPIX venue index, which agrees to the decimal with the press; there is no Yahoo index symbol for the TOPIX |
| tw | TAIEX | 40,092.11 | -947.97 / -2.31% | 2026-11-17 | TradingView TWSE:IX0001 agrees to the decimal with Focus Taiwan/CNA, 17 Nov; Investing.com's -2.18% read is a third-party quote, not the close |
| ca | S&P/TSX Composite | 35,315.30 | -406.83 / -1.14% | 2026-11-17 | TradingView TSX:TSX venue index; Reuters, 17 Nov, had it 0.5% lower at 35,551.57 intraday at 10:35 ET |
| eu-de | DAX (Xetra) | 26,045.37 | -553.27 / -2.08% | 2026-11-17 | TradingView XETR:DAX venue index; Bloomberg and DPA, 17 Nov, confirm the technology-led fall |
| eu-fr | CAC 40 | 8,216.78 | -135.22 / -1.62% | 2026-11-17 | TradingView EURONEXT:PX1 venue index; DPA, 17 Nov, reported the CAC down 0.92% at the time of writing - an intraday reading, not the close |
| eu-it | FTSE MIB | 50,845.81 | -674.74 / -1.31% | 2026-11-17 | TradingView FTSE:FTSEMIB venue index |
| eu-es | IBEX 35 | 19,625.30 | -321.30 / -1.61% | 2026-11-17 | TradingView BME:IBC venue index |
| eu-nl | AEX | 1,109.89 | -24.24 / -2.14% | 2026-11-17 | TradingView EURONEXT:AEX venue index; the Irish Times, 17 Nov |
| eu-be | BEL 20 | 5,986.98 | -114.35 / -1.87% | 2026-11-17 | TradingView EURONEXT:BEL20 venue index |
| eu-at | ATX | 6,521.88 | -109.21 / -1.65% | 2026-11-17 | TradingView VIE:ATX venue index |
| eu-pt | PSI 20 | 9,593.72 | -116.07 / -1.20% | 2026-11-17 | TradingView EURONEXT:PSI20 venue index |
| eu-ie | ISEQ | 14,796.32 | -227.75 / -1.52% | 2026-11-17 | TradingView EURONEXT:ISEQ venue index; the Irish Times, 17 Nov, reports the ISEQ down 1.5% to 14,796.32 |
| eu-fi | OMX Helsinki 25 | 6,174.05 | -115.62 / -1.84% | 2026-11-17 | TradingView OMXHEX:OMXH25 venue index |
| eu-dk | OMX Copenhagen 20 | 1,656.42 | -29.80 / -1.77% | 2026-11-17 | TradingView OMXCOP:OMXC20 venue index |
| eu-gr | ATHEX General | 2,637.69 | -12.73 / -0.48% | 2026-11-17 | euro2day, 17 Nov 17:45, reports the General Index closing at 2,637.69, down 0.48%, after a low of 2,624.67; the ATHEX has no Yahoo symbol and no TradingView venue index |
| *context* | STOXX 600 | 650.72 | -11.59 / -1.75% | 2026-11-17 | TradingView STOXX:SXXP venue index; Bloomberg and the Irish Times, 17 Nov, report the pan-European index down 1.8% at the close with 92% of the constituents in the red |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 295 | -1.75% | 30 / 251 / 14 | -16.57% | +8.86% |
| jp | 1,384 | -1.10% | 248 / 1106 / 30 | -14.71% | +12.53% |
| tw | 863 | -1.86% | 148 / 685 / 30 | -10.00% | +10.00% |
| ca | 618 | -0.43% | 196 / 344 / 78 | -12.64% | +14.91% |
| eu-de | 123 | -1.43% | 24 / 99 / 0 | -8.47% | +4.15% |
| eu-fr | 262 | -1.26% | 36 / 197 / 29 | -50.00% | +9.60% |
| eu-it | 179 | -1.25% | 31 / 128 / 20 | -9.93% | +14.90% |
| eu-es | 136 | -1.02% | 18 / 82 / 36 | -6.41% | +2.72% |
| eu-nl | 56 | -1.37% | 4 / 52 / 0 | -5.34% | +3.11% |
| eu-be | 76 | -1.02% | 15 / 56 / 5 | -7.69% | +1.85% |
| eu-at | 51 | -1.27% | 14 / 30 / 7 | -5.30% | +2.92% |
| eu-pt | 27 | -0.55% | 5 / 17 / 5 | -4.44% | +9.77% |
| eu-ie | 16 | -1.41% | 3 / 11 / 2 | -8.13% | +0.95% |
| eu-fi | 101 | -1.28% | 19 / 79 / 3 | -4.99% | +4.65% |
| eu-dk | 75 | -0.78% | 15 / 57 / 3 | -4.49% | +1.69% |
| eu-gr | 83 | -0.18% | 30 / 38 / 15 | -2.38% | +5.33% |

An index move and the typical name regularly disagree, so both are published: the DAX fell 2.08% while the median German name fell 1.43%, but the German median understates the 4% moves in the chip and software names; the TSX's -1.14% came with a median written name at -0.16%, and Athens was the outlier - a -0.48% General Index with a median written name at +0.00% and 30 of 83 names higher.

## Top movers

Liquid names (volume ≥ 100,000 and market cap at or above the region's floor) whose move cleared ±5%, with the driver that was actually sourced. A row with no sourced driver is not here - it is under `## No catalyst`. Regions where no name cleared the threshold publish their largest liquid mover instead, marked *(fallback)*.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:CAT` | Catapult Sports Ltd. | **-16.57%** | 3.02 AUD | 6,033,921 | $755M | none | Fell 16.57% to A$3.02 after its first-half FY27 result: the Rule of 40 hit 45% and margins doubled, but the print missed the market's bar (Investing.com, 17 Nov; TheBull, 17 Nov; Kalkine, 17 Nov) |
| `ASX:IPH` | IPH Ltd. | **-13.42%** | 3.42 AUD | 5,843,779 | $682M | none | Fell 13.42% to A$3.42 after a four-month earnings decline as the organic-growth reset began, on the same day it appointed a new CEO and outlined its FY27 growth plan and passed all five resolutions at its AGM (Kalkine, 17 Nov; Small Caps, 17 Nov) |
| `ASX:SRL` | Sunrise Energy Metals Limited | **-11.00%** | 10.76 AUD | 786,001 | $1.41B | OTC | Fell 11.00% to A$10.76 with no company release for 17 November - it was sold with the resources complex as the ASX materials sector dropped 3.86% on iron ore hitting a four-year low and copper a four-month low, against a Morningstar note on its Mount Ridley/Grass Patch scandium resource (Mining.com.au, 17 Nov; Kalkine, 17 Nov; Trading Economics, 17 Nov) |
| `ASX:TNE` | Technology One Limited | **+8.86%** | 35.15 AUD | 2,498,334 | $7.13B | OTC | Rose 8.86% to A$35.15, the ASX 200's best performer, after a 17th consecutive record profit - FY26 revenue up and all FY26 targets met - and the appointment of a new CFO (Investing.com, 17 Nov; Stocks Down Under, 16 Nov; MarketScreener, 17 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:446A` | Northsand,Inc. | **-10.42%** | 2329 JPY | 3,399,600 | $1.12B | none | Fell 10.42% to Y2,329 after announcing the terms of a secondary offering (TipRanks, 17 Nov) |
| `TSE:4180` | Appier Group, Inc. | **-8.89%** | 1496 JPY | 1,763,300 | $1.06B | none | Fell 8.89% to Y1,496 with no company release for 17 November - it was sold with the AI-linked software names as US chip curbs and Nvidia uncertainty weighed on Asian data-centre stocks (Nikkei Asia, 17 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TWSE:3443` | Global Unichip Corp. | **-10.00%** | 6975 TWD | 3,602,185 | $31.49B | none | Fell 10.00% to NT$6,975, locked at its lower limit, with the whole AI-supply chain sold - the TAIEX lost 947.97 points as Washington tightened AI-chip export restrictions to China and the National Financial Stabilization Fund was believed to have stepped in (Focus Taiwan/CNA, 17 Nov; BigGo Finance, 17 Nov) |
| `TWSE:8046` | Nan Ya Printed Circuit Board Corporation | **-10.00%** | 792 TWD | 7,833,957 | $17.24B | none | Fell 10.00% to NT$792, locked at its lower limit, with the PCB and laminate complex sold after reports that Nvidia's next-generation Vera Rubin platform could face production-volume delays (Taiwan News/Business Next, 17 Nov; BigGo Finance, 17 Nov) |
| `TWSE:6213` | ITEQ Corporation | **-10.00%** | 432 TWD | 17,149,066 | $5.29B | none | Fell 10.00% to NT$432, locked at its lower limit, with no company release found for 17 November - sold with the rest of the electronics complex as the TAIEX closed 2.31% lower (BigGo Finance, 17 Nov) |
| `TWSE:3605` | ACES Electronics Co., Ltd. | **-10.00%** | 103.5 TWD | 7,140,347 | $611M | none | Fell 10.00% to NT$103.5, locked at its lower limit, with no company release found for 17 November - sold with the rest of the electronics complex (BigGo Finance, 17 Nov) |
| `TPEX:3081` | LandMark Optoelectronics Corp. | **-10.00%** | 1710 TWD | 3,867,381 | $5.86B | none | Fell 10.00% to NT$1,710, locked at its lower limit, with no company release found for 17 November - sold with the rest of the electronics complex as the Taipei exchange lost its last four-digit-priced stock (BigGo Finance, 17 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:SCZ` | Santacruz Silver Mining Ltd. | **+14.91%** | 10.56 CAD | 700,540 | $598M | NASDAQ | Rose 14.91% to C$10.56, the TSX's top gainer, after its third-quarter result: net income of US$37.6m as blockade-delayed shipments cleared (the deep dive, 17 Nov; Investorideas, 17 Nov; Motley Fool, 17 Nov) |
| `TSX:QBR.B` | Quebecor Inc. Class B | **-12.64%** | 57 CAD | 5,005,994 | $10.18B | OTC | Fell 12.64% to C$57 - the acquirer paid for its own bid: Quebecor's shares are down on its unsolicited US$21.96bn proposal for TELUS, which the target has said raises 'serious concerns' (WSJ, 17 Nov; Bloomberg/BNN, 16 Nov; Reuters, 17 Nov) |
| `TSX:GRGD` | Groupe Dynamite Inc. | **-12.02%** | 49.83 CAD | 712,717 | $4.32B | OTC | Fell 12.02% to C$49.83 after Spruce Point Capital Management disclosed a short position and published a strong-sell research opinion on the apparel retailer (Spruce Point, 17 Nov; Bloomberg, 17 Nov; Investing.com, 17 Nov) |
| `TSX:WCN` | Waste Connections, Inc. | **-8.12%** | 259.09 CAD | 1,537,985 | $49.36B | NYSE | Fell 8.12% to C$259.09 after a routine drilling operation at its Chiquita Canyon landfill in Los Angeles County went awry - a methane release sent six workers to hospital and prompted an emergency health order (Los Angeles Times, 17 Nov; KTLA, 17 Nov; MarketScreener, 17 Nov) |
| `TSX:BB` | BlackBerry Limited | **-7.33%** | 11.63 CAD | 3,968,518 | $5.15B | NYSE | Fell 7.33% to C$11.63 with no company release found for 17 November - sold with the technology and financial groups as Toronto waited for Nvidia's first results without Jensen Huang (Reuters, 17 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:DBK` | Deutsche Bank Aktiengesellschaft | **-6.00%** | 30.94 EUR | 10,498,861 | $66.02B | NYSE | Fell 6.00% to EUR30.94, the worst DAX constituent, after media reports based on leaked documents detailed the bank's dealings with clients including Russian oligarchs, US President Donald Trump and the late financier Jeffrey Epstein (Reuters, 17 Nov; Bloomberg, 17 Nov; DPA, 17 Nov) |
| `XETR:IOS` | IONOS Group SE | **-5.60%** | 35.06 EUR | 198,358 | $5.72B | none | Fell 5.60% to EUR35.06 after Thomas Saueressig was named to replace Achim Weiss as IONOS Group's CEO, a day after he resigned as SAP's Chief Customer Officer (Bloomberg, 17 Nov; TradingView, 17 Nov) |
| `XETR:SAP` | SAP SE | **-5.58%** | 201.5 EUR | 2,538,784 | $274.23B | ADR | Fell 5.58% to EUR201.50, Europe's biggest software company, after its Chief Customer Officer Thomas Saueressig resigned to become IONOS Group's CEO (Bloomberg, 17 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:OVH` | OVH Groupe S.A. | **-6.73%** | 13.85 EUR | 255,912 | $2.49B | none | Fell 6.73% to EUR13.85 with no negative company release - it launched its first open-source LLM, Olala Mini 7A1B, on 17 November but was sold with the European technology sector, which fell 3.9%, its steepest day since early February (ActuIA, 17 Nov; Irish Times, 17 Nov) |
| `EURONEXT:RMS` | Hermes International SCA | **-5.11%** | 1280.5 EUR | 145,304 | $155.42B | none | Fell 5.11% to EUR1,280.50 - the CAC 40's laggard - as the luxury complex dragged the index lower; Hermès has been under pressure since the heir to a reported US$9bn stake was placed under investigation (Luxus Plus, 17 Nov; Ideal Investisseur, 17 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:AVIO` | Avio SpA | **+14.90%** | 39.18 EUR | 7,871,309 | $1.86B | ADR | Rose 14.90% to EUR39.18 after Finland's satellite firm ICEYE made an all-cash takeover offer of about EUR2.05bn for the Vega launch-vehicle maker (Reuters, 17 Nov; FlightGlobal, 17 Nov; ANSA, 17 Nov) |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `BME:IDR` | Indra Sistemas, S.A. Class A | **-6.41%** | 54 EUR | 1,362,782 | $11.19B | ADR | Fell 6.41% to EUR54 as an anti-corruption probe put Indra's defence contracts in focus (ad-hoc-news.de, 17 Nov) |
| `BME:EDR` | eDreams ODIGEO | **-6.36%** | 4.635 EUR | 792,108 | $597M | OTC | Fell 6.36% to EUR4.635 after its Q2 FY2027 results: revenue grew 5% and subscribers reached 8.2m, but the shares fell as the market read the growth investment (Marketscreener, 17 Nov; Investing.com transcript, 17 Nov) |

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ASML` | ASML Holding NV | **-5.34%** | 1236.8 EUR | 995,320 | $549.32B | ADR | Fell 5.34% to EUR1,236.80 after Washington tightened restrictions on AI-chip sales to China - ASML was the European technology sector's largest faller (Reuters, 17 Nov; Irish Times, 17 Nov) |

### eu-be

No moved name cleared the threshold with a sourced driver in this region.

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | **-3.24%** | 113.4 EUR | 159,811 | $5.01B | OTC | Fell 3.24% to EUR113.40, the ATX's largest liquid faller, with no company release found for 17 November - sold with the European technology complex (TradingView venue index, 17 Nov) |

### eu-pt

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:JMT` | Jeronimo Martins, SGPS S.A. | **-3.00%** | 19.4 EUR | 1,118,427 | $13.85B | ADR | Fell 3.00% to EUR19.40, the PSI 20's largest liquid faller, with no company release found for 17 November (TradingView venue index, 17 Nov) |

### eu-ie

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:C5H` | Cairn Homes PLC | **-2.37%** | 2.675 EUR | 400,331 | $1.85B | none | Fell 2.37% to EUR2.675, the ISEQ's largest liquid faller, with no company release found for 17 November - the Dublin session was led lower by Ryanair, Kingspan and Kerry Group (Irish Times, 17 Nov) |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:NOKIA` | Nokia Oyj | **-3.83%** | 6.934 EUR | 26,519,260 | $44.91B | none | Fell 3.83% to EUR6.934, the OMX Helsinki 25's largest liquid faller, with no company release found for 17 November (TradingView venue index, 17 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:ZEAL` | Zealand Pharma A/S | **-4.25%** | 229.6 DKK | 595,947 | $2.34B | ADR | Fell 4.25% to DKK229.60, the OMX Copenhagen 20's largest liquid faller, with no company release found for 17 November (TradingView venue index, 17 Nov) |

### eu-gr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ATHEX:GEKTERNA` | Gek Terna S.A. | **+3.66%** | 43.02 EUR | 197,437 | $4.42B | OTC | Rose 3.66% to EUR43.02, the ATHEX's largest liquid gainer, as GEK Terna posted strong gains against the market's direction on a session when the banks were sold (euro2day, 17 Nov) |
| `ATHEX:ALPHA` | Alpha Bank S.A. | **-2.38%** | 4.707 EUR | 6,959,383 | $11.75B | none | Fell 2.38% to EUR4.707 as sellers took profits in the banking sector - the Athens banking index fell 1.03% and led the General Index's 0.48% decline (euro2day, 17 Nov) |

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a +100% or a -50% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:VEN | Vintage Energy Ltd. | **+100.00%** | 1,202,590 | below the $300M cap floor |
| ASX:LU7 | Lithium Universe Limited | **+100.00%** | 800,000 | below the $300M cap floor |
| ASX:MMR | MEC Resources Ltd | **+100.00%** | 963,428 | below the $300M cap floor |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:2388 | Wedge Holdings CO., LTD. | **+77.78%** | 25,961,400 | below the $300M cap floor |
| TSE:3624 | Axel Mark Inc. | **+42.62%** | 17,208,600 | below the $300M cap floor |
| TSE:4586 | Medrx Co., Ltd. | **+28.21%** | 9,832,100 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:7759 | Sunhawk Vision Biotech, Inc. | **-11.56%** | 195,798 | below the $200M cap floor |
| TPEX:3117 | Tecstar Technology Co., Ltd. | **-11.47%** | 382,623 | below the $200M cap floor |
| TPEX:7943 | LIONIC Corp. | **-10.88%** | 150,335 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSXV:SAF.H | Seasif Exploration Inc. | **+100.00%** | 2,963,000 | below the $200M cap floor |
| CSE:ENBI.X | Entheon Biomedical Corp. | **+66.67%** | 121,500 | below the $200M cap floor |
| CSE:ROBO | Humanoid Global Holdings Corp. | **+63.64%** | 322,875 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| XETR:TPG0 | Platform Group SE & Co. KGaA | **-44.24%** | 1,739,141 | below the $300M cap floor |
| XETR:AB9 | ABO Energy GmbH & Co. KGaA | **+24.76%** | 332,409 | below the $300M cap floor |
| XETR:SNG | SINGULUS TECHNOLOGIES AG | **-8.42%** | 293,753 | below the $300M cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALTHO | Metavisio SA | **+14.29%** | 4,769,412 | below the $100M cap floor |
| EURONEXT:ALNEV | Neovacs SA | **-13.24%** | 764,182 | below the $100M cap floor |
| EURONEXT:ALDBT | Douaisienne de Basse Tension SAS | **+8.46%** | 6,018,462 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:ENY | Energy SpA | **+32.88%** | 239,000 | below the $100M cap floor |
| MIL:RN | Risanamento S.p.A. | **-12.39%** | 23,808,335 | below the $100M cap floor |
| MIL:MTV | Mondo TV S.p.A. | **-12.33%** | 3,875,378 | below the $100M cap floor |

### eu-es

No name below the cap floor moved hard enough on volume to publish.

### eu-nl

No name below the cap floor moved hard enough on volume to publish.

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:OXUR | Oxurion NV | **-25.00%** | 1,050,429 | below the $100M cap floor |

### eu-at

No name below the cap floor moved hard enough on volume to publish.

### eu-pt

No name below the cap floor moved hard enough on volume to publish.

### eu-ie

No name below the cap floor moved hard enough on volume to publish.

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:NANOFH | Nanoform Finland Oyj | **+5.11%** | 242,461 | below the $100M cap floor |
| OMXHEX:EAGLE | Eagle Filters Group Plc Class A | **-5.07%** | 649,623 | below the $100M cap floor |

### eu-dk

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXCOP:MOVINN | Movinn A/S | **-15.44%** | 125,586 | below the $100M cap floor |

### eu-gr

No name below the cap floor moved hard enough on volume to publish.

## No catalyst

The names that moved with **no sourced driver**: no company release, no filing, no analyst action, and no sector or macro move behind them that could be sourced. Separate, so they do not dilute the mover table.

### au

No moved name without a sourced driver in this region.

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TSE:6834` | Seikoh Giken Co., Ltd. | **-14.71%** | 3625 JPY | 2,263,600 | $1.24B | none | Fell 14.71% to 3625 JPY with no driver found - no release for 17 November could be sourced, and no sector move explains it |
| `TSE:319A` | Next Generation Technology Group, Inc. | **-12.74%** | 21510 JPY | 126,300 | $1.37B | none | Fell 12.74% to 21510 JPY with no driver found - no release for 17 November could be sourced, and no sector move explains it |
| `TSE:4547` | Kissei Pharmaceutical Co., Ltd. | **+12.53%** | 4400 JPY | 544,200 | $1.00B | none | Rose 12.53% to 4400 JPY with no driver found - no release for 17 November could be sourced, and no sector move explains it |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TWSE:3704` | Zyxel Group Corporation | **+10.00%** | 38.5 TWD | 8,965,294 | $431M | none | Rose 10.00% to 38.5 TWD with no driver found - no release for 17 November could be sourced, and no sector move explains it |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `TSX:NGEX` | NGEX Minerals Limited | **-8.67%** | 18.12 CAD | 233,975 | $3.01B | OTC | Fell 8.67% to 18.12 CAD with no driver found - no release for 17 November could be sourced, and no sector move explains it |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `XETR:NEM` | Nemetschek SE | **-5.06%** | 60.95 EUR | 264,784 | $8.16B | ADR | Fell 5.06% to 60.95 EUR with no driver found - no release for 17 November could be sourced, and no sector move explains it |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ADOC` | Adocia SA | **-10.14%** | 3.792 EUR | 684,987 | $105M | none | Fell 10.14% to 3.792 EUR with no driver found - no release for 17 November could be sourced, and no sector move explains it |
| `EURONEXT:IVA` | Inventiva SA | **-8.25%** | 2.89 EUR | 553,995 | $829M | ADR | Fell 8.25% to 2.89 EUR with no driver found - no release for 17 November could be sourced, and no sector move explains it |
| `EURONEXT:NANO` | Nanobiotix SA | **-6.16%** | 24.7 EUR | 124,853 | $1.48B | ADR | Fell 6.16% to 24.7 EUR with no driver found - no release for 17 November could be sourced, and no sector move explains it |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `MIL:BFF` | BFF Bank SpA | **-9.93%** | 1.261 EUR | 8,949,264 | $291M | none | Fell 9.93% to 1.261 EUR with no driver found - no release for 17 November could be sourced, and no sector move explains it |
| `MIL:EGLA` | EuroGroup Laminations S.p.A | **-9.13%** | 0.7265 EUR | 2,907,863 | $143M | none | Fell 9.13% to 0.7265 EUR with no driver found - no release for 17 November could be sourced, and no sector move explains it |
| `MIL:IF` | Banca IFIS S.p.A. | **-8.24%** | 8.8 EUR | 772,715 | $636M | none | Fell 8.24% to 8.8 EUR with no driver found - no release for 17 November could be sourced, and no sector move explains it |

### eu-es

No moved name without a sourced driver in this region.

### eu-nl

No moved name without a sourced driver in this region.

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Note |
|---|---|---|---|---|---|---|---|
| `EURONEXT:ONTEX` | Ontex Group N.V. | **-7.69%** | 1.272 EUR | 322,494 | $123M | OTC | Fell 7.69% to 1.272 EUR with no driver found - no release for 17 November could be sourced, and no sector move explains it |

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

- **Universe** - the TradingView per-country scanner, `types=["stock"]`, filtered on the issuer's own country (`filter: [{left: country, equal, <country>}]`). One pull per region; the completeness test is a SET test (the rows returned equal the pull's `totalCount`), and every region returned 100% of its names - **18,281 stock rows across the 16 countries**, every pull equal to its totalCount. The `type` filter matters: the same country endpoints also carry funds and structured products, which would have added 5,982 rows that are not equities.
- **Venue collapse** - one line per symbol and share class, and the issuer's **primary** venue wins (au ASX; jp TSE, NAG, FSE, SAPSE; tw TWSE, TPEX; ca TSX, TSXV, CSE, NEO; eu-de XETR, FWB, LSX, LS, GETTEX, DUS, MUN, SWB, TRADEGATE, HAM, HAN; the single-venue regions keep their venue), then reported cap, then volume, then cap - the busiest venue is not the authoritative venue. A line whose implied prior close (`close / (1 + change/100)`) fails to reconcile with the **prior session's published close for the same symbol** by more than 5% is a stale venue print and is dropped; **no line was dropped today** (`off-official rows` = 0 in every region), and a row whose close is unchanged is a carry-over, not a stale print.
- **Cap carrier** - the cap is resolved to the issuer's PRIMARY (common) line and converted ONCE with that line's currency; every other line of the issuer publishes that same USD figure in `cap_source_symbol`, and a group with no common line is excluded as `issuer_unresolved` rather than published with a borrowed cap. The floor is applied to the group, so a published preferred never points at a cap source that is not in the file. Canada shows the rule working: **125 rows are excluded as `issuer_unresolved`** because their issuer's common line sits on another venue, and their cap could not be carried without borrowing it.
- **Floors (USD)** - au $300M + volume ≥ 100,000; jp $300M; tw $200M; ca $200M; eu-de $300M + volume ≥ 50,000; eu-fr/it/es/nl/be/at $100M; eu-pt/gr $50M; eu-ie $200M; eu-fi/dk $100M. The floor is applied AFTER the conversion, never as a server-side screener filter (`market_cap_basic` on a per-country endpoint is in the listing currency).
- **FX** - open.er-api's base-USD table for 17 November 2026 (updated Tue, 17 Nov 2026 00:02:31 +0000: EUR 0.908584, JPY 159.580113, AUD 1.483068, CAD 1.42937, DKK 6.789305, TWD 32.977405). The table quotes **local units per 1 USD**, so the conversion is a division: `usd_cap = market_cap_basic / FX_per_USD[currency]`. Share-count reconciliation confirms the direction - `market_cap_basic / close` returns CBA 1,678.7m shares, Westpac 3,465.5m, NAB 3,197.0m, ANZ 3,037.2m, BHP 5,347.9m, all the issuers' real counts, so the published USD caps are the issuers' own company-level caps.
- **Cross-venue cap check** - the America scanner (13,533 rows, `types=["stock","dr"]`) is the second reading on every issuer that has a US line. **1,062 published issuers matched**, and the large caps agree to within a tenth of a percent: ASX:BHP $196.10bn vs NYSE:BHP $195.88bn (0.11%), XETR:SAP $274.23bn vs NYSE:SAP $273.95bn (0.10%), EURONEXT:ASML $549.32bn vs NASDAQ:ASML $548.77bn (0.10%), ASX:CBA $192.92bn vs OTC:CMWAY $192.71bn (0.11%), ASX:RIO $138.30bn vs NYSE:RIO $138.41bn (0.08%), MIL:AVIO $1.86bn vs OTC:AVVSY $1.85bn (0.10%). **37 names disagree by more than 10%** and are a finding, not a defect to hide: most are lines whose US market cap covers a different share base (an ADR or OTC line quoted for one share), and the one clean exception in the movers tables is **TSX:SCZ, 13.2%** ($597.9m published against $689.1m on NASDAQ:SCZM) - the TSX line's cap is published and the delta is recorded here.
- **`us_listing`** - the America scanner, matched on the ISSUER (the US line's depositary-receipt wording is cut, the corporate-form words are normalised, and a US line whose name is SHORTER than the local line is a different issuer and does not match). **A depositary receipt is published as `ADR` wherever it sits; an issuer's own US listing is published as `NYSE`/`NASDAQ`; an OTC quotation is `OTC`. This is a change from the 2026-11-16 session**, which labelled ASX:BHP, XETR:SAP, EURONEXT:ASML and MIL:AVIO `OTC` because the matcher took the OTC line; they are `ADR` today, and 520 of the 4,343 published rows now carry `ADR` against 447 `OTC`, 164 `NYSE`, 30 `NASDAQ` and 3,182 `none`.
- **Venue-official price rule** - where an exchange's own auction/close is published it is the price, and the row carries the conflict in `price_conflict`. **No row-level conflict was found today**: the scanner close stood for every published row and every `price_conflict` cell is empty. The one venue-official price in this artifact is at index level - the ATHEX General's official close 2,637.69 (euro2day, 17 Nov), which no vendor index covers.
- **CSV schema** - **18 columns** (`date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`), unchanged from the 2026-11-16 session. The numeric format is unchanged too and was regression-tested against the previous published file: **105,275 numeric cells re-formatted, 105,274 byte-for-byte identical** (prices 4 decimals with trailing zeros stripped, `volume` and `market_cap` integers, `change_pct` and `pe_ratio` at full precision). The single difference is one cell the previous session itself wrote in scientific notation (`1.3610846959619412e-05`), which this run writes as `0.000013610847` - the same double, in the decimal form every other cell in the archive uses.
- **Files written** - `international-eod/2026-11-17/`: 16 region CSVs (`au.csv` … `eu-gr.csv`), `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView country scanner (16 regions) | scanner.tradingview.com/{au,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan, types=stock, filter country | ok | 18,281 stock rows across the 16 regions; every pull returned exactly its `totalCount` |
| TradingView America scanner (`us_listing` + ADR cap reading) | scanner.tradingview.com/america/scan, types=[stock,dr], sorted on a stable name sort | ok | 13,533 rows, union = totalCount; 1,062 published issuers matched to a US line |
| TradingView venue indices | scanner.tradingview.com/global/scan, 18 index tickers | ok | 17 index closes (16 regions + the STOXX 600); the ASX index is `SP:XJO` and the Nikkei `TVC:NI225` |
| ATHEX official close | euro2day.gr, 17 Nov 2026 17:45 | ok | the General Index closed at 2,637.69, down 0.48% - the ATHEX has no Yahoo symbol and no TradingView venue index |
| Yahoo chart API | query1.finance.yahoo.com/v8/finance/chart, daily bars for the index proxies | degraded | **HTTP 429 (Too Many Requests) on every request from this egress**, including the cookie+crumb handshake, so no index bar could be pulled; the index levels are the TradingView venue indices, cross-checked against the press instead |
| open.er-api | open.er-api.com/v6/latest/USD | ok | the 17 Nov 2026 00:02:31 UTC table, 6 currencies |
| Prior published sessions (2026-11-16 … 2026-11-09) | karizaco/minimax-cloud-outputs, international-eod/<date>/<region>.csv | ok | 6 sessions per region, used for the stale-print reconciliation and the carry-over walk-back |
| Google News RSS + web search | news.google.com/rss/search (when:2d) and the web search tool | ok | every catalyst above carries a source and a date; names with no company release found are listed under `## No catalyst` |

### Caveats

- **The day's driver was the AI trade, and it was a two-day unwind**: Washington tightened restrictions on AI-chip sales to China, Nvidia reported after the close for the first time without Jensen Huang at the helm, and Anthropic lists on Thursday - the Philadelphia Semiconductor Index fell 5.28% overnight and the Nasdaq 2.49%, and the selling ran from Taipei (TAIEX -2.31%) through Tokyo (Nikkei -1.34%) into Europe (STOXX 600 -1.75%, DAX -2.08%, AEX -2.14%). **Deutsche Bank's -6.00% was the one company-specific shock in Europe** (leaked documents on client dealings); everything else that moved moved with its sector.
- **The unit convention is the standing caveat**: `market_cap` is in **USD**, while `open`/`high`/`low`/`close` are in the **listing currency** - the `currency` column says which, and the cap is the only USD number in the row.
- **Taiwan's -10% prints are limit-downs, not calculated moves** - TWSE and TPEX cap a daily move at ±10%, so a -10.00% close is a limit print and the market was shut at that price; the same applies to the ASX's and the Nordic boards' smaller bands. Taiwan's index was also volatile: it traded between 39,786.45 and 41,533.84, and dealers said the National Financial Stabilization Fund was believed to have intervened to hold it above 40,000.
- **Carry-over rows** - 93 published rows carry a close from an earlier session (zero volume, or the scanner's stale change field beside an unchanged close): 53 last traded on 16 November, 14 on 13 November, 2 on 12 November, and 24 are not in the archive before 9 November (almost all Canadian preferred lines that do not trade). They stay in the CSVs because the schema is fixed, each one is listed in `_carryover.json` with its last trade date, and they are excluded from every mover list.
- **Illiquid lines move in percent, not in money** - `EURONEXT:ALTOO` closed at EUR0.0002, -50.00%, on 11.8m shares, and `EURONEXT:ALECR` shows -18.48% on a single share; their percentages are real but their prices carry no information, and they are published for completeness rather than as signals.
- **The Canadian preferred lines are the carry-over tail** - 46 of Canada's 93 carry-overs are preferred or floating-rate lines that trade in the hundreds of shares; their caps are the issuer's company-level cap carried from the common line, which is why a `preferred` row never outranks the issuer's `common` row on cap.
- **Santacruz Silver's cap is a finding** - the TSX line publishes $597.9m against $689.1m on its NASDAQ line, a 13.2% gap; the TSX figure is published and the delta is recorded here rather than averaged away.
- **No off-official venue rows today** - every region's primary-venue line reconciled with the prior session's close for the same instrument, so no line was dropped as a stale venue print.
- **Sector rotation** (mean `change_pct` per sector over the written rows) is not a section of its own; the per-region read is carried here and uses the same rows:

  - `au` - the best sector was Transportation (-0.56% mean over 6 names) and the worst Electronic Technology (-5.76% over 6); the median written name closed -1.75%.
  - `jp` - the best sector was Consumer Non-Durables (+0.03% mean over 79 names) and the worst Energy Minerals (-2.79% over 6); the median written name closed -1.10%.
  - `tw` - the best sector was Transportation (-0.54% mean over 21 names) and the worst Producer Manufacturing (-3.63% over 119); the median written name closed -1.86%.
  - `ca` - the best sector was Utilities (-0.01% mean over 46 names) and the worst Technology Services (-2.83% over 20); the median written name closed -0.43%.
  - `eu-de` - the best sector was Process Industries (+0.05% mean over 12 names) and the worst Technology Services (-4.31% over 9); the median written name closed -1.43%.
  - `eu-fr` - the best sector was Distribution Services (-0.31% mean over 7 names) and the worst Technology Services (-4.93% over 22); the median written name closed -1.26%.
  - `eu-it` - the best sector was Technology Services (+0.55% mean over 9 names) and the worst Commercial Services (-1.96% over 9); the median written name closed -1.25%.
  - `eu-es` - the best sector was Process Industries (-0.09% mean over 4 names) and the worst Consumer Services (-1.65% over 8); the median written name closed -1.02%.
  - `eu-nl` - the best sector was Consumer Non-Durables (-1.06% mean over 4 names) and the worst Technology Services (-2.89% over 4); the median written name closed -1.37%.
  - `eu-be` - the best sector was Producer Manufacturing (-0.36% mean over 4 names) and the worst Industrial Services (-1.96% over 4); the median written name closed -1.02%.
  - `eu-at` - the best sector was Non-Energy Minerals (-0.08% mean over 4 names) and the worst Producer Manufacturing (-1.74% over 7); the median written name closed -1.27%.
  - `eu-pt` - the best sector was Consumer Services (+0.35% mean over 4 names) and the worst Process Industries (-0.37% over 4); the median written name closed -0.55%.
  - `eu-ie` - the best sector was Finance (-0.35% mean over 5 names) and the worst Finance (-0.35% over 5); the median written name closed -1.41%.
  - `eu-fi` - the best sector was Consumer Services (+0.24% mean over 5 names) and the worst Electronic Technology (-2.33% over 8); the median written name closed -1.28%.
  - `eu-dk` - the best sector was Consumer Services (-0.01% mean over 6 names) and the worst Health Technology (-1.58% over 11); the median written name closed -0.78%.
  - `eu-gr` - the best sector was Process Industries (+2.21% mean over 5 names) and the worst Distribution Services (-0.60% over 4); the median written name closed -0.18%.
