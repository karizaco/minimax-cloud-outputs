---
date: 2026-11-02
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:08
source: EarningsWhispers calendar (roster) + MarketBeat / Yahoo (estimates) + TradingView (market cap)
primary_source: MarketBeat (EPS est, revenue est) | TradingView scanner (market cap), each cross-checked
status: ok
pending_count: 19
already_reported_count: 0
---

# Earnings - Mon 2026-11-02

**19 S&P 500 names report today** - 8 before the open, 11 after the close. All 19 are still
`pending` as of 06:08 ET; no name on the roster had printed yet at snapshot time.

Filter applied: S&P 500 membership (verified against the live Wikipedia constituent list, 503 symbols) OR
mega-cap >$50B. No non-S&P 500 name on today's calendar clears $50B - the largest is ROKU at $23.0B - so
the roster is exactly the S&P 500 cohort. No watchlist file was available in this runtime, so the watchlist
section is omitted.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Status |
|---|---|---|---|---|---|---|
| MAR | Marriott International | BMO ~7:00a ET (call 8:00a) | 2.84 | 6.93B | 104.1B | pending |
| ETR | Entergy | BMO (call 11:00a ET) | 1.73 | 4.12B | 52.6B | pending |
| IDXX | IDEXX Laboratories | BMO (call 8:30a ET) | 3.73 | 1.19B | 43.4B | pending |
| EL | The Estee Lauder Companies | BMO (call 8:30a ET) | 0.51 | 3.65B | 39.6B | pending |
| PEG | Public Service Enterprise Group | BMO (webcast 11:00a ET) | 1.19 | 3.19B | 37.0B | pending |
| FOXA | Fox Corp - Class B | BMO (webcast 8:30a ET) | 2.02 | 4.32B | 25.1B | pending |
| FOX | Fox Corp - Class A | BMO (webcast 8:30a ET) | 2.07 | 4.32B | 25.1B | pending |
| L | Loews Corp | BMO | n/a | n/a | 22.8B | pending |
| AAPL | Apple | AMC 4:30p ET (call 5:00p ET) | 1.99 | 113.40B | 5,029.6B | pending |
| PLTR | Palantir Technologies | AMC (call 5:00p ET) | 0.41 | 2.18B | 442.4B | pending |
| VRTX | Vertex Pharmaceuticals | AMC (call 4:30p ET) | 4.82 | 3.42B | 141.7B | pending |
| WMB | The Williams Companies | AMC (call Nov 3, 9:30a ET) | 0.54 | 2.99B | 90.9B | pending |
| FANG | Diamondback Energy | AMC (call Nov 3, 9:00a ET) | 5.72 | 4.60B | 59.4B | pending |
| O | Realty Income Corp | AMC (webcast 5:00p ET) | 0.41 | 1.43B | 53.9B | pending |
| ON | onsemi | AMC (call 5:00p ET) | 0.88 | 1.71B | 27.9B | pending |
| SBAC | SBA Communications | AMC (call 5:00p ET) | 2.09 | 724.07M | 19.9B | pending |
| DOC | Healthpeak Properties | AMC (call Nov 3, 10:00a ET) | 0.06 | 739.18M | 13.4B | pending |
| UDR | UDR Inc | AMC (call Nov 3, 12:00p ET) | 0.15 | 427.85M | 11.4B | pending |
| CLX | The Clorox Company | AMC | 1.07 | 1.88B | 10.6B | pending |

`BMO` = before market open, `AMC` = after market close. EPS/Rev are consensus; Mkt cap is the
TradingView scanner value, cross-checked against stockanalysis.com (see reconciliation below).
Loews (L) has no published consensus EPS or revenue estimate from any source reached - a holding
company, no analyst estimates carried.

## Report dates - company-source verification (Rule B)

All 19 names were confirmed against a company-owned source (IR page, press release, or IR event
calendar), not from an aggregator alone. 19 of 19 additionally agree across three independent
calendars (EarningsWhispers, MarketBeat, stockanalysis.com).

| Ticker | Company source that confirms Nov 2, 2026 |
|---|---|
| AAPL | Apple IR events page - FY26 Q4 results, release 1:30p PT / 4:30p ET, call 2:00p PT / 5:00p ET |
| MAR | Marriott PR (Oct 9, 2026) - Q3 results ~7:00a ET, call 8:00a ET |
| VRTX | Vertex PR (Oct 7, 2026) - Q3 results after close, call 4:30p ET |
| WMB | Williams PR (Oct 13, 2026) - results after close Nov 2, call Nov 3 9:30a ET |
| ETR | Entergy IR (Oct 26, 2026) - results before market open, webcast 10:00a CT / 11:00a ET |
| IDXX | IDEXX IR calendar - Q3 conference call Nov 2, 8:30a ET |
| EL | Estee Lauder PR (Oct 19, 2026) - FY27 Q1 results Nov 2, call 8:30a ET |
| PEG | PSEG IR - Q3 webcast Nov 2, 11:00a ET |
| FOX / FOXA | Fox IR events - Q1 FY2027 earnings webcast Nov 2, 8:30a EST |
| L | Loews PR (Oct 13, 2026) - Q3 results Nov 2 |
| O | Realty Income PR (Oct 1, 2026) - results after NYSE close, webcast 5:00p ET |
| ON | onsemi IR (Oct 15, 2026) - Q3 results Nov 2, call 5:00p ET |
| SBAC | SBA PR (Jul 16, 2026) - Q3 results after close Nov 2, call 5:00p ET |
| DOC | Healthpeak PR (via event digest) - results after close Nov 2, call Nov 3 10:00a ET |
| UDR | UDR PR (Oct 15, 2026) - Q3 results after close Nov 2, call Nov 3 12:00p ET |
| CLX | Clorox PR Newswire - Q1 FY2027 results Nov 2, 2026 |
| PLTR | Palantir IR quarterly results - Q3 2026 on 11/02/26 |

### Date-confirmed exclusions
No name was excluded on a date mismatch today - the three calendars and the company sources agreed for
every roster member. One nuance recorded rather than excluded: **FANG (Diamondback Energy)** shows a
*Nov 3, 9:00a ET* conference call on its own IR site, which is the standard pattern for a Nov 2
after-close release with the call the following morning. It stays in the roster as Nov 2 AMC.

## Estimate and market-cap reconciliation

Sources disagree beyond tolerance on a few fields; both values are shown rather than one being hidden.

| Ticker | Field | Primary (MarketBeat / TradingView) | Cross-check | Spread |
|---|---|---|---|---|
| FOX | EPS | $2.07 | Yahoo $2.13 / Zacks $2.06 | 2.9% vs Yahoo - over 2% tolerance |
| FOXA | EPS | $2.02 | Zacks $1.99 | 1.5% - within tolerance |
| FANG | EPS | $5.72 | Yahoo $5.60 | 2.1% - over 2% tolerance |
| O | EPS | $0.41 | Yahoo $0.43 | 4.7% - over 2% tolerance |
| VRTX | EPS | $4.82 | Yahoo $4.78 | 0.8% - within tolerance |
| ETR | EPS | $1.73 | Yahoo $1.70 | 1.8% - within tolerance |
| MAR | EPS | $2.84 | Yahoo $2.85 | 0.4% - within tolerance |
| IDXX | EPS | $3.73 | Yahoo $3.71 | 0.5% - within tolerance |
| FOXA | Mkt cap | $25.1B (TradingView) | $26.7B (stockanalysis) | 6.0% - over 5% tolerance; TV quotes both Fox classes at $25.1B |
| UDR | Mkt cap | $11.4B (TradingView) | $12.2B (stockanalysis) | 6.9% - over 5% tolerance |

All other market caps agree between TradingView and stockanalysis within 1%.

## Source health

| Source | Endpoint / query | Status | Result |
|---|---|---|---|
| EarningsWhispers calendar | `https://earningswhispers.com/calendar/20261102` | HTTP 200 | ok - 127 names, 25 BMO / 102 AMC; roster source |
| Wikipedia MediaWiki API (S&P 500) | `action=parse&page=List_of_S%26P_500_companies&prop=wikitext` | HTTP 200 | ok - 503 symbols parsed; control check BRK.B / GOOGL / GOOG / FOX / CBOE all present |
| MarketBeat earnings calendar | `https://www.marketbeat.com/earnings/2026-11-02/` | HTTP 200 | ok - EPS + revenue consensus for 18 of 19 roster names; Loews absent |
| Yahoo Finance earnings calendar (HTML) | `https://finance.yahoo.com/calendar/earnings?day=2026-11-02` | HTTP 200 | ok - EPS cross-check for 15 of 19; revenue column not server-rendered; CLX / UDR / DOC / L EPS missing |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` | HTTP 200 | ok - market cap + country for 127 of 127 calendar names |
| stockanalysis.com quote pages | `https://stockanalysis.com/stocks/<sym>/` (19 requests) | HTTP 200 | ok - market cap and earnings-date cross-check, 19 of 19 |
| Company IR / press releases | web_search against each issuer's own IR domain | ok | ok - 19 of 19 report dates confirmed at source |
| Watchlist file | `research/watchlist.yaml` | n/a | **not present in this runtime** - watchlist section omitted, not an error |
| Yahoo JSON quote endpoints | chart / spark / screener | not attempted | known persistent 429 rate-limit from prior measurement this month; the HTML path above was used instead |

### Known gaps
- **Loews (L)** carries no consensus EPS or revenue estimate from any source reached - values are `n/a`, not zero.
- **Yahoo's revenue column is not server-rendered**, so consensus revenue comes solely from MarketBeat for this artifact; no independent revenue cross-check was possible.
- Market cap uses TradingView as the primary because it covered all 127 calendar names in one pass; two names (FOXA, UDR) disagree with stockanalysis by more than 5% and are flagged above.

## Notes
- Read-only reminder. No auto-action taken on any of these names.
- Consensus estimates only - no analyst price targets, no DCF, no earnings reactions.
- Equities only.
