---
date: 2026-11-27
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 07:24
source: EarningsWhispers earnings calendar + Yahoo Finance earnings calendar + Nasdaq earnings calendar + TradingView scanner
primary_source: Yahoo Finance (market cap, EPS est, revenue est) | TradingView america scanner (issuer-level USD caps for the band)
status: ok
pending_count: 0
already_reported_count: 3
non_us_count: 2
reaction_ranked: true
band_low_usd: 40000000000
reaction_degraded: 0
contract: EARNINGS_REMINDER_V4
coverage_receipt: calendar_rows=24 s_and_p_500_hits=0 bigcap_hits=0 us_roster_rows=0 band_rows=10
coverage_floor: floor_usd=50000000000 band_low_usd=40000000000 us_population=5489 below_band_us=4907 band_us=64 at_or_above_floor_us=412 no_cap_us=106 source=TradingView america scanner (market_cap_basic, issuer-level USD)
---

# Earnings - Fri 2026-11-27

## TL;DR

- **Coverage floor - a scope limit, not a missing company.** This reminder covers S&P 500
  constituents plus US-listed reporters with a market cap of **$50B or more** (TradingView
  america scanner, `market_cap_basic`, issuer-level USD). The band just under the floor -
  **$40B to $50B** - is published in the *Just below the line* table so the cliff is visible.
  **A US reporter below $40B market cap is out of scope for this reminder: it is not on this list,
  and its absence does not mean it did not report.** Of the scanner's **5,489** US names,
  **4,907** are below the $40B band floor and therefore out of scope, **64** sit in the
  $40B-$50B band, **412** are at or above the $50B floor, and **106** carry no market cap at
  all.
- **The US board is empty, and that is the measured answer, not a missing feed.** No S&P 500
  constituent prints today and no US reporter at or above the $50B floor prints today. Three
  independent calendars (Nasdaq, Yahoo Finance, EarningsWhispers) were unioned into **24**
  distinct tickers: **0** S&P 500 hits and **0** names at or above the floor. The largest US
  printer on the calendar is Virgin Galactic (VFS, **$6.57B**) - two orders of magnitude below
  the floor - and the next two are Dream Vegas (DRVN, $1.91B) and Hub Group (HUBG, $1.42B).
- **Nothing is pending: every print of the day was already public before the 06:00 ET fire.**
  Three names reported and all three landed before the fire - **Meituan (3690.HK) at 03:40 ET**,
  **DiDi Global (DIDIY) at ~04:40 ET**, and **Cathay Financial (2882.TW)** with its results on
  the issuer's site ahead of the 14:00 TWD (06:00 ET) analyst meeting. `pending_count` is 0 and
  the reaction ranking has no row to rank; the ranking rule is still in force.
- **What a US reader can actually trade this morning is the two ADSs, not the boards.** NYSE and
  Nasdaq open at 09:30 ET and close early at **13:00 ET** (Black Friday; Nov 26 was closed for
  Thanksgiving). **MPNGY** (Meituan's OTC ADR) and **DIDIY** (DiDi's NYSE ADS) both have their
  results out but have not traded since - they are the live expression of today's prints.
- **Meituan's Hong Kong close ran +8.21% BEFORE the release - the ADR has not caught up yet.**
  3690.HK closed at HK$67.85 (+8.21%) on Nov 27, and the results announcement was published
  only **after** that close, at ~16:40 HKT (03:40 ET). The move was anticipation plus
  Chinese State Council capital-market news, not the print. MPNGY's last close was **$16.00**
  on Nov 25.
- **The band is ten names and none of them reports.** CVE, TRI, FNV, WCN, TEVA, VIK, NTRA, RKT,
  FER and RPRX sit in the $40B-$50B band the floor excluded; every next release date on the
  scanner falls in February or March 2027.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

_No row qualifies, and the emptiness is the finding._ The roster is defined as S&P 500
constituents plus US-listed reporters at or above the **$50B** floor, and on Nov 27 neither set
produces a row: the 503-name S&P 500 sweep returns only December-2026 to March-2027 next
earnings dates (the sole exception is AMCR, whose date the scanner does not carry), and the
412-name at-or-above-the-floor sweep does the same. Friday after Thanksgiving is a thin tape
for issuers, and the calendar confirms it: 24 distinct tickers across three sources, of which
**none** is an S&P 500 member and **none** clears the floor.

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|
| 3690.HK | HKEX (Hong Kong) | Meituan | Nov 27, 16:40 HKT (03:40 ET), after the HK close | MPNGY | ADR (OTC) | reported |
| 2882.TW | TWSE (Taiwan) | Cathay Financial Holding | Nov 27, 14:00 TWD (06:00 ET) analyst meeting; results already public | none (no US-listed line) | none | reported |

_Both rows are non-US primary listings whose results fall on the fire date and whose dates are
confirmed on issuer-owned pages; both had already printed when the 06:00 ET fire arrived, so
both carry `reported` rather than `pending`._ **Meituan** is confirmed by its own HKEX
announcement (stock codes 3690/83690, filed 2026/11/27) and by the board-meeting notice it
published on Nov 17. **Cathay** is confirmed by the issuer's own IR event calendar
(2026 Third Quarter Analyst Meeting, 2026/11/27 14:00 TWD, webcast + presentation) and its
results-presentation page, which lists the Q3 2026 deck under 2026/11/27. Neither issuer has a
US-listed line beyond Meituan's OTC ADR, and Cathay has none at all, so `us_tradeable` is
`none` for it rather than a placeholder.

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| CVE | Cenovus Energy | $48.85B | no (next 2027-02-09) |
| TRI | Thomson Reuters | $47.40B | no (next 2027-02-11) |
| FNV | Franco-Nevada | $47.22B | no (next 2027-03-10) |
| WCN | Waste Connections | $46.85B | no (next 2027-02-17) |
| TEVA | Teva Pharmaceutical Industries | $46.51B | no (next 2027-02-10) |
| VIK | Viking Holdings | $43.90B | no (next 2027-03-16) |
| NTRA | Natera | $43.69B | no (next 2027-03-04) |
| RKT | Rocket Companies | $43.42B | no (next 2027-02-25) |
| FER | Ferrovial | $42.21B | no (next 2027-03-04) |
| RPRX | Royalty Pharma | $40.48B | no (next 2027-02-16) |

_Ten US-listed common shares sit in the $40B-$50B band the floor excluded, and **none of them
reports today** - every next release date on the scanner falls in February or March 2027. The
caps are the TradingView scanner's issuer-level `market_cap_basic`; the Yahoo cross-check
agrees to within 0.6% on all ten (FER $42.21B vs $42.45B, RPRX $40.48B vs $40.58B, the other
eight within 0.1%), so no spread needs flagging._ The band holds 64 scanner names in total;
the other 54 are S&P 500 members (whose roster row would be the US list above), sponsored ADRs
of foreign issuers (ABEV, HMC, MT, VALE, HLN, NOK, SE, ONC - primary-listed elsewhere, so they
belong in the non-US universe rather than here), and preferred shares and notes (FITB/STT
preferreds, PRU notes), which are not common shares.

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus | us_tradeable |
|---|---|---|---|---|---|
| DIDIY (NYSE: DIDIY ADS) | DiDi Global Inc. | ~04:40 ET (issuer PR dated Beijing, Nov 27, 2026; wire timestamps 17:38-17:46 Beijing) | Q3 2026: revenue RMB 65.7B (+12.2% y/y); net loss RMB 792M (Q2 was a RMB 1.46B profit); loss per ADS RMB 0.18; adjusted EBITDA RMB 907M (-43% y/y); adjusted EBITA RMB 10M (-99%); GTV RMB 140.8B (+21.5%); core platform transactions 5.226B (+11.5%); international revenue +57% to RMB 6.2B; 448.6M ADS repurchased for $1.963B to Nov 25 | revenue **beat** (RMB 65.7B vs the Yahoo consensus RMB 64.89B, +1.25%); the loss per ADS (RMB 0.18) came in **narrower than the consensus loss** (-$0.0413 per ADS, about -RMB 0.30), but adjusted EBITDA fell 43% y/y and adjusted EBITA fell 99% | US-listed |

_DiDi is a US reporter below the $40B band floor - out of scope for the roster - and it is
published here for one reason only: its results were public before the 06:00 ET fire and its
NYSE ADS still trades this morning._ The release hour is measured, not assumed: the issuer's
press release is dated "Beijing, November 27, 2026" without an hour, and the two wire
timestamps that carry the numbers (Cailian Press at 17:38 Beijing, Investing.com at 04:46 ET)
both put the release at roughly **04:40 ET**, before the fire. The historical control is
consistent - DiDi's Q2 release on Aug 13 was followed by a +10.45% move in DIDIY on Aug 13 -
so the reaction day is the same ET day as the release, and the ADS opens this morning with the
numbers already out. Last close **$2.81** (Nov 25).

## Notes

- **Ranked by reaction potential, not by size.** With zero roster rows the ranking is empty,
  and that is the honest output: no S&P 500 constituent and no at-or-above-the-floor US
  reporter prints today, so there is no prior-result history to average and no implied move to
  compute. `reaction_ranked` stays `true` because the rule governs the roster whenever it has
  rows; `reaction_degraded` is **0** because no row lost a column.
- **Three prints, three clocks, and each one is anchored to an issuer-owned page.** Meituan:
  HKEX announcement filed 2026/11/27, published at ~16:40 HKT (03:40 ET) - Sina's HK tape
  carries it at 16:40 Beijing, Investing.com's Chinese desk at 16:41 - with the board-meeting
  notice of Nov 17 as the date anchor. DiDi: issuer PR dated Beijing Nov 27, wire timestamps
  17:38-17:46 Beijing (04:38-04:46 ET), corroborated by Reuters and Bloomberg running the
  story on the Beijing evening of Nov 27. Cathay: the issuer's IR event calendar and
  results-presentation page both date the Q3 disclosure to 2026/11/27, and the Q3 presentation
  PDF carries a file timestamp of 2026-11-26 15:03 +08:00, so the numbers were on the
  issuer's site before the fire.
- **Cathay's date carries an unresolved conflict, and it is disclosed rather than hidden.**
  TradingEconomics and TipRanks record a Cathay Q3 print on **2026-11-13** (EPS 2.64 vs a 2.16
  consensus, revenue 81.77B vs a 102.72B consensus), while the issuer's own pages - the Q3
  analyst meeting on 2026/11/27 14:00 TWD, the results-presentation page listing the Q3 deck
  under 2026/11/27, and the transcript published 05:05 ET on Nov 27 - put the disclosure on
  Nov 27. The issuer's own pages win under Rule B, and either way the numbers were public
  before this fire, so Cathay is published as already-reported and nothing about it is pending.
  The Taiwan session has already priced it: 2882.TW closed at NT$102.0 on Nov 27 (**-2.39%**)
  after NT$104.5 (+3.98%) on Nov 26; the Nov 24 +9.47% gap was market-wide (TAIEX +8.99%),
  not Cathay-specific.
- **Cathay's numbers as published.** 9M 2026 net income NT$105.4B (EPS NT$6.94), or NT$223.7B
  including after-tax FVOCI equity disposal gains taken straight to retained earnings - an
  all-time high; Q3 net interest margin 1.67%, up 4bp quarter-on-quarter; CSM balance +10.9%
  year-to-date; operating cash inflow NT$4.8B. Market cap NT$1.50T, about **US$45.5B** at the
  Nov 27 close of 32.97 TWD/USD - below the $50B floor in any case, and irrelevant to it,
  because the floor applies to US-listed common shares and Cathay is TWSE-listed with no US
  line.
- **Meituan's numbers as published.** Revenue RMB 115.556B (+21.6% y/y) against the Yahoo
  consensus of RMB 113.08B (+2.19%) and against the market expectation of RMB 113.37B
  (+1.93%) - a **beat** on revenue. Operating profit RMB 2.741B against a RMB 19.759B loss a
  year ago; profit for the period RMB 2.071B against a RMB 18.632B loss a year ago; adjusted
  EBITDA RMB 4.581B; segment operating profit swung positive to RMB 4.4B with core local
  commerce at RMB 5.7B, against a RMB 1.3B operating loss in new businesses. The **adjusted
  net profit of RMB 1.850B missed the market expectation of RMB 2.201B by 15.9%** - that is
  the line to watch, and it is the reason the HK close ran +8.21% *before* the print rather
  than after it. Meituan's market cap is about **$49.4B** (MPNGY basis), just under the $50B
  floor; as a non-US issuer with an OTC line it is not subject to the floor.
- **Date-confirmed exclusion.** **Nidec (Tokyo: 6594, OTC: NJDCY, ~$12.1B)** is excluded: on
  Nov 16, 2026 the company announced it is **postponing** the disclosure of its Q2 FY2027
  results beyond the 45-day window, so the scanner's Nov 27 release date is wrong and Nidec
  does not report today. It is named here rather than published on a stale estimate.
- **The 47-name standing non-US universe was swept and returned nothing for today.** Every
  standing candidate was checked across the whole global release calendar (851 names stamped
  for the Nov 27 window, plus the US calendars); none carries a Nov 27 date - the next dates
  run 2027-01-21 to 2027-05-07. Alibaba (9988.HK) next reports Nov 19, already past.
- **Watchlist.** The watchlist was fetched successfully and **no watchlist ticker reports
  today**, so the `## Your watchlist` section is omitted rather than shipped empty.
- **This snapshot was taken at 07:24 ET, before the 09:30 ET open**, in a shortened session -
  NYSE and Nasdaq close at 13:00 ET on Nov 27, and both were closed on Nov 26 for
  Thanksgiving. Nothing in this artifact depends on a price after the Nov 25 close except the
  Meituan ADR and DiDi ADS lines, which have not traded since.

## Source health

| Source | Used for | Status | Note |
|---|---|---|---|
| Coverage floor (scope limit) | the $50B floor and the $40B band | ok | A US reporter below **$40B** market cap is **out of scope** for this reminder - it is **not on this list**, and its absence does not mean it did not report. The floor is the TradingView america scanner's `market_cap_basic` column (issuer-level USD): 5,489 US names, 4,907 below the $40B band, 64 in the band, 412 at or above the $50B floor, 106 with no cap. |
| TradingView america scanner | market cap, next/previous earnings date, band membership | ok | `type in (stock,dr)`, `exchange in (NASDAQ,NYSE,AMEX)`, `close>1`; issuer-level caps. Every band cap is cross-checked against Yahoo. |
| Yahoo Finance | market cap, EPS/revenue estimates, consensus, price bars | ok | `quoteSummary` with the crumb handshake; daily bars for 3690.HK, MPNGY, DIDIY, 2882.TW and the USD/TWD rate. |
| Nasdaq earnings calendar | the daily calendar | ok | 12 rows for 2026-11-27; largest name KT Corporation at $7.9B. |
| EarningsWhispers calendar | the daily calendar | ok | 6 rows for 2026-11-27 (GEBHY, LEDS, V.GBU, V.OMG, XYF before the open; TRX after the close). |
| HKEX / issuer PR (Meituan) | the Nov 27 report date and time | ok | HKEX announcement 2026112700341 (codes 3690/83690) filed 2026/11/27; board-meeting notice of Nov 17; HK close HK$67.85 (+8.21%). |
| Cathay Financial IR pages | the Nov 27 date | ok (date conflict disclosed) | IR event calendar and results-presentation page both date the Q3 disclosure to 2026/11/27; TradingEconomics/TipRanks carry a Nov 13 print - the issuer's own pages win, and the conflict is published in the notes. |
| DiDi IR press release + wires | the Nov 27 release and its hour | ok | Issuer PR "Beijing, November 27, 2026"; Cailian Press 17:38 Beijing, Investing.com 04:46 ET, Reuters/Bloomberg on the Beijing evening. |
| Wikipedia MediaWiki wikitext | S&P 500 membership | ok | 503 symbols parsed across all three templates; controls BRK.B, GOOGL, GOOG, FOX, CBOE all present. |
| Blocked this run | - | blocked | MOPS (Taiwan), HKEX titleSearchServlet, MarketBeat, Investing.com (main site), stockanalysis.com, `symbol-search.tradingview.com`, Cathay Financial's own corporate site - issuer-owned HKEX, PR and IR pages were used instead. |

## Rules applied

- **Rule A - S&P 500 membership from a live constituent list.** MediaWiki wikitext, all three
  symbol templates parsed, 503 symbols, controls `BRK.B` / `GOOGL` / `GOOG` / `FOX` / `CBOE`
  present. The rendered HTML table and the stale datasets CSV were not used.
- **Rule B - every report date confirmed against a company source.** Meituan, DiDi and Cathay
  are each anchored to an issuer-owned page (HKEX announcement, issuer PR, issuer IR event
  calendar). Nidec's Nov 27 date was refuted by the issuer's own postponement notice and the
  name is excluded rather than published.
- **Rule C - one primary source per field, spreads flagged.** Market cap: TradingView scanner
  (issuer-level USD), cross-checked against Yahoo; the widest spread is FER at +0.57% and
  RPRX at +0.25%, both inside the 5% tolerance, so nothing needs flagging. Revenue and EPS
  estimates: Yahoo for Meituan and DiDi, the market expectation quoted by Futu/Investing for
  Meituan's adjusted net profit. Where no consensus exists (Cathay's 9M figures), it is not
  invented - it is stated as unmeasured.
- **The floor is stated, not implied.** Front matter, TL;DR and the source-health table all
  carry the $50B floor, the $40B band, the source of the floor and the counts that bound the
  list, so a scope limit never reads as a missing company.
- **Status is published.** Every row says `pending` or `reported`; today all three prints are
  `reported`, and the reason is the measured release hour, not a guess.
- **No fabricated numbers.** Every figure in the tables traces to an issuer page, an exchange
  filing, the Yahoo/TradingView APIs or a dated wire story. The one figure deliberately not
  published is a Meituan per-share EPS: the announcement's attributable profit is RMB 2.070B,
  but the per-share figure is not stated in the text extracted, so the revenue and
  adjusted-profit comparisons are published instead.
