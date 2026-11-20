# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled until the cached vintage STOPS CHANGING (min 2, max 4) and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks. `tape_lag_min` is how many minutes the newest print is BEHIND the wall clock - the number that makes staleness visible._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Driver | Tape newest | Lag (min) | Pulls | Vintages | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ATEN** | 32.5400 | -2.77% | 200 | 6,328 | 3,891 | -2.89% | BORDERLINE_INTRADAY | SECTOR_BETA | 08:21:22 | 18 | 2 | 08:21:22 | — | Pre-Market |
| **BRBR** | 15.1100 | +0.79% | 3 | 46 | 6,541 | +0.46% | BELOW | NO_MOVE | 08:20:01 | 16 | 3 | 08:14:00, 08:20:01 | — | Pre-Market |
| **FSLY** | 16.8600 | -3.02% | 300 | 4,905 | 16,073 | -3.02% | BELOW | SECTOR_BETA | 08:23:01 | 16 | 2 | 08:23:01 | — | Pre-Market |
| **GNRC** | 205.0900 | -2.97% | 68 | 13,532 | 7,367 | -3.84% | BORDERLINE_INTRADAY | IDIOSYNCRATIC | 08:22:03 | 18 | 2 | 08:22:03 | — | Pre-Market |
| **NTSK** | 24.8000 | -2.49% | 50 | 1,209 | 16,766 | -3.23% | BELOW | SECTOR_BETA | 08:24:02 | 16 | 2 | 08:24:02 | — | Pre-Market |
| **NUAI** | 4.2800 | -8.88% | 1 | 4 | 453,793 | -12.38% | BORDERLINE_THIN | IDIOSYNCRATIC | 08:23:34 | 16 | 2 | 08:23:34 | — | Pre-Market |
| **OKTA** | 206.8500 | -3.96% | 3 | 596 | 25,392 | -4.22% | BORDERLINE_TAPE_ONLY | SECTOR_BETA | 08:24:05 | 16 | 2 | 08:24:05 | — | Pre-Market |
| **PANW** | 361.7300 | -2.41% | 15 | 5,295 | 101,268 | -2.33% | BELOW | MARKET_BETA | 08:24:02 | 16 | 2 | 08:24:02 | — | Pre-Market |
| **QLYS** | 192.4300 | -2.32% | 1 | 188 | 338 | -2.82% | BELOW | SECTOR_BETA | 07:59:06 | 41 | 2 | 07:59:06 | — | Pre-Market |
| **S** | 24.0100 | -2.22% | 2 | 47 | 36,456 | -2.87% | BORDERLINE_INTRADAY | SECTOR_BETA | 08:21:10 | 19 | 2 | 08:21:10 | — | Pre-Market |
| **SAIL** | 22.0400 | +0.00% | 92,207 | 2,032,242 | 107,005 | -2.22% | BORDERLINE_INTRADAY | SECTOR_BETA | 08:22:26 | 16 | 2 | 08:22:26 | — | Pre-Market |
| **TENB** | 44.0900 | -2.15% | 40 | 1,726 | 10,854 | -2.31% | BORDERLINE_INTRADAY | SECTOR_BETA | 08:22:28 | 17 | 2 | 08:22:28 | — | Pre-Market |

_Widest absolute gap on any source: 8.88% against a 4.00% trigger - a 0.45x margin, so the flag decision is immune to whichever cached vintage a source returns._
_Tape lag (newest print behind the wall clock): median 16 min, max 41 min._
_Tape waves: wave 1 at 08:35:55 ET (12 names); wave 2 at 08:38:43 ET (11 names); wave 2 at 08:39:44 ET (10 names)_

_12 of 12 symbols priced._
