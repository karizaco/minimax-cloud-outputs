# Breadth and regime snapshot

_Data date 2026-10-27 · cron date 2026-10-28 · computed from shibui's daily close series._

## Regime

| Flag | Value | Meaning |
|---|---|---|
| `size_cut_pct` | 0 | Percent to trim every Tier-A position. Zero means no size cut. |
| `uncertainty` | false | VIX above VIX3M signals front-end stress. |
| `late_cycle` | false | An index ETF more than 6% extended above its 50-day MA. |
| Large-cap breadth | 65.86% | Share of the 905 names above $10B trading above their 20-day MA. |
| Index breadth | 40% above 20-DMA | Share of SPY/RSP/QQQ/QQQE/IWM above their 20-day MA. |
| VIX / VIX3M | 16.91 / 19.22 (ratio 0.880) | Below 1.0 means no front-end stress premium. |

The index breadth reading and the large-cap breadth reading disagree: only 40% of the
five index ETFs are above their 20-day moving average, while 65.9% of the large-cap universe is. Because the
size-cut rule needs *both* an index below its 20-day average and breadth under 40%, the regime resolves to a
**zero size cut** — the index weakness is narrow rather than broad.

## Index ETF extension from the 50-day MA

| Ticker | Close | 20-DMA | 50-DMA | Extension | ATR(14) |
|---|---|---|---|---|---|
| IWM | $280.18 | 277.10 | 285.37 | -1.82% | 3.62 |
| QQQ | $721.25 | 733.18 | 725.26 | -0.55% | 11.43 |
| QQQE | $119.31 | 119.84 | 120.19 | -0.73% | 1.50 |
| RSP | $217.52 | 213.44 | 215.18 | +1.09% | 1.97 |
| SPY | $769.66 | 770.41 | 767.53 | +0.28% | 7.16 |

Extension is measured against the 50-day moving average. No index ETF is more than 6% extended, so `late_cycle`
stays false.

## Sector and industry-group relative strength

| ETF | 1M | 3M | 6M | Composite |
|---|---|---|---|---|
| IGV | 7.89% | 21.04% | 29.95% | 58.88 |
| IBB | 3.80% | 16.01% | 28.81% | 48.62 |
| XLE | 9.05% | 17.85% | 15.90% | 42.80 |
| XOP | 9.18% | 17.59% | 13.32% | 40.08 |
| XLV | 5.74% | 10.09% | 22.85% | 38.68 |
| ARKK | -4.14% | 20.68% | 13.54% | 30.07 |
| XBI | 1.84% | 6.43% | 20.59% | 28.85 |
| VGT | -1.55% | 10.94% | 18.72% | 28.11 |
| XLK | -2.17% | 10.53% | 19.08% | 27.44 |
| SMH | -6.22% | 7.14% | 12.59% | 13.51 |
| SOXX | -8.22% | 6.18% | 13.84% | 11.80 |
| XLP | 6.15% | 0.98% | 2.50% | 9.63 |
| XLF | 2.67% | -1.21% | 7.12% | 8.57 |
| OIH | 3.17% | 10.83% | -8.30% | 5.70 |
| XLY | 5.19% | 2.82% | -2.77% | 5.24 |
| XLB | 5.20% | -0.67% | 0.43% | 4.96 |
| KRE | 0.88% | -5.81% | 3.24% | -1.70 |
| PBJ | 4.56% | -3.04% | -5.96% | -4.44 |
| IYT | 2.23% | -5.85% | -0.90% | -4.52 |
| XLU | 7.61% | -5.99% | -9.29% | -7.66 |
| XLI | -0.51% | -5.83% | -3.85% | -10.19 |
| XLRE | 1.23% | -8.29% | -5.30% | -12.37 |
| VIS | -0.88% | -5.94% | -5.64% | -12.46 |
| PPA | 0.13% | -7.79% | -5.91% | -13.57 |
| JETS | -5.37% | -14.03% | 5.39% | -14.00 |
| XME | -4.40% | 1.69% | -13.94% | -16.65 |
| XLC | -8.54% | -3.13% | -11.72% | -23.39 |
| URA | -9.69% | -4.77% | -34.72% | -49.17 |
| TAN | -5.99% | -16.18% | -29.77% | -51.94 |

The top three themes by composite relative strength are IGV (software), IBB (biotechnology) and XLE (energy).
Those three GICS buckets are what the Hernandez theme-to-group screen pulled leaders from.
