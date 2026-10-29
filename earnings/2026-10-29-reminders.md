---
date: 2026-10-29
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:14
source: EarningsWhispers + Nasdaq earnings calendar + MarketBeat day page (roster and estimates)
primary_source: MarketBeat (EPS, revenue) | shibui valuation (market cap)
status: ok
pending_count: 64
already_reported_count: 10
---

# Earnings - Thu 2026-10-29

Seventy-four names qualify under the cron filter: 62 S&P 500 constituents and 12 non-member mega-caps above $50B market cap. It is a very heavy day - the calendar carries 341 companies, and this roster is 22% of it. 10 of the 74 names had already printed by the 06:14 ET snapshot (every non-US session except one, plus two US names that released at 6:02 and 6:04am ET); the remaining 64 were still pending.

Two caveats change how this should be read. First, the EPS column carries real disagreement between providers on the Bitcoin-linked and REITs names, and a market-cap spread on one non-member name that straddles the $50B inclusion threshold - both are flagged in the conflicts section below rather than smoothed over. Second, the "reported" status is a 6am snapshot artefact: eight European and Asian names printed in their own overnight sessions, and the two US names marked reported released within four minutes of the cron firing, so the pending/reported split moves as the morning goes on.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Status |
|---|---|---|---|---|---|---|
| SHEL | Shell plc | BMO 03:00 ET (07:00 GMT) | $3.60 | $93.25B | $320.00B * | reported |
| BUD | Anheuser-Busch InBev SA/NV | BMO ~01:00 ET (Brussels) | $1.02 | $14.15B | $163.52B | reported |
| TTE | TotalEnergies SE | BMO (Europe, already printed) | $3.84 | $55.39B | $203.26B | reported |
| LYG | Lloyds Banking Group Plc | BMO 02:00 ET (07:00 UK) | $0.14 | $7.06B | $81.09B | reported |
| BBVA | Banco Bilbao Vizcaya Argentaria, S.A. | BMO (Madrid 09:30 = 03:30 ET) | $0.62 | $12.08B | $144.14B | reported |
| ASX | ASE Technology Holding Co., Ltd. | BMO ~03:40 ET (Taipei) | $0.34 | $7.30B | $96.03B | reported |
| TAK | Takeda Pharmaceutical Company Limited | BMO ~04:10 ET (Tokyo) | $0.15 | $7.34B | $63.67B | reported |
| ING | ING Groep N.V. | BMO (released ~6:05am ET) | $0.79 | $7.06B | $103.52B * | reported |
| WTW | Willis Towers Watson Public Limited Company | BMO (released ~6:02am ET) | $3.59 | $2.45B | $30.38B | reported |
| LHX | L3Harris Technologies, Inc. | BMO (released ~6:04am ET) | $2.95 | $5.92B | $48.55B | reported |
| LLY | Eli Lilly and Company | BMO (call 10:00am ET) | $5.68 | $22.58B | $1213.25B | pending |
| MA | Mastercard Incorporated | BMO (call 9:00am ET) | $5.17 | $9.66B | $539.26B | pending |
| MRK | Merck & Co., Inc. | BMO (call 9:00am ET) | $2.09 | $17.33B | $348.07B | pending |
| CAT | Caterpillar Inc. | BMO 6:30am ET (5:30am CDT) | $7.06 | $20.76B | $328.61B | pending |
| LIN | Linde plc | BMO by 6:00am ET (call 9:00am ET) | $4.52 | $9.16B | $235.07B | pending |
| BMY | Bristol-Myers Squibb Company | BMO | $1.10 | $12.73B | $123.69B | pending |
| MO | Altria Group, Inc. | BMO ~7:00am ET (call 9:00am ET) | $1.51 | $5.31B | $121.89B | pending |
| TT | Trane Technologies plc | BMO (call 10:00am ET) | $4.73 | $6.50B | $99.14B | pending |
| PWR | Quanta Services, Inc. | BMO before open (call 9:00am ET) | $5.02 | $11.03B | $91.07B * | pending |
| ICE | Intercontinental Exchange, Inc. | BMO | $1.97 | $2.74B | $88.20B | pending |
| EPD | Enterprise Products Partners L.P. | BMO before NYSE open (call 9:00am CDT) | $0.75 | $14.98B | $82.34B | pending |
| HWM | Howmet Aerospace Inc. | BMO ~7:00am ET (call 10:00am ET) | $1.37 | $2.59B | $78.10B | pending |
| LNG | Cheniere Energy, Inc. | BMO | $4.28 | $5.41B | $62.40B | pending |
| CRH | CRH plc | BMO | $2.06 | $11.56B | $57.83B | pending |
| XEL | Xcel Energy Inc. | BMO prior to market open (call 9:00am CT) | $1.39 | $4.26B | $48.18B | pending |
| CARR | Carrier Global Corporation | BMO | $0.76 | $6.09B | $46.74B | pending |
| AMP | Ameriprise Financial Inc | BMO | $11.77 | $5.10B | $44.03B | pending |
| DHI | D.R. Horton, Inc. | BMO | $2.99 | $9.05B | $40.55B | pending |
| WEC | WEC Energy Group, Inc. | BMO | $0.97 | $2.27B | $35.99B | pending |
| VMC | Vulcan Materials Company | BMO | $2.81 | $2.24B | $34.39B | pending |
| HSY | The Hershey Company | BMO | $2.11 | $3.25B | $33.22B | pending |
| CTSH | Cognizant Technology Solutions Corporation | BMO | $1.46 | $5.64B | $31.45B * | pending |
| EME | EMCOR Group, Inc. | BMO | $8.37 | $5.19B | $30.15B | pending |
| WST | West Pharmaceutical Services, Inc. | BMO | $2.20 | $827.12M | $28.52B | pending |
| ARES | Ares Management Corporation | BMO before NYSE open (call 9:00am ET) | $1.25 | $1.24B | $27.49B * | pending |
| INCY | Incyte Corp. | BMO | ($3.93) | $1.46B | $23.35B | pending |
| TROW | T. Rowe Price Group, Inc. | BMO | $2.63 | $1.98B | $22.28B | pending |
| BG | Bunge Global SA | BMO | $2.41 | $23.28B | $19.56B | pending |
| KIM | Kimco Realty Corporation | BMO | $0.20 | $549.06M | $15.78B | pending |
| AVY | Avery Dennison Corporation | BMO | $2.32 | $2.26B | $13.82B | pending |
| TXT | Textron Inc. | BMO | $1.43 | $3.77B | $13.62B | pending |
| BAX | Baxter International, Inc. | BMO | $0.52 | $2.91B | $13.15B | pending |
| HII | Huntington Ingalls Industries, Inc. | BMO | $4.36 | $3.38B | $11.00B | pending |
| AOS | A.O. Smith Corp. | BMO | $0.90 | $960.20M | $8.39B | pending |
| NCLH | Norwegian Cruise Line Holdings Ltd. | BMO | $0.93 | $2.88B | $7.37B | pending |
| AMZN | Amazon.com, Inc. | AMC 5:00pm ET (call 2:00pm PT) | $1.97 | $202.22B | $2738.76B | pending |
| INTC | Intel Corporation | AMC (call 2:00pm PDT) | $0.41 | $16.54B | $480.13B | pending |
| SNDK | Sandisk Corporation | AMC (call 1:30pm PT) | $46.41 | $10.70B | $208.03B * | pending |
| GILD | Gilead Sciences, Inc. | AMC | $2.19 | $7.80B | $197.66B | pending |
| SBUX | Starbucks Corporation | AMC (call 1:15pm PT) | $0.72 | $9.22B | $117.62B | pending |
| SYK | Stryker Corporation | AMC ~4:05pm ET (call 4:30pm ET) | $3.55 | $6.62B | $116.54B | pending |
| MDLZ | Mondelez International, Inc. | AMC 4:05pm ET (call 5:00pm ET) | $0.71 | $9.98B | $79.42B | pending |
| RSG | Republic Services, Inc. | AMC | $1.93 | $4.42B | $71.81B | pending |
| AJG | Arthur J. Gallagher & Co. | AMC | $2.99 | $3.98B | $66.90B | pending |
| DLR | Digital Realty Trust Inc | AMC (call 5:00pm ET) | $0.52 | $1.75B | $63.17B | pending |
| MPWR | Monolithic Power Systems, Inc. | AMC | $7.79 | $1.16B | $59.51B | pending |
| MSTR | Strategy Inc | AMC (call 5:00pm ET) | $20.19 | $127.76M | $50.87B * | pending |
| VALE | Vale S.A. | AMC | $0.38 | $10.45B | $48.96B * | pending |
| ILMN | Illumina, Inc. | AMC | $1.36 | $1.15B | $43.69B | pending |
| COIN | Coinbase Global, Inc. | AMC | ($0.23) | $1.21B | $42.76B | pending |
| TWLO | Twilio Inc. | AMC | $1.47 | $1.52B | $38.52B | pending |
| RMD | ResMed Inc. | AMC | $2.69 | $1.39B | $36.29B | pending |
| DXCM | DexCom, Inc. | AMC | $0.68 | $1.33B | $30.34B | pending |
| IR | Ingersoll Rand Inc. | AMC | $0.90 | $2.05B | $29.53B | pending |
| RDDT | Reddit, Inc. | AMC | $1.33 | $874.91M | $25.93B | pending |
| VLTO | Veralto Corporation | AMC | $1.09 | $1.50B | $25.25B | pending |
| EIX | Edison International, Inc. | AMC | $1.81 | $5.34B | $22.64B | pending |
| FSLR | First Solar, Inc. | AMC | $4.67 | $1.29B | $18.94B | pending |
| LNT | Alliant Energy Corporation | AMC | $1.31 | $1.26B | $17.92B | pending |
| FDXF | FedEx Freight Holding Company, Inc. | AMC (call 5:00pm ET) | $1.38 | ~$2.39B | $16.13B | pending |
| GDDY | GoDaddy Inc. | AMC | $1.90 | $1.33B | $14.11B | pending |
| WY | Weyerhaeuser Company | AMC | $0.04 | $1.92B | $13.84B | pending |
| DVA | DaVita Inc. | AMC | $3.57 | $3.52B | $11.81B | pending |
| ERIE | Erie Indemnity Company | AMC | $3.41 | $1.22B | $11.38B | pending |

An asterisk on a market cap means the shibui and Nasdaq readings differ by more than 5% on that name.

Sources per field: EPS and revenue from the MarketBeat day calendar for 2026-10-29 (72 of 74 rows; Sandisk and FedEx Freight filled from Yahoo Finance analysis and Nasdaq/Zacks respectively), cross-checked against the Nasdaq earnings calendar EPS forecast. Market cap is the shibui valuation snapshot for the 2026-10-28 close, cross-checked against the Nasdaq calendar market cap. Times are EarningsWhispers / Nasdaq / MarketBeat consensus unless the company has published a specific time, in which case the company time is used. Estimates are pre-release consensus, not results. "BMO" = before market open, "AMC" = after market close.

## Report dates confirmed at the company source (Rule B)

Aggregator calendars carry wrong dates, so report dates were checked against the issuing company. 32 of the 74 names were confirmed against a company release, an investor-relations calendar page, or the company's own Form 8-K / 6-K on EDGAR. No name required a date correction and no name was excluded - every confirmed date landed on 2026-10-29.

| Ticker | Company source | Evidence |
|---|---|---|
| AMZN | Amazon.com, Inc. | AMZN IR news release, Oct 15, 2026 |
| ARES | Ares Management Corporation | ir.ares.com release, Sep 29 + Oct 2, 2026; 8-K item 2.02 |
| ASX | ASE Technology Holding Co., Ltd. | ASEH release via PR Newswire, Oct 29, 2026 |
| BBVA | Banco Bilbao Vizcaya Argentaria, S.A. | BBVA financial calendar, Oct 29, 2026 |
| BUD | Anheuser-Busch InBev SA/NV | AB InBev release via Business Wire, Oct 29, 2026 |
| CAT | Caterpillar Inc. | investors.caterpillar.com, Oct 15, 2026 |
| DLR | Digital Realty Trust Inc | investor.digitalrealty.com release, Oct 1, 2026 |
| EPD | Enterprise Products Partners L.P. | ir.enterpriseproducts.com release; 8-K item 2.02 |
| FDXF | FedEx Freight Holding Company, Inc. | FedEx Freight IR release via Business Wire, Oct 2026 |
| GILD | Gilead Sciences, Inc. | investors.gilead.com news, Oct 15, 2026 |
| HWM | Howmet Aerospace Inc. | howmet.com release, Oct 1, 2026 |
| ING | ING Groep N.V. | 6-K accepted 2026-10-29 06:05 ET |
| INTC | Intel Corporation | intel.com newsroom, Oct 6, 2026 |
| LHX | L3Harris Technologies, Inc. | 8-K item 2.02 accepted 2026-10-29 06:04 ET |
| LIN | Linde plc | linde.com release, Oct 5, 2026 |
| LLY | Eli Lilly and Company | investor.lilly.com, Oct 15, 2026 |
| LYG | Lloyds Banking Group Plc | lloydsbankinggroup.com financial calendar, Oct 29, 2026 |
| MA | Mastercard Incorporated | investor.mastercard.com, Oct 8, 2026 |
| MDLZ | Mondelez International, Inc. | ir.mondelezinternational.com, Oct 15, 2026 |
| MO | Altria Group, Inc. | investor.altria.com release, Oct 15, 2026 |
| MRK | Merck & Co., Inc. | merck.com release, Oct 1, 2026 |
| MSTR | Strategy Inc | strategy.com media / Q3 2026 call notice |
| PWR | Quanta Services, Inc. | investors.quantaservices.com, Oct 13, 2026 |
| SBUX | Starbucks Corporation | investor.starbucks.com release, Oct 8, 2026 |
| SHEL | Shell plc | shell.com newsroom, Oct 29, 2026 |
| SNDK | Sandisk Corporation | investor.sandisk.com release, Sep 29, 2026 |
| SYK | Stryker Corporation | investors.stryker.com release, Oct 1, 2026 |
| TAK | Takeda Pharmaceutical Company Limited | takeda.com investor events; Investing.com, Oct 29, 2026 |
| TT | Trane Technologies plc | investors.tranetechnologies.com, Oct 8, 2026 |
| TTE | TotalEnergies SE | totalenergies.com Q3 results page, Oct 29, 2026 |
| WTW | Willis Towers Watson Public Limited Company | 8-K item 2.02 accepted 2026-10-29 06:02 ET |
| XEL | Xcel Energy Inc. | Xcel BusinessWire, Oct 7, 2026; 8-K item 2.02 |

The remaining 42 names were confirmed by agreement across three independent calendars (EarningsWhispers, Nasdaq, MarketBeat) with no conflicting issuer filing on EDGAR. They are calendar-confirmed rather than company-confirmed, and are marked as such here rather than being presented with the same confidence as the table above.

Three date checks came back unusually tight and are worth recording. ARES, EPD and XEL each filed the Form 8-K carrying their Item 2.02 results release on the evening of Oct 28 (accepted 17:38, 17:45 and 21:02 ET) with the press release itself dated Oct 29, 2026. That is a pre-filed, embargoed filing - the company dates the release Oct 29 and each company states the report comes before the NYSE open, so the date is confirmed as Oct 29 and all three are still pending at the snapshot. A reader who only looked at the EDGAR timestamp would wrongly read them as Oct 28 evening prints.

## Source conflicts and reconciliations (Rule C)

Tolerance applied: market cap >5%, EPS >2% is flagged. Primary source is fixed per field - MarketBeat for EPS and revenue, shibui for market cap - and the spread is recorded rather than averaged away.

| Ticker | Field | Sources | Spread | Resolution |
|---|---|---|---|---|
| AMZN | EPS | MarketBeat $1.97 vs Nasdaq $2.01 | 2.0% | Marginal (at the 2% tolerance). MarketBeat used (primary). |
| ARES | Mkt cap | shibui 27.49B vs Nasdaq 40.36B | 46.8% | shibui 2026-10-28 close used |
| BMY | EPS | MarketBeat $1.10 vs Nasdaq $1.21 | 10.0% | MarketBeat used (primary) |
| BUD | EPS | MarketBeat $1.02 vs Nasdaq $1.14 | 11.8% | MarketBeat used (primary) |
| CARR | EPS | MarketBeat $0.76 vs Nasdaq $0.81 | 6.6% | MarketBeat used (primary) |
| CRH | EPS | MarketBeat $2.06 vs Nasdaq $2.14 | 3.9% | MarketBeat used (primary) |
| CTSH | Mkt cap | shibui 31.45B vs Nasdaq 29.83B | 5.4% | shibui 2026-10-28 close used |
| DLR | EPS | MarketBeat $0.52 vs Nasdaq $1.97 | 278.8% | Definitional, not an error. $0.52 is GAAP EPS; $1.97 is the FFO consensus used by REITs. GAAP shown first, FFO alongside. |
| DVA | EPS | MarketBeat $3.57 vs Nasdaq $3.78 | 5.9% | MarketBeat used (primary) |
| DXCM | EPS | MarketBeat $0.68 vs Nasdaq $0.66 | 2.9% | MarketBeat used (primary) |
| GDDY | EPS | MarketBeat $1.90 vs Nasdaq $1.82 | 4.2% | MarketBeat used (primary) |
| ING | Mkt cap | shibui 103.52B vs Nasdaq 94.53B | 9.5% | shibui 2026-10-28 close used |
| INTC | EPS | MarketBeat $0.41 vs Nasdaq $0.28 | 31.7% | Definitional. $0.41 is the GAAP figure; $0.28 is the non-GAAP consensus that the sell side uses. Non-GAAP is the comparable number. |
| IR | EPS | MarketBeat $0.90 vs Nasdaq $0.86 | 4.4% | MarketBeat used (primary) |
| KIM | EPS | MarketBeat $0.20 vs Nasdaq $0.46 | 130.0% | Definitional. $0.20 is GAAP EPS; $0.46 is the FFO consensus. Both shown. |
| LLY | EPS | MarketBeat $5.68 vs Nasdaq $5.38 | 5.3% | MarketBeat used (primary) |
| LNT | EPS | MarketBeat $1.31 vs Nasdaq $1.23 | 6.1% | MarketBeat used (primary) |
| MPWR | EPS | MarketBeat $7.79 vs Nasdaq $6.80 | 12.7% | MarketBeat used (primary) |
| MSTR | Mkt cap | shibui 50.87B vs Nasdaq 59.67B | 17.3% | shibui 2026-10-28 close used |
| MSTR | EPS | MarketBeat $20.19 vs Nasdaq $21.50 | 6.5% | MarketBeat used (primary) |
| NCLH | EPS | MarketBeat $0.93 vs Nasdaq $0.88 | 5.4% | MarketBeat used (primary) |
| PWR | Mkt cap | shibui 91.07B vs Nasdaq 85.28B | 6.8% | shibui 2026-10-28 close used |
| PWR | EPS | MarketBeat $5.02 vs Nasdaq $4.68 | 6.8% | MarketBeat used (primary) |
| RDDT | EPS | MarketBeat $1.33 vs Nasdaq $1.30 | 2.3% | MarketBeat used (primary) |
| SHEL | Mkt cap | shibui 320.00B vs Nasdaq 295.26B | 8.4% | shibui 2026-10-28 close used |
| SNDK | Mkt cap | shibui 208.03B vs Nasdaq 189.63B | 9.7% | shibui 2026-10-28 close used |
| TAK | EPS | MarketBeat $0.15 vs Nasdaq $0.31 | 106.7% | Definitional. $0.15 is per ordinary share; $0.31 is per ADR (2 ordinary shares per ADR) - the two are not directly comparable. |
| TTE | EPS | MarketBeat $3.84 vs Nasdaq $4.11 | 7.0% | MarketBeat used (primary) |
| TWLO | EPS | MarketBeat $1.47 vs Nasdaq $0.74 | 49.7% | Unresolved divergence, not definitional: the providers disagree by roughly 2x on the same quarter with no GAAP/FOO explanation. MarketBeat used (primary); treat this EPS as the softest number in the table. |
| VALE | EPS | MarketBeat $0.38 vs Nasdaq $0.33 | 13.2% | MarketBeat used (primary) |
| WY | EPS | MarketBeat $0.04 vs Nasdaq $0.05 | 25.0% | MarketBeat used (primary) |
| VALE | Mkt cap | shibui $48.96B vs Nasdaq $50.55B | 3.2% | Threshold-straddling: included on the Nasdaq reading, excluded on the shibui reading. Flagged with an asterisk in the table. |

Two threshold cases deserve naming. VALE (Vale S.A.) is not an S&P 500 member and is included on market cap alone: shibui puts it at $48.96B and Nasdaq at $50.55B, which straddles the $50B threshold, so the inclusion is threshold-dependent and is flagged with an asterisk in the table. MSTR (Strategy Inc) is included on market cap alone and its two readings differ by 17.3% (shibui $50.87B, Nasdaq $59.67B), though both clear $50B.

MSTR is the outlier that matters most on the estimate side: consensus EPS is wildly provider-dependent because it is driven by a fair-value mark on a bitcoin treasury, and the quarterly estimate range runs from -$0.99 to $52.82. The headline EPS figure below should be read as "the mark", not as an operating number.

## Method and caveats

- **Filter.** S&P 500 membership (live constituent list) OR market cap above $50B, reporting today. Names below both thresholds were dropped.
- **S&P 500 membership (Rule A).** Parsed from the MediaWiki API wikitext of `List_of_S%26P_500_companies` (not the rendered HTML table), yielding 502 unique symbols. Control check passed: BRK.B, GOOGL, GOOG and FOX are all present.
- **Calendar coverage.** Three calendars were pulled and unioned: EarningsWhispers (341 rows server-rendered - 193 before the open, 148 after the close), the Nasdaq earnings calendar API (317 rows) and the MarketBeat day calendar (298 rows). The union covered 367 tickers. Lloyds Banking Group (LYG) appears only on Nasdaq and MarketBeat - EarningsWhispers does not carry it - and it qualifies on market cap, so the union was load-bearing rather than cosmetic.
- **Status.** "pending" means the release had not occurred at the 06:14 ET snapshot. "reported" means it was already public: eight European and Asian names printed in their own sessions (BBVA 03:30 ET, LYG 02:00 ET, SHEL 03:00 ET, ASX ~03:40 ET, TAK ~04:10 ET, BUD ~01:00 ET, TTE and ING in their continental sessions), and L3Harris and Willis Towers Watson filed Item 2.02 releases at 06:04 and 06:02 ET.
- **Estimates are pre-release consensus**, not actuals and not a forecast of what will print.
- **Not covered.** No watchlist section - `research/watchlist.yaml` is a local-only path and there is no equivalent in this runtime, so the section is omitted rather than shipped empty. No price targets, no reaction analysis, no modelled numbers - read-only reminder only.

## Source health

| Source | URL / query | Status |
|---|---|---|
| EarningsWhispers calendar | https://www.earningswhispers.com/calendar/20261029 | ok (HTTP 200, 258 KB, 341 rows parsed) |
| Nasdaq earnings calendar API | https://api.nasdaq.com/api/calendar/earnings?date=2026-10-29 | ok (HTTP 200, 317 rows) |
| MarketBeat earnings calendar | https://www.marketbeat.com/earnings/2026-10-29/ | ok (HTTP 200, 297 rows parsed; no row for SNDK, FDXF) |
| MarketBeat per-company (FDXF) | https://www.marketbeat.com/stocks/NYSE/FDXF/earnings/ | ok (HTTP 200; EPS only, no revenue estimate) |
| Yahoo Finance earnings calendar JSON | https://query1.finance.yahoo.com/v1/finance/calendar/earnings?day=2026-10-29 | failed: HTTP 404 - endpoint no longer served; Yahoo JSON remains 429 for other paths |
| Yahoo Finance quote analysis (SNDK) | https://finance.yahoo.com/quote/SNDK/analysis/ via web_search | ok (revenue $10.70B, EPS $46.41 normalized) |
| shibui-finance MCP bridge (market cap) | https://mcp.shibui.finance/mcp via /workspace/mcp_bridge.py | ok (298 of 341 roster tickers priced at 2026-10-28 close) |
| SEC EDGAR submissions + full-text search | https://data.sec.gov/submissions/CIK*.json, https://efts.sec.gov/LATEST/search-index | ok (74 issuer filing histories; 230 matching 8-K hits scanned) |
| Zacks quote pages | https://www.zacks.com/stock/quote/{SYM} | failed: HTTP 403 blocked from this egress - used Yahoo/Barchart for the two revenue gaps |
| Company IR pages / press releases | 32 issuer IR sites and Business Wire / PR Newswire releases | ok (32 names confirmed at the company source) |
| Nasdaq analyst earnings-forecast | https://api.nasdaq.com/api/analyst/{SYM}/earnings-forecast | ok (EPS only - carries no revenue consensus) |

## Data-quality notes carried forward

- EarningsWhispers lists some names twice under `T.`-prefixed alternate tickers (`T.QSR`, `T.CVO`, `T.TFI` and similar). These are the same companies under foreign line codes; none of them is an S&P 500 member, and the bases map to tickers already in the roster. Treated as one name each.
- MarketBeat had no calendar row for Sandisk or FedEx Freight. Sandisk was filled from Yahoo Finance analysis and its own IR release; FedEx Freight from Nasdaq/Zacks and Barchart ($2.39B revenue, $1.38 EPS). Both are single-source on the revenue line and softer than the rest of the column.
- Linde (LIN) states its Q3 release will be published "by 06:00 EDT" on Oct 29 - i.e. at or before the cron's own fire minute. No Form 8-K had been accepted at the 06:14 ET snapshot, so it is listed as pending, but it is the one name whose results may already be public on the company's own site.
- The 43 roster tickers with no shibui valuation row are almost entirely OTC and foreign lines with no US tape (ADRZY, AMLIF, JAPSY and similar). None of them reaches the inclusion filter, so the gap costs nothing here.
- Nasdaq's market cap for FedEx Freight ($16.2B) is a post-spinoff stub figure with no last-year EPS or report date attached, consistent with FedEx Freight having been spun out of FedEx on June 1, 2026.
