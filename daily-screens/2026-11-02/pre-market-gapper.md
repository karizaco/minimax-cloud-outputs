# Pre-Market Gapper — 2026-11-02 (US/Eastern)

**Session:** Monday 2026-11-02 pre-market. **Cron:** #8 `stock-screener-pre-market-gapper` (scheduled 08:30 ET; snapshots at 08:46, 08:52, 08:57 and a paired 09:00 ET pull).
**Focus-list source:** `daily-screens/2026-10-30/focus.md` — the most recent completed 18:30 ET sweep (Friday 2026-10-30; 12 names). **Reference close:** settled 2026-10-30 regular-session close, taken from that sweep's own `focus.csv` and confirmed to the cent by the TradingView scanner's `close` on 12/12 names.
**Data source:** Nasdaq public quote API (`/info` + `/extended-trading?markettype=pre`) per ticker, cross-checked against the TradingView america scanner. `_source=nasdaq_public_api`.

## Result

**0 of 12 Focus names flagged.** No Focus ticker satisfied both conditions (gap > 4% AND pre-market volume > 50,000 shares) at the final snapshot. This is a clean no-setup session, not a data failure — every name returned a live quote and a pre-market tape, and the two independent sources agree on every name to within 1.24pp.

The screen is a **price filter first and a liquidity filter second**, and this session failed on price. Only two Focus names even approached the 4% gap trigger, and neither cleared it: **DFIN** briefly printed $70.00 (+4.65%) on a *single share* at 07:00 ET before fading to $66.95 by the final snapshot, and **FTAI** traded up +2.37% ($191.71) on 2,615 shares of pre-market volume — the largest live upside gap in the list, at barely half the trigger. The one name with genuine pre-market liquidity — **PURR**, 524,772 shares — is trading *down* -1.02%.

**No conclusion in this report is sensitive to the data-quality issues documented below.** The widest gap observed on *any* source at *any* snapshot was **2.37%** against a 4% trigger, so even a source disagreement of more than 1pp cannot flip a flag. The two names with a live gap above 1% (FTAI +2.37%, CVNA +1.38%) both sit far below the bar, and the only name with real liquidity (PURR) is on the wrong side of zero.

### Volume cleared, gap did not

- **PURR** -1.02% on 524,772 shares of pre-market volume — the only Focus name trading like a market this morning, and it is trading down. gave back the prior day's +23% on the Druckenmiller/Hyperliquid backing; 28.4M shares, IV30 112%

## Full Focus scan (all 12)

| Ticker | Prior close (2026-10-30) | PM last | Gap % | PM volume | PM high | PM low | PM timestamp | Last tape print | Flag |
|---|---|---|---|---|---|---|---|---|---|
| FTAI | 187.27 | $191.71 | +2.37% | 2,615 | $191.4142 | $191 | 08:47:27 | 08:47:27 (3 sh) | — |
| CVNA | 68.29 | $69.23 | +1.38% | 26,144 | $69.5 | $68.21 | 08:47:11 | 08:47:11 (1 sh) | — |
| PURR | 11.01 | $10.90 | -1.02% | 524,772 | $11.14 | $10.66 | 08:46:04 | 08:46:04 (1,000 sh) | — |
| CROX | 150.52 | $152.00 | +0.98% | 2,423 | $152 | $150.655 | 08:47:40 | 08:47:40 (1 sh) | — |
| GKOS | 237.60 | $236.00 | -0.67% | 2,294 | $242 | $237.43 | 08:45:01 | 08:45:01 (1 sh) | — |
| PRCH | 20.56 | $20.45 | -0.54% | 24,542 | $20.605 | $20.1746 | 08:43:23 | 08:43:23 (1 sh) | — |
| BHC | 8.20 | $8.23 | +0.35% | 3,875 | $8.245 | $7.84 | 08:42:41 | 08:42:41 (1 sh) | — |
| INSM | 112.58 | $112.90 | +0.28% | 6,502 | $114.3 | $112.01 | 08:47:03 | 08:47:03 (250 sh) | — |
| GEN | 29.13 | $29.09 | -0.14% | 16,590 | $29.1 | $28.5228 | 08:44:31 | 08:44:31 (1 sh) | — |
| ADT | 9.86 | $9.87 | +0.10% | 6,726 | $9.87 | $9.85 | 08:38:58 | 08:38:58 (1 sh) | — |
| DFIN | 66.89 | $66.95 | +0.09% | 101 | — | — | 08:40:38 | 08:40:38 (5 sh) | — |
| MAX | 14.75 | $14.75 | +0.00% | 1,198 | $14.75 | $14.4 | 08:24:10 | 08:24:10 (113 sh) | — |

Sorted by absolute gap, largest first. Every `Prior close` is the 2026-10-30 sweep's own `focus.csv` close, independently confirmed to the cent by the TradingView scanner on 12/12 names, so the gap is measured against the settled prior regular session with no reference-price lag.

## Flags by test

| Ticker | Gap | PM vol | Gap > 4% | Vol > 50k | Flagged | Note |
|---|---|---|---|---|---|---|
| FTAI | +2.37% | 2,615 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| CVNA | +1.38% | 26,144 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| PURR | -1.02% | 524,772 | no | yes | no | pm_vol>50k but abs(gap)<=4 |
| CROX | +0.98% | 2,423 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| GKOS | -0.67% | 2,294 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| PRCH | -0.54% | 24,542 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| BHC | +0.35% | 3,875 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| INSM | +0.28% | 6,502 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| GEN | -0.14% | 16,590 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| ADT | +0.10% | 6,726 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| DFIN | +0.09% | 101 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| MAX | +0.00% | 1,198 | no | no | no | abs(gap)<=4 and pm_vol<=50k |

## Snapshot trend (liveness confirmation)

Four snapshots confirm the quotes were live rather than stale. The final column is the paired Nasdaq + TradingView pull taken back-to-back, so the two sources are compared at the same instant.

| Ticker | 08:46 gap | 08:52 gap | 08:57 gap | 09:00 gap | 08:46 vol | 08:52 vol | 08:57 vol | 09:00 vol |
|---|---|---|---|---|---|---|---|---|
| FTAI | -0.01% | +1.54% | +2.44% | +2.37% | 2,602 | 2,607 | 2,615 | 2,615 |
| CVNA | +0.29% | +0.29% | +0.83% | +1.38% | 19,871 | 19,929 | 25,385 | 26,144 |
| PURR | -2.41% | -2.81% | -0.73% | -1.02% | 517,568 | 520,347 | 522,533 | 524,772 |
| CROX | +0.42% | +0.62% | +0.98% | +0.98% | 2,288 | 2,300 | 2,423 | 2,423 |
| GKOS | +0.00% | +0.00% | +0.59% | -0.67% | 1,723 | 1,724 | 2,294 | 2,294 |
| PRCH | -0.44% | +1.99% | +0.44% | -0.54% | 24,541 | 24,541 | 24,541 | 24,542 |
| BHC | +0.35% | +0.35% | +0.43% | +0.35% | 3,725 | 3,725 | 3,875 | 3,875 |
| INSM | +0.37% | +0.37% | +0.37% | +0.28% | 6,178 | 6,230 | 6,302 | 6,502 |
| GEN | -0.79% | -0.45% | -0.62% | -0.14% | 16,588 | 16,588 | 16,589 | 16,590 |
| ADT | +0.00% | +0.00% | +0.10% | +0.10% | 6,500 | 6,500 | 6,500 | 606,500 ⚠ |
| DFIN | +0.04% | +0.04% | +0.09% | +0.09% | — | — | — | — |
| MAX | +0.00% | +0.00% | +0.00% | +0.00% | 1,198 | 1,198 | 1,198 | 1,198 |

⚠ ADT's 09:00 Nasdaq counter (606,500) is the faulty value described in the data-quality section — its complete 71-print tape sums to 6,726 shares and TradingView independently read 5,913, so the headline figure uses 6,726.

## Source cross-check (Nasdaq vs TradingView, paired at 09:00 ET)

| Ticker | Nasdaq PM last | Nasdaq gap | TradingView PM last | TradingView gap | Divergence |
|---|---|---|---|---|---|
| FTAI | $191.71 | +2.37% | $191.41 | +2.21% | 0.16 pp |
| CVNA | $69.23 | +1.38% | $69.15 | +1.26% | 0.12 pp |
| PURR | $10.90 | -1.02% | $10.85 | -1.45% | 0.43 pp |
| CROX | $152.00 | +0.98% | $151.50 | +0.65% | 0.33 pp |
| GKOS | $236.00 | -0.67% | $238.94 | +0.57% | 1.24 pp |
| PRCH | $20.45 | -0.54% | $20.57 | +0.05% | 0.58 pp |
| BHC | $8.23 | +0.35% | $8.23 | +0.43% | 0.07 pp |
| INSM | $112.90 | +0.28% | $112.90 | +0.28% | 0.00 pp |
| GEN | $29.09 | -0.14% | $29.09 | -0.14% | 0.00 pp |
| ADT | $9.87 | +0.10% | $9.87 | +0.10% | 0.00 pp |
| DFIN | $66.95 | +0.09% | — | — | n/a |
| MAX | $14.75 | +0.00% | $14.74 | -0.07% | 0.07 pp |

Divergence is under 0.6pp on 10 of 12 names. The outlier is **GKOS at 1.24pp** (GKOS read $236.00 on the tape while TradingView carried $238.94) — both figures are far inside the 4% trigger, so the disagreement changes nothing. TradingView publishes no pre-market print for DFIN, whose tape is too thin for the scanner to carry a consolidated value; that is consistent with Nasdaq publishing no consolidated row for it either.

## Deviations from the skill spec (read first)

| # | Spec says | What ran instead | Why | Impact |
|---|---|---|---|---|
| 1 | `mcp__tradingview-advanced__stock_extended_hours(ticker)` per ticker (≤ 12 calls) | Nasdaq public quote API, 2 HTTP calls per ticker per snapshot, plus the TradingView america scanner as an independent second source | The entire `mcp__*` tier is **unbound in this Cloud session** — `mcp__tradingview__*`, `mcp__tradingview-advanced__*` and `mcp__shibui-finance__*` are not registered. The catalog probe returns `catalog_ok total=133 finance_tools=0`, and the published MCP bridge (`mcp_bridge.py`) exposes only `tradier`, `fmp` and `market-recap` — no tradingview server. | Primary source unavailable. |
| 2 | Tier-2 fallback `finviz_premarket_gap_url(tickers)` → one `web_fetch` | Not attempted; the Nasdaq API and the TradingView scanner both returned complete data, and the zero-fallback policy stops at the first tier that returns real data | Finviz bot-blocks this sandbox's IP (403 Cloudflare, confirmed 2026-10-27 and 2026-10-28) | Tier 2 known-unusable; not needed. |
| 3 | Flag `gap_pct > 4` AND `pre_market_volume > 50_000` | Same thresholds and semantics | — | None. |
| 4 | Run at 09:00 ET | Cron fired 08:30 ET; snapshots at 08:46, 08:52, 08:57 and a paired 09:00 ET pull | The deployed cron schedule is `30 8 * * 1-5` (08:30 ET weekdays) | The final snapshots land inside the spec's intended window, so the figures are directly comparable to a 09:00 ET run. |
| 5 | Reference price = prior session close | The **2026-10-30 sweep's own `focus.csv` close**, cross-checked against TradingView's `close` | Nasdaq's `/info` `secondaryData` drifted intraday on PRCH (read 20.68 against the true 20.56) and on 3/12 names in the earlier snapshots, while the sweep close and TradingView agree with each other on 12/12 | A more reliable denominator; the drift is documented below. |
| 6 | "One chat line per flagged name" | No chat lines emitted (0 flags) | Cron spec: quiet if no flags | — |

**Fallback chain terminated at the working substitute.** No MCP call was retried and no deeper tier was chained, per the zero-fallback policy.

## Method & caveats

- **Focus list:** the 12 names from the 2026-10-30 18:30 ET sweep (`daily-screens/2026-10-30/focus.md`), capped at 12 per the spec. All 12 were scanned; none were dropped.
- **Gap %** = (pre-market last ÷ prior regular close − 1) × 100.
- **Pre-market price** is the Nasdaq `extended-trading` consolidated print. Where no consolidated row is published (DFIN), the last **executed** tape print is used and labelled as such in the CSV's `pm_price_source` column.
- **The `/info` endpoint's `primaryData` was deliberately not used for the price.** It was observed flipping on GEN from $28.00 (−3.88%) to $29.09 (−0.14%) inside one minute while the consolidated tape and TradingView both sat near −1%; on CVNA it read $69.22 while the consolidated print was $68.49. It is used only as a timestamp/liveness cross-check.
- **Pre-market volume** is the Nasdaq `extended-trading` `infoTable` cumulative share counter. The `info` endpoint's `primaryData.volume` was deliberately not used — it returns a non-share-count value (e.g. `253,595.484401`) and is not comparable to the 50,000-share threshold. Two exceptions are handled explicitly: **ADT**, whose counter was rejected as faulty (its complete tape and TradingView both read ~6k while the counter read 606,500), and **DFIN**, which publishes no counter at all — there the figure is the **tape sum and is a lower bound only**. Every row's basis is recorded in the CSV's `pm_volume_source` column.
- **Thin prints are quotes, not markets.** The tape carries many 1–2 share prints. Session extremes are therefore computed on prints of 25+ shares; on that basis the widest *realised* moves are materially smaller than the raw tape extremes. DFIN's $70.00 print (+4.65%) was a **single share** — correctly not a flag.
- **Nasdaq's `tradeDetailTable` is served newest-first.** The last executed print is taken after sorting by clock time; taking the last row unsorted silently reports the *oldest* print on the page, which for DFIN would have shown a stale $70.00 (+4.65%) instead of the actual $66.95 (+0.09%).
- **Four snapshots** confirm the quotes were live rather than stale. The reported table is the final paired 09:00 ET snapshot.
- **No session lag on the reference price.** The denominator is the settled 2026-10-30 regular session, confirmed independently by two agreeing sources.
- **Errors:** 0 failed ticker fetches across all four snapshots — all 12 names returned a usable quote, a gap figure and a pre-market tape.

## Data quality — what this runtime's feeds got wrong, and how it was handled

The pre-market feed exposed four distinct traps this morning. Each is handled explicitly rather than silently, and none of them changes the 0-flag result.

| # | Trap | What was observed | Handling |
|---|---|---|---|
| 1 | **`/info` `primaryData` flips intraday** | GEN read `$28.00` (−3.88%) at 08:40 ET and `$29.09` (−0.14%) at 08:41 ET, while the consolidated tape and TradingView both sat near −1%. CVNA read `$69.22` while the tape printed `$68.49`. | The `/info` endpoint's `primaryData` is **not used for the price at all**. It is read only for a liveness timestamp. |
| 2 | **`secondaryData` (the supposed prior close) drifts** | PRCH's `secondaryData` read `20.68` against the true settled close of `20.56`; in earlier snapshots it drifted on CVNA (68.49 vs 68.29), DFIN (68.00 vs 66.89) and GKOS (237.44 vs 237.60). | The denominator is the **2026-10-30 sweep's own `focus.csv` close**, independently confirmed to the cent by TradingView's `close` on 12/12 names. Two agreeing sources beat one drifting one. |
| 3 | **The extended-trading tape is served newest-first** | Taking the last row of `tradeDetailTable` unsorted returns the *oldest* print on the page. For DFIN that is a stale `$70.00` (+4.65%) instead of the actual `$66.95` (+0.09%) — and DFIN's stale value was the only thing in the entire run that came close to the 4% trigger. | Prints are sorted by clock time and the freshest executed print is used. |
| 4 | **A cumulative volume counter can be faulty** | ADT's counter jumped from `6,500` to `606,500` mid-session while its 71-row tape stayed flat at 6,726 shares; TradingView independently read `5,913`. | Where the trade-detail tape is **complete** (fewer than 100 rows, Nasdaq's cap) and contradicts the counter by more than 3x, the tape sum is used and the counter is rejected. Documented per-name in the CSV's `pm_volume_source` column. |

**Feed latency.** Nasdaq's extended-trading tape runs **16–39 minutes behind wall clock** (median 18 min) — the newest print on the page at a 09:03 ET pull is timestamped ~08:45 ET. The `/info` endpoint's own timestamps are fresher (up to 09:03 ET), but see trap 1: its values are not trustworthy. TradingView's scanner was near-static across a 3-minute re-pull, consistent with a similar lag. Because the largest gap on any source is 2.37% against a 4% trigger, a ~20-minute delay cannot change the flag decision for any name — but it does mean the figures here are a slightly earlier state of the tape than the clock suggests.

## Context — what the tape is reacting to

Monday is a relief bounce after a punishing week for tech: the Nasdaq shed more than 2% into Friday's close, Intel issued weaker-than-expected guidance and fell 24% in one session, and Alphabet logged its sharpest weekly drop since 2008. Futures are up — S&P 500 +0.5%, Nasdaq-100 +0.8%, Dow +0.6% — positioning ahead of **Tuesday's US midterm elections** and a heavy earnings week (Apple and Palantir after Monday's close, AMD on Tuesday). Oil is down more than 4% on US–Iran diplomatic progress and the dollar is softer. Midterms plus a dense earnings calendar together imply elevated two-way volatility into the open — which is consistent with a Focus list that is liquid but flat rather than gapping.

### Catalyst notes on the Focus names

- **PURR** (Hyperliquid Strategies) is the one Focus name with real pre-market liquidity — **524,772 shares**, about 3% of its 30-day average volume — and it is trading **down -1.02%**. Two Hyperliquid wallets held a combined $1.06bn of short positions as of Sunday night and the HYPE token is down ~2.5%. That extends Friday's −10.4%, which gave back the prior session's +23%.
- **DFIN** (Donnelley Financial) is the only Focus name that actually *printed* above the 4% trigger: **$70.00 (+4.65%) at 07:00 ET — on one share**. It faded to $66.95 (+0.09%) by the final snapshot on 101 shares of total pre-market volume. A single-share print at a round number is a quote, not a market. The name closed Friday +9.53% and carries a $74.12 consensus target.
- **FTAI** (FTAI Aviation) filed its Q3 results and an 8-K pre-market (quarterly profit $151M, but nine-month operating cash use grew) and is indicated up +2.37% on thin volume — the largest live upside gap in the Focus list without approaching the trigger.
- **CROX** (Crocs) continues to work after a 25%+ post-earnings surge: Q3 adj EPS +26.4% to $3.69 vs a $3.31 consensus, HeyDude revenue +6.1%, international +11.8%. Wall Street is raising targets (consensus +18.9%).
- **GKOS** (Glaukos) beat Q3 by a wide margin (EPS $0.47 vs −$0.09 est, revenue $211M +23%) and its consensus target was raised 22.1% to $247.31 — it is drifting, not gapping.
- **BHC** (Bausch Health) is the clearest gap-and-fade in the group: +28.8% on earnings Wednesday, −8.0% on Friday, and flat in pre-market on very light volume.

## Source health

| Source | URL / query | HTTP status | Result |
|---|---|---|---|
| Nasdaq quote `extended-trading` | `https://api.nasdaq.com/api/quote/{SYM}/extended-trading?assetclass=stocks&markettype=pre` | 200 | **ok** — 12/12 tickers × 4 snapshots; consolidated pre-market print + cumulative volume + trade tape. No consolidated row for DFIN. |
| Nasdaq quote `info` | `https://api.nasdaq.com/api/quote/{SYM}/info?assetclass=stocks` | 200 | **ok but NOT used for the price** — `primaryData` demonstrably flips intraday (GEN −3.88% → −0.14% in 60s; CVNA $69.22 vs consolidated $68.49) and `secondaryData` drifted on PRCH and on 3/12 names in the earlier snapshots. Used only as a liveness/timestamp cross-check. |
| TradingView america scanner | `POST https://scanner.tradingview.com/america/scan` | 200 | **ok** — independent second source for `close`, `premarket_close`, `premarket_change`, `premarket_volume`, `average_volume_30d_calc`. Its `close` matches the sweep's `focus.csv` close to the cent on 12/12; pre-market divergence vs Nasdaq is under 0.6pp on 10/12 names (worst: GKOS 1.24pp). |
| MCP catalog probe | `probe_mcp.py` | n/a | `catalog_ok total=133 finance_tools=0` — **no financial MCP registered**. The absent `mcp__*` tools are not an error and are not counted. |
| MCP bridge `market-recap` | `mcp_bridge.py market-recap market_snapshot` / `get_quotes` | 200 | **ok** — used for market context only (indices, futures, oil, dollar). Packs available: `tradier`, `fmp`, `market-recap`; **no `tradingview` server**. |
| Nasdaq earnings calendar | `https://api.nasdaq.com/api/calendar/earnings?date=2026-11-02` | 200 | **ok** — 150 rows; **none of the 12 Focus names reports today**, so no gap is earnings-driven. |
| Yahoo Finance JSON | `query1/query2.finance.yahoo.com` | not attempted | Known 429 from this egress (per RUNTIME-CONTRACT.md); the Nasdaq API and TradingView returned complete data first, so the zero-fallback policy stops here. |
| Finviz screener | `finviz.com/screener.ashx?v=170` | not attempted | Known 403 (Cloudflare) from this egress. Not needed. |
| `web_search` (catalyst cross-check) | PURR / DFIN / FTAI / CROX / GEN / GKOS queries, `freshness=day` | 200 | **ok** — used for catalysts and to independently confirm the settled closes and the PURR / DFIN stories. |

## Files

- `daily-screens/2026-11-02/pre-market-gapper.md` — this report.
- `daily-screens/2026-11-02/pre-market-gapper.csv` — machine-readable per-ticker rows.

_Source: `nasdaq_public_api` + `tradingview_scanner` on every row. Scan time: 2026-11-02 08:46–09:00 ET._
