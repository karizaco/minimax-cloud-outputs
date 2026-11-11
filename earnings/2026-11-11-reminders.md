---
date: 2026-11-11
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:14
source: EarningsWhispers earnings calendar (209 companies - 99 BMO / 110 AMC) + Nasdaq earnings calendar (218 rows) + Yahoo Finance earnings calendar + issuer IR calendars
primary_source: TradingView scanner (market cap) | Yahoo Finance (EPS est, revenue est) | issuer IR pages (report date and local announcement time)
status: ok
pending_count: 2
already_reported_count: 4
non_us_count: 5
reaction_ranked: true
band_low_usd: 40000000000
reaction_degraded: 1
degraded_sources: 1
---

# Earnings - Wed 2026-11-11

A light mega-cap day. Exactly **one** S&P 500 constituent reports today - Vylor Inc. (VYLR),
after the close - and **no** US-listed name above the $50B market-cap floor prints today. The
action on this calendar sits in Europe before the US open: E.ON, RWE, Siemens Energy and
ABN AMRO all published at 07:00 CET (01:00 ET), and Siemens Energy is already +8.95% at XETRA
as this artifact was written.

## Your watchlist

Omitted. The published watchlist (`refs/watchlist.yaml`, 8 tickers: AAPL, MSFT, NVDA, GOOGL,
AMZN, IWM, GLD, TLT) was fetched successfully, but **none** of those names reports on
2026-11-11 in any of the three calendars checked, so the section is left out rather than
shipped as an empty table.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VYLR | Vylor Inc. | AMC (after close, Nov 11) | -0.52 | $918.1M | $48.4B | 0.00 | +6.26 | n/a | 6.48 | n/a | n/a | pending | - |

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|
| ENR.DE | XETRA | Siemens Energy AG | Nov 11, 2026 (release before 07:00 CET; analyst call 11:00 CET) | SMERY (OTC ADR) | ADR (OTC) | reported |
| EOAN.DE | XETRA | E.ON SE | Nov 11, 2026, 07:00 CET | EONGY (OTC ADR) | ADR (OTC) | reported |
| RWE.DE | XETRA | RWE AG | Nov 11, 2026, approx. 07:00 CET | RWEOY (OTC ADR) | ADR (OTC) | reported |
| ABN.AS | Euronext Amsterdam | ABN AMRO Bank N.V. | Nov 11, 2026, 07:00 CET | AAVMY (OTC ADR) | ADR (OTC) | reported |
| POW.TO | Toronto Stock Exchange | Power Corporation of Canada | Nov 11, 2026, after market close (16:00 ET) | PWCDF (OTC) | ADR (OTC) | pending |

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| TEVA | Teva Pharmaceutical Industries Limited | $49.5B | no |
| FNV | Franco-Nevada Corporation | $49.3B | yes |
| WCN | Waste Connections, Inc. | $47.8B | no |
| AU | Anglogold Ashanti PLC | $47.4B | no |
| TRI | Thomson Reuters Corporation | $47.0B | no |
| NTRA | Natera, Inc. | $45.2B | no |
| FER | Ferrovial N.V. | $43.5B | no |
| RVMD | Revolution Medicines, Inc. | $41.8B | no |
| UI | Ubiquiti Inc. | $41.5B | no |
| RKT | Rocket Companies, Inc. Class A | $41.0B | no |

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus |
|---|---|---|---|---|
| ENR.DE (SMERY) | Siemens Energy AG | Nov 11, pre-US-open (XETRA +8.95% by 06:00 ET) | FY26 revenue EUR 44.2bn (+15.5% comparable), profit before special items EUR 5,486m (FY25 EUR 2,355m), margin 12.4%, EPS EUR 4.44; Q4 revenue EUR 12.8bn, EPS EUR 1.49; dividend EUR 2.30 proposed | n/a - no consensus sourced for this run |
| EOAN.DE (EONGY) | E.ON SE | Nov 11, 01:00 ET (07:00 CET) | 9M26 adjusted Group EBITDA EUR 7.11bn (flat YoY), adjusted Group net income EUR 2.2bn (+4%); FY26 guidance (EBITDA EUR 9.4-9.6bn, net income EUR 2.7-2.9bn) reaffirmed | in line (Vara-compiled consensus, via Reuters) |
| RWE.DE (RWEOY) | RWE AG | Nov 11, 01:00 ET (approx. 07:00 CET) | 9M26 revenue EUR 12,367m, adjusted EBITDA EUR 4,575m (9M25 EUR 3,398m), adjusted EPS EUR 2.52 (EUR 1.77); FY26 guidance reaffirmed | n/a - no consensus sourced for this run |
| ABN.AS (AAVMY) | ABN AMRO Bank N.V. | Nov 11, 01:00 ET (07:00 CET) | Q3 2026 net profit EUR 940m | n/a - no consensus sourced for this run |

## Notes

- **Why the roster is one row.** The US roster is every S&P 500 constituent plus every US-listed
  name above the $50B floor, intersected with three independent calendars (EarningsWhispers
  209 names, Nasdaq 218 rows, Yahoo Finance). The live Wikipedia constituent list parses to
  **503** symbols with all three symbol templates (NyseSymbol, NasdaqSymbol, BZX link) and the
  control tickers BRK.B, GOOGL, GOOG, FOX and CBOE all present. Only **VYLR** survives as an
  S&P 500 constituent reporting today, and **no** US-listed name above $50B prints - the only
  names over that line on the calendar are OTC ADR lines of non-US issuers (IFNNY, EONGY, RWEOY,
  LBLCF), which belong in the non-US universe, not in this table.
- **VYLR is in the roster on membership, not size.** Vylor joined the S&P 500 on 2026-10-01
  (Consumer Staples / Agricultural Products, CIK 212862). Its $48.4B cap sits below the $50B
  floor; the Nasdaq calendar carries $46.8B for the same name, a 3.4% spread that is inside
  tolerance and does not change the floor test. Flag is `-`: a row inside the floor by less than
  $0.5B carries `boundary_case`, and VYLR is not inside the floor at all.
- **Reaction columns are degraded on VYLR, and that is a real gap, not a fetch failure.**
  Nasdaq's earnings-surprise endpoint returns **zero** past report dates for VYLR - it is a newly
  listed entity with no earnings history - so `Avg abs move %` and `Prior result` are `n/a` and no
  composite score can be computed. `reaction_degraded: 1` records exactly that one row. The
  implied move **is** measured: a Cboe ATM straddle at strike 75.00 against the 2026-11-20 expiry
  (the first expiry that straddles the event) is 6.48% of the $72.53 close. With a single row and
  no score, no reaction ranking could be established today - the table is not sorted by score
  because there is only one row.
- **Two aggregator dates were wrong and both names were dropped.** EarningsWhispers carried
  **IFNNY (Infineon)** as BMO on Nov 11; Infineon's own press release and TDnet timestamp show it
  published its FY2026 Q4 on **10 November 07:30 CET**, which is the 10 November ET day. Nasdaq
  carried **TECH (Bio-Techne)**; its 8-K (Nov 4) and 10-Q (Nov 6) show Q1 FY2027 was already
  reported on Nov 5. Neither appears in this artifact.
- **Loblaw is not a November 11 name either.** Its own press release (Oct 22) says Q3 2026
  results come on **November 19, 2026** at approx. 06:30 ET. EarningsWhispers' Nov 11 BMO entry
  for LBLCF is wrong.
- **Poste Italiane is deliberately excluded.** Its own 2026 corporate events calendar splits the
  Q3 event across two days: the board approves the interim report on operations at 30 September
  2026 on **Nov 11**, and the Q3 & 9M-26 Group Results presentation is **Nov 12, 11:00 CET**
  (= Nov 12, 05:00 ET). The results announcement therefore falls on the **12 November ET day**,
  and the Nov 11 entry carries no published local time to convert, so it is not published here.
- **Checked and not published:** Nan Ya Plastics (TWSE 1303, $69.5B) carries an aggregator
  earnings date on Nov 11 but no issuer-confirmed ET announcement time and no US line.
- **The four names printed before the fire appear twice on purpose.** They are listed in the
  non-US table for their reference data (primary listing, venue, US line, status) and again in
  the "Already reported" table for the published figures. No issuer appears twice inside the
  three contract tables.
- **Count definitions:** `pending_count: 2` = published names still ahead (VYLR, POW.TO);
  `already_reported_count: 4` = names that printed before the 06:00 ET fire;
  `non_us_count: 5` = rows in the non-US table.
- **Band caveats.** The band is a **lower bound** on what the $50B floor excluded - names below
  $40B are excluded by the band, not by the floor. Twelve names qualify once depositary-receipt
  lines (TradingView type `dr`) and preferreds, notes, bonds, warrants, rights and units are
  filtered out; the ten largest are published and SLF ($40.9B) and HEI ($40.8B) sit just below
  the cut. That same filter is why the ADR lines in the band (INFY, MT, NOK, VALE, SE, HMC,
  ABEV, ONC, WDS) are absent - they are depositary receipts, and their issuers are covered by
  the non-US universe when they report.
- **Ticker convention.** Primary listing first with its exchange suffix; the US line follows in
  parentheses or in `us_peer`. No OTC or ADR line is ever the headline. Foreign amounts are
  published in the issuer's own currency and labelled.
- **Cadence and reliability of the calendars.** EarningsWhispers publishes a per-day calendar
  and **rolls a company forward** once it has reported (its IFNNY page now points at Nov 18) -
  its dates are a screening list, not a source of truth. Nasdaq's calendar is a same-day snapshot
  with a market cap, an EPS forecast and a BMO/AMC flag, but **no revenue** and a
  `time-not-supplied` value on some rows. Yahoo's calendar carries EPS but no revenue. Issuer IR
  pages are the only authority for a date and a local announcement time, and every row published
  here was confirmed on one.
- **Degraded source.** Yahoo's quote API (`v7/finance/quote`, `quoteSummary`) returned
  **HTTP 429 rate-limited** for the whole run from this egress. A 429 is a rate limit, not an
  absence: market caps were taken from the TradingView scanner instead and EPS/revenue from the
  Yahoo and Nasdaq calendar and analysis pages. No published field was left unmeasured.
- **Limitations.** The reaction layer needs prior earnings history, so on a day with one
  S&P 500 constituent the screen has almost no surface. Consensus "vs consensus" cells are
  `n/a` where no consensus figure was sourced in this run - they are not estimated.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| EarningsWhispers earnings calendar | `https://www.earningswhispers.com/calendar/20261111` | ok | server-rendered; page headline "209 companies ... 99 before the open and 110 after the close" matched the parsed lists exactly (99 BMO / 110 AMC) |
| Nasdaq earnings calendar | `api.nasdaq.com/api/calendar/earnings?date=2026-11-11` | ok | 218 rows; carries `marketCap`, `epsForecast`, `time`; no revenue field |
| Yahoo Finance earnings calendar | `finance.yahoo.com/calendar/earnings?day=2026-11-11` | ok | first rows server-rendered; EPS estimate present, revenue not shown |
| Yahoo Finance quote API | `query1.finance.yahoo.com/v7/finance/quote` | failed: 429 rate-limited | every attempt, whole run; fell back to the TradingView scanner for market caps |
| Yahoo Finance chart API | `query1.finance.yahoo.com/v8/finance/chart/<SYM>` | ok | daily bars for prior-day/YTD moves and the European reaction check; a few symbols returned no chart |
| TradingView scanner | `scanner.tradingview.com/america/scan`, `/global/scan` | ok | `market_cap_basic` + `earnings_release_next_date`; the market-cap band was sliced into windows because a single wide sweep silently truncates at the range cap |
| Nasdaq earnings-surprise | `api.nasdaq.com/api/company/VYLR/earnings-surprise` | ok (0 rows) | HTTP 200 with an empty set - VYLR has no past report dates, so `Avg abs move %` and `Prior result` are `n/a` rather than a fetch failure |
| Cboe delayed option chain | `cdn.cboe.com/api/global/delayed_quotes/options/VYLR.json` | ok | ATM straddle at strike 75.00, expiry 2026-11-20 -> implied move 6.48% |
| Wikipedia S&P 500 wikitext | `en.wikipedia.org/w/api.php?action=parse&page=List_of_S%26P_500_companies&prop=wikitext` | ok | 503 symbols; controls BRK.B, GOOGL, GOOG, FOX, CBOE all present |
| Issuer IR pages | E.ON, RWE, Siemens Energy, ABN AMRO, Power Corporation, Vylor, Poste Italiane, Loblaw, Infineon, Bio-Techne | ok | date and local announcement time confirmed on each issuer's own page |
| Published watchlist | `refs/watchlist.yaml` (minimax-cloud-outputs) | ok | 8 tickers, none reporting today - section omitted, not shipped empty |

## Rules applied

- S&P 500 membership verified against the live constituent list (503 symbols, all three symbol
  templates parsed, control tickers checked) - never from memory.
- Every published report date confirmed on an issuer-owned page; aggregator-only dates were not
  published, and every date-confirmed exclusion is recorded in the Notes.
- Reaction columns measured from Yahoo daily bars and the Cboe delayed chain. A column that could
  not be measured is published as `n/a` and counted in `reaction_degraded` - never estimated from
  market cap, a peer name, or a guess.
- The roster is ranked by reaction potential, not by market cap; with one row and no derivable
  score, no ordering was available.
- Primary listing first with its exchange suffix; no OTC or ADR ticker is ever the headline, and
  local-currency amounts carry their currency.
- The three contract tables do not overlap, and no issuer is published twice inside them.
- The $50B floor is published with the band it excludes, and a row inside the floor by less than
  $0.5B carries `boundary_case` (none today).
- Local announcement times converted with `zoneinfo` and compared against the fire's scheduled
  instant (2026-11-11 06:00 ET), never against the wall clock.
