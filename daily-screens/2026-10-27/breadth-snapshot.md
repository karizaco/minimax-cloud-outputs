<!-- cron #10 stock-screener-breadth-snapshot | cron_date=2026-10-27 | data_date=2026-10-26 | _source=nasdaq_public_chart_api | generated=2026-10-27T18:35Z -->
# Breadth & regime — 2026-10-26 close (cron date 2026-10-27)

**71.5% of the S&P 500 closed above its 20-DMA** on the 2026-10-26 settle, and 72.7% are above it on the in-progress 2026-10-27 session. No regime flag fires: `size_cut_pct` = 0, `uncertainty` = false, `late_cycle` = false. The story is not a level but a split: the equal-weight index is flat while the cap-weighted index is being pulled up by a chip complex, and the 4-of-5 index ETFs still below their 20-DMA is the same divergence the prior run printed.

**Degraded path — read this before trusting the numbers.** Every Tier-1 MCP for this skill (`shibui-finance`, `tradingview-advanced`, `financekit`) is **not registered in this cloud sandbox**, and the Yahoo chart API that the prior run used is now **HTTP-429 throttling this egress** (521/521 requests rejected on a burst; even single spaced requests are intermittently rejected). The breadth snapshot was therefore rebuilt on the **Nasdaq public chart API** (`api.nasdaq.com/api/quote/<SYM>/chart`), which returns 500+ settled daily OHLC bars *and* the live quote in one call, with the Yahoo **history HTML page** used for the two volatility indices and the two share-class tickers Nasdaq does not carry. Three consequences: (1) the breadth denominator is the real S&P 500 constituent list (502 of 503, `VYLR` excluded for insufficient history), same as the prior run; (2) sector rotation is computed from sector-ETF price performance, as before; (3) `^VIX3M` remains the long-end vol proxy per `screen.py:compute_regime()`, so `uncertainty` is computable.

## Breadth

| Measure | 2026-10-26 close | 2026-10-27 (in progress) |
| --- | --- | --- |
| S&P 500 above 20-DMA | 71.5% (359 / 502) | 72.7% |
| S&P 500 above 50-DMA | 59.4% | 59.4% |
| Index ETFs below their 20-DMA | 4 of 5 (SPY, QQQ, QQQE, IWM) | 3 of 5 (SPY, QQQ, QQQE) |
| Names below their own 20-DMA | 143 of 502 | 137 of 502 |

Breadth at 71.5% is a healthy tape and it is *improving*, not decaying — the count of names below their own 20-DMA has fallen from 152 on the 2026-10-23 settle to 143, and 59.4% of the index sits above its 50-DMA. The divergence is the signal and it has not resolved: 4 of the 5 index ETFs are still below their 20-DMA on the settle, and only RSP sits above both its 20-DMA and 50-DMA. That is the signature of a cap-weighted index being dragged by a complex that the median constituent does not share.

## Index detail

| Index | Close (10-26) | 20-DMA | 50-DMA | Ext from 50 | ATR% | ATR× median | Live 10-27 | Live vs 20-DMA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 765.37 | 770.14 | 767.59 | -0.29% | 0.95 | 0.92 | 769.42 (+0.53%) | -0.09% |
| RSP | 217.29 | 213.04 | 215.24 | +0.95% | 0.95 | 0.94 | 217.18 (-0.05%) | +1.94% |
| QQQ | 712.20 | 734.02 | 725.43 | -1.82% | 1.74 | 1.07 | 720.71 (+1.19%) | -1.81% |
| QQQE | 118.06 | 119.89 | 120.28 | -1.85% | 1.40 | 1.09 | 119.04 (+0.83%) | -0.71% |
| IWM | 276.99 | 277.04 | 285.85 | -3.10% | 1.31 | 0.81 | 279.92 (+1.06%) | +1.04% |

The equal-weight/cap-weight gap is the cleanest read on the session: RSP is flat while QQQ is up more than a percent, and the chip complex is doing the work (the live tape has the SOX group and the AI/semicap names leading while refiners and the industrials complex get hit). SPY is the one to watch — it is trading within a tenth of a percent of its own 20-DMA, so the cap-weighted index has effectively made a round trip back to the line it broke on Monday. IWM is the improving leg: it crossed back above its 20-DMA intraday and still carries the most compressed volatility in the group (ATR×median 0.81).

## Volatility

| Measure | 2026-10-26 close | 2026-10-27 live |
| --- | --- | --- |
| ^VIX | 18.39 | 17.77 |
| ^VIX3M | 19.94 | 19.62 |
| VIX / VIX3M | 0.922 | 0.906 |

The front end is trading *below* the 3-month term, so there is no front-end stress signal: `uncertainty` = false. The ratio has compressed further intraday (0.922 → 0.906) as the equity bid comes back and the vol market sells off, which is a constructive read: this is a rally on *falling* volatility, not a melt-up bid. Note the long end (VIX3M) remains the higher of the two legs, so the market is still paying up for the multi-month horizon ahead of this week's Fed decision and the Alphabet / Microsoft / Amazon earnings prints.

## Sector rotation

| Sector | ETF | Perf 1M | Perf 3M | Perf 6M | Composite | Members above 20-DMA | Ext from 50-DMA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Energy | XLE | +12.25% | +20.97% | +22.67% | +18.63 | 90.5% | +5.88% |
| Health Care | XLV | +5.03% | +7.19% | +24.97% | +12.39 | 88.3% | +4.94% |
| Information Technology | XLK | -5.07% | +8.90% | +16.04% | +6.62 | 48.0% | -0.75% |
| Consumer Staples | XLP | +7.19% | +1.03% | +6.83% | +5.02 | 90.9% | +3.05% |
| Financials | XLF | +2.15% | -2.74% | +8.13% | +2.51 | 77.6% | -0.10% |
| Consumer Discretionary | XLY | +3.35% | +1.58% | -3.04% | +0.63 | 66.0% | -0.14% |
| Materials | XLB | +3.17% | -1.83% | -0.77% | +0.19 | 83.3% | +0.02% |
| Real Estate | XLRE | +2.98% | -6.98% | -1.59% | -1.86 | 83.3% | +0.04% |
| Utilities | XLU | +7.69% | -6.52% | -7.88% | -2.24 | 90.3% | +2.05% |
| Industrials | XLI | -2.04% | -8.51% | -3.22% | -4.59 | 60.2% | -0.35% |
| Communication Services | XLC | -8.06% | -5.31% | -10.33% | -7.90 | 36.4% | -6.28% |

Rotation is still commodity-and-defensive at the top of the composite table — Energy leads at +18.63 with 90.5% of members above their 20-DMA and the whole group stretched +5.88% above its 50-DMA. That is the one crowded corner of the market. At the bottom, Communication Services is the worst composite (-7.90) on only 36.4% member breadth. The wrinkle today is that the rotation is being *re-priced* rather than continued: energy is the top composite but the live tape has Energy ETF down -1.80% with the refiners (VLO, MPC, PSX) down hard on falling crude, while Technology is up +1.63% intraday off a chip rally — the same complex that has the worst 1-month performance on the board. Today's leadership is a bounce inside a downtrend for tech, not a rotation into it, and the prior run's read still stands.

## Regime flags

| Flag | Value | Rule |
| --- | --- | --- |
| `size_cut_pct` | **0** | 50 when a majority of index ETFs are < 20-DMA **and** breadth < 40%. 4 of 5 indices are below, but breadth is 71.5%, so the second condition fails. |
| `uncertainty` | **false** | VIX / VIX3M > 1. Ratio is 0.922 (0.906 intraday). |
| `late_cycle` | **false** | Any index ETF > 6% above its 50-DMA. Max is +0.95% (RSP); max ATR% vs 252-day median is 1.09×. |

No position-sizing action is implied by this snapshot. The `size_cut_pct` rule is intentionally two-legged, and the breadth leg vetoes it: a market sitting on its 20-DMAs with 59% above its 50-DMA is a different animal from four index ETFs punching below theirs with internals deteriorating, which is not what the tape shows. The one thing that would change the read is the energy complex rolling over — it is the crowded corner of the market and it is the sector where a 6% extension unwinds fastest.

## Method & caveats

- **Data source.** Nasdaq public chart API (`api.nasdaq.com/api/quote/<SYM>/chart?assetclass=…`, 2024-10-01 to 2026-10-27) for 501 constituents, all 16 index/sector ETFs — daily settled OHLC and the live quote arrive in the same response, so the intraday overlay costs no extra calls. Yahoo Finance **history HTML page** for `^VIX`, `^VIX3M`, `BRK-B` and `BF-B` (Nasdaq carries no data for the two Berkshire share classes and no volatility indices). The Yahoo *chart* API — the prior run's source — is 429-throttled from this egress and was abandoned after 521/521 rejections; Yahoo *HTML* on the same host is not throttled.
- **Pipeline validation.** Recomputed at the 2026-10-23 bar, this implementation reproduces the prior published run's close, 20-DMA, 50-DMA, 200-DMA, ATR(14), ATR%, ATR×median, 50-DMA extension and all four performance windows for all five index ETFs — **60 of 60 values match** (`daily-screens/2026-10-26/breadth-snapshot.json`). Conventions confirmed along the way: ATR(14) is the *simple mean of True Range*, not Wilder smoothing; performance windows are 21 / 63 / 126 / 252 **trading sessions**; the `ATR× median` column is ATR% against the trailing 252-bar median of ATR%.
- **Data lag.** Primary figures are on the **2026-10-26** settle, the most recent completed bar. The 2026-10-27 session was still open at the time of the run (2026-10-27 14:35 ET); its values appear only in the explicitly labeled live columns. Live constituent breadth compares the live print against 20-DMAs computed through 2026-10-26.
- **Constituent coverage.** 502 of 503 S&P 500 constituents produced usable history. `VYLR` returned only 18 bars and is excluded from every denominator. `BRK-B` and `BF-B` carry one year of history rather than two, so their 252-bar ATR median is computed on a shorter window; neither is close to any threshold, so the effect is immaterial. Sector membership uses the GICS sector from the Wikipedia constituent table, which can lag an index reclassification by a few days.
- **Definition notes.** `Perf 1M / 3M / 6M` are computed on **trading sessions** (21 / 63 / 126 bars), not calendar months, so they differ slightly from a vendor's calendar-month return. Composite = equal-weight mean of the three, matching the skill's equal-weight RS convention. Sector member extension is the mean across that sector's constituents.
- **Not computed.** `^VXV` and `^VXVCLS` return zero bars on Yahoo, so the VIX/VXV ratio is unavailable; `^VIX3M` is used as the long-end proxy per `screen.py:compute_regime()`. The `mcap > $10B` breadth proxy from the skill's SQL was not reproduced — no market-cap source is available in this sandbox — so the headline uses actual S&P 500 membership instead. Live prices are a snapshot, not a tick, and the constituent and index quotes were taken within a few minutes of each other.

## Files

- `breadth-snapshot.md` — this report.
- `breadth-snapshot.json` — full computed payload: per-index detail, sector rotation, live-session overlay, volatility, regime.
- `breadth-snapshot.csv` — per-constituent rows (close, 20/50-DMA, breadth flags, 1M/3M performance, ATR%, live price and change), `_source=nasdaq_public_chart_api`.
- `_regime.json` — the regime contract payload consumed by the 18:30 ET daily sweep and the 07:37 ET pre-market brief. The sweep's copy is authoritative; this one will be overwritten on the same date.
