---
date: 2026-11-10
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:07
source: EarningsWhispers earnings calendar + Yahoo Finance quote + TradingView scanner + Nasdaq earnings calendar + issuer IR pages
primary_source: Yahoo Finance (market cap) | EarningsWhispers (EPS est, revenue est, release time)
status: ok
pending_count: 3
already_reported_count: 2
non_us_count: 2
reaction_ranked: true
band_low_usd: 40000000000
---

# Earnings - Tue 2026-11-10

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TDG | TransDigm Group Incorporated | BMO 7:15 AM ET | 12.31 | $2.94B | $67.4B | 1.82 | -10.28 | 3.71 | 7.99 | beat | 5.42 | pending | - |

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|
| SE.SI | Singapore Exchange | Sea Limited | Nov 10, before the US market open (webcast 7:30 AM ET) | SE (NYSE ADR) | ADR (US-listed) | pending |
| PETR4.SA | B3 (Brazil) | Petroleo Brasileiro S.A. - Petrobras | Nov 10, after the B3 close (BRT) | PBR (NYSE ADR) | ADR (US-listed) | pending |

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| HEI | Heico Corporation | $47.9B | no |
| WCN | Waste Connections, Inc. | $47.5B | no |
| TRI | Thomson Reuters Corp | $46.9B | no |
| NTRA | Natera, Inc. | $46.5B | no |
| FER | Ferrovial N.V. | $44.1B | no |
| RKT | Rocket Companies, Inc. | $43.1B | no |
| UI | Ubiquiti Inc. | $41.5B | no |
| SLF | Sun Life Financial Inc. | $41.0B | no |

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus |
|---|---|---|---|---|
| IFX.DE (IFNNY) | Infineon Technologies AG | Nov 10, 07:30 CET (01:30 ET) | Q4 FY26 revenue EUR 4.706B, segment result EUR 1.119B (23.8% margin), adj. diluted EPS EUR 0.60; FY26 revenue EUR 16.353B (+12% YoY), adj. EPS EUR 1.73 | n/a - no consensus published |
| 9984.T (SFTBY) | SoftBank Group Corp | Nov 10, 15:30 JST (01:30 ET) | H1 FY26 net sales JPY 4,235.0B (+13.3% YoY); income before tax JPY -438.7B; net income JPY -768.0B; total gain on investments JPY 1,725.8B | n/a - no consensus published |

## Notes

- **A genuinely light day.** TDG is the **only** S&P 500 constituent on today's calendar, and it is the
  only row in the US roster. Three independent passes agree: the EarningsWhispers roster (58 BMO + 89
  AMC) intersected with the live 503-symbol S&P 500 list, the Nasdaq earnings calendar (173 rows), and
  a TradingView date sweep over every US name with an earnings date on 2026-11-10 (114 names). No
  mega-cap sits behind the floor and nothing above $50B other than TDG reports today.
- **The roster is ranked by reaction potential, not by market cap** - with one row the ranking is
  trivially satisfied, but the columns are all measured: TDG's average absolute reaction is 3.71% over
  its last 4 reports (2026-08-04, 2026-05-05, 2026-02-03, 2025-11-12) and the implied move is 7.99%,
  giving 0.6 x 3.71 + 0.4 x 7.99 = 5.42.
- **TDG's implied move was recomputed by hand from the Cboe chain**, not taken on trust: TDG has no
  expiry before 2026-11-20, so that expiry is the first one straddling the event; the ATM strike 1220
  has a call mid of 49.15 and a put mid of 48.20, i.e. a straddle of 97.35 on a 1218.85 spot = 7.99%.
- **TDG's date is company-confirmed, not aggregator-confirmed**: TransDigm's own 2 November 2026 press
  release says it will report fiscal Q4 2026 before the market opens on Tuesday 10 November 2026, with
  a 10:00 ET call. EarningsWhispers independently shows 7:15 AM ET, consensus EPS $12.31 (non-GAAP),
  revenue estimate $2.94B.
- **TDG is not a boundary case** - $67.4B is $17.4B above the floor, so the Flag cell is `-`.
- **Two large non-US issuers printed before this fire and are therefore in the "Already reported"
  section rather than the non-US table**: Infineon (07:30 CET = 01:30 ET) and SoftBank Group
  (15:30 JST = 01:30 ET). Both are published on their primary listing with the US line in
  parentheses - Infineon's US peer is the OTC ADR IFNNY, SoftBank's is the OTC ADR SFTBY - and both
  are `ADR (OTC)`, not US-listed lines.
- **Petrobras and Sea are still pending at 06:00 ET.** Petrobras discloses 3Q26 on 10 November per its
  own IR calendar (the webcast is the following day, 11 November), i.e. after the B3 close; Sea's own
  27 October 2026 release says Q3 2026 results come before the US market open on 10 November, so at
  the 06:00 ET fire they are still ahead of the reader.
- **Sea's primary listing is Singapore**: the ordinary shares trade on the SGX and the NYSE line is
  the ADS, so the headline ticker is `SE.SI` with `SE (NYSE ADR)` as the US peer. Yahoo does not quote
  the SGX line (its quote endpoint returns no result for `SE.SI`), so the `.SI` suffix follows the
  standard exchange-suffix convention rather than a live quote.
- **The Pass B standing list was checked in full** - 44 candidates - and **none of them carries an
  issuer-confirmed 10 November date**; every one of them stays unpublished. The four non-US rows
  published today were found by a market-wide sweep and each is confirmed on an issuer-owned page:
  Infineon (EQS release 10/11/26 07:30 CET), SoftBank Group (IR calendar and 2 October 2026 briefing
  notice), Petrobras (IR events page and 4 November 2026 market notice), Sea (27 October 2026 release).
- **The band table is a LOWER BOUND on what the floor excluded** - names below $40B are excluded by the
  band, not by the $50B floor. All 8 band rows are US-listed common shares between $40B and $50B that
  are not S&P 500 members, and none of them reports today. Preferreds, notes, depositary receipts and
  other non-common lines were filtered out on the line description; Heico's Class A (`HEI`) and Class
  B (`HEI.A`) are one issuer and are published once, on the more liquid class. TRI, FER and SLF are
  foreign issuers whose US lines sit in the band.
- **`HEI` and `WCN` are not S&P 500 members** - they are absent from the live Wikipedia constituent
  list (503 symbols, all control checks passed) and an independent index-membership database dated
  23 October 2026 lists both as "not in the S&P 500". The "S&P 500" text on a Yahoo quote page is a
  benchmark label, not a membership statement.
- **No watchlist section.** `refs/watchlist.yaml` fetched cleanly (8 tickers: AAPL, MSFT, NVDA,
  GOOGL, AMZN, IWM, GLD, TLT) but **none of them reports today**, so the section is omitted rather
  than shipped empty.
- **Consensus basis.** EPS and revenue estimates are EarningsWhispers' adjusted (non-GAAP) figures;
  TDG's $12.31 is the non-GAAP consensus, with the whisper at $12.54. Sea's consensus is $1.04 EPS
  on $8.32B revenue and Petrobras' is $1.38 on $32.92B (both USD, per EarningsWhispers). Market caps
  are Yahoo Finance's. No consensus was published for the Infineon or SoftBank ADR lines, so their
  `vs consensus` cell is `n/a` rather than an invented beat/miss.

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| EarningsWhispers calendar | `https://www.earningswhispers.com/calendar/20261110` | ok | server-rendered, 58 BMO + 89 AMC |
| EarningsWhispers company pages | `https://www.earningswhispers.com/stocks/{TDG,SE,PBR}` | ok | TDG, SE and PBR confirmed; IFNNY/SFTBY pages carry no estimate for the just-printed quarter |
| Yahoo Finance quote API | `query1.finance.yahoo.com/v7/finance/quote` | ok | market caps, cookie+crumb handshake |
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/{SYM}` | ok | daily bars for prior-day and YTD moves |
| Nasdaq earnings calendar | `api.nasdaq.com/api/calendar/earnings?date=2026-11-10` | ok | 173 rows, used as a cross-check only |
| Nasdaq earnings-surprise | `api.nasdaq.com/api/company/TDG/earnings-surprise` | ok | past report dates (M/D/YYYY) for the 4-event reaction average |
| Cboe delayed option chain | `cdn.cboe.com/api/global/delayed_quotes/options/TDG.json` | ok | 810 contracts, 5 expiries; chain timestamp 2026-11-10 00:28:51 |
| TradingView scanner | `scanner.tradingview.com/america/scan` | ok | date sweep over the US universe; the `range 5000` cap silently truncated the first pass, so the sweep was re-run with a market-cap filter |
| Wikipedia S&P 500 wikitext | `en.wikipedia.org/w/api.php?action=parse` | ok | 503 symbols; controls BRK.B, GOOGL, GOOG, FOX, CBOE all present |
| Yahoo chart API for `SE.SI` | `query1.finance.yahoo.com/v8/finance/chart/SE.SI` | degraded | no coverage for Sea's SGX line; the symbol follows the exchange-suffix convention instead |
| stockanalysis.com | `stockanalysis.com/quote/sgx/SE/` | blocked | Cloudflare challenge; the primary listing was confirmed from Wikipedia instead |

## Rules applied

- S&P 500 membership verified against the live constituent list - never from memory.
- Report dates confirmed against issuer sources for every published name.
- Reaction columns computed from measured bars, past report dates and option chains; a value that
  could not be measured is published as `n/a` and counted in `reaction_degraded` (none degraded today).
- One row per issuer, primary listing first, US line in parentheses.
- The three content tables do not overlap, and the non-US table is a separate universe from the roster.
- The market-cap floor is published with what it excludes, and no row inside the floor by less than
  $0.5B is present.
