# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled until the cached vintage STOPS CHANGING (min 2, max 4) and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks. `tape_lag_min` is how many minutes the newest print is BEHIND the wall clock - the number that makes staleness visible._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Driver | Tape newest | Lag (min) | Pulls | Vintages | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AMTM** | 24.8600 | +0.56% | 8 | 200 | 2,164 | +0.56% | BELOW | NO_MOVE | 08:06:32 | 31 | 2 | 08:06:32 | — | Pre-Market |
| **ANF** | 176.9600 | +0.24% | 100 | 17,739 | 11,356 | +0.02% | BELOW | NO_MOVE | 08:15:28 | 22 | 2 | 08:15:28 | — | Pre-Market |
| **CELC** | 71.7400 | +0.92% | 9 | 652 | 24 | +17.30% | BORDERLINE_TAPE_ONLY | NO_MOVE | 08:19:09 | 18 | 2 | 08:19:09 | — | Pre-Market |
| **COGT** | 36.0800 | +0.61% | 250 | 9,075 | 3,814 | +0.98% | BORDERLINE_INTRADAY | NO_MOVE | 08:22:23 | 15 | 4 | 08:11:45, 08:22:23 | — | Pre-Market |
| **DKS** | 158.5900 | +0.18% | 10 | 1,589 | 6,877 | +0.88% | BELOW | NO_MOVE | 08:17:06 | 20 | 2 | 08:17:06 | — | Pre-Market |
| **INSM** | 170.3100 | -0.02% | 13 | 2,214 | 31,211 | -0.01% | BELOW | NO_MOVE | 08:09:36 | 28 | 2 | 08:09:36 | — | Pre-Market |
| **IRON** | 89.3200 | +0.00% | 1 | 89 | 1 | +0.00% | BELOW | NO_MOVE | 04:01:58 | 280 | 2 | 04:01:58 | — | Pre-Market |
| **KSS** | 26.7000 | +1.01% | 10 | 270 | 4,988 | +0.92% | BELOW | MARKET_BETA | 08:18:21 | 19 | 2 | 08:18:21 | — | Pre-Market |
| **MMED** | 18.8400 | +3.29% | 30 | 584 | 95 | +3.29% | BELOW | IDIOSYNCRATIC | 07:23:29 | 78 | 2 | 07:23:29 | — | Pre-Market |
| **NAMS** | 24.1800 | +2.48% | 5 | 124 | 1,559 | +3.39% | BORDERLINE_INTRADAY | MARKET_BETA | 07:50:10 | 52 | 2 | 07:50:10 | — | Pre-Market |
| **NNNN** | 3.6500 | +0.00% | 20 | 73 | 35 | +0.00% | BELOW | NO_MOVE | 07:00:12 | 102 | 2 | 07:00:12 | — | Pre-Market |
| **STOK** | 35.4100 | +0.00% | 15 | 531 | 594 | +0.00% | BELOW | NO_MOVE | 07:28:24 | 73 | 2 | 07:28:24 | — | Pre-Market |

_Widest absolute gap on any source: 3.29% against a 4.00% trigger - a 1.22x margin, so the flag decision is immune to whichever cached vintage a source returns._
_Tape lag (newest print behind the wall clock): median 31 min, max 280 min._
_Tape waves: wave 1 at 08:37:39 ET (12 names); wave 2 at 08:41:50 ET (5 names)_

_12 of 12 symbols priced._
