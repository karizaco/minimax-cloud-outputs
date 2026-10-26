# Daily Stock Screener Sweep — 2026-10-26 (US/Eastern)

**Session:** Monday 2026-10-26 close. **Cron:** #9 `stock-screener-daily-sweep-18:30` (fired 18:33 ET).
**Data path:** TradingView public scanner (tier-2 fallback) + Yahoo Finance daily bars. **Session lag: none** — every price in this report is the settled 2026-10-26 close, pinned by Yahoo `regularMarketTime` = 2026-10-26 16:00 ET.

---

## ⚠ Deviations from the skill spec (read first)

| # | Spec says | What ran instead | Why | Impact |
|---|---|---|---|---|
| 1 | `mcp__shibui-finance__stock_data_query` (prefilter + 8-CTE sweep) | TradingView public scanner `POST /america/scan`, 20,095 rows | The whole MCP tier is **provably unbound** in this Cloud session (see QC). Discovery returned `partial=false` with an empty catalog, so this is disconnection, not a partial catalog. | Every shibui SQL screen was re-expressed in scanner columns. |
| 2 | `mcp__tradingview__screen_stocks` / `screen_etf` / `volume_breakout_scanner` | Same scanner, different column sets | Same root cause. | Jeff Sun's CANSLIM screen lost its **sales-growth leg** (`sales_growth_quarterly_yoy` is null on this source) — that sub-screen is **partial**, and is labelled as such everywhere it appears. |
| 3 | `mcp__tradingview-advanced__yahoo_price` for VIX/VXV | Yahoo chart API directly | Same root cause. | VIX leg computed. **VXV leg unavailable** (see Regime). |
| 4 | `financekit sector_rotation` | Sector-ETF relative strength from scanner `Perf.1M/3M/6M` | Same root cause. | Theme ranking is ETF-based, not the financekit rotation table. |
| 5 | Finviz fallback (tier 3) | Not reached | The tier-2 fallback succeeded, so the chain stopped there. | Finviz's HTTP 403 behaviour was not re-tested this run. |
| 6 | `ADR = AVG((high-low)/close, 20)` computed in SQL | Same formula, computed from Yahoo daily bars | No bar-level SQL available. | **Not a proxy** — true ADR, same definition. |
| 7 | Anticipation (coil) uses `avg(close,7)/avg(close,65)` and a 10-day base | `close/SMA50` and the 1-month range | The scanner exposes no 7/65-day averages. | Coil screen is a **coarser approximation**; 3 names qualified. |
| 8 | Hernandez step 3 = `yahoo-finance get_financial_statements` per candidate | Scanner `price_earnings_ttm` + `earnings_per_share_diluted_yoy_growth_ttm` | Avoids 30 extra single-ticker calls. | Fundamentals overlay is thinner than the spec's. |
| 9 | 3:55 PM reversal-bullish scan (Bonde, 8 criteria) | **Not run** | The cron fired at 18:33 ET; that screen is only valid 15:30–16:00 ET. | No `reversal-bullish-3:55` file. Not a failure — out of window. |
| 10 | IPO + high-short-float weekly refresh | **Not run** | Sunday-only screens; today is Monday. | No `ipo.md` / `high-short-float.md`. |
| 11 | Pre-market gapper (09:00 ET) and live RVOL re-rank (09:45–11:15 ET) | **Not run** | Outside this cron's window. | No `focus-rvol-snapshot.md`. |

**Fallback chain terminated at tier 2, as the zero-fallback policy requires.** No MCP call was retried, and no deeper tier was chained.

---

## Headline

A **rotation day with a violent single-name tail**. Breadth is healthy (71.5% of the S&P 500 above its 20-DMA) and VIX fell 5.4% to 18.39, but the headline indices (SPY, QQQ, QQQE, IWM) closed *below* their 20-DMA while equal-weight RSP and DIA stayed above it — the average stock is healthier than the cap-weighted index. Leadership rotated hard into Energy (XLE +12.5% in a month) and Healthcare (XLV +5.5%), while Communication Services (XLC −8.5%) and Technology (XLK −4.7%) lagged. On top of that rotation, semis ripped: **P +6.5%, NXPI +4.6%, ADI +4.3%, HEI +4.2%, CSCO +3.5%** — which is exactly what the Focus and Tier-A lists are built from.

**The caveat that most changes how to read this:** Tier-A is 8 names and 7 of the 8 are large-cap technology/semi names converging on the same catalyst, while the true "high-conviction" screens (parabolic short, parabolic long, EP gap) are nearly empty — 1, 2, and 2 names respectively. The list is a coherent *sector* call, not a collection of independently-convicted single-stock setups.

---

## Data path and QC

| Check | Result |
|---|---|
| MCP tier availability | `tool_search` → 0 hits for any finance keyword. `mcode-tools connector tools` → catalog of 16 tools, all `connector__matrix__*` / `connector__email_workbench_credentials__*`; keyword `shibui` → `{"tools":[],"partial":false,"provider_failures":[]}`; keyword `tradingview` → same. A direct `mcp__tradingview_advanced__screen_stocks` call returned **"Unknown tool_name"**. |
| Scanner coverage | 20,095 rows fetched vs 20,095 reported (`stock` 11,755 / `fund` 6,734 / `dr` 1,606) = **100.0%**, no duplicate ticker ids. |
| Session-date proof | Yahoo `regularMarketTime` = 2026-10-26 16:00 ET for SPY; last daily bar dated 2026-10-26 on all 5 index series. |
| Independent price cross-check | 48 sampled tickers, **46 agreed with Yahoo to the cent (100%)**, 0 mismatches, 2 no-data (class-share symbols with no Yahoo mapping). |
| Breadth cross-check | 40 sampled S&P 500 members, TV-SMA20 vs Yahoo-computed SMA20 above/below verdict: **40/40 agreement**. |
| Yahoo bar coverage of the prefiltered universe | **2,927 / 2,927** (100%) after alias-patching class shares (`BRK.B`→`BRK-B`, `ALL/PH`→`ALL-PH`). |
| Stale carry-over rows dropped | **13** — all SPAC shells / closed-end funds that did not trade today (AEAQ, CRAN, DSAC, GCGR, GHXI, GIW, HVMC, IACO, KFII, MESH, SAC, TJGC, TMTS). Each carried a 0.00–0.20% TV "change", the signature of a carried-over quote. **A `volume` floor does not catch these** — a shell can print volume on a thin day and still be days stale. |
| Yahoo access notes | Short `User-Agent: Mozilla/5.0` + `curl` only. The long Chrome UA and `urllib` are both 429'd by Yahoo's edge. |

### Universe funnel

| Stage | Rows |
|---|---|
| Scanner rows (all types, all exchanges) | 20,095 |
| `type = stock` | 11,755 |
| NYSE / NASDAQ / AMEX only (OTC and CBOE excluded) | 5,715 |
| Prefilter: close > $3, mcap > $300M, 30d avg vol > 100k | **2,927** |
| …with Yahoo daily bars available | 2,927 (100%) |
| …after dropping stale carry-over rows | 2,914 |

The prefilter is the skill's step-1 shibui gate, reproduced exactly. It is a genuinely small universe, and every screen below runs on all 2,927 names — not a sampled subset.

---

## Regime and breadth

| Metric | Value | Read |
|---|---|---|
| % S&P 500 above 20-DMA | **71.46%** (358 above / 143 below / 1 no data) | Broad participation. Not a distribution top. |
| Index vs 20-DMA | SPY 765.37 (below), RSP 217.29 (above), QQQ 712.20 (below), QQQE 118.06 (below), IWM 276.99 (below), DIA 522.97 (above) | Cap-weighted indices below their 20-DMA while equal-weight is above → mega-cap drag, not broad weakness. |
| VIX | **18.39, −5.45%** (from 19.45) | Volatility compressing into the close. |
| VIX/VXV ratio | **null** | `^VXV` and `^VXVCLS` both return 0 bars from Yahoo (`Not Found`). The ratio needs both legs; the uncertainty flag is left `null` rather than inferred from VIX alone. |
| ATR extension vs 252d median ATR% | SPY 0.93×, RSP 0.94×, QQQ 1.07×, QQQE 1.09×, IWM 0.82× | No index is anywhere near the 6× late-cycle threshold. |
| `size_cut_pct` | **0** | Rule is (index < 20-DMA) AND (breadth < 40%). Breadth is 71.5%, so the size cut does not trigger even though four indices sit below their 20-DMA. |
| `uncertainty` | **null** (VXV unavailable) | — |
| `late_cycle` | **false** | — |

Breadth says the average stock is in a healthy uptrend. Index structure says the market's weight is in a few names that are not. Those are different trades, and the screener's job is to tell you which one you are in.

### Sector relative strength (Hernandez theme → group)

| Rank | ETF | Sector | Perf 1M | Perf 3M | Perf 6M | Composite | > 20-DMA |
|---|---|---|---|---|---|---|---|
| 1 | XLE | Energy | +12.47% | +19.23% | +19.49% | **51.19** | yes |
| 2 | XLV | Healthcare | +5.50% | +8.01% | +26.02% | **39.53** | yes |
| 3 | XLK | Electronic Technology | −4.71% | +8.83% | +17.31% | **21.42** | no |
| 4 | XLP | Consumer Defensive | +8.05% | +1.02% | +6.28% | 15.35 | yes |
| 5 | XLF | Financial | +2.55% | −1.94% | +7.46% | 8.07 | yes |
| … | | | | | | | |
| 10 | XLI | Industrial | −1.52% | −8.58% | −2.51% | −12.60 | no |
| 11 | XLC | Communication Services | −8.47% | −4.14% | −10.12% | **−22.73** | no |

The composite (1M + 3M + 6M, equal weight) puts Energy, Healthcare and Technology on top, but Technology's top rank is carried entirely by the 3M/6M legs — its 1M is −4.7% and it closed below its 20-DMA. That is a recovering-but-not-leading sector, and it is the sector most of today's Focus names sit in.

---

## Screen results

| Screen | Stylist | Rows | Notes |
|---|---|---|---|
| 4% breakout | Stockbee / Bonde | 69 | `change ≥ 4%` **and** relative volume > 1.0 (the spec's "volume > prev volume" restated as volume expansion). |
| EP9 Million | Stockbee / Bonde | 158 | Volume ≥ 8.9M, close ≥ $3. |
| Anticipation (coil) | Stockbee / Bonde | 3 | KRT, MG, PRTH. Approximate — see deviation 7. |
| Multi-timeframe RS leaders | Qullamaggie | 33 | True ADR20 ≥ 4.5%, ADV$ ≥ 20M, stacked SMAs (50 > 150 > 200), price > 200-DMA. |
| EP (10%+ gap) | Qullamaggie | 2 | RRC (+11.6% gap), SGRY (+46.2% gap). |
| 5-day gainers (parabolic short) | Qullamaggie | **1** | NTSK only: +26.2% over 5 sessions, true ADR 6.09%, ADV$ 184M, but **94% above its 200-DMA** — stretched, not base-building. |
| 5-day losers (parabolic long) | Qullamaggie | **2** | CORT (−25.2%, 18.1% above 200-DMA — a genuine pullback-to-trend candidate) and XP (−49.9%, −18.4% vs 200-DMA — a broken name, not a dip). |
| CANSLIM | Jeff Sun | 357 | **Partial** — no sales-growth leg (deviation 2). |
| Theme → group → leaders | Ariel Hernandez | 30 | Top-3 sector ETFs' sectors, P/E > 0, EPS yoy growth > 0, ranked by 1M RS. |
| Compression (VCP) | Ariel Hernandez | 4 | CCC, IHS, PRTH, PTC. "Screen within a screen", run on the Master list: 10-day mean range ÷ 50-day mean range < 0.6 and price > 20-DMA. |
| ADR + $vol + velocity | Peoplewish | 200 | True ADR20 ≥ 5%, ADV$ ≥ 50M, sorted by true 14-day velocity. |

**On the near-empty screens:** the parabolic-short and parabolic-long lists are short because the gates are strict and today's tape does not satisfy them, not because the screens failed. The 200-row cap on peoplewish was hit — the full set of 200 is in `peoplewish_adr_velocity.csv`, and the screen's own gates (ADR ≥ 5% **and** ADV$ ≥ 50M) leave a large eligible pool.

**One methodology note that changes a headline number:** the ADR gates were first applied with an `ATR(14)/close` proxy, which would have produced a *larger* peoplewish list (272 rows). Every ADR gate in the published artifacts is applied to the **true 20-day ATR-style range** from Yahoo bars, per the spec's formula. The proxy was discarded, not reported.

### Top of the peoplewish velocity sort

| Ticker | 14d velocity | True ADR20 | ADV$ | Close | Day |
|---|---|---|---|---|---|
| LQDA | +68.8% | 15.96% | $240M | 43.74 | +2.56% |
| FIGS | +47.7% | 5.53% | $76M | 20.83 | +3.12% |
| BSP | +41.0% | 9.54% | $170M | 46.63 | +5.78% |
| DXC | +37.8% | 5.10% | $72M | 16.30 | +1.31% |
| ASAN | +29.3% | 5.71% | $82M | 12.01 | −0.08% |

---

## Focus list (12) and Tier-A (8)

**Focus** = ≥2 distinct stylists, or top-5 velocity, cap 12. **Tier-A** = Focus with ≥3 distinct stylists, cap 8.

| Ticker | Close | Day | True ADR20 | ADV$ | 14d vel | Stylists | Flags |
|---|---|---|---|---|---|---|---|
| P | 131.33 | +6.49% | 4.87% | $887M | −10.8% | 4 | ma_shrink |
| ORKA | 90.33 | +12.70% | 5.10% | $93M | +12.7% | 3 | — |
| TENB | 48.21 | +8.12% | 5.49% | $185M | +22.1% | 3 | — |
| NXPI | 245.83 | +4.64% | 3.20% | $864M | +0.6% | 3 | — |
| ADI | 407.93 | +4.31% | 2.91% | $1,347M | −3.0% | 3 | higher-low base |
| HEI | 309.71 | +4.15% | 2.46% | $146M | +2.1% | 3 | — |
| CSCO | 110.24 | +3.51% | 2.46% | $1,992M | −6.5% | 3 | ma_shrink |
| RNG | 86.31 | +3.50% | 5.40% | $149M | +11.7% | 3 | d2_nofollow |
| OKTA | 220.01 | +3.27% | 5.25% | $790M | +0.6% | 3 | — |
| FIGS | 20.83 | +3.12% | 5.53% | $76M | +47.7% | 3 | ma_shrink |
| SDGR | 24.50 | +2.94% | 7.47% | $70M | −15.2% | 3 | ma_shrink |
| PENG | 54.92 | +2.83% | 8.58% | $223M | −14.5% | 3 | ma_shrink |

**What the list actually says.** Seven of the eight Tier-A names are technology or semiconductor names (P, NXPI, ADI, HEI, CSCO, OKTA, TENB), and four of them have a **negative** 14-day velocity while gapping up today (P −10.8%, ADI −3.0%, CSCO −6.5%, PENG −14.5%). That is the signature of a *reversal bounce off a downtrend within a pullback*, not of momentum continuation — the stocks that were already trending up are not the ones converging. `RNG` carries `day2_no_follow` (day-2 close below day-1 midpoint) and is the one Tier-A name whose setup is already weakening.

**Flag meanings:** `ma_shrink` = 5-day range < 50% of 20-day range (coiling, watch for the break); `d2_nofollow` = day-2 close below day-1 midpoint (reconsider if you are holding from day 1); `atr_shrink` = ATR(14) < 60% of its 63-day median (too quiet); `wicky` = breakout candle with wick > body and close RVOL < 1.2 (abandon).

---

## Largest movers inside the Master list

| Ticker | Day | Close | Stylists | Note |
|---|---|---|---|---|
| SGRY | **+47.6%** | 23.25 | 2 | Also the EP-gap name: gapped +46.2%, RVOL 27.5. |
| SWRD | +21.6% | 3.04 | 1 | Sub-$4 name, barely above the $3 price floor. |
| RPD | +20.3% | 17.93 | 2 | 14d velocity +46.1%. |
| RRC | +17.7% | 53.56 | 2 | Gapped +11.6% at the open, RVOL 10.2. |
| XNCR | +15.9% | 29.18 | 2 | — |
| ORKA | +12.7% | 90.33 | 3 | Also Tier-A. |
| XP | **−48.4%** | 15.71 | 3 | Also the parabolic-long candidate: −49.9% over 5 sessions, −18.4% vs 200-DMA. |
| STNE | −27.4% | 8.33 | 2 | — |
| ASST | −9.1% | 26.32 | 2 | RS leader on the 3M leg (+128%) but −9.1% today and −12% on 1M. |

**The two names that deserve a trader's attention, not a screener's:** SGRY (+47.6% on a 27× relative volume) and XP (−48.4% in five sessions). Both are genuine single-name events, and both sit in the Master list alongside 192 names that merely satisfied a threshold.

---

## Files in this directory

| File | Contents |
|---|---|
| `daily-sweep.md` | This report. |
| `_summary.md` | Four-bullet digest for the pre-market brief. |
| `breadth.md`, `daily-screens/breadth/2026-10-26.md` | Breadth + regime detail. |
| `_regime-screener.json` | `size_cut_pct` / `uncertainty` / `late_cycle` payload from **this** sweep. **Not** named `_regime.json`: that path in this directory is owned by cron #10 (`stock-screener-breadth-snapshot`, written 18:08Z) and overwriting a sibling cron's artifact would destroy it. |
| `master.md` / `.csv` | Union of all screens, deduped, cap 200. |
| `stalk.md` / `.csv` | Master, within 2% of 10/20-DMA, with a setup tag (13). |
| `focus.md` / `.csv` | ≥2 stylists or top-5 velocity, cap 12. |
| `tier-a.md` / `.csv` | ≥3 stylists, cap 8. |
| `stockbee.md`, `qullamaggie.md`, `jeff-sun.md`, `ariel-hernandez.md`, `peoplewish.md` (+ `.csv`) | Per-stylist merged views. |
| `short-candidates.md`, `long-reversal-candidates.md` | Kullamägi parabolic short / long (the same rows as the two sub-screen files, in the skill's naming). |
| `<screen_name>.md` / `.csv` | One file per individual sub-screen (11 screens). |

**Not produced, by design:** `ipo.md`, `high-short-float.md` (Sunday-only), `reversal-bullish-3:55.{md,csv}` (15:30–16:00 ET only), `focus-rvol-snapshot.md` (09:45–11:15 ET only).

**Next step for the trader:** the 07:37 ET pre-market brief reads `_summary.md`; Tier-A + regime should be prepended there from `_regime-screener.json` (and cron #10's `_regime.json`, which covers the same ground from a different date — see the corroboration note below).

---

## Cross-cron corroboration (cron #10, written 18:08Z today)

Cron #10 (`stock-screener-breadth-snapshot`) had already written `daily-screens/2026-10-26/_regime.json` before this run. Comparing the two independent computations is a free check on this one:

| Metric | Cron #10 (data_date 2026-10-23) | This sweep (data_date 2026-10-26) | Verdict |
|---|---|---|---|
| Indices below 20-DMA | SPY, QQQ, QQQE, IWM | SPY, QQQ, QQQE, IWM | **Identical** |
| Max ATR% / median multiple | 1.09× | 1.09× | **Identical** |
| `size_cut_pct` | 0 | 0 | **Identical** |
| `late_cycle` | false | false | **Identical** |
| % S&P 500 above 20-DMA | 69.7% (on Friday's close) | 71.46% (on today's close) | Different by 1.8 pt — expected, different session |
| `uncertainty` | false, using `^VIX3M` as the long-end proxy (ratio 0.950) | null — `^VXV`/`^VXVCLS` return 0 bars | Cron #10's substitution is the more useful number, and it agrees with the `false` direction |

Two of this sweep's three regime flags are now confirmed by a second, independent pipeline, and the only genuine disagreement (the uncertainty leg) is a **missing-data** disagreement, not a contradictory one. Cron #10's VIX/VIX3M proxy of 0.95 is the defensible substitute if a boolean is required; this sweep leaves the field null because the spec's own leg is unavailable.

---

## Method notes (reproduction)

- **Yahoo access:** `curl` subprocess only, `User-Agent: Mozilla/5.0`, `query2` before `query1`. Yahoo 429s the long Chrome UA and `urllib` alike; quoting a symbol list needs `safe=","` or the comma is escaped and never reaches the API.
- **Scanner paging:** sort by `name` with a 1,500-row step against a 2,000-row page and dedupe by full ticker id. Sorting by `market_cap_basic` is unstable because that column is NULL for every ETF — the first attempt silently lost 117 stocks and every major index ETF (SPY/QQQ/IWM) and duplicated ~1,650 rows.
- **Stale-row filter:** a row is dropped unless its last Yahoo daily bar is dated 2026-10-26. TV `change` alone is not sufficient (13 shells carried 0.00% changes).
- **ATR extension:** computed as a median of the **ATR% series** over 252 bars, not an average of rolling ATRs of differing window length.
