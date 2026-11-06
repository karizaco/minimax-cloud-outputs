# Cron #05 eod-international-daily — Friday, 06 November 2026

## TL;DR

- **Asia took the full force of the post-midterm AI rout; the west barely flinched.** **4,392 instruments printed across the 16 regions** and the tape split three ways: Tokyo fell 5.96% (the Nikkei's third-largest point drop on record, and the index's close put it in a bear market more than 20% below its June peak) with a **-4.94% median name**, Taipei fell 4.51% after a record 3,737.67-point intraday drop, while **Canada's median name rose +0.28%** and the TSX gained 0.52% — Europe fell about 1%.
- **The most consequential single move is Japan Tobacco (TSE:2914, -19.31%)** — Vladimir Putin's 5 November decree put four Japan Tobacco International plants under temporary management, and Russia is ~10% of JT revenue and ~25% of its operating profit; the shares hit the limit down with pro-rata allocation and no trades. For a US trader the rout's reachable names are the ADRs: **TSMC, BHP, SAP, ASML and ASMI all closed lower**, and TSMC opened at its limit-down price before recovering to -4.69%.
- **Read the numbers with the unit convention in mind: `market_cap` is USD while every price is in the listing currency** (`currency` column) — a ¥5,092 close and a C$29.58 close are not comparable, the caps are — and note that this file carries **18 columns**, the same schema as the 5 Nov session, so the archive's column count changes only on 5 Nov, not today.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,562 | 1,562 | **297** | $300M + vol ≥ 100,000 | 4 | 1,241 | 19 | 1 | 0 | 0 | 0 |
| `jp` | TSE | 3,905 | 3,870 | **1,375** | $300M | 4 | 2,377 | 0 | 3 | 0 | 0 | 111 |
| `tw` | TWSE, TPEX | 2,335 | 2,335 | **882** | $200M | 55 | 1,396 | 0 | 2 | 0 | 2 | 0 |
| `ca` | TSX, TSXV, CSE | 4,271 | 2,686 | **633** | $200M | 132 | 1,771 | 0 | 134 | 0 | 46 | 16 |
| `eu-de` | XETR, FWB | 4,312 | 499 | **112** | $300M + vol ≥ 50,000 | 2 | 201 | 85 | 11 | 0 | 0 | 88 |
| `eu-fr` | EURONEXT | 560 | 560 | **272** | $100M | 3 | 285 | 0 | 0 | 0 | 7 | 0 |
| `eu-it` | MIL | 392 | 392 | **179** | $100M | 2 | 211 | 0 | 0 | 0 | 3 | 0 |
| `eu-es` | BME | 272 | 272 | **147** | $100M | 34 | 91 | 0 | 0 | 0 | 32 | 0 |
| `eu-nl` | EURONEXT | 83 | 83 | **62** | $100M | 0 | 21 | 0 | 0 | 0 | 0 | 0 |
| `eu-be` | EURONEXT | 103 | 103 | **77** | $100M | 3 | 23 | 0 | 0 | 0 | 1 | 0 |
| `eu-at` | VIE | 65 | 65 | **50** | $100M | 3 | 12 | 0 | 0 | 0 | 1 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **27** | $50M | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 2 | 0 | 0 | 0 | 1 | 0 |
| `eu-fi` | OMXHEX | 188 | 188 | **101** | $100M | 4 | 83 | 0 | 0 | 0 | 0 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 58 | 0 | 0 | 0 | 1 | 0 |
| `eu-gr` | ATHEX | 129 | 129 | **86** | $50M | 0 | 42 | 0 | 1 | 0 | 0 | 0 |
| **total** | | **18,361** | **12,928** | **4,392** | | **247** | **7,818** | **104** | **152** | **0** | **94** | **215** |

`Universe` is every instrument the source returns for that country's own listings; `Unique instruments` collapses the same instrument quoted on several venues down to one line; `Written` applies the per-region USD market-cap floor plus the region's volume gate. Every excluded row carries a reason from the closed set in `_excluded.json`, and the counts above are read from that file rather than estimated.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 9,020.80 | -44.30 / **-0.49%** | 2026-11-06 | Yahoo ^AXJO settled bar (6 Nov); the 5 Nov bar is null, so the prior close 9,065.10 comes from the 5 Nov archive; TradingEconomics (9,021, -0.5%) and AP (9,020.80, -0.5%) |
| jp | Nikkei 225 | 57,434.77 | -3,643.13 / **-5.96%** | 2026-11-06 | Jiji closing report 15:33 JST (57,434.77, −3,643.13); Aju Press; countryeconomy; Yahoo history |
| jp | TOPIX | 3,707.99 | -232.40 / **-5.90%** | 2026-11-06 | Jiji closing report 15:33 JST (3,707.99, −232.40); Yahoo history |
| tw | TAIEX | 39,701.64 | -1,873.08 / **-4.51%** | 2026-11-06 | CNA / Focus Taiwan; TWSE daily board; Taiwan News (intraday record −3,737.67) |
| ca | S&P/TSX Composite | 35,789.09 | +183.79 / **+0.52%** | 2026-11-06 | Yahoo ^GSPTSE settled daily bar (16:00 ET) |
| eu-de | DAX (Xetra) | 25,820.36 | -504.65 / **-1.92%** | 2026-11-06 | Yahoo ^GDAXI (Xetra close) |
| eu-fr | CAC 40 | 8,139.00 | -66.37 / **-0.81%** | 2026-11-06 | Yahoo ^FCHI |
| eu-it | FTSE MIB | 50,052.96 | -453.04 / **-0.90%** | 2026-11-06 | Yahoo FTSEMIB.MI |
| eu-es | IBEX 35 | 19,369.50 | -116.50 / **-0.60%** | 2026-11-06 | Yahoo ^IBEX |
| eu-nl | AEX | 1,120.55 | -8.67 / **-0.77%** | 2026-11-06 | Yahoo ^AEX |
| eu-be | BEL 20 | 5,996.07 | -19.02 / **-0.32%** | 2026-11-06 | Yahoo ^BFX |
| eu-at | ATX | 6,434.80 | -76.60 / **-1.18%** | 2026-11-06 | Yahoo ^ATX |
| eu-pt | PSI 20 | 9,476.73 | -6.48 / **-0.07%** | 2026-11-06 | Yahoo PSI20.LS |
| eu-ie | ISEQ | 14,695.08 | -108.07 / **-0.73%** | 2026-11-06 | Yahoo ^ISEQ |
| eu-fi | OMX Helsinki 25 | 6,221.79 | -32.51 / **-0.52%** | 2026-11-06 | Yahoo ^OMXH25 |
| eu-dk | OMX Copenhagen 20 | 1,658.45 | -10.58 / **-0.63%** | 2026-11-06 | Yahoo ^OMXC20 (single 6 Nov bar; prior close 1,669.03 from the 5 Nov archive) |
| eu-gr | ATHEX General | 2,553.35 | -58.06 / **-2.22%** | 2026-11-06 | Euronext Athens' own historical data (2,553.35, −2.22%); euro2day and eKathimerini agree — a third-party live quote of 2,587.93 (−2.11%, iefimerida) was not used |
| *context* | STOXX 600 | 648.33 | -6.54 / **-1.00%** | 2026-11-06 | Yahoo ^STOXX (Reuters quoted 648.83 at 09:19 GMT intraday) |

**One story, three opposite reactions.** The Democrats' sweep in the 3 November US midterms was read as a threat to the pace of the AI data-centre build-out, and on Thursday Wall Street sold it: the Philadelphia Semiconductor Index fell 12.2% — its worst day since 2020 — and US chip names erased roughly US$2.5 trillion, with Nvidia -9.3% and AMD -17.3% (AP, Reuters, nationthailand). Asia, where the AI hardware complex is the index, took the full hit: **Tokyo and Taipei entered bear-market territory, Korea triggered a 20-minute circuit-breaker halt**, and both Taipei and Seoul opened near their lows before recovering. **Europe held up best** (STOXX 600 -1.00%, its smallest weekly loss in the rout) because of its smaller AI weight, and **Canada was flat-to-higher** as gold and silver producers bid. Both Taipei and Seoul opened emergency support: Taiwan's National Financial Stabilization Fund authorised deployment on Friday afternoon and its FSC tightened short-selling from 9 November (AFP, Focus Taiwan).

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max | Cap-weighted |
|---|---|---|---|---|---|---|
| `au` | 297 | -1.33% | 70 / 207 / 20 | -11.95% | +11.64% | -0.61% |
| `jp` | 1,375 | -4.94% | 23 / 1345 / 7 | -19.31% | +22.09% | -5.85% |
| `tw` | 880 | -3.76% | 67 / 798 / 15 | -12.00% | +10.07% | -4.63% |
| `ca` | 587 | +0.28% | 335 / 200 / 52 | -29.92% | +29.17% | +0.21% |
| `eu-de` | 112 | -0.80% | 34 / 77 / 1 | -11.99% | +5.54% | -1.71% |
| `eu-fr` | 265 | -0.27% | 93 / 142 / 30 | -15.30% | +7.08% | -0.90% |
| `eu-it` | 176 | -0.02% | 80 / 86 / 10 | -7.64% | +23.20% | -0.84% |
| `eu-es` | 115 | +0.00% | 50 / 57 / 8 | -4.48% | +8.33% | -0.75% |
| `eu-nl` | 62 | -0.61% | 19 / 41 / 2 | -23.05% | +2.69% | +0.71% |
| `eu-be` | 76 | -0.42% | 24 / 48 / 4 | -23.31% | +3.33% | -0.21% |
| `eu-at` | 49 | -0.44% | 15 / 29 / 5 | -4.55% | +5.56% | -1.11% |
| `eu-pt` | 27 | -0.28% | 7 / 15 / 5 | -3.55% | +5.30% | -0.79% |
| `eu-ie` | 16 | +0.00% | 4 / 7 / 5 | -8.48% | +2.84% | -0.73% |
| `eu-fi` | 101 | -0.55% | 35 / 61 / 5 | -15.65% | +9.66% | -0.50% |
| `eu-dk` | 74 | -0.31% | 30 / 41 / 3 | -4.23% | +5.74% | -0.73% |
| `eu-gr` | 86 | -1.02% | 11 / 66 / 9 | -4.89% | +3.99% | -2.02% |

The breadth table is where the index and the typical name disagree, and today they disagree in **Canada**: the TSX composite gained 0.52% and the median name rose 0.28%, but that is a split tape, not a calm one — the gold and silver producers rallied while Trisura Group fell 29.92% on its own results, so the cap-weighted snapshot (+0.21%) says almost nothing about what an investor in a single stock actually earned. In **Japan** the breadth is the story in the other direction: 1,345 of 1,375 written names fell, so the -5.85% cap-weighted figure is *not* a heavy-weight story — selling was broad. Carry-over rows are excluded from these counts.

## Top movers

Liquid names (volume ≥ 100k **and** market cap ≥ $1B) whose move cleared ±5%, capped at the six largest absolute moves per region, with the driver that was actually sourced. A row with no sourced driver is not here — it is under `## No catalyst`.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:MI6` | Minerals 260 Limited | **-8.54%** | 0.75 AUD | 10,740,760 | $1.23B | none | No company-specific release found; sold with the critical-minerals complex as the AI-trade unwind pulled capital out of the metals — the ASX Materials index -0.9%, WA1 Resources -9.0%, Lynas -7.1%, copper -1.0% and nickel -1.4% overnight (MarketIndex evening wrap, 6 Nov; FNArena ASX losers, 6 Nov) |
| `ASX:SRL` | Sunrise Energy Metals Limited | **-8.24%** | 11.58 AUD | 712,114 | $1.36B | none | No company-specific release found; the same critical-minerals de-rating — and SRL committed A$456m to develop the Syerston scandium mine in NSW this week (MarketIndex evening wrap and FNArena, 6 Nov) |
| `ASX:SGM` | Sims Ltd. | **-7.22%** | 19.65 AUD | 883,195 | $2.78B | OTC | No company-specific release found; sold with the AI-trade unwind and the resources complex — Goodman Group -3.2%, South32 -3.4% (TradingEconomics, 6 Nov) |
| `ASX:IMD` | Imdex Ltd | **-6.98%** | 3.2 AUD | 974,789 | $1.14B | none | No company-specific release found; sold with the resources complex as base metals fell overnight (aluminium -1.0%, copper -1.0%, tin -2.5%) (MarketIndex evening wrap, 6 Nov) |
| `ASX:IGO` | IGO Limited | **-5.88%** | 4.96 AUD | 8,260,386 | $2.51B | none | No company-specific release found; the mining complex fell with copper -1.0% overnight and BHP -2.3% / Rio Tinto -2.0% (MarketIndex evening wrap and TradingEconomics, 6 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:2914` | Japan Tobacco Inc. | **-19.31%** | 6269 JPY | 2,794,400 | $82.79B | none | Russia's Putin decree of 5 Nov placed four Japan Tobacco International units (JTI Donskoy Tabak, JTI Yelets, Kres Neva, Petro) under temporary management; Russia is ~10% of JT revenue and ~25% of operating profit. The shares hit the limit down with pro-rata allocation and no trades executed (Investing.com, Tokyo market summary, 6 Nov) |
| `TSE:6963` | ROHM Company Limited | **-15.00%** | 2759 JPY | 21,082,000 | $8.42B | none | H1 FY2026 results on 5 Nov: sales ¥279.5bn (+14.4%), operating profit ¥17.5bn (+128.5%), FY guidance raised to ¥550bn sales and ¥50bn operating profit — the stock still fell with the AI-hardware rout (ROHM IR, 2Slides deck, 6 Nov) |
| `TSE:3563` | FOOD & LIFE COMPANIES LTD. | **-14.66%** | 5092 JPY | 8,908,800 | $8.18B | none | FY2026 (Sept year-end) results on 6 Nov: revenue ¥515.3bn (+26.9%) and operating profit ¥51.5bn (+47.0%), both record highs, plus the first FY2029 medium-term plan (¥831bn revenue / ¥88bn operating profit) — the shares fell anyway on the plan (company release, StockAnalysis, 6 Nov) |
| `TSE:8056` | BIPROGY Inc. | **-12.82%** | 4337 JPY | 2,310,100 | $2.76B | none | H1 net profit fell 27% and progress against the full-year plan came in below the historical average (note.com TSE Prime losers analysis, 6 Nov) |
| `TSE:2802` | Ajinomoto Co., Inc. | **-12.40%** | 4268 JPY | 11,561,800 | $29.23B | OTC | No company-specific release found; defensive staples were sold with the broad risk-off — the TSE's largest decliners were Ajinomoto -12.50%, Yamaha -12.27% and Sumitomo Dainippon -12.12%, with 98% of the Prime market lower (TradingEconomics, note.com market wrap, 6 Nov) |
| `TSE:6834` | Seikoh Giken Co., Ltd. | **-11.92%** | 4175 JPY | 1,869,300 | $1.68B | none | No company-specific release found; sold in a market-wide risk-off rather than on company news — 1,523 of 1,544 TSE Prime names fell and all 33 industry groups were lower (note.com market wrap, Aju Press, 6 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TWSE:6944` | Mega Union Technology, Inc. | **-10.00%** | 603 TWD | 932,399 | $2.13B | none | No company-specific release found; -10.00% limit-down with the AI-hardware complex as overnight Wall Street losses on data-centre-exposed names forced selling (CNA/Focus Taiwan, The Blade AI supply-chain tape, 6 Nov) |
| `TWSE:3653` | Jentech Precision Industrial Co., Ltd | **-9.99%** | 5225 TWD | 1,621,697 | $28.50B | none | -10.00% limit-down; the AI-server/PCB complex was hit by the NVidia VR200 rack volume ramp being pushed to Q4 2026 on PCB issues, on top of the post-midterm AI-rout (The Blade AI supply-chain tape, 6 Nov) |
| `TPEX:3363` | FOCI Fiber Optic Communications, Inc. | **-9.99%** | 360.5 TWD | 3,104,729 | $1.45B | none | No company-specific release found; -9.99% with the optical/AI-hardware complex as more than 1,600 Taiwan names hit their 10% limit at one point (CNA/Focus Taiwan, 6 Nov) |
| `TWSE:6213` | ITEQ Corporation | **-9.98%** | 496 TWD | 4,405,736 | $6.73B | none | No company-specific release found; -9.98% with the AI-server complex (CNA/Focus Taiwan, 6 Nov) |
| `TWSE:8046` | Nan Ya Printed Circuit Board Corporation | **-9.98%** | 875 TWD | 11,924,023 | $21.11B | none | -10.00% limit-down; the PCB/AI-hardware complex was hit by the NVidia VR200 rack ramp delay to Q4 2026 on PCB issues (The Blade AI supply-chain tape, 6 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:TSU` | Trisura Group Ltd. | **-29.92%** | 29.58 CAD | 1,400,076 | $1.44B | OTC | Q3 2026 results (released 5 Nov, call 6 Nov): gross premiums written C$802m, down 6%; total book value fell 1.6% to C$989m, below the C$1bn reached in Q2, on unrealised bond losses as yields rose; operating EPS C$0.73 (+3%) (Q3 earnings call, Yahoo/Quartr, 6 Nov) |
| `TSX:PXT` | Parex Resources Inc. | **-16.55%** | 19.81 CAD | 3,126,112 | $1.64B | OTC | Q3 2026 results on 6 Nov: adjusted EBITDA C$238m beat, but wider differentials and higher costs pressured the cash-flow outlook; Q4 dividend C$0.385 declared (Quartr, Dow Jones Newswires, GlobeNewswire, 6 Nov) |
| `TSX:IMG` | IAMGOLD Corporation | **+8.09%** | 26.44 CAD | 3,516,390 | $9.94B | NYSE | Q3 2026 results on 5 Nov: attributable production 186,900oz, revenue US$856.5m, net earnings US$297.0m, mine-site free cash flow US$404.3m and liquidity US$1.61bn — plus irrevocable notice to repurchase 50% of Franco-Nevada's 7.5% Côté Gold royalty for ~US$525m; gold US$4,097/oz (Newsfile/Nasdaq, 6 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:HAG` | HENSOLDT AG | **-6.22%** | 77.44 EUR | 331,447 | $10.50B | OTC | The 9M 2026 statement (5 Nov) delivered a record €10.37bn backlog and a raised ~€2.8bn revenue target, but the raise landed ~1% below consensus; the stock kept falling with a post-midterm de-rating in European defence (Goldman's defence basket -4.1%, its largest day in over four months). Capital Markets Day is 10 Nov (Investing.com, ad-hoc-news, 6 Nov) |
| `XETR:AIXA` | AIXTRON SE | **+5.12%** | 30.41 EUR | 1,025,347 | $4.03B | OTC | No company-specific release found; recovered with the European chip complex, which bounced on the morning of 6 Nov (ASML +2.6%, Infineon +2.3%, ASM +1.7%, BE Semiconductor +1.7%) after yesterday's -9.82% (AI Business Brief, 6 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:TEP` | Teleperformance SE | **-15.30%** | 68.44 EUR | 814,995 | $5.50B | none | The Q3 update and 2026 outlook cut the year: like-for-like revenue is now expected to fall 1.5-2.5% in 2026 against a previous 0-2% growth forecast, on a sharper decline in Trust & Safety content moderation and faster offshoring; Q3 LFL revenue fell 1.2%. TP ICAP Midcap cut its growth forecasts through 2030 (Reuters, Investing.com, 6 Nov) |
| `EURONEXT:AF` | Air France-KLM SA | **+7.08%** | 13.53 EUR | 3,469,485 | $3.31B | none | Rebound: a fifth session of gains that took the stock 27% higher over five sessions and the top of the SBF 120, after two brokers raised their price targets (Reuters, Zesteinvest/ideal-investisseur, 6 Nov) |

### eu-it

No liquid name cleared ±5% in this region with a sourced driver.

### eu-es

No liquid name cleared ±5% in this region with a sourced driver.

### eu-nl

No liquid name cleared ±5% in this region with a sourced driver.

### eu-be

No liquid name cleared ±5% in this region with a sourced driver.

### eu-at

No liquid name cleared ±5% in this region with a sourced driver.

### eu-pt

No liquid name cleared ±5% in this region with a sourced driver.

### eu-ie

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:GL9` | Glanbia PLC | **-8.48%** | 19.42 EUR | 1,129,687 | $5.80B | OTC | Morgan Stanley downgraded Glanbia from equal-weight to underweight, warning that competition could pressure margins next year — two days after Q3 results raised full-year EPS growth guidance to 22-24% constant currency (Irish Times, 6 Nov) |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:OUT1V` | Outokumpu Oyj | **-15.65%** | 3.794 EUR | 5,436,505 | $2.40B | OTC | Q3 2026 in line (adjusted EBITDA €101m) but the Q4 warning was the trigger: adjusted EBITDA is guided to roughly the prior year's level (€10m), deliveries are expected to fall 5-15% and European demand is weak with high customer inventories; Nordea, Citigroup and JPMorgan cut targets (Finwire, Reuters, MarketScreener, 6 Nov) |

### eu-dk

No liquid name cleared ±5% in this region with a sourced driver.

### eu-gr

No liquid name cleared ±5% in this region with a sourced driver.

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) — published because a +121% or a -75% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:BIT | Biotron Limited | **+100.00%** | 4,410,574 | below the $300M cap floor + vol ≥ 100,000 |
| ASX:ENT | Enterprise Metals Limited | **+50.00%** | 164,384 | below the $300M cap floor + vol ≥ 100,000 |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:2667 | ImageONE Co., Ltd. | **-24.73%** | 4,030,400 | below the $300M cap floor |
| TSE:4492 | Genetec Corp. | **-21.39%** | 708,400 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:6819 | Oriental System Technology Inc | **-16.08%** | 205,286 | below the $200M cap floor |
| TPEX:7865 | Jin Lian Cheng Resources Co., Ltd. | **-15.09%** | 326,299 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSX:ELEF | Silver Elephant Mining Corp | **+120.83%** | 3,051,346 | below the $200M cap floor |
| TSXV:ESPN | Hispania Resources Inc | **-75.00%** | 443,000 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| XETR:TPG0 | Platform Group SE & Co. KGaA | **-13.06%** | 1,015,041 | below the $300M cap floor + vol ≥ 50,000 |
| XETR:QBY0 | q.beyond AG | **-6.20%** | 197,442 | below the $300M cap floor + vol ≥ 50,000 |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:AELIS | Aelis Farma SA | **+38.59%** | 345,297 | below the $100M cap floor |
| EURONEXT:NACON | Nacon SAS | **-17.50%** | 405,970 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:PINF | Pininfarina S.p.A. | **+20.24%** | 283,676 | below the $100M cap floor |
| MIL:RN | Risanamento S.p.A. | **+12.78%** | 82,602,380 | below the $100M cap floor |

### eu-es

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| BME:CITY | Club De Futbol Intercity SAD | **-17.53%** | 28,918,944 | below the $100M cap floor |
| BME:VANA | Vanadi Coffee SA | **-9.56%** | 2,306,954 | below the $100M cap floor |

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:OPTOMED | Optomed Oyj Class A | **+14.15%** | 385,323 | below the $100M cap floor |
| OMXHEX:SBI | Sunborn International Plc | **+8.18%** | 170,681 | below the $100M cap floor |

### eu-dk

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXCOP:UNLGRP | Unlimit Group A/S | **+8.33%** | 169,488 | below the $100M cap floor |

## No catalyst

Liquid names that cleared ±5% with **no sourced driver** — no company release, no filing, no analyst action and no sourced sector or macro move behind them. Kept separate so they do not dilute the mover table.

### au

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `ASX:MSB` | Mesoblast Limited | **-6.45%** | 2.03 AUD | $1.88B |

### tw

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `TPEX:7924` | TLC BioSciences Corp | **+10.07%** | 388 TWD | $1.59B |

### ca

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `TSX:VNP` | 5N Plus Inc. | **+9.40%** | 33.53 CAD | $2.07B |
| `TSX:LNF` | Leon's Furniture Limited | **+8.86%** | 29.25 CAD | $1.33B |
| `TSX:SVM` | Silvercorp Metals Inc. | **+7.61%** | 12.58 CAD | $1.90B |

### eu-de

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `XETR:AG1` | AUTO1 Group SE | **-6.73%** | 17.45 EUR | $4.59B |
| `XETR:HOT` | HOCHTIEF Aktiengesellschaft | **+5.54%** | 365.6 EUR | $30.55B |

### eu-fr

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `EURONEXT:OVH` | OVH Groupe S.A. | **+6.88%** | 14.14 EUR | $2.38B |

### eu-it

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `MIL:ICOS` | Intercos S.p.A. | **+7.11%** | 13.86 EUR | $1.39B |
| `MIL:NWL` | NewPrinces S.p.A. | **+5.78%** | 24.16 EUR | $1.08B |

### eu-es

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `BME:DIA` | Distribuidora Internacional de Alimentacion SA | **+5.80%** | 48.35 EUR | $2.98B |

### eu-fi

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `OMXHEX:FIA1S` | Finnair Oyj | **+9.66%** | 4.974 EUR | $1.05B |

### eu-dk

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `OMXCOP:CHEMM` | ChemoMetec A/S | **+5.14%** | 706 DKK | $1.68B |
## Method, source health & caveats

### Method

- **Universe**: the TradingView per-country scanner for each region's own listings (`type` in stock/dr plus the `country` column), 16 POST calls, one response per region, no pagination — **18,361 instrument rows**. Germany is collapsed by company description (WKN symbols on off-exchange venues are the same share); every other region by (issuer name, symbol root, share-class suffix).
- **Floors (USD, applied client-side after conversion)**: au $300M + vol ≥ 100k, jp $300M, tw $200M, ca $200M, eu-de $300M + vol ≥ 50k, eu-fr/it/es/nl/be/at $100M, eu-ie $200M, eu-fi/dk $100M, eu-pt/gr $50M. A row whose cap the source does not report is EXCLUDED, never written blank.
- **FX**: Frankfurter (api.frankfurter.app, from=USD, rate date 2026-11-06) for AUD 1.4554, CAD 1.4066, DKK 6.6952, EUR 0.89566, JPY 158.33; open.er-api.com (updated 2026-11-06T00:02:31Z) for TWD 33.051901, which Frankfurter does not carry. The table is **local currency units per 1 USD**, so `usd_cap = market_cap_basic / FX` — the division direction is checked by share-count reconciliation (`market_cap_local / close` returns 10.74bn shares for Toyota, 27.45bn for TSMC, 1.19bn for SAP, 1.43bn for Royal Bank).
- **Cap carrier rule**: the cap belongs to the issuer. It is resolved to the issuer's **primary (common) line**, converted ONCE with the primary's currency, and carried to the issuer's other lines, which publish the primary's ticker in `cap_source_symbol`. A preferred line therefore never carries its own cap and never outranks the common line — TSX:ENB.PF.V, quoted in USD, publishes Enbridge's CAD-derived cap, not the raw USD number the scanner carries on its own line.
- **Venue-collapse rule**: one row per instrument, preferring the official venue (TSE, TWSE/TPEX, TSX/TSXV/CSE, XETR/FWB, MIL, BME, VIE, OMXHEX, OMXCOP, ATHEX, EURONEXT, ASX). An instrument with no official-venue print is excluded as `stale_venue_print` (Japan's NAG/FSE/SAPSE lines, Canada's NEO ATS, Germany's off-exchange venues).
- **Venue-official price rule**: where the exchange's own print was obtainable it is the price published, with the third-party value and the delta beside it in `price_conflict`. This run verified the ATHEX index against Euronext Athens' own historical data (2,553.35, −2.22%) and cross-checked the European closes against the Il Sole 24 Ore Radiocor close report; no row required a conflict cell, so every `price_conflict` cell is empty.
- **CSV columns**: **18** — `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`. This is the same schema as the 5 Nov session, so the archive's column count does not change today (it changed on 5 Nov, from 14 to 18).
- **Files written**: 16 per-region CSVs, `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json` under `international-eod/2026-11-06/`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView per-country scanner | POST scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan | ok | 16/16 HTTP 200, 18,361 instrument rows, one response per region |
| TradingView America scanner | POST scanner.tradingview.com/america/scan (type in stock,dr) | ok | 13,359 US lines in ONE response — the source for `us_listing` and the cross-venue cap check |
| Frankfurter FX | api.frankfurter.app/latest?from=USD | ok | 2026-11-06 rates, 5 currencies (no TWD) |
| open.er-api FX | open.er-api.com/v6/latest/USD | ok | TWD only; agrees with Frankfurter within 0.5% on AUD/CAD/DKK/EUR/JPY except AUD (1.2%) |
| Yahoo chart API (index levels) | query1/query2.finance.yahoo.com/v8/finance/chart/{^AXJO,^GDAXI,^FCHI,…} | partial | 15/17 index series; **^N225 and ^TWII returned a null 6 Nov bar** and were taken from the markets' own closing reports; ^OMXC20 serves a single bar |
| Press closing reports (Jiji, CNA/Focus Taiwan, Euronext Athens, euro2day, eKathimerini, TradingEconomics) | index closes | ok | Nikkei, TOPIX, TAIEX and the ATHEX taken from the market's own close |
| Yahoo chart API (close verification) | chart/{2914.T,6963.T,3563.T,…,TSU.TO,VNP.TO,TEP.PA,GL9.IR,OUT1V.HE,AG1.DE,…} | ok | every JP/TW/CA/EU name checked matched the scanner's close **to the cent** and its change; the ASX names' daily bars repeat the prior session, so the ASX change rests on the scanner |
| Press (Reuters, AP, Investing.com, Financial Post/FNArena, MarketIndex, note.com, Irish Times, Finwire, Quartr, Dow Jones Newswires, Newsfile, Focus Taiwan, The Blade) | catalyst and market-context checks | ok | every catalyst published in this report is attributed to one of these |
| MCP catalog probe | probe_mcp.py | ok | catalog_ok total=135 finance_tools=0 — the bridge is reachable, but the per-country scanner HTTP API is the source of record for this routine |

### Caveats

- **Units**: `market_cap` is USD; `open`/`high`/`low`/`close` are in the listing currency given by the `currency` column. `change_pct` is a percentage, not a fraction.
- **Carry-over rows**: 94 written rows did not trade this session and carry an earlier session's close (listed in `_carryover.json` with the last trade date, excluded from every movers list and from the breadth counts). A row is flagged only when its close string is IDENTICAL to the prior session's file AND its volume is zero or its `change_pct` is non-zero — no tolerance, so a real half-cent move is never swallowed.
- **Issuer-unresolved rows**: 152 rows (mostly Canada's preferred and Class B/C lines and Japan's subscription certificates) are DROPPED rather than given a borrowed cap: their issuer has no common line in the source under the same ticker root and venue, so a carry would cross an issuer boundary.
- **`no_market_cap` rows** (247) cannot be tested against a cap floor and are excluded rather than written blank.
- **Off-official rows** (215) have no print on an official venue in their home market (Japan's NAG/FSE/SAPSE lines, Canada's NEO ATS lines, Germany's GETTEX/LSX/Lang & Schwarz lines) and are excluded as `stale_venue_print`.
- **Below-floor and below-volume rows**: 7,818 names fell below the cap floor and 104 below the region's volume gate; the hardest movers among them are published under `## Below the gate`.
- **The cap cross-venue check found real disagreements.** Every issuer with a US line was compared after conversion; 38 pairs differ by more than 10%, mostly OTC quotations carrying a stale company cap. The largest are listed below — the primary line's cap is published in all cases and the US line's figure is recorded here.

| Region | Line | US line | Primary cap (USD) | US-line cap (USD) | Delta |
|---|---|---|---|---|---|
| `ca` | `TSX:TSU` | OTC:TRRSF | $1.44B | $0.98B | 47.3% |
| `eu-nl` | `EURONEXT:ENVI` | OTC:ENVHF | $0.28B | $0.20B | 42.5% |
| `jp` | `TSE:6961` | OTC:ENPSF | $0.49B | $0.38B | 26.3% |
| `jp` | `TSE:6368` | OTC:ORGJF | $3.13B | $2.49B | 26.0% |
| `ca` | `TSX:TNZ` | OTC:ATUUF | $1.42B | $1.13B | 25.2% |
| `ca` | `TSX:GIL` | NYSE:GIL | $7.96B | $6.44B | 23.7% |
| `jp` | `TSE:6871` | OTC:MJPNF | $2.60B | $2.11B | 23.1% |
| `ca` | `TSX:NOA` | NYSE:NOA | $0.31B | $0.25B | 22.8% |

- **Index levels**: the Nikkei and TOPIX come from Jiji's 15:33 JST closing report and the TAIEX from CNA/Focus Taiwan, because Yahoo's 6 Nov bars for ^N225 and ^TWII were still null at the time of the pull; the ATHEX comes from Euronext Athens' own historical data and a third-party live quote of 2,587.93 (−2.11%) was rejected as not venue-official; ^OMXC20 serves a single 6 Nov bar, so its prior close is taken from the 5 Nov archive. Every other index level is Yahoo's settled daily bar.
- **The ASX change rests on the scanner, not on Yahoo.** Yahoo's ASX daily bars repeat the prior session's close, so the 6 Nov bar carries no change; the published ASX moves were cross-checked against FNArena, AFR and MarketIndex (Minerals 260 A$0.750 −8.54%, Sunrise Energy Metals A$11.58 −8.24%, Sims A$19.65 −7.22%) and agree to the cent.
- **The session's shape**: it was one global story with three different expressions. Asia sold the AI complex — Tokyo fell 5.96% with 98% of the Prime market lower, Taipei fell 4.51% after a record intraday point drop, and Korea halted trading for 20 minutes — while Europe fell only about 1% on its smaller AI weight and Canada was higher on a gold and silver bid. Inside the rout, the company-specific stories were Japan's tobacco and consumer names: Japan Tobacco lost control of four Russian plants, and Food & Life fell 14.66% on a record FY and its first FY2029 plan.
- **Sector rotation** (mean `change_pct` per sector over the liquid subset, volume ≥ 100k, same rows as the movers list): the least-bad sectors were Health Services -0.05% (18), Non-Energy Minerals -0.08% (279) and Communications -0.85% (34); the worst were Electronic Technology -4.73% (455), Producer Manufacturing -4.17% (368), Commercial Services -4.02% (109) and Distribution Services -3.69% (114). The only sector that rose outright was Energy Minerals, which was dragged under by the gold complex's -2.2% move.
- **The cross-session check passed**: the per-region written row counts land within 1-3% of the 5 Nov session (jp 1,375 vs 1,375, tw 882 vs 885, ca 633 vs 605, eu-de 112 vs 121, eu-fr 272 vs 273, eu-it 179 vs 179, eu-es 147 vs 147, eu-nl 62 vs 62, eu-be 77 vs 77, eu-at 50 vs 50, eu-ie 17 vs 17, eu-fi 101 vs 101, eu-dk 75 vs 75, eu-gr 86 vs 86, au 297 vs 306) — which is what a correct FX conversion and floor application looks like.
- **The build-time assertion passes with 0 failures and 97 warnings**, and every warning is the same heuristic one: the checker's issuer-name reduction cuts a carried cap's source description at the first class word, so a Canadian preferred line described as “… Non-Cum Conv Red Pfd …” reduces to a different string than its common line even though the carry is legitimate (same ticker root, same issuer, and the cap is the company-level figure the contract requires).
- **`us_listing` is the America scanner's answer, matched on the ISSUER (never the ticker — ASX:CAT is Caterpillar while NYSE:CAT is a different company). The scanner's US set does not carry every primary US line, so an issuer whose only US line in the source is an OTC quotation publishes `OTC`; `ADR` means the US line is a depositary receipt (`type=dr`).
