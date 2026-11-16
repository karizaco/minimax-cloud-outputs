# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled until the cached vintage STOPS CHANGING (min 2, max 4) and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks. `tape_lag_min` is how many minutes the newest print is BEHIND the wall clock - the number that makes staleness visible._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Driver | Tape newest | Lag (min) | Pulls | Vintages | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AMD** | 534.0600 | -5.54% | 17 | 8,576 | 1,345,581 | -5.90% | BORDERLINE_THIN | SECTOR_BETA | 08:23:00 | 16 | 2 | 08:23:00, 08:23:44 | 521.20 | Pre-Market |
| **ANET** | 197.2900 | -3.64% | 2 | 380 | 67,226 | -3.75% | BORDERLINE_INTRADAY | SECTOR_BETA | 08:22:03 | 17 | 2 | 08:22:03 | 194.77 | Pre-Market |
| **CHA** | 14.3700 | -0.83% | 6 | 86 | 29,074 | -0.83% | BELOW | NO_MOVE | 08:19:01 | 17 | 2 | 08:19:01 | 14.37 | Pre-Market |
| **DPC** | 34.2600 | -0.03% | 1 | 34 | 59 | -0.03% | BELOW | NO_MOVE | 07:00:00 | 99 | 2 | 07:00:00 | 34.26 | Pre-Market |
| **FIGR** | 25.2200 | -5.71% | 1 | 24 | 51,042 | -5.04% | BORDERLINE_THIN | IDIOSYNCRATIC | 08:23:48 | 16 | 4 | 08:11:15, 08:23:48 | 24.83 | Pre-Market |
| **HUBS** | 217.2500 | +3.57% | 10 | 2,250 | 4,105 | +3.26% | BORDERLINE_INTRADAY | IDIOSYNCRATIC | 08:23:01 | 16 | 2 | 08:23:01 | 217.00 | Pre-Market |
| **IBP** | 229.0000 | +0.39% | 1 | 230 | 69 | +0.00% | BELOW | NO_MOVE | 08:04:07 | 32 | 2 | 08:04:07 | 229.00 | Pre-Market |
| **IRTC** | 91.9100 | -0.48% | 1 | 91 | 77 | -0.45% | BELOW | NO_MOVE | 08:11:37 | 25 | 2 | 08:11:37 | 90.12 | Pre-Market |
| **LMND** | 44.1900 | -1.54% | 20 | 870 | 5,632 | -1.47% | BELOW | MARKET_BETA | 08:10:41 | 26 | 2 | 08:10:41 | 44.19 | Pre-Market |
| **LUNR** | 13.0000 | -2.92% | 78 | 984 | 176,601 | -3.69% | BORDERLINE_INTRADAY | SECTOR_BETA | 08:22:04 | 17 | 2 | 08:22:04 | 12.65 | Pre-Market |
| **PLBL** | 7.2400 | +0.00% | 13 | 94 | 61 | +0.00% | BELOW | NO_MOVE | 07:05:45 | 94 | 2 | 07:05:45 | 7.24 | Pre-Market |
| **TOP** | 17.0000 | -0.71% | 1 | 17 | 1 | +0.00% | BELOW | NO_MOVE | 05:34:44 | 185 | 2 | 05:34:44 | 16.97 | Pre-Market |

_Widest absolute gap on any source: 5.71% against a 4.00% trigger - a 0.70x margin, so the flag decision is immune to whichever cached vintage a source returns._
_Tape lag (newest print behind the wall clock): median 25 min, max 185 min._
_Tape waves: wave 1 at 08:36:31 ET (12 names); wave 2 at 08:39:34 ET (8 names)_

_12 of 12 symbols priced._
