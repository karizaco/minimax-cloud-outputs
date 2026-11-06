---
date: 2026-11-06
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:24
source: EarningsWhispers + Nasdaq earnings calendars; issuer IR pages and press releases; TradingView scanner; Yahoo chart API; Cboe delayed-quote option chains
primary_source: Yahoo Finance (market cap) | Nasdaq/Zacks (EPS est) | TradingView (revenue est)
status: ok
pending_count: 9
already_reported_count: 2
non_us_count: 3
reaction_ranked: true
band_low_usd: 40000000000
---

# Earnings - Fri 2026-11-06

## Your watchlist

Fetched from the published `refs/watchlist.yaml`. **No watchlist name reports today** - including none of the five `earnings_flag` names.

| Ticker | Note | Reports today |
|---|---|---|
| AAPL | mega-cap core; earnings flag | no |
| MSFT | mega-cap core; earnings flag | no |
| NVDA | mega-cap core; earnings flag | no |
| GOOGL | mega-cap core; earnings flag | no |
| AMZN | mega-cap core; earnings flag | no |
| IWM | small-cap beta leg | no |
| GLD | gold leg | no |
| TLT | duration leg | no |

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHTR | Charter Communications, Inc. | BMO 7:00 AM ET | 10.06 | $13.50B | $16.36B | +4.67 | -39.86 | 9.23 | 12.35 | beat (+5.9%) | 10.48 | pending | - |
| MRNA | Moderna, Inc. | BMO (call 8:00 AM ET) | -1.10 | $0.89B | $96.40B | -6.55 | +682.44 | 3.79 | 8.26 | beat (+4.3%) | 5.58 | pending | - |
| HUM | Humana Inc. | BMO 6:00 AM ET | -1.03 | $40.87B | $49.45B | -1.35 | +55.70 | 5.27 | 5.80 | beat (+8.8%) | 5.48 | pending | - |
| BEN | Franklin Resources, Inc. | BMO (call 11:00 AM ET) | 0.78 | $1.86B | $16.37B | -4.90 | +35.34 | 4.05 | 6.60 | beat (+8.3%) | 5.07 | pending | - |
| BAM | Brookfield Asset Management | BMO (released before 7:00 AM ET) | 0.44 | $1.60B | $83.79B | -3.05 | -1.85 | 2.16 | 6.81 | beat (+0.4%) | 4.02 | pending | - |
| VST | Vistra Corp | BMO (call 10:00 AM ET) | 2.89 | $6.03B | $37.89B | -6.15 | -31.68 | 1.99 | 6.87 | miss (-54.2%) | 3.94 | pending | - |
| ENB | Enbridge Inc. | BMO (webcast 9:00 AM ET) | 0.36 | $9.62B | $107.23B | -1.37 | -0.02 | 2.05 | 4.21 | beat (+5.6%) | 2.91 | pending | - |
| PPL | PPL Corporation | BMO (call 11:00 AM ET) | 0.53 | $2.41B | $27.09B | +0.78 | +2.53 | 1.59 | 4.10 | miss (-4.0%) | 2.59 | pending | - |

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|
| 9433.T | Tokyo Stock Exchange | KDDI Corp | Nov 6, 16:00 JST (02:00 ET) | KDDIY (OTC) | ADR (OTC) | reported |
| 0388.HK | Hong Kong Stock Exchange | Hong Kong Exchanges & Clearing | Nov 6 HKT - no clock time published (released after the HK close) | HKXCY (OTC) | ADR (OTC) | reported (time unconfirmed) |
| CSU.TO | Toronto Stock Exchange | Constellation Software Inc. | Nov 6, after the TSX close (16:00 ET) | CNSWF (OTC) | ADR (OTC) | pending |

## Just below the line

US-listed common shares in the $40B-$50B band the $50B floor excluded. None reports today.

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| TEVA | Teva Pharmaceutical Industries | $48.75B | no |
| FNV | Franco-Nevada Corporation | $48.35B | no |
| WCN | Waste Connections, Inc. | $47.96B | no |
| TEAM | Atlassian Corporation | $46.40B | no |
| AU | AngloGold Ashanti PLC | $44.79B | no |
| FER | Ferrovial N.V. | $42.56B | no |
| RKT | Rocket Companies, Inc. | $42.06B | no |
| SLF | Sun Life Financial Inc. | $40.86B | no |

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus |
|---|---|---|---|---|
| 9433.T (KDDIY) | KDDI Corp | Nov 6, 16:00 JST (02:00 ET) | H1 FY2027: sales JPY 3,052.8B, adj. operating profit JPY 633.1B, adj. net profit JPY 390.0B | n/a (no consensus sourced) |
| 0388.HK (HKXCY) | Hong Kong Exchanges & Clearing | Nov 6 HKT (no clock time published) | 2026 Q3 results published (9M ended 30 Sep 2026) | n/a (no consensus sourced) |

## Notes

- **Ranked by reaction potential, not size.** CHTR tops the screen at 10.48 (4-quarter average absolute move 9.23% + a 12.35% implied move) on a $16.36B cap - it is the name most likely to move, not the biggest. VST is the one to watch for disappointment: it missed its last quarter by 54.2%.
- **Two mega-caps on the calendars were excluded after checking the issuer's own page.** BRK.B - Berkshire's own 4 Nov notice says its Q3 release posts **Saturday, November 7**, not today. ECHO - EchoStar filed its 10-Q for the quarter ended 30 Sep 2026 on **3 November**, so it had already reported when Nasdaq's calendar still listed it for today.
- **HUM is in the roster at $49.45B** because it is an S&P 500 constituent, not because of the floor. Nasdaq's market cap would place it at $50.12B, inside the floor by $0.12B; Yahoo's $49.45B puts it $0.55B below it, so it carries **no** `boundary_case` flag.
- **Market-cap spread on CHTR:** Yahoo $16.36B vs TradingView $22.17B (35% apart) - Yahoo is published. The other seven names agree within 2.6%.
- **EPS basis:** Nasdaq/Zacks consensus (adjusted) is published. TradingView's forecast differs on CHTR ($8.90 vs $10.06) and ENB ($0.34 vs $0.36) - GAAP vs adjusted bases.
- **Revenue:** TradingView next-quarter forecast, cross-checked against MarketBeat for VST ($6.03B) and BEN ($1.86B) - identical.
- **Implied-move expiry matters for four names.** MRNA, VST, CHTR and HUM are measured on the 6 Nov expiry. BEN, PPL, ENB and BAM have **no 6 Nov series** in the Cboe chain, so their implied move is measured on the 20 Nov expiry - a longer-dated and therefore smaller measure. Their reaction scores are conservative.
- **Prior result was recomputed** from Yahoo's `earningsHistory` selecting the **latest** quarter (ended 30 Jun 2026). The helper's default takes the *oldest* entry of that array, which would have published a year-old verdict (it called CHTR a miss; the latest quarter was a beat). The published column is corrected.
- **Pass B:** 43 standing candidates were checked against their own IR calendars and announcements. Published: KDDI (issuer-confirmed 6 Nov, 16:00 JST = 02:00 ET). **Constellation Software** and **HKEX** were added to the standing universe - both issuer-confirmed for 6 Nov. Excluded on the ET-day rule: Mitsubishi Heavy (disclosed 6 Nov 13:30 JST = 5 Nov 23:30 ET) and Macquarie (7:00 AEDT = 5 Nov 15:00 ET) - both landed on the **previous ET day**. Nestle (22 Oct) and Novartis (27 Oct) are not candidates for today.
- **Band:** 8 US-listed common shares in [$40B, $50B). Two names in that band that *do* report today were excluded by the common-share rule: HMC (Honda ADR, $47.05B) and ONC (BeOne ADR, $44.06B), both pre-market. The band is a lower bound - names under $40B are excluded by the band, not by the floor.
- **HKEX publishes no release clock time**, so its pending/reported cell is timing-unconfirmed; the results PDF is published and HKEX announces after the Hong Kong close.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| EarningsWhispers calendar | `earningswhispers.com/calendar/20261106` | ok | server-rendered; 133 companies (101 before the open, 32 after the close) |
| Nasdaq earnings calendar | `api.nasdaq.com/api/calendar/earnings?date=2026-11-06` | ok | 118 rows; EPS consensus, BMO/AMC, market cap, fiscal quarter |
| S&P 500 constituent list | Wikipedia MediaWiki wikitext | ok | 503 symbols; BRK.B, GOOGL, GOOG, FOX and CBOE all present |
| Issuer IR pages / press releases | 12 issuer-owned pages | ok | every date in the roster was confirmed on the issuer's own page |
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/<SYM>` | ok | 2y daily bars for all 8 roster names; last bar 2026-11-05 |
| Yahoo quote v7 | `query1.finance.yahoo.com/v7/finance/quote` | ok | market caps, batches of 50 |
| Yahoo quoteSummary | `.../v10/finance/quoteSummary/<SYM>` | degraded | crumb endpoint intermittently returns HTTP 429 from this egress; `earningsHistory` worked with the seeded jar, `earningsTrend` (revenue) did not - TradingView substituted |
| Nasdaq earnings-surprise | `api.nasdaq.com/api/company/<SYM>/earnings-surprise` | ok | four past report dates per name (M/D/YYYY format) |
| Cboe delayed-quote chains | `cdn.cboe.com/api/global/delayed_quotes/options/<SYM>.json` | ok | four names have no 6 Nov expiry - 20 Nov used |
| TradingView scanner | `scanner.tradingview.com/america/scan` | ok | market caps, revenue forecasts, and a completeness sweep (42 names with cap > $5B report on 6 Nov) |
| Watchlist | `minimax-cloud-outputs` `refs/watchlist.yaml` | ok | published file, 8 tickers, none reporting today |
| EarningsWhispers company pages | `earningswhispers.com/stocks/<SYM>` | failed | 2 KB cookie wall on every page - Nasdaq/Zacks and TradingView used for estimates instead |
| stockanalysis.com quote pages | `stockanalysis.com/quote/<exch>/<sym>/` | partial | 40 of 43 Pass B candidates resolved; the three SIX lines (NESN, ROG, NOVN) 404 on the venue code - checked separately on the issuers' own pages (Nestle 22 Oct, Novartis 27 Oct) |

## Rules applied

- S&P 500 membership verified against the live constituent list (503 symbols) - never from memory.
- Report dates confirmed against issuer-owned pages for every name in the roster and for every Pass B candidate published; date-confirmed exclusions are recorded above.
- One source per field: Yahoo for market cap, Nasdaq/Zacks for the EPS estimate, TradingView for the revenue estimate. Spreads above 5% (market cap) and 2% (EPS) are noted.
- Reaction columns are measured, never estimated: Yahoo daily bars, Nasdaq past report dates, Yahoo earnings history and Cboe option chains. Nothing was interpolated from market cap or from a similar name.
- The non-US table is a separate universe and does not overlap the US roster; the headline ticker is always the issuer's primary listing with the US line in parentheses.
- The $50B floor is published with what it excludes, and a row inside the floor by less than $0.5B would carry `boundary_case` (none today).
