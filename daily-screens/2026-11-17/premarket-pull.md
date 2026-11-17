# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled until the cached vintage STOPS CHANGING (min 2, max 4) and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks. `tape_lag_min` is how many minutes the newest print is BEHIND the wall clock - the number that makes staleness visible._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Driver | Tape newest | Lag (min) | Pulls | Vintages | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ALM** | 8.1500 | +0.86% | 250 | 2,055 | 35,505 | -0.12% | BORDERLINE_INTRADAY | NO_MOVE | 08:19:23 | 17 | 2 | 08:19:23 | 8.08 | Pre-Market |
| **ALNY** | 159.7300 | +1.45% | 25 | 4,051 | 1,155 | -0.05% | BELOW | NO_MOVE | 08:18:16 | 18 | 2 | 08:18:16 | 160.55 | Pre-Market |
| **CBRS** | 100.9900 | +0.58% | 20 | 2,032 | 197,853 | +0.06% | BELOW | NO_MOVE | 08:21:17 | 15 | 2 | 08:21:17 | 99.60 | Pre-Market |
| **CGON** | 84.7800 | -0.11% | 5 | 423 | 1,969 | +0.26% | BELOW | SECTOR_BETA | 08:21:01 | 16 | 2 | 08:21:01 | 84.48 | Pre-Market |
| **CPRI** | 20.5500 | -3.89% | 100 | 1,975 | 12,685 | -1.75% | BORDERLINE_INTRADAY | IDIOSYNCRATIC | 08:03:00 | 38 | 2 | 08:03:00 | 19.65 | Pre-Market |
| **FENC** | 12.7600 | +0.31% | 10 | 128 | 377 | +0.31% | BORDERLINE_INTRADAY | SECTOR_BETA | 07:33:50 | 67 | 2 | 07:33:50 | 12.70 | Pre-Market |
| **FOUR** | 42.4800 | -0.31% | 100 | 4,235 | 1,379 | +5.93% | BORDERLINE_TAPE_ONLY | NO_MOVE | 08:00:02 | 37 | 2 | 08:00:02 | 42.30 | Pre-Market |
| **MOD** | 130.5500 | +1.24% | 8 | 1,057 | 7,137 | +2.26% | BELOW | SECTOR_BETA | 08:25:03 | 16 | 2 | 08:25:03 | 129.50 | Pre-Market |
| **SENS** | 10.9000 | +2.84% | 25 | 280 | 3,436 | +3.21% | BELOW | IDIOSYNCRATIC | 08:20:26 | 20 | 3 | 08:14:33, 08:20:26 | 11.05 | Pre-Market |
| **TNDM** | 18.4800 | +0.65% | 100 | 1,860 | 6,047 | +0.21% | BORDERLINE_INTRADAY | NO_MOVE | 08:10:19 | 26 | 2 | 08:10:19 | 18.80 | Pre-Market |
| **U** | 51.8800 | -0.08% | 2 | 104 | 61,428 | -0.39% | BELOW | NO_MOVE | 08:19:26 | 17 | 2 | 08:19:26 | 51.69 | Pre-Market |
| **VKTX** | 26.8000 | +0.07% | 50 | 1,341 | 9,869 | +0.26% | BELOW | NO_MOVE | 08:10:58 | 26 | 2 | 08:10:58 | 26.73 | Pre-Market |

_Widest absolute gap on any source: 3.89% against a 4.00% trigger - a 1.03x margin, so the flag decision is immune to whichever cached vintage a source returns._
_Tape lag (newest print behind the wall clock): median 20 min, max 67 min._
_Tape waves: wave 1 at 08:36:46 ET (12 names); wave 2 at 08:40:38 ET (4 names)_

_12 of 12 symbols priced._
