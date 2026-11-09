# Pre-market pull

_Cache-safe pre-market prices. The tape is pulled 4 times per symbol and the payload with the newest internal timestamp wins, because Nasdaq's extended-trading endpoint is served from a shared HTTP cache that can return hours-old snapshots for the same URL. The published gap comes from the tape's last EXECUTED print; the live quote is published separately; Cboe and TradingView supply independent, explicitly-timestamped cross-checks._

| Ticker | Close | Gap % (tape) | Exec shares | Exec notional | PM volume | Quote % | Verdict | Price source | Tape newest | Tape vintages seen | Cboe | Mkt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **RUN** | 9.9800 | -0.78% | 7 | 69 | 142,438 | +0.00% | BELOW | /info primaryData (LIVE) | 08:21:30 | 08:21:30 | 9.98 | Pre-Market |
| **SEZL** | 149.4300 | +2.37% | 2 | 306 | 741 | +2.53% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:20:33 | 08:20:33 | 150.00 | Pre-Market |
| **XERS** | 15.2000 | +0.53% | 1 | 15 | 61,130 | +0.46% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:21:52 | 08:19:34, 08:21:52 | 15.08 | Pre-Market |
| **ACHC** | 37.0000 | +0.68% | 15 | 559 | 1,888 | +0.68% | BELOW | /info primaryData (LIVE) | 08:20:47 | 08:20:47 | 37.41 | Pre-Market |
| **MRNA** | 254.1900 | +1.32% | 15 | 3,863 | 220,156 | +1.36% | BELOW | /info primaryData (LIVE) | 08:20:00 | 08:20:00 | 256.80 | Pre-Market |
| **APP** | 391.2200 | -1.31% | 4 | 1,544 | 84,176 | -1.17% | BELOW | /info primaryData (LIVE) | 08:22:04 | 08:20:01, 08:21:02, 08:22:04 | 391.22 | Pre-Market |
| **U** | 51.4900 | +0.44% | 50 | 2,586 | 159,091 | +0.60% | BELOW | /info primaryData (LIVE) | 08:22:00 | 08:19:01, 08:22:00 | 52.16 | Pre-Market |
| **FUN** | 10.0000 | +2.50% | 95 | 974 | 27,778 | +2.50% | BELOW | /info primaryData (LIVE) | 08:10:57 | 08:10:57 | 10.14 | Pre-Market |
| **JOBY** | 5.9300 | -1.01% | 1 | 6 | 434,125 | -0.68% | BELOW | /info primaryData (LIVE) | 08:22:03 | 08:22:03 | 5.92 | Pre-Market |
| **WRBY** | 25.4800 | +1.26% | 1 | 26 | 8,373 | +0.23% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:21:08 | 08:21:08 | 25.48 | Pre-Market |
| **VRDN** | 28.4900 | -1.54% | 86 | 2,412 | 13,614 | +3.78% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 07:43:02 | 07:43:02 | 28.60 | Pre-Market |
| **XNCR** | 35.7500 | +2.57% | 1 | 37 | 3,648 | +2.91% | BORDERLINE_INTRADAY | /info primaryData (LIVE) | 08:19:56 | 08:19:56 | 35.82 | Pre-Market |


_Widest absolute gap on any source: 2.57% against a 4.00% trigger — a 1.55x margin, so the flag decision is immune to whichever cached vintage a source returns._

_12 of 12 symbols priced.
