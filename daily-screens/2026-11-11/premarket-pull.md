# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled 4 times per symbol and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Price source | Tape newest | Tape vintages seen | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **BW** | 4.4800 | +4.49% | 45 | 211 | 157,925 | +4.46% | FLAGGED | /info primaryData (LIVE) | 08:20:04 | 08:18:15, 08:20:04 | 4.48 | Pre-Market |
| **FRVO** | 11.3800 | +4.57% | 2 | 24 | 80,080 | +4.22% | BORDERLINE_THIN | /info primaryData (LIVE) | 08:19:22 | 08:19:22 | 11.30 | Pre-Market |
| **IAM** | 14.7800 | -1.49% | 4 | 58 | 7,382 | -1.89% | BELOW | /info primaryData (LIVE) | 08:19:46 | 08:19:46 | 15.30 | Pre-Market |
| **IMVT** | 35.7100 | +0.87% | 35 | 1,261 | 1,410 | -1.29% | BELOW | /info primaryData (LIVE) | 07:50:23 | 07:50:23 | 35.72 | Pre-Market |
| **LUNR** | 11.8100 | +5.00% | 25 | 310 | 221,926 | +4.65% | FLAGGED | /info primaryData (LIVE) | 08:20:08 | 08:19:07, 08:20:08 | 11.84 | Pre-Market |
| **MPWR** | 1357.6000 | +5.78% | 5 | 7,180 | 4,531 | +5.43% | BORDERLINE_THIN | /info primaryData (LIVE) | 08:20:17 | 08:20:17 | 1378.33 | Pre-Market |
| **PL** | 14.2700 | +3.75% | 10 | 148 | 173,491 | +3.15% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:19:06 | 08:19:06 | 14.68 | Pre-Market |
| **PRAX** | 337.5900 | +0.61% | 2 | 679 | 625 | +0.61% | BELOW | /info primaryData (LIVE) | 07:44:41 | 07:44:41 | 337.59 | Pre-Market |
| **QXO** | 13.7300 | +1.09% | 100 | 1,388 | 28,529 | +0.95% | BELOW | /info primaryData (LIVE) | 08:19:51 | 08:19:51 | 13.71 | Pre-Market |
| **TLS** | 7.6700 | +0.78% | 600 | 4,638 | 4,900 | +0.80% | BELOW | /info primaryData (LIVE) | 08:19:14 | 08:19:14 | 7.54 | Pre-Market |
| **TTD** | 15.4200 | -0.56% | 300 | 4,600 | 153,000 | -0.13% | BELOW | /info primaryData (LIVE) - equals the ASK, so it is a quote not a print | 08:21:06 | 08:21:06 | 15.40 | Pre-Market |
| **WRBY** | 29.9000 | +2.48% | 2 | 61 | 9,426 | +2.95% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:17:23 | 08:17:23 | 29.90 | Pre-Market |


_Widest absolute gap on any source: 5.78% against a 4.00% trigger — a 0.69x margin, so the flag decision is immune to whichever cached vintage a source returns._

_12 of 12 symbols priced.
