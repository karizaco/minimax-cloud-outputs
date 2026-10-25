<!-- cron #9 stock-screener-daily-sweep-18:30 | cron_date=2026-10-23 | data_date=2026-10-22 | _source=tv_fallback+yahoo_verify | generated=2026-10-23T11:39Z -->
## Real Simple Ariel — theme → group funnel
**I. Top-down sector/industry RS** — equal-weight *median* constituent 1M/3M/6M return per group, composite = unweighted sum. This replaces the spec's `screen_etf` call, which is unavailable.

| Kind | Group | N | Perf1M | Perf3M | Perf6M | Composite | MedDay% |
| --- | --- | --- | --- | --- | --- | --- | --- |
| industry | Packaged Software | 186 | 6.1 | 23.6 | 35.6 | 65.2 | 0.82 |
| industry | Information Technology Services | 51 | 7.3 | 23.7 | 20.7 | 51.6 | 1.80 |
| sector | Technology Services | 311 | 3.9 | 17.8 | 23.8 | 45.5 | 0.84 |
| sector | Health Services | 56 | 5.6 | 7.6 | 24.4 | 37.6 | 1.51 |
| industry | Medical/Nursing Services | 35 | 1.5 | 8.5 | 24.8 | 34.8 | 1.17 |
| industry | Medical Specialties | 105 | 4.4 | 8.6 | 20.0 | 33.0 | 1.91 |
| industry | Property/Casualty Insurance | 34 | 8.0 | 8.3 | 16.5 | 32.8 | 1.75 |
| industry | Marine Shipping | 33 | -3.2 | 12.3 | 21.3 | 30.3 | -1.39 |
| industry | Miscellaneous Commercial Services | 74 | 6.0 | 7.0 | 12.7 | 25.7 | 1.97 |
| industry | Integrated Oil | 31 | 6.8 | 8.8 | 8.5 | 24.1 | -0.59 |
| sector | Commercial Services | 102 | 4.8 | 6.7 | 11.2 | 22.7 | 2.27 |
| sector | Energy Minerals | 74 | 6.4 | 9.0 | 3.3 | 18.7 | -0.77 |
| industry | Multi-Line Insurance | 30 | 4.8 | 2.1 | 10.3 | 17.2 | 2.00 |
| industry | Oil & Gas Production | 27 | 6.8 | 8.8 | 0.9 | 16.5 | -0.66 |

**Sector rotation on the session (median constituent day change):**

| Sector | Median day % | 1M | 3M |
| --- | --- | --- | --- |
| Consumer Durables | 3.73 | -1.5 | -5.9 |
| Consumer Non-Durables | 3.54 | 6.8 | 3.1 |
| Retail Trade | 3.16 | 7.0 | 6.6 |
| Commercial Services | 2.27 | 4.8 | 6.7 |
| Utilities | 2.22 | 3.2 | -7.0 |
| Finance | 1.81 | -1.0 | -3.9 |
| Health Services | 1.51 | 5.6 | 7.6 |
| Miscellaneous | 1.43 | -6.3 | -1.4 |
| Consumer Services | 1.30 | 3.0 | -2.9 |
| Process Industries | 1.23 | -1.8 | -6.3 |
| Technology Services | 0.84 | 3.9 | 17.8 |
| Communications | 0.45 | -8.9 | -6.4 |

**Skip-rule flags applied to every candidate** — `atr_shrink` (ATR% < 0.6× universe median 3.366%), `wicky_breakout` (breakout day on RVOL<1.2). `day2_no_follow` and `ma_shrink_5d` are **not computable** here (need multi-day range history) and are omitted.
