# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled 4 times per symbol and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Price source | Tape newest | Tape vintages seen | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CYRX** | 20.4700 | +0.35% | 4 | 82 | 1,195 | -0.73% | BELOW | /info primaryData (LIVE) | 07:26:31 | 07:26:31 | 20.32 | Pre-Market |
| **ETON** | 64.3500 | +0.61% | 77 | 4,985 | 2,087 | +0.68% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:20:46 | 08:20:46 | 64.79 | Pre-Market |
| **FLY** | 24.3100 | -3.54% | 100 | 2,345 | 134,697 | -4.73% | BORDERLINE_TAPE_ONLY | /info primaryData (LIVE) | 08:24:37 | 08:24:37 | 23.85 | Pre-Market |
| **FROG** | 108.1800 | +0.62% | 50 | 5,442 | 6,936 | -1.78% | BELOW | /info primaryData (LIVE) | 08:24:03 | 08:23:04, 08:24:03 | 108.75 | Pre-Market |
| **IONQ** | 35.3400 | -3.31% | 8 | 273 | 1,085,423 | -5.50% | BORDERLINE_TAPE_ONLY | /info primaryData (LIVE) | 08:24:01 | 08:23:00, 08:24:01 | 34.70 | Pre-Market |
| **KRMN** | 45.9000 | -1.96% | 99 | 4,455 | 3,086 | -2.00% | BELOW | /info primaryData (LIVE) | 08:24:12 | 08:19:48, 08:24:12 | 45.01 | Pre-Market |
| **LASR** | 43.2100 | -1.64% | 1 | 42 | 6,710 | -3.84% | BELOW | /info primaryData (LIVE) | 08:21:46 | 08:21:46 | 43.46 | Pre-Market |
| **OKLO** | 26.8400 | -2.39% | 1 | 26 | 269,452 | -4.47% | BORDERLINE_TAPE_ONLY | /info primaryData (LIVE) | 08:24:01 | 08:24:01 | 26.80 | Pre-Market |
| **QNT** | 40.0400 | -1.65% | 2 | 79 | 43,467 | -2.83% | BELOW | /info primaryData (LIVE) | 08:22:16 | 08:22:16 | 39.80 | Pre-Market |
| **RGTI** | 12.9800 | -3.16% | 15 | 189 | 474,890 | -5.39% | BORDERLINE_TAPE_ONLY | /info primaryData (LIVE) | 08:24:00 | 08:23:01, 08:24:00 | 12.81 | Pre-Market |
| **RHLD** | 163.8500 | -4.42% | 1 | 157 | 1,986 | -1.68% | BORDERLINE_THIN | /info primaryData (LIVE) | 07:47:00 | 07:47:00 | 159.54 | Pre-Market |
| **TMDX** | 93.7900 | -0.31% | 100 | 9,350 | 755 | -1.26% | BELOW | /info primaryData (LIVE) | 08:20:46 | 08:20:46 | 93.03 | Pre-Market |


_Widest absolute gap on any source: 4.42% against a 4.00% trigger — a 0.91x margin, so the flag decision is immune to whichever cached vintage a source returns._

_12 of 12 symbols priced.
