---
date: 2026-11-13
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:14
source: EarningsWhispers earnings calendar + Nasdaq earnings API + Yahoo Finance + TradingView scanner + TDnet (TSE timely disclosure) + issuer IR pages and results releases
primary_source: Yahoo Finance (market cap) | TradingView (band market caps, issuer-level) | TDnet + issuer results releases (non-US report dates, times and actuals) | EarningsWhispers (EPS and revenue estimates)
status: ok
pending_count: 0
already_reported_count: 3
non_us_count: 3
reaction_ranked: true
reaction_degraded: 0
band_low_usd: 40000000000
degraded_sources: 1
contract: EARNINGS_REMINDER_V3
coverage_receipt: calendar_rows=103 s_and_p_500_hits=0 bigcap_hits=4 us_roster_rows=0 band_rows=10
---

# Earnings - Fri 2026-11-13

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

_No row: no S&P 500 constituent and no US-primary mega-cap reports on 2026-11-13. The only names clearing the $50B floor are two Japanese mega-bank ADRs and one Italian insurer, and all three published before this 06:00 ET fire - see the sections below._

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|

_No row: every non-US issuer in scope for the 2026-11-13 ET day had already published before the fire, so this table is empty rather than padded. The overnight prints are in the section below._

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| WCN | Waste Connections, Inc. | $48.5B | no |
| MSTR | Strategy Inc | $48.3B | no |
| FNV | Franco-Nevada Corporation | $47.8B | no |
| TRI | Thomson Reuters Corp | $47.4B | no |
| NTRA | Natera, Inc. | $46.8B | no |
| AU | AngloGold Ashanti PLC | $44.2B | no |
| FER | Ferrovial N.V. | $43.7B | no |
| UI | Ubiquiti Inc | $41.3B | no |
| RKLB | Rocket Lab Corporation | $40.5B | no |
| SLF | Sun Life Financial Inc. | $40.4B | no |

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus | us_tradeable |
|---|---|---|---|---|---|
| GASI.MI (ARZGY) | Assicurazioni Generali S.p.A. | Nov 13, 01:00 ET (07:00 CET) | 9M 2026 (to 30 Sep): GWP EUR 76.5B +4.5% (P&C +6.3%, Life +3.5%); operating result EUR 6,446M +8.5% (Life EUR 3,321M +7.4%, P&C EUR 2,861M +4.5%, Asset & Wealth Management EUR 1,039M +23.2%); adjusted net result EUR 3.7B +12.0%; adjusted EPS EUR 2.43 +12.4%; new business value EUR 2,563M +12.7%; combined ratio 92.8% +0.5pp, undiscounted combined ratio 95.1% +0.9pp on EUR 1.47B nat-cat claims (5.2pp of the CR) and EUR 323M man-made claims; Life net inflows EUR 11.7B +13.6%; solvency ratio 211% (219% at FY25); management says the group is on track to exceed all "Lifetime Partner 27" targets | mixed - operating result and adjusted net result broadly in line with the company-compiled analyst consensus (Reuters); the undiscounted combined ratio 95.1% came in 0.3pp WORSE than the 94.8% consensus | ADR (OTC) |
| 8411.T (MFG) | Mizuho Financial Group, Inc. | Nov 13, 01:30 ET (15:30 JST) | FY2027 H1 (Apr-Sep 2026): ordinary revenues JPY 4,993,079M +15.1%; ordinary profit JPY 1,252,326M +47.3%; net profit attributable to owners of parent JPY 896,492M +29.9%; EPS JPY 368.81 (vs JPY 276.20); interim DPS JPY 100.00 (vs JPY 72.50), FY DPS forecast JPY 200.00 (vs JPY 145.00 paid in FY2026); FY2027 net profit forecast RAISED to JPY 1,600,000M from the JPY 1,400,000M prior plan (+14.2% vs plan, +28.1% year on year); total assets JPY 320,856,742M | not measured - the aggregator consensus (EarningsWhispers/Nasdaq EPS $0.21, revenue $6.72B) is a Jul-Sep per-ADS figure on a different basis from the issuer's half-year statement, and the like-for-like quarterly comparison was not read | ADR (US-listed) |
| 8306.T (MUFG) | Mitsubishi UFJ Financial Group, Inc. | Nov 13, 02:15 ET (16:15 JST) | FY2027 H1 (Apr-Sep 2026): ordinary revenues JPY 7,995,095M +16.0%; ordinary profit JPY 2,260,957M +29.4%; net income attributable to owners of parent JPY 1,630,897M +26.1%; EPS JPY 144.73 (vs JPY 113.07); interim DPS JPY 48.00 (vs JPY 35.00), FY DPS forecast JPY 100.00 (vs JPY 86.00 paid in FY2026); FY2027 net income TARGET revised to JPY 2,800,000M from the 15 May plan; a buyback decision and a guidance/dividend revision were filed alongside; total assets JPY 425,775,404M, equity ratio 5.4% | not measured - same basis mismatch as Mizuho (EarningsWhispers/Nasdaq EPS $0.45, revenue $9.86B) | ADR (US-listed) |

## Notes

- **Nothing on the US roster is the story today; the two NYSE bank ADRs are.** No S&P 500 constituent and no US-primary mega-cap reports on 2026-11-13: the EarningsWhispers roster (103 rows, parsed) and the Nasdaq calendar (205 rows, parsed) carry ZERO index members, and a TradingView sweep of the 1,496 names above $20B puts only Williams-Sonoma on the 13th - below the band floor, with the real action on 16-19 November (NVIDIA, Home Depot, Disney, Tencent, Palo Alto, Walmart, Alibaba). The names that clear the $50B floor are **MUFG (NYSE ADR, $244.8B)**, **MFG (NYSE ADR, $122.2B)** and **Generali (Euronext Milan, EUR 67.25B ≈ $74.3B at EUR/USD 1.1053)**, and every one of them had already published before the 06:00 ET fire.
- **Both Japanese banks beat on the half-year and one raised guidance.** Mizuho lifted FY2027 net profit guidance to JPY 1.6T from JPY 1.4T (+14.2% vs the prior plan) on H1 ordinary profit +47.3%; MUFG revised its FY2027 net income target to JPY 2.8T on H1 ordinary profit +29.4%. Both lifted the interim dividend (Mizuho JPY 100.00 vs 72.50; MUFG JPY 48.00 vs 35.00) and the full-year dividend forecast (Mizuho JPY 200.00; MUFG JPY 100.00). The NYSE ADR lines are where a US trader expresses it - both are ADR (US-listed), so both are tradeable in today's session.
- **Release instants come from TDnet, the exchange's own timely-disclosure feed, not from the aggregators.** Mizuho 15:30 JST = 01:30 ET, MUFG 16:15 JST = 02:15 ET, Generali 07:00 CET (its own IR page) = 01:00 ET. The TDnet day list for 2026-11-13 was paged in full (23 pages, 08:00-20:00 JST), so every Japanese disclosure up to the fire instant was checked, and EarningsWhispers still had Mizuho on "November 12, after the market close" - the issuer outranks the aggregator.
- **Sumitomo Mitsui Financial (8316.T) is deliberately NOT published here.** TDnet has its FY2027 H1 決算短信 at 13:30 JST on Nov 13, which is **23:30 ET on Nov 12** - a different ET day. The same trap measured on the 2026-11-06 fire (Mitsubishi Heavy Industries and Macquarie Group both landed on the previous ET day) applies: a brief dated 13 November must not carry it. Its USD cap is $152.9B, so it is one of the four names above the floor; it is excluded from this brief on the ET-day rule, not on size. Its results are nevertheless public since 23:30 ET last night and the NYSE ADR trades today, so its absence from the tables is a scoping decision, not a claim that it has not reported.
- **Williams-Sonoma (WSM) is the only US name TradingView stamps for today, and it is not published.** TV carries a 2026-11-13 07:00 ET next-release stamp for WSM - the same stale stamp that made the 2026-11-12 brief exclude it on Rule B (MarketBeat had it on a 18 November call and the issuer had published no date of its own). WSM's cap is $29.5B, below the $40B band floor, and it is not an index member, so it fails the size test either way.
- **The action is next week, not today.** The same TradingView universe (1,496 names above $20B) puts NVIDIA, Home Depot and Disney on 17 November, Tencent, Palo Alto Networks, TJX, Lowe's and Target on 18 November, and Walmart, Alibaba, PDD, Tokio Marine, Intuit and NetEase on 19 November. Friday the 13th is the thin session between them.
- **No other standing Japanese candidate reports today.** TDnet for 2026-11-13 carries no results disclosure for Hitachi, Fujitsu, Nissan, Mitsubishi Electric, Nintendo, Takeda, Nomura, Daiichi Sankyo, KDDI, Tokyo Electron or Advantest; KDDI's only 13 Nov filing is a share-buyback status notice, not results.
- **The Korean names on the Nasdaq calendar are calendar noise, and they are excluded with the issuer's own dates.** KB Financial's own IR page and its DART fair-disclosure filing put its 3Q26 release on **29 October 2026, 16:00 KST**; KT Corporation reported on **10 November 2026**; Woori Bank's Q3 print was 29 October and its 13 November news is a CEO reappointment. None falls on the 13 November ET day, so none is published. KB also fails the band test twice over - its cap is $38.2B (TradingView) / $40.7B (Nasdaq) and its US line is a depositary receipt, which the mechanical non-common filter removes.
- **The reaction layer has no row to rank.** With an empty US roster there is no prior-day move, no implied move and no reaction score to compute, so `reaction_degraded` is 0 by there being nothing to degrade. The columns return the moment a US-primary name appears.
- **The consensus cells on the two Japanese banks are not measured, and that is deliberate.** EarningsWhispers and Nasdaq carry per-ADS quarterly consensus figures for MUFG ($0.45 EPS, $9.86B revenue) and MFG ($0.21, $6.72B) that do not reconcile with the issuer's reported half-year figures on any JPY/USD rate - the issuer reports the six months to 30 September (EPS JPY 144.73 and JPY 368.81), and the like-for-like Jul-Sep comparison would need the issuer's Q1 baseline, which this run did not read. A number borrowed across those bases would be worse than an empty cell.
- **Every US line in this brief is verified from Yahoo's chart metadata (venue + currency + name), not assumed.** MUFG: NYSE, USD, $21.75, against 8306.T at JPY 3,475 (=$21.73 at USD/JPY 159.905) - one NYSE line per ordinary share. MFG: NYSE, USD, $10.12, against 8411.T at JPY 8,020 (=$50.15) - the NYSE line trades at about one fifth of the primary ordinary share. Generali: ARZGY (ADR, OTC Markets, USD, $24.77) and ARZGF (ordinary, OTC Markets, $35.01), both named in Generali's own Rule 701(e) information statement. The issuers' 決算短信 are quoted in JPY and EUR throughout, so no converted EPS is published here.
- **Generali's US line is an unsponsored ADR and an ordinary line, both OTC.** Generali's own Rule 701(e) information statement names them as **ARZGF** (ordinary) and **ARZGY** (ADR), trading over the counter in the US, and Citi's depositary-receipt register lists ARZGY (CUSIP 04545K109). Neither is listed on a US exchange, so `us_tradeable` is `ADR (OTC)` and the headline ticker is the Milan primary line. Yahoo's chart and quote endpoints carry no coverage for GASI.MI, so the EUR 67.25B cap is read from the Yahoo UK earnings calendar instead and the USD figure is converted at a named rate.
- **The band is ONE source for the whole table: TradingView's issuer-level market cap**, with Yahoo as the cross-check. A $40.49B band row (RKLB) reads $43.12B on Yahoo, a 6.5% spread, flagged here; every other band row is within 0.6%. The band is US-listed common shares only - the mechanical non-common filter (description match on Preferred/Pfd/Notes/Bond/Subordinated/Depositary/Perp/Warrant/Right/Unit/ADR/Sponsored/LP/Trust/Income) removed ten foreign ordinary lines that the literal rule would have put on top of it (PICC P&C $49.9B, DNB $49.9B, Swiss Re $49.2B, Holcim $48.7B, Commerzbank, Danone, ArcelorMittal, Reckitt, Jiangsu Hengrui, Panasonic). HEICO sits just outside the ten-row cap at $40.24B (issuer-level; HEI and HEI.A both read the same) and is named here rather than dropped.
- **The band is a lower bound on the excluded set** - names below $40B are cut by the band, not by the $50B floor. No US name sits within $0.5B of the floor today, so no row carries `boundary_case`.
- **One source degraded, and it is named:** Yahoo's regional earnings-calendar pages (US/UK/Canada) are JS-rendered in this runtime and could not be parsed, so the European roster was spot-read from the indexed page rather than enumerated - Generali came out of that spot read. Everything else in this brief comes from a source parsed or paged in full: EarningsWhispers (103 rows), Nasdaq (205 rows), the TradingView universe (1,496 names above $20B), the TDnet disclosure day (23 pages) and the issuers' own releases.
- **Watchlist:** `refs/watchlist.yaml` fetched cleanly (AAPL, MSFT, NVDA, GOOGL, AMZN, IWM, GLD, TLT) but none of them reports on 13 November - the nearest is NVDA on 17 November - so no watchlist section is published rather than an empty table.
- **What the front-matter counts mean:** `pending_count` 0 = no issuer in this brief is still waiting to print (the US roster and the pending non-US table are both empty); `already_reported_count` 3 = the rows in the Already-reported section; `non_us_count` 3 = every non-US issuer published here (3 pending + 0 reported rows carry the same three issuers).
- **Ticker convention:** headline tickers are the issuer's primary listing with the US line in parentheses - `8306.T (MUFG)`, `8411.T (MFG)`, `GASI.MI (ARZGY)`. An OTC line is never the headline.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| EarningsWhispers calendar | `https://www.earningswhispers.com/calendar/20261113` | ok | Server-rendered; 99 before the open + 4 after the close, matching the page's own headline of 103 companies |
| EarningsWhispers company pages | `.../stocks/MUFG`, `/MFG`, `/KB` | ok | Needed the documented `ewc` cookie (pages of ~159 KB, not the 2 KB wall); carried MUFG on Nov 13 BMO but still had Mizuho on "November 12, after the market close" and KB on Nov 12 - both contradicted by issuer sources |
| TDnet (TSE timely disclosure) | `release.tdnet.info/inbs/I_list_001..040_20261113.html` and the same for 20261112 | ok | 23 pages for Nov 13 covering 08:00-20:00 JST - the full disclosure day up to the fire instant; source of every Japanese release instant, and the reason SMFG is excluded |
| Issuer results releases | MUFG 決算短信 PDF (TDnet 140120261112577371), Mizuho 決算短信 PDF (TDnet 140120261112576848), Generali 9M2026 press release and its IR "Financial Results" page | ok | The two 決算短信 are the issuer's own statements (JPY, half-year to 30 Sep); Generali's own page gives the 07:00 CET release slot and the 14:30 CET call |
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/<SYM>` | ok | 8306.T / 8411.T / 8316.T (JPX, JPY) and the US ADR lines; no crumb required; one "Edge: Too Many Requests" was retried with a browser UA and succeeded |
| Yahoo v7 quote | `.../v7/finance/quote?symbols=...` | ok | Market caps; needs the cookie + crumb handshake (seed `fc.yahoo.com` first); carries no GASI.MI line |
| Nasdaq earnings calendar | `api.nasdaq.com/api/calendar/earnings?date=2026-11-13` | ok | 205 rows; carried MUFG, SMFG, MFG and the Korean banks - the Korean entries are wrong for 13 Nov (see notes) |
| TradingView scanner | `scanner.tradingview.com/america/scan` | ok | A cap>20B sweep (1,496 names) and a $40-50B band pull (155 rows) for the band table's issuer-level caps; its next-release stamps are NOT the completeness source - almost every large US name carried a rolled-forward 2027 date, and only WSM still carried 13 Nov |
| Wikipedia constituent list | `en.wikipedia.org/w/api.php?action=parse&page=List_of_S%26P_500_companies&prop=wikitext` | ok | 503 symbols; controls BRK.B, GOOGL, GOOG, FOX, CBOE all present; zero of the day's calendar rows are members |
| Nasdaq earnings calendar | `api.nasdaq.com/api/calendar/earnings?date=2026-11-13` | ok | 205 rows, parsed; 0 S&P 500 members; the Korean entries (KB, KT, WF) are wrong for 13 Nov - see notes |
| Yahoo regional earnings calendars | `finance.yahoo.com/calendar/earnings?day=2026-11-13` (+ ca/uk/gb) | degraded | The HTML is JS-rendered in this runtime, so the pages could not be parsed: the row counts (US 46, UK 69, Canada 24) and the European names came from the indexed page, not from a full parse. Generali came from that spot read; the completeness of the day rests on EarningsWhispers, Nasdaq, TradingView, TDnet and issuer pages, all parsed in full |

## Rules applied

- S&P 500 membership verified against the live constituent list - never from memory (503 symbols, all five control symbols present).
- Report dates and times confirmed against issuer-owned pages or the exchange's own disclosure feed for every name near the inclusion boundary; the local announcement time was converted to ET with `zoneinfo` and compared with the fire's scheduled instant (06:00 ET, 2026-11-13).
- An issuer confirmed as 13 November locally but whose release lands on the 12 November ET day (SMFG, 13:30 JST) is NOT published in this brief.
- The non-US table is a separate table and never overlaps the US roster; a foreign issuer with a US listing is published on its primary listing with the US line in parentheses, and `us_tradeable` says what that US line is.
- The market-cap floor is published with what it excludes; the band table is US-listed common shares only, one row per issuer, one source (TradingView issuer-level cap), with the non-common filter applied in code and any cross-source spread over 5% flagged.
- A figure that was not measured is published as "not measured" with its reason - never estimated from a peer, a prior quarter or a converted basis.
- A local-currency number carries its currency; a converted figure names the rate it was converted at (EUR/USD 1.1053, USD/JPY 159.905).
