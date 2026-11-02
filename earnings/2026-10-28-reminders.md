---
date: 2026-10-28
cron: 19-earnings-reminder-daily
fire_time_et: 06:00 (reconstructed — this run did not fire; see note)
snapshot_et: backfilled 2026-11-01
source: TheStreet Pro weekly calendar + Yahoo Finance earnings calendar + EarningsWhispers + StockTitan
primary_source: TheStreet Pro (market cap, EPS, revenue) | Yahoo (cross-check)
status: backfilled_missed_run
pending_count: 0
already_reported_count: 34
---

# Earnings — Wed 2026-10-28

**Backfilled artifact.** Cron #19 did not fire on 2026-10-28: the task was deleted from the
scheduler and recreated on 2026-10-29 under a new task_id, leaving a two-day hole (2026-10-27 and
2026-10-28) in the series. This file was reconstructed on 2026-11-01 from published calendars, so
it is a **retrospective** record, not a pre-market reminder: every name below had already reported
by the time this was written. Timing and estimates are as published before the open on 2026-10-28.

Heaviest day of the week by value — 34 names qualify under the cron filter: 23 S&P 500
constituents and 11 mega-caps above $50B that are not index members. S&P 500 membership was
verified live against the MediaWiki constituent list (503 symbols; control checks BRK.B / GOOGL /
GOOG / FOX / CBOE all present).

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Status |
|---|---|---|---|---|---|---|
| MSFT | Microsoft | AMC | 4.72 | 90.62B | 3.94T | reported |
| GOOGL | Alphabet Class A | AMC | 3.01 | 127.97B | 3.44T | reported |
| GOOG | Alphabet Class C | AMC | 3.04 | — | 3.42T | reported |
| GEV | GE Vernova | BMO | 4.01 | 11.99B | 235B | reported |
| KLAC | KLA | AMC | 1.18 | 4.04B | 218B | reported |
| APH | Amphenol | BMO | 0.73 | 9.49B | 202B | reported |
| TMUS | T-Mobile US | BMO | 2.91 | 23.15B | 156.6B | reported |
| UBS | UBS Group | pre-mkt EU | 0.96 | — | 144.5B | reported |
| BBVA | Banco Bilbao Vizcaya | pre-mkt EU | 0.62 | — | 128.9B | reported |
| ADP | Automatic Data Processing | BMO | 2.77 | 5.48B | 113.2B | reported |
| EQNR | Equinor | pre-mkt EU | 1.35 | — | 115.4B | reported |
| PSX | Phillips 66 | BMO | 11.79 | 44.91B | 106.7B | reported |
| NOW | ServiceNow | AMC | 1.02 | — | 109.1B | reported |
| EQIX | Equinix | AMC | 3.96 | — | 100.3B | reported |
| FTNT | Fortinet | AMC | 0.86 | — | 99.8B | reported |
| VRT | Vertiv Holdings | BMO | 1.82 | — | 89.5B | reported |
| AEM | Agnico Eagle Mines | AMC | 2.56 | — | 83.6B | reported |
| CP | Canadian Pacific Kansas City | AMC | 1.31 | — | 78.0B | reported |
| FDX | FedEx | AMC | 3.38 | — | 73.4B | reported |
| AEP | American Electric Power | BMO | 2.04 | 6.55B | 70.4B | reported |
| ORLY | O'Reilly Automotive | AMC | 0.93 | 5.01B | 71.3B | reported |
| AON | Aon | BMO | 3.30 | 4.08B | 68.3B | reported |
| TEL | TE Connectivity | BMO | 3.07 | 5.29B | 64.0B | reported |
| BSX | Boston Scientific | BMO | 0.72 | 5.09B | 61.9B | reported |
| EBAY | eBay | AMC | 1.42 | 3.12B | 54.1B | reported |
| F | Ford Motor | AMC | 0.93 | 47.2B | 48.9B | reported |
| CMG | Chipotle Mexican Grill | AMC | 1.02 | 3.3B | 40.3B | reported |
| CVNA | Carvana | AMC | — | — | — | reported |
| ALGN | Align Technology | AMC | — | — | — | reported |
| SAN | Banco Santander | pre-mkt EU | 0.26 | — | — | reported |
| GSK | GSK plc | pre-mkt EU | 1.40 | — | — | reported |
| ETSY | Etsy | BMO | 0.76 | 668.05M | — | reported |
| VFC | VF Corporation | BMO | — | — | — | reported |

## Source health

| Source | URL | Status |
|---|---|---|
| TheStreet Pro weekly calendar | `pro.thestreet.com/earnings/week/2026-10-26` | ok — Wed 28 rows (EPS + rev + mcap) |
| TheStreet Pro day page | `pro.thestreet.com/earnings/2026-10-28` | ok — cross-check on EPS/revenue |
| Yahoo Finance earnings calendar | `finance.yahoo.com/calendar/earnings?...&day=2026-10-28` | ok — 25 rows rendered server-side (JS-limited) |
| EarningsWhispers | `earningswhispers.com/calendar/20261028` | ok — 218 tickers, full BMO/AMC split |
| StockTitan weekly | `stocktitan.net/articles/earnings-calendar-week-of-october-26-2026` | ok — call times + consensus EPS |
| Investing.com | `in.investing.com/news/...-microsoft-google-ford-and-more-set-to-report-earnings-wednesday` | ok — EPS + revenue for the BMO subset |
| Wikipedia constituent list | MediaWiki API wikitext | ok — 503 symbols, controls BRK.B/GOOGL/GOOG/FOX/CBOE present |

## Conflicts and caveats

- **Alphabet is listed twice** (GOOGL and GOOG) because both share classes report and the filter
  is per-ticker. EPS differs slightly: 3.01 (GOOGL) vs 3.04 (GOOG).
- **MSFT EPS consensus spread $4.71–$4.82** across providers; TheStreet 4.72 shown. GOOGL EPS
  ranged $2.94–$3.11 across providers — StockTitan/Nasdaq consensus is ~$2.94–$3.03 and Yahoo's
  calendar shows 3.01; the 3.01 figure is shown and the spread is inside the 2% tolerance for
  most providers but sits above it for the highest. Flagged rather than smoothed.
- **PSX EPS is the widest GAAP/adjusted gap** on the board: 11.73–11.84 adjusted vs a GAAP
  reference near 14. The 11.79 Yahoo value is shown; this is a definitional spread, not a
  data conflict.
- **GOOGL / GOOG / MSFT revenue estimates disagree across providers** (MSFT $90.6B vs $92.5B;
  GOOGL $127.97B vs $132.0B). TheStreet is primary; the gap is recorded here.
- **CVNA, ALGN, ETSY, VFC, SAN, GSK** are carried with partial fields because a primary estimate
  was not obtainable for every column; the cron rule is never to invent a number, so missing
  cells stay blank.
- **Status is uniformly "reported"** because this file was written after the close on 2026-11-01.
  The pre-open status each name had on the morning of 2026-10-28 is not recoverable now.
- **FOMC decision landed the same day at 14:00 ET** — a same-day macro event for the reader.
