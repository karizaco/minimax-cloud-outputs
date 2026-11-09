# Cron #05 eod-international-daily — Monday, 09 November 2026

## TL;DR

- **Every region but one closed higher, and the tape was a relief rally, not a new advance: 4,308 instruments printed across the 16 regions.** Last week's post-election AI rout was the thing being bought back: Taipei **+4.94%** (its second-largest daily point gain on record, after the National Financial Stabilization Fund authorised intervention), Tokyo **+2.33%** (the Nikkei's first rise in six sessions, with 208 of 225 constituents up), Milan **+2.69%** on an Italian bank consolidation wave, Frankfurt **+1.73%**, Toronto **+1.84%**, Athens **+2.20%**. **Sydney was the outlier: the ASX 200 managed only +0.10%**, because materials +2.88% was offset by all four big banks falling.
- **The most consequential single move is Japan Tobacco (TSE:2914, -15.95%)** — a second straight limit-down, close to -30% in two sessions, after Moscow's 6 November decree put **every** JT entity in Russia under temporary administration (Russia is ~10% of revenue and ~25% of adjusted operating profit, with ~¥1.5tn of assets). The TSE widened JT's daily limit to ±¥4,000 for 10 November. **The reachable names for a US trader are the ADRs and the OTC Italian banks: TSMC +4.68% (ADR), Toyota +4.58% (ADR), ASML +4.69% (ADR), Banco BPM +10.67% (OTC, Crédit Agricole merger proposal) and UniCredit +6.28% (OTC, record Q3).**
- **Read the numbers with the unit convention in mind: `market_cap` is USD while every price is in the listing currency** (the `currency` column says which) — a ¥5,269 close and a C$10.94 close are not comparable, the caps are. This file carries **18 columns**, the same schema as the 6 November session, so the archive's width changed only on 5 November.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,545 | 1,545 | **295** | $300M + vol ≥ 100,000 | 4 | 1,218 | 17 | 11 | 0 | 1 | 0 |
| `jp` | TSE | 3,902 | 3,869 | **1,358** | $300M | 2 | 2,497 | 0 | 12 | 0 | 1 | 0 |
| `tw` | TWSE, TPEX | 2,334 | 2,334 | **846** | $200M | 53 | 1,418 | 0 | 17 | 0 | 1 | 0 |
| `ca` | TSX, TSXV, CSE | 4,299 | 2,690 | **629** | $200M | 33 | 1,856 | 0 | 172 | 0 | 44 | 0 |
| `eu-de` | XETR, FWB | 4,307 | 929 | **108** | $300M + vol ≥ 50,000 | 4 | 462 | 323 | 32 | 0 | 0 | 0 |
| `eu-fr` | EURONEXT | 547 | 547 | **258** | $100M | 3 | 284 | 0 | 2 | 0 | 4 | 0 |
| `eu-it` | MIL | 392 | 392 | **180** | $100M | 2 | 209 | 0 | 1 | 0 | 4 | 0 |
| `eu-es` | BME | 275 | 275 | **147** | $100M | 35 | 93 | 0 | 0 | 0 | 32 | 0 |
| `eu-nl` | EURONEXT | 78 | 78 | **56** | $100M | 0 | 21 | 0 | 1 | 0 | 0 | 0 |
| `eu-be` | EURONEXT | 100 | 100 | **77** | $100M | 1 | 22 | 0 | 0 | 0 | 2 | 0 |
| `eu-at` | VIE | 65 | 65 | **51** | $100M | 3 | 11 | 0 | 0 | 0 | 1 | 0 |
| `eu-pt` | EURONEXT | 32 | 32 | **27** | $50M | 0 | 5 | 0 | 0 | 0 | 0 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| `eu-fi` | OMXHEX | 188 | 188 | **100** | $100M | 4 | 83 | 0 | 1 | 0 | 0 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 58 | 0 | 0 | 0 | 1 | 0 |
| `eu-gr` | ATHEX | 130 | 130 | **84** | $50M | 0 | 44 | 0 | 2 | 0 | 1 | 0 |
| **total** | | **18,347** | **13,327** | **4,308** | | **145** | **8,283** | **340** | **251** | **0** | **92** | **0** |

`Universe` is every instrument the source returns for that country's own listings (the scanner's issuer-country filter, so a foreign company's local line is not counted); `Unique instruments` collapses the same line quoted on several venues down to one line per issuer and share class; `Written` applies the per-region USD market-cap floor plus the region's volume gate. Every excluded row carries a reason from the closed set in `_excluded.json`, and the counts above are read from that file rather than estimated.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 9,029.70 | +8.90 / +0.10% | 2026-11-09 | Yahoo ^AXJO settled bar; AFR, Samso and Investing.com all quote 9,029.7 +0.10%. Yahoo's series omits the 6 Nov bar, so the prior close 9,020.80 is the published 6 Nov close |
| jp | Nikkei 225 | 58,775.50 | +1,340.73 / +2.33% | 2026-11-09 | Jiji Press closing report, 15:30 JST (9 Nov); newsonjapan and Kabutan agree. Yahoo's daily bar had not published at the time of this run |
| jp | TOPIX | 3,818.16 | +110.17 / +2.97% | 2026-11-09 | Jiji Press closing report, 15:30 JST (9 Nov); Kabutan |
| tw | TAIEX | 41,661.70 | +1,960.06 / +4.94% | 2026-11-09 | CNA / Focus Taiwan and the TWSE daily board — second-largest daily point gain on record; range 40,347.28-42,349.36 |
| ca | S&P/TSX Composite | 36,446.26 | +657.16 / +1.84% | 2026-11-09 | Yahoo ^GSPTSE settled bar (16:00 ET). TradingEconomics' CFD read 36,423.30 (+1.77%) is a third-party value, not published |
| eu-de | DAX (Xetra) | 26,267.19 | +446.83 / +1.73% | 2026-11-09 | Yahoo ^GDAXI Xetra close; dpa and Investing.com quote +1.72%. Radiocor's 26,282.55 (+1.89%) is a later auction value and is not published |
| eu-fr | CAC 40 | 8,233.30 | +94.30 / +1.16% | 2026-11-09 | Yahoo ^FCHI; Euronext close as quoted by ideal-investisseur (8,233.30, +1.16%) |
| eu-it | FTSE MIB | 51,399.88 | +1,346.88 / +2.69% | 2026-11-09 | Yahoo FTSEMIB.MI; ANSA reports 51,399 +2.69% — Europe's best session |
| eu-es | IBEX 35 | 19,742.50 | +373.00 / +1.93% | 2026-11-09 | Yahoo ^IBEX; BME's own board (Norbolsa, 17:35) prints 19,742.50 +1.93%. Radiocor's 19,755.29 (+1.99%) is not published |
| eu-nl | AEX | 1,129.97 | +9.42 / +0.84% | 2026-11-09 | Yahoo ^AEX |
| eu-be | BEL 20 | 6,098.09 | +102.02 / +1.70% | 2026-11-09 | Yahoo ^BFX |
| eu-at | ATX | 6,562.46 | +127.66 / +1.98% | 2026-11-09 | Yahoo ^ATX |
| eu-pt | PSI 20 | 9,554.88 | +78.15 / +0.82% | 2026-11-09 | Yahoo PSI20.LS |
| eu-ie | ISEQ | 14,875.33 | +180.25 / +1.23% | 2026-11-09 | Yahoo ^ISEQ |
| eu-fi | OMX Helsinki 25 | 6,278.95 | +57.16 / +0.92% | 2026-11-09 | Yahoo ^OMXH25; Inderes' OMX Helsinki PI prints 13,135 +1.33% |
| eu-dk | OMX Copenhagen 20 | 1,668.69 | +10.24 / +0.62% | 2026-11-09 | Yahoo ^OMXC20 (single 9 Nov bar); Investing.com quotes +0.63% |
| eu-gr | ATHEX General | 2,609.63 | +56.28 / +2.20% | 2026-11-09 | Euronext Athens' own historical data via eKathimerini (2,609.63, +2.20%); euro2day and iefimerida agree. There is no Yahoo symbol for the ATHEX |
| *context* | STOXX 600 | 656.52 | +1.26% | 2026-11-09 | Irish Times Europe close (9 Nov) |

**One story, one catalyst.** Last week the Democrats' sweep in the US midterms was read as a threat to the pace of the AI data-centre build-out and the global AI complex was liquidated; on Monday, US-Iran de-escalation hopes pushed **Brent to about $93-94 (-5%)**, which eased the inflation worry, and buyers took back the semiconductor complex - **Infineon +6.27%, ASML +4.69%, ASM +3.38%, TSMC +4.68%, Soitec +5.87%** - while the European banks were carried by an Italian consolidation wave (**Banco BPM +10.67%** on Credit Agricole's proposal, **UniCredit +6.28%** on a 24% jump in Q3 profit, Intesa +2.8% after Consob cleared its MPS tender offer). **Gold and uranium bid hard**: Barrick +4.5% on Q3, Paladin +10.86%, Silex +12.12%, and the London precious-metal miners +4.5%. **Japan Tobacco was the single name that could not be bought back.**

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 295 | +0.00% | 142 / 133 / 20 | -16.23% | +12.68% |
| jp | 1,358 | +2.31% | 1220 / 124 / 14 | -15.95% | +22.74% |
| tw | 846 | +3.76% | 683 / 130 / 33 | -10.00% | +13.70% |
| ca | 629 | +0.69% | 403 / 156 / 70 | -11.06% | +37.96% |
| eu-de | 108 | +0.56% | 68 / 39 / 1 | -4.36% | +6.92% |
| eu-fr | 258 | +0.34% | 147 / 86 / 25 | -4.79% | +11.76% |
| eu-it | 180 | +0.68% | 122 / 44 / 14 | -4.35% | +12.59% |
| eu-es | 147 | +0.21% | 76 / 29 / 42 | -8.24% | +10.97% |
| eu-nl | 56 | +0.40% | 34 / 17 / 5 | -2.89% | +4.69% |
| eu-be | 77 | +0.91% | 55 / 20 / 2 | -4.25% | +21.78% |
| eu-at | 51 | +0.88% | 34 / 9 / 8 | -2.13% | +6.90% |
| eu-pt | 27 | +0.52% | 16 / 5 / 6 | -4.21% | +3.60% |
| eu-ie | 17 | +0.32% | 10 / 5 / 2 | -1.51% | +4.76% |
| eu-fi | 100 | +0.00% | 49 / 43 / 8 | -5.66% | +11.83% |
| eu-dk | 75 | +0.45% | 44 / 25 / 6 | -6.36% | +5.20% |
| eu-gr | 84 | +0.38% | 49 / 18 / 17 | -1.97% | +5.40% |

**The index and the typical name agree everywhere except Australia.** In Tokyo the median published name rose while the index added 2.33% — the rebound was broad (semis, banks, retail), not index-led. In Taipei the median name rose as well. **In Australia the index managed +0.10% because the median name was flat-to-lower: the banks fell while materials rose, and the median Sydney name did not share the materials bid.** In Europe the median name is a fraction of the index move, which says the index moves were led by the large caps — banks and semiconductors — rather than by the broad market.

## Top movers

Liquid names (volume ≥ 100,000 **and** market cap ≥ $1B) whose move cleared ±5%, capped at the six largest absolute moves per region, with the driver that was actually sourced. A row with no sourced driver is not here — it is under `## No catalyst`.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:VNT` | Ventia Services Group Limited | **-16.23%** | 4.8 AUD | 9,199,537 | $3.22B | NYSE | FY26 results: the telecommunications and energy segments remain challenging and second-half group revenue is expected to be below the same half a year ago; underlying NPATA growth is still guided to 7-10% with at least A$60m of annualised savings by December 2027. The shares fell to a 52-week low (AFR and ABC market wraps, 9 Nov; Samso market update, 9 Nov) |
| `ASX:DNL` | Dyno Nobel Limited | **-10.99%** | 3.4 AUD | 11,149,542 | $4.61B | none | Annual results day - the second-biggest ASX 200 fall of the session, and the biggest blue-chip fall of the day alongside Ventia (ABC market wrap, 9 Nov; Samso market update, 9 Nov) |
| `ASX:PDN` | Paladin Energy Ltd | **+10.86%** | 8.27 AUD | 4,276,521 | $2.31B | OTC | Uranium: Paladin rose with the uranium complex, the ASX's strongest materials names, as the metals bid returned (ABC market wrap, 9 Nov; Samso market update, 9 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:1515` | Nittetsu Mining Co., Ltd. | **+17.67%** | 3110 JPY | 993,600 | $1.34B | none | Nittetsu Mining rose with the metals complex - the Nikkei's materials sector led the session - and no company-specific release was found (Jiji Press sector report, 9 Nov; Kabutan gainers ranking, 9 Nov) |
| `TSE:6787` | Meiko Electronics Co., Ltd. | **+16.10%** | 7210 JPY | 752,000 | $2.07B | OTC | H1 operating profit Y17.5bn, +53.2% y/y, with the full-year earnings and dividend forecasts revised upward; the shares hit the limit-up on the earnings beat (Fisco Japan, 9 Nov; Jiji Press, 9 Nov) |
| `TSE:2914` | Japan Tobacco Inc. | **-15.95%** | 5269 JPY | 10,929,900 | $70.47B | OTC | Russia's 6 Nov presidential decree added three more JTI entities - including JTI Russia, the sales company - so ALL of JT's Russian subsidiaries are now under temporary administration. JT disclosed that Russia is ~10% of revenue and ~25% of adjusted operating profit, with ~Y1.5tn of Russia-related assets. The shares were untraded at the limit for a second straight day (closed Y5,269, -1,000 yen, 10.93m shares) and the TSE widened the daily limit to Y4,000 for 10 Nov (Reuters/Dow Jones, 9 Nov; JT disclosure, 9 Nov; NHK World, 9 Nov; The Star, 9 Nov) |

### tw

The TAIEX jumped 4.94% - its second-largest daily point gain on record - after the National Financial Stabilization Fund authorised intervention on Friday; foreign investors still sold a net NT$90.06bn (CNA / Focus Taiwan, 9 Nov).

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:GFR` | Greenfire Resources Ltd. | **+37.96%** | 10.94 CAD | 3,514,974 | $1.35B | NYSE | Strathcona Resources said on Sunday it would acquire Greenfire Resources in a deal valued at about C$2.7-2.9bn including debt, expanding its Alberta oil-sands position; the shares jumped about 38% (Yahoo Finance/Toronto Star, 9 Nov; TradingEconomics, 9 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:HAG` | HENSOLDT AG | **+6.92%** | 82.8 EUR | 253,432 | $10.01B | OTC | Top MDAX and TecDAX performer, +6.92% to EUR 82.80, as the European defence sector rose 4.2% (Investing.com, 9 Nov; Irish Times, 9 Nov) |
| `XETR:DEZ` | DEUTZ AG | **+6.59%** | 9.86 EUR | 1,391,791 | $2.48B | OTC | DEutz rose with the industrials rebound and the defence/energy-engineering complex; no company-specific release was found (Investing.com Europe close, 9 Nov) |
| `XETR:IFX` | Infineon Technologies AG | **+6.27%** | 48.62 EUR | 5,295,742 | $66.65B | OTC | Led the DAX higher: buyers judged that last week's post-election AI rout had pushed semiconductor valuations into oversold territory, and Infineon rose 6.27% to EUR 48.63 in the relief rally (Investing.com/dpa, 9 Nov; Reuters and Investing.com, 9 Nov) |
| `XETR:ENR` | Siemens Energy AG | **+5.08%** | 124.1 EUR | 2,728,715 | $111.15B | NYSE | Second-biggest DAX gainer, +5.08% to EUR 124.10, in the industrials-led rebound (Investing.com, 9 Nov; dpa, 9 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:SOI` | Soitec SA | **+5.87%** | 99.88 EUR | 376,065 | $3.78B | OTC | Soitec rebounded above its EUR 91.64 support, +5.87% to EUR 99.88, among the strongest SBF 120 gainers as the semiconductor complex recovered (ideal-investisseur, 9 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:BAMI` | Banco BPM SpA | **+10.67%** | 14.88 EUR | 15,069,632 | $22.75B | OTC | Credit Agricole proposed a friendly merger between its Italian subsidiary and Banco BPM - a EUR 1bn dividend for roughly a 45% stake in the combined group, creating Italy's third-largest bank - and BPM rose as much as 12% intraday before closing +10.6% at EUR 14.88 (ANSA, 9 Nov; Dow Jones, 9 Nov; Il Sole 24 Ore, 9 Nov) |
| `MIL:NWL` | NewPrinces S.p.A. | **+8.86%** | 26.3 EUR | 351,339 | $1.16B | NASDAQ | NewPrinces rose with the Italian technology recovery; no company-specific release was found (Il Sole 24 Ore, 9 Nov) |
| `MIL:AVIO` | Avio SpA | **+7.71%** | 31.15 EUR | 844,572 | $1.60B | OTC | Avio rose 7.71% with the Italian technology-sector recovery, alongside Prysmian and ST (Il Sole 24 Ore, 9 Nov) |
| `MIL:UCG` | UniCredit S.p.A. | **+6.28%** | 81.62 EUR | 10,119,849 | $129.63B | OTC | Third-quarter net profit rose 24% year on year, far above forecasts, and 2026 guidance was raised - 'the best quarter ever' per CEO Orcel - as the bank prepares its strategy for Commerzbank (ANSA, 9 Nov; Il Sole 24 Ore, 9 Nov; Reuters, 9 Nov) |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `BME:ENO` | Elecnor S.A. | **+7.92%** | 31.35 EUR | 128,562 | $2.75B | NYSE | The board proposed the distribution of a dividend against unrestricted reserves, filed with the CNMV as inside information at 12:14 on 9 Nov (CNMV, 9 Nov) |
| `BME:ALM` | Almirall SA | **-6.42%** | 10.5 EUR | 631,073 | $2.73B | NASDAQ | Almirall fell 6.42% to EUR 10.50 with no company-specific release found (BME board via Norbolsa, 9 Nov) |

### eu-nl

No name cleared the ±5% screen with a $1bn cap. ASML rose 4.69%, ASM International 3.38% and Koninklijke BAM 4.52% in the European semiconductor rebound.

### eu-be

No name cleared the ±5% screen with a $1bn cap. Hyloris Pharmaceuticals rose 21.78% and Texaf 7.22%; KBC added 2.77%.

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | **+5.29%** | 111.4 EUR | 269,671 | $4.60B | NYSE | AT&S rose 5.29% with the European electronics rebound; no company-specific release was found (Investing.com Europe close, 9 Nov) |

### eu-pt

No name cleared the ±5% screen with a $1bn cap. Banco Comercial Portugues rose 3.60% and Sporting Clube de Portugal fell 4.21%.

### eu-ie

No name cleared the ±5% screen with a $1bn cap. The session's notable move was Irish Residential Properties REIT +4.76% to EUR 1.364, whose board accepted an all-cash offer of EUR 731m from Barings Investment (Irish Times, 9 Nov).

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:IQMX` | IQM Quantum Computers Oyj Class A | **+9.15%** | 7.275 EUR | 174,620 | $1.49B | ADR | IQM Quantum rose 9.15% with the European technology rebound; no company-specific release was found (Inderes market data, 9 Nov) |
| `OMXHEX:FIA1S` | Finnair Oyj | **+8.26%** | 5.385 EUR | 1,134,358 | $1.14B | OTC | Finnair rose 8.26% as Brent fell to about USD 93-94 (-5%) on hopes of US-Iran de-escalation, taking jet fuel lower; airlines bid (Il Sole 24 Ore, 9 Nov; Irish Times, 9 Nov) |
| `OMXHEX:NOKIA` | Nokia Oyj | **+5.30%** | 7.352 EUR | 14,994,612 | $44.22B | OTC | Nokia was the most-traded Helsinki name, +5.30%, in the European technology rebound (Inderes market data, 9 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:ZEAL` | Zealand Pharma A/S | **+5.20%** | 245 DKK | 627,301 | $2.31B | OTC | Boehringer Ingelheim reported positive Phase 3 SYNCHRONIZE-CVOT results for survodutide - the first glucagon/GLP-1 dual agonist to show a favourable cardiovascular safety profile - released by Zealand as inside information at 15:45 CET (company release, 9 Nov) |

### eu-gr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ATHEX:ETE` | National Bank of Greece S.A. | **+5.04%** | 17.1 EUR | 3,108,963 | $16.45B | OTC | National Bank of Greece rose 5.04% with the banking index up 3.57% (eKathimerini and euro2day, 9 Nov) |

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) — published because a +38% or a -24% move is not noise. Their tickers are printed without the backtick ticker format used for CSV rows precisely because they are not CSV rows.

### au

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ASX:FHS | Freehill Mining Ltd. | **+100.00%** | 8,000 | below the $300M cap floor + vol ≥ 100,000 |
| ASX:ATC | Altech Batteries Limited | **+100.00%** | 1,483,408 | below the $300M cap floor + vol ≥ 100,000 |

### jp

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSE:2667 | ImageONE Co., Ltd. | **+42.86%** | 6,720,200 | below the $300M cap floor |
| TSE:2134 | Kitahama Capital Partners Co., Ltd. | **+41.67%** | 23,907,100 | below the $300M cap floor |

### tw

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TPEX:5355 | Gia Tzoong Enterprise Co. Ltd. | **+104.70%** | 73,750 | below the $200M cap floor |
| TPEX:5246 | ProbeLeader Co Ltd | **+37.33%** | 1,076,371 | below the $200M cap floor |

### ca

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| TSXV:HXC.H | HFX Holding Corp. | **+300.00%** | 1,000 | below the $200M cap floor |
| TSXV:REE | ReeXploration Inc. | **+266.70%** | 5,610 | below the $200M cap floor |

### eu-de

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| LS:A3E5C0 | co.don AG | **-62.50%** | 220 | below the $300M cap floor + vol ≥ 50,000 |
| LS:A1PG50 | Fast Finance24 Holding AG | **-61.54%** | 5,000 | below the $300M cap floor + vol ≥ 50,000 |

### eu-fr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:NACON | Nacon SAS | **+24.24%** | 1,110,192 | below the $100M cap floor |
| EURONEXT:JBOG | Jacques Bogart SA | **+21.37%** | 24,398 | below the $100M cap floor |

### eu-it

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| MIL:TCM | Tecma Solutions SpA | **+26.00%** | 111,600 | below the $100M cap floor |
| MIL:RN | Risanamento S.p.A. | **-22.67%** | 81,809,449 | below the $100M cap floor |

### eu-es

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| BME:ETC | Energy Solar Tech, S.A. | **+8.70%** | 1,916 | below the $100M cap floor |
| BME:END | Endurance Motive SA | **-8.33%** | 20,060 | below the $100M cap floor |

### eu-nl

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:SIFG | Sif Holding N.V. | **-23.96%** | 820,243 | below the $100M cap floor |
| EURONEXT:BEVER | N.V. Bever Holding | **-7.14%** | 100 | below the $100M cap floor |

### eu-be

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| EURONEXT:OPTI | OPTION | **+17.43%** | 9,425 | below the $100M cap floor |
| EURONEXT:MLTV | CHOICE NV | **-9.65%** | 13,737 | below the $100M cap floor |

### eu-fi

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXHEX:LAMOR | Lamor Corporation Oyj | **-13.90%** | 63,215 | below the $100M cap floor |
| OMXHEX:NANOFH | Nanoform Finland Oyj | **+10.73%** | 113,927 | below the $100M cap floor |

### eu-dk

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| OMXCOP:FASTPC | FastPassCorp A/S | **-16.19%** | 216 | below the $100M cap floor |
| OMXCOP:WIRTEK | Wirtek A/S | **+6.21%** | 5,315 | below the $100M cap floor |

### eu-gr

| Ticker | Name | Change | Volume | Reason |
|---|---|---|---|---|
| ATHEX:CPI | CPI Computer Peripherals International S.A. | **-6.96%** | 13,760 | below the $50M cap floor |

## No catalyst

Liquid names that cleared ±5% with **no sourced driver** — no company release, no filing, no analyst action and no sourced sector or macro move behind them. Kept separate so they do not dilute the mover table.

### au

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `ASX:EQR` | EQ Resources Limited | **+8.93%** | 0.305 AUD | $1.00B |
| `ASX:SRL` | Sunrise Energy Metals Limited | **+8.72%** | 12.59 AUD | $1.38B |
| `ASX:MI6` | Minerals 260 Limited | **+8.00%** | 0.81 AUD | $1.32B |

### jp

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `TSE:4912` | Lion Corporation | **+14.42%** | 2118 JPY | $3.18B |
| `TSE:7966` | Lintec Corporation | **+11.69%** | 4825 JPY | $1.86B |
| `TSE:8425` | Mizuho Leasing Company, Limited | **+11.17%** | 1374 JPY | $2.44B |

### tw

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `TPEX:7861` | Bellwether Electronic Corp. | **+13.70%** | 697 TWD | $1.21B |
| `TPEX:3081` | LandMark Optoelectronics Corp. | **+10.00%** | 1925 TWD | $5.41B |
| `TPEX:3163` | Browave Corporation | **+10.00%** | 434.5 TWD | $1.14B |

### ca

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `TSX:FDY` | Faraday Copper Corp | **+10.91%** | 4.37 CAD | $1.20B |
| `TSX:HPS.A` | Hammond Power Solutions Inc. Class A | **+10.55%** | 207.8 CAD | $1.59B |
| `CSE:HG` | Hydrograph Clean Power Inc | **+10.42%** | 4.45 CAD | $1.04B |

### eu-fr

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `EURONEXT:NANO` | Nanobiotix SA | **+5.56%** | 28.5 EUR | $1.54B |
| `EURONEXT:MEDCL` | MedinCell SA | **+5.49%** | 30 EUR | $1.14B |

### eu-it

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `MIL:PRY` | Prysmian S.p.A. | **+5.94%** | 107 EUR | $33.83B |

### eu-es

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `BME:TRE` | Tecnicas Reunidas SA | **+5.18%** | 30.88 EUR | $2.57B |

### eu-gr

| Ticker | Name | Change | Close | Mkt cap (USD) |
|---|---|---|---|---|
| `ATHEX:EUROB` | EUROBANK S.A. | **+5.40%** | 4.726 EUR | $17.99B |

## Method, source health & caveats

### Method

- **Universe** — the TradingView per-country scanner, one pull per region, filtered on the issuer's `country` field so a region's file holds that country's own issuers (this reproduces the 6 November session's universe counts: at 65/65, it 392/392, dk 134/134, ie 19/19, fi 188/188). Venue duplicates of the same line collapse to one row per issuer and share class; every preferred SERIES stays its own line.
- **Floors (USD, applied AFTER the FX conversion)** — au $300M + vol ≥ 100,000; jp $300M; tw $200M; ca $200M; eu-de $300M + vol ≥ 50,000; eu-fr/eu-it/eu-es/eu-nl/eu-be/eu-at/eu-fi/eu-dk $100M; eu-ie $200M; eu-pt/eu-gr $50M. A row whose source reports no market cap is EXCLUDED (`no_market_cap`), never written blank.
- **FX** — Frankfurter (2026-11-09) for AUD 1.4505, CAD 1.4103, DKK 6.6785, EUR 0.89342, JPY 157.95; open.er-api (09 Nov 2026 00:02 UTC) for TWD 32.851408. **These tables are local units per 1 USD, so the conversion is a DIVISION**: `usd_cap = market_cap_local / FX_per_USD`. The direction is settled by share-count reconciliation (`market_cap_local / close` returns the issuer's real share count) and by the identity `usd_cap × FX_per_USD == market_cap_local`.
- **Cap carrier rule** — the cap belongs to the ISSUER and is resolved to the group's **primary (common) line**, converted ONCE with that line's currency, and every other line of the issuer carries it and names it in `cap_source_symbol`. A group with no common line has no primary and is dropped (`issuer_unresolved`). The primary's line is the common line whose ticker carries no share-class suffix.
- **Venue-official price rule** — where an exchange's own official close was obtainable it is the published close and any third-party difference is recorded in `price_conflict`. This run published **no `price_conflict` cells**: every row's close is the scanner's session print, and the three index rows where a third party disagreed (TSX CFD 36,423.30 vs 36,446.26; Radiocor's DAX 26,282.55 vs the Xetra close 26,267.19; Radiocor's IBEX 19,755.29 vs 19,742.50) are index rows, published in the index table with the third-party value named in the source column.
- **`us_listing`** — from the America scanner (`types = ["stock","dr"]`, 13,470 rows), matched to the issuer by ticker root first and then by normalised issuer name, because a US ADR carries a different ticker root (TSE:7203 → NYSE:TSM). A `dr` line is `ADR`, a US-own listing is `NYSE`/`NASDAQ`, an OTC quotation is `OTC`, no match is `none`.
- **Columns** — **18** (`date, ticker, name, open, high, low, close, volume, change_pct, market_cap, pe_ratio, sector, currency, exchange, cap_source_symbol, share_class, us_listing, price_conflict`), unchanged from the 6 November session, so the archive's width did not change today.
- **Files written** — 16 region CSVs (`<region>.csv`), `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json` in `international-eod/2026-11-09/`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView per-country scanner | POST scanner.tradingview.com/{country}/scan, types=["stock"], filter country=<region country> | ok | 16 regions, 18,347 rows pulled |
| TradingView America scanner | POST scanner.tradingview.com/america/scan, types=["stock","dr"] | ok | 13,470 rows — the source for `us_listing` and the cross-venue cap second reading |
| Frankfurter | api.frankfurter.dev/v1/latest?base=USD | ok | 2026-11-09 table: AUD, CAD, DKK, EUR, JPY |
| open.er-api | open.er-api.com/v6/latest/USD | ok | TWD 32.851408 (09 Nov 2026 00:02 UTC) |
| Yahoo chart API (indexes) | query1.finance.yahoo.com/v8/finance/chart/{index} | ok for 14 of 16 | au/jp/tw daily bars are incomplete or absent — the ASX series omits the 6 Nov bar and Japan's and Taiwan's 9 Nov bars had not published; those three are taken from the exchange's own closing reports |
| Yahoo chart API (price spot-checks) | 7203.T, 2330.TW, 2914.T intraday | ok | Toyota 3,491, TSMC 2,235 and JT 5,269 all match the published closes to the tick — Japan's and Taiwan's scanner prints are this session's, not the prior session's |
| ATHEX close | Euronext Athens historical data via eKathimerini | ok | 2,609.63 +2.20% — there is no Yahoo symbol for the ATHEX |
| Press wire (catalysts) | ANSA, Reuters, Dow Jones, Jiji, CNA, eKathimerini, Investing.com, Irish Times, Il Sole 24 Ore, ABC/AFR, Inderes, Kabutan, CNMV, ACCESS Newswire | ok | catalyst for every name in `## Top movers` |

### Caveats

- **Carry-over rows** — 92 instruments across the 16 regions did not trade today (their close is identical to the 6 November published close and the row carries no volume or a stale non-zero change). They are published as the source returned them, listed in `_carryover.json` with each instrument's last trade date, and excluded from every movers list.
- **The share-count plausibility band is not a defect** — 22 published rows imply fewer than a million shares (micro-caps with a genuinely tiny share count, e.g. VIE:HRX5 and EURONEXT:COBH). The guard that matters is the issuer-preservation assertion, which passes for every published row.
- **The ATHEX constituent close for Cenergy** is published at EUR 21.90 from the scanner against EUR 21.54 in Investing.com's late-trade read — a third-party late quote, not the auction print.
- **Australia's index series is one session out of step** — Yahoo's ^AXJO carries no 6 November bar, so the prior close 9,020.80 is the published 6 November close and today's 9,029.70 (+0.10%) is confirmed by AFR, Samso and Investing.com.
- **A cap claim without a second reading is not publishable**, and the second reading here is the America scanner's own company-level cap. Where the US line and the local line disagree the local primary line's cap is the one published.
- **This is a full-universe pull, not a watchlist** — the 12-name personal watchlist is not used as a universe anywhere in this routine.

