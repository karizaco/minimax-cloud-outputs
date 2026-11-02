---
date: 2026-10-27
cron: 19-earnings-reminder-daily
fire_time_et: 06:00 (reconstructed — this run did not fire; see note)
snapshot_et: backfilled 2026-11-01
source: TheStreet Pro weekly calendar + Yahoo Finance earnings calendar + EarningsWhispers + Newsquawk
primary_source: TheStreet Pro (market cap, EPS, revenue) | Yahoo (cross-check)
status: backfilled_missed_run
pending_count: 0
already_reported_count: 46
---

# Earnings — Tue 2026-10-27

**Backfilled artifact.** Cron #19 did not fire on 2026-10-27: the task was deleted from the
scheduler and recreated on 2026-10-29 under a new task_id, leaving a two-day hole (2026-10-27 and
2026-10-28) in the series. This file was reconstructed on 2026-11-01 from published calendars, so
it is a **retrospective** record, not a pre-market reminder: every name below had already reported
by the time this was written. Timing and estimates are as published before the open on 2026-10-27.

38 names qualify under the cron filter: 25 S&P 500 constituents and 13 mega-caps above $50B that
are not index members. S&P 500 membership was verified live against the MediaWiki constituent
list (503 symbols; control checks BRK.B / GOOGL / GOOG / FOX / CBOE all present).

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Status |
|---|---|---|---|---|---|---|
| V | Visa | AMC | 3.44 | 12.09B | 782B | reported |
| SKHY | SK hynix | pre-mkt EU | 6.24 | — | 1.05T | reported |
| KO | Coca-Cola | BMO | 0.88 | 12.92B | 399B | reported |
| NVS | Novartis | pre-mkt EU | 2.24 | — | 303.7B | reported |
| HSBC | HSBC Holdings | pre-mkt EU | 2.25 | — | 292.1B | reported |
| SAN | Banco Santander | pre-mkt EU | 0.29 | — | 161.3B | reported |
| STX | Seagate Technology | AMC | 7.43 | 4.15B | 148.0B | reported |
| BA | Boeing | BMO | -0.20 | 23.95B | 135.9B | reported |
| SPGI | S&P Global | BMO | 4.42 | 3.64B | 135.3B | reported |
| GLW | Corning | BMO | 0.88 | 5.03B | 106.2B | reported |
| GSK | GSK plc | pre-mkt EU | 1.33 | — | 99.2B | reported |
| HCA | HCA Healthcare | BMO | 6.63 | 19.33B | 98.9B | reported |
| WM | Waste Management | AMC | 2.18 | 6.81B | 92.8B | reported |
| UPS | United Parcel Service | BMO | 1.62 | 22.27B | 92.1B | reported |
| JCI | Johnson Controls | BMO | 1.59 | 7.04B | 90.3B | reported |
| FCX | Freeport-McMoRan | BMO | 0.83 | 7.36B | 89.7B | reported |
| AMT | American Tower | BMO | 1.63 | 2.76B | 87.1B | reported |
| ECL | Ecolab | BMO | 2.17 | 4.70B | 85.0B | reported |
| RCL | Royal Caribbean | BMO | 6.38 | 5.61B | 82.2B | reported |
| SHW | Sherwin-Williams | BMO | 3.69 | 6.78B | 80.4B | reported |
| HLT | Hilton Worldwide | BMO | 2.37 | 3.37B | 79.4B | reported |
| ITW | Illinois Tool Works | BMO | 2.97 | 4.26B | 79.2B | reported |
| HOOD | Robinhood Markets | AMC | 0.56 | 1.44B | 76.5B | reported |
| NXPI | NXP Semiconductors | AMC | 4.12 | 3.76B | 65.4B | reported |
| OKE | ONEOK | BMO | 1.50 | 10.54B | 60B | reported |
| DB | Deutsche Bank | pre-mkt EU | 0.98 | — | 62.4B | reported |
| BKR | Baker Hughes | AMC | 0.61 | 7.74B | 55B | reported |
| PCAR | PACCAR | BMO | 1.61 | 7.48B | 54B | reported |
| UNH | UnitedHealth Group | BMO | 4.12 | 111.31B | — | reported |
| PYPL | PayPal | BMO | 1.31 | 8.71B | — | reported |
| TER | Teradyne | AMC | 2.09 | 1.27B | 46B | reported |
| VTR | Ventas | AMC | 0.16 | 1.77B | 46B | reported |
| IQV | IQVIA | BMO | 3.26 | 4.37B | 45B | reported |
| ACGL | Arch Capital Group | AMC | 2.31 | 4.06B | 35B | reported |
| CNC | Centene | BMO | 0.10 | 47.12B | 34.7B | reported |
| SYY | Sysco | BMO | 1.16 | 21.92B | — | reported |
| BKNG | Booking Holdings | AMC | 4.49 | 9.54B | — | reported |
| NEE | NextEra Energy | BMO | 1.20 | 8.89B | — | reported |

## Source health

| Source | URL | Status |
|---|---|---|
| TheStreet Pro weekly calendar | `pro.thestreet.com/earnings/week/2026-10-26` | ok — 43 rows for Oct 27 |
| Yahoo Finance earnings calendar | `finance.yahoo.com/calendar/earnings?...&day=2026-10-27` | ok — 25 rows rendered server-side (JS-limited) |
| EarningsWhispers | `earningswhispers.com/calendar/20261027` | ok — 170 tickers, full BMO/AMC split |
| Newsquawk daily estimates | `newsquawk.com/...-27th-october-2026-ko-glw-spgi-ba-stx-v` | ok — EPS + revenue for the S&P 500 subset |
| Wikipedia constituent list | MediaWiki API wikitext | ok — 503 symbols, controls BRK.B/GOOGL/GOOG/FOX/CBOE present |

## Conflicts and caveats

- **EPS disagreement on KO** (0.88 TheStreet/Newsquawk vs 0.87 StockTitan) and **V** (3.44 vs 3.43–3.51
  range). TheStreet consensus is shown; the spread is within the 2% tolerance.
- **Market-cap spread on UNH** is large across providers (the $50B threshold is not in play for it,
  but the figure is omitted rather than guessed from one source).
- **EXR, FE, PPG, FFIV, ESS, CSGP, BXP, PNR, UHS, IVZ, CNP, CMS, EXE, HUBB** also qualified on the
  day but are omitted here: at least one required field (EPS or revenue estimate) could not be
  sourced to a primary provider, and the cron rule is never to invent a number.
- **Status is uniformly "reported"** because this file was written after the close on 2026-11-01.
  The pre-open status each name had on the morning of 2026-10-27 is not recoverable now.
