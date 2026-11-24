# Cron #05 eod-international-daily — Tuesday, 24 November 2026

## TL;DR

- **Asia ripped, Europe gave it all back.** Nvidia's board reinstated Jensen Huang as CEO overnight and the AI complex split by geography: the **TAIEX closed +8.99% at 40,122.35, a record 3,310.46-point single-day gain**, the **Nikkei +3.91% at 58,644.56** in its first session after the 21-23 November holiday, and the **ASX 200 +1.82% at 8,726.40** - while **Europe sold the same trade back**, with the DAX **-1.26% at 25,017.81**, the FTSE MIB **-1.84%**, the ATX **-1.90%** and the **STOXX 600 -0.66% at 632.74**. **4,202 names were published across all 16 boards**, and every board traded: no market was closed, and Japan is back after two lost sessions.
- **The one consequential move was the split in the AI-hardware trade itself.** Japanese suppliers ripped and European suppliers fell in the same session - a US trader can reach both sides: **Advantest +12.45%** (ADR), **Murata Manufacturing +14.89%** (ADR), **IBIDEN +14.98%** (OTC), **TSMC +9.85%** (ADR) and **ASE Technology +9.96%** (ADR) on the way up, against **ASML -5.58%** (ADR), **ASM International -7.97%** (ADR), **BE Semiconductor -8.79%** (ADR), **Infineon -9.68%** (ADR), **Aixtron -16.32%** (OTC) and **AT&S -12.34%** (OTC) on the way down - with **Sanofi +9.76%** (ADR, the Insmed deal) and **Clariane +35.30%** the stand-out non-tech winners and **First Quantum -10.35%** (OTC, the Kansanshi fatality) the stand-out loser.
- **The caveat that changes how to read it: `market_cap` is in USD while `open`/`high`/`low`/`close` are in the listing currency** (the `currency` column says which), and Taiwan's **+10.00% prints are limit prices, not calculated moves** - 621 Taiwanese stocks closed limit-up, so the TAIEX's +8.99% is a ceiling, not a valuation. Two further facts change the numbers themselves: **Europe's chip leg has its own driver** (US export curbs added Megaspeed to the Entity List on 23 November, and Nvidia fell 8.12% in US trading on criticism of the board's reinstatement), and **one row, `TPEX:7861` +32.78%, prints outside Taiwan's +/-10% band** - the limit-band class the archive flagged on 23 November, kept out of the published tables.

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| au | 1 | 1548 | 1548 | 292 | $300M + vol >= 100,000 | 4 | 1233 | 18 | 1 | 0 | 2 | 0 |
| jp | 3 | 3890 | 3867 | 1347 | $300M | 3 | 2516 | 0 | 1 | 0 | 0 | 0 |
| tw | 2 | 2345 | 2345 | 787 | $200M | 58 | 1500 | 0 | 0 | 0 | 1 | 0 |
| ca | 3 | 4286 | 2709 | 604 | $200M | 62 | 1918 | 0 | 125 | 0 | 26 | 0 |
| eu-de | 1 | 4303 | 709 | 121 | $300M + vol >= 50,000 | 4 | 400 | 184 | 0 | 0 | 0 | 0 |
| eu-fr | 1 | 543 | 543 | 257 | $100M | 1 | 285 | 0 | 0 | 0 | 4 | 0 |
| eu-it | 1 | 377 | 377 | 177 | $100M | 2 | 198 | 0 | 0 | 0 | 3 | 0 |
| eu-es | 1 | 230 | 230 | 134 | $100M | 24 | 72 | 0 | 0 | 0 | 22 | 0 |
| eu-nl | 1 | 78 | 78 | 56 | $100M | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| eu-be | 1 | 101 | 101 | 76 | $100M | 1 | 24 | 0 | 0 | 0 | 2 | 0 |
| eu-at | 1 | 65 | 65 | 50 | $100M | 2 | 13 | 0 | 0 | 0 | 3 | 0 |
| eu-pt | 1 | 30 | 30 | 26 | $50M | 0 | 4 | 0 | 0 | 0 | 2 | 0 |
| eu-ie | 1 | 19 | 19 | 16 | $200M | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| eu-fi | 1 | 189 | 189 | 101 | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| eu-dk | 1 | 133 | 133 | 75 | $100M | 1 | 57 | 0 | 0 | 0 | 0 | 0 |
| eu-gr | 1 | 127 | 127 | 83 | $50M | 0 | 44 | 0 | 0 | 0 | 3 | 0 |
| **total** | | 18264 | | **4202** | | 166 | 8373 | 202 | 127 | 0 | 68 | 0 |

The exclusion counts are the per-reason counts in `_excluded.json`, not estimates, and the reconciliation identity `unique_instruments == written + sum(excluded)` holds for every region. Written rows are 4202 against 2841 on 23 November - a 15-board artifact then, all 16 today with Japan back - and the 15 boards that traded on both days are within 0.4% of the prior session's counts, which is the cheapest available proof that the FX conversion direction, the per-region floors and the cap-carrier rule all still hold.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 8,726.40 | +155.80 / +1.82% | 2026-11-24 | TradingView SP:XJO; samso Market Update (close 4:30pm AEDT) and ABC's live blog both report 8,726.4, up 155.8 points or 1.82% - the first gain in nearly two weeks |
| jp | Nikkei 225 | 58,644.56 | +2,207.91 / +3.91% | 2026-11-24 | TradingView TVC:NI225; Trading Economics reports the close at 58,645, up 2,207.98 points or 3.91%, the post-holiday rebound after Nvidia reinstated Jensen Huang - the index touched 59,262.57 intraday |
| jp | TOPIX | 3,764.88 | +90.66 / +2.47% | 2026-11-24 | TradingView TSE:TOPIX |
| tw | TAIEX | 40,122.35 | +3,310.46 / +8.99% | 2026-11-24 | TradingView TWSE:IX0001; CNA (Focus Taiwan) and Taiwan News report the close at 40,122.35, up 3,310.46 points or 8.99% - a record single-day point gain, past the previous record of 3,186.45 points set on 31 July - after a 3,368.49-point intraday swing between 39,148.91 and 40,180.48, on turnover of NT$419.4bn, with 335 main-board and 286 OTC stocks closing limit-up |
| ca | S&P/TSX Composite | 33,962.25 | -119.19 / -0.35% | 2026-11-24 | TradingView TSX:TSX; Reuters had it down 0.42% at 33,939.50 mid-session as miners fell on softer gold and the heavyweight financial sector lagged |
| eu-de | DAX | 25,017.81 | -319.46 / -1.26% | 2026-11-24 | TradingView XETR:DAX; finanznachrichten/dpa-AFX report the close at 25,017.81, down 1.26%, with tech under pressure on US import-tariff worries |
| eu-fr | CAC 40 | 8,040.49 | -4.35 / -0.05% | 2026-11-24 | TradingView EURONEXT:PX1; BourseDirect and Boursorama report the close at 8,040.49, down 0.05%, with the SBF 120 down 0.04% |
| eu-it | FTSE MIB | 48,121.19 | -900.74 / -1.84% | 2026-11-24 | TradingView FTSE:FTSEMIB |
| eu-es | IBEX 35 | 19,015.80 | -165.30 / -0.86% | 2026-11-24 | TradingView BME:IBC |
| eu-nl | AEX | 1,077.41 | -11.67 / -1.07% | 2026-11-24 | TradingView EURONEXT:AEX |
| eu-be | BEL 20 | 5,884.12 | -3.67 / -0.06% | 2026-11-24 | TradingView EURONEXT:BEL20 |
| eu-at | ATX | 6,221.75 | -120.26 / -1.90% | 2026-11-24 | TradingView VIE:ATX |
| eu-pt | PSI 20 | 9,333.54 | +17.68 / +0.19% | 2026-11-24 | TradingView EURONEXT:PSI20 |
| eu-ie | ISEQ | 14,421.15 | -220.79 / -1.51% | 2026-11-24 | TradingView EURONEXT:ISEQ |
| eu-fi | OMX Helsinki 25 | 5,954.82 | -58.57 / -0.97% | 2026-11-24 | TradingView OMXHEX:OMXH25 - note Investing.com's close table prints the index down 1.03%; the scanner's settle prints -0.97% and no OMX official close was obtained |
| eu-dk | OMX Copenhagen 20 | 1,626.40 | +10.95 / +0.68% | 2026-11-24 | TradingView OMXCOP:OMXC20 |
| eu-gr | ATHEX General | 2,524.88 | -37.48 / -1.46% | 2026-11-24 | **Euronext Athens' own print, via euro2day (24 Nov, 17:44) and xrimatistirio's close table**: close 2,524.88, down 37.48 points or 1.46%, a four-month low (the last lower close was 28 July, 2,521.18), on a range of 2,571.05 (+0.34%) to 2,522.27 (-1.56%), with 24 stocks rising against 86 falling and 17 unchanged - the ATHEX has no Yahoo symbol and no TradingView venue index |
| *context* | STOXX Europe 600 | 632.74 | -4.23 / -0.66% | 2026-11-24 | TradingView STOXX:SXXP |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 292 | +2.03% | 260 / 23 / 9 | -6.57% | +32.35% |
| jp | 1347 | +0.78% | 850 / 472 / 25 | -8.13% | +15.04% |
| tw | 787 | +8.62% | 770 / 13 / 4 | -9.99% | +41.67% |
| ca | 604 | -0.11% | 229 / 325 / 50 | -23.79% | +10.84% |
| eu-de | 121 | -0.31% | 52 / 68 / 1 | -16.32% | +5.18% |
| eu-fr | 257 | +0.32% | 140 / 93 / 24 | -9.97% | +35.30% |
| eu-it | 177 | -0.36% | 58 / 104 / 15 | -10.09% | +6.21% |
| eu-es | 134 | +0.00% | 46 / 55 / 33 | -6.87% | +3.45% |
| eu-nl | 56 | +0.04% | 28 / 27 / 1 | -8.79% | +5.36% |
| eu-be | 76 | +0.03% | 38 / 32 / 6 | -7.15% | +4.55% |
| eu-at | 50 | -1.30% | 9 / 35 / 6 | -12.91% | +4.76% |
| eu-pt | 26 | +0.31% | 15 / 9 / 2 | -8.22% | +2.50% |
| eu-ie | 16 | -0.17% | 3 / 9 / 4 | -4.74% | +1.77% |
| eu-fi | 101 | -0.79% | 34 / 62 / 5 | -6.73% | +4.06% |
| eu-dk | 75 | -0.35% | 29 / 42 / 4 | -6.70% | +6.72% |
| eu-gr | 83 | -1.07% | 13 / 60 / 10 | -4.80% | +1.33% |

The index level and the typical name disagree in both directions today, which is why both are published: Taiwan's index rose 8.99% while its median name closed at a limit price, and Germany's index fell 1.26% while its median name fell far more than that, because the damage was concentrated in semis, metals and industrials while banks, telecoms and insurers held up.

## Top movers

Liquid names (volume >= 100,000, market cap at or above the region's floor) whose move cleared +/-5%, with the driver that was actually sourced, largest absolute move first within the region. A row with no sourced driver is not here - it is under `## No catalyst`. Each region also publishes its single biggest liquid mover even when it did not clear +/-5%, so no region is silent; a region with no name at all says so instead of publishing an unsourced row. Taiwan and Japan each had far more qualifying names than a table can carry: the tables publish the largest movers with a sourced driver, and the remainder stays in the CSVs.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:LOV` | Lovisa Holdings Ltd. | **+10.58%** | 26.54 AUD | 830,436 | $1.77B | none | Rose 10.58% to A$26.54 on its AGM trading update: global sales for the first 21 weeks of FY27 up 15.5% on a constant-currency basis, with comparable store sales up 3.4% (samso Market Update, 24 Nov; MarketIndex Evening Wrap, 24 Nov) |
| `ASX:TEA` | Tasmea Limited | **+10.38%** | 8.4 AUD | 1,775,664 | $1.42B | OTC | Rose 10.38% to A$8.40 on agreeing to buy ABC Group, a Mackay-based Bowen Basin engineering-services business, for A$135.0m upfront - A$65.0m cash plus A$70.0m of new Tasmea shares at A$12.00 - with settlement targeted for on or about 31 December 2026 subject to ACCC approval (samso Market Update, 24 Nov; MarketIndex Evening Wrap, 24 Nov) |
| `ASX:ZIP` | Zip Co Ltd. | **+7.55%** | 8.4 AUD | 1,919,774 | $1.29B | none | Rose 7.55% to A$8.40 - the second full session on the post-consolidation basis, so the move is measured against 23 November's A$7.81 post-consolidation close and is a real move rather than an artefact; the 1-for-5 consolidation went ex on 23 November with the record date on 24 November (ASX Notice 1312.26.11, 24 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:4062` | IBIDEN CO., LTD. | **+14.98%** | 5372 JPY | 2,094,700 | $16.63B | OTC | Rose 14.98% to Y5,372 - buy orders piled up at the upper limit with no trades executed through the morning session; IBIDEN is a named Nvidia supplier and led the Nikkei's advance (Reuters via Business Recorder, 24 Nov; Aju Press, 24 Nov) |
| `TSE:6981` | Murata Manufacturing Co., Ltd. | **+14.89%** | 5400 JPY | 25,033,000 | $54.50B | ADR | Rose 14.89% to Y5,400 - a named Nvidia component supplier in the relief rally, its biggest percentage gain since late July (Reuters via Business Recorder, 24 Nov; Trading Economics, 24 Nov) |
| `TSE:3110` | Nitto Boseki Co., Ltd. | **+14.30%** | 2398.5 JPY | 5,303,000 | $2.47B | OTC | Rose 14.30% to Y2,398.5 - no company-specific release found for 24 November; it rose with the Japanese AI-hardware supplier complex after Nvidia's board reinstated Jensen Huang as CEO (RTTNews, 24 Nov) |
| `TSE:6525` | Kokusai Electric Corporation | **+14.29%** | 5597 JPY | 5,270,200 | $7.31B | none | Rose 14.29% to Y5,597 - a semiconductor-equipment name in the Japanese AI-hardware rally (RTTNews, 24 Nov) |
| `TSE:6324` | Harmonic Drive Systems Inc. | **+13.27%** | 4216 JPY | 1,842,200 | $2.25B | OTC | Rose 13.27% to Y4,216 - no company-specific release found for 24 November; it rose with the Japanese robotics and precision-machinery complex after Nvidia's CEO reinstatement (RTTNews, 24 Nov) |
| `TSE:6787` | Meiko Electronics Co., Ltd. | **+13.08%** | 8730 JPY | 2,380,000 | $2.55B | none | Rose 13.08% to Y8,730 - no company-specific release found for 24 November; it rose with the Japanese AI-hardware supplier complex (RTTNews, 24 Nov) |
| `TSE:6857` | Advantest Corp. | **+12.45%** | 27275 JPY | 24,019,000 | $106.37B | ADR | Rose 12.45% to Y27,275 - Nvidia's semiconductor test-equipment supplier, up almost 15% intraday; Advantest, Tokyo Electron and SoftBank Group together contributed about 1,300 points to the Nikkei (Reuters via Business Recorder, 24 Nov; Aju Press, 24 Nov) |
| `TSE:268A` | Rigaku Holdings Corporation | **+12.19%** | 1381 JPY | 3,405,200 | $1.75B | ADR | Rose 12.19% to Y1,381 - no company-specific release found for 24 November; it rose with the Japanese AI-hardware and materials complex (RTTNews, 24 Nov) |
| `TSE:6323` | Rorze Corporation | **+12.06%** | 3086 JPY | 2,909,900 | $3.05B | none | Rose 12.06% to Y3,086 - no company-specific release found for 24 November; a semiconductor cleaning-equipment name in the Japanese AI rally (RTTNews, 24 Nov) |
| `TSE:4004` | Resonac Holdings Corporation | **+11.55%** | 12265 JPY | 4,528,500 | $12.99B | OTC | Rose 11.55% to Y12,265 - a named member of the Japanese AI-hardware complex in the relief rally (RTTNews, 24 Nov; Trading Economics, 24 Nov) |
| `TSE:5801` | Furukawa Electric Co., Ltd. | **+11.54%** | 1807 JPY | 36,568,200 | $7.16B | ADR | Rose 11.54% to Y1,807 - a named Nvidia supplier in the relief rally (Reuters via Business Recorder, 24 Nov; Trading Economics, 24 Nov) |
| `TSE:6507` | Sinfonia Technology Co., Ltd. | **+11.48%** | 8060 JPY | 340,900 | $1.28B | none | Rose 11.48% to Y8,060 - no company-specific release found for 24 November; it rose with the Japanese AI-hardware complex (RTTNews, 24 Nov) |
| `TSE:3436` | SUMCO Corporation | **+11.07%** | 2031.5 JPY | 11,316,200 | $4.03B | OTC | Rose 11.07% to Y2,031.5 - a silicon-wafer supplier named in the Japanese AI rally (RTTNews, 24 Nov) |
| `TSE:8035` | Tokyo Electron Ltd. | **+7.67%** | 8946 JPY | 25,272,700 | $121.53B | ADR | Rose 7.67% to Y8,946 - the semiconductor-equipment heavyweight named in the relief rally (Trading Economics, 24 Nov; Aju Press, 24 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TPEX:5347` | Vanguard International Semiconductor Corp | **+10.00%** | 121 TWD | 4,489,467 | $6.29B | none | Rose 10.00% to NT$121 - a semiconductor-equipment name locked at its daily limit (UURL, 24 Nov) |
| `TWSE:2327` | Yageo Corporation | **+10.00%** | 341 TWD | 2,637,078 | $19.44B | none | Rose 10.00% to NT$341 - locked at its limit-up price; the passive-component bellwether closed at the limit together with Walsin Technology and Holy Stone Enterprise (Taiwan News, 24 Nov) |
| `TWSE:2345` | Accton Technology Corp. | **+10.00%** | 1485 TWD | 459,009 | $22.97B | none | Rose 10.00% to NT$1,485 - locked at its limit-up price; the network-equipment maker closed at the limit (Taiwan News, 24 Nov) |
| `TWSE:2408` | Nanya Technology Corporation | **+9.96%** | 309 TWD | 3,169,655 | $29.46B | none | Rose 9.96% to NT$309 - a memory name locked at its daily limit with the AI-supply-chain complex (UURL, 24 Nov) |
| `TWSE:3711` | ASE Technology Holding Co., Ltd. | **+9.96%** | 530 TWD | 6,654,669 | $64.80B | ADR | Rose 9.96% to NT$530 - the IC packaging and testing house closed at its daily limit (CNA via Focus Taiwan, 24 Nov) |
| `TWSE:2317` | Hon Hai Precision Industry Co., Ltd. | **+9.95%** | 226.5 TWD | 19,140,213 | $88.28B | ADR | Rose 9.95% to NT$226.5 - closed at its daily limit with the AI-supply-chain complex (CNA via Focus Taiwan, 24 Nov) |
| `TWSE:2344` | Winbond Electronics Corp. | **+9.95%** | 105 TWD | 4,660,026 | $13.73B | none | Rose 9.95% to NT$105 - a memory name locked at its daily limit with the AI-supply-chain complex (UURL, 24 Nov) |
| `TWSE:3189` | Kinsus Interconnect Technology Corp. | **+9.95%** | 514 TWD | 1,244,368 | $7.50B | none | Rose 9.95% to NT$514 - a PCB-substrate maker locked at its daily limit (UURL, 24 Nov) |
| `TWSE:3017` | Asia Vital Components Co., Ltd. | **+9.94%** | 2600 TWD | 327,848 | $28.28B | none | Rose 9.94% to NT$2,600 - a thermal-solutions name locked at its daily limit (UURL, 24 Nov) |
| `TWSE:2454` | MediaTek Inc | **+9.91%** | 4050 TWD | 1,291,792 | $179.21B | none | Rose 9.91% to NT$4,050 - the smartphone IC designer closed at its daily limit with the AI-supply-chain complex (CNA via Focus Taiwan, 24 Nov) |
| `TWSE:2383` | Elite Material Co., Ltd. | **+9.87%** | 3395 TWD | 132,755 | $33.71B | none | Rose 9.87% to NT$3,395 - a PCB-substrate maker locked at its daily limit (UURL, 24 Nov) |
| `TWSE:3037` | Unimicron Technology Corp. | **+9.86%** | 613 TWD | 1,143,329 | $27.38B | none | Rose 9.86% to NT$613 - a PCB-substrate maker locked at its daily limit (UURL, 24 Nov) |
| `TWSE:2337` | Macronix International Co., Ltd. | **+9.85%** | 68 TWD | 2,981,582 | $3.72B | none | Rose 9.85% to NT$68 - a memory name locked at its daily limit with the AI-supply-chain complex (UURL, 24 Nov) |
| `TWSE:2330` | Taiwan Semiconductor Manufacturing Co., Ltd. | **+9.85%** | 2230 TWD | 11,501,344 | $1602.95B | ADR | Rose 9.85% to NT$2,230 - hit its upper daily price limit almost immediately after the open and closed at the limit, contributing about 1,600 points of the index's record 3,310.46-point gain (CNA via Focus Taiwan, 24 Nov; Coinotag, 24 Nov) |
| `TWSE:2308` | Delta Electronics, Inc. | **+9.60%** | 1085 TWD | 1,064,016 | $78.30B | none | Rose 9.60% to NT$1,085 - closed at its daily limit with the AI-supply-chain complex (CNA via Focus Taiwan, 24 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:FM` | First Quantum Minerals Ltd. | **-10.35%** | 24.42 CAD | 4,127,030 | $15.86B | OTC | Fell 10.35% to C$24.42 - the company disclosed a fatality at its Kansanshi operation, where a contract employee died in an isolated area at a low-grade stockpile and operations in that area were temporarily suspended (GlobeNewswire, 24 Nov) |
| `TSX:CLS` | Celestica Inc. | **-8.40%** | 280.8 CAD | 736,958 | $26.98B | NYSE | Fell 8.40% to C$280.80 - an AI-hardware name that fell with the Canadian technology complex as the relief rally faded; Nvidia itself was down 8.12% in US trading on criticism of the board's reinstatement (Reuters, 24 Nov; MarketScreener, 24 Nov) |
| `TSX:CS` | Capstone Copper Corp. | **-7.95%** | 7.99 CAD | 4,014,528 | $4.64B | ADR | Fell 7.95% to C$7.99 - copper, with the materials sector down 2% on softer gold and expectations of higher-for-longer Fed rates (Reuters, 24 Nov) |
| `TSX:CFP` | Canfor Corporation | **+7.67%** | 14.88 CAD | 369,348 | $1.13B | OTC | Rose 7.67% to C$14.88 - no company-specific release found for 24 November; it rose with the softwood-lumber complex (Canfor also up, West Fraser +6.83%) against a materials sector that fell 2% (Reuters via MarketScreener, 24 Nov) |
| `TSX:ERO` | Ero Copper Corp. | **-7.48%** | 31.05 CAD | 945,589 | $2.45B | NYSE | Fell 7.48% to C$31.05 - copper, with weaker commodity prices weighing on the base-metals sector (Reuters, 24 Nov) |
| `TSX:HPS.A` | Hammond Power Solutions Inc. Class A | **-6.97%** | 177.78 CAD | 103,893 | $1.59B | OTC | Fell 6.97% to C$177.78 - no company-specific release found for 24 November; it fell with the Canadian technology and industrial complex (Reuters, 24 Nov) |
| `TSX:IVN` | Ivanhoe Mines Ltd. Class A | **-6.90%** | 6.07 CAD | 8,877,267 | $6.49B | OTC | Fell 6.90% to C$6.07 - copper, in the base-metals selloff (Reuters, 24 Nov) |
| `TSX:MAU` | Montage Gold Corp. | **-6.88%** | 12.86 CAD | 1,015,702 | $3.93B | OTC | Fell 6.88% to C$12.86 - gold, with softer gold prices and higher-for-longer Fed expectations weighing on the miners (Reuters, 24 Nov) |
| `TSX:WFG` | West Fraser Timber Co. Ltd. | **+6.83%** | 98.18 CAD | 379,991 | $5.02B | NYSE | Rose 6.83% to C$98.18 - no company-specific release found for 24 November; it rose with the softwood-lumber complex (Canfor also up 7.67%) against a materials sector that fell 2% (Reuters via MarketScreener, 24 Nov) |
| `TSX:HBM` | Hudbay Minerals Inc | **-6.65%** | 24 CAD | 3,004,728 | $7.97B | NYSE | Fell 6.65% to C$24.00 - copper and gold, in the materials-sector decline (Reuters, 24 Nov) |
| `TSX:EDR` | Endeavour Silver Corp. | **-6.24%** | 8.27 CAD | 911,901 | $1.82B | NYSE | Fell 6.24% to C$8.27 - a silver and gold miner, in the materials-sector selloff (Reuters, 24 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:AIXA` | AIXTRON SE | **-16.32%** | 26.81 EUR | 1,924,152 | $3.95B | OTC | Fell 16.32% to EUR26.81 - UBS cut the chip-equipment maker to sell and more than halved its price target, from EUR50 to EUR24, wiping out the prior session's gain (DOW JONES via finanzen.net, 24 Nov; dpa-AFX via ariva.de, 24 Nov) |
| `XETR:NDA` | Aurubis AG | **-14.97%** | 107.9 EUR | 653,042 | $6.07B | OTC | Fell 14.97% to EUR107.90 - a profit warning: the copper producer said the operating result for the current financial year will land about EUR430-530m below market expectations because of problems ramping up a new US plant, taking the stock to a twelve-month low (DOW JONES via finanzen.net, 24 Nov; dpa-AFX, 24 Nov) |
| `XETR:SZG` | Salzgitter AG | **-13.38%** | 40.4 EUR | 450,508 | $3.07B | ADR | Fell 13.38% to EUR40.40 - the steelmaker holds about a quarter of Aurubis and fell with the profit warning (DOW JONES via finanzen.net, 24 Nov; stock3.com, 24 Nov) |
| `XETR:JEN` | Jenoptik AG | **-9.71%** | 32.56 EUR | 117,390 | $2.26B | OTC | Fell 9.71% to EUR32.56 - no company-specific release found for 24 November; it fell with the German technology and photonics complex after the AI-hardware relief rally unwound (DOW JONES via finanzen.net, 24 Nov) |
| `XETR:IFX` | Infineon Technologies AG | **-9.68%** | 43.735 EUR | 5,793,999 | $69.08B | ADR | Fell 9.68% to EUR43.74 - the largest DAX loser; a chip name giving back the prior session's relief rally while Nvidia fell 8.12% in US trading on criticism of the board's reinstatement (DOW JONES via finanzen.net, 24 Nov; Reuters, 24 Nov) |
| `XETR:WAF` | Siltronic AG | **-8.42%** | 50.05 EUR | 115,115 | $1.98B | ADR | Fell 8.42% to EUR50.05 - a silicon-wafer supplier in the semiconductor give-back (tradegate, 24 Nov) |
| `XETR:SMHN` | SUSS MicroTec SE | **-8.35%** | 44.12 EUR | 135,541 | $1.01B | OTC | Fell 8.35% to EUR44.12 - an assembly-technology supplier in the semiconductor give-back (dpa-AFX, 24 Nov) |
| `XETR:ENR` | Siemens Energy AG | **-6.78%** | 117.88 EUR | 2,561,661 | $116.57B | ADR | Fell 6.78% to EUR117.88 - a power-infrastructure name, cited among the European decliners as the AI outlook was reassessed (Trading Economics, 24 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:CLARI` | Clariane SE | **+35.30%** | 4.5 EUR | 18,538,767 | $1.30B | none | Rose 35.30% to EUR4.50 - HLD Europe (via Ker Holding) and Credit Agricole Assurances (via Predica) announced a takeover project in concert, under which HLD would file a mandatory simplified public offer at EUR4.60 a share with no squeeze-out; the board welcomed the project preliminarily (ideal-investisseur, 24 Nov; Boursorama, 24 Nov) |
| `EURONEXT:SOI` | Soitec SA | **-9.97%** | 91.38 EUR | 565,389 | $3.98B | OTC | Fell 9.97% to EUR91.38 - a semiconductor-substrate supplier giving back the prior session's relief rally (BourseDirect, 24 Nov; Boursorama, 24 Nov) |
| `EURONEXT:SAN` | Sanofi SA | **+9.76%** | 93.58 EUR | 9,041,843 | $112.12B | ADR | Rose 9.76% to EUR93.58, the best CAC 40 performer, on agreeing to buy the US respiratory-disease specialist Insmed for about $41bn (EUR37.6bn) (AFP via Boursorama, 24 Nov; BourseDirect, 24 Nov) |
| `EURONEXT:EMEIS` | Emeis | **+8.08%** | 10.97 EUR | 429,072 | $1.80B | none | Rose 8.08% to EUR10.97 - a rebound after a prolonged decline in the French care-home sector, which Clariane's takeover proposal pulled up; Kepler Cheuvreux cut its target to EUR11 from EUR16 and kept a hold (ideal-investisseur, 24 Nov) |
| `EURONEXT:LR` | Legrand SA | **-5.57%** | 125.35 EUR | 670,548 | $38.08B | OTC | Fell 5.57% to EUR125.35 - an electrical-equipment supplier, with Schneider Electric down 4.13% (AFP via Boursorama, 24 Nov) |
| `EURONEXT:NEX` | Nexans SA | **-5.28%** | 118.3 EUR | 107,694 | $5.99B | OTC | Fell 5.28% to EUR118.30 - an electrical-equipment supplier; the only fresh company news was the appointment of Marie Ollier as Chief Human Resources and ESG Officer, which does not explain the move (AFP via Boursorama, 24 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:TPRO` | Technoprobe SpA | **-10.09%** | 18 EUR | 2,727,243 | $14.05B | ADR | Fell 10.09% to EUR18.00 - a chip-test-card maker; the Milan close had STMicroelectronics down 10.01% as the AI rally faded (Reuters via mlq.ai, 24 Nov) |
| `MIL:PRY` | Prysmian S.p.A. | **-8.04%** | 98.44 EUR | 1,622,319 | $35.13B | ADR | Fell 8.04% to EUR98.44 - a cable and power-infrastructure name, in the European industrials give-back (Reuters via mlq.ai, 24 Nov) |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `BME:TRE` | Tecnicas Reunidas SA | **-6.23%** | 28.32 EUR | 233,255 | $2.59B | none | Fell 6.23% to EUR28.32 - no company-specific release found for 24 November (the nine-month results were published on 13 November and the RWE Germany plant award was announced on 23 November); it fell with the European industrials complex as the AI trade unwound (Reuters, 24 Nov) |

### eu-nl

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:BESI` | BE Semiconductor Industries N.V. | **-8.79%** | 142.2 EUR | 621,581 | $13.80B | ADR | Fell 8.79% to EUR142.20 - a chip-assembly-equipment maker; the five European chip stocks tracked rose 6.6-9.3% on Monday and gave it back on Tuesday as the AI-hardware trade unwound (FourWeekMBA, 24 Nov; Reuters, 24 Nov) |
| `EURONEXT:ASM` | ASM International N.V. | **-7.97%** | 637.4 EUR | 200,544 | $36.95B | ADR | Fell 7.97% to EUR637.40 - the deposit-and-etch equipment maker gave back its Monday gain, in the European chip give-back (Reuters, 24 Nov) |
| `EURONEXT:ASML` | ASML Holding NV | **-5.58%** | 1201.2 EUR | 955,152 | $532.76B | ADR | Fell 5.58% to EUR1,201.20 - the lithography benchmark gave back its Monday gain as the relief rally faded in Europe (Reuters, 24 Nov; MarketScreener midday briefing, 24 Nov) |

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | **-12.34%** | 96.6 EUR | 190,797 | $4.69B | OTC | Fell 12.34% to EUR96.60 - the Vienna exchange's own tick data prints 96.60, -13.60 (-12.34%) at 17:35; the advanced-substrate and assembly name gave back more than its +13.03% Monday surge as European chip stocks fell on new US export curbs (Wiener Borse, 24 Nov; Yahoo Finance, 24 Nov) |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:METSO` | Metso Corporation | **-6.69%** | 14.22 EUR | 2,262,443 | $13.83B | none | Fell 6.69% to EUR14.22 - the biggest OMX Helsinki 25 loser, in the industrials-led decline after its +4.53% Monday gain (Investing.com, 24 Nov) |
| `OMXHEX:OUT1V` | Outokumpu Oyj | **-5.20%** | 3.208 EUR | 2,131,630 | $1.74B | ADR | Fell 5.20% to EUR3.208 - the stainless-steel maker fell to a 52-week low (Investing.com, 24 Nov) |
| `OMXHEX:NOKIA` | Nokia Oyj | **-5.07%** | 6.662 EUR | 11,733,283 | $43.54B | ADR | Fell 5.07% to EUR6.66 - the telecom name led the Helsinki decliners after its +8.60% Monday rally (Investing.com, 24 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:GMAB` | Genmab A/S | **+6.72%** | 3809 DKK | 228,793 | $31.37B | ADR | Rose 6.72% to DKK3,809 - Jefferies raised its price target to DKK4,100 from DKK3,200 and reiterated buy (Finwire via MarketScreener, 24 Nov) |

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) - published, because a -39% or a +200% move is not noise. Their tickers are printed **without** the backtick format used for CSV rows precisely because they are not CSV rows. **Most of them are sub-$0.05 micro-caps whose percentage carries little information** - their prices, not their percentages, are the signal.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| ASX:1TT | Thrive Tribe Technologies Limited | **+200.00%** | 0.003 | 53,507,730 | $114.6M | below the $300.0M Australia cap floor |
| ASX:HE8 | Helios Energy Ltd | **+100.00%** | 0.002 | 666,037 | $5.2M | below the $300.0M Australia cap floor |
| ASX:TOU | Tlou Energy Ltd | **+100.00%** | 0.002 | 186,242 | $862,445 | below the $300.0M Australia cap floor |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| TSE:6573 | CRAVIA Inc. | **+47.06%** | 25 | 13,750,300 | $8.4M | below the $300.0M Japan cap floor |
| TSE:3237 | Intrance Co., Ltd. | **+42.31%** | 74 | 16,935,700 | $15.2M | below the $300.0M Japan cap floor |
| TSE:5255 | Monstarlab Inc. | **+36.36%** | 60 | 10,592,900 | $17.9M | below the $300.0M Japan cap floor |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| TPEX:6820 | Acon Optics Communications, Inc. | **+59.22%** | 285 | 319,467 | $117.8M | below the $200.0M Taiwan cap floor |
| TPEX:7960 | Yea Shin Technology Co., Ltd. | **+46.74%** | 135 | 166,234 | $143.8M | below the $200.0M Taiwan cap floor |
| TPEX:3585 | Advance Materials Corporation | **+37.43%** | 52.5 | 2,471,489 | $123.1M | below the $200.0M Taiwan cap floor |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| TSXV:SAF.H | Seasif Exploration Inc. | **+200.00%** | 0.015 | 948,700 | $511,159 | below the $200.0M Canada cap floor |
| TSXV:GVR | Grosvenor Resource Corporation | **+137.50%** | 0.095 | 101,500 | $932,525 | below the $200.0M Canada cap floor |
| TSXV:NNX | Nickel North Exploration Corp. | **+66.67%** | 0.025 | 566,455 | $2.5M | below the $200.0M Canada cap floor |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| XETR:DMRE | DEMIRE Deutsche Mittelstand Real Estate AG | **-10.11%** | 0.169 | 214,028 | $21.7M | below the $300.0M Germany cap floor |
| XETR:LPK | LPKF Laser & Electronics SE | **-6.82%** | 7.1 | 432,101 | $204.6M | below the $300.0M Germany cap floor |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| EURONEXT:ALNEV | Neovacs SA | **-39.43%** | 0.051 | 2,573,257 | $168,156 | below the $100.0M France cap floor |
| EURONEXT:ALREE | REED | **-28.57%** | 0.002 | 9,077,682 | $5.5M | below the $100.0M France cap floor |
| EURONEXT:POXEL | Poxel SA | **+18.05%** | 0.1334 | 2,639,094 | $6.7M | below the $100.0M France cap floor |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| MIL:ENY | Energy SpA | **-9.14%** | 0.308 | 243,500 | $21.5M | below the $100.0M Italy cap floor |
| MIL:AEDES | Aedes Societa Anonima Ligure per Imprese e Costruzioni per azioni | **+8.97%** | 0.85 | 255,866 | $10.9M | below the $100.0M Italy cap floor |
| MIL:DIT | DESTINATION ITALIA S.P.A. | **-8.26%** | 0.2 | 120,000 | $5.0M | below the $100.0M Italy cap floor |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| BME:PVA | Pescanova, S.A. | **-13.64%** | 0.19 | 1,545,040 | $6.9M | below the $100.0M Spain cap floor |
| BME:NYE | Nyesa Valores Corporacion, S.A. | **-11.11%** | 0.0024 | 113,662,050 | $15.6M | below the $100.0M Spain cap floor |
| BME:SAI | Substrate Artificial Intelligence SA | **+6.79%** | 0.0283 | 11,674,417 | $24.7M | below the $100.0M Spain cap floor |

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| EURONEXT:NYXH | Nyxoah SA | **-5.47%** | 0.708 | 122,654 | $83.6M | below the $100.0M Belgium cap floor |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| OMXHEX:WETTERI | Wetteri Oyj | **-19.57%** | 0.113 | 447,172 | $24.9M | below the $100.0M Finland cap floor |
| OMXHEX:BRETEC | Bioretec Ltd. | **-8.08%** | 0.0182 | 4,468,552 | $29.1M | below the $100.0M Finland cap floor |
| OMXHEX:EEZY | Eezy Oyj | **-6.33%** | 0.1405 | 497,513 | $20.6M | below the $100.0M Finland cap floor |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| OMXCOP:STENO | StenoCare A/S | **+7.27%** | 0.62 | 120,195 | $3.7M | below the $100.0M Denmark cap floor |

## No catalyst

Names that moved with no sourced driver - no company release, no filing, no analyst action, and no sourced sector or macro move behind them - kept separate so they do not dilute the mover table.

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) |
|---|---|---|---|---|---|
| `TSE:6976` | Taiyo Yuden Co., Ltd. | **+11.10%** | 6874 JPY | 22,045,300 | $5.17B |
| `TSE:6368` | Organo Corp. | **+10.81%** | 1656 JPY | 2,631,800 | $2.17B |
| `TSE:6278` | Union Tool Co. | **+10.05%** | 10510 JPY | 287,800 | $1.17B |
| `TSE:285A` | Kioxia Holdings Corporation | **+9.95%** | 8034 JPY | 146,697,700 | $75.64B |
| `TSE:6920` | Lasertec Corp. | **+9.75%** | 33200 JPY | 4,631,400 | $17.04B |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) |
|---|---|---|---|---|---|
| `TPEX:7861` | Bellwether Electronic Corp. | **+32.78%** | 802 TWD | 286,245 | $1.19B |
| `TPEX:6696` | Lin BioScience, Inc. | **+10.13%** | 130.5 TWD | 11,773,002 | $3.01B |
| `TPEX:4979` | Luxnet Corporation | **+10.00%** | 280.5 TWD | 400,366 | $1.10B |
| `TPEX:6548` | Chang Wah Technology Co., Ltd. | **+10.00%** | 60.5 TWD | 442,653 | $1.58B |
| `TPEX:8299` | Phison Electronics Corp. | **+10.00%** | 1595 TWD | 494,999 | $9.76B |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) |
|---|---|---|---|---|---|
| `TSX:SXGC` | Southern Cross Gold Consolidated Ltd. | **-6.41%** | 6.42 CAD | 506,966 | $1.29B |
| `TSX:SEA` | Seabridge Gold Inc | **-5.97%** | 25.99 CAD | 153,574 | $2.09B |
| `TSX:SVM` | Silvercorp Metals Inc. | **-5.71%** | 9.42 CAD | 1,079,129 | $1.55B |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) |
|---|---|---|---|---|---|
| `XETR:NDX1` | Nordex SE | **-5.46%** | 36.04 EUR | 392,231 | $9.90B |
| `XETR:1SXP` | SCHOTT Pharma AG & Co. KGaA | **-5.39%** | 21.05 EUR | 135,709 | $3.67B |
| `XETR:SAX` | Stroeer SE & Co. KGaA | **+5.18%** | 38.6 EUR | 111,272 | $2.22B |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) |
|---|---|---|---|---|---|
| `OMXHEX:IQMX` | IQM Quantum Computers Oyj Class A | **-6.73%** | 5.825 EUR | 215,301 | $1.22B |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) |
|---|---|---|---|---|---|
| `OMXCOP:FLS` | FLSmidth & Co. A/S | **-5.95%** | 458 DKK | 228,740 | $4.06B |
| `OMXCOP:DEMANT` | Demant A/S | **-5.08%** | 332.6 DKK | 612,945 | $10.53B |

## Method, source health & caveats

### Method

- **Universe.** The TradingView per-country scanner for each of the 16 boards, pulled with `symbols.query.types = ["stock"]` and the endpoint's `filter` on the scanner's **`country` column - the issuer's own country, not the venue's**. That is what makes a region file hold that country's own issuers; a venue pull would file Apple as a German and a Japanese name. Every pull was set-asserted: the pages were disjoint and their union equalled `totalCount` (au 1,548; jp 3,890; tw 2,345; ca 4,286; eu-de 4,303; eu-fr 543; eu-it 377; eu-es 230; eu-nl 78; eu-be 101; eu-at 65; eu-pt 30; eu-ie 19; eu-fi 189; eu-dk 133; eu-gr 127 - all complete). The America scanner (types `stock` + `dr`, 13,596 rows, set-asserted the same way) is the source for `us_listing` and for the cross-venue cap check.
- **Floors.** Per-region USD floors applied **after** conversion: au $300M + volume >= 100,000; jp $300M; tw $200M; ca $200M; eu-de $300M + volume >= 50,000; eu-fr/it/es/nl/be/at $100M; eu-ie $200M; eu-fi/dk $100M; eu-pt/gr $50M. **The CSV carries 18 columns** - the same 18-column schema as the previous session, so no positional break for a consumer reading the archive.
- **FX.** `usd_cap = market_cap_basic / FX_per_USD[listing_currency]`, i.e. a **division**, because every FX table here is *local currency per 1 USD*. Provider: **frankfurter.app (base USD), rate date 2026-11-24**, plus **open.er-api.com/v6/latest/USD** for TWD (32.841226 per USD), which Frankfurter does not publish. The direction was settled by share-count reconciliation, not by a spot check: `market_cap_basic / close` returns 1.14bn shares for SAP, 11.85bn for Toyota, 56.2m for Genmab, 404.6m for ASML - the issuers' real share counts.
- **Cap carrier.** The cap belongs to the issuer and is resolved to the issuer's **primary (common) line**, converted **once** on the primary's currency, and carried to every line of that issuer; `cap_source_symbol` records which line it came from. The primary is the common line whose own `market_cap_basic` carries the source's per-line cap (a fractional part), with the most liquid common line as the tie-break. A group with no common line has no primary and is dropped as `issuer_unresolved`; a carry that fails the same-issuer assertion drops the group as `cap_issuer_mismatch`.
- **Venue collapse.** The issuer's **primary venue's** line wins, not the busiest venue's, and a line whose implied prior close (`close / (1 + change/100)`) misses the prior session's published close by more than 5% is dropped as a stale print and counted in `off_official_rows`. The lookup is per symbol including its share-class suffix, so a Canadian preferred is not compared with its common line.
- **Venue-official price.** Where a venue's own print was obtained it is published; where the third-party quote stands, the row carries an empty `price_conflict` cell. The one venue print checked this session, the Vienna Stock Exchange's own tick data for AT&S, prints **96.60, -13.60 (-12.34%) at 17:35** - identical to the scanner's settle, so the row carries no conflict.
- **Cross-venue cap check.** The ADR/OTC line is a second reading of the same company-level cap and must agree within 10%. **1,411 comparisons ran; 68 disagreed by more than 10%**, but a conservative same-issuer test (distinctive issuer tokens of the US line must be a subset of the local line's, at least two shared) removes the matcher's false pairs - the well-known ones being APA Group paired with APA Corporation, Rio Tinto with Perpetuals.com, and Endeavour Group with Endeavour Silver. **21 genuine comparisons survive**, and almost all of them are the ADR **ratio** rather than a data error: an ADR line carries a different number of underlying shares, so its converted cap differs by design. The two outliers are disclosed below. Every published cap therefore has a second reading behind it, and the local line's cap is what is published.
- **Carry-over.** A row whose close equals the prior session's published close **exactly** (string equality on the written value, never a tolerance) while its volume is zero or its change field is a non-zero leftover is a carry-over; it stays in the CSV with the source's own field, is listed in `_carryover.json` with its `last_trade_date` walked backwards, and is excluded from every mover list.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView per-country scanner | `scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan`, `filter=[{country equal <issuer country>}]`, `types=[stock]` | ok | 16/16 pulls complete; every pull set-asserted (disjoint pages, union == totalCount) |
| TradingView America scanner | `scanner.tradingview.com/america/scan`, `types=[stock, dr]` | ok | 13,596 rows, set-asserted; the source for `us_listing` and the cross-venue cap check |
| TradingView index scanner | `scanner.tradingview.com/global/scan`, `tickers=[SP:XJO, TVC:NI225, TSE:TOPIX, TWSE:IX0001, TSX:TSX, XETR:DAX, EURONEXT:PX1, FTSE:FTSEMIB, BME:IBC, EURONEXT:AEX, EURONEXT:BEL20, VIE:ATX, EURONEXT:PSI20, EURONEXT:ISEQ, OMXHEX:OMXH25, OMXCOP:OMXC20, STOXX:SXXP]` | ok | 16 region index levels plus the STOXX 600 context row |
| Yahoo chart API | `query2.finance.yahoo.com/v8/finance/chart/{^AXJO,^N225,^TWII,^GSPTSE,^GDAXI,^FCHI,FTSEMIB.MI,^IBEX,^AEX,^BFX,^ATX,PSI20.LS,^ISEQ,^OMXH25,^OMXC25}` | ok (partial) | the daily bars for `^N225` and `^TWII` still lag (last settled bar 2026-11-20 and 2026-11-23); the live quote confirms both sessions, and the TradingView scanner's settled index levels were used instead |
| Frankfurter FX | `api.frankfurter.app/latest?base=USD` | ok | rate date 2026-11-24; no TWD quote, so TWD came from open.er-api.com |
| open.er-api FX | `open.er-api.com/v6/latest/USD` | ok | used only for TWD (32.841226 per USD) |
| Yahoo daily bars (session probe) | `query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=2y&interval=1d` for all 16 regions | ok | every region reports a session dated 2026-11-24 - **no market was closed** |
| Euronext Athens index page / greek press | `euro2day.gr`, `xrimatistirio.com` close tables | ok | ATHEX General 2,524.88, -1.46% - the venue's own print (no Yahoo symbol, no TradingView venue index) |
| Wiener Borse tick data | `wienerborse.at` ATS quote page | ok | AT&S 96.60, -13.60 (-12.34%) at 17:35 - **identical to the scanner's settle**, so no price conflict |
| TMX / GlobeNewswire / exchange releases | per-name company news via web_search | ok | catalysts for every name published in `## Top movers` |
| MCP finance tools | - | not registered | the `mcp__*` finance tools are absent from this runtime by design; the MCP-over-HTTP bridge was not needed because the scanner and press sources answered |

### Caveats

- **The unit convention.** `market_cap` is **USD**; `open`/`high`/`low`/`close` are in the **listing currency** named in the `currency` column. A cap and a price in one row are therefore in two different currencies, by contract.
- **Taiwan's limit prices are not calculated moves.** 621 Taiwanese stocks closed limit-up (335 main-board, 286 OTC) and 30 of the 33 stocks priced above NT$1,000 reached their daily limit; the +10.00% prints in the TAIEX tables are **the ceiling of the band**, not a valuation. The TAIEX's +8.99% is a record point gain partly produced by names that simply could not go higher.
- **The limit-band class is still live on one published row.** `TPEX:7861` (Bellwether Electronic) prints **+32.78%** - outside Taiwan's +/-10% band - while every other Taiwan name over 10% is at the band exactly. Its implied prior (NT$603.9) reconciles exactly with its 23 November close, so it is not a stale print, but no price-basis explanation was found and no company-specific release was located. It is kept out of every published table and disclosed here.
- **The contract-adjustment class has cleared for Zip, but not by itself.** `ASX:ZIP` went ex on a **1-for-5 share consolidation on 23 November** (ASX Notice 1312.26.11). On 23 November the source measured its change on the pre-consolidation basis and published +363.50% against an inflated $6.97bn cap - the artefact this archive flagged on that session. **Today's +7.55% is measured against 23 November's post-consolidation close of A$7.81 and the cap is back to $1.29bn, so today's row is on a consistent basis and is publishable as a real move.** Any consumer joining the two files must not treat 23 November's ZIP change or cap as a market fact.
- **Europe's chip leg has its own driver, and it is not the same one as Asia's.** The US Commerce Department added **Megaspeed International and six related entities** to the Entity List on 23 November (Al Jazeera, CNBC, Reuters, 24 Nov), and **Nvidia fell 8.12% in US trading** on criticism of the board's reinstatement while Huang was back. European chip and equipment names fell on that, not on a Chinese-demand story.
- **The US-listing matcher can pair two different companies that share a name.** The `us_listing` column comes from the archive's shipped issuer-name matcher, which is prefix-based: it pairs `ASX:APA` (APA Group) with `NASDAQ:APA` (APA Corporation) and `ASX:PPT` (Perpetual) with `NASDAQ:PDC` (Perpetuals.com). A stricter country-plus-token matcher was built and measured for this run: it fixes those pairs but downgrades **true** matches such as Rio Tinto's ADR from `ADR` to `OTC`, so it was **not** adopted and the shipped matcher stands. The false pairs are disclosed here rather than silently published; the cross-venue cap check uses the stricter test instead, because a false pair there would manufacture a cap finding.
- **A cross-venue cap disagreement is usually the ADR ratio, not an error.** Of the 21 genuine same-issuer comparisons, the widest gaps are `TSXV:MOON` (local $0.24bn vs US $0.21bn, -13.7%), `XETR:AIXA` (Aixtron, -15.6%), `XETR:NDA` (Aurubis, -14.7%), `TSX:FM` (First Quantum, -10.1%) and `VIE:ATS` (AT&S, -11.9%). Two comparisons are large enough to flag rather than explain: `TSE:9716` (local $0.86bn against a US line at $25.24bn) and `TPEX:5425` (local $0.47bn against `NYSE:TSM` at $1,603.8bn) - both look like name-key collisions rather than issuer matches, and neither is published as a cap finding.
- **Carry-over rows.** 68 rows across the 16 boards did not trade on 24 November and keep an earlier session's close and change field. They stay in the CSVs with the source's own field, are listed in `_carryover.json` with the date each one last traded, and are excluded from every movers list.
- **Two third-party closes disagree with the source and no official print was obtained.** Investing.com's close table prints the **OMX Helsinki 25 at -1.03%** against the scanner's -0.97%, and Outokumpu at EUR3.23 against the scanner's EUR3.208. The scanner's settle is published (it is the source of record) and the disagreement is disclosed rather than reconciled.
- **Greece's index has no machine-readable vendor feed.** The ATHEX General is published from the venue's own print via the Greek press (euro2day, 17:44) because the ATHEX has neither a Yahoo index symbol nor a TradingView venue index; the 83 Greek rows themselves come from the scanner like every other board.
- **The universe rule drops issuers filed under a country this skill does not cover.** STMicroelectronics - the biggest single European AI mover on 23 November at +8.96% - is filed by the vendor as **Switzerland**, so its Milan and Paris lines fall outside all 16 boards and it is absent from the artifact entirely. It returned **-10.22%** on 24 November (Boursorama, 24 Nov), and a reader looking for it here will not find it.
- **No region was closed.** The session probe reports a session dated 2026-11-24 for all 16 boards, and the Japan pull was verified fresh against the 20 November published file - 1,322 of 1,347 Japanese rows differ from it, so it is 24 November's session and not a repeat of the last one.

### Sector rotation

Mean and median `change_pct` per sector over the liquid subset (volume >= 100,000), across all 16 boards:

| Sector | Names | Mean | Median |
|---|---|---|---|
| Electronic Technology | 375 | +7.11% | +9.65% |
| Producer Manufacturing | 303 | +4.35% | +3.78% |
| Health Services | 19 | +3.75% | +1.52% |
| Process Industries | 197 | +3.34% | +2.25% |
| Consumer Durables | 122 | +2.94% | +1.86% |
| Health Technology | 125 | +2.46% | +1.68% |
| Distribution Services | 96 | +1.88% | +1.28% |
| Technology Services | 135 | +1.88% | +1.41% |
| Finance | 365 | +1.76% | +1.44% |
| Commercial Services | 95 | +1.73% | +1.01% |
| Communications | 35 | +1.71% | +1.02% |
| Industrial Services | 133 | +1.70% | +1.55% |

The rotation is a clean two-way split on one theme: **semiconductor and electronics supply chains are the best sector in Asia and the worst in Europe**, which is what a single global AI-supply-chain trade repriced on opposite sides of the world looks like. The cross-market spread - Japanese and Taiwanese suppliers up double digits against European equipment makers down 6-16% - is the day's real story, and it is the reason the movers tables are not one list.

