<!-- cron #9 stock-screener-daily-sweep-18:30 | cron_date=2026-10-23 | data_date=2026-10-22 | _source=tv_fallback+yahoo_verify | generated=2026-10-23T11:39Z -->
# Breadth & regime — 2026-10-22

**% above 20-DMA: 65.3%** (mcap > $10B proxy (858 names); no SPX constituents table on this source). Full pre-filtered universe: 58.7%.

| Index | Close | 20-DMA | 50-DMA | Ext from 50 | ATR% | ATR× median |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 763.96 | 770.72 | 768.17 | -0.55 | 0.96 | 0.93 |
| RSP | 218.22 | 212.39 | 215.48 | 1.27 | 0.95 | 0.95 |
| QQQ | 704.47 | 737.24 | 726.37 | -3.01 | 1.71 | 1.04 |
| QQQE | 117.63 | 120.17 | 120.56 | -2.43 | 1.40 | 1.08 |
| IWM | 276.67 | 277.50 | 286.97 | -3.59 | 1.36 | 0.86 |

**Indices below their 20-DMA:** SPY, QQQ, QQQE, IWM

**VIX: 19.03** — `uncertainty` flag is **not computed**: both `^VXV` and `^VXVCLS` return zero bars from Yahoo, and a VIX/VXV ratio cannot be built from one leg. Left null rather than assumed.

| Regime flag | Value | Rule |
| --- | --- | --- |
| `size_cut_pct` | `None` | 50 when an index is < 20-DMA **and** breadth < 40%. Breadth is 65.3%, so breadth fails the second condition despite 4 of 5 indices being below the 20-DMA. |
| `uncertainty` | `None` | VIX/VXV > 1. Not computable (see above). |
| `late_cycle` | `False` | any index > 6× median ATR%. Max observed is 1.08. |
