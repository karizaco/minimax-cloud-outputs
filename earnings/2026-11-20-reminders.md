---
date: 2026-11-20
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 11:45
snapshot_date: 2026-11-21
source: EarningsWhispers earnings calendar + Nasdaq earnings calendar + Yahoo Finance earnings calendar + TradingView america scanner
primary_source: EarningsWhispers (day's roster, 12 rows) | TradingView america scanner (issuer-level market caps and the coverage floor) | issuer and wire releases (release instants and actuals)
status: ok
pending_count: 0
already_reported_count: 2
non_us_count: 0
reaction_ranked: true
reaction_degraded: 0
degraded_sources: 1
band_low_usd: 40000000000
contract: EARNINGS_REMINDER_V4
coverage_receipt: calendar_rows=12 s_and_p_500_hits=0 bigcap_hits=0 us_roster_rows=0 band_rows=10
coverage_floor: floor_usd=50000000000 band_low_usd=40000000000 us_population=5498 below_band_us=4925 band_us=65 at_or_above_floor_us=405 no_cap_us=103 source=TradingView america scanner (market_cap_basic, issuer-level USD)
---

# Earnings - Fri 2026-11-20

## TL;DR

- **Coverage floor — a scope limit, not a missing company.** This reminder covers S&P 500
  constituents plus US-listed reporters with a market cap of **$50B or more** (TradingView
  scanner, `market_cap_basic`, issuer-level USD). The band just under the floor — **$40B to $50B**
  — is published in the *Just below the line* table so the cliff is visible. **A US reporter below
  $40B market cap is out of scope for this reminder: it is not on this list, and its absence does
  not mean it did not report.** Of the scanner's **5,498** US names, **4,925** are below the $40B
  band floor and therefore out of scope, **65** sit in the $40B-$50B band, **405** are at or above
  the $50B floor, and **103** carry no market cap at all.
- **The roster is empty, and the floor is what empties it.** No S&P 500 constituent and no
  US-listed name at or above $50B reports on Friday, November 20, 2026. The biggest name on any
  of the day's calendars is Bending Spoons (BSP) at **$29.7B**, a Nasdaq listing below the $40B
  band floor; the biggest US print of the day was BJ's Wholesale Club at **$14.0B**. All ten band
  names answer "no".
- **Two prints crossed before this 06:00 ET fire, and only two.** Frontline (NYSE: FRO) at
  **01:30 ET** and RLX Technology (NYSE: RLX) at **04:30 ET** — both are in the *Already
  reported* table with their actuals. Every other US release that day landed after the fire:
  BitFuFu 06:30 ET, BJ's 06:45 ET, Buckle 06:45 ET, Moog 06:50 ET, IES Holdings 07:45 ET.
- **Frontline beat on revenue and split on EPS; RLX missed on EPS.** FRO: revenues **$921.3M**
  (+113% YoY) against a $717.4M consensus, adjusted EPS **$2.38** against Yahoo's $2.26 — but
  against FactSet's $2.64 it is a miss. RLX: US GAAP diluted **CNY 0.123** (US$0.018) per ADS
  against the only published estimate, CNY 0.23.
- **This brief was produced on 2026-11-21 at 11:45 ET, about 29 hours after its 06:00 ET fire on
  November 20.** The screen is complete for its date, but every price below is the settled Friday
  November 20 close, not a 06:00 ET pre-market print, and the release instants are the issuers'
  own timestamps rather than readings taken at the fire.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

_No row: no S&P 500 constituent and no US-listed name at or above the $50B floor reports on
2026-11-20. The day's coverage was not thin — EarningsWhispers carried 12 rows (11 before the
open, 1 after the close, matching the page's own headline), Nasdaq carried 39, and the scanner's
own date sweep stamped 41 US names for that date — but not one of the 41 is an S&P 500
constituent and not one clears $50B. The largest name in the day's coverage is Bending Spoons
(BSP) at $29.7B; the largest US print was BJ's Wholesale Club at $14.0B. The reaction layer has
no row to rank, so there is no reaction score to publish; `reaction_degraded` is 0 because
nothing was degraded — there was nothing to degrade._

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|

_No row: no issuer on the standing Pass B candidate list has an issuer-confirmed report date on
2026-11-20. The per-market date sweep across 33 exchanges carried 435 names stamped for that
date and none of them is a standing candidate — the only keyword match was FIBRA Macquarie
Mexico, a Mexican trust that is not Macquarie Group and is not on the list. CTBC Financial
Holding (2891.TW) is the one name in midgard's S&P 500 / STOXX coverage stamped for November 20;
it is a Taiwan listing whose US line is OTC, far below the $50B floor and not on the standing
list, so it is named in the notes rather than published here._

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| MDLN | Medline Inc. | $49.78B | no |
| CVE | Cenovus Energy Inc | $49.09B | no |
| WCN | Waste Connections, Inc. | $45.14B | no |
| TEVA | Teva Pharmaceutical Industries Limited | $44.97B | no |
| FNV | Franco-Nevada Corporation | $44.53B | no |
| TRI | Thomson Reuters Corp | $43.58B | no |
| FER | Ferrovial N.V. | $42.15B | no |
| NTRA | Natera, Inc. | $42.04B | no |
| VIK | Viking Holdings Ltd | $42.03B | no |
| UI | Ubiquiti Inc. | $40.11B | no |

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus | us_tradeable |
|---|---|---|---|---|---|
| FRO (NYSE, primary; Oslo: FRO.OL) | Frontline plc | Nov 20, 2026, 01:30 ET (07:30 CET) | Profit $641.4M, $2.88 per share; adjusted profit $530.9M, $2.38 per share; revenues $921.3M (+113% YoY); TCE earnings $703.9M (against $753.3M in Q2); spot TCE $148,500/d VLCC, $102,500/d Suezmax, $67,800/d LR2/Aframax; dividend $2.38 per share | revenue beat — $921.3M against Yahoo's $717.4M four-analyst consensus (range $658.0M-$780.2M); adjusted EPS $2.38 beat Yahoo's $2.26 (range $2.21-$2.37) but missed FactSet's $2.64 — the two bases differ by 17% | US-listed |
| RLX (NYSE ADS, primary) | RLX Technology Inc. | Nov 20, 2026, 04:30 ET | Net revenues RMB1,916.6M (US$285.9M), +69.7% YoY; gross profit RMB446.6M (US$66.6M), margin 23.3% against 31.2%; US GAAP net income RMB147.1M (US$21.9M); non-GAAP net income RMB235.6M (US$35.1M); GAAP diluted EPS RMB0.123 (US$0.018) per ADS; non-GAAP diluted RMB0.175 (US$0.026) | miss on both bases — the only published estimate is Yahoo's calendar figure of CNY 0.23 per ADS and the issuer reports in CNY, so GAAP diluted CNY 0.123 and non-GAAP CNY 0.175 both sit below it; no second source carries a consensus and Yahoo's estimate series for RLX is one analyst wide | ADR (US-listed) |

## Notes

- **Coverage receipt, accounted for row by row.** The calendar carried **12** rows (11 before the
  open, 1 after the close, matching EarningsWhispers' own headline) and Nasdaq carried **39** rows
  for the same date; Yahoo's calendar rendered **7** server-side rows (BJ, BKE, RLX, WRD, FUFU,
  DLNG, KPTI) and its offset pagination returns no further rows, so it was used as a cross-check
  only. **0** of those rows is an S&P 500 constituent and **0** clears the $50B floor. The largest
  are BSP $29.7B, BJ $14.0B, MOG $10.6B, FRO $9.9B, KT $8.5B, IESC $6.8B, BKE $2.2B, RLX $1.8B and
  WRD $1.2B; the other 29 Nasdaq rows are below $0.1B.
- **Two prints before the fire, each on a timestamped release.** FRO: Euronext's own company-news
  page carries the Oslo Børs announcement the issuer is obliged to publish, stamped "20 Nov 2026
  07:30 CET" = 01:30 ET — before the Oslo open and four and a half hours before this fire. RLX:
  the PR Newswire release carries "Nov 20, 2026, 04:30 ET". A date with no release hour is not
  publishable (Metro Inc and Golar LNG on 2026-11-18 were named instead), so no other name is
  claimed as pre-fire.
- **Every other US release that day landed after the fire**, on the issuer's or the wire's own
  stamp: BitFuFu 06:30 ET (GlobeNewswire), BJ's 06:45 ET (Business Wire), Buckle 06:45 ET
  (Business Wire; MT Newswires wrote it up at 07:11 ET), Moog 06:50 ET (Business Wire), IES
  Holdings 07:45 ET (GlobeNewswire). RLX's own call was at 07:00 ET and Frontline's at 09:00 ET.
- **The prints that came after the fire, with their actuals and their settled moves.** **BJ's
  Wholesale Club** ($14.0B, 06:45 ET): diluted EPS $1.73 — the same on an adjusted basis, there
  were no adjustments — against Nasdaq's $1.24 and Yahoo's $1.26, a beat on both; net sales
  $6,145.1M (+17.6% YoY), comparable club sales +13.5%, adjusted EBITDA $421.6M; closed $104.82,
  **-5.35%**. **Moog** ($10.6B, 06:50 ET): fiscal Q4 sales $1.3B (+20%), adjusted EPS $3.37
  against Nasdaq's $2.70, fiscal-year sales $4.5B (+17%), fiscal-year adjusted EPS $12.36 (+42%),
  free cash flow $307M, and another strong year guided for fiscal 2027; closed $334.47, **+1.95%**
  (MOG.A) and $338.56, **+1.86%** (MOG.B). **IES Holdings** ($6.8B, 07:45 ET): fiscal Q4 revenue
  $1,390.0M (+55%), operating income $217.2M (+108%), diluted EPS $4.50 and adjusted diluted EPS
  $4.07, fiscal-year revenue $4,477.9M (+33%), fiscal-year diluted EPS $13.24, and an extra
  $350M authorised for the buyback; closed $156.06, **-6.49%**. **Buckle** ($2.2B, 06:45 ET):
  diluted EPS $0.94 against FactSet's $0.87 and Yahoo's $0.84, a beat; net sales $329.2M (+2.6%),
  comparable sales +0.6%; closed $44.15, **+5.67%**. **WeRide** ($1.2B ADR): revenue RMB321.5M
  (US$48.0M, +88.0% YoY), gross margin 43.0% against 32.9%, loss per ADS RMB0.96 (US$0.15)
  against the CNY 0.99 loss Yahoo carried — a smaller loss; closed $2.985, **-8.58%**.
  **BitFuFu** ($0.14B ADR): revenue $37.7M (-79.1%), net income $24.9M, diluted EPS $0.14
  against Yahoo's $0.03; closed $0.88, **+2.33%**. **Dynagas LNG** (after the close, $0.11B) and
  **Karyopharm** (after the close, $0.03B) are far below the floor; Karyopharm closed **-26.25%**.
- **Frontline's two lines tell one story.** NYSE: FRO closed $45.21, **+1.03%**; Oslo: FRO.OL
  closed NOK 442.60, **+2.12%**. The Oslo session runs before the New York one, so its close is
  the earlier print; the release crossed at 07:30 CET, before the Oslo open.
- **The calendar's `VK — VIKING THERAPEUTICS` row is a ticker collision, and it points both ways.**
  `VK` on Euronext Paris is Vallourec, whose own release (Meudon, November 20, 2026) reported Q3
  2026 — group EBITDA $181M (-26% YoY, 18.9% margin) with Q4 guided to $170M-$210M — and whose
  sponsored Level 1 ADR (VLOWY; the release states the parity at five ADRs to one ordinary
  share) closed $3.38, **-14.65%**. Viking Therapeutics trades as VKTX on Nasdaq and last
  reported before this date (it closed $24.77, -4.14% on November 20 with no print), and Viking
  Holdings (VIK, NYSE) reported on **November 17** at 07:00 ET on its own IR page and its 6-K, so
  its November 20 close of $94.02 (-1.03%) is not a reaction. Vallourec is below the floor, its US
  line is OTC and it is not on the standing Pass B list, so it is named and not published.
- **All ten band names answer "no", and it was checked three ways.** Each one's next-release stamp
  falls in February or March 2027, none appears on any of the three calendars, and EDGAR carries
  no results-type filing (8-K, 10-Q, 10-K, 20-F, 40-F) for any of them on November 19 or 20.
- **How the band was cut from the 65 raw rows.** The 65 rows in the $40B-$50B band decompose
  exactly: **7** depositary lines (INFY, ONC, MT, NOK, HMC, ABEV, STM — foreign issuers' ADR
  lines, which belong to the non-US universe), **7** non-common-share descriptions (FITB/PM,
  FITB/PI, FITB/PK, FITB/PA, STT/PG, PFH, PRS), **41** S&P 500 members (index membership
  overrides the cap and puts a name on the roster instead of the band) and the **10** published
  above.
- **Just under the band floor**, the nearest names are Paychex $39.66B, Haleon $39.23B, Sea Limited
  $39.23B, Vale $39.18B and Take-Two $39.06B — all out of scope on the same rule.
- **Estimates: one source per name, with the spread named rather than averaged.** Yahoo's
  `earningsTrend` has already rolled past the quarters that reported on November 20 (BJ's 0q now
  points at 2027-01-31), so the consensus used here is the figure the calendars carried for the
  day, with FactSet and MT Newswires as a second source where they published one. The two bases
  disagree for FRO ($2.26 on Yahoo, $2.64 on FactSet, and Yahoo's series is on the adjusted basis
  — its year-ago EPS of 0.19 is Frontline's adjusted Q3 2025 figure, not the reported 0.18) and
  both are published.
- **Market caps: the scanner is the source, cross-checked in a second source and, for Frontline,
  in shares.** Yahoo's `v7/finance/quote` carried the same issuer-level caps; the widest spread
  across the ten band names is Ferrovial (Yahoo $42.40B against the scanner's $42.15B, 0.6%).
  Frontline's scanner cap of $9.96B reconciles with the issuer's own count of 222,622,889
  ordinary shares at the November 19 close of $44.75.
- **No watchlist section.** The published watchlist fetched successfully (8 tickers: AAPL, MSFT,
  NVDA, GOOGL, AMZN, IWM, GLD, TLT) and **none of them reports today** — the five earnings-flagged
  names' next releases fall between 2027-01-26 and 2027-02-24 — so the section is omitted rather
  than shipped empty.
- **This run was suspended mid-way and resumed late; no data source failed.** The session was
  suspended after the discovery phase and resumed on 2026-11-21 at 11:0x ET, about 29 hours after
  the 06:00 ET fire, so this brief is a reconstruction of the November 20 ET day built on settled
  closes and on the issuers' own release timestamps rather than on a reading taken at the fire.
  That is the one degradation this run carries (`degraded_sources: 1`); every source answered.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| EarningsWhispers calendar (roster) | `https://www.earningswhispers.com/calendar/20261120` | ok | server-rendered; 11 before the open and 1 after the close, matching the page's own headline; 12 rows |
| Nasdaq earnings calendar | `https://api.nasdaq.com/api/calendar/earnings?date=2026-11-20` | ok | 39 rows; independent confirmation of BMO/AMC and a second EPS estimate for BJ, MOG and BSP |
| Yahoo Finance earnings calendar | `https://finance.yahoo.com/calendar/earnings?day=2026-11-20` | ok | JS-rendered; 7 server-side rows (BJ, BKE, RLX, WRD, FUFU, DLNG, KPTI) and offset pagination 0/7/14/21 returns no new rows, so it was used as a cross-check only |
| TradingView america scanner (universe sweep + caps) | `https://scanner.tradingview.com/america/scan` | ok | one full sweep (10,214 rows, server-side `exchange in (NYSE, NASDAQ, AMEX)` and `close > 1`) filtered to `type in (stock, dr)` = 5,498 US names, of which 41 carry a 2026-11-20 release stamp; issuer-level USD caps for the band |
| Coverage floor (scope limit) | `scanner.tradingview.com/america/scan` - `market_cap_basic` (issuer-level USD), constants `MCAP_FLOOR = $50B` and `band_low_usd = $40B` | ok | The roster is bounded by the market-cap band, not by who reported: S&P 500 constituents plus US-listed names at or above $50B, with the $40B-$50B band published below the floor. A US reporter below $40B market cap is out of scope - it is not on this list (a scope limit, not a missing company). US names below the band floor: 4,925 of 5,498 (65 in the band, 405 at or above the floor, 103 with no cap) |
| Yahoo Finance quoteSummary (estimates, cap cross-check) | `https://query2.finance.yahoo.com/v10/finance/quoteSummary/<TICKER>?modules=earningsTrend,earningsHistory` | ok | cookie+crumb handshake (jar seeded from fc.yahoo.com); the estimate series and the prior-result history |
| Yahoo Finance v7 quote (market cap cross-check) | `https://query1.finance.yahoo.com/v7/finance/quote?symbols=<TICKERS>` | ok | worked this fire; agrees with the scanner's issuer-level caps on all ten band names (widest spread Ferrovial 0.6%), so the scanner remains the published source for the caps and the band order |
| Yahoo Finance chart API (settled bars) | `https://query1.finance.yahoo.com/v8/finance/chart/<SYM>?interval=1d` | ok | settled daily bars for every move published here (November 19 close against November 20 close) |
| Euronext company news (Frontline) | `https://live.euronext.com/nb/node/12925008` | ok | the Oslo Børs announcement the issuer is obliged to publish, stamped "20 Nov 2026 07:30 CET" (= 01:30 ET) — the release hour that puts FRO in the already-reported table |
| PR Newswire (RLX) | `https://www.prnewswire.com/news-releases/rlx-technology-announces-unaudited-third-quarter-2026-financial-results-302946757.html` | ok | release stamped "Nov 20, 2026, 04:30 ET" |
| Business Wire / GlobeNewswire (release instants) | `businesswire.com`, `globenewswire.com` | ok | BJ's 06:45 ET, Buckle 06:45 ET, Moog 06:50 ET, BitFuFu 06:30 ET, IES Holdings 07:45 ET, MT Newswires 07:11 ET for Buckle — every stamp after the 06:00 ET fire |
| Issuer IR pages and results releases (actuals) | `frontlineplc.cy`, `vikingcruises.com` and `ir.viking.com`, `investors.ies-corporate.com`, `corporate.buckle.com`, `moog.com`, `newsroom.bjs.com`, `vallourec` Q3 release | ok | issuer-owned releases and IR pages; Viking Holdings' Q3 is dated November 17 at 07:00 ET on its own IR page and its 6-K |
| EDGAR submissions | `https://data.sec.gov/submissions/CIK<cik>.json` | ok | no results-type filing for any of the ten band names on November 19-20; acceptance times for the calendar names' 8-K/6-K filings |
| S&P 500 constituent list (Rule A) | MediaWiki wikitext for `List of S%26P 500 companies` | ok | 503 symbols parsed from all three templates (NyseSymbol, NasdaqSymbol, BZX link); control check BRK.B, GOOGL, GOOG, FOX, CBOE all present |
| Midgard (S&P 500 / STOXX coverage) | `https://www.midgard.com` coverage sweep | ok | the only name it stamps for November 20 is CTBC Financial Holding (2891.TW), which is out of scope on every count |
| Run schedule (session suspension) | - | degraded | the session was suspended after the discovery phase and resumed on 2026-11-21 at 11:0x ET, about 29 hours after the 06:00 ET fire; this brief is a late reconstruction of the November 20 ET day built on settled closes and issuer release timestamps. No data source failed |
| Published watchlist | `https://api.github.com/repos/karizaco/minimax-cloud-outputs/contents/refs/watchlist.yaml` | ok | fetched; 8 tickers, none reporting today, so no watchlist section is published |

## Rules applied

- S&P 500 membership verified against the live constituent list - never from memory. 503 symbols
  parsed from all three symbol templates, with the BRK.B / GOOGL / GOOG / FOX / CBOE control check
  passed.
- Report dates confirmed against issuer sources for every name published, and both already-reported
  rows carry a timestamped release (Euronext 07:30 CET for Frontline, PR Newswire 04:30 ET for
  RLX) - a date with no release hour is not publishable.
- The coverage floor is published with what it excludes, in three places - the front matter, the
  `## TL;DR` and the `## Source health` - and the counts add up
  (5,498 = 4,925 + 65 + 405 + 103).
- The band table is US-exchange-listed common shares only, one row per issuer, one source for the
  caps and the order, with non-common lines filtered mechanically on the description, depositary
  lines (INFY, ONC, MT, NOK, HMC, ABEV, STM) excluded as foreign issuers' ADR lines, and S&P 500
  members excluded because index membership overrides the cap.
- The three tables do not overlap: no issuer is published in two of them, and the non-US table
  carries a `us_tradeable` cell on every row with the ticker cell set to the primary listing and
  the US line in parentheses.
- The reaction layer has no row to rank, so no reaction column is published and
  `reaction_degraded` is 0 - nothing was degraded, there was nothing to degrade.
- Nothing in this brief is estimated: every cap, count and move published here was measured on
  this run, and every value that could not be measured is named in the notes instead of being
  filled in.
