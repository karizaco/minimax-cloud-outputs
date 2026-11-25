# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled until the cached vintage STOPS CHANGING (min 2, max 4) and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks. `tape_lag_min` is how many minutes the newest print is BEHIND the wall clock - the number that makes staleness visible._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Driver | Tape newest | Lag (min) | Pulls | Vintages | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ALAB** | 191.3000 | -5.37% | 50 | 9,052 | 123,008 | -6.17% | FLAGGED | SECTOR_BETA | 08:22:04 | 16 | 2 | 08:22:04 | — | Pre-Market |
| **APLD** | 12.2200 | -4.75% | 5 | 58 | 528,424 | -5.65% | BORDERLINE_THIN | IDIOSYNCRATIC | 08:22:05 | 16 | 2 | 08:22:05 | — | Pre-Market |
| **AXTI** | 31.5800 | -6.17% | 20 | 593 | 510,423 | -7.43% | BORDERLINE_THIN | IDIOSYNCRATIC | 08:22:02 | 16 | 2 | 08:22:02 | — | Pre-Market |
| **CRWV** | 42.6000 | -6.60% | 344 | 13,688 | 3,050,076 | -7.75% | FLAGGED | IDIOSYNCRATIC | 08:21:00 | 17 | 2 | 08:21:00 | — | Pre-Market |
| **DELL** | 295.2800 | -5.48% | 40 | 11,164 | 2,054,190 | -5.68% | FLAGGED | SECTOR_BETA | 08:21:11 | 17 | 2 | 08:21:02, 08:21:11 | — | Pre-Market |
| **KYMR** | 173.9200 | -1.68% | 1 | 171 | 2,037 | -2.25% | BELOW | NO_MOVE | 08:14:45 | 21 | 2 | 08:14:45 | — | Pre-Market |
| **LITE** | 487.1200 | -6.06% | 10 | 4,576 | 127,819 | -6.71% | BORDERLINE_THIN | IDIOSYNCRATIC | 08:22:07 | 16 | 2 | 08:22:07 | — | Pre-Market |
| **MXL** | 41.8900 | -6.90% | 10 | 390 | 51,826 | -7.78% | BORDERLINE_THIN | IDIOSYNCRATIC | 08:22:23 | 16 | 4 | 08:17:03, 08:22:23 | — | Pre-Market |
| **NBIS** | 87.3100 | -5.94% | 60 | 4,927 | 2,071,558 | -7.04% | FLAGGED | IDIOSYNCRATIC | 08:22:19 | 16 | 2 | 08:22:19 | — | Pre-Market |
| **NVDA** | 155.3800 | -5.27% | 5 | 736 | 13,140,160 | -5.92% | BORDERLINE_THIN | SECTOR_BETA | 08:21:47 | 16 | 4 | 08:20:46, 08:21:45, 08:21:47 | — | Pre-Market |
| **SITM** | 378.2900 | -5.91% | 5 | 1,780 | 6,910 | -6.95% | BORDERLINE_THIN | SECTOR_BETA | 08:21:13 | 17 | 2 | 08:21:13 | — | Pre-Market |
| **SMTC** | 86.4600 | -6.18% | 1 | 81 | 48,889 | -6.93% | BORDERLINE_THIN | IDIOSYNCRATIC | 08:21:20 | 17 | 2 | 08:21:20 | — | Pre-Market |

_Widest absolute gap on any source: 6.90% against a 4.00% trigger - a 0.58x margin, so the flag decision is immune to whichever cached vintage a source returns._
_Tape lag (newest print behind the wall clock): median 16 min, max 21 min._
_Tape waves: wave 1 at 08:36:00 ET (12 names); wave 2 at 08:38:12 ET (11 names)_

_12 of 12 symbols priced._
