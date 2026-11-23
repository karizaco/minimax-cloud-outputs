---
date: 2026-11-23
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:04
source: EarningsWhispers earnings calendar + company pages, Nasdaq earnings calendar, TradingView america scanner, Yahoo Finance chart/quoteSummary
primary_source: TradingView scanner (market cap, issuer-level USD) | EarningsWhispers company pages (EPS est, Rev est, release time) | issuer IR (report date and time)
status: ok
pending_count: 3
already_reported_count: 0
non_us_count: 0
reaction_ranked: true
band_low_usd: 40000000000
contract: EARNINGS_REMINDER_V4
coverage_receipt: calendar_rows=59 s_and_p_500_hits=3 bigcap_hits=1 us_roster_rows=3 band_rows=9
coverage_floor: floor_usd=50000000000 band_low_usd=40000000000 us_population=5468 below_band_us=4899 band_us=62 at_or_above_floor_us=402 no_cap_us=105 source=TradingView america scanner (market_cap_basic, issuer-level USD)
---

# Earnings - Mon 2026-11-23

## TL;DR

- **Coverage floor — a scope limit, not a missing company.** This reminder covers S&P 500
  constituents plus US-listed reporters with a market cap of **$50B or more** (TradingView
  scanner, `market_cap_basic`, issuer-level USD). The band just under the floor — **$40B to $50B**
  — is published in the *Just below the line* table so the cliff is visible. **A US reporter below
  $40B market cap is out of scope for this reminder: it is not on this list, and its absence does
  not mean it did not report.** Of the scanner's **5,468** US names, **4,899** are below the $40B
  band floor and therefore out of scope, **62** sit in the $40B-$50B band, **402** are at or above
  the $50B floor, and **105** carry no market cap at all.
- **Three names report today, all after the close: HPE, Agilent (A) and Jacobs (J).** The roster
  is ranked by reaction potential, not by size: **HPE** leads on a 7.41 average absolute earnings
  move, **Agilent** on 5.98 and **Jacobs** on 4.20.
- **HPE is the one to watch.** It closed the last session down **10.07%** while sitting **+69.26%
  YTD**, and its own guidance puts fiscal Q4 revenue at $13.9B-$14.8B with non-GAAP diluted EPS
  of $1.20-$1.30. A name that has already re-rated 69% YTD and then dropped 10% into a print is
  the widest reaction distribution on the board.
- **Agilent's consensus is the outlier on the tape.** EarningsWhispers carries $1.29 for HPE,
  Nasdaq/Zacks carries $1.18 — a 9% spread, flagged below. HPE's own guidance ($1.20-$1.30
  non-GAAP) sits on the EarningsWhispers side of it.
- **No overnight print on the board.** Nothing in the roster, and no non-US standing-list
  candidate, had published before the 06:00 ET fire.

## Your watchlist

The published watchlist (`refs/watchlist.yaml`, fetched at run time) carries 8 names. **None of
them reports today**, so every row below is a "no" — the section is published because the
watchlist file exists and was readable, not to pad the board.

| Ticker | Note | Earnings flag | Reports today |
|---|---|---|---|
| AAPL | mega-cap core; earnings flag | yes | no |
| MSFT | mega-cap core; earnings flag | yes | no |
| NVDA | mega-cap core; earnings flag | yes | no |
| GOOGL | mega-cap core; earnings flag | yes | no |
| AMZN | mega-cap core; earnings flag | yes | no |
| IWM | small-cap beta leg | no | no |
| GLD | gold leg | no | no |
| TLT | duration leg | no | no |

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HPE | Hewlett Packard Enterprise Company | AMC 4:05 PM | $1.29 | $14.45B | $54.31B | -10.07 | 69.26 | 7.41 | n/a | beat | 7.41 | pending | - |
| A | Agilent Technologies, Inc. | AMC 4:05 PM | $1.72 | $1.98B | $48.04B | -2.83 | 23.51 | 5.98 | n/a | beat | 5.98 | pending | - |
| J | Jacobs Solutions Inc. | AMC 4:10 PM | $2.11 | $3.61B | $17.63B | -2.56 | 11.28 | 4.20 | n/a | beat | 4.20 | pending | - |

## Non-US primary listings

**Empty on this fire.** A date sweep over 15 non-US TradingView markets (taiwan, japan, korea,
hongkong, australia, canada, brazil, singapore, india, uk, germany, switzerland, france, spain,
netherlands) for the 2026-11-23 release window returned **no standing-list candidate** with an
issuer-owned report date, and no standing-list candidate had published before the 06:00 ET fire.
The table is published as a header with no rows rather than dropped, so a reader can see the
section was checked and came back empty.

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|

## Just below the line - excluded by the $50B floor

US-listed common shares in the $40B-$50B band that the $50B floor excluded. One row per issuer,
issuer-level market cap from the TradingView scanner (the same row that produced the candidate
set). None of them reports today.

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| WPM | Wheaton Precious Metals Corp | $49.9B | no |
| CVE | Cenovus Energy Inc | $48.9B | no |
| MDLN | Medline Inc. | $48.7B | no |
| TEVA | Teva Pharmaceutical Industries Limited | $45.8B | no |
| WCN | Waste Connections, Inc. | $44.9B | no |
| TRI | Thomson Reuters Corp | $44.0B | no |
| FNV | Franco-Nevada Corporation | $43.1B | no |
| VIK | Viking Holdings Ltd | $41.6B | no |
| FER | Ferrovial N.V. | $40.9B | no |

## Notes

- **Ranked by reaction potential, not by market cap.** HPE, Agilent and Jacobs lead on their
  typical earnings move, not on size; HPE is both the largest name on the board and the most
  reactive, which is not always the case.
- **The implied move is `n/a` on every row, and the score is still published.** The Cboe
  delayed-quote chain (`cdn.cboe.com/api/global/delayed_quotes/options/<SYM>.json`) answered with
  a Cloudflare HTML challenge page instead of JSON for all three names from this egress, so no
  ATM straddle could be measured. Under the contract's substitution rule a missing implied move is
  replaced by the average absolute move, so each score equals its `Avg abs move %` exactly. **No
  row lost its score, so `reaction_degraded` is not declared** — the degradation is in one
  column, not in the ranking, and it is named here rather than hidden.
- **Market-cap spread flagged (HPE).** The TradingView scanner carries HPE at $54.31B; Nasdaq
  carries it at $60.39B — a 10% spread, above the 5% tolerance, and it is flagged here. The
  published cap is the scanner's, because the scanner is also the source of the band table and
  the floor. Agilent ($48.04B vs $49.43B) and Jacobs ($17.63B vs $18.09B) are within tolerance.
- **EPS spread flagged (HPE).** EarningsWhispers carries $1.29 (non-GAAP basis, and inside HPE's
  own $1.20-$1.30 non-GAAP guidance range); Nasdaq/Zacks carries $1.18. The published EPS is the
  EarningsWhispers figure. Agilent ($1.72) and Jacobs ($2.11) agree across both sources.
- **Agilent is in the roster as an index member, not as a $50B name.** At $48.04B it sits below
  the market-cap floor; it is published because it is an S&P 500 constituent, and the roster's
  scope is every constituent whatever its cap. It is therefore *not* repeated in the band table.
- **Report dates confirmed on issuer-owned pages (Rule B), not on aggregators:**
  - **HPE** — the issuer's own newsroom release *"HPE to present live audio webcast of fiscal 2026
    fourth quarter earnings conference call"* (hpe.com, 2 Nov 2026) states the Q4 call is
    scheduled for Monday, 23 November 2026 at 4:00 p.m. CT, and `investors.hpe.com` carries the
    11/23/2026 Q4 FY2026 event.
  - **Agilent** — the issuer press release *"Agilent to Announce Fourth-Quarter Fiscal Year 2026
    Financial Results on Nov. 23"* (investor.agilent.com, 29 Oct 2026) states results are released
    **after the stock market closes on Monday, Nov. 23**, with the call at 1:30 p.m. PST
    (4:30 p.m. ET).
  - **Jacobs** — the issuer release *"Jacobs to hold its fiscal fourth quarter and full year 2026
    earnings conference call and webcast"* (invest.jacobs.com, 26 Oct 2026) states results are
    released **after market close on Monday, Nov. 23, 2026**, with the call at 4:30 p.m. ET; the
    issuer's event page carries November 23, 2026 4:30 PM ET.
- **Published release times are EarningsWhispers' expected prints** (HPE 4:05 PM, A 4:05 PM,
  J 4:10 PM ET); the issuers publish the *call* time, not the release time. All three are
  after-close releases on their own calendars.
- **Calendar hits not published, with the reason (59 distinct common-line rows scanned across
  three calendars):** 3 S&P 500 members and 1 name at or above the $50B floor were published;
  the remaining hits were excluded because they are below the $40B band floor (Zoom $23.7B,
  Symbotic $18.8B, Amentum $5.1B, Semtech $9.5B, Trip.com Group $26.6B, Tuya $0.9B, Compass
  Minerals $0.8B, Fluence $0.6B, Danaos $2.6B, Central Garden & Pet $2.6B, Alico, VNET, CRGO,
  THCH and the sub-$300M remainder) or because they are non-common lines (HPE/PC, PNNT, PFLT,
  FSCO, ALCO and the remaining preferred/depositary lines, filtered mechanically on the
  description). **Trip.com Group** (9961.HK / TCOM, $26.6B) is the one non-US issuer of US-market
  relevance on the calendar: it is below the $40B band floor and is not on the standing non-US
  candidate list, and Nasdaq carries no release time for it, so it is not published.
- **The per-day count of reporters below the band was not enumerated** — that would need a
  market-cap pull for every one of the 59 calendar rows and does not fit the 06:45 ET discovery
  cutoff. The four population counts above are the measured decomposition and are never
  estimated.
- **Ticker convention:** all three roster rows are US-primary listings, so no ADR or OTC line is
  published as a headline ticker.
- **No `## Already reported` table.** Nothing printed before the 06:00 ET fire.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| Coverage floor (scope limit) | `scanner.tradingview.com/america/scan` — `market_cap_basic` (issuer-level USD), constants `MCAP_FLOOR = $50B` and `band_low_usd = $40B` | ok | The roster is bounded by the market-cap band, not by who reported: S&P 500 constituents plus US-listed names at or above $50B, with the $40B-$50B band published below the floor. A US reporter below $40B market cap is out of scope — it is not on this list (a scope limit, not a missing company). US names below the band floor: 4,899 of 5,468 (62 in the band, 402 at or above the floor, 105 with no cap) |
| EarningsWhispers calendar | `https://www.earningswhispers.com/calendar/20261123` | ok | Server-rendered; the page's own headline count (4 before the open, 19 after the close) matches the parsed BMO and AMC lists |
| EarningsWhispers company pages | `https://www.earningswhispers.com/stocks/{HPE,A,J}` | ok | Consensus EPS, `Rev est` and the expected release time in ET; fetched with the `ewc` cookie, pages ~161 KB each |
| Nasdaq earnings calendar | `api.nasdaq.com/api/calendar/earnings?date=2026-11-23` | ok | 37 rows; EPS consensus and BMO/AMC, no revenue field; used as the cross-check on the EPS and market-cap spreads |
| S&P 500 constituent list | `en.wikipedia.org/w/api.php?action=parse&page=List_of_S%26P_500_companies&prop=wikitext` | ok | 503 symbols parsed from all three symbol templates (`NyseSymbol`, `NasdaqSymbol`, `BZX link`); control check passed on BRK.B, GOOGL, GOOG, FOX and CBOE |
| TradingView america scanner — earnings-date sweep | `scanner.tradingview.com/america/scan`, `earnings_release_next_date` within 2026-11-23 | ok | 52 rows; the completeness cross-check on the calendar roster (every hit confirmed on a second source before publication) |
| TradingView non-US market sweeps | `scanner.tradingview.com/{taiwan,japan,korea,hongkong,australia,canada,brazil,singapore,india,uk,germany,switzerland,france,spain,netherlands}/scan` | ok | Pass B completeness evidence for the fire date; no standing-list candidate hit |
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/<SYM>` | ok | Daily bars for the prior-day move, the YTD move and the 4-report reaction average (no crumb needed) |
| Yahoo quoteSummary (`earningsHistory`) | `query1.finance.yahoo.com/v10/finance/quoteSummary/<SYM>?modules=earningsHistory` | ok | Prior result for all three rows (`prior_report_source: yahoo_earningsHistory`); latest quarter-end selected, not the oldest |
| Cboe delayed-quote option chain | `cdn.cboe.com/api/global/delayed_quotes/options/{A,J,HPE}.json` | degraded | Answers a Cloudflare HTML challenge page (4.5 KB) instead of JSON from this egress, so no implied move could be measured; the score substitutes `Avg abs move %` per the contract's substitution rule |
| Watchlist | `api.github.com/repos/karizaco/minimax-cloud-outputs/contents/refs/watchlist.yaml` | ok | Published file fetched (HTTP 200); 8 names, none reporting today |

## Rules applied

- S&P 500 membership verified against the live constituent list — never from memory; 503
  symbols, control-checked.
- Report dates confirmed against issuer-owned pages for every published name (HPE, Agilent,
  Jacobs); the aggregators agreed, and each confirmation is cited in the notes.
- Reaction columns computed from measured bars, past report dates and option chains; the one
  column that could not be measured is published as `n/a` and named in the notes and here.
- Market cap taken from one source for the whole artifact (the TradingView scanner, issuer-level
  USD), with the Nasdaq spread above 5% flagged for HPE.
- The market-cap floor is published with what it excludes: front matter, TL;DR and source health
  carry the same floor, band and counts, and the counts add up.
- The two tables do not overlap: no name appears in both the US roster and the non-US table, and
  the US roster's rows are not repeated in the band table.
