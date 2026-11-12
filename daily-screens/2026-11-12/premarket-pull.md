# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled 4 times per symbol and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Price source | Tape newest | Tape vintages seen | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AAON** | 76.3300 | -2.54% | 5 | 372 | 2,022 | -3.05% | BELOW | /info primaryData (LIVE) | 08:19:19 | 08:19:19 | 75.45 | Pre-Market |
| **BW** | 4.8400 | -0.60% | 30 | 144 | 85,270 | -1.86% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:17:09 | 08:17:09 | 4.90 | Pre-Market |
| **CHTR** | 136.3100 | +1.24% | 10 | 1,380 | 4,145 | +0.76% | BELOW | /info primaryData (LIVE) | 08:20:15 | 08:20:15 | 136.06 | Pre-Market |
| **GDYN** | 13.8300 | -0.58% | 15 | 206 | 2,408 | +8.46% | BORDERLINE_TAPE_ONLY | /info primaryData (LIVE) | 08:11:42 | 08:11:42 | 13.80 | Pre-Market |
| **HROW** | 29.3700 | -1.26% | 20 | 580 | 12,432 | +0.61% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:11:07 | 08:11:07 | 29.40 | Pre-Market |
| **LQDA** | 55.2100 | -0.13% | 22 | 1,213 | 2,056 | -0.51% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:20:25 | 08:20:25 | 54.90 | Pre-Market |
| **LUMN** | 4.4500 | -2.02% | 100 | 436 | 53,773 | -2.02% | BELOW | /info primaryData (LIVE) | 08:15:14 | 08:15:14 | 4.42 | Pre-Market |
| **MARA** | 7.6600 | -5.74% | 85 | 614 | 732,319 | -5.41% | FLAGGED | /info primaryData (LIVE) | 08:21:02 | 08:21:02 | 7.56 | Pre-Market |
| **PEPG** | 5.2600 | +2.28% | 200 | 1,076 | 1,260,122 | +0.76% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:21:03 | 08:19:13, 08:21:03 | 5.35 | Pre-Market |
| **QNT** | 40.5700 | -3.53% | 100 | 3,914 | 37,770 | -2.52% | BELOW | /info primaryData (LIVE) | 08:21:19 | 08:21:19 | 39.35 | Pre-Market |
| **TNGX** | 25.7300 | -0.15% | 50 | 1,284 | 2,592 | -0.12% | BELOW | /info primaryData (LIVE) | 07:09:31 | 07:09:31 | 25.73 | Pre-Market |
| **ZETA** | 37.7400 | -3.92% | 200 | 7,252 | 73,230 | -3.15% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:21:35 | 08:21:35 | 37.25 | Pre-Market |


_Widest absolute gap on any source: 5.74% against a 4.00% trigger — a 0.70x margin, so the flag decision is immune to whichever cached vintage a source returns._

_12 of 12 symbols priced.
