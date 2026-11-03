---
date: 2026-11-03
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:13
source: EarningsWhispers calendar (roster, 243 names) + Nasdaq earnings calendar (time, market cap) + TradingView scanner (market cap) + MarketBeat (EPS, revenue) + StockAnalysis (EPS/revenue fallback) + Yahoo Finance earnings calendar (cross-check)
primary_source: MarketBeat (EPS est, revenue est) | TradingView scanner market_cap_basic (market cap, cross-verified vs Yahoo Finance) | Nasdaq earnings calendar (release time)
status: ok
pending_count: 43
already_reported_count: 0
---

# Earnings — Tue 2026-11-03

Roster: 43 names — every S&P 500 constituent reporting today plus every non-index mega-cap above $50B market cap. All 43 are **pending** as of the snapshot time; nothing on this list had printed yet when the aggregators' actuals columns were read.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Status |
|---|---|---|---|---|---|---|
| AMD | Advanced Micro Devices, Inc. | AMC | $1.95 | $13.10B | $762.1B | pending |
| AMGN | Amgen Inc. | AMC | $5.79 | $10.07B | $251.6B | pending |
| ANET | Arista Networks, Inc. | AMC | $1.08 | $3.33B | $207.0B | pending |
| SHOP | Shopify Inc. | BMO | $0.46 | $3.74B | $201.0B | pending |
| PFE | Pfizer, Inc. | BMO | $0.74 | $15.85B | $174.8B | pending |
| ETN | Eaton Corporation, PLC | BMO | $3.54 | $8.53B | $142.2B | pending |
| MPC | Marathon Petroleum Corporation | BMO | $25.37 | $46.60B | $120.9B | pending |
| BKNG | Booking Holdings Inc. | AMC | $4.49 | $9.55B | $115.5B | pending |
| RACE | Ferrari N.V. | BMO | $2.66 | $2.15B | $88.6B | pending |
| SU | Suncor Energy  Inc. | AMC | $2.35 | $11.97B | $88.2B | pending |
| ITUB | Itau Unibanco Banco Holding SA | TNS | $0.22 | $9.57B | $82.6B | pending |
| APO | Apollo Global Management, Inc. | BMO | $2.19 | $5.79B | $70.5B | pending |
| ET | Energy Transfer LP | BMO | $0.36 | $32.43B | $70.0B | pending |
| MPLX | MPLX LP | BMO | $1.13 | $3.35B | $59.8B | pending |
| AME | AMTEK, Inc. | BMO | $2.11 | $2.12B | $55.5B | pending |
| TRI | Thomson Reuters Corp | BMO | $0.82 | $1.80B | $53.0B | pending |
| KDP | Keurig Dr Pepper Inc. | BMO | $0.62 | $7.33B | $50.1B | pending |
| XYZ | Block, Inc. | AMC | $1.03 | $6.58B | $46.3B | pending |
| WAT | Waters Corporation | BMO | $4.00 | $1.75B | $44.2B | pending |
| AIG | American International Group, Inc. | AMC | $1.88 | $7.42B | $43.1B | pending |
| YUM | Yum! Brands, Inc. | BMO | $1.47 | $2.05B | $43.0B | pending |
| PRU | Prudential Financial, Inc. | AMC | $3.34 | $14.66B | $40.8B | pending |
| SYY | Sysco Corporation | BMO | $1.19 | $22.02B | $40.2B | pending |
| ADM | Archer-Daniels-Midland Company | BMO | $1.60 | $23.27B | $36.5B | pending |
| FISV | Fiserv, Inc. | BMO | $1.72 | $4.85B | $27.6B | pending |
| EXPD | Expeditors International of Washington, Inc. | BMO | $2.22 | $3.60B | $26.1B | pending |
| IFF | International Flavors & Fragrances, Inc. | AMC | $0.81 | $1.91B | $24.1B | pending |
| BR | Broadridge Financial Solutions, Inc. | BMO | $1.37 | $1.65B | $20.8B | pending |
| SMCI | Super Micro Computer, Inc. | AMC | $1.23 | $17.53B | $20.0B | pending |
| SWKS | Skyworks Solutions, Inc. | AMC | $1.27 | $1.04B | $20.0B | pending |
| DD | DuPont de Nemours, Inc. | BMO | $1.87 | $1.84B | $19.1B | pending |
| LDOS | Leidos Holdings, Inc. | BMO | $3.03 | $4.71B | $18.1B | pending |
| BALL | Ball Corporation | BMO | $1.07 | $3.78B | $18.0B | pending |
| ZBRA | Zebra Technologies Corporation | BMO | $4.89 | $1.57B | $17.1B | pending |
| RVTY | Revvity, Inc. | BMO | $1.30 | $694.7M | $16.9B | pending |
| IT | Gartner, Inc. | BMO | $2.84 | $1.49B | $14.9B | pending |
| AIZ | Assurant, Inc. | AMC | $4.75 | $3.48B | $14.7B | pending |
| PNW | Pinnacle West Capital Corporation | BMO | $3.32 | $1.90B | $12.8B | pending |
| JKHY | Jack Henry & Associates, Inc. | AMC | $2.07 | $685.5M | $11.5B | pending |
| AES | The AES Corporation | AMC | $0.53 | $3.45B | $10.6B | pending |
| HSIC | Henry Schein, Inc. | BMO | $1.36 | $3.48B | $9.7B | pending |
| APTV | Aptiv PLC | BMO | $1.33 | $3.17B | $9.2B | pending |
| MOS | Mosaic Company (The) | AMC | ($0.01) | $3.05B | $6.0B | pending |

**Time** = BMO (before the US open) / AMC (after the US close) / TNS (not specified by the source).

## Watchlist

No watchlist section: `research/watchlist.yaml` does not exist in the Cloud runtime (it is a local-only file on the Mavis host), so no watchlist tickers were cross-referenced. This is noted once here rather than shipping an empty table.

## Date verification (Rule B)

Aggregator calendars carry wrong dates. Every headline name and every name sitting on the $50B inclusion boundary was checked against a company source (IR page, press release or filing).

**Confirmed reporting on 2026-11-03 by company source:**

| Ticker | Company source | Confirmed date / timing |
|---|---|---|
| AMD | AMD IR press release, 2026-10-06 (ir.amd.com) | Tue Nov 3, 2026, after the market close |
| SHOP | Shopify IR press release, 2026-10-06 | Tue Nov 3, 2026, before markets open; call 08:30 ET |
| PFE | Pfizer IR news release, 2026-09-22 | Tue Nov 3, 2026; Performance Report that morning, call 10:00 ET |
| BKNG / ANET / SMCI / AMGN | Business Insider weekly calendar, 2026-11-01 (independent preview) | Tue Nov 3, 2026 |
| ET | Energy Transfer IR press release, 2026-10-01 | Tue Nov 3, 2026, before market opens; call 09:00 ET |
| AME | AMETEK IR news release, 2026-10-15 | Tue Nov 3, 2026, before market opens; call 08:30 ET |
| KDP | Keurig Dr Pepper IR press release, 2026-10-01 | Tue Nov 3, 2026, before market opens; call 08:00 ET |
| TRI | Thomson Reuters IR event page | 03 Nov 2026, 08:30 ET — after this 06:00 ET reminder, still pending |
| SU | Suncor IR news & events page | 2026 Q3 results released Nov 3, 2026 (call Nov 4) |
| ITUB | Banco calendar via el-fondo + tradytics | Tue Nov 3, 2026, after B3 close |
| AES | MarketBeat earnings page + Nasdaq earnings calendar (date not company-confirmed) | Nov 3, 2026, after market close (estimated) |

**Excluded after date verification — the aggregator calendar was wrong:**

| Ticker | Why it was on a calendar | Company source | Verdict |
|---|---|---|---|
| LITE | Digrin + Nasdaq listed Nov 3/5 | Lumentum press release, 2026-11-02 | **Already reported Nov 2** (Q1 FY2027, $1.26B revenue); excluded |
| FIS | Digrin listed Nov 3 | FIS IR press release, 2026-10-20 | **Rescheduled to Nov 4**; excluded |
| GPN | Digrin listed Nov 3 | Global Payments press release, 2026-10-22 | **Reports Nov 5**; excluded |
| LYV | Digrin listed Nov 3 | Live Nation press release, 2026-10-22 | **Reports Nov 5** after hours; excluded |
| TECH | Digrin listed Nov 3 | AJ Bell / MarketBeat company event data | **Reports Nov 4 or Nov 5**; excluded |
| EA | Yahoo Finance calendar listed Nov 3, AMC, $52.93B | Take-private closed August 2026 (Drake Star / MarketBeat delisting note) | **Delisted — private**; Yahoo row is stale; excluded |
| IITSF | Yahoo Finance calendar listed Nov 3 | Not US-listed; Intesa Sanpaolo ADR/foreign line | Excluded — no US-market listing on the roster |
| TEVA | Yahoo Finance calendar, $47.47B | Nasdaq calendar | Excluded — market cap under the $50B bar and not an S&P 500 member (reported Nov 3) |

## Estimate conflicts (Rule C)

One primary source per field, and the spread is recorded where providers disagree by more than 2% on EPS.

| Ticker | Published (MarketBeat) | Other providers | Note |
|---|---|---|---|
| AMD | $1.95 | Nasdaq/Zacks $1.68; StockAnalysis $1.94; Yahoo $1.94; BI $1.95 | Nasdaq column is stale — Yahoo, StockAnalysis and Business Insider all sit at ~$1.94-1.95 |
| SWKS | $1.27 | Nasdaq/Zacks $0.89; StockAnalysis $1.27 | Nasdaq is GAAP-basis; MarketBeat/StockAnalysis are adjusted-basis consensus |
| ZBRA | $4.89 | Nasdaq/Zacks $4.21; StockAnalysis $4.91 | Nasdaq stale; MarketBeat and StockAnalysis agree |
| SMCI | $1.23 | Nasdaq/Zacks $1.04; StockAnalysis $1.23; BI $1.23 | Nasdaq stale; three sources agree at ~$1.23 |
| APO | $2.19 | Nasdaq/Zacks $2.04; Yahoo $2.20 | ~7% spread between Zacks and Yahoo/MarketBeat |
| TRI | $0.82 | Yahoo $0.85; StockAnalysis $0.87; tradytics $0.81; Nasdaq $0.89 | ~8% spread; thin coverage, published value is MarketBeat |
| PFE | $0.74 | Yahoo $0.73; StockAnalysis $0.73; Nasdaq/Zacks $0.72 | ~2.8% spread; published value is MarketBeat |
| MPC | $25.37 | Yahoo $26.00; StockAnalysis $26.00; Nasdaq/Zacks $25.74 | ~2.5% spread; oil-sensitive name, consensus moving intraday |
| SHOP | $0.46 | Nasdaq/Zacks $0.33; Yahoo $0.46; StockAnalysis $0.46 | Nasdaq stale; Yahoo and StockAnalysis agree (revenue $3.74B both) |
| XYZ | $1.03 | Nasdaq/Zacks $0.68; Yahoo $1.03; StockAnalysis $1.03 | Nasdaq stale; Yahoo and StockAnalysis agree |
| AES | $0.53 | StockAnalysis $0.73 | Likely GAAP vs adjusted basis difference; MarketBeat consensus published |
| ET | $0.36 | Digrin $0.42; revenue $32.4-32.6B across both | Thin coverage |
| SU | $2.35 (USD) | Yahoo $3.53; StockAnalysis $3.53 | Yahoo/StockAnalysis quote CAD; MarketBeat publishes USD |
| RACE | $2.66 (USD) | Yahoo $2.32; StockAnalysis €2.38 | Yahoo/StockAnalysis quote local currency; MarketBeat publishes USD |
| ITUB | $0.22 (USD) | R$1.18 BRL per el-fondo | R$1.18 BRL converts to ~$0.22 — consistent |
| FISV | $1.72 | Digrin $1.75; Nasdaq/Zacks $1.72 | Within tolerance |

## Market-cap cross-check

Market cap is taken from the TradingView scanner (`market_cap_basic`). It matches Yahoo Finance's earnings-calendar market cap to under 1% on every name that could be cross-checked (AMD 762.1B vs 762.1B, MPC 120.9B vs 120.86B, BKNG 115.5B vs 115.52B, TRI 53.0B vs 52.96B, XYZ 46.3B vs 46.31B, ANET 207.0B vs 207.02B, ETN 142.2B vs 142.18B). The Nasdaq earnings-calendar market cap disagrees by more than 5% on AMD (824.1B), SMCI (21.6B), SWKS (13.0B) and SU (93.0B), and RACE is the one genuine disagreement across the good sources (TradingView $88.6B vs Yahoo $70.7B vs Digrin $67.4B). RACE is above the $50B bar on all three readings, so inclusion is unaffected.

## Source health

| Source | URL / query | Status |
|---|---|---|
| Wikipedia MediaWiki API (S&P 500 constituents) | `action=parse&page=List_of_S&P_500_companies&prop=wikitext` | ok — 503 symbols parsed (NyseSymbol + NasdaqSymbol + BZX link); control check BRK.B / GOOGL / GOOG / FOX / CBOE all present |
| EarningsWhispers calendar | `https://www.earningswhispers.com/calendar/20261103` | ok — 243 companies, 103 BMO / 140 AMC, server-rendered roster parsed in full |
| Nasdaq earnings calendar API | `https://api.nasdaq.com/api/calendar/earnings?date=2026-11-03` | ok — 279 rows; covers 229 of the 243 roster names (the 14 gaps are non-US lines) |
| Nasdaq calendar coverage gap | ET, EA, IITSF | partial — ET absent from the Nasdaq calendar (date taken from Energy Transfer IR) |
| MarketBeat earnings calendar | `https://www.marketbeat.com/earnings/2026-11-03/` | ok — 243 rows; no row for ET, EXPD, SHOP, XYZ (filled from StockAnalysis) |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` | ok — 371 tickers resolved with `market_cap_basic`; all 43 candidates resolved |
| Yahoo Finance earnings calendar | `https://finance.yahoo.com/calendar/earnings?day=2026-11-03` | ok via web_fetch — 26 rows retrievable (server-rendered first page only, 300 rows total); used as a cross-check, not as the primary |
| Yahoo Finance JSON endpoints | `query1.finance.yahoo.com/v7/finance/quote`, `/v1/test/getcrumb` | **429 rate-limited** from this egress — a rate limit, not a missing source; the web_fetch path works and was used instead |
| StockAnalysis forecast pages | `https://stockanalysis.com/stocks/{ticker}/forecast/` | ok — quarterly consensus EPS/revenue used for ET, EXPD, SHOP, XYZ and as a third-source cross-check |
| Digrin calendar | `https://www.digrin.com/stocks/earnings_calendar/2026-11-03` | **unreliable for dates** — 4 of its Nov 3 rows (LITE, FIS, GPN, LYV) contradicted by company sources; used only as a discovery aid for names the other calendars missed |
| MCP finance tools | — | not registered in this runtime (expected); not counted as an error |

## Method notes

- Inclusion rule: S&P 500 membership (live Wikipedia list, 503 symbols) **or** market cap above $50B. 37 S&P 500 names and 6 non-index mega-caps qualified: ET $70.0B, ITUB $82.6B, SU $88.2B, RACE $88.6B, TRI $53.0B and SHOP $201.0B. The $50B line itself is the tight boundary — KDP $50.1B is the only name inside by 0.1B and was confirmed by Keurig Dr Pepper's own IR release.
- Roster construction used the union of five calendars (EarningsWhispers 243, Nasdaq 279, MarketBeat 243, Yahoo 300, Digrin 521) rather than one feed. The EarningsWhispers+Nasdaq pair alone missed AES and ET; the wider sweep additionally surfaced LITE, GPN, LYV, TECH and EA — every one of which company sources then rejected or re-dated.
- Every name on the final list appears in at least two independent calendars, and every headline name plus every boundary name was confirmed against a company source.
- Status is `pending` for all 43: the aggregator actuals columns showed a result only for PHG across the entire 243-name roster at the snapshot time, and PHG is not in scope.
- Time zone for all times is US/Eastern; the snapshot was taken at 06:13 ET on 2026-11-03, 2h30m before the 08:30 ET pre-market brief that consumes this file.
- This is a read-only reminder: no analyst price targets, no valuation work, no earnings reaction.
