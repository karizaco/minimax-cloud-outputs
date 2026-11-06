---
fire_time_et: 2026-11-06 18:30:58 ET
cron: #09 stock-screener-daily-sweep-18:30
data_date: 2026-11-06 (settled regular-session close; feed is NOT T+1 for this file — every number below is the 2026-11-06 close)
data_date_t_plus_1: false
breadth_universe: "NYSE/NASDAQ/AMEX, TradingView type=stock, market_cap_basic > $10B — 986 names (totalCount 5711 for the full exchange/type universe, 986 fetched above the $10B floor, 986 unique). No domicile filter; type=stock includes REITs."
breadth_universe_source: "POST https://scanner.tradingview.com/america/scan (settled close columns SMA20/SMA50/SMA200/ATR)"
vix_quote_time: "2026-11-06T16:15:01 ET — VIX and VIX3M from the Cboe delayed-quote CDN (cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json and _VIX3M.json); pulled twice, both pulls identical (vix_stable: true)"
vix: 25.64
vix3m: 24.6
vix_ratio: 1.0423
cross_reference: "intraday counterpart: daily-screens/2026-11-06/breadth-snapshot.md (cron #10, 14:00 ET)"
read_type: "END-OF-DAY read from the settled close — this file is authoritative for 2026-11-06 breadth; breadth-snapshot.md is the 14:00 ET intraday snapshot and is expected to differ"
---

# Breadth & regime — 2026-11-06 (end-of-day)

**One volatility pair is used everywhere in this document: VIX 25.64 / VIX3M 24.6, both stamped 2026-11-06T16:15:01 ET by the Cboe delayed-quote CDN.** No second reading is mixed in.

## Headline

A relief rally that only the mega-caps bought. **QQQ +1.40%** and **SMH +3.62%** while the equal-weight **RSP fell -0.38%** and the Dow proxy **DIA -0.40%**: the index rose because the AI complex rose, not because the average stock did. Breadth confirms it — **57.26%** of the 986-name large-cap universe closed above its 20-DMA, **425 names advanced against 549 declined** (median **-0.23%**), and **0 of the 5** index ETFs sit above their 20-DMA. The divergence is therefore **+57.26 pp (BROAD)** — the widest of this series, and the fourth consecutive session in which the cap-weighted index is below its 20-day mean while the broad universe is not. `size_cut_pct` stays at 0 because the rule needs breadth under 40% and breadth is 57.26%; `uncertainty` is **true** (VIX 25.64 above VIX3M 24.6, ratio 1.0423); `late_cycle` is **false**.

The macro driver was the **October jobs report**: payrolls **+165,000** against roughly 59,000–70,000 expected, unemployment down to **4.1%**, wages +3.1% y/y — which put a **December Fed hike back in the market at ~75–85% odds** (from ~67–75% the day before) and pushed the 10-year back above 4.87% and the 30-year above 5.28%. That is why the rate-sensitive corner (RSP, DIA, XLRE, GLD) sold while the long-duration AI names rallied: this was a duration rally inside a rising-rate tape, not a risk-on session.

| Metric | Value | Rule |
|---|---|---|
| % large caps above 20-DMA | **57.26%** (564/986) | size-cut needs < 40% → not triggered |
| % large caps above 50-DMA | 48.68% | — |
| % large caps above 200-DMA | 46.94% | — |
| Advance / decline (universe) | 425 / 549 / 12 | — |
| Median change (universe) | -0.23% | — |
| Index ETFs above 20-DMA | **0.0%** (0 of 5) | < 50% → index_below_20sma = true |
| Breadth divergence | **+57.26 pp (BROAD)** | ≥ +15 pp → the broad universe is healthier than the index |
| VIX / VIX3M | **1.0423** | > 1.0 → uncertainty; **true** |
| Max ATR extension from 50-DMA | RSP +0.59% (QQQ -9.00%) | > 6% → late_cycle; **false** |
| Volatility pair stability | `vix_stable: true` (two pulls, identical) | — |

## Regime payload (`_regime.json`)

```json
{
  "_schema": 2,
  "size_cut_pct": 0,
  "uncertainty": true,
  "late_cycle": false,
  "breadth_pct_spx": 57.26,
  "index_below_20sma": true,
  "vix": 25.64,
  "vix3m": 24.6,
  "atr_extensions": {
    "SPY": {
      "extension_pct": -3.969
    },
    "RSP": {
      "extension_pct": 0.5904
    },
    "QQQ": {
      "extension_pct": -8.9977
    },
    "QQQE": {
      "extension_pct": -5.9816
    },
    "IWM": {
      "extension_pct": -2.9913
    }
  }
}
```

`uncertainty` is the flag that has now held for a second session: front-end stress is still above the long end (ratio 1.0423), even though the VIX itself fell 9.01% on the day. `late_cycle` is false — but note that it is false because **every** index ETF is *below* its 50-DMA, which is the opposite of the extension case the flag was built for.

## Index ETFs — settled 2026-11-06 close

| ETF | Close | Day % | 20-DMA | 50-DMA | Extension from 50-DMA | Above 20-DMA |
|---|---|---|---|---|---|---|
| SPY | 735.29 | +0.31% | 763.36 | 765.68 | -3.97% | no (3.68% below) |
| RSP | 216.05 | -0.38% | 216.72 | 214.78 | +0.59% | no (0.31% below) |
| QQQ | 656.10 | +1.40% | 707.64 | 720.97 | -9.00% | no (7.28% below) |
| QQQE | 112.01 | +0.44% | 117.63 | 119.14 | -5.98% | no (4.78% below) |
| IWM | 273.67 | +0.99% | 276.84 | 282.11 | -2.99% | no (1.15% below) |

RSP (equal-weight) underperforming SPY (cap-weight) by **69bp** is the cleanest statement of the session: the mega-cap index rose while the average S&P name fell. RSP is now the only index line within 1% of its 20-DMA (0.31% below), and it is the only one above its 50-DMA (+0.59%). QQQ remains the extreme — **9.00% below its 50-DMA** even after a +1.40% day.

## Sector rotation — the 986-name large-cap universe (TradingView taxonomy)

| Sector | n | % > 20-DMA | % > 50-DMA | Perf 1M | Perf 3M | Perf 6M | Median day |
|---|---|---|---|---|---|---|---|
| Consumer Durables | 19 | 89.5% | 68.4% | +12.6% | +1.3% | +3.6% | -0.94% |
| Consumer Non-Durables | 34 | 85.3% | 91.2% | +11.0% | +2.0% | +8.0% | -1.79% |
| Commercial Services | 23 | 82.6% | 86.4% | +14.0% | +8.3% | +12.0% | -0.40% |
| Consumer Services | 35 | 80.0% | 71.4% | +9.6% | +1.1% | +3.0% | -0.82% |
| Health Technology | 71 | 77.5% | 81.7% | +9.5% | +12.5% | +27.5% | +0.55% |
| Process Industries | 22 | 77.3% | 68.2% | +7.9% | +0.5% | +4.1% | -0.98% |
| Retail Trade | 33 | 75.8% | 87.9% | +12.0% | +3.8% | +2.4% | -1.13% |
| Health Services | 16 | 75.0% | 100.0% | +7.2% | +9.3% | +20.0% | -1.28% |
| Communications | 13 | 69.2% | 38.5% | -4.1% | -7.8% | -14.3% | -0.06% |
| Utilities | 51 | 66.7% | 64.7% | +6.2% | -0.5% | -4.4% | -0.57% |
| Finance | 315 | 65.1% | 34.6% | +1.4% | -5.7% | -4.9% | -0.20% |
| Transportation | 23 | 56.5% | 60.9% | +4.9% | -5.3% | +7.5% | -1.70% |
| Non-Energy Minerals | 29 | 55.2% | 41.4% | +2.4% | -6.1% | -5.0% | +1.33% |
| Distribution Services | 15 | 53.3% | 46.7% | -0.7% | -8.1% | +4.9% | -0.17% |
| Technology Services | 95 | 35.1% | 48.9% | -0.0% | +2.2% | +18.0% | -0.38% |
| Producer Manufacturing | 50 | 30.0% | 28.0% | -5.6% | -13.3% | -14.4% | +1.61% |
| Industrial Services | 31 | 25.8% | 32.3% | -2.2% | -4.7% | -5.0% | -0.25% |
| Electronic Technology | 86 | 23.3% | 25.6% | -17.1% | -17.8% | -13.9% | +2.66% |
| Energy Minerals | 23 | 4.3% | 4.3% | -2.3% | +8.7% | +8.3% | -0.60% |
| Miscellaneous | 2 | 0.0% | 0.0% | -13.1% | -12.9% | -22.3% | +1.19% |

The sector table shows the same split as the index table, only more clearly: the **median** name fell 0.23% while the cap-weighted index rose, because the two biggest Technology Services and Electronic Technology blocks carried it. Electronic Technology is the epicentre of the whole two-week episode and is still the worst 1-month sector (**-17.1%**) with only **23.3%** of names above their 20-DMA, even though its median day was **+2.66%** — the rebound is a relief bounce inside a broken structure. **Energy Minerals is the damaged sector that never bounced: 4.3% above the 20-DMA, unchanged from 2026-11-04**, on a -0.60% median day.

## Sector ETF read-through (same 2026-11-06 close)

| ETF | Day % | 1M | 3M | 6M |
|---|---|---|---|---|
| SMH | +3.62% | -25.3% | -20.5% | -15.9% |
| SOXX | +3.51% | -29.0% | -24.9% | -18.8% |
| ARKK | +3.16% | -14.8% | -1.9% | -3.7% |
| XLK | +1.45% | -17.7% | -12.4% | -4.0% |
| XBI | +2.57% | +1.9% | -3.0% | +13.7% |
| PAVE | +0.81% | -5.5% | -13.0% | -10.8% |
| IGV | -0.13% | -10.6% | -2.7% | +10.1% |
| XLI | +0.12% | -4.1% | -12.3% | -7.1% |
| XLY | -0.05% | +5.9% | -0.8% | -2.2% |
| TAN | +3.38% | +5.0% | -13.5% | -25.1% |
| XME | +3.35% | -11.6% | -17.8% | -23.3% |
| IYT | -1.28% | +2.0% | -6.2% | +0.0% |
| XRT | -1.72% | +8.4% | -1.1% | +5.8% |
| XLE | -0.02% | -3.8% | +7.1% | +10.3% |
| XLB | -0.73% | +5.4% | -0.7% | +0.3% |
| XLF | -0.59% | +6.8% | -0.8% | +10.6% |
| IYC | -0.59% | +7.6% | +0.6% | +0.1% |
| KRE | -0.15% | +4.2% | -5.5% | +3.0% |
| XLV | -0.06% | +10.1% | +12.7% | +27.8% |
| XLRE | -0.68% | +6.8% | -1.9% | -1.2% |
| IYR | -0.61% | +6.7% | -2.5% | -1.2% |
| ITB | -2.13% | +12.8% | -2.7% | +3.1% |
| XLU | -0.39% | +5.2% | -0.2% | -4.9% |
| XLC | +0.43% | -5.9% | -5.0% | -10.4% |
| XLP | -1.28% | +9.7% | +6.6% | +6.6% |
| IBB | +1.73% | +5.8% | +8.9% | +26.0% |
| GDX | +2.16% | +2.7% | -1.9% | -5.9% |

Semis led the bounce (**SMH +3.62%, SOXX +3.51%**) after being the epicentre of Thursday's rout, but both are still down **-25.3%** and **-29.0%** over one month. Defensive sectors did not participate: XLV -0.06%, XLP -1.28%, XLU -0.39%. Gold fell (GLD -0.79%) and long bonds were flat (TLT -0.01%) — the rates move, not a risk-off bid.

## Index levels (Cboe delayed-quote CDN, settled prints)

| Index | Close | Last trade time | Day |
|---|---|---|---|
| ^SPX | 7376.86 | 2026-11-06 16:14:59 ET | +0.31% (open 7377.65, low 7369.55) |
| ^NDX | 26989.99 | 2026-11-06 16:14:59 ET | +1.35% (open 26629.81, high 27316.09) |
| ^RUT | 2754.11 | 2026-11-06 16:09:55 ET | +0.89% (open 2731.05) |
| ^DJI | 51786.72 | **2026-11-03 16:14:59 ET — stale** | not used (see caveat) |

The Dow's day move is published from **DIA via the bridge (-0.40%)**: the Cboe `_DJI` record was last stamped **2026-11-03** — the second session in a row it has been stale — and is not used anywhere in this document. The Nasdaq-100's +1.35% against the Dow's -0.40% is the session in one line.

## Cross-check against the T+1 shibui feed (2026-11-05 session)

The stylist screens in this directory run on shibui, whose newest settled session on the cron day is **2026-11-05**. Its own breadth read for that session (891-name population, market cap > $10B from shibui's `valuation`):

| | shibui 2026-11-05 | TradingView 2026-11-06 |
|---|---|---|
| Large-cap population | 891 names | 986 names |
| % above 20-DMA | 59.26% | 57.26% |
| % above 50-DMA | 56.68% | 48.68% |
| Advance / decline | 155 / 734 | 425 / 549 |
| Index ETFs above 20-DMA | 1 of 5 | 0 of 5 |
| Breadth divergence | +39.26 pp (BROAD) | +57.26 pp (BROAD) |

The two feeds agree on the **shape** — the index is below its 20-DMA while the broad universe is not — but they describe **different sessions and different populations** (891 vs 986 names, because the market-cap source differs: shibui `valuation` vs TradingView `market_cap_basic`). **Do not treat the two breadth percentages as the same series.** The divergence widened from +39.26 pp on the 2026-11-05 session to +57.26 pp on 2026-11-06: the cap-weighted index and the average large cap are pulling further apart, not together.

### Breadth percentile (shibui series, 1-year expanding window)

The 2026-11-05 shibui reading sits at the **62.32th percentile** of its own trailing 1-year distribution (`NORMAL` — the 20–80 band), and the 50-DMA split at the **52.17th percentile**. The 2026-11-06 TradingView reading has **no percentile of its own**: TradingView's scanner is a current snapshot with no history, and the shibui series that *does* have history stops one session earlier. The percentile is therefore published against the shibui series and labelled as such — it is context for the 2026-11-05 reading, not a band for today's number.

### Last 5 shibui sessions (the trailing series)

| Session | n | % > 20-DMA | % > 50-DMA | Adv / Dec | ETFs > 20-DMA | Divergence |
|---|---|---|---|---|---|---|
| 2026-10-27 | 891 | 66.55% | 54.55% | 452 / 436 | 2 of 5 | +26.55 pp |
| 2026-10-28 | 891 | 64.20% | 54.43% | 457 / 429 | 4 of 5 | -15.80 pp |
| 2026-10-29 | 891 | 69.70% | 60.38% | 666 / 225 | 2 of 5 | +29.70 pp |
| 2026-10-30 | 891 | 64.31% | 56.23% | 376 / 515 | 2 of 5 | +24.31 pp |
| 2026-11-02 | 891 | 65.99% | 61.62% | 587 / 304 | 2 of 5 | +25.99 pp |
| 2026-11-03 | 891 | 64.53% | 60.49% | 347 / 542 | 2 of 5 | +24.53 pp |
| 2026-11-04 | 891 | 69.92% | 65.88% | 650 / 240 | 2 of 5 | +29.92 pp |
| 2026-11-05 | 891 | 59.26% | 56.68% | 155 / 734 | 1 of 5 | +39.26 pp |
## Source health

| Source | URL / query | Status | Used for |
|---|---|---|---|
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` (stocks universe 5,711 rows, funds universe 6,751 rows, one call each) | ok — totalCount 5,711 fetched 5,711 unique; funds totalCount 6,751 fetched 6,751 | close, SMA20/50/200, ATR, Perf 1M/3M/6M, sector, market cap, RVOL |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/quotes/{_VIX,_VIX3M,_SPX,_NDX,_RUT,_DJI}.json` | ok — `last_trade_time` 16:15:01 ET (VIX pair, two pulls identical), 16:14:59 / 16:09:55 ET (indexes); **`_DJI` stale at 2026-11-03** | VIX, VIX3M, index levels (independent of TV) |
| MCP bridge (`market-recap`) | `get_quotes` for 36 index/ETF symbols; `top_movers` for gainers and losers | ok — all 36 symbols found, `as_of` 21:00:00–21:00:01 UTC (16:00 ET), `market_state: post` | index/ETF closes and day %, movers |
| shibui via MCP bridge | `stock_data_query` — resolve_date, 8 sweep branches (paged), breadth SQL, 1-year breadth series, CANSLIM, 2 master-detail chunks | ok — every branch paged to `rows_passing` | screen metrics, T+1 breadth cross-check, percentile series, Stalk gate, skip flags |
| Nasdaq `/info` | `api.nasdaq.com/api/quote/{SYM}/info` | ok — 12/12 names; `secondaryData` (stamped "Closed at Nov 6, 2026 4:00 PM ET") agrees with the published close on **12 of 12** | official 4:00 PM close cross-check |
| web_search | 11 catalyst/macro queries | ok | catalyst sourcing for the table above |
| MCP availability probe | `probe_mcp.py` | `catalog_ok total=135 finance_tools=0` | no finance MCP registered; the bridge is the finance path |
| Finviz | — | not attempted | known Cloudflare 403 from this egress |
| Yahoo JSON | — | not used | — |

**Close-source verification.** On the 12 Focus names, Nasdaq's `secondaryData` — the print stamped *"Closed at Nov 6, 2026 4:00 PM ET"* — agreed with the published close on **12 of 12** (RUN 9.98, SEZL 149.43, APP 391.22, U 51.49, FUN 10.00, JOBY 5.93, WRBY 25.475, XERS 15.20, APPN 51.60, ACHC 37.00, MRNA 254.19, PURR 8.815). Nasdaq's `primaryData` on the same pulls is the **18:36 ET after-hours print** (SEZL 152.00 vs the 149.43 close) and is not used for a settled close anywhere in this directory. The bridge's `get_quotes` agreed with TradingView's `close` to the cent on all 36 index/ETF symbols (SPY 735.29, RSP 216.05, QQQ 656.10, QQQE 112.01, IWM 273.67, DIA 512.22), so the bridge/TradingView pair is the published source and Nasdaq is a third reading that confirmed it.

## Caveats

- The breadth universe is a **market-cap proxy**, not an index membership list: shibui has no S&P-500 table and TradingView's `market_cap_basic` does not equal the index's float-adjusted cap. 986 names at $10B+ is the population stated above, not "the market".
- `type=stock` includes REITs and foreign-domiciled US listings; no domicile filter was applied.
- Sector labels are **TradingView's taxonomy** (Health Technology, Commercial Services, …), not GICS.
- ATR extension here is `(close − SMA50) / SMA50`, the same formula the skill's breadth SQL uses; the skill's "6%" late-cycle test is applied to that percentage, not to an ATR multiple.
- **One session is missing from the ETF set.** `_DJI` was stale on the Cboe CDN (last stamped 2026-11-03), so the Dow's day move is published from DIA via the bridge rather than from the index print.
- The divergence band and the percentile are computed on the **shibui population**, which is one session behind and 95 names smaller. The 2026-11-06 divergence value (+57.26 pp) is computed directly from the TradingView population and is the one published here.
