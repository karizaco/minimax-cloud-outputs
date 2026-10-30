---
date: 2026-10-30
cron: 19-earnings-reminder-daily
fire_time_et: 06:02
snapshot_et: 06:14
source: Yahoo Finance earnings calendar + Earnings Whispers + MarketBeat
primary_source: Yahoo (market cap, EPS) | MarketBeat (revenue, EPS fallback)
status: ok
pending_count: 16
already_reported_count: 4
---

# Earnings — Fri 2026-10-30

Read-only reminder. 20 names qualify: **13 S&P 500 constituents** plus **7 mega-caps above $50B**
that are not in the index. 16 are still pending; 4 already printed before this cron fired.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Status |
|---|---|---|---|---|---|---|
| XOM | ExxonMobil Holdings | BMO 06:30 ET | 4.04 | 105.43B | 749.2B | pending |
| ABBV | AbbVie | BMO | 3.77 | 17.32B | 509.4B | pending |
| CVX | Chevron | BMO | 4.83 | 61.33B | 451.9B | pending |
| AZN | AstraZeneca | 03:00 ET (07:00 GMT) | 2.59 | 16.2B | 269.6B | reported |
| BP | BP plc | 03:00 ET (07:00 GMT) | 2.62 | 63.14B | 129.4B | reported |
| IITSF | Intesa Sanpaolo (OTC ADR) | TNS — board approves 30 Oct | 0.15 (C$) | 7.88B | 129.4B | pending |
| SNY | Sanofi | 00:30 ET (06:30 CET) | 1.51 | 14.87B | 101.6B | reported |
| GD | General Dynamics | BMO | 4.13 | 13.72B | 100.2B | pending |
| REGN | Regeneron Pharmaceuticals | BMO | 16.25 | 4.56B | 83.6B | pending |
| CNI | Canadian National Railway | BMO 07:30 ET | 2.08 (C$) | 3.27B | 74.5B | pending |
| CL | Colgate-Palmolive | BMO | 0.93 | 5.34B | 73.7B | pending |
| NWG | NatWest Group | 03:00 ET (07:00 GMT) | 0.51 | 6.18B | 66.9B | reported |
| IMO | Imperial Oil | BMO | 3.43 | 12.42B | 63.3B | pending |
| D | Dominion Energy | BMO | 1.21 | 4.90B | 57.2B | pending |
| EXC | Exelon | BMO | 0.79 | 6.76B | 47.2B | pending |
| KVUE | Kenvue | BMO, call 09:30 ET | 0.29 | 3.86B | 37.2B | pending |
| CBOE | Cboe Global Markets | BMO, call 08:30 ET | 3.43 | 707.3M | 32.9B | pending |
| CHD | Church & Dwight | BMO | 0.90 | 1.58B | 25.0B | pending |
| LYB | LyondellBasell | BMO | 2.55 | 8.87B | 21.0B | pending |
| FRT | Federal Realty Investment Trust | BMO, call 09:30 ET | 0.71 | 336.6M | 9.7B | pending |

`EPS est` and `Mkt cap` are the Yahoo Finance calendar values; `Rev est` is the MarketBeat
consensus. Fallbacks and unit caveats are listed under **Estimate conflicts** below.

## Already reported (before this cron fired)

European issuers released in their own morning, so four of the largest names on the calendar are
already out of the bag by 06:00 ET. Do not read their rows as a pending catalyst.

- **BP** — released 03:00 ET. Underlying replacement cost profit $8.46B vs a $7.33B company-compiled
  consensus and $2.2B a year ago; profit attributable to shareholders $4.70B vs $1.16B a year ago.
  Refining indicator margin $46.7/bbl (from $29.6 in Q2, $15.8 a year ago). Net debt fell to $13.87B
  from $26.05B, hitting the net-debt target a year early. Underlying RC profit per ADS $3.26.
- **AZN** — released 03:00 ET. Q3 revenue $16.21B, +7%; core EPS $2.79, +17% at CER (+19% at
  constant currency). FY2026 guidance reaffirmed. Webcast 14:30 GMT / 10:30 ET.
- **NWG** — released 03:00 ET. Attributable profit £1,532m, **−4.4% YoY**, against a consensus that
  had income and NIM broadly on plan (income £4.64B vs £4.6B expected; NIM 2.50% vs 2.51% expected).
  Operating profit £2,225m, RoTE 21.6%, EPS 19.3p, CET1 13.5%. Impairment charges £277m, +97.9%
  YoY. FY26 guidance reaffirmed (underlying income ~£17.9B, RoTE >19%). Shares fell in early
  London trading; the ADR was −7.5% on the Nasdaq premarket print at 06:09 ET.
- **SNY** — released 00:30 ET (press release stamped 06:30 CET). Q3 sales €14,444m, +14.3% at CER;
  business EPS €3.55, +19.6% at CER; IFRS EPS €2.52. FY2026 guidance **upgraded**. Webcast
  13:30 CET / 08:30 ET.

## Pending — the US session's names

- **XOM and CVX** land back-to-back before the open (XOM ~06:30 ET, CVX shortly after; calls at
  09:30 and 11:00 ET). Both faces a large year-over-year step-up: XOM consensus $4.04 on $105.4B
  against $1.88 on $83.3B a year ago, CVX $4.83 on $61.3B against $1.85 on $48.2B. Refining margin
  capture is the swing factor in both, with UBS at $4.14 on XOM above consensus.
- **REGN** consensus $16.25 versus $11.83 a year ago, and the widest EPS dispersion of any name
  here (see below).
- **CNI** reports at 07:30 ET, the only large name with a confirmed time after this cron fired.
- **GD** $4.13 on $13.7B (call 09:00 ET) — defense budget continuity is the setup.
- **CBOE** $3.43 on ~$705M (call 08:30 ET) — options volume momentum against a Q2 record of $731.6M.
- **KVUE** $0.29 on $3.86B (call 09:30 ET) — the only date on this list confirmed by the company
  as of today.

## Notes

- **No watchlist section.** `research/watchlist.yaml` is a local-only file on the Mavis host and does
  not exist in the Cloud sandbox, so no watchlist cross-reference was possible. The watchlist
  section is omitted rather than shipped empty.
- **S&P 500 membership was verified live**, not recalled. The MediaWiki wikitext for
  `List_of_S&P_500_companies` carries **503** symbol templates — 345 `{{NyseSymbol}}`,
  157 `{{NasdaqSymbol}}` and **1 `{{BZX link|CBOE}}`**. A parse that only handles the first two
  templates silently yields 502 and drops **CBOE**, which is an S&P 500 constituent reporting today.
  Control symbols BRK.B, GOOGL, GOOG and FOX are all present. The parse was cross-checked against
  an independent CSV of the same list (503 rows); the only differences are `BRK.B` vs `BRK-B`
  formatting and the CBOE row.
- **Magna International (MGA) and nVent Electric (NVT) are not S&P 500 constituents** and were
  excluded. Both are absent from the live constituent list and the independent CSV; a third source
  states outright that Magna is not in the index. At $17.2B and $22.5B both are also below the $50B
  mega-cap floor. Including them would have been wrong on both counts.
- **Rule B — report dates confirmed against company sources** for every name near the inclusion
  boundary. Excluded on date:
  - **Shell (SHEL)** — released Thu 29 Oct (07:00 GMT), confirmed on shell.com.
  - **TotalEnergies (TTE)** — released Thu 29 Oct, confirmed on totalenergies.com.
  - **HSBC** — released Tue 27 Oct, confirmed on hsbc.com/investors.
  - **Novartis (NVS)** — 27 Oct, confirmed on novartis.com/events.
  - **Roche** — Q3 sales published 22 Oct, confirmed on roche.com.
  - **Eni** — Q3 results 23 Oct, confirmed on eni.com financial calendar.
  - **Santander** — 28 Oct, confirmed on santander.com press room.
  - **Deutsche Bank** — 28 Oct, confirmed on db.com media release.
  - **Mercedes-Benz Group** — 28 Oct, confirmed on group.mercedes-benz.com.
  - **Bayer** — Q3 report dated 3 Nov, confirmed on bayer.com.
  - **Intesa Sanpaolo** — the first pass on the IR page read as 23 Oct, but the H1 2026 press release
    states the Board meets on **30 October 2026** to approve the consolidated results as at
    30 September. Date confirmed; the name stays in.
  - **ASML** — 14 Oct; **TSMC** — 15 Oct. Both confirmed on their IR sites.
- **NWG** was not on the Earnings Whispers forward calendar at all. The company IR page and the
  results centre both confirm a 07:00 GMT (03:00 ET) release on 30 October, so it is included on
  company authority rather than the aggregator.
- **IITSF carries three caveats**: it is an unsponsored OTC ADR rather than a US exchange listing;
  the release time is not published (the board approves the results during 30 October); and the
  EPS estimate is disputed — Yahoo and TradingEconomics show 0.15 in EUR while WSJ and MarketBeat
  show 1.03–1.04 for the same quarter, a spread too large to reconcile from the available feeds.
  Market cap is also inconsistent between sources: $129.4B on the Yahoo quote page against $113.5B
  in the Yahoo earnings calendar.
- **Standard Chartered** was checked and carries no date for 30 October on its IR page; at roughly
  $35B it would fall below the $50B floor in any case.

## Estimate conflicts (Rule C)

Primary source per field: **market cap and EPS from the Yahoo Finance earnings calendar**;
**revenue from MarketBeat**, falling back to Investing.com, Zacks/Seeking Alpha or Earnings
Whispers where MarketBeat publishes nothing. Spreads beyond tolerance (market cap >5%, EPS >2%,
revenue >5%) are recorded here rather than silently averaged.

| Ticker | Field | Spread | Detail |
|---|---|---|---|
| XOM | EPS | 3.90 – 4.12 (5.6%) | MarketBeat 4.12, Yahoo 4.04, Investing.com 3.99, 247wallst 3.981, Zacks 3.90 |
| XOM | Revenue | 102.98B – 115.45B (12.1%) | Investing.com 115.45B, MarketBeat 105.43B, 247wallst 104.03B, Zacks 102.98B |
| REGN | EPS | 13.76 – 16.48 (19.8%) | MarketBeat 16.42, Yahoo 16.25, Zacks/whispers 16.11–16.48, MetaCap 13.76 (likely stale) |
| IMO | Revenue | 11.09B – 15.44B (39.3%) | MarketBeat 12.42B, Seeking Alpha 11.09B, Earnings Whispers 15.44B |
| SNY | EPS | 1.51 – 1.63 (7.9%) | Yahoo 1.51 (IFRS basis), MarketBeat/MetaCap 1.63 (business EPS) |
| CVX | EPS | 4.78 – 4.88 (2.1%) | Investing.com 4.88, MarketBeat 4.86, Yahoo 4.83, MetaCap/whispers 4.78 |
| CNI | EPS | currency, not a conflict | Yahoo's 2.08 is CAD; US$1.49 is the same consensus converted |
| FRT | EPS | 0.71 vs 1.85 | 0.71 is GAAP EPS (Yahoo, MarketBeat, Zacks, TradingView); 1.85 is the FFO-style figure on some feeds |
| CBOE | Mkt cap | 32.85B – 35.14B (7.0%) | Yahoo calendar 32.85B, Nasdaq close-derived 35.14B |
| BP | Revenue | 63.14B vs 66.19B (4.8%) | MarketBeat 63.14B, Earnings Whispers 66.19B |

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| Wikipedia MediaWiki API | `action=parse&page=List_of_S%26P_500_companies&prop=wikitext` | ok | 503 symbols; control checks BRK.B / GOOGL / GOOG / FOX all present |
| Wikipedia rendered HTML | `action=parse&prop=text` | ok | cross-check only; agrees on membership, confirms the `{{BZX link}}` row |
| GitHub datasets CSV | `raw.githubusercontent.com/datasets/s-and-p-500-companies/.../constituents.csv` | ok | 503 rows; independent match to the Wikipedia parse |
| Earnings Whispers calendar page | `earningswhispers.com/calendar/20261030` | ok | 69 names, 69 BMO / 0 AMC |
| Earnings Whispers API | `GET /api/caldata/20261030` with `Accept: application/json` | ok | 57 rows, all `releaseTime=1`; needs the JSON Accept header or it returns an error page |
| Nasdaq quote API | `api.nasdaq.com/api/quote/{SYM}/{summary,info}?assetclass=stocks` | ok | market cap + close-based mcap for all 19 US-listed names |
| MarketBeat earnings pages | `/earnings/reports/2026-10-30-<slug>-stock/` | ok | consensus EPS + revenue for 17 of 20 names |
| Investing.com calendar | `investing.com/earnings-calendar` | ok (via search) | direct fetch returns HTTP 403; values recovered through search |
| Yahoo earnings calendar | `finance.yahoo.com/calendar/earnings?day=2026-10-30` | ok (via search) | 62 names; direct `web_fetch` timed out, HTML is JS-rendered |
| Yahoo quote JSON | `query1/query2.finance.yahoo.com/v1/finance/calendar/earnings` | failed:HTTP 404 | endpoint shape no longer served; table recovered via search instead |
| MarketBeat report pages (direct fetch) | `marketbeat.com/earnings/reports/2026-10-30-{exxon-mobil,cboe-global-markets,astrazeneca}-*-stock/` | failed:file load failed | three slugs 404'd; same values recovered via search and other providers |
| slickcharts / datahub / S&P Global | constituent-list cross-checks | failed:HTTP 403 / 404 | all three blocked; the GitHub CSV carried the cross-check instead |
| metacap.si, digrin.com calendars | daily calendar pages | failed:timeout | both exceeded the 15s fetch window; used only as search-surfaced cross-checks |

## Deliberately not used

- No watchlist file exists in this runtime, so no watchlist section was produced.
- Analyst price targets, valuation work and earnings reactions are out of scope for this reminder and
  were not collected, beyond the single intraday ADR move quoted for NWG as evidence of an
  already-printed result.
- No audit log was written; on Cloud the chat reply and this artifact are the record.
