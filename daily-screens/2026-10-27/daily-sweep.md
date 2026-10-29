# Daily Stock Screener Sweep — 2026-10-27 (US/Eastern)

**Session:** Tuesday 2026-10-27 close. **Cron:** #9 `stock-screener-daily-sweep-18:30` (fired 18:33 ET).
**Data path:** TradingView public scanner (tier-2 fallback) + Yahoo Finance daily bars. **Session lag: none** — every price here is the settled 2026-10-27 close, and the scanner agrees with Yahoo's official close to **0.0000% on 128 of 128 sampled tickers** (mean |gap| 0.0000 pp, max 0.0000 pp).

---

## ⚠ Deviations from the skill spec (read first)

| # | Spec says | What ran instead | Why | Impact |
|---|---|---|---|---|
| 1 | `mcp__shibui-finance__stock_data_query` (prefilter + 8-CTE sweep) | TradingView public scanner `POST /america/scan`, 20,053 rows | The whole MCP tier is **provably unbound** in this Cloud session (see QC). Discovery returned `partial=false` with an empty catalog, so this is disconnection, not a partial catalog. | Every shibui SQL screen was re-expressed in scanner columns. |
| 2 | `mcp__tradingview__screen_stocks` / `screen_etf` / `volume_breakout_scanner` | Same scanner, different column sets | Same root cause. | Jeff Sun's CANSLIM screen lost its **sales-growth leg** (`sales_growth_quarterly_yoy` is null on this source) — that sub-screen is **partial**, and is labelled as such everywhere it appears. |
| 3 | `mcp__tradingview-advanced__yahoo_price` for VIX/VXV | Yahoo chart API directly | Same root cause. | VIX leg computed. **VXV leg unavailable** (see Regime). |
| 4 | `financekit sector_rotation` | Sector-ETF relative strength from scanner `Perf.1M/3M/6M` | Same root cause. | Theme ranking is ETF-based, not the financekit rotation table. |
| 5 | Finviz fallback (tier 3) | Not reached | The tier-2 fallback succeeded, so the chain stopped there. | Finviz's HTTP 403 behaviour was not re-tested this run. |
| 6 | `ADR = AVG((high-low)/close, 20)` computed in SQL | Same formula, computed from Yahoo daily bars | No bar-level SQL available. | **Not a proxy** — true ADR, same definition. |
| 7 | Anticipation (coil) uses `avg(close,7)/avg(close,65)` and a 10-day base | `close/SMA50` and the 1-month range | The scanner exposes no 7/65-day averages. | Coil screen is a **coarser approximation**; 3 names qualified. |
| 8 | Hernandez step 3 = `yahoo-finance get_financial_statements` per candidate | Scanner `price_earnings_ttm` + `earnings_per_share_diluted_yoy_growth_ttm` | Avoids 30 extra single-ticker calls. | Fundamentals overlay is thinner than the spec's. |
| 9 | 3:55 PM reversal-bullish scan (Bonde, 8 criteria) | **Not run by this cron** | The cron fired at 18:33 ET; that screen is only valid 15:30–16:00 ET. | Cron #4 owns `reversal-bullish-3:55.{md,csv}` in this directory — it was written today on a different (Nasdaq) path, flagged `degraded=true` there. |
| 10 | IPO + high-short-float weekly refresh | **Not run** | Sunday-only screens; today is Tuesday. | No `ipo.md` / `high-short-float.md`. |
| 11 | Pre-market gapper (09:00 ET) and live RVOL re-rank (09:45–11:15 ET) | **Not run by this cron** | Outside this cron's window. | Cron #8 / cron #7 own those files in this directory. |

**Fallback chain terminated at tier 2, as the zero-fallback policy requires.** No MCP call was retried, and no deeper tier was chained. One fallback was counted for the whole run.

---

## Headline

A **one-day violent reversal of yesterday's leadership**, with the screener's high-conviction screens almost empty. Energy — yesterday's clear composite leader at +12.5% over a month — fell **2.05%**, while Technology ripped **+1.70%** and the Nasdaq-100 added **+1.27%** (SPY +0.56%, RSP only +0.11%, so this was mega-cap-led). **447 of 2,936 live names closed up ≥4%** and 64 closed up ≥10% — the 4%-breakout screen went from 69 rows yesterday to **219** today.

**The caveat that most changes how to read this:** the Focus list is a **bounce off a drawdown, not momentum continuation**. Nine of the twelve Focus names have a **negative 14-day velocity** while gapping up today (MXL −30.4%, ALAB −25.0%, OUST −21.3%, GLXY −19.7%, LUNR −19.8%, RKLB −18.9%, RDW −13.2%, ON −4.7%, SDGR −2.1%). Meanwhile the Stalk list — the names sitting *ready to go* at a 10/20-DMA — is only **9** and is dominated by mega-caps that never sold off (AVGO, NVDA, AMZN, UI). The two lists are disjoint: today's momentum is a V-shaped snapback, and the setups that are actually loaded are the ones that never dipped.

---

## Data path and QC

| Check | Result |
|---|---|
| MCP tier availability | `tool_search` → 0 hits for `shibui` / `tradingview` / `stock` / `finance`. `mcode-tools connector tools` → `partial=false`, `provider_failures=[]`, 15 tools, all `connector__matrix__*` and `connector__email_workbench_credentials__*`. `partial=false` is the decisive detail: discovery was complete, so the empty result proves disconnection rather than a partial catalog. |
| Scanner coverage | **20,053 / 20,053 rows = 100.000%** (`stock` 11,712 / `fund` 6,734 / `dr` 1,607), zero duplicate ticker ids. Sorted by `name` with a 1,500-row step over 2,000-row pages — sorting by `market_cap_basic` is unstable because that column is NULL for every ETF. |
| Session-date proof | Yahoo last daily bar dated 2026-10-27 on all 5 regime indices; `regularMarketTime` on SPY = the 16:00 ET settle. |
| Independent price cross-check | **128 sampled tickers, 128 agreed with Yahoo to the cent (100.0%)**; mean \|gap\| 0.0000 pp, median 0.0000 pp, max 0.0000 pp, 0 rows off by >0.1%. The scanner's ~900s delayed stream has fully settled by 18:40 ET — the 0.43% mean gap measured on this same feed at 16:0x ET is **not** present at this read time. |
| Breadth cross-check | 40 sampled S&P 500 members, TV-SMA20 vs Yahoo-computed SMA20 above/below verdict: **40/40 agreement**. |
| Yahoo bar coverage of the prefiltered universe | **2,949 / 2,949 (100%)** after alias-patching class shares and preferreds (`BRK.B`→`BRK-B`, `BAC/PB`→`BAC-PB`; two general rules cover the rest). 63 names failed on the first pass and all 63 were recovered on the alias retry. |
| Stale carry-over rows dropped | **13** — SPAC shells / closed-end funds that did not trade on 2026-10-27: ACAA, AEAQ, DMII, GHXI, GSRV, HACQ, IEAG, ILLU, MEVO, PMTR, TJGC, TLNC, TMTS. Nine of them carried a TV `change` of 0.00–0.10%; **a `volume` floor does not catch these** — several printed 200k–1.2M shares on their last live session. |
| Yahoo access notes | Short `User-Agent: Mozilla/5.0` + `curl` only. The long Chrome UA and `urllib` are both 429'd by Yahoo's edge. |

### Universe funnel

| Stage | Rows |
|---|---|
| Scanner rows (all types, all exchanges) | 20,053 |
| `type = stock` | 11,712 |
| NYSE / NASDAQ / AMEX only (OTC 5,996 and CBOE 1 excluded) | 5,715 |
| Prefilter: close > $3, mcap > $300M, 30d avg vol > 100k | **2,949** |
| …with Yahoo daily bars available | 2,949 (100%) |
| …after dropping stale carry-over rows | **2,936 (live)** |

The prefilter is the skill's step-1 shibui gate, reproduced exactly. Every screen below runs on all 2,936 live names — not a sampled subset.

### Session tape

| Measure | Value |
|---|---|
| Live universe advance / decline / flat | **1,764 / 1,144 / 28** (60.1% up) |
| Names up ≥4% / ≥10% / ≥20% | **447 / 64 / 7** |
| Names down ≤−4% / ≤−10% | 80 / 7 |
| Sector of the ≥4% cohort | Electronic Technology 102, Health Technology 98, Non-Energy Minerals 56, Technology Services 52, Producer Manufacturing 41, Finance 22 |

---

## Regime and breadth

| Metric | Value | Read |
|---|---|---|
| % S&P 500 above 20-DMA | **73.05%** (366 above / 135 below / 1 no data, 502 constituents) | Broad participation, and improving from 71.46% yesterday. |
| Index vs 20-DMA (settled) | SPY 769.66 (+0.56%, **below**), RSP 217.52 (+0.11%, above), QQQ 721.25 (+1.27%, **below**), QQQE 119.31 (+1.06%, **below**), IWM 280.18 (+1.15%, above), DIA 523.28 (+0.06%, above) | 3 of 5 index ETFs below their 20-DMA — one fewer than yesterday. IWM crossed back above. The cap-weighted leg is still the weak one (SPY 0.10% below its 20-DMA). |
| VIX | **17.52, −4.73%** (from 18.39) | Volatility compressing hard into the close; a rally on falling vol. |
| VIX/VXV ratio | **null** | `^VXV` and `^VXVCLS` both return 0 bars from Yahoo (`Not Found`). The ratio needs both legs; the uncertainty flag is left `null` rather than inferred from VIX alone. Cron #10's `^VIX3M` substitution (ratio 0.906 intraday) gives `uncertainty=false` and is the more useful number — see corroboration below. |
| ATR extension vs 252d median ATR% | SPY 0.92×, RSP 0.91×, QQQ 1.07×, QQQE 1.06×, IWM 0.80× | No index is anywhere near the 6× late-cycle threshold. |
| `size_cut_pct` | **0** | Rule is (index < 20-DMA) AND (breadth < 40%). Breadth is 73.05%, so the size cut does not trigger even though SPY, QQQ and QQQE sit below their 20-DMA. |
| `uncertainty` | **null** (VXV unavailable) | — |
| `late_cycle` | **false** | — |

### Sector relative strength (Hernandez theme → group)

| Rank | ETF | Sector | Perf 1M | Perf 3M | Perf 6M | Composite | Day | > 20-DMA |
|---|---|---|---|---|---|---|---|---|
| 1 | XLE | Energy | +10.16% | +15.45% | +17.20% | **42.81** | **−2.05%** | yes |
| 2 | XLV | Healthcare | +5.44% | +7.20% | +24.71% | **37.34** | −0.06% | yes |
| 3 | XLK | Electronic Technology | −3.09% | +10.74% | +18.69% | **26.34** | **+1.70%** | no |
| 4 | XLP | Consumer Defensive | +7.05% | +0.94% | +4.63% | 12.62 | −0.92% | yes |
| 5 | XLF | Financial | +2.30% | −2.46% | +8.48% | 8.32 | −0.25% | yes |
| … | | | | | | | | |
| 10 | XLI | Industrial | −0.95% | −7.23% | −2.08% | −10.26 | +0.57% | no |
| 11 | XLC | Communication Services | −8.71% | −5.42% | −9.93% | **−24.06** | −0.26% | no |

The composite table is unchanged in shape from yesterday — Energy, Healthcare, Technology — but the **day** column inverts the top of it: Energy fell 2.05% while Technology rose 1.70%. The third-ranked theme (Technology) is a recovering-but-not-leading sector: its 1M is still −3.1% and it closed below its 20-DMA. That is where seven of today's twelve Focus names sit.

---

## Screen results

| Screen | Stylist | Rows | Notes |
|---|---|---|---|
| 4% breakout | Stockbee / Bonde | **219** | `change ≥ 4%` **and** relative volume > 1.0 (the spec's "volume > prev volume" restated as volume expansion). Up from 69 yesterday — a 3.2× expansion. |
| EP9 Million | Stockbee / Bonde | 178 | Volume ≥ 8.9M, close ≥ $3. |
| Anticipation (coil) | Stockbee / Bonde | 3 | KRT, MGRC, PRTH. Approximate — see deviation 7. |
| Multi-timeframe RS leaders | Qullamaggie | 37 | True ADR20 ≥ 4.5%, ADV$ ≥ 20M, stacked SMAs (50 > 150 > 200), price > 200-DMA. |
| EP (10%+ gap) | Qullamaggie | **0** | Funnel: 10 names gapped ≥10% → 2 cleared RVOL ≥ 10 (BRAI 64.2×, MFIC 15.1×) → **0** cleared ADV$ ≥ 50M. The two gappers are $6M and $8M dollar-volume names. |
| 5-day gainers (parabolic short) | Qullamaggie | **1** | CRML: +27.2% over 5 sessions, true ADR 7.20%, ADV$ 74M, 13.5% **below** its 200-DMA. |
| 5-day losers (parabolic long) | Qullamaggie | **1** | XP: −46.6% over 5 sessions, −17.1% vs 200-DMA, ADV$ 262M. |
| CANSLIM | Jeff Sun | 361 | **Partial** — no sales-growth leg (deviation 2). |
| Theme → group → leaders | Ariel Hernandez | 30 | Top-3 sector ETFs' sectors, P/E > 0, EPS yoy growth > 0, ranked by 1M RS. |
| Compression (VCP) | Ariel Hernandez | 4 | CCC, PRTH, PTC, RXO. "Screen within a screen", run on the Master list. |
| ADR + $vol + velocity | Peoplewish | 214 | True ADR20 ≥ 5%, ADV$ ≥ 50M, sorted by true 14-day velocity. |

**On the near-empty screens:** the EP-gap and parabolic screens are short because the gates are strict and today's tape does not satisfy them, not because the screens failed. The EP funnel above is the proof — the two names that gapped hard did so on a dollar volume an institution cannot trade, which is exactly what the $50M floor is designed to exclude.

**The ADR gates are applied to true 20-day ATR-style range from Yahoo bars**, per the spec's formula. An `ATR(14)/close` proxy was used only for a first-pass universe scan and was discarded, not reported.

### Top of the peoplewish velocity sort

| Ticker | 14d velocity | True ADR20 | ADV$ | Close | Day |
|---|---|---|---|---|---|
| LQDA | +70.3% | 15.94% | $252M | 45.44 | +3.89% |
| TRAX | +48.3% | 8.70% | $50M | 45.38 | +4.37% |
| FIGS | +45.7% | 5.54% | $75M | 20.48 | −1.68% |
| NTSK | +35.9% | 6.11% | $189M | 26.15 | +3.73% |
| DXC | +31.8% | 5.11% | $70M | 15.84 | −2.82% |

---

## Focus list (12) and Tier-A (8)

**Focus** = ≥2 distinct stylists, or top-5 velocity, cap 12. **Tier-A** = Focus with ≥3 distinct stylists, cap 8.

| Ticker | Close | Day | True ADR20 | ADV$ | 14d vel | Stylists | Flags |
|---|---|---|---|---|---|---|---|
| CRML | 8.13 | +27.43% | 7.20% | $74M | **+15.2%** | 3 | gap-up ready |
| HRI | 156.06 | +22.76% | 5.89% | $136M | **+25.4%** | 3 | gap-up ready |
| MXL | 74.67 | +12.34% | 8.61% | $265M | −30.4% | 3 | ma_shrink |
| CYPH | 3.13 | +10.78% | 12.19% | $50M | +2.8% | 3 | — |
| ALAB | 286.69 | +10.47% | 6.72% | $1,179M | −25.0% | 3 | ma_shrink |
| OUST | 32.79 | +10.37% | 6.65% | $85M | −21.3% | 3 | ma_shrink |
| LUNR | 11.56 | +10.31% | 6.76% | $92M | −19.8% | 3 | ma_shrink |
| GLXY | 17.18 | +9.57% | 7.48% | $109M | −19.7% | 3 | ma_shrink |
| SDGR | 26.72 | +9.06% | 7.73% | $75M | −2.1% | 3 | ma_shrink |
| RKLB | 58.31 | +8.34% | 5.74% | $1,243M | −18.9% | 3 | ma_shrink |
| RDW | 8.89 | +6.85% | 6.15% | $117M | −13.2% | 3 | ma_shrink |
| ON | 78.67 | +6.22% | 4.04% | $886M | −4.7% | 3 | ma_shrink |

**What the list actually says.** Seven of the twelve are the same complex — semis, optical/networking and space (MXL, ALAB, OUST, LUNR, RKLB, RDW, ON) — and **nine of the twelve have a negative 14-day velocity**. That is the signature of a *reversal bounce inside a downtrend*, not momentum continuation: the stocks that were already trending up are not the ones converging. Only CRML (Critical Metals) and HRI (Herc Holdings) have positive 14-day velocity, and both carry the `gap-up ready` tag.

**Convergence caps bind hard today.** The union of all screens is **787 names**; 196 carry ≥2 stylists and **35 carry the maximum 3 stylists**. Tier-A's 8 slots are therefore chosen from 35 equally-converged names (ties broken by convergence, then day move), and Focus's 12 slots go to the 3-stylist names first. A side effect worth stating: the Focus rule's **top-5 velocity clause contributes only HRI**, because FIGS (+45.7% 14d), NTSK (+35.9%), ENVX (+31.4%) and BHVN (+28.7%) each carry a single stylist flag and lose the cap cut. Four of the five fastest names in the market are in Master but not in Focus.

**Flag meanings:** `ma_shrink` = 5-day range < 50% of 20-day range (coiling, watch for the break); `gap-up ready` = gap > 4% **and** RVOL > 2; `atr_shrink` = ATR(14) < 60% of its 63-day median (too quiet); `wicky` = breakout candle with wick > body and close RVOL < 1.2 (abandon).

---

## Largest movers inside the Master list

| Ticker | Day | Close | Stylists | Note |
|---|---|---|---|---|
| BRAI | **+56.13%** | 3.31 | 1 | Braiin Ltd (NASDAQ), rvol **64.2×**, ADR20 19.2%, ADV$ 6M. Gapped +52.4% and closed $3.31 — still **below** its $3.55 close of two sessions earlier, after a −37% day on 10-26. A whipsaw, not a breakout. |
| CRML | **+27.43%** | 8.13 | 3 | Critical Metals Corp. Also the parabolic-short candidate and a Focus/Tier-A name. |
| ENVX | +25.00% | 3.35 | 1 | Enovix, +31.4% over 14 sessions, rvol 1.68. |
| HRI | **+22.76%** | 156.06 | 3 | Herc Holdings. Also Tier-A, and the one Focus name with a positive 14-day velocity above +25%. |
| MFIC | +22.73% | 10.26 | 1 | MidCap Financial Investment (BDC), rvol 15.1×, ADV$ 8M — the only other ≥10% RVOL gapper, and equally untradeable at size. |
| KNSA | +22.23% | 89.20 | 1 | Kiniksa Pharmaceuticals, $7.0B cap. |
| PRME | +20.50% | 4.35 | 1 | Prime Medicine. |
| ZURA | +19.94% | 4.27 | 1 | Zura Bio — rvol 0.71, i.e. a low-volume drift, not a volume event. |
| CHRN | +19.55% | 17.49 | 1 | ChronoScale Holdings, ADV$ 2M. |
| NB | +17.59% | 3.41 | 1 | NioCorp, ADV$ 9M. |
| USAR | +16.72% | 10.40 | 1 | USA Rare Earth, ADV$ 142M — the one large-cap member of the critical-minerals cohort. |
| XP | +1.62% | 15.96 | 3 | Also the parabolic-long candidate: **−46.6% over 5 sessions**, −17.1% vs 200-DMA, ADV$ 262M. |

**The two names that deserve a trader's attention, not a screener's:** BRAI (+56% on 64× relative volume) and XP (−46.6% in five sessions). Both are genuine single-name events sitting in a Master list of 200 threshold-satisfiers — and BRAI's is a bounce off a −37% collapse that still leaves the stock below its two-day-ago level.

---

## Files in this directory

| File | Contents |
|---|---|
| `daily-sweep.md` | This report. |
| `_summary.md` | Four-bullet digest for the pre-market brief. |
| `breadth.md`, `daily-screens/breadth/2026-10-27.md` | Breadth + regime detail. |
| `_regime-screener.json` | `size_cut_pct` / `uncertainty` / `late_cycle` payload from **this** sweep. **Not** named `_regime.json`: that path in this directory is owned by cron #10 (`stock-screener-breadth-snapshot`, written 18:35Z) and overwriting a sibling cron's artifact would destroy it. |
| `master.md` / `.csv` | Union of all screens, deduped, cap 200. |
| `stalk.md` / `.csv` | Master, within 2% of 10/20-DMA, with a setup tag (9). |
| `focus.md` / `.csv` | ≥2 stylists or top-5 velocity, cap 12. |
| `tier-a.md` / `.csv` | ≥3 stylists, cap 8. |
| `stockbee.md`, `qullamaggie.md`, `jeff-sun.md`, `ariel-hernandez.md`, `peoplewish.md` (+ `.csv`) | Per-stylist merged views. |
| `short-candidates.md`, `long-reversal-candidates.md` | Kullamägi parabolic short / long (the same rows as the two sub-screen files, in the skill's naming). |
| `<screen_name>.md` / `.csv` | One file per individual sub-screen (11 screens). |

**Not produced by this cron, by design:** `ipo.md`, `high-short-float.md` (Sunday-only), `reversal-bullish-3:55.{md,csv}` (15:30–16:00 ET only — cron #4 owns it), `focus-rvol-snapshot.md` (09:45–11:15 ET only — cron #7 owns it), `pre-market-gapper.{md,csv}` (09:00 ET only — cron #8 owns it).

**Next step for the trader:** the 07:37 ET pre-market brief reads `_summary.md`; Tier-A + regime should be prepended there from `_regime-screener.json` (and cron #10's `_regime.json`, which covers the same ground from a different date — see the corroboration note below).

---

## Cross-cron corroboration (cron #10, written 18:35Z today)

Cron #10 (`stock-screener-breadth-snapshot`) had already written `daily-screens/2026-10-27/_regime.json` before this run, from a different data path (Nasdaq public chart API, Yahoo throttled). Comparing the two independent computations is a free check on this one:

| Metric | Cron #10 | This sweep | Verdict |
|---|---|---|---|
| SPY move | +0.53% (live 14:35 ET) | **+0.56%** (settled) | Consistent — the settle landed where the 14:35 print was |
| RSP move | −0.05% (live) | **+0.11%** (settled) | Consistent (RSP rallied into the close) |
| QQQ move | +1.19% (live) | **+1.27%** (settled) | Consistent |
| IWM move | +1.06% (live) | **+1.15%** (settled) | Consistent |
| Index ETFs below 20-DMA | 3 of 5 (SPY, QQQ, QQQE) | **3 of 5 (SPY, QQQ, QQQE)** | **Identical** |
| VIX | 17.77 (live) / 18.39 (10-26 settle) | **17.52** (settled) | Consistent |
| % S&P 500 above 20-DMA | 72.7% (intraday) | **73.05%** (settled) | Consistent |
| `size_cut_pct` / `late_cycle` | 0 / false | 0 / false | **Identical** |
| `uncertainty` | false, using `^VIX3M` (ratio 0.906 intraday) | null — `^VXV` returns 0 bars | Cron #10's substitution is the more useful number, and it agrees with the `false` direction |

Two independent pipelines, two different price sources, agreeing on the shape of the session. The only disagreement is a **missing-data** disagreement (the VXV leg), not a contradictory one. Cron #10's VIX/VIX3M proxy of 0.906 is the defensible substitute if a boolean is required; this sweep leaves the field null because the spec's own leg is unavailable.

---

## Method notes (reproduction)

- **Yahoo access:** `curl` subprocess only, `User-Agent: Mozilla/5.0`, `query2` before `query1`. Yahoo 429s the long Chrome UA and `urllib` alike; quoting a symbol list needs `safe=","` or the comma is escaped and never reaches the API.
- **Scanner paging:** sort by `name` with a 1,500-row step against a 2,000-row page and dedupe by full ticker id. Sorting by `market_cap_basic` is unstable because that column is NULL for every ETF — an earlier attempt silently lost 117 stocks and every major index ETF.
- **Symbol aliases:** TradingView writes `BRK.B` and `BAC/PB`; Yahoo's chart endpoint only accepts `BRK-B` and `BAC-PB`. Two general rules (preferred `X/PY`→`X-PY`, class share `X.Y`→`X-Y`) recovered all 63 names that failed on the first pass, taking universe bar coverage to 100%.
- **Stale-row filter:** a row is dropped unless its last Yahoo daily bar is dated 2026-10-27. TV `change` alone is not sufficient (9 of the 13 shells carried 0.00–0.10% changes).
- **ATR extension:** computed as a median of the **ATR% series** over 252 bars, not an average of rolling ATRs of differing window length.
- **Tiering reads the enriched universe.** The derived fields (`adr20`, `atr_shrink`, `ma_shrink`, `contraction`) are computed onto the full prefiltered universe before the tier cut, so no skip-rule flag is silently blank in master/stalk/focus/tier-a.
