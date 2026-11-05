# Cron #05 eod-international-daily — Thursday, 05 November 2026

## TL;DR

- **Risk-on in materials, risk-off in AI hardware.** Australia closed +2.61% at 9,065.10 with the S&P/ASX 200 Materials index +7.2% (its best day since March 2020) and gold +5.2% in two sessions, while Taiwan's TAIEX fell 3.20% and Europe's chip complex sold off; **1,375 Japanese names** printed, with the median name up +2.36% while the Nikkei fell 1.79%.
- **The most consequential move is NextDC (ASX:NXT, +50.84%)** — Goodman's and Digital Realty's joint 9.9% bookbuild turned an embattled data-centre operator into a takeover target and lifted the whole ASX technology complex; the other extreme is Taiwan's AI hardware complex, where four names hit the −10.00% limit.
- **Read the numbers with the unit convention in mind: `market_cap` is USD, while every price is in the listing currency** (`currency` column) — a ¥2,335 close and a €1,250 close are not comparable, and the caps are; and note that the 18-column schema is new today (the 4 Nov files were 14 columns).

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,562 | 1,562 | **306** | $300M + vol ≥ 100k | 4 | 1,239 | 10 | 3 | 0 | 0 | 0 |
| `jp` | TSE | 3,901 | 3,869 | **1,375** | $300M | 3 | 2,377 | 0 | 3 | 0 | 0 | 111 |
| `tw` | TWSE, TPEX | 2,334 | 2,334 | **885** | $200M | 54 | 1,386 | 0 | 9 | 0 | 1 | 0 |
| `ca` | TSX, TSXV, CSE | 4,304 | 2,721 | **605** | $200M | 134 | 1,774 | 0 | 192 | 0 | 44 | 16 |
| `eu-de` | XETR, FWB | 4,308 | 499 | **121** | $300M + vol ≥ 50k | 2 | 200 | 77 | 11 | 0 | 0 | 88 |
| `eu-fr` | EURONEXT | 561 | 561 | **273** | $100M | 3 | 285 | 0 | 0 | 0 | 5 | 0 |
| `eu-it` | MIL | 392 | 392 | **179** | $100M | 2 | 211 | 0 | 0 | 0 | 3 | 0 |
| `eu-es` | BME | 271 | 271 | **147** | $100M | 34 | 90 | 0 | 0 | 0 | 33 | 0 |
| `eu-nl` | EURONEXT | 83 | 83 | **62** | $100M | 0 | 21 | 0 | 0 | 0 | 0 | 0 |
| `eu-be` | EURONEXT | 103 | 103 | **77** | $100M | 3 | 23 | 0 | 0 | 0 | 1 | 0 |
| `eu-at` | VIE | 65 | 65 | **50** | $100M | 3 | 12 | 0 | 0 | 0 | 0 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **27** | $50M | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| `eu-fi` | OMXHEX | 188 | 188 | **101** | $100M | 4 | 83 | 0 | 0 | 0 | 0 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 58 | 0 | 0 | 0 | 1 | 0 |
| `eu-gr` | ATHEX | 128 | 128 | **86** | $50M | 0 | 40 | 0 | 2 | 0 | 0 | 0 |
| **total** | | **18,384** | **12,960** | **4,386** | | **247** | **7,805** | **87** | **220** | **0** | **88** | **215** |

`Universe` is every instrument the source returns for that country's own listings; `Unique instruments` collapses the same instrument quoted on several venues down to one line; `Written` applies the per-region USD market-cap floor plus the region's volume gate. Every excluded row carries a reason from the closed set in `_excluded.json`.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| `au` | S&P/ASX 200 | **9,065.10** | +230.60 / **+2.61%** | 2026-11-05 | Yahoo ^AXJO; MarketIndex and Samso (9,065.1, +230.6) |
| `jp` | Nikkei 225 | **61,077.90** | -1,110.73 / **-1.79%** | 2026-11-05 | Jiji closing report 15:31 JST (61,077.90, −1,110.73) |
| `jp` | TOPIX | **3,940.39** | +45.01 / **+1.16%** | 2026-11-05 | Jiji closing report 15:31 JST (3,940.39, +45.01) |
| `tw` | TAIEX | **41,574.72** | -1,374.19 / **-3.20%** | 2026-11-05 | CNA/Focus Taiwan; Taiwan Index Plus; TWSE official board |
| `ca` | S&P/TSX Composite | **35,605.27** | -736.13 / **-2.03%** | 2026-11-05 | Yahoo ^GSPTSE settled daily bar (16:00 ET) |
| `eu-de` | DAX (Xetra) | 26,325.01 | -112.66 / -0.43% | 2026-11-05 | Yahoo ^GDAXI (Xetra close) |
| `eu-fr` | CAC 40 | 8,205.37 | +27.48 / +0.34% | 2026-11-05 | Yahoo ^FCHI |
| `eu-it` | FTSE MIB | **50,505.87** | -525.15 / **-1.03%** | 2026-11-05 | Yahoo FTSEMIB.MI |
| `eu-es` | IBEX 35 | 19,486.00 | +115.10 / +0.59% | 2026-11-05 | Yahoo ^IBEX |
| `eu-nl` | AEX | 1,129.22 | -7.07 / -0.62% | 2026-11-05 | Yahoo ^AEX |
| `eu-be` | BEL 20 | 6,015.09 | +36.08 / +0.60% | 2026-11-05 | Yahoo ^BFX |
| `eu-at` | ATX | 6,511.40 | -7.12 / -0.11% | 2026-11-05 | Yahoo ^ATX |
| `eu-pt` | PSI 20 | 9,483.21 | +91.64 / +0.98% | 2026-11-05 | Yahoo PSI20.LS |
| `eu-ie` | ISEQ | 14,803.15 | -49.68 / -0.33% | 2026-11-05 | Yahoo ^ISEQ |
| `eu-fi` | OMX Helsinki 25 | 6,254.30 | -35.43 / -0.56% | 2026-11-05 | Yahoo ^OMXH25 |
| `eu-dk` | OMX Copenhagen 20 | **1,669.03** | -23.43 / **-1.38%** | 2026-11-05 | Yahoo ^OMXC20 (5 Nov bar; prior close 1,692.46 from Yahoo and the 4 Nov archive) |
| `eu-gr` | ATHEX General | **2,611.41** | -51.04 / **-1.92%** | 2026-11-05 | Euronext Athens official historical data; euro2day (2,611.41, −1.92%) |
| *context* | STOXX 600 | 654.87 | −2.53 / −0.38% | 2026-11-05 | Yahoo ^STOXX; Reuters (653.55, −0.6% at 16:11 GMT) |

**One election, two opposite reactions.** The Democratic sweep in the US midterms (3 Nov) was read as a risk-on event for cyclicals and materials — the Dow rallied 3.0% on 4 Nov and the ASX materials index jumped 7.2% on 5 Nov — and as a direct threat to the pace of AI data-centre build-out. Nomura's Wataru Akiyama: “Funds that had previously been flowing into AI and semiconductors have shifted to other sectors… the Democrats' gains will lead to delays in data-centre plans” (The Star, 5 Nov). The Nasdaq then confirmed a correction on 5 Nov, and Europe closed lower with the tech sector −3.9% (Reuters).

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max | Cap-weighted |
|---|---|---|---|---|---|---|
| `au` | 306 | +3.27% | 259 / 40 / 7 | -13.22% | +50.84% | +2.91% |
| `jp` | 1,375 | +2.36% | 974 / 392 / 9 | -23.06% | +22.80% | +1.20% |
| `tw` | 884 | -3.59% | 108 / 742 / 34 | -22.60% | +10.18% | -3.44% |
| `ca` | 561 | -0.91% | 135 / 391 / 35 | -31.15% | +8.70% | -2.04% |
| `eu-de` | 121 | +0.00% | 60 / 58 / 3 | -23.98% | +11.47% | -0.40% |
| `eu-fr` | 268 | +0.00% | 127 / 119 / 22 | -16.73% | +12.06% | +0.58% |
| `eu-it` | 176 | -0.70% | 53 / 108 / 15 | -9.28% | +5.49% | -0.82% |
| `eu-es` | 114 | +0.00% | 56 / 50 / 8 | -21.10% | +11.58% | +0.70% |
| `eu-nl` | 62 | -0.49% | 21 / 38 / 3 | -7.30% | +4.51% | -2.82% |
| `eu-be` | 76 | +0.00% | 37 / 33 / 6 | -6.17% | +4.33% | +0.56% |
| `eu-at` | 50 | +0.00% | 18 / 23 / 9 | -18.16% | +8.57% | +0.55% |
| `eu-pt` | 27 | +0.00% | 13 / 11 / 3 | -5.71% | +5.57% | +0.43% |
| `eu-ie` | 17 | +0.18% | 10 / 5 / 2 | -3.02% | +2.68% | -0.33% |
| `eu-fi` | 101 | -0.79% | 32 / 64 / 5 | -12.29% | +16.02% | -0.87% |
| `eu-dk` | 74 | -0.11% | 32 / 37 / 5 | -14.61% | +15.43% | -1.51% |
| `eu-gr` | 86 | -0.57% | 24 / 52 / 10 | -7.39% | +10.00% | -0.40% |

The breadth table is the one to read when the index and the typical name disagree — and today they disagree twice: **Japan** printed a −1.79% Nikkei against a **+1.16% TOPIX** and a +2.36% median name (161 of 225 Nikkei components rose; 1,130 TSE Prime names rose against 410 that fell), and **the Netherlands** printed an AEX −0.62% against a −2.82% cap-weighted snapshot, because ASML — roughly 60% of the Dutch cap weight — fell 6.55% while the index barely moved. Carry-over rows are excluded from these counts.

## Top movers

Liquid names (volume ≥ 100k **and** market cap ≥ $1B) whose move cleared ±5%, with the driver that was actually sourced. A row with no sourced driver is not here — it is under `## No catalyst`.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:NXT` | Nextdc Limited | **+50.84%** | 9.85 AUD | 81,639,234 | $3.47B | OTC | Goodman Group and US-listed Digital Realty (vehicle Ackland Investments) ran an after-market bookbuild on 4 Nov for up to 9.9% at A$9.50; NextDC's board called it “opportunistic” and hired Barrenjoey/UBS (CNBC, The Age, AFR, Samso, 5 Nov) |
| `ASX:NEU` | Neuren Pharmaceuticals Limited | **+17.49%** | 23.24 AUD | 1,096,995 | $1.76B | OTC | Q3 FY26 DAYBUE net sales +39% with full-year guidance upgraded (company announcement, 5 Nov 09:57) |
| `ASX:GMD` | Genesis Minerals Limited | **+15.43%** | 7.33 AUD | 13,888,782 | $5.22B | OTC | No company release; the gold bid — gold +5.2% in two sessions to US$4,136/oz, All Ords Gold Index +11.95% (MarketIndex, 5 Nov) |
| `ASX:OBM` | Ora Banda Mining Ltd. | **+15.23%** | 1.475 AUD | 9,133,802 | $1.74B | OTC | No company release; the same gold bid — All Ords Gold Index +11.95% (MarketIndex, 5 Nov) |
| `ASX:RSG` | Resolute Mining Limited | **+14.68%** | 1.25 AUD | 8,305,792 | $1.63B | ADR | No company release; the same gold bid — All Ords Gold Index +11.95% (MarketIndex, 5 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:6590` | Shibaura Mechatronics Corp. | **-23.06%** | 2335 JPY | 4,515,100 | $1.32B | OTC | Q2 FY27 earnings miss — EPS ¥35.58 against a consensus of ¥701.7; the shares fell 23% (Yahoo Finance results page, StockAnalysis, moomoo, 5 Nov) |
| `TSE:6368` | Organo Corp. | **-19.56%** | 1725.5 JPY | 6,206,900 | $3.13B | ADR | Q2 results after the 4 Nov close: H1 orders +70% but first-half operating profit 12.9% below plan — the “Organo shock” that dragged the AI-infrastructure complex (Note.com market wrap, 5 Nov) |
| `TSE:6834` | Seikoh Giken Co., Ltd. | **-17.42%** | 4740 JPY | 708,800 | $1.68B | none | No company release; sold with the AI-infrastructure complex (TSE Prime top-10 losers, Note.com market wrap, 5 Nov) |
| `TSE:6890` | Ferrotec Corporation | **-17.29%** | 6576 JPY | 5,141,500 | $2.71B | OTC | No company release; sold with the AI-infrastructure complex — the TSE Prime top-10 losers were dominated by semiconductor-equipment and component names (Note.com market wrap, 5 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TPEX:3595` | Alliance Material Co., Ltd. | **-22.60%** | 630 TWD | 1,218,639 | $1.01B | none | No company release; sold with the AI-hardware complex as dealers flagged delays in AI data-centre deployment (CNA/Focus Taiwan, 5 Nov) |
| `TWSE:3653` | Jentech Precision Industrial Co., Ltd | **-10.00%** | 5805 TWD | 2,440,971 | $28.69B | none | No company release; −10.00% limit-down with the AI-hardware complex (CNA/Focus Taiwan, 5 Nov) |
| `TWSE:8046` | Nan Ya Printed Circuit Board Corporation | **-10.00%** | 972 TWD | 13,927,016 | $21.26B | none | No company release; −10.00% limit-down with the AI-hardware complex on AI data-centre deployment delays (CNA/Focus Taiwan, 5 Nov) |
| `TPEX:3081` | LandMark Optoelectronics Corp. | **-10.00%** | 1890 TWD | 4,869,389 | $6.50B | none | No company release; −10.00% limit-down with the AI-hardware complex (CNA/Focus Taiwan, 5 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:GIL` | Gildan Activewear Inc. | **-18.86%** | 49.04 CAD | 2,920,434 | $8.01B | NYSE | Q3 FY26 miss and a full-year guidance cut — revenue now $5.4–5.5bn (from $6.0–6.2bn) and adj. EPS $3.70–3.80 (from $4.65–4.75); the 2026–28 objectives were withdrawn (Gildan release, Canadian Press, RTTNews, 5 Nov) |
| `TSX:TNZ` | Tenaz Energy Corp | **-18.37%** | 50.45 CAD | 1,354,555 | $1.43B | OTC | No company release; moved with the Canadian energy complex (MT Newswires, 5 Nov) |
| `TSX:RUS` | Russel Metals Inc. | **-13.62%** | 76.87 CAD | 481,776 | $3.50B | OTC | No company release; moved with the Canadian metals/energy complex (MT Newswires, 5 Nov) |
| `TSX:CLS` | Celestica Inc. | **-12.66%** | 288.43 CAD | 1,109,105 | $29.82B | NYSE | No company release; sold with the AI-hardware complex as the Nasdaq confirmed a correction (Reuters, 5 Nov) |
| `TSX:LUN` | Lundin Mining Corporation | **-11.43%** | 28.05 CAD | 5,490,369 | $19.40B | ADR | No company release; the TSX Capped Energy Index fell 5.12% as crude slid (MT Newswires, 5 Nov) |
| `TSX:SLF` | Sun Life Financial Inc. | **-10.21%** | 102.83 CAD | 3,998,622 | $45.59B | NYSE | No company release; the TSX Capped Financial Index fell 2.78% (MT Newswires, 5 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:RHM` | Rheinmetall AG | **-16.14%** | 841.5 EUR | 1,102,186 | $52.54B | ADR | FY26 guidance cut — revenue now ~€13.2bn (from €13.7–14.2bn) and margin ~18.5% (from 19%); the Arminius order is unlikely this year and ammunition acceptance delays push revenue into 2027. JPMorgan cut its target to €1,150 from €1,350 (Yahoo/Reuters, Business Post, 5 Nov) |
| `XETR:WAF` | Siltronic AG | **-12.31%** | 50.2 EUR | 500,475 | $2.12B | ADR | No company release; sold with the European chip stocks as AI-capex doubts hit semiconductor equipment (Reuters, 5 Nov) |
| `XETR:SMHN` | SUSS MicroTec SE | **-9.98%** | 44.4 EUR | 291,971 | $1.06B | OTC | No company release; sold with the European chip stocks (Reuters, 5 Nov) |
| `XETR:AIXA` | AIXTRON SE | **-9.82%** | 28.93 EUR | 1,534,553 | $4.05B | ADR | No company release; sold with the European chip stocks (Reuters, 5 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:SOI` | Soitec SA | **-16.73%** | 91.64 EUR | 1,022,342 | $4.42B | none | No company release; slumped with the European chip stocks as AI-capex doubts hit semiconductor equipment — Soitec slumped 17.3% intraday (Reuters, Il Sole 24 Ore Radiocor, 5 Nov) |
| `EURONEXT:AF` | Air France-KLM SA | **+12.06%** | 12.635 EUR | 4,966,125 | $3.32B | ADR | Better-than-expected Q3 operating profit; the Dutch unit KLM announced a cost plan cutting 1,000 jobs (Reuters, Il Sole 24 Ore Radiocor, 5 Nov) |
| `EURONEXT:OVH` | OVH Groupe S.A. | **-5.36%** | 13.23 EUR | 197,617 | $2.39B | ADR | No company release; moved with the European data-centre/cloud complex as AI-spending expectations were reset (Reuters, 5 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:TPRO` | Technoprobe SpA | **-9.28%** | 20.52 EUR | 4,120,241 | $16.26B | ADR | No company release; moved with the European semiconductor-equipment complex (Reuters, Il Sole 24 Ore Radiocor, 5 Nov) |

### eu-es

No liquid name cleared ±5% in this region.

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:BESI` | BE Semiconductor Industries N.V. | **-7.30%** | 140.9 EUR | 1,009,011 | $13.77B | ADR | No company release; European chip stocks fell on AI-capex doubts and China export-control risk (Reuters, Il Sole 24 Ore Radiocor, 5 Nov) |
| `EURONEXT:ASM` | ASM International N.V. | **-6.99%** | 635.8 EUR | 387,395 | $37.34B | ADR | No company release; European chip stocks fell on AI-capex doubts (Il Sole 24 Ore Radiocor, 5 Nov) |
| `EURONEXT:ASML` | ASML Holding NV | **-6.55%** | 1250 EUR | 1,602,606 | $573.48B | ADR | No company release; fell on AI-capex doubts and China export-control risk; the US line fell 7.4–7.9% (Reuters, GuruFocus/Yahoo, 5 Nov) |

### eu-be

No liquid name cleared ±5% in this region.

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | **-15.62%** | 110.2 EUR | 447,534 | $5.69B | none | Q2 FY2027 results released on 5 Nov (earnings call 13:00 CET); the shares fell to €110.20 (−15.62%) (Yahoo Finance ATS.VI, StockAnalysis, 5 Nov) |

### eu-pt

No liquid name cleared ±5% in this region.

### eu-ie

No liquid name cleared ±5% in this region.

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:IQMX` | IQM Quantum Computers Oyj Class A | **-11.96%** | 6.955 EUR | 227,281 | $1.67B | ADR | Q3 2026 report at 08:00 EET — backlog €102.5m (+52% YTD), Q3 revenue €8.9m (+51% y/y), FY26 guidance reaffirmed, cash €260.4m — and the shares still fell 12% from the €7.90 close of 4 Nov (Nasdaq Helsinki release, Yahoo/Nasdaq IQMX, 5 Nov) |
| `OMXHEX:NOKIA` | Nokia Oyj | **-7.51%** | 6.846 EUR | 26,451,296 | $47.01B | ADR | No pre-close release; sold with the European AI/tech complex as the Nasdaq confirmed a correction. Nokia and NVIDIA announced a strategic partnership at 18:29 EET — AFTER the Helsinki close (Nokia IR, 5 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:GN` | GN Store Nord A/S | **+11.61%** | 124 DKK | 3,923,310 | $2.43B | ADR | Q3 2026: profit DKK 379m (from DKK 73m), adj. EBITA from continuing operations DKK 413m (+113%), and a new capital-allocation policy — ≥DKK 4bn of distributions plus a buyback of up to DKK 1bn (company release, RTTNews, 5 Nov) |

### eu-gr

No liquid name cleared ±5% in this region.

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) — published because a +100% or a −16% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:ENV | Enova Mining Limited | **+100.00%** | 5,373,502 | below the $300M + vol ≥ 100k cap floor |
| ASX:BIT | Biotron Limited | **+100.00%** | 4,410,574 | below the $300M + vol ≥ 100k cap floor |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:4582 | Symbio Pharmaceuticals Limited | **+71.43%** | 49,877,600 | below the $300M cap floor |
| TSE:2667 | ImageONE Co., Ltd. | **+47.62%** | 6,806,100 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:4117 | General Biologicals Corp. | **+37.27%** | 263,245 | below the $200M cap floor |
| TPEX:6610 | TWi Biotechnology, Inc | **-10.26%** | 1,162,480 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSXV:PUL | Pulse Oil Corp. | **+100.00%** | 114,128 | below the $200M cap floor |
| CSE:DATT | Digital Asset Technologies Inc. | **+100.00%** | 100,000 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| XETR:LEOW | Leo International Precision Health Aktiengesellschaft | **+12.73%** | 104,501 | below the $300M + vol ≥ 50k cap floor |
| XETR:BRNK | BRANICKS Group AG | **-12.64%** | 178,874 | below the $300M + vol ≥ 50k cap floor |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:ALSPW | Spineway SA | **+12.21%** | 212,265 | below the $100M cap floor |
| EURONEXT:ALHUN | Hunyvers | **-8.57%** | 166,460 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:RN | Risanamento S.p.A. | **+35.71%** | 41,155,056 | below the $100M cap floor |
| MIL:AEF | Aeffe S.p.A. | **-13.50%** | 291,660 | below the $100M cap floor |

### eu-es

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| BME:CITY | Club De Futbol Intercity SAD | **-13.00%** | 11,234,483 | below the $100M cap floor |

### eu-nl

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:EBUS | Ebusco Holding N.V. | **-7.21%** | 1,624,538 | below the $100M cap floor |

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:SBI | Sunborn International Plc | **-21.37%** | 207,333 | below the $100M cap floor |
| OMXHEX:MODU | Modulight Oyj | **+11.88%** | 116,864 | below the $100M cap floor |

### eu-dk

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXCOP:PEG | Pharma Equity Group A/S Class A | **+8.29%** | 240,141 | below the $100M cap floor |

## No catalyst

Liquid names that cleared ±5% with **no sourced driver** — no company release, no filing, no analyst action and no sector or macro move behind them. Kept separate so they do not dilute the mover table.

### au

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `ASX:ZIP` | Zip Co Ltd. | **+15.68%** | 2.14 AUD | $1.61B |

### jp

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `TSE:5857` | ARE Holdings, Inc. | **+22.80%** | 3770 JPY | $1.61B |
| `TSE:485A` | PowerX, Inc. | **-20.59%** | 1620 JPY | $1.50B |

### tw

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `TPEX:7861` | Bellwether Electronic Corp. | **-15.57%** | 591 TWD | $1.38B |
| `TPEX:7924` | TLC BioSciences Corp | **-10.31%** | 352.5 TWD | $1.60B |

### eu-de

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `XETR:NEM` | Nemetschek SE | **-10.17%** | 68 EUR | $9.81B |
| `XETR:S92` | SMA Solar Technology AG | **-9.36%** | 49.08 EUR | $2.11B |

### eu-fr

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `EURONEXT:DEC` | JCDecaux SE | **+5.77%** | 26.76 EUR | $6.08B |

### eu-it

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `MIL:ARIS` | Ariston Holding NV | **-8.26%** | 3.042 EUR | $1.30B |

### eu-es

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `BME:ROVI` | Laboratorios Farmaceuticos Rovi, S.A. | **+8.31%** | 69.05 EUR | $3.62B |
| `BME:GEST` | Gestamp Automocion S.A. | **-7.91%** | 2.735 EUR | $1.92B |

### eu-at

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `VIE:VER` | VERBUND AG Class A | **+8.57%** | 75.35 EUR | $27.06B |

### eu-pt

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `EURONEXT:SON` | Sonae SGPS SA | **+5.57%** | 2.275 EUR | $4.84B |

## Method, source health & caveats

### Method

- **Universe**: the TradingView per-country scanner for each region's own listings (`type` in stock/dr plus the `country` column), 16 POST calls, one response per region, no pagination. Germany is collapsed by company description (WKN symbols on off-exchange venues are the same share); every other region by (issuer name, symbol root, share-class suffix).
- **Floors (USD, applied client-side after conversion)**: au $300M + vol ≥ 100k, jp $300M, tw $200M, ca $200M, eu-de $300M + vol ≥ 50k, eu-fr/it/es/nl/be/at $100M, eu-ie $200M, eu-fi/dk $100M, eu-pt/gr $50M. A row whose cap the source does not report is EXCLUDED, never written blank.
- **FX**: Frankfurter (api.frankfurter.app, from=USD, rate date 2026-11-05) for AUD 1.4285, CAD 1.3966, DKK 6.6596, EUR 0.89095, JPY 158.46; open.er-api.com (updated 2026-11-05T00:02:31Z) for TWD 32.824108, which Frankfurter does not carry. The table is **local currency units per 1 USD**, so `usd_cap = market_cap_basic / FX` — the division direction is checked by share-count reconciliation (`market_cap_local / close` returns 10.1bn shares for Toyota, 26.2bn for TSMC, 1.16bn for SAP, 1.42bn for Royal Bank).
- **Cap carrier rule**: the cap belongs to the issuer. It is resolved to the issuer's **primary (common) line**, converted ONCE with the primary's currency, and carried to the issuer's other lines, which publish the primary's ticker in `cap_source_symbol`. A preferred line therefore never carries its own cap and never outranks the common line — TSX:ENB.PF.V, quoted in USD, publishes Enbridge's CAD-derived $110.4bn, not $155.5bn.
- **Venue-collapse rule**: one row per instrument, preferring the official venue (TSE, TWSE/TPEX, TSX/TSXV/CSE, XETR/FWB, MIL, BME, VIE, OMXHEX, OMXCOP, ATHEX, EURONEXT, ASX). An instrument with no official-venue print is excluded as `stale_venue_print` (Japan's NAG/FSE/SAPSE lines, Canada's NEO ATS, Germany's off-exchange venues).
- **Venue-official price rule**: where the exchange's own print was obtainable it is the price published, with the third-party value and the delta beside it in `price_conflict`. This run verified the ATHEX index against Euronext Athens' own historical data (2,611.41, −1.92%) and cross-checked the European closes against the Il Sole 24 Ore Radiocor close report; no row required a conflict cell, so every `price_conflict` cell is empty.
- **CSV columns**: **18** — `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`. The 4 Nov files in this archive were **14-column**, so a consumer reading the archive by position will see a break on today's date.
- **Files written**: 16 per-region CSVs, `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json` (and the internal `_digest.json` / `_cap_findings.json`) under `international-eod/2026-11-05/`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView per-country scanner | POST scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan | ok | 16/16 HTTP 200, 18,326 instrument rows, one response per region |
| TradingView America scanner | POST scanner.tradingview.com/america/scan | ok | 13,439 US lines (stock + dr) in ONE response — the paginated pull used first lost rows (NYSE:SAP was missing) and was replaced |
| Frankfurter FX | api.frankfurter.app/latest?from=USD | ok | 2026-11-05 rates, 5 currencies |
| open.er-api FX | open.er-api.com/v6/latest/USD | ok | TWD only; agrees with Frankfurter within 0.10% on the shared currencies |
| Yahoo chart API (index levels) | query1.finance.yahoo.com/v8/finance/chart/{^AXJO,^GDAXI,^FCHI,…} | ok | 14/16 indices; **^N225 and ^TWII returned a null 5 Nov bar** and were taken from the press instead |
| Jiji / CNA / Focus Taiwan / Euronext Athens | index closing reports | ok | Nikkei, TOPIX, TAIEX and the ATHEX taken from the market's own closing report |
| Press (Reuters, Il Sole 24 Ore Radiocor, MarketIndex, AFP/CN, Canadian Press, RTTNews, Cabot, investsmart, note.com, euro2day, newsit.gr) | catalyst and market-context checks | ok | every catalyst published in this report is attributed to one of these |
| Yahoo spark/quote pages | quote pages for index verification | partial | used only as a cross-check (Nokia €6.85 −7.51%, AT&S €110.20 −15.62%, IQMX €7.90 prior close) |
| Yahoo chart API (verification) | chart/{ENV.AX,BIT.AX,SPX.AX,4582.T} | ok | confirms the below-gate penny moves (0.001→0.002, +100.00% exactly) and TSE:4582 ¥42→¥72 |
| Yahoo chart API for ^OMXC20 | query1...^OMXC20 | partial | the series is sparse — a single 5 Nov bar — so the prior close is taken from the 4 Nov archive |

### Caveats

- **Units**: `market_cap` is USD; `open`/`high`/`low`/`close` are in the listing currency given by the `currency` column. `change_pct` is a percentage, not a fraction.
- **Carry-over rows**: 88 written rows did not trade this session and carry an earlier session's close (they are listed in `_carryover.json` with the last trade date, excluded from every movers list and from the breadth counts). A row is flagged only when its close string is IDENTICAL to the prior session's file AND its volume is zero or its `change_pct` is non-zero — no tolerance, so a real half-cent move is never swallowed.
- **Issuer-unresolved rows**: 220 rows (mostly Canada's preferred and Class B/C lines, plus Japan's subscription certificates and Germany's preferred lines) are DROPPED rather than given a borrowed cap: their issuer has no common line in the source under the same ticker root, so a carry would cross an issuer boundary.
- **`no_market_cap` rows** (247) cannot be tested against a cap floor and are excluded rather than written blank.
- **Off-official rows** (215) have no print on an official venue in their home market (Japan's NAG/FSE/SAPSE lines, Canada's NEO ATS lines, Germany's GETTEX/LSX/Lang & Schwarz lines) and are excluded as `stale_venue_print`.
- **The cap cross-venue check found real disagreements.** Every issuer with a US line was compared after conversion; 49 pairs differ by more than 10%, mostly OTC quotations carrying a stale company cap. The largest are listed below — the primary line's cap is published in all cases and the US line's figure is recorded here.

| Region | Line | US line | Primary cap (USD) | US-line cap (USD) | Delta |
|---|---|---|---|---|---|
| `tw` | `TWSE:1604` | OTC:SAXPY | $258M | $29.37B | 11288.6% |
| `jp` | `TSE:4985` | OTC:FTEG | $689M | $3M | 99.5% |
| `au` | `ASX:WOW` | OTC:WLWHY | $34.41B | $2.12B | 93.8% |
| `jp` | `TSE:9984` | OTC:SOBKY | $153.79B | $70.31B | 54.3% |
| `au` | `ASX:WAF` | OTC:WFRSF | $2.53B | $3.62B | 43.1% |
| `ca` | `TSX:MKP` | OTC:MAMTF | $646M | $407M | 37.0% |
| `au` | `ASX:L1G` | OTC:PTMGF | $2.12B | $1.36B | 35.9% |
| `eu-nl` | `EURONEXT:ENVI` | OTC:ENVHF | $284M | $198M | 30.2% |

- **Index levels**: the ATHEX comes from Euronext Athens' own historical data because no Yahoo symbol exists for it; the Nikkei and TOPIX come from Jiji's closing report and the TAIEX from CNA/Taiwan Index Plus, because Yahoo's 5 Nov bars for ^N225 and ^TWII were still null at the time of the pull. Every other index level is Yahoo's settled daily bar and matches the press close where one was published (ASX 9,065.1; DAX 26,325.01; CAC 8,205.37; ASML €1,250.00; ASM International €635.80; Infineon €45.95; Soitec €91.64; Air France-KLM €12.64 — all exact).
- **The session's shape**: it was not one global move. Australia rose on materials and gold (ASX 200 +2.61%, Materials +7.2%, best since March 2020, gold +5.2% in two sessions to US$4,136/oz); Taiwan fell 3.20% as dealers flagged AI data-centre deployment delays; Tokyo fell 1.79% in the Nikkei but rose 1.16% in the TOPIX as money left AI hardware; Europe closed lower with tech −3.9% and defence weak after Rheinmetall's guidance cut; Athens fell 1.92% on the Coca-Cola HBC Russian-exposure story.
- **Sector rotation** (mean and median `change_pct` per sector over the liquid subset, volume ≥ 100k, same rows as the movers list): Retail Trade +3.05% mean / +3.95% median (124), Consumer Services +2.59% mean / +2.86% median (112), Consumer Non-Durables +2.50% mean / +2.65% median (121) at the top; Energy Minerals -3.22% (67), Producer Manufacturing -3.46% (356), Electronic Technology -5.71% (456) at the bottom.
- **The below-gate moves were verified against an independent price source**: Yahoo's own daily bars confirm ASX:ENV 0.001 → 0.002 and ASX:BIT 0.001 → 0.002 (both exactly +100.00% — a sub-cent doubling, not a data artefact) and TSE:4582 ¥42 → ¥72 (+71.43%).
- **The build-time assertion passes with 0 failures and 96 warnings**, and every warning is the same heuristic one: the checker's issuer-name reduction cuts a carried cap's source description at the first class word, so a Canadian preferred line described as "… Non-Cum Conv Red Pfd …" reduces to a different string than its common line even though the carry is legitimate (same ticker root, same issuer, and the cap is the company-level figure the contract requires).
- **`us_listing` is the America scanner's answer, matched on the ISSUER (never the ticker — ASX:CAT is Caterpillar while NYSE:CAT is a different company). The scanner's US set does not carry every primary US line, so an issuer whose only US line in the source is an OTC quotation publishes `OTC`; `ADR` means the US line is a depositary receipt (`type=dr`).

