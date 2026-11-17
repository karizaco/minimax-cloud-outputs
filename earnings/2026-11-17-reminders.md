---
date: 2026-11-17
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:10
source: EarningsWhispers earnings calendar + TradingView scanner (market_cap_basic) + issuer IR releases
primary_source: EarningsWhispers (EPS est, revenue est, release slot) | Yahoo Finance (market cap, bars) | issuer IR (report date, actuals)
status: ok
pending_count: 2
already_reported_count: 1
non_us_count: 0
reaction_ranked: true
band_low_usd: 40000000000
reaction_degraded: 0
contract: EARNINGS_REMINDER_V4
coverage_receipt: calendar_rows=42 s_and_p_500_hits=3 bigcap_hits=3 us_roster_rows=3 band_rows=8
coverage_floor: floor_usd=50000000000 band_low_usd=40000000000 us_population=5533 below_band_us=4951 band_us=68 at_or_above_floor_us=412 no_cap_us=102 source=TradingView america scanner (market_cap_basic, issuer-level USD)
---

# Earnings - Tue 2026-11-17

## TL;DR

- **Coverage floor — a scope limit, not a missing company.** This reminder covers S&P 500
  constituents plus US-listed reporters with a market cap of **$50B or more** (TradingView
  scanner, `market_cap_basic`, issuer-level USD). The band just under the floor — **$40B to $50B**
  — is published in the *Just below the line* table so the cliff is visible. **A US reporter below
  $40B market cap is out of scope for this reminder: it is not on this list, and its absence does
  not mean it did not report.** Of the scanner's **5,533** US names, **4,951** are below the $40B
  band floor and therefore out of scope, **68** sit in the $40B-$50B band, **412** are at or above
  the $50B floor, and **102** carry no market cap at all.
- **Three names on the roster, and only three.** NVIDIA ($3,763.0B, AMC 4:20 PM ET), The Walt
  Disney Company ($205.0B, BMO ~6:30 AM ET) and Home Depot ($346.7B, BMO ~6:00 AM ET). Ranked by
  **reaction potential**, not by size: DIS 6.58, NVDA 6.22, HD 3.24 — DIS carries the largest
  typical reaction (6.59% avg abs move over its last four reports) and NVDA the largest implied
  move (8.37% at the 18 Nov expiry).
- **One of the three has already printed.** Home Depot released Q3 FY2026 at ~6:00 AM ET (adj EPS
  $3.86, in line with the $3.86 consensus; sales $43.398B vs ~$42.7B expected; comps +2.2%; FY26
  guidance updated). Disney's release slot is ~6:30 AM ET and NVIDIA's is ~4:20 PM ET, so both are
  still `pending` at this 06:10 ET snapshot.
- **No standing non-US issuer reports on the fire date.** 47 Pass B candidates were checked; none
  has an issuer-confirmed 17-November ET date (Tencent is confirmed for 18 November).

## Your watchlist

| Ticker | Note | Reports today | Earnings flag |
|---|---|---|---|
| NVDA | mega-cap core; earnings flag | yes — AMC 4:20 PM ET | true |
| AAPL | mega-cap core; earnings flag | no | true |
| MSFT | mega-cap core; earnings flag | no | true |
| GOOGL | mega-cap core; earnings flag | no | true |
| AMZN | mega-cap core; earnings flag | no | true |
| IWM | small-cap beta leg | no | - |
| GLD | gold leg | no | - |
| TLT | duration leg | no | - |

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DIS | The Walt Disney Company | BMO 6:30 AM ET | 1.67 | $25.26B | $205.0B | -0.23 | +6.12 | 6.59 | 6.57 | beat | 6.58 | pending | - |
| NVDA | NVIDIA Corporation | AMC 4:20 PM ET | 2.49 | $108.99B | $3,763.0B | -4.12 | -17.32 | 4.78 | 8.37 | beat | 6.22 | pending | - |
| HD | Home Depot, Inc. | BMO 6:00 AM ET | 3.86 | $42.72B | $346.7B | -0.34 | +0.49 | 2.25 | 4.73 | beat | 3.24 | reported | - |

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|

No standing Pass B candidate has an issuer-confirmed report date on 17 November 2026 (ET), so no
row is published. 47 candidates were screened; 1 of them (Tencent) has a confirmed date inside the
window and it falls on 18 November, outside the fire date; the other 46 publish no date on their
own IR pages, and an aggregator date is not a publishable date.

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| WCN | Waste Connections, Inc. | $49.4B | no |
| TRI | Thomson Reuters Corp | $46.9B | no |
| FNV | Franco-Nevada Corporation | $46.3B | no |
| MSTR | Strategy Inc | $43.5B | no |
| NTRA | Natera, Inc. | $41.8B | no |
| UI | Ubiquiti Inc | $40.5B | no |
| VIK | Viking Holdings Ltd | $40.3B | yes (BMO) |
| SLF | Sun Life Financial Inc | $40.2B | no |

## Notes

- **The roster is ranked by reaction potential, not by market cap.** NVIDIA is the largest company
  in the world and the second most likely to move; Disney is a quarter of its size and the most
  likely to move. Every reaction column was measured: `Prior day %` and `YTD %` from Yahoo daily
  bars, `Avg abs move %` as the mean absolute reaction over each name's last 4 past reports
  (report dates from the Nasdaq `earnings-surprise` table, bars from Yahoo), `Implied move %` as
  the ATM straddle mid at the first Cboe expiry that straddles the event (DIS and HD 20 Nov, NVDA
  18 Nov), `Prior result` from Yahoo `earningsHistory` (all three beat, latest quarter for each),
  `Reaction score = 0.6 x avg_abs_move + 0.4 x implied_move`. No column is estimated and none
  degraded (`reaction_degraded: 0`).
- **Report dates were confirmed on issuer-owned pages (Rule B), not on the aggregator.** NVIDIA:
  issuer press release (28 Oct) and IR event page — Q3 FY2027 results on Tuesday 17 November, call
  5:00 p.m. ET, results published ~1:20 p.m. PT. Disney: issuer release (16 Nov) — results posted
  17 November ~6:30 a.m. ET, webcast 8:30 a.m. ET. Home Depot: IR events page and news-release
  index — Q3 FY2026 release 17 November, call 9:00 a.m. ET.
- **Home Depot has reported (status `reported`); Disney has not yet (status `pending`).** HD's
  17-November release is on its own IR index: sales $43.398B (+4.9%), comps +2.2%, GAAP EPS $3.72,
  adjusted EPS $3.86 (vs the $3.86 consensus), FY2026 guidance updated to ~+4.5% total sales,
  ~+1.4% comps and ~+2.0% adjusted EPS growth; it also named Richard McPhail CEO effective
  23 November. Disney's figures were still circulating on third-party sites at the 06:10 snapshot
  while the issuer's own release slot (~6:30 a.m. ET) had not arrived and Nasdaq's
  `earnings-surprise` table still showed 5 Aug 2026 as its latest print — so no actual is published
  for Disney here. NVDA reports ~4:20 p.m. ET.
- **Consensus spread (Rule C).** One source per field: EPS and revenue estimates from
  EarningsWhispers (Zacks-consistent), market cap from Yahoo with the TradingView issuer-level cap
  as the cross-check. DIS EPS $1.67 (LSEG also $1.67) and revenue $25.26B vs LSEG $25.18B (0.3%
  spread, under tolerance); HD EPS $3.86 (Zacks) vs $3.83 (MarketBeat) and revenue $42.72B vs
  $42.69B-$42.79B. Market caps agree with the scanner to within 0.2% on all three names
  (NVDA $3,763.0B scanner vs $3,770.3B Yahoo). No spread exceeds the 5% market-cap or 2% EPS
  tolerance on a published row.
- **Completeness basis.** The EarningsWhispers calendar carried **42** rows for 17 November
  (29 before the open, 13 after the close); **3** of them are S&P 500 constituents and **3** clear
  the $50B floor, and all 3 are published. A TradingView `earnings_release_next_date` sweep of the
  US universe independently returned **86** names with a 17-November ET date, and **no** name at
  or above $50B was missing from the calendar roster. The remaining calendar names are below the
  $40B band floor and are therefore out of scope: VIK $40.3B (published in the band table above),
  JD $33.2B, ESLT $31.9B, AS $16.9B, ZTO $15.3B, SQM $14.4B, TME $13.4B, DLB $5.7B, SR $5.3B,
  KLAR $5.2B, GFF $4.5B, CAAP $4.0B, MNSO $3.4B, LUXE $1.5B, WB $1.5B, OPRA $1.4B, ENR $1.7B,
  FUBO $0.8B, SMWB $0.7B, HUYA $0.5B, and the remaining sub-$500M lines.
- **The US date sweep also carried 43 names the aggregator calendar did not** (Macy's $6.2B,
  NIO $6.7B, Freedom Holding $10.2B, Brady $3.7B, Grupo Financiero Galicia $4.9B, Driven Brands
  $1.8B, Central Puerto $1.7B, Hub Group $1.5B, GoodRx $1.2B, Mitek $0.8B and small caps below).
  Every one of them is below the $40B band floor — out of scope, not missing.
- **The band table is US-listed common shares only, one row per issuer, at the issuer-level cap**
  from the same scanner row that ranked them. Three names in the raw $40B-$50B band were dropped
  because they are foreign issuers whose primary listing is not the US (TEVA $49.7B, primary
  Tel Aviv; FER $44.4B, primary Madrid; AU $42.7B) — a foreign ordinary line belongs to Pass B,
  not to the US band. Non-common lines were filtered mechanically on the description, which also
  removed preferred, depositary and perp lines inside the band.
- **Non-US check.** 47 standing Pass B candidates were screened across the TSE, KRX, TWSE, HKEX,
  XETRA, SIX, LSE, Euronext, BME, Nasdaq Copenhagen, BVMF, TSX, ASX and SGX calendars for the
  16-18 November window; no standing candidate has an issuer-confirmed 17-November ET date, so the
  table is empty. **Tencent** is confirmed by its own IR page for 18 November, outside the fire
  date. **Alstom** (Euronext, ~$5.0B) is confirmed by its own IR page for 17 November 18:00 CET =
  12:00 ET — it is not on the standing Pass B list, so it is not published here, and it is the
  obvious candidate to add. No standing candidate printed before the 06:00 ET fire, so the
  *Already reported* section is omitted rather than shipped empty.
- **Watchlist.** `refs/watchlist.yaml` was fetched successfully, so the section is published.
  NVDA is the only watchlist name on today's calendar (earnings flag set).
- **Ticker convention.** Every published US name is a US listing, so no ADR/OTC headline appears;
  the foreign issuers that appear above are named by company only.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| EarningsWhispers calendar | `https://www.earningswhispers.com/calendar/20261117` | ok | server-rendered; 29 before the open, 13 after the close = 42 rows, matching the page's own headline counts |
| EarningsWhispers company pages | `https://www.earningswhispers.com/stocks/{HD,DIS,NVDA}` | ok | consensus EPS $3.86 / $1.67 / $2.49, `Rev est` $42.72B / $25.26B / $108.99B, release slot and slot time; read with the documented `ewc` cookie (160 KB pages, not the cookie wall) |
| Issuer IR pages | `ir.homedepot.com`, `investors.thewaltdisneycompany.com`, `investor.nvidia.com` | ok | Rule B confirmation of the report date, the release slot and (for HD) the actual result; HD's release is on its own news-release index |
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/<SYM>` | ok | daily bars for `Prior day %`, `YTD %` and the reaction windows; no crumb needed |
| Yahoo quote API | `query1.finance.yahoo.com/v7/finance/quote` | ok | market caps, after the fc.yahoo.com cookie+crumb seed; cross-check only, the scanner is the cap source |
| Yahoo `earningsHistory` | `quoteSummary?modules=earningsHistory` | ok | prior result and surprise for all three names, latest quarter selected (not the first array entry) |
| Nasdaq earnings API | `api.nasdaq.com/api/company/<SYM>/earnings-surprise` | ok | past report dates (`M/D/YYYY`) and surprise; also used to confirm that DIS had not yet printed at the snapshot |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/options/<SYM>.json` | ok | ATM straddle mid for the implied move; expiry parsed from the OCC symbol (DIS/HD 20 Nov, NVDA 18 Nov) |
| Wikipedia S&P 500 list | `en.wikipedia.org/w/api.php?action=parse&page=List_of_S%26P_500_companies&prop=wikitext` | ok | 503 symbols parsed from all three symbol templates; control check passed (`BRK.B`, `GOOGL`, `GOOG`, `FOX`, `CBOE` all present) |
| TradingView scanner (population) | `scanner.tradingview.com/america/scan` — `market_cap_basic`, `exchange match NASDAQ\|NYSE\|AMEX`, `close > 1`, `type in (stock, dr)` filtered in python | ok | 10,230 rows returned for 10,230 `totalCount` (no truncation); 5,533 US names after the type filter; the date sweep used `earnings_release_next_date` over the 17-November ET window |
| Coverage floor (scope limit) | `scanner.tradingview.com/america/scan` — `market_cap_basic` (issuer-level USD), constants `MCAP_FLOOR = $50B` and `band_low_usd = $40B` | ok | The roster is bounded by the market-cap band, not by who reported: S&P 500 constituents plus US-listed names at or above $50B, with the $40B-$50B band published below the floor. A US reporter below $40B market cap is out of scope — it is not on this list (a scope limit, not a missing company). US names below the band floor: 4,951 of 5,533 (68 in the band, 412 at or above the floor, 102 with no cap) |
| stockanalysis.com | `stockanalysis.com/quote/...` | unreachable | not used: Cloudflare-walled from this runtime (measured 403); primary listings resolved with Yahoo chart metadata and the scanner's `exchange`/`type` columns instead |

## Rules applied

- S&P 500 membership verified against the live constituent list (503 symbols, all three templates
  parsed, control check passed) — never from memory.
- Report dates confirmed on issuer-owned pages for every published name; aggregator-only dates were
  not published.
- One source per field; spreads beyond 5% (market cap) or 2% (EPS) would be noted — none occurred
  on a published row.
- Reaction columns computed from measured bars, past report dates and option chains. A value that
  could not be measured is published as `n/a` and counted in `reaction_degraded`; none degraded.
- The non-US table is a separate table and never overlaps the US roster; a row is published only
  with an issuer-confirmed date and a local announcement hour that fixes the ET day.
- The market-cap floor is published with what it excludes, and a row inside the floor by less than
  $0.5B would carry `boundary_case`; no roster row is that close to the floor.
- Read-only reminder: no position, price target or analyst rating is published.
