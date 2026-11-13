# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled until the cached vintage STOPS CHANGING (min 2, max 4) and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks. `tape_lag_min` is how many minutes the newest print is BEHIND the wall clock - the number that makes staleness visible._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Driver | Tape newest | Lag (min) | Pulls | Vintages | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AAON** | 78.8000 | +1.84% | 20 | 1,605 | 8,127 | +5.27% | BORDERLINE_TAPE_ONLY | IDIOSYNCRATIC | 08:23:34 | 16 | 2 | 08:23:34 | 82.00 | Pre-Market |
| **BW** | 4.8600 | +1.65% | 3,000 | 14,820 | 10,044 | +2.26% | BELOW | IDIOSYNCRATIC | 08:19:56 | 17 | 2 | 08:19:56 | 4.84 | Pre-Market |
| **CHTR** | 132.6600 | +1.76% | 70 | 9,449 | 1,298 | +0.00% | BELOW | NO_MOVE | 08:13:03 | 24 | 2 | 08:13:03 | 132.63 | Pre-Market |
| **GDYN** | 13.3800 | -0.22% | 70 | 934 | 618 | -0.82% | BORDERLINE_INTRADAY | IDIOSYNCRATIC | 08:21:45 | 15 | 4 | 08:15:38, 08:21:45 | 13.38 | Pre-Market |
| **HROW** | 28.3000 | +3.50% | 1 | 29 | 1,602 | +2.08% | BORDERLINE_INTRADAY | NO_MOVE | 08:23:58 | 15 | 3 | 08:20:05, 08:23:58 | 28.65 | Pre-Market |
| **LQDA** | 58.1200 | -0.03% | 35 | 2,034 | 7,115 | +0.00% | BELOW | NO_MOVE | 08:19:10 | 18 | 2 | 08:19:10 | 57.75 | Pre-Market |
| **LUMN** | 4.1700 | +0.65% | 100 | 420 | 15,077 | +0.88% | BORDERLINE_INTRADAY | NO_MOVE | 08:18:00 | 19 | 2 | 08:18:00 | 4.19 | Pre-Market |
| **MARA** | 7.2000 | -0.56% | 100 | 716 | 676,696 | +1.07% | BELOW | NO_MOVE | 08:21:07 | 16 | 4 | 08:19:00, 08:21:07 | 7.27 | Pre-Market |
| **PEPG** | 5.0400 | +0.51% | 14 | 71 | 17,597 | +0.41% | BELOW | NO_MOVE | 08:14:11 | 23 | 2 | 08:14:11 | 5.09 | Pre-Market |
| **QNT** | 37.4600 | -0.19% | 9 | 337 | 30,890 | +0.96% | BELOW | NO_MOVE | 08:20:52 | 16 | 2 | 08:20:52 | 37.78 | Pre-Market |
| **TNGX** | 24.8500 | +0.55% | 1 | 25 | 577 | +0.55% | BORDERLINE_INTRADAY | IDIOSYNCRATIC | 07:18:04 | 81 | 2 | 07:18:04 | 24.85 | Pre-Market |
| **ZETA** | 37.2700 | +0.47% | 20 | 749 | 19,428 | +1.05% | BELOW | IDIOSYNCRATIC | 08:18:59 | 18 | 2 | 08:18:59 | 37.48 | Pre-Market |

_Widest absolute gap on any source: 3.50% against a 4.00% trigger - a 1.14x margin, so the flag decision is immune to whichever cached vintage a source returns._
_Tape lag (newest print behind the wall clock): median 18 min, max 81 min._
_Tape waves: wave 1 at 08:37:05 ET (12 names); wave 2 at 08:39:07 ET (3 names)_

_12 of 12 symbols priced._
