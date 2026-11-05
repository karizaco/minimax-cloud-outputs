---
fire_time_et: 2026-11-05 18:30:46 ET
cron: #09 stock-screener-daily-sweep-18:30
data_date: 2026-11-05 (settled regular-session close; feed is NOT T+1 for this file — every number below is the 2026-11-05 close)
data_date_t_plus_1: false
breadth_universe: "NYSE/NASDAQ/AMEX, TradingView type=stock, market_cap_basic > $10B — 981 names (totalCount 981, 981 fetched, 981 unique). No domicile filter; type=stock includes REITs."
breadth_universe_source: "POST https://scanner.tradingview.com/america/scan (settled close columns SMA20/SMA50/SMA200/ATR)"
vix_quote_time: "2026-11-05T16:15:01 ET — VIX and VIX3M from the Cboe delayed-quote CDN (cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json and _VIX3M.json); pulled twice, both pulls identical (vix_stable: true)"
vix: 28.18
vix3m: 25.55
vix_ratio: 1.1029
cross_reference: "intraday counterpart: daily-screens/2026-11-05/breadth-snapshot.md (cron #10, 14:00 ET)"
read_type: "END-OF-DAY read from the settled close — this file is authoritative for 2026-11-05 breadth; breadth-snapshot.md is the 14:00 ET intraday snapshot and is expected to differ"
---

# Breadth & regime — 2026-11-05 (end-of-day)

**One volatility pair is used everywhere in this document: VIX 28.18 / VIX3M 25.55, both stamped 2026-11-05T16:15:01 ET by the Cboe delayed-quote CDN.** No second reading is mixed in.

## Headline

A violent, AI-hardware-led de-rating: **58.31%** of the 981-name large-cap universe closed above its 20-DMA and **145 names advanced against 832 declined**, but only **1 of the 5** index ETFs (RSP) sits above its 20-DMA — the cap-weighted index is below its 20-day mean while the *average* stock is not. The divergence is **+38.31 pp (BROAD)**: the average large cap is materially healthier than the index, which is the signature of a mega-cap-led de-rating, not of a healthy market. `size_cut_pct` stays at 0 only because the rule needs breadth under 40% and breadth is 58.31%; `uncertainty` is **true** because the VIX (28.18) sits above the VIX3M (25.55) for the first time in this leg.

| Metric | Value | Rule |
|---|---|---|
| % large caps above 20-DMA | **58.31%** (572/981) | size-cut needs < 40% → not triggered |
| % large caps above 50-DMA | 48.93% (480/981) | — |
| % large caps above 200-DMA | 46.28% (454/981) | — |
| Advance / decline (universe) | 145 / 832 / 4 | — |
| Median change (universe) | -1.93% | — |
| Index ETFs above 20-DMA | **20.0%** (1 of 5) | < 50% → index_below_20sma = true |
| Breadth divergence | **+38.31 pp (BROAD)** | ≥ +15 pp → the broad universe is healthier than the index |
| VIX / VIX3M | **1.1029** | > 1.0 → uncertainty; **true** |
| Max ATR extension from 50-DMA | RSP +0.92% (QQQE -6.57%) | > 6% → late_cycle; **false** |
| Volatility pair stability | `vix_stable: true` (two pulls, identical) | — |

## Regime payload (`_regime.json`)

```json
{
  "_schema": 2,
  "size_cut_pct": 0,
  "uncertainty": true,
  "late_cycle": false,
  "breadth_pct_spx": 58.31,
  "index_below_20sma": true,
  "vix": 28.18,
  "vix3m": 25.55,
  "atr_extensions": {
    "SPY":  {"extension_pct": -4.3575},
    "RSP":  {"extension_pct": 0.9214},
    "QQQ":  {"extension_pct": -10.4145},
    "QQQE": {"extension_pct": -6.5713},
    "IWM":  {"extension_pct": -4.1225}
  }
}
```

`uncertainty` is the flag that changed today: front-end stress is now *above* the long end (ratio 1.1029), where on 2026-11-04 the curve carried a 0.88 discount. `late_cycle` is false — but note that it is false because every index ETF is *below* its 50-DMA, which is the opposite of the extension case the flag was built for.

## Index ETFs — settled 2026-11-05 close

| ETF | Close | Day % | 20-DMA | 50-DMA | Extension from 50-DMA | Above 20-DMA |
|---|---|---|---|---|---|---|
| SPY | 733.00 | **-4.41%** | 765.53 | 766.40 | -4.36% | no (by 4.25%) |
| RSP | 216.87 | **-2.89%** | 216.57 | 214.89 | +0.92% | yes (by 0.14%) |
| QQQ | 647.05 | **-6.49%** | 712.40 | 722.27 | -10.41% | no (by 9.17%) |
| QQQE | 111.52 | -4.99% | 118.12 | 119.36 | -6.57% | no (by 5.58%) |
| IWM | 270.98 | -4.59% | 277.11 | 282.63 | -4.12% | no (by 2.21%) |

RSP (equal-weight) beating SPY (cap-weight) by **152bp** is the cleanest statement of the session: the average stock fell a third as hard as the mega-cap index. QQQ is the extreme — **-6.49%** and **10.41% below its 50-DMA**, the worst position of any index line.

## Sector rotation — the 981-name large-cap universe (TradingView taxonomy)

| Sector | n | % > 20-DMA | % > 50-DMA | Perf 1M | Perf 3M | Perf 6M | Median day |
|---|---|---|---|---|---|---|---|
| Consumer Non-Durables | 34 | 91.2% | 97.1% | +14.5% | +3.1% | +9.6% | -0.37% |
| Consumer Durables | 19 | 94.7% | 73.7% | +13.4% | +3.6% | +6.3% | -1.82% |
| Consumer Services | 36 | 80.6% | 75.0% | +12.5% | +1.2% | +2.9% | -1.43% |
| Retail Trade | 33 | 81.8% | 90.9% | +14.2% | +5.0% | +4.2% | -1.65% |
| Health Services | 16 | 87.5% | 93.8% | +10.3% | +11.2% | +19.2% | -1.32% |
| Health Technology | 70 | 75.7% | 78.6% | +7.5% | +12.9% | +27.4% | -3.07% |
| Utilities | 51 | 64.7% | 64.7% | +7.1% | 0.0% | -4.0% | -0.45% |
| Transportation | 22 | 68.2% | 68.2% | +5.4% | -3.7% | +8.3% | -3.85% |
| Finance | 317 | 66.2% | 37.9% | +0.8% | -5.8% | -5.0% | -1.16% |
| Energy Minerals | 23 | **4.3%** | 4.3% | +0.4% | +7.9% | +8.7% | -2.75% |
| Technology Services | 93 | 40.9% | 49.5% | -0.7% | +3.3% | +20.0% | -2.11% |
| Industrial Services | 31 | 29.0% | 29.0% | -1.4% | -3.6% | -4.3% | -3.27% |
| Distribution Services | 15 | 60.0% | 46.7% | -1.7% | -7.3% | +2.7% | -4.05% |
| Non-Energy Minerals | 28 | 50.0% | 32.1% | -3.1% | -7.5% | -6.6% | -3.15% |
| Communications | 13 | 53.8% | 30.8% | -4.5% | -4.7% | -16.7% | -0.13% |
| Producer Manufacturing | 48 | 25.0% | 25.0% | -7.7% | -15.0% | -14.7% | -4.75% |
| **Electronic Technology** | 85 | **18.8%** | **20.0%** | **-19.2%** | **-19.6%** | -17.3% | **-9.26%** |

Electronic Technology is the epicentre: a **-9.26% median day** with only 18.8% of names above their 20-DMA and a 1M relative strength of -19.2%. Producer Manufacturing (-4.75% median, 25% above 20-DMA) is the second-worst. Defensive consumer, retail, health services and utilities held up. Note that the sector stats are **medians within a sector**, so the 981-name universe average (-1.93%) is far better than the cap-weighted index (-4.41%): the damage is concentrated in the AI-hardware complex, not spread across the market.

## Sector ETF read-through (same 2026-11-05 close)

| ETF | Day % | 1M | 3M | 6M |
|---|---|---|---|---|
| **SMH (semis)** | **-11.21%** | -29.9% | -23.3% | -18.8% |
| **SOXX (semis)** | **-12.15%** | -33.3% | -27.4% | -21.5% |
| **ARKK (innovation)** | **-8.98%** | -22.2% | -5.0% | -6.7% |
| XLK (tech) | -8.00% | -19.8% | -13.6% | -5.4% |
| XBI (biotech) | -6.73% | -5.4% | -5.4% | +10.9% |
| PAVE (infrastructure) | -5.90% | -6.9% | -13.7% | -11.5% |
| IGV (software) | -4.39% | -10.6% | -2.6% | +10.2% |
| XLI (industrials) | -4.12% | -4.8% | -12.4% | -7.2% |
| XLY (cons. disc.) | -3.83% | +6.1% | -0.7% | -2.2% |
| TAN (solar) | -3.71% | +0.4% | -16.4% | -27.6% |
| XME (metals & mining) | -5.60% | -16.9% | -20.5% | -25.8% |
| IYT (transport) | -3.54% | +2.5% | -4.9% | +1.3% |
| XRT (retail) | -2.83% | +9.9% | +0.7% | +7.7% |
| XLE (energy) | -2.98% | -2.2% | +7.1% | +10.4% |
| XLB (materials) | -2.91% | +5.6% | 0.0% | +1.0% |
| XLF (financials) | -2.87% | +6.5% | -0.2% | +11.3% |
| IYC (cons. staples) | -2.60% | +8.6% | +1.2% | +0.7% |
| KRE (regional banks) | -2.46% | +2.6% | -5.4% | +3.1% |
| XLV (health) | -2.50% | +10.1% | +12.8% | +27.9% |
| XLRE (real estate) | -1.82% | +8.6% | -1.2% | -0.5% |
| IYR (real estate) | -1.71% | +8.2% | -1.9% | -0.6% |
| ITB (homebuilders) | -1.67% | +15.2% | -0.6% | +5.4% |
| XLU (utilities) | -0.71% | +7.2% | +0.2% | -4.5% |
| XLC (comm.) | -0.59% | -6.8% | -5.4% | -10.8% |
| XLP (staples) | -0.75% | +12.6% | +8.0% | +8.0% |
| IBB (biotech) | -5.04% | +0.3% | +7.1% | +23.9% |
| GDX (miners) | **+1.37%** | -2.3% | -4.0% | -7.9% |

Every sector ETF fell except GDX. The dispersion inside "technology" is the story of the session: SOXX -12.15% and SMH -11.21% against XLK -8.00% and IGV -4.39% — the damage is in hardware and connectivity, not software.

## Index levels (Cboe delayed-quote CDN, settled prints)

| Index | Close | Last trade time | Day |
|---|---|---|---|
| ^SPX | 7353.73 | 2026-11-05 16:14:59 ET | -4.29% (open 7678.72, low 7350.35) |
| ^NDX | 26629.81 | 2026-11-05 16:14:59 ET | -6.34% (open 28437.17, low 26606.43) |
| ^RUT | 2729.89 | 2026-11-05 16:09:55 ET | -4.39% (open 2855.25) |
| ^DJI | 51786.72 | **2026-11-03 16:14:59 ET — stale** | not used (see flags) |

DIA's -3.53% (from the bridge) is the Dow's proxy for 2026-11-05; the Cboe `_DJI` record was last stamped two sessions earlier and is **not** used anywhere in this document.

## Cross-check against the T+1 shibui feed (2026-11-04 session)

The stylist screens in this directory run on shibui, whose newest settled session on the cron day is **2026-11-04**. Its own breadth read for that session (909-name population, market cap > $10B from shibui's `valuation`):

| | shibui 2026-11-04 | TradingView 2026-11-05 |
|---|---|---|
| Large-cap population | 909 names | 981 names |
| % above 20-DMA | 69.42% | 58.31% |
| % above 50-DMA | 65.35% | 48.93% |
| Advance / decline | 658 / 250 | 145 / 832 |
| Index ETFs above 20-DMA | 40% (2 of 5) | 20% (1 of 5) |
| Breadth divergence | +29.42 pp (BROAD) | +38.31 pp (BROAD) |
| SPY extension from 50-DMA | -0.03% (11-04 close) | -4.36% |
| QQQ extension from 50-DMA | -4.37% | -10.41% |

The two feeds agree on the **shape** — the index is below its 20-DMA while the broad universe is not, and QQQ is the weakest major index — but they describe **different sessions and different populations** (909 vs 981 names, because the market-cap source differs: shibui `valuation` vs TradingView `market_cap_basic`). **Do not treat the two breadth percentages as the same series.** The divergence widened from +29.42 pp to +38.31 pp in one session: the cap-weighted index deteriorated much faster than the average large cap.

### Breadth percentile (shibui series, 1-year expanding window)

The 2026-11-04 shibui reading sits at the **94.57th percentile** of its own trailing 1-year distribution (`ABOVE_NORMAL`), and the 50-DMA split at the 89.13th percentile. The 2026-11-05 TradingView reading has **no percentile of its own**: TradingView's scanner is a current snapshot with no history, and the shibui series that *does* have history stops one session earlier. The percentile is therefore published against the shibui series and labelled as such — it is context for the 11-04 reading, not a band for today's number.

### Last 5 shibui sessions (the trailing series)

| Session | n | % > 20-DMA | % > 50-DMA | Adv / Dec | ETFs > 20-DMA | Divergence |
|---|---|---|---|---|---|---|
| 2026-11-04 | 909 | 69.42% | 65.35% | 658 / 250 | 2 of 5 | +29.42 pp |
| 2026-11-03 | 909 | 64.14% | 59.96% | 360 / 547 | 2 of 5 | +24.14 pp |
| 2026-11-02 | 909 | 65.13% | 60.95% | 598 / 311 | 2 of 5 | +25.13 pp |
| 2026-10-30 | 909 | 63.70% | 55.67% | 377 / 532 | 2 of 5 | +23.70 pp |
| 2026-10-29 | 909 | 69.20% | 60.07% | 675 / 234 | 2 of 5 | +29.20 pp |

## Source health

| Source | URL / query | Status | Used for |
|---|---|---|---|
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` (large-cap universe, index ETFs, sector ETFs, movers, >$1B universe in 3 pages) | ok — totalCount 981, fetched 981, 981 unique; 2,593 names in the $1B+ universe, 2,593 unique, no paging loss | close, SMA20/50/200, ATR, Perf 1M/3M/6M, sector, market cap, RVOL |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/quotes/{_VIX,_VIX3M,_SPX,_NDX,_RUT,_DJI}.json` | ok — `last_trade_time` 16:15:01 ET (VIX pair, two pulls identical), 16:14:59 / 16:09:55 ET (indexes); `_DJI` stale at 2026-11-03 | VIX, VIX3M, index levels (independent of TV) |
| MCP bridge (`market-recap`) | `get_quotes` for 15 index/ETF symbols; `top_movers` for gainers/losers | ok — all 15 symbols found, `as_of` 21:00:00–21:00:01 UTC (16:00 ET), `market_state: post` | index/ETF closes and day %, movers |
| shibui via MCP bridge | `stock_data_query` — resolve_date, prefilter, 8 sweep branches (paged), breadth SQL, 1-year breadth series, tier ranges | ok — all 13 calls returned rows; branch coverage asserted | screen metrics, T+1 breadth cross-check, percentile series, Stalk gate |
| Nasdaq `/info` | `api.nasdaq.com/api/quote/{SYM}/info` | ok — 12/12 names | official 4:00 PM close cross-check (see below) |
| MCP availability probe | `probe_mcp.py` | `catalog_ok total=135 finance_tools=0` | no finance MCP registered; the bridge is the finance path |
| Finviz | — | not attempted | known Cloudflare 403 from this egress |
| Yahoo JSON | — | not used | — |

**Close-source verification.** On the 12 Focus/Tier-A names, the bridge's `get_quotes` price and TradingView's `close` agreed on **12 of 12 to the cent** (DUOL 157.02, ENOV 28.62, KD 16.18, LIVN 91.14, OUST 30.52, VRDN 28.55, XNCR 34.05, XYZ 84.04, YOU 56.50, CRCT 9.25). Nasdaq's `secondaryData` differs on two of them by more than 0.6% — ENOV (bridge 28.62 vs Nasdaq 28.44, **-0.63%**) and ARRY (bridge 5.30 vs Nasdaq 5.245, **-1.05%**) — and the disagreement runs in BOTH directions across the other ten (Nasdaq higher on DUOL, KD, LIVN, OUST, XNCR, CRCT; lower on YOU, VRDN), so it is a different auction reference on thin names rather than a stale feed. **A same-day finding from cron #20 (`docs/IMPROVEMENTS-cron20-eod-watchlist.md` §1) applies directly here: on the 2026-11-05 session Nasdaq's `/info` served PRE-AUCTION prints stamped "Closed at Nov 5, 2026 4:00 PM ET", so its settlement stamp is not proof of its value.** The bridge/TradingView pair is therefore the published source here, and Nasdaq is a third reading that was checked and found to differ — not a confirmation. Nasdaq's `primaryData` is the 18:40 ET after-hours print and is not used for a settled close anywhere in this directory.

## Caveats

- The breadth universe is a **market-cap proxy**, not an index membership list: shibui has no S&P-500 table and TradingView's `market_cap_basic` does not equal the index's float-adjusted cap. 981 names at $10B+ is the population stated above, not "the market".
- `type=stock` includes REITs and foreign-domiciled US listings; no domicile filter was applied.
- Sector labels are **TradingView's taxonomy** (Health Technology, Commercial Services, …), not GICS.
- ATR extension here is `(close − SMA50) / SMA50`, the same formula the skill's breadth SQL uses; the skill's "6%" late-cycle test is applied to that percentage, not to an ATR multiple.
- **One session is missing from the ETF set.** `_DJI` was stale on the Cboe CDN (last stamped 2026-11-03), so the Dow's day move is published from DIA via the bridge rather than from the index print.
- The divergence band and the percentile are computed on the **shibui population**, which is one session behind and 72 names smaller. The 2026-11-05 divergence value (+38.31 pp) is computed directly from the TradingView population and is the one published here.
