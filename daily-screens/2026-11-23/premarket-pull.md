# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled until the cached vintage STOPS CHANGING (min 2, max 4) and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks. `tape_lag_min` is how many minutes the newest print is BEHIND the wall clock - the number that makes staleness visible._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Driver | Tape newest | Lag (min) | Pulls | Vintages | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AMBA** | 53.0700 | +4.86% | 2 | 111 | 26,179 | +4.82% | BORDERLINE_THIN | SECTOR_BETA | 08:26:22 | 16 | 2 | 08:26:22 | — | Pre-Market |
| **DPC** | 30.7400 | +4.20% | 7 | 224 | 7 | +0.00% | BORDERLINE_THIN | IDIOSYNCRATIC | 07:46:19 | 56 | 2 | 07:46:19 | — | Pre-Market |
| **INSM** | 141.3300 | +1.46% | 1 | 143 | 7,822 | +1.32% | BELOW | SECTOR_BETA | 08:15:44 | 21 | 2 | 08:15:44 | — | Pre-Market |
| **IVR** | 5.3800 | +1.63% | 15 | 82 | 10,035 | +1.67% | BELOW | NO_MOVE | 08:11:27 | 25 | 2 | 08:11:27 | — | Pre-Market |
| **NTSK** | 23.9300 | +4.47% | 50 | 1,250 | 60,496 | +4.47% | FLAGGED | SECTOR_BETA | 08:25:56 | 16 | 2 | 08:25:56 | — | Pre-Market |
| **NUAI** | 3.7800 | +7.94% | 100 | 408 | 545,447 | +7.94% | FLAGGED | IDIOSYNCRATIC | 08:25:00 | 17 | 2 | 08:25:00 | — | Pre-Market |
| **OKTA** | 191.4600 | +5.30% | 1 | 202 | 24,513 | +5.39% | BORDERLINE_THIN | SECTOR_BETA | 08:26:13 | 16 | 2 | 08:26:13 | — | Pre-Market |
| **P** | 92.0500 | +7.29% | 18 | 1,778 | 21,532 | +6.51% | BORDERLINE_THIN | SECTOR_BETA | 08:25:09 | 17 | 2 | 08:25:09 | — | Pre-Market |
| **PANW** | 343.3200 | +1.71% | 4 | 1,397 | 203,583 | +1.29% | BORDERLINE_INTRADAY | MARKET_BETA | 08:21:17 | 15 | 4 | 08:20:01, 08:21:17 | — | Pre-Market |
| **PURR** | 7.4800 | +8.02% | 53 | 428 | 549,259 | +8.02% | FLAGGED | IDIOSYNCRATIC | 08:26:00 | 16 | 2 | 08:26:00 | — | Pre-Market |
| **TU** | 11.0700 | -0.27% | 10 | 110 | 9,334 | -0.45% | BELOW | NO_MOVE | 08:19:43 | 17 | 2 | 08:19:43 | — | Pre-Market |
| **VRDN** | 29.9600 | -1.50% | 1 | 30 | 1,347 | -1.50% | BORDERLINE_INTRADAY | NO_MOVE | 08:03:13 | 33 | 2 | 08:03:13 | — | Pre-Market |

_Widest absolute gap on any source: 8.02% against a 4.00% trigger - a 0.50x margin, so the flag decision is immune to whichever cached vintage a source returns._
_Tape lag (newest print behind the wall clock): median 17 min, max 56 min._
_Tape waves: wave 1 at 08:36:33 ET (12 names); wave 2 at 08:40:11 ET (7 names); wave 2 at 08:42:17 ET (7 names)_

_12 of 12 symbols priced._
