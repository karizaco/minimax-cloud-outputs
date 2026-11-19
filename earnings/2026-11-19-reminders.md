---
date: 2026-11-19
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:31
source: EarningsWhispers earnings calendar + TradingView america scanner + Yahoo Finance quoteSummary + Nasdaq earnings calendar
primary_source: EarningsWhispers (EPS est, revenue est, release time, confirmed report dates) | TradingView scanner (market cap, issuer-level USD) | Yahoo Finance quoteSummary (estimate cross-check) | Nasdaq earnings calendar (second EPS estimate)
status: ok
pending_count: 6
already_reported_count: 2
non_us_count: 2
reaction_ranked: true
band_low_usd: 40000000000
contract: EARNINGS_REMINDER_V4
coverage_receipt: calendar_rows=59 s_and_p_500_hits=5 bigcap_hits=6 us_roster_rows=6 band_rows=10
coverage_floor: floor_usd=50000000000 band_low_usd=40000000000 us_population=5512 below_band_us=4937 band_us=64 at_or_above_floor_us=408 no_cap_us=103 source=TradingView america scanner (market_cap_basic, issuer-level USD)
---

# Earnings - Thu 2026-11-19

## TL;DR

- **Coverage floor — a scope limit, not a missing company.** This reminder covers S&P 500
  constituents plus US-listed reporters with a market cap of **$50B or more** (TradingView
  scanner, `market_cap_basic`, issuer-level USD). The band just under the floor — **$40B to $50B**
  — is published in the *Just below the line* table so the cliff is visible. **A US reporter below
  $40B market cap is out of scope for this reminder: it is not on this list, and its absence does
  not mean it did not report.** Of the scanner's **5,512** US names, **4,937** are below the $40B
  band floor and therefore out of scope, **64** sit in the $40B-$50B band, **408** are at or above
  the $50B floor, and **103** carry no market cap at all.
- **Six names carry the US roster today** — two before the open (WMT, PDD) and four (WSM plus
  three after the close) on the scanner's clock, with WSM the third before-the-open name. The list
  is ranked by **reaction potential, not by size**: Keysight leads on a **9.76** reaction score (a
  9.99% typical move against a 9.41% implied move), Intuit second on **7.82**, Ross Stores on
  **7.60**. Walmart is the largest name on the list at $1,010.4B and ranks fifth on 6.09.
- **Two Hong Kong issuers already printed before this fire.** Alibaba (9988.HK / NYSE: BABA)
  released at **05:02 ET** and NetEase (9999.HK / NASDAQ: NTES) at **03:30 ET** — both before the
  06:00 ET snapshot, so both are in the *Already reported* table with their actuals. Alibaba beat
  on revenue (RMB271.52B vs RMB269.81B consensus) and **missed** on adjusted EPS per ADS (RMB8.10
  vs ~RMB10.75 expected); NetEase missed on both. Both ADRs are indicated lower in the
  pre-market prints.
- **The most likely mover is not the biggest name.** Keysight ($48.7B) is on this list because it
  is an S&P 500 constituent, not on size; Walmart and Alibaba are the two largest names in the
  day's coverage and neither leads the ranking.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KEYS | Keysight Technologies Inc. | AMC 4:05 PM ET | 3.36 | $1.94B | $48.74B | 0.65 | 38.58 | 9.99 | 9.41 | beat | 9.76 | pending | - |
| INTU | Intuit Inc. | AMC 4:00 PM ET | 2.47 | $4.30B | $83.71B | -2.35 | -50.24 | 7.75 | 7.93 | beat | 7.82 | pending | - |
| ROST | Ross Stores, Inc. | AMC 4:00 PM ET | 1.85 | $6.23B | $72.72B | 3.26 | 24.57 | 7.24 | 8.15 | beat | 7.60 | pending | - |
| PDD | PDD Holdings Inc. | BMO 6:30 AM ET | 2.78 | $17.30B | $110.24B | 0.08 | -33.09 | 5.95 | 6.45 | beat | 6.15 | pending | - |
| WMT | Walmart Inc. | BMO 7:00 AM ET | 0.64 | $186.52B | $1,010.44B | -0.13 | 12.95 | 6.07 | 6.12 | beat | 6.09 | pending | - |
| WSM | Williams-Sonoma, Inc. | BMO 8:00 AM ET | 2.18 | $1.98B | $30.63B | 4.02 | 38.46 | 3.02 | 7.42 | beat | 4.78 | pending | - |

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|
| 9988.HK | Hong Kong Stock Exchange | Alibaba Group Holding Limited | Nov 19, 2026, 18:02 HKT (05:02 ET) | BABA (NYSE ADR) | ADR (US-listed) | reported |
| 9999.HK | Hong Kong Stock Exchange | NetEase, Inc. | Nov 19, 2026, 16:30 HKT (03:30 ET) | NTES (Nasdaq ADS) | ADR (US-listed) | reported |

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| TEVA | Teva Pharmaceutical Industries Limited | $49.28B | no |
| CVE | Cenovus Energy Inc | $49.21B | no |
| FNV | Franco-Nevada Corporation | $45.79B | no |
| WCN | Waste Connections, Inc. | $45.53B | no |
| TRI | Thomson Reuters Corp | $45.04B | no |
| VIK | Viking Holdings Ltd | $44.41B | no |
| FER | Ferrovial N.V. | $43.48B | no |
| NTRA | Natera, Inc. | $41.98B | no |
| UI | Ubiquiti Inc. | $41.33B | no |
| AU | AngloGold Ashanti PLC | $40.14B | no |

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus | us_tradeable |
|---|---|---|---|---|---|
| 9988.HK (BABA) | Alibaba Group Holding Limited | Nov 19, 2026, 05:02 ET (18:02 HKT) | Revenue RMB271,519M (US$40,498M), +10% YoY; non-GAAP net income RMB19,909M (US$2,969M), +92% YoY; non-GAAP diluted EPS per ADS RMB8.10 (US$1.21); GAAP diluted EPS per ADS RMB25.94 (US$3.87) | revenue beat — RMB271.52B vs RMB269.81B LSEG consensus (RMB270.53B Bloomberg); adjusted EPS per ADS miss — RMB8.10 vs ~RMB10.75 expected | ADR (US-listed) |
| 9999.HK (NTES) | NetEase, Inc. | Nov 19, 2026, 03:30 ET (16:30 HKT) | Net revenues RMB27,852.4M (US$4,154.3M), -1.8% YoY; non-GAAP net income RMB9,163.6M (US$1,366.8M); non-GAAP diluted EPS RMB14.21 (US$2.12) per ADS; GAAP diluted EPS US$1.94 per ADS | miss on both — revenue RMB27.85B vs ~RMB30.27B consensus; non-GAAP EPS per ADS US$2.12 vs US$2.49 expected | ADR (US-listed) |

## Notes

- **Ranked by reaction potential, not by market cap.** Keysight (9.76), Intuit (7.82) and Ross
  Stores (7.60) lead the roster on typical and implied reaction size, not on size; Walmart
  ($1,010.4B) and PDD ($110.2B) sit fifth and fourth. Every reaction column is measured and
  `reaction_degraded` is absent because no row was degraded: all six rows carry a prior-day move, a
  YTD move, a 4-event average absolute move (Nasdaq `earnings-surprise` report dates plus Yahoo
  daily bars), a Cboe ATM implied move at the 2026-11-20 expiry, and a prior result from Yahoo
  `earningsHistory`.
- **The Cboe chain has no 2026-11-19 expiry, so every implied move is taken at the 2026-11-20
  expiry** — the first expiry that straddles the event for both the before-the-open and the
  after-the-close names. The WMT chain's listed expiries run 261120, 261127, 261204, 261211,
  261218 and out; 261119 does not exist, so the definition ("the first expiry that straddles the
  event"), not "the expiry on the report date", is what governs.
- **Keysight is on the list as an S&P 500 constituent, not on its cap.** At $48.74B it is below the
  $50B floor, so it carries no `boundary_case` flag (that flag marks names inside the floor by less
  than $0.5B); it is in scope because index membership overrides the cap. Williams-Sonoma
  ($30.63B) is on the same basis.
- **Release times are EarningsWhispers' confirmed slots, cross-checked against the issuers'
  own announcements.** Walmart's own IR page carries the FY2027 Q3 release on November 19 with a
  6 a.m. CT release and a 7 a.m. CT call (= 7:00 a.m. ET release); Williams-Sonoma's release
  notice says "before the market opens" on November 19 with a 10:00 a.m. ET call; Intuit's release
  is "following the close of market" on November 19 with a 4:30 p.m. ET call; Ross Stores' release
  notice says "approximately 4:00 p.m. Eastern time" on November 19 with a 4:15 p.m. ET call;
  Keysight's release is "after the close of the stock market" on November 19 with a 4:30 p.m. ET
  call; PDD's own notice says it reports "before U.S. markets open" on November 19 with a 7:30
  a.m. ET call. TradingView's stamps are placeholders and were not used for any published time.
- **Estimate source, and two spreads worth naming.** EPS and revenue estimates are
  **EarningsWhispers'** — the one source that is in USD for every name including the Chinese ADRs,
  which Yahoo's `earningsTrend` is not (it returns PDD in RMB: EPS 18.84 and revenue RMB115.51B).
  Two published EPS figures differ from a second source by more than the 2% tolerance:
  **INTU 2.47 (EarningsWhispers, Nasdaq) vs Yahoo 2.64**, and **KEYS 3.36 (EarningsWhispers,
  Yahoo) vs Nasdaq 3.09** — different bases rather than one being wrong. For PDD the two second
  sources also disagree: **EW 2.78 vs Nasdaq 2.61**. Market caps are the scanner's issuer-level
  USD figures; Yahoo's `v7/finance/quote` worked this fire and agrees with the scanner within
  0.9% on all six roster names (largest spread: WMT 1,013.5B vs 1,010.4B).
- **Prior result on Williams-Sonoma is a beat, and one aggregator labels it a miss.** Yahoo
  `earningsHistory`, Zacks ($2.10 vs $2.05), MarketBeat ($2.10 vs $2.08) and TIPRanks ($2.10 vs
  $2.07) all show a beat on the August 26 quarter; EarningsWhispers' own history headline labels
  that print "Missed Expectations". The published verdict follows the four sources that show a
  beat, on the adjusted basis.
- **Alibaba's GAAP EPS per ADS (US$3.87) is not comparable to consensus.** It is inflated by net
  investment gains; the adjusted figure (US$1.21) is the like-for-like number against the
  ~RMB10.75 expected. Alibaba also beat on revenue (LSEG RMB269.81B, Bloomberg RMB270.53B) while
  its adjusted EPS missed by roughly a quarter — the revenue beat and the EPS miss are both in the
  release.
- **Pre-market reaction, indicative only.** Yahoo's 5-minute bars show BABA at ~$83.30 against a
  $86.65 prior close (about -3.9%) and NTES at ~$111.92 against $119.62 (about -6.4%) around
  06:20 ET. Yahoo reports zero volume on pre-market bars, so these are indicative prints, not
  traded quotes.
- **Alibaba and NetEase are excluded from the US roster on purpose.** Both issuers' primary
  listings are in Hong Kong, so their headline tickers are `9988.HK` and `9999.HK` with the US
  line in parentheses — the Non-US table's shape, not the US roster's. They are counted as
  big-cap hits in the coverage receipt and published in the two tables above.
- **Ticker convention (primary listing first):** ADR and OTC lines are shown on the issuer's
  PRIMARY listing with its exchange suffix, with the US line in parentheses — `9988.HK (BABA)`,
  `9999.HK (NTES)`.
- **Coverage receipt, accounted for row by row.** The calendar carried **59** rows (39 before the
  open, 20 after the close, matching the page's own headline) and the Nasdaq calendar carried 63
  rows for the same date. **5** of those rows were S&P 500 constituents (WMT, WSM, ROST, INTU,
  KEYS) and **6** cleared the $50B floor (those four plus PDD and BABA, with NTES as a sixth
  big-cap line). All 5 index hits are published in the roster; the one big-cap hit that is not in
  the roster is BABA, a non-US issuer published in the non-US and already-reported tables. The
  remaining **53** calendar rows are out of scope: 17 of them are not US-exchange lines at all
  (EVGN, SUBCY, ARBE, ATKR, ECDA, KDOZF, LBLCF, NILIF, T.REA, V.CEI, V.DWS, V.NIL, EARN, GRSD,
  LEEF, NTAR, PKK) and the rest are below the floor without being index members — the largest is
  **WMG at $17.2B**, then FUTU at $11.7B.
- **Three independent feeds agree on the day's coverage.** The scanner's own date sweep surfaced 67
  US names stamped 2026-11-19; after removing the preferred and depositary lines it carries, its
  index members are the same five and its ≥$50B names the same six as the calendar feeds. No name
  appears on one feed and not the others.
- **Overnight non-US prints outside this scope, named rather than dropped.** Sompo Holdings
  (TSE: 8630) reported at 01:30 ET on November 19 per its own investor calendar — this is the name
  yesterday's brief excluded as the wrong-date trap, and it is today's ET day; it is below the $50B
  floor, is not an index member and is not on the standing Pass B list, so it is not published.
  Lenovo (0992.HK), Kuaishou (1024.HK), Tokio Marine (8766.T), MS&AD (8725.T) and Halma (HLMA.L)
  also reported on November 19 and are outside this reminder's scope for the same reasons.
  Loblaw (TSX: L) reports November 19; its US line is an OTC line, not a US-exchange listing, so
  it is out of scope as well.
- **The per-day count of reporters below the $40B band was not enumerated.** That would need a
  market-cap pull for every calendar row and does not fit the run budget; the population counts
  above are the measured decomposition of the scanner's US universe, and nothing here is estimated.
- **No watchlist section.** The published watchlist was fetched successfully (8 tickers: AAPL,
  MSFT, NVDA, GOOGL, AMZN, IWM, GLD, TLP), but **none of them reports today**, so the section is
  omitted rather than shipped empty.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| EarningsWhispers calendar (roster) | `https://www.earningswhispers.com/calendar/20261119` | ok | server-rendered; 39 before the open and 20 after the close, matching the page's own headline; 59 rows |
| EarningsWhispers company pages (estimates, times) | `https://www.earningswhispers.com/stocks/<TICKER>` | ok | consensus EPS, Rev est and the confirmed slot for all six roster names and both ADR prints; all read "confirmed to report earnings on November 19, 2026" |
| Nasdaq earnings calendar | `https://api.nasdaq.com/api/calendar/earnings?date=2026-11-19` | ok | 63 rows; independent confirmation of BMO/AMC and a second EPS estimate for the six roster names |
| TradingView america scanner (universe sweep + caps) | `https://scanner.tradingview.com/america/scan` | ok | one full sweep (10,225 rows, totalCount 10,225) filtered to `type in (stock, dr)` = 5,512 US names, plus one date sweep (67 names stamped 2026-11-19); issuer-level USD market caps for the roster and the band |
| Coverage floor (scope limit) | `scanner.tradingview.com/america/scan` - `market_cap_basic` (issuer-level USD), constants `MCAP_FLOOR = $50B` and `band_low_usd = $40B` | ok | The roster is bounded by the market-cap band, not by who reported: S&P 500 constituents plus US-listed names at or above $50B, with the $40B-$50B band published below the floor. A US reporter below $40B market cap is out of scope - it is not on this list (a scope limit, not a missing company). US names below the band floor: 4,937 of 5,512 (64 in the band, 408 at or above the floor, 103 with no cap) |
| Yahoo Finance quoteSummary (EPS + revenue estimates) | `https://query1.finance.yahoo.com/v10/finance/quoteSummary/<TICKER>?modules=earningsTrend` | ok | cookie+crumb handshake (jar seeded from fc.yahoo.com); the estimate cross-check, and the prior result from `earningsHistory` |
| Yahoo Finance v7 quote (market cap) | `https://query1.finance.yahoo.com/v7/finance/quote` | ok | worked this fire with the seeded jar + crumb; agrees with the scanner's issuer-level caps within 0.9% on all six roster names, so the scanner remains the published source for the caps and the band order |
| Yahoo Finance chart API (reaction bars, pre-market prints) | `https://query1.finance.yahoo.com/v8/finance/chart/<SYM>` | ok | daily bars for the prior-day move, the YTD move and the 4-event average absolute move; 5-minute pre-market bars for the two ADR prints (indicative — zero volume) |
| Nasdaq earnings-surprise (past report dates) | `https://api.nasdaq.com/api/company/<SYM>/earnings-surprise` | ok | the four past report dates behind each average absolute move |
| Cboe delayed-quote option chain | `https://cdn.cboe.com/api/global/delayed_quotes/options/<SYM>.json` | ok | ATM straddle at the 2026-11-20 expiry for the implied move; the chain carries no 2026-11-19 expiry |
| Walmart investor relations (issuer confirmation) | `https://corporate.walmart.com/news/events/fy2027-q3-earnings-release` | ok | issuer-owned page: FY2027 Q3 release on November 19, 2026, 6 a.m. CT release and 7 a.m. CT call |
| Williams-Sonoma investor relations (issuer confirmation) | `https://ir.williams-sonomainc.com/investor-information/news-releases/news-release-details/2026/Williams-Sonoma-Inc--announces-release-date-for-third-quarter-results-Thursday-November-19th-2026/default.aspx` | ok | issuer-owned release: results before the market open on November 19, 2026, conference call 10:00 a.m. ET |
| Intuit investor relations (issuer confirmation) | `https://investors.intuit.com/news-events/press-releases/detail/1330/intuit-to-announce-first-quarter-fiscal-year-2027-results-on-nov-19` | ok | issuer-owned release: first-quarter fiscal 2027 results on November 19 following the close of market; call 4:30 p.m. ET |
| Ross Stores investor relations (issuer confirmation) | `https://investors.rossstores.com/news-releases/news-release-details/ross-stores-inc-announces-third-quarter-2026-earnings-release` | ok | issuer-owned release: third-quarter 2026 results on November 19, 2026 at approximately 4:00 p.m. ET; call 4:15 p.m. ET |
| Keysight Technologies investor relations (issuer confirmation) | `https://investor.keysight.com/investor-news-and-events/financial-press-releases/press-release-details/2026/Keysight-Technologies-to-Report-Fourth-Quarter-and-Fiscal-Year-2026-Results-on-November-19-2026/default.aspx` | ok | issuer-owned release: fiscal Q4 and FY2026 results after the close of market on November 19, 2026; call 4:30 p.m. ET |
| PDD Holdings investor relations (issuer confirmation) | `https://investor.pddholdings.com/news-releases/` | ok | issuer-owned release: third-quarter 2026 results before U.S. markets open on November 19, 2026; call 7:30 a.m. ET |
| Alibaba Group investor relations + results release (issuer confirmation and actuals) | `https://www.alibabagroup.com/en-US/document-2054756418245885952` and the September Quarter 2026 results announcement (HKEX filing, `hkexnews.hk`) | ok | issuer-owned: results before the U.S. market opens on November 19, 2026, call 7:00 a.m. ET; the results release carried a 05:02 ET publication stamp (US$ translations at CNY6.7045) |
| NetEase investor relations + HKEX filing (issuer confirmation and actuals) | `https://ir.netease.com/news-releases/news-release-details/netease-report-third-quarter-2026-financial-results-november-19` and the HKEX board-meeting announcement | ok | issuer-owned: third-quarter 2026 results on November 19, 2026 before the U.S. market opens, call 7:00 a.m. ET; the results release carried a 03:30 ET publication stamp |
| S&P 500 constituent list (Rule A) | MediaWiki wikitext for `List of S%26P 500 companies` | ok | 503 symbols parsed from all three templates (NyseSymbol, NasdaqSymbol, BZX link); control check BRK.B, GOOGL, GOOG, FOX, CBOE all present |
| Published watchlist | `https://api.github.com/repos/karizaco/minimax-cloud-outputs/contents/refs/watchlist.yaml` | ok | fetched; 8 tickers, none reporting today, so no watchlist section is published |

## Rules applied

- S&P 500 membership verified against the live constituent list - never from memory. 503 symbols
  parsed from all three symbol templates, with the BRK.B / GOOGL / GOOG / FOX / CBOE control
  check passed.
- Report dates confirmed against issuer sources for every name on the roster, and both non-US
  prints carry their issuer's own release (Alibaba's and NetEase's own IR pages and, for
  NetEase, the HKEX board-meeting announcement).
- Reaction columns computed from measured bars, past report dates and option chains. A value that
  could not be measured is published as `n/a` and counted in `reaction_degraded`; nothing was
  degraded on this fire, so the key is absent.
- The roster is ranked by reaction potential, not by market cap, and every published row carries
  the six reaction columns.
- The market-cap floor is published with what it excludes, in three places - the front matter,
  the `## TL;DR` and the `## Source health` - and the counts add up
  (5,512 = 4,937 + 64 + 408 + 103).
- The band table is US-exchange-listed common shares only, one row per issuer, one source for the
  caps and the order, with non-common lines filtered mechanically on the description and
  depositary lines (INFY, ONC, MT, HMC, ABEV, SE, NOK) excluded - they are the foreign issuers'
  ADR lines, which belong to the non-US universe rather than this band.
- The non-US table and the already-reported table carry a `us_tradeable` cell for every row, and
  the ticker cell is the primary listing with the US line in parentheses.
