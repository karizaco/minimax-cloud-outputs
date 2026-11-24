# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled until the cached vintage STOPS CHANGING (min 2, max 4) and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks. `tape_lag_min` is how many minutes the newest print is BEHIND the wall clock - the number that makes staleness visible._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Driver | Tape newest | Lag (min) | Pulls | Vintages | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ANT** | 87.6400 | -5.44% | 11 | 912 | 10,355,993 | -5.43% | BORDERLINE_THIN | IDIOSYNCRATIC | 08:22:14 | 16 | 4 | 08:20:00, 08:22:14, 08:22:39 | — | Pre-Market |
| **CBLL** | 29.2900 | +1.16% | 4 | 119 | 350 | -0.03% | BELOW | SECTOR_BETA | 07:52:33 | 43 | 2 | 07:52:33 | — | Pre-Market |
| **GPN** | 91.4700 | -0.91% | 1 | 91 | 2,119 | +1.89% | BELOW | NO_MOVE | 08:19:25 | 16 | 4 | 08:18:29, 08:19:25 | — | Pre-Market |
| **HTFL** | 48.3100 | +0.35% | 1 | 48 | 3,524 | -0.79% | BORDERLINE_INTRADAY | NO_MOVE | 08:17:01 | 19 | 2 | 08:17:01 | — | Pre-Market |
| **INTC** | 59.6600 | -6.15% | 100 | 5,599 | 3,810,286 | -6.10% | FLAGGED | SECTOR_BETA | 08:22:06 | 16 | 4 | 08:20:01, 08:21:04, 08:22:06 | — | Pre-Market |
| **IREN** | 14.6400 | -4.99% | 110 | 1,530 | 3,106,301 | -4.99% | FLAGGED | CRYPTO_BETA | 08:22:01 | 16 | 4 | 08:20:01, 08:21:00, 08:22:01 | — | Pre-Market |
| **KVYO** | 23.3000 | -0.86% | 1 | 23 | 98,635 | -2.69% | BORDERLINE_INTRADAY | MARKET_BETA | 08:19:06 | 16 | 2 | 08:19:06 | — | Pre-Market |
| **NOK** | 7.5500 | -2.91% | 5 | 37 | 1,808,116 | -2.91% | BELOW | IDIOSYNCRATIC | 08:22:02 | 16 | 3 | 08:20:01, 08:22:02 | — | Pre-Market |
| **NTLA** | 10.1500 | -1.48% | 18 | 180 | 5,972 | -1.48% | BELOW | MARKET_BETA | 08:20:08 | 16 | 2 | 08:20:08 | — | Pre-Market |
| **NVDA** | 165.0500 | -5.35% | 2 | 312 | 21,596,737 | -5.27% | BORDERLINE_THIN | SECTOR_BETA | 08:22:42 | 15 | 4 | 08:21:31, 08:22:37, 08:22:42 | — | Pre-Market |
| **PLMR** | 164.4400 | -0.57% | 1 | 164 | 410 | +0.00% | BELOW | NO_MOVE | 07:37:04 | 61 | 2 | 07:37:04 | — | Pre-Market |
| **SNDK** | 87.7100 | -6.20% | 44 | 3,620 | 5,577,574 | -5.97% | FLAGGED | SECTOR_BETA | 08:21:31 | 16 | 2 | 08:21:31, 08:21:33 | — | Pre-Market |

_Widest absolute gap on any source: 6.20% against a 4.00% trigger - a 0.64x margin, so the flag decision is immune to whichever cached vintage a source returns._
_Tape lag (newest print behind the wall clock): median 16 min, max 61 min._
_Tape waves: wave 1 at 08:35:52 ET (12 names); wave 2 at 08:38:03 ET (7 names)_

_12 of 12 symbols priced._
