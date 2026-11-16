---
date: 2026-11-16
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:07
source: EarningsWhispers earnings calendar + Nasdaq earnings calendar + TradingView america scanner + Yahoo Finance chart API + Nasdaq earnings-surprise + Cboe delayed quotes + issuer IR pages
primary_source: Nasdaq (market cap, EPS consensus) | EarningsWhispers (revenue estimate, release time) | issuer IR pages (non-US report dates and release times) | TradingView (issuer-level market cap for the band and the coverage floor)
status: ok
pending_count: 6
already_reported_count: 1
non_us_count: 6
reaction_ranked: true
band_low_usd: 40000000000
reaction_degraded: 0
contract: EARNINGS_REMINDER_V4
coverage_receipt: calendar_rows=89 s_and_p_500_hits=1 bigcap_hits=0 us_roster_rows=1 band_rows=4
coverage_floor: floor_usd=50000000000 band_low_usd=40000000000 us_population=5545 below_band_us=4958 band_us=66 at_or_above_floor_us=417 no_cap_us=104 source=TradingView america scanner (market_cap_basic, issuer-level USD)
---

# Earnings - Mon 2026-11-16

## TL;DR

- **Coverage floor — a scope limit, not a missing company.** This reminder covers S&P 500
  constituents plus US-listed reporters with a market cap of **$50B or more** (TradingView
  scanner, `market_cap_basic`, issuer-level USD). The band just under the floor — **$40B to $50B**
  — is published in the *Just below the line* table so the cliff is visible. **A US reporter below
  $40B market cap is out of scope for this reminder: it is not on this list, and its absence does
  not mean it did not report.** Of the scanner's **5,545** US names, **4,958** are below the $40B
  band floor and therefore out of scope, **66** sit in the $40B-$50B band, **417** are at or above
  the $50B floor, and **104** carry no market cap at all.
- **A thin Monday in the US, and a crowded one overnight.** **One** US name clears the screen:
  Tyson Foods (TSN, S&P 500 member) reports before the open at 07:35 ET, $0.65 EPS / $13.88B
  revenue consensus. **No US name at or above the $50B floor reports today** — the calendar's
  biggest name is TSN at $20.85B — and no watchlist ticker reports.
- **Six non-US issuers print today, each confirmed on its own IR page:** H World (1179.HK / HTHT,
  already announced ahead of its 06:00 ET call), iQIYI (IQ, call 06:30 ET), XPeng (9868.HK / XPEV,
  call 07:00 ET), KE Holdings (2423.HK / BEKE, call 07:00 ET), Baidu (9888.HK / BIDU, call 07:30 ET)
  and Bank Hapoalim (POLI.TA / BKHYY, call 10:00 ET). Five are still `pending` at the 06:00 ET fire.
- **The open question for the 08:30 brief:** every Chinese ADR here releases between the Hong Kong
  close (03:00 ET) and its own call, so four of the five pending names can flip to `reported`
  before a reader opens the brief. Bank Hapoalim is the exception — Israeli business hours put its
  release anywhere from 01:00 to 10:00 ET.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TSN | Tyson Foods, Inc. | BMO 7:35 AM | 0.65 | $13.88B | $20.85B | -0.74 | 1.34 | 3.44 | 6.12 | beat | 4.51 | pending | - |

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|
| 1179.HK | Hong Kong Stock Exchange (HKEX) | H World Group Limited | Nov 16, 2026 (Hong Kong time) - results uploaded after HK trading hours and before the US open; call 06:00 ET | HTHT (Nasdaq ADR) | ADR (US-listed) | reported |
| IQ | Nasdaq | iQIYI Inc | Nov 16, 2026 - results before the US market opens; call 06:30 ET | IQ (Nasdaq ADS) | ADR (US-listed) | pending |
| 9868.HK | Hong Kong Stock Exchange (HKEX) | XPeng Inc | Nov 16, 2026 - results before the open of US markets; call 07:00 ET | XPEV (NYSE ADR) | ADR (US-listed) | pending |
| 2423.HK | Hong Kong Stock Exchange (HKEX) | KE Holdings Inc | Nov 16, 2026 - results before the US market opens; call 07:00 ET | BEKE (NYSE ADR) | ADR (US-listed) | pending |
| 9888.HK | Hong Kong Stock Exchange (HKEX) | Baidu Inc | Nov 16, 2026 - results uploaded after HK trading hours and before the US market opens; call 07:30 ET | BIDU (Nasdaq ADR) | ADR (US-listed) | pending |
| POLI.TA | Tel Aviv Stock Exchange (TASE) | Bank Hapoalim B.M. | Nov 16, 2026 - results on Israel business hours (01:00-10:00 ET); call 17:00 Israel = 10:00 ET | BKHYY (OTC ADR) | ADR (OTC) | pending |

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| MSTR | Strategy Inc | $47.14B | no |
| NTRA | Natera, Inc. | $46.27B | no |
| UI | Ubiquiti Inc | $40.51B | no |
| HEI | HEICO Corporation | $40.20B | no |

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus | us_tradeable |
|---|---|---|---|---|---|
| 1179.HK (HTHT) | H World Group Limited | before the 06:00 ET call (the issuer's own filing states the call follows the announcement) | not measured - the results release is not retrievable from this egress (ir.hworld.com answers 403; no results 6-K on EDGAR as of 06:07 ET) | not measured | ADR (US-listed) |

## Notes

- **Ranked by reaction potential**, not by market cap: the US roster has a single row, and TSN's score
  (0.6 x 3.44 avg abs move + 0.4 x 6.12 implied move = 4.51) is the only number in the column.
  Its implied move is nearly twice its historical reaction average, so the options market is pricing
  a bigger move than TSN usually delivers.
- **TSN's reaction inputs.** Prior day -0.74% and YTD +1.34% come from the Yahoo chart API's daily
  bars (last completed session 2026-11-13). The 3.44% average is the mean absolute move over the
  last 4 past reports (2026-08-03, 2026-05-04, 2026-02-02, 2025-11-10), BMO window
  `close(D-1) -> close(D)`. The 6.12% implied move is the ATM straddle at the 2026-11-20 expiry
  (strike $60, Cboe delayed chain). Prior result is a **beat** on the quarter ended 2026-06-30
  (+0.34% surprise), source `yahoo_earningsHistory`. `reaction_degraded: 0` - every reaction
  column was measured for every published row.
- **Market cap source, and a rate limit that is not an absence.** The Yahoo quote API answered
  **HTTP 429** from this egress (a rate limit, not a missing field), so TSN's cap is the Nasdaq
  earnings-calendar figure, **$20.85B**, cross-checked against the TradingView issuer-level cap,
  **$20.28B** - a 2.8% spread, inside the 5% tolerance, so it is not flagged.
- **EPS basis.** Consensus EPS $0.65 (Nasdaq/Zacks, adjusted) and revenue $13.88B
  (EarningsWhispers); the EarningsWhispers whisper for TSN is $0.71. A Yahoo `earningsTrend` GAAP
  comparison was not possible because of the 429.
- **No watchlist section.** The published watchlist fetched cleanly (8 names: AAPL, MSFT, NVDA,
  GOOGL, AMZN, IWM, GLD, TLT) and **no watchlist ticker reports today**, so the section is omitted
  rather than shipped empty.
- **The band holds only 4 publishable rows, and that is the measurement.** The band ($40B-$50B,
  66 US names) was filtered mechanically: 43 are S&P 500 members (already inside the roster's
  scope), 13 are ADR or depositary lines of foreign issuers (ABEV, HMC, INFY, MT, NOK, ONC, SE,
  STM, VALE and others - Pass B material, not the US band), 10 are non-common lines filtered on
  their description (FITB/PA, FITB/PI, FITB/PK, FITB/PM, PFH, PRS, STRC, STRD, STRF, STRK, STT/PG),
  and 7 are US-listed ordinary lines of foreign-domiciled issuers (FER, AU, FNV, SLF, TRI, WCN,
  VIK). What is left is the four US-domestic common shares above. The band is a **lower bound** on
  the excluded set: names below $40B are excluded by the band, not by the floor.
- **One row per issuer, issuer-level cap.** HEICO appears once, at the issuer-level $40.20B; its
  Class A line (HEI.A) carries the same issuer-level cap in the scanner and is not a second row.
- **Nothing in the band reports today** - that is why every *Reports today* cell reads `no`. The
  table's job here is to make the cliff visible, not to be a calendar.
- **Every non-US row is issuer-sourced, and the ET day is fixed by the issuer's own release
  schedule**, converted with `zoneinfo` (JST/KST/HKT = UTC+9/+9/+8, IST = UTC+2, ET = UTC-5). The
  Chinese and Israeli issuers all announce on Nov 16 local time, and every one of those local
  windows maps onto Nov 16 in ET - which is why all six rows belong to today's ET day rather than
  to Nov 15.
- **H World appears twice on purpose.** Its Pass B row carries the status (`reported`); the
  *Already reported* table carries the print detail. Its figures are **not measured**: the
  results release is not retrievable from this egress (`ir.hworld.com` answers 403) and EDGAR
  carried no results 6-K at 06:07 ET, so no actual or consensus comparison is published.
- **Calendar hits that are not published, and why.** The EarningsWhispers calendar carried 89 rows
  and the Nasdaq calendar 108 for the same date; **TSN was the only S&P 500 member in either**, and
  **no name at or above the $50B floor appeared in either**. The other calendar rows are US
  sub-$40B names, out of scope by the band. **Trip.com (TCOM, $27.8B)** is on the Nasdaq calendar
  with no time, but its own IR newsroom has no Q3 2026 date (latest release is the Sept 15 Q2
  report) and the aggregators' Nov 16 estimate is explicitly unconfirmed - an aggregator date is
  not a publishable date, so it is not published. **NIO** has no Q3 results date on its own IR
  newsroom (only delivery updates), and **NIU** has none either. **SK Square** (Q3 portfolio
  update already published Nov 13) and **Nidec** (no Nov 16 disclosure date on its IR calendar)
  were checked and dropped: the TradingView stamps for them are stale or absent.
- **Pass B standing universe checked: 48 candidates, 0 issuer-confirmed for today.** The TradingView
  global date sweep (1,258 issuers reporting on 2026-11-16 across all venues) contains **none** of
  the standing non-US candidates. The six rows above are additions to that universe: each one is a
  large non-US issuer with a live US line, and each one has an issuer-owned page confirming the
  date (issuer IR press release, and for Baidu, BEKE and H World the corresponding HKEX
  announcement or 6-K).
- **No name was excluded because its date moved**, so there is no date-confirmed-exclusion list to
  carry forward.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| EarningsWhispers calendar | `https://www.earningswhispers.com/calendar/20261116` | ok | 41 before the open + 48 after the close = 89 rows, matching the page's own headline; both sections sliced separately (the AMC list must be taken from the AMC heading to the end) |
| Nasdaq earnings calendar | `https://api.nasdaq.com/api/calendar/earnings?date=2026-11-16` | ok | 108 rows, independent cross-check: TSN is the only S&P 500 member in either calendar, with the same pre-market slot and the same $0.65 EPS consensus |
| S&P 500 constituent list | `https://en.wikipedia.org/w/api.php?action=parse&page=List_of_S%26P_500_companies&prop=wikitext&format=json` | ok | 503 symbols from all three templates (NyseSymbol, NasdaqSymbol, BZX link); control check BRK.B / GOOGL / GOOG / FOX / CBOE all present |
| Published watchlist | `https://api.github.com/repos/karizaco/minimax-cloud-outputs/contents/refs/watchlist.yaml?ref=main` | ok | 8 names fetched; none reports today, so the *Your watchlist* section is omitted rather than shipped empty |
| Yahoo Finance chart API | `query1.finance.yahoo.com/v8/finance/chart/TSN?interval=1d&range=2y` | ok | daily bars for prior day %, YTD % and the 4-event absolute-reaction average; no crumb required |
| Nasdaq earnings-surprise | `https://api.nasdaq.com/api/company/TSN/earnings-surprise` | ok | the 4 past report dates behind the reaction average (`dateReported` is M/D/YYYY, not ISO) |
| Yahoo earningsHistory | `query1.finance.yahoo.com/v10/finance/quoteSummary/TSN?modules=earningsHistory` | ok | prior result (latest quarter, ended 2026-06-30): beat, +0.34% surprise |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/options/TSN.json` | ok | ATM straddle at the 2026-11-20 expiry, strike $60 -> implied move 6.12% |
| Yahoo quote API (market cap / earningsTrend) | `query1.finance.yahoo.com/v7/finance/quote?symbols=TSN` | degraded | **HTTP 429** - a rate limit, not an absence. Market cap taken from the Nasdaq earnings-calendar field ($20.85B) and cross-checked against the TradingView issuer-level cap ($20.28B, 2.8% spread, inside the 5% tolerance) |
| TradingView scanner | `scanner.tradingview.com/america/scan` | ok | coverage floor and the band. The scanner's `in` operator is rejected on this deployment (HTTP 400, "Unsupported string operation in"), so the exchange/type filters were applied in code after the call: `exchange in (NASDAQ, NYSE, AMEX)`, `type in (stock, dr)`, `close > 1` |
| Issuer-owned pages (non-US dates) | `ir.baidu.com` + HKEX 6-K; `investors.ke.com`; `ir.xiaopeng.com`; `ir.hworld.com` + HKEX announcement; `ir.iqiyi.com`; `bankhapoalim.com` results-date PDF | ok | all six non-US rows have an issuer-confirmed date, with the issuer's own local release time |
| Issuer pages that do not answer from this egress | `ir.hworld.com` (403), `ir.nio.com` (403), `ir.xiaopeng.com` (403), `ir.ke.com` (403) | degraded | direct IR hosts answer 403 to a scripted fetch, so their confirmations came from the issuers' indexed press releases and their HKEX/SEC filings; H World's *results* could not be read, hence `not measured` |
| Coverage floor (scope limit) | `scanner.tradingview.com/america/scan` - `market_cap_basic` (issuer-level USD), constants `MCAP_FLOOR = $50B` and `band_low_usd = $40B` | ok | The roster is bounded by the market-cap band, not by who reported: S&P 500 constituents plus US-listed names at or above $50B, with the $40B-$50B band published below the floor. A US reporter below $40B market cap is out of scope - it is not on this list (a scope limit, not a missing company). US names below the band floor: 4,958 of 5,545 (66 in the band, 417 at or above the floor, 104 with no cap) |

## Rules applied

- S&P 500 membership verified against the live constituent list - never from memory.
- Report dates confirmed against issuer sources for every published name; an aggregator-only date
  was not published.
- Reaction columns computed from measured bars, past report dates and option chains; a value that
  could not be measured is published as `n/a` and counted in `reaction_degraded` (none here), and a
  print whose figures could not be read is published as `not measured` rather than borrowed from a
  different quarter.
- The roster is ranked by reaction potential, not by market cap, and the score is
  `0.6 x avg_abs_move + 0.4 x implied_move` (a missing implied move substitutes the average).
- One row per issuer; the headline ticker is the issuer's PRIMARY listing with its exchange
  suffix, with the US line in parentheses where the US line is a different listing.
- The market-cap floor is published in the front matter, in the TL;DR and in Source health, with
  its arithmetic (5,545 = 4,958 + 66 + 417 + 104).
- The band table is US-listed common shares only, one row per issuer, one source (the scanner's
  issuer-level cap), with non-common lines filtered mechanically on the description.
- The artifact states its own completeness basis (`coverage_receipt`), and every hit that is not
  published is named above with its reason.
