# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled until the cached vintage STOPS CHANGING (min 2, max 4) and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks. `tape_lag_min` is how many minutes the newest print is BEHIND the wall clock - the number that makes staleness visible._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Driver | Tape newest | Lag (min) | Pulls | Vintages | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ALAB** | 216.7500 | +4.83% | 5 | 1,136 | 107,195 | +4.66% | BORDERLINE_THIN | IDIOSYNCRATIC | 08:23:10 | 15 | 4 | 08:21:00, 08:22:04, 08:23:10 | 223.50 | Pre-Market |
| **ARM** | 182.7600 | +4.24% | 1 | 190 | 76,393 | +3.63% | BORDERLINE_THIN | SECTOR_BETA | 08:23:09 | 15 | 4 | 08:19:03, 08:23:09 | 187.40 | Pre-Market |
| **BRBR** | 13.6600 | -1.40% | 12 | 162 | 1,975 | -0.18% | BELOW | NO_MOVE | 08:15:51 | 20 | 2 | 08:15:51 | 13.66 | Pre-Market |
| **ENR** | 28.2900 | +0.39% | 200 | 5,680 | 670 | +0.39% | BELOW | NO_MOVE | 08:07:29 | 29 | 2 | 08:07:29 | 28.29 | Pre-Market |
| **LUMN** | 4.3000 | +1.16% | 3 | 13 | 5,930 | +0.47% | BELOW | SECTOR_BETA | 08:22:28 | 16 | 2 | 08:22:28 | 4.30 | Pre-Market |
| **RARE** | 17.7300 | -0.90% | 1 | 18 | 3,215 | -0.96% | BELOW | NO_MOVE | 08:21:20 | 15 | 3 | 08:20:00, 08:21:20 | 17.74 | Pre-Market |
| **RYTM** | 119.0400 | +0.91% | 1 | 120 | 2,375 | +0.80% | BORDERLINE_INTRADAY | NO_MOVE | 08:15:45 | 21 | 2 | 08:15:45 | 119.00 | Pre-Market |
| **SHAZ** | 21.9900 | +9.60% | 8 | 193 | 36,564 | +8.23% | BORDERLINE_THIN | IDIOSYNCRATIC | 08:19:14 | 19 | 2 | 08:19:14 | 23.39 | Pre-Market |
| **SLS** | 17.9500 | -21.45% | 40 | 564 | 6,113,630 | -19.50% | FLAGGED | IDIOSYNCRATIC | 08:22:00 | 16 | 2 | 08:22:00, 08:22:46 | 17.98 | Pre-Market |
| **SNAP** | 5.4400 | +1.47% | 200 | 1,104 | 155,319 | +1.29% | BELOW | MARKET_BETA | 08:20:01 | 16 | 2 | 08:20:01 | 5.45 | Pre-Market |
| **VIK** | 100.3700 | -0.44% | 25 | 2,498 | 301 | -0.41% | BELOW | NO_MOVE | 08:21:19 | 15 | 2 | 08:21:19 | 100.37 | Pre-Market |
| **YALA** | 5.9400 | +0.34% | 1 | 6 | 199 | +0.00% | BELOW | NO_MOVE | 04:03:34 | 275 | 2 | 04:03:34 | 5.94 | Pre-Market |

_Widest absolute gap on any source: 21.45% against a 4.00% trigger - a 0.19x margin, so the flag decision is immune to whichever cached vintage a source returns._
_Tape lag (newest print behind the wall clock): median 16 min, max 275 min._
_Tape waves: wave 1 at 08:36:36 ET (12 names); wave 2 at 08:38:28 ET (6 names)_

_12 of 12 symbols priced._
