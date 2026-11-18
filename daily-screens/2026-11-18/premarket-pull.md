# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled until the cached vintage STOPS CHANGING (min 2, max 4) and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks. `tape_lag_min` is how many minutes the newest print is BEHIND the wall clock - the number that makes staleness visible._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Driver | Tape newest | Lag (min) | Pulls | Vintages | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **BILL** | 64.8800 | +0.34% | 3 | 195 | 13,477 | +0.18% | BELOW | NO_MOVE | 08:20:33 | 16 | 2 | 08:20:33 | 65.18 | Pre-Market |
| **CGON** | 78.9400 | -0.87% | 1 | 78 | 263 | -0.53% | BELOW | NO_MOVE | 07:56:41 | 40 | 2 | 07:56:41 | 79.00 | Pre-Market |
| **FENC** | 13.5800 | +0.52% | 100 | 1,365 | 100 | +0.52% | BORDERLINE_INTRADAY | NO_MOVE | 07:56:16 | 40 | 2 | 07:56:16 | 13.57 | Pre-Market |
| **HUBS** | 216.3000 | -0.42% | 3 | 646 | 1,165 | -0.42% | BELOW | NO_MOVE | 08:18:46 | 17 | 2 | 08:18:46 | 216.30 | Pre-Market |
| **MOH** | 221.2100 | -0.10% | 1 | 221 | 144 | -1.06% | BORDERLINE_INTRADAY | NO_MOVE | 08:10:07 | 26 | 2 | 08:10:07 | 221.21 | Pre-Market |
| **POWL** | 150.8600 | +0.50% | 3 | 455 | 39,835 | +0.92% | BELOW | NO_MOVE | 08:07:24 | 29 | 2 | 08:07:24 | 154.00 | Pre-Market |
| **QLYS** | 174.6700 | -0.33% | 1 | 174 | 1,311 | -0.27% | BELOW | MARKET_BETA | 08:21:00 | 15 | 2 | 08:21:00 | 174.67 | Pre-Market |
| **SEZL** | 154.2500 | +0.28% | 2 | 309 | 1,340 | +0.49% | BELOW | NO_MOVE | 08:17:19 | 19 | 2 | 08:17:19 | 156.61 | Pre-Market |
| **TSN** | 63.6500 | -0.82% | 30 | 1,894 | 1,965 | -0.53% | BELOW | NO_MOVE | 08:15:01 | 21 | 2 | 08:15:01 | 64.78 | Pre-Market |
| **TU** | 9.2600 | +0.00% | 1 | 9 | 4,612 | -1.48% | BELOW | NO_MOVE | 08:05:21 | 31 | 2 | 08:05:21 | 9.27 | Pre-Market |
| **ULCC** | 7.7300 | +0.52% | 1 | 8 | 1,100 | +0.26% | BORDERLINE_INTRADAY | NO_MOVE | 08:07:18 | 29 | 2 | 08:07:18 | 7.85 | Pre-Market |
| **URGN** | 29.8700 | -0.40% | 1 | 30 | 499 | +0.17% | BORDERLINE_INTRADAY | NO_MOVE | 08:16:36 | 20 | 2 | 08:16:36 | 31.05 | Pre-Market |

_Widest absolute gap on any source: 0.87% against a 4.00% trigger - a 4.58x margin, so the flag decision is immune to whichever cached vintage a source returns._
_Tape lag (newest print behind the wall clock): median 26 min, max 40 min._
_Tape waves: wave 1 at 08:36:21 ET (12 names); wave 2 at 08:37:20 ET (0 names)_

_12 of 12 symbols priced._
