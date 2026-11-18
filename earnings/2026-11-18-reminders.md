---
date: 2026-11-18
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:18
source: EarningsWhispers calendar + TradingView america scanner + Yahoo Finance quoteSummary + Nasdaq earnings calendar
primary_source: TradingView scanner (market cap, issuer-level USD) | Yahoo Finance earningsTrend (EPS est, revenue est) | EarningsWhispers (release time, confirmed report dates)
status: ok
pending_count: 5
already_reported_count: 2
non_us_count: 1
reaction_ranked: true
band_low_usd: 40000000000
contract: EARNINGS_REMINDER_V4
coverage_receipt: calendar_rows=59 s_and_p_500_hits=5 bigcap_hits=5 us_roster_rows=5 band_rows=10
coverage_floor: floor_usd=50000000000 band_low_usd=40000000000 us_population=5520 below_band_us=4941 band_us=67 at_or_above_floor_us=410 no_cap_us=102 source=TradingView america scanner (market_cap_basic, issuer-level USD)
---

# Earnings - Wed 2026-11-18

## TL;DR

- **Coverage floor — a scope limit, not a missing company.** This reminder covers S&P 500
  constituents plus US-listed reporters with a market cap of **$50B or more** (TradingView
  scanner, `market_cap_basic`, issuer-level USD). The band just under the floor — **$40B to
  $50B** — is published in the *Just below the line* table so the cliff is visible. **A US
  reporter below $40B market cap is out of scope for this reminder: it is not on this list, and
  its absence does not mean it did not report.** Of the scanner's **5,520** US names,
  **4,941** are below the $40B band floor and therefore out of scope, **67** sit in the
  $40B-$50B band, **410** are at or above the $50B floor, and **102** carry no market cap at
  all.
- **Five names carry the US roster today** - three before the open (LOW, TGT, TJX) and two
  after the close (PANW, P). The list is ranked by **reaction potential, not by size**: Everpure
  (P) leads on a 10.08 reaction score (a 6.12% typical move against a 16.01% implied move),
  ahead of Palo Alto Networks on 6.06. Two names already printed overnight and are in the
  *Already reported* table.
- **The most likely mover is not the biggest name.** Everpure is a $33.9B cap - below the $50B
  floor - and is on this list only because it is an S&P 500 constituent; Palo Alto Networks is a
  $253.2B name and ranks second.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P | Everpure, Inc. | AMC 4:05 PM | 0.78 | $1.33B | $33.92B | -1.82 | 47.50 | 6.12 | 16.01 | beat | 10.08 | pending | - |
| PANW | Palo Alto Networks, Inc. | AMC 4:05 PM | 0.97 | $3.31B | $253.24B | -2.15 | 72.43 | 2.24 | 11.79 | beat | 6.06 | pending | - |
| TGT | Target Corporation | BMO 6:30 AM | 2.08 | $26.54B | $72.47B | -0.49 | 58.72 | 4.41 | 7.79 | beat | 5.76 | pending | - |
| TJX | The TJX Companies, Inc. | BMO 7:30 AM | 1.34 | $15.85B | $142.83B | -0.95 | -15.83 | 2.80 | 5.62 | beat | 3.93 | pending | - |
| LOW | Lowe's Companies, Inc. | BMO 6:00 AM | 2.88 | $22.36B | $123.69B | -1.99 | -10.71 | 3.22 | 4.54 | beat | 3.75 | pending | - |

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|
| 0700.HK | Hong Kong Stock Exchange | Tencent Holdings Ltd | Nov 18, 2026, 16:30 HKT (08:30 UTC) | TCEHY (OTC) | ADR (OTC) | reported |

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| TEVA | Teva Pharmaceutical Industries | $49.73B | no |
| MDLN | Medline Inc. | $49.57B | no |
| FNV | Franco-Nevada Corporation | $47.71B | no |
| WCN | Waste Connections, Inc. | $45.41B | no |
| TRI | Thomson Reuters Corp | $44.87B | no |
| FER | Ferrovial N.V. | $43.46B | no |
| AU | AngloGold Ashanti PLC | $42.76B | no |
| VIK | Viking Holdings Ltd | $42.11B | no |
| NTRA | Natera, Inc. | $41.68B | no |
| MSTR | Strategy Inc | $40.76B | no |

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus | us_tradeable |
|---|---|---|---|---|---|
| 0700.HK (TCEHY) | Tencent Holdings Ltd | Nov 18, 2026, 03:30 ET (16:30 HKT) | Q3 revenue RMB207.3B, +8% YoY; IFRS diluted EPS RMB6.947; net profit RMB63.6B | revenue miss vs LSEG consensus RMB210.8B; net profit beat vs RMB59.46B | ADR (OTC) |
| HAFNI.OL (HAFN) | Hafnia Limited | Nov 18, 2026, 01:38 ET (07:30 CET) | Q3 net profit USD170.8M, USD0.34 per share, vs USD91.5M and USD0.18 in Q3 2025; operating revenue USD417.4M | not measured - no comparable consensus found in the sources read | US-listed |

## Notes

- **Ranked by reaction potential, not by market cap.** Everpure (10.08) and Palo Alto Networks
  (6.06) lead on typical and implied reaction size; the two $120B+ retailers sit at the bottom.
  Every reaction column is measured, and `reaction_degraded` is absent because no row was
  degraded: all five rows carry a prior-day move, a YTD move, a 4-event average absolute move
  (Nasdaq `earnings-surprise` report dates plus Yahoo daily bars), a Cboe ATM implied move at
  the 2026-11-20 expiry, and a prior result from Yahoo `earningsHistory`.
- **Everpure is on the list as an S&P 500 constituent, not on its cap.** At $33.92B it is below
  the $50B floor, so it carries no `boundary_case` flag (that flag marks names inside the floor
  by less than $0.5B); it is in scope because the index membership overrides the cap.
- **Release times are EarningsWhispers' confirmed slots**, cross-checked against Nasdaq's
  calendar. TradingView's stamps are placeholders and were not used for any published time: it
  carried 09:30 for TJX (EarningsWhispers: 7:30 AM ET, pre-market) and 16:00/16:05 for every
  US name.
- **EPS estimate spread, two names worth naming.** The published EPS estimates are Yahoo's
  `earningsTrend` (period 0q), with EarningsWhispers agreeing to the cent. Nasdaq's Zacks
  figure disagrees on two names beyond the 2% tolerance: **PANW $0.97 (Yahoo/EarningsWhispers)
  vs $0.52 (Nasdaq)** and **P $0.78 vs $0.27**. Yahoo's series is GAAP-leaning and Zacks'
  adjusted-leaning, so the two are different bases, not one being wrong. The other three agree
  within 2%: TGT $2.08 vs $2.05, LOW $2.88 vs $2.86, TJX $1.34 vs $1.33.
- **Market caps are the scanner's issuer-level USD figures.** Yahoo's `v7/finance/quote`
  endpoint answers **Unauthorized** from this egress, so Yahoo could not serve the market-cap
  field; `quoteSummary` did work and is the primary source for both estimate fields. The caps
  and the band order therefore come from one source - the same scanner row - as the contract
  requires.
- **Coverage receipt, accounted for row by row.** The calendar carried **59** rows (33 before
  the open, 26 after the close - matching the page's own headline). **5** were S&P 500
  constituents (TGT, LOW, TJX, PANW, P) and **5** cleared the $50B floor (those four plus
  TCEHY, Tencent's OTC line at $431.63B). All 5 index hits are published in the roster; the one
  big-cap hit that is not in the roster is Tencent, a non-US issuer whose OTC line is published
  in the non-US table and the already-reported table instead. The remaining **54** calendar rows
  are below the floor and not index members - they are out of scope by the floor, not missing.
- **The per-day count of reporters below the $40B band was not enumerated.** That would need a
  market-cap pull for every calendar row and does not fit the run budget; the population counts
  above are the measured decomposition of the scanner's US universe, and nothing here is
  estimated.
- **Three Rule B exclusions, each named.** **CPRT (Copart)** was stamped 2026-11-18 by the
  scanner but the company has not confirmed a date; Nasdaq, Zacks and MarketBeat all put it at
  **November 19**, so it is excluded. **SMPNY (Sompo Holdings)** is on the calendar as a
  November 18 before-open print, but the issuer's own investor calendar says **November 19,
  3:30pm JST** (= November 19, 01:30 ET) - the aggregator's date is the wrong-date trap and the
  name is excluded. **LNVGY (Lenovo)** carries no issuer-confirmed November 18 date (its own
  calendar's last confirmed slot was August 13; the scanner says November 19).
- **Two issuer-confirmed November 18 reporters are NOT published as already-reported**, because
  their release time was not confirmed as before 06:00 ET: **Metro Inc** (TSX: MRU; the issuer's
  IR page confirms Q4 2026 results on Wednesday, November 18 with a 9:00 a.m. ET call) and
  **Golar LNG** (NYSE: GLNG; the issuer's own release says Q3 2026 results "before the market
  opens" on November 18 with a presentation at 08:00 ET). Both are below the $50B floor, so
  neither is a roster row.
- **Tencent appears in two tables on purpose.** The non-US table says it belongs to this ET
  day (issuer-confirmed, its own results announcement is dated Hong Kong, 18 November 2026); the
  already-reported table carries the numbers it printed at 03:30 ET. **Hafnia** is in the
  already-reported table only: it is not on the standing Pass B candidate list, and its results
  release is dated by the issuer at approximately 07:30 CET (= 01:30 ET) on November 18.
- **Pass B completeness.** The standing non-US candidate list (47 issuers) was checked against
  per-market earnings-date sweeps for 15 markets (Taiwan, Japan, Korea, Hong Kong, China
  listings, Australia, Canada, Brazil, Singapore, India, the UK, Germany, Switzerland, France,
  Spain, the Netherlands) and against the issuers' own IR pages where a sweep flagged a date.
  **Tencent was the only standing candidate with a November 18 date.** The sweeps also flagged
  Nidec (TSE: 6594), SSE PLC (LSE: SSE) and other names that are not on the standing candidate
  list and carry no issuer-confirmed November 18 release; they are not published.
- **Ticker convention (primary listing first):** ADR and OTC lines are shown on the issuer's
  PRIMARY listing with its exchange suffix, with the US line in parentheses - `0700.HK (TCEHY)`,
  `HAFNI.OL (HAFN)`.
- **No watchlist section.** The published watchlist was fetched successfully (8 tickers: AAPL,
  MSFT, NVDA, GOOGL, AMZN, IWM, GLD, TLT), but **none of them reports today**, so the section is
  omitted rather than shipped empty.
- **One band name was dropped for length, not for a rule.** 67 US names sit in the $40B-$50B
  band; the table publishes the 10 largest US-exchange-listed common shares that are not S&P 500
  members. The 11th, **SLF (Sun Life Financial, $40.35B)**, is below the table's 10-row
  convention and no name below $40B is listed - names under $40B are excluded by the band, not
  by the floor. Three of the ten (TEVA, FER, AU) are foreign issuers whose ordinary shares are
  US-exchange-listed; foreign issuers whose ordinary lines trade outside the US belong to the
  non-US universe, not to this band.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| EarningsWhispers calendar (roster) | `https://www.earningswhispers.com/calendar/20261118` | ok | server-rendered; 33 before the open and 26 after the close, matching the page's own headline; 59 rows |
| EarningsWhispers company pages (estimates, times) | `https://www.earningswhispers.com/stocks/<TICKER>` | ok | consensus EPS, Rev est and the confirmed slot; all five roster names read "confirmed to report earnings on November 18, 2026" |
| Nasdaq earnings calendar | `https://api.nasdaq.com/api/calendar/earnings?date=2026-11-18` | ok | 79 rows; independent confirmation of BMO/AMC and a second EPS estimate for the five roster names |
| TradingView america scanner (universe sweep + caps) | `https://scanner.tradingview.com/america/scan` | ok | one date sweep (76 US names stamped 2026-11-18) and one cap sweep; issuer-level USD market caps for the roster and the band |
| Coverage floor (scope limit) | `scanner.tradingview.com/america/scan` - `market_cap_basic` (issuer-level USD), constants `MCAP_FLOOR = $50B` and `band_low_usd = $40B` | ok | The roster is bounded by the market-cap band, not by who reported: S&P 500 constituents plus US-listed names at or above $50B, with the $40B-$50B band published below the floor. A US reporter below $40B market cap is out of scope - it is not on this list (a scope limit, not a missing company). US names below the band floor: 4,941 of 5,520 (67 in the band, 410 at or above the floor, 102 with no cap) |
| Yahoo Finance quoteSummary (EPS + revenue estimates) | `https://query1.finance.yahoo.com/v10/finance/quoteSummary/<TICKER>?modules=earningsTrend` | ok | cookie+crumb handshake (jar seeded from fc.yahoo.com); the primary source for both estimate fields |
| Yahoo Finance v7 quote (market cap) | `https://query1.finance.yahoo.com/v7/finance/quote` | degraded | answers `Unauthorized` from this egress - market caps are the scanner's issuer-level USD figures instead |
| Yahoo Finance chart API (reaction bars) | `https://query1.finance.yahoo.com/v8/finance/chart/<SYM>` | ok | daily bars for the prior-day move, the YTD move and the 4-event average absolute move |
| Nasdaq earnings-surprise (past report dates) | `https://api.nasdaq.com/api/company/<SYM>/earnings-surprise` | ok | the four past report dates behind each average absolute move |
| Cboe delayed-quote option chain | `https://cdn.cboe.com/api/global/delayed_quotes/options/<SYM>.json` | ok | ATM straddle at the 2026-11-20 expiry for the implied move |
| Target investor relations (issuer confirmation) | `https://corporate.target.com/investors/events-presentations` | ok | issuer-owned page: Q3 2026 earnings call, Wednesday November 18, 2026, 8:00-9:00 a.m. ET |
| Everpure investor relations (issuer confirmation) | `https://investor.everpuredata.com/news-and-events/events-and-presentations/default.aspx` | ok | issuer-owned page: Q3 FY2027 results, November 18, 2026, 5:00 PM EST webcast |
| Tencent investor relations (issuer confirmation + results) | `https://www.tencent.com/investors/announcements/` and the 3Q2026 results PDF | ok | issuer-owned: results announced November 18, 2026; the HKEX filing timestamp is 08:30 UTC = 03:30 ET |
| Sompo Holdings investor relations (Rule B exclusion) | `https://www.sompo-hd.com/en/ir/event/` | ok | issuer calendar says FY2026 2nd quarter results on November 19, 3:30pm JST - the aggregator's November 18 is wrong |
| S&P 500 constituent list (Rule A) | MediaWiki wikitext for `List of S%26P 500 companies` | ok | 503 symbols parsed from all three templates (NyseSymbol, NasdaqSymbol, BZX link); control check BRK.B, GOOGL, GOOG, FOX, CBOE all present |
| Published watchlist | `https://api.github.com/repos/karizaco/minimax-cloud-outputs/contents/refs/watchlist.yaml` | ok | fetched; 8 tickers, none reporting today, so no watchlist section is published |

## Rules applied

- S&P 500 membership verified against the live constituent list - never from memory. 503 symbols
  parsed from all three symbol templates, with the BRK.B / GOOGL / GOOG / FOX / CBOE control
  check passed.
- Report dates confirmed against issuer sources for every name near the inclusion boundary. Two
  issuer-owned confirmations (Target, Everpure) and one issuer-owned results release (Tencent);
  the three Rule B exclusions (CPRT, SMPNY, LNVGY) are named in the notes with their reason.
- Reaction columns computed from measured bars, past report dates and option chains. A value
  that could not be measured is published as `n/a` and counted in `reaction_degraded`; nothing
  was degraded on this fire, so the key is absent.
- The roster is ranked by reaction potential, not by market cap, and every published row carries
  the six reaction columns.
- The market-cap floor is published with what it excludes, in three places - the front matter,
  the `## TL;DR` and the `## Source health` - and the counts add up
  (5,520 = 4,941 + 67 + 410 + 102).
- The band table is US-exchange-listed common shares only, one row per issuer, one source for
  the caps and the order, with non-common lines filtered mechanically on the description.
- The non-US table and the already-reported table carry a `us_tradeable` cell for every row, and
  the ticker cell is the primary listing with the US line in parentheses.
