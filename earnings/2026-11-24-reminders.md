---
date: 2026-11-24
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:05
source: EarningsWhispers earnings calendar + TradingView scanner + Nasdaq earnings calendar
primary_source: TradingView scanner (market cap, issuer-level USD) | EarningsWhispers (EPS est, revenue est, release time)
status: ok
pending_count: 9
already_reported_count: 2
non_us_count: 1
reaction_ranked: true
band_low_usd: 40000000000
contract: EARNINGS_REMINDER_V4
coverage_receipt: calendar_rows=38 s_and_p_500_hits=9 bigcap_hits=4 us_roster_rows=9 band_rows=8
coverage_floor: floor_usd=50000000000 band_low_usd=40000000000 us_population=5489 below_band_us=4914 band_us=62 at_or_above_floor_us=407 no_cap_us=106 source=TradingView america scanner (market_cap_basic, issuer-level USD)
---

# Earnings - Tue 2026-11-24

## TL;DR

- **Coverage floor — a scope limit, not a missing company.** This reminder covers S&P 500
  constituents plus US-listed reporters with a market cap of **$50B or more** (TradingView
  scanner, `market_cap_basic`, issuer-level USD). The band just under the floor — **$40B to
  $50B** — is published in the *Just below the line* table so the cliff is visible. **A US
  reporter below $40B market cap is out of scope for this reminder: it is not on this list, and
  its absence does not mean it did not report.** Of the scanner's **5,489** US names, **4,914** are
  below the $40B band floor and therefore out of scope, **62** sit in the $40B-$50B band, **407**
  are at or above the $50B floor, and **106** carry no market cap at all.
- **Nine names print today and all nine are S&P 500 constituents** — Analog Devices, Medtronic,
  Dell, Autodesk, Workday, HP, Dollar Tree, Best Buy and J.M. Smucker. Ranked by reaction
  potential, not by size: **Dell (19.08)** leads on a 19.08% average move off its last four
  reports after a +20.46% day on Nov 23, then **Best Buy (8.17)**, **Dollar Tree (7.95)**,
  **Smucker (6.83)** and **Workday (5.25)**. Autodesk, Medtronic, Analog Devices and HP round
  the list out.
- **One important signal sits in the session, not on the calendar: Dell rose 20.46% on Nov 23
  and is +162.06% YTD.** A 19.08% average reaction on top of a 20% single-day move is the
  largest reaction potential on the board.
- **Two prints already landed before the 06:00 ET fire** — Valneva (01:00 ET) and Vipshop
  (05:00 ET) — both in the *Already reported* table.
- **One non-US issuer with a US line prints tonight**: Alimentation Couche-Tard (TSX: ATD,
  C$76.7B ≈ US$55B), results after the TSX close, US line OTC only.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DELL | Dell Technologies | AMC 4:05 PM | $6.77 | $50.63B | $212.94B | +20.46 | +162.06 | 19.08 | n/a | beat | 19.08 | pending | - |
| BBY | Best Buy | BMO 7:00 AM | $1.48 | $9.84B | $20.34B | -0.97 | +40.21 | 8.17 | n/a | beat | 8.17 | pending | - |
| DLTR | Dollar Tree | BMO 6:30 AM | $0.89 | $5.05B | $26.10B | +0.83 | +8.93 | 7.95 | n/a | beat | 7.95 | pending | - |
| SJM | J.M. Smucker | BMO 7:00 AM | $2.57 | $2.28B | $14.18B | -0.67 | +37.41 | 6.83 | n/a | beat | 6.83 | pending | - |
| WDAY | Workday | AMC 4:00 PM | $2.74 | $2.69B | $42.44B | +0.89 | -14.44 | 5.25 | n/a | beat | 5.25 | pending | - |
| ADSK | Autodesk | AMC 4:00 PM | $3.07 | $2.13B | $53.36B | +4.44 | -10.95 | 3.84 | n/a | beat | 3.84 | pending | - |
| MDT | Medtronic | BMO 6:45 AM | $1.34 | $9.46B | $128.84B | +0.78 | +4.86 | 3.75 | n/a | beat | 3.75 | pending | - |
| ADI | Analog Devices | BMO 7:00 AM | $3.89 | $4.32B | $183.53B | +9.49 | +38.36 | 3.18 | n/a | beat | 3.18 | pending | - |
| HPQ | HP Inc. | AMC 4:15 PM | $0.74 | $15.47B | $26.06B | +3.36 | +30.65 | 1.56 | n/a | beat | 1.56 | pending | - |

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|
| ATD.TO | Toronto Stock Exchange | Alimentation Couche-Tard Inc. | Nov 24, after the TSX close (16:00 ET) | ANCTF (OTC) | ADR (OTC) | pending |

_One issuer outside the standing 47-name non-US list qualifies on this date: Alimentation
Couche-Tard (C$76.7B, issuer-owned IR newsroom confirms its Q2 FY2027 results are released on
November 24, 2026 after the market close). Its US line is the OTC ordinary line only — it has
no NYSE or Nasdaq listing — so it is published here and not in the US tables. Every one of the
47 standing non-US candidates was checked across 15 market sweeps and none carries a release
date on this fire date._

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| CVE | Cenovus Energy | $47.88B | no |
| TEVA | Teva Pharmaceutical Industries | $46.65B | no |
| FNV | Franco-Nevada | $45.66B | no |
| WCN | Waste Connections | $45.42B | no |
| VIK | Viking Holdings | $44.45B | no |
| TRI | Thomson Reuters | $44.41B | no |
| FER | Ferrovial | $42.56B | no |
| NTRA | Natera | $42.40B | no |

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus | us_tradeable |
|---|---|---|---|---|---|
| VLA.PA (VALN) | Valneva SE | 01:00 ET (GlobeNewswire, Nov 24) | 9M-2026: total revenues €84.0M, product sales €81.4M, net loss €84.6M, adjusted EBITDA -€52.4M; 2026 guidance reaffirmed | not measured - the published consensus is a quarterly USD figure, not like-for-like with a nine-month IFRS number | US-listed |
| VIPS (NYSE ADS) | Vipshop Holdings Ltd | 05:00 ET (PR Newswire, Nov 24) | Q3-2026: net revenues RMB20.44B (US$3.05B), net income RMB1.09B (US$157.2M), special dividend US$0.73 per ADS | revenue in line - US$3.05B actual vs US$3.05B estimate; EPS not measured | ADR (US-listed) |

## Notes

- **Ranked by reaction potential**, not by market cap. DELL leads on a 19.08% mean absolute move
  across its last four reports, on a day after the stock jumped +20.46% (YTD +162.06%). BBY
  (8.17), DLTR (7.95), SJM (6.83) and WDAY (5.25) are the next tier; HPQ (1.56) is the quietest
  name on the board despite a $26.06B cap.
- **Every name's prior result is a beat.** All nine prior quarters beat consensus (sources:
  Yahoo `earningsHistory`, latest quarter-end 2026-07-31), so today's bar is a beat-after-beat
  setup — the beat rate does not distinguish the names, the reaction size does.
- **`Implied move %` is `n/a` on all nine rows.** Cboe's delayed-quote option chain
  (`cdn.cboe.com/api/global/delayed_quotes/options/`) answers a Cloudflare block from this
  egress, so no ATM straddle could be measured for any name. Per the contract the score
  substitutes `avg_abs_move` for the missing implied move, so **no row's reaction score is
  degraded** (`reaction_degraded: 0`) — but every score in this table is a historical-average
  score, not a market-implied one, and the implied-move half of the signal is missing for all
  nine names.
- **`avg_abs_move %` is a 4-event mean** (Nasdaq `earnings-surprise` report dates, Yahoo daily
  bars), measured over ADI's Aug 19 / May 20 / Feb 18 2025-Nov 25, DELL's Sep 1 / May 28 / Feb 26
  2025-Nov 25 and each name's three prior prints.
- **EPS basis differs by source and the spread is published, not hidden.** EarningsWhispers
  (Zacks-adjusted) vs Nasdaq/Zacks for the same names: **DELL $6.77 vs $6.55** (2.3%, and
  MarketBeat carries $6.62 — a >2% spread, so the disagreement is flagged rather than averaged
  away); **ADSK $3.07 vs $2.27** and **WDAY $2.74 vs $1.28** are GAAP-vs-adjusted basis
  differences, not estimate revisions. Every other name agrees to within 1 cent
  (ADI $3.89/$3.90, MDT $1.34/$1.33, HPQ $0.74/$0.75, DLTR $0.89/$0.91, BBY $1.48/$1.49,
  SJM $2.57/$2.56, WDAY $2.74/$2.74, ADSK $3.07/$3.07). This artifact publishes
  EarningsWhispers as the single EPS source and names the second source here.
- **Dell's date is confirmed on the issuer's own IR page**: `investors.delltechnologies.com`
  lists "Dell Technologies Fiscal Year 2027 Third Quarter Results — Nov 24, 2026 • 3:30 pm CST"
  (4:30 pm ET) and states results are issued before the call. The published 4:05 PM ET release
  stamp is EarningsWhispers', the call hour is the issuer's.
- **Every roster date is confirmed on two independent calendars.** EarningsWhispers ("is
  confirmed to report earnings on November 24, 2026", with BMO/AMC) and the Nasdaq earnings
  calendar (2026-11-24, `time-pre-market` / `time-after-hours`) agree on all nine names, and
  TradingView's release-date sweep over the US universe returns the same nine S&P 500 names.
  No row is published on a single aggregator's word.
- **Release times are EarningsWhispers'** (the per-name company pages): ADI 7:00 AM, MDT 6:45
  AM, DLTR 6:30 AM, BBY 7:00 AM, SJM 7:00 AM, ADSK 4:00 PM, WDAY 4:00 PM, HPQ 4:15 PM, DELL
  4:05 PM. TradingView stamps are placeholders (16:00/16:01 ET for every US name) and were not
  used.
- **Ticker convention (primary listing first):** a non-US issuer is shown on its primary
  listing with the US line in parentheses — `VLA.PA (VALN)`, `ATD.TO`. Vipshop has no listing
  outside the US, so `VIPS (NYSE ADS)` names the ADS directly.
- **Valneva is published as `US-listed`, not as an ADR.** Its Euronext Paris ordinary shares
  (VLA) are dual-listed on Nasdaq (VALN); TradingView types the Nasdaq line `dr`, but the
  security is the issuer's own share listing on Nasdaq, so it is published as a US-listed line.
  The Euronext Paris line is the primary listing and the headline ticker.
- **No watchlist section.** The published watchlist (`refs/watchlist.yaml`) fetched fine — AAPL,
  MSFT, NVDA, GOOGL, AMZN (earnings-flagged), plus IWM, GLD and TLT — and **none of them
  reports today**, so the section is omitted rather than shipped empty.
- **Every calendar hit that is not published is named here.** The EarningsWhispers calendar
  carried 38 rows and the TradingView US release-date sweep carried 56; the 26 sweep-only names
  (VFS, GGAL, DRVN, HUBG, MITK, HDL, AIV, IMPP, BNR, AREC, ICG, DAVA, ANTA, PSHG, GAUZ and
  preferred lines) and the 8 calendar-only names (BILI, MMED, TIGR, BWLP, BZUN, CMBT, FLX, ZH)
  are all below the $50B floor and none is an S&P 500 member — excluded on scope, not on
  judgement. 9 calendar rows were S&P 500 members and 4 cleared the $50B floor on their own
  (DELL, ADI, MDT, ADSK); the roster's 9 rows are the union.
- **Two large non-US reporters today are NOT in the non-US table, and the reason is structural.**
  **Compass Group** (LSE: CPG, ~$44B, H2 FY2026 results today per the Alliance News UK calendar)
  and **George Weston** (TSX: WN, C$42.4B, Nov 24) have **no US-listed line and no US peer**, so
  the table's `us_peer` contract cannot be filled for them — they are named here instead of being
  published in a form that would imply a tradable US security.
- **Alimentation Couche-Tard's US line is OTC only.** Its ordinary shares trade on the TSX (home
  listing, C$76.7B), Cboe Canada, Frankfurt and Mexico, with `ANCTF` as the US OTC line and no
  NYSE or Nasdaq listing — which is why it is absent from the TradingView `america` scanner
  universe, absent from the band table, and present in the non-US table instead.
- **The band is a lower bound on the excluded set.** Names below $40B are excluded by the band,
  not by the floor, and the per-day count of reporters below the band was not enumerated (it
  would need a market-cap pull for every calendar row, which does not fit the discovery
  cutoff). The band rows' caps are the scanner's issuer-level `market_cap_basic`; no Yahoo
  cross-check was possible because Yahoo's `v7/finance/quote` endpoint answers
  `Unauthorized` from this egress.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| EarningsWhispers calendar | `https://www.earningswhispers.com/calendar/20261124` | ok | server-rendered; 38 rows (26 before the open, 12 after the close), asserted against the page's own headline |
| EarningsWhispers company pages | `https://www.earningswhispers.com/stocks/<TICKER>` (JS cookie wall; token extracted from the wall and replayed) | ok | consensus EPS, revenue estimate and ET release time for all 9 roster names and for VALN/VIPS |
| Nasdaq earnings calendar | `https://api.nasdaq.com/api/calendar/earnings?date=2026-11-24` | ok | 50 rows; the independent second-source date and BMO/AMC confirmation for all 9 roster names |
| TradingView america scanner | `scanner.tradingview.com/america/scan` — `market_cap_basic` (issuer-level USD) | ok | 10,220 rows scanned; 5,489 US names after the `type in (stock, dr)` filter; caps for every calendar row and the whole band |
| TradingView per-market sweeps | `scanner.tradingview.com/<market>/scan` over `taiwan, japan, korea, hongkong, australia, canada, brazil, singapore, india, uk, germany, switzerland, france, spain, netherlands` | ok | the Pass B completeness check; 0 standing-list candidates stamped for 2026-11-24 |
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/<SYM>?interval=1d&range=2y` | ok | daily bars for prior-day %, YTD % and the 4-event reaction averages |
| Yahoo `v7/finance/quote` | `query1.finance.yahoo.com/v7/finance/quote` | degraded | answers `Unauthorized` from this egress; market caps are taken from the TradingView scanner instead, so the roster and the band share one source and one basis |
| Cboe delayed option chain | `cdn.cboe.com/api/global/delayed_quotes/options/<SYM>.json` | blocked | Cloudflare block from this egress; no ATM straddle could be measured, so `implied move %` is `n/a` on all 9 rows and the score substitutes `avg_abs_move` |
| Coverage floor (scope limit) | `scanner.tradingview.com/america/scan` — `market_cap_basic` (issuer-level USD), constants `MCAP_FLOOR = $50B` and `band_low_usd = $40B` | ok | The roster is bounded by the market-cap band, not by who reported: S&P 500 constituents plus US-listed names at or above $50B, with the $40B-$50B band published below the floor. A US reporter below $40B market cap is out of scope — it is not on this list (a scope limit, not a missing company). US names below the band floor: 4,914 of 5,489 (62 in the band, 407 at or above the floor, 106 with no cap) |
| Issuer IR pages | `investors.delltechnologies.com`, `corporate.couche-tard.com`, `ir.vip.com`, `valneva.com` | ok | Dell's Nov 24 event, Couche-Tard's Nov 24 after-close release, Vipshop's Nov 24 pre-open release and Valneva's Nov 24 results, each read on an issuer-owned page |

## Rules applied

- S&P 500 membership verified against the live constituent list - never from memory: the
  MediaWiki wikitext of `List_of_S&P_500_companies` parsed with all three symbol templates
  (`NyseSymbol`, `NasdaqSymbol`, `BZX link`), **503** symbols, with the control set
  `BRK.B`, `GOOGL`, `GOOG`, `FOX`, `CBOE` all present.
- Report dates confirmed against issuer or second-source pages before inclusion; every roster
  row is confirmed on EarningsWhispers **and** Nasdaq, and the highest-impact name (DELL) on
  its own IR page.
- The non-US issuer's own IR page outranks every aggregator - used for Valneva, Vipshop and
  Alimentation Couche-Tard.
- One row per issuer; a multi-class issuer carries the issuer-level market cap, and the
  non-common filter is applied in code over the scanner's descriptions, not by hand.
- Reaction columns computed from measured bars, past report dates and option chains; a value
  that could not be measured is published as `n/a` and named in the notes.
- Read-only reminder: no action is taken on any of these names.
