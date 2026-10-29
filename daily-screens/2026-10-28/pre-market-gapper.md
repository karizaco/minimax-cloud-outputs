# Pre-Market Gapper — 2026-10-28 (US/Eastern)

**Session:** Wednesday 2026-10-28 pre-market. **Cron:** #8 `stock-screener-pre-market-gapper` (fired 08:30 ET; snapshots taken 08:34, 08:37 and 08:58 ET).
**Focus-list source:** `daily-screens/2026-10-27/focus.md` — the most recent completed 18:30 ET sweep (12 names). **Reference close:** settled 2026-10-27 regular-session close.
**Data source:** Nasdaq public quote API (`/info` + `/extended-trading?markettype=pre`), per ticker. `_source=nasdaq_public_api`.

## Result

**0 of 12 Focus names flagged.** No Focus ticker satisfied both conditions (gap > 4% AND pre-market volume > 50,000 shares) at the final snapshot. This is a clean no-setup session, not a data failure — every name returned a live quote.

9 of the twelve names cleared the *volume* bar, but **none cleared the 4% gap bar** — the widest pre-market gap in the Focus list was MXL at +1.92%. The screen is a price filter first and a liquidity filter second, so a session can be liquid and still produce no setups.

The one name that ever came close to triggering was **GLXY**: it ran to **+3.55%** on 65,726 shares of cumulative pre-market volume, i.e. 45 bps short of the gap trigger with the volume bar already cleared. It then faded back to **+1.86%** by the final snapshot while volume kept building to 109,057 shares. That is the shape of a pre-market push that did not hold — the gap was given back into the open rather than extended, so it is correctly not a flag.

| Ticker | PM volume | Gap % | Distance to gap trigger |
|---|---|---|---|
| CRML | 278,328 | -2.89% | 6.89 pp |
| GLXY | 109,057 | +1.86% | 2.14 pp |
| RKLB | 406,391 | -0.19% | 4.19 pp |
| RDW | 259,313 | -0.34% | 4.34 pp |
| MXL | 70,344 | +1.92% | 2.08 pp |
| CYPH | 221,457 | -3.03% | 7.03 pp |
| ALAB | 51,815 | +1.63% | 2.37 pp |
| OUST | 53,899 | +1.40% | 2.60 pp |
| LUNR | 81,620 | -0.35% | 4.35 pp |

Pre-market volume is a running counter, so any of these names can still cross before the 09:30 ET open. None of them qualified at the time of this scan.

## Full Focus scan (all 12)

| Ticker | Prior close (2026-10-27) | PM last | Gap % | PM volume | PM high | PM low | PM timestamp | Last tape print | Flag |
|---|---|---|---|---|---|---|---|---|---|
| MXL | 74.67 | 76.1 | +1.92% | 70,344 | 77.5 | 75.51 | 8:57 AM ET | 08:42:40 | vol-only |
| GLXY | 17.18 | 17.5 | +1.86% | 109,057 | 17.8 | 17.21 | 8:56 AM ET | 08:40:09 | vol-only |
| ALAB | 286.69 | 291.35 | +1.63% | 51,815 | 296.0 | 287.98 | 8:57 AM ET | 08:41:41 | vol-only |
| OUST | 32.79 | 33.25 | +1.40% | 53,899 | 33.9798 | 33.25 | 8:57 AM ET | 08:41:31 | vol-only |
| SDGR | 26.72 | 26.84 | +0.45% | 7,707 | 26.97 | 26.6 | 8:57 AM ET | 08:41:45 | — |
| HRI | 156.06 | 156.0 | -0.04% | 1,626 | 156.84 | 154.25 | 8:44 AM ET | 08:37:29 | — |
| RKLB | 58.31 | 58.2 | -0.19% | 406,391 | 59.09 | 58.1173 | 8:56 AM ET | 08:40:07 | vol-only |
| RDW | 8.89 | 8.86 | -0.34% | 259,313 | 9.02 | 8.81 | 8:57 AM ET | 08:40:58 | vol-only |
| LUNR | 11.56 | 11.52 | -0.35% | 81,620 | 11.7 | 11.48 | 8:56 AM ET | 08:42:13 | vol-only |
| ON | 78.67 | 76.925 | -2.22% | 36,915 | 78.15 | 76.803 | 8:55 AM ET | 08:42:09 | — |
| CRML | 8.13 | 7.895 | -2.89% | 278,328 | 8.0009 | 7.74 | 8:57 AM ET | 08:40:54 | vol-only |
| CYPH | 3.135 | 3.04 | -3.03% | 221,457 | 3.22 | 3.0206 | 8:56 AM ET | 08:41:41 | vol-only |

Sorted by gap, largest first. Every `Prior close` here matches the 2026-10-27 sweep's `focus.csv` close to the cent (delta 0.00 for all 12), so the gap is measured against the settled prior regular session — there is no reference-price lag in this run.

## Flags by test

| Ticker | Gap > 4% | PM vol > 50k | Flagged | Note |
|---|---|---|---|---|
| MXL | no | yes | no | pm_vol>50k but gap<=4 |
| GLXY | no | yes | no | pm_vol>50k but gap<=4 |
| ALAB | no | yes | no | pm_vol>50k but gap<=4 |
| OUST | no | yes | no | pm_vol>50k but gap<=4 |
| SDGR | no | no | no | gap<=4 |
| HRI | no | no | no | gap<=4 |
| RKLB | no | yes | no | pm_vol>50k but gap<=4 |
| RDW | no | yes | no | pm_vol>50k but gap<=4 |
| LUNR | no | yes | no | pm_vol>50k but gap<=4 |
| ON | no | no | no | gap<=4 |
| CRML | no | yes | no | pm_vol>50k but gap<=4 |
| CYPH | no | yes | no | pm_vol>50k but gap<=4 |

## Snapshot trend (liveness confirmation)

Three snapshots were taken to confirm the quotes were live rather than stale, and to track the one name sitting near the gap threshold.

| Ticker | 08:34 ET gap | 08:37 ET gap | 08:58 ET gap | Vol 08:34 | Vol 08:37 | Vol 08:58 |
|---|---|---|---|---|---|---|
| MXL | +2.18% | +1.94% | +1.92% | 65,349 | 65,724 | 70,344 |
| GLXY | +2.50% | +3.55% | +1.86% | 65,424 | 65,726 | 109,057 |
| ALAB | +1.85% | +1.57% | +1.63% | 47,723 | 48,839 | 51,815 |
| OUST | +1.86% | +2.07% | +1.40% | 52,132 | 52,260 | 53,899 |
| SDGR | +0.49% | +0.49% | +0.45% | 7,105 | 7,105 | 7,707 |
| HRI | -1.16% | -1.16% | -0.04% | 1,024 | 1,624 | 1,626 |
| RKLB | +0.22% | -0.17% | -0.19% | 351,929 | 353,789 | 406,391 |
| RDW | +0.09% | +0.11% | -0.34% | 230,945 | 232,758 | 259,313 |
| LUNR | -0.43% | -0.09% | -0.35% | 74,021 | 74,243 | 81,620 |
| ON | -1.81% | -1.81% | -2.22% | 35,570 | 35,570 | 36,915 |
| CRML | -1.97% | -3.06% | -2.89% | 253,165 | 257,010 | 278,328 |
| CYPH | -1.13% | -1.75% | -3.03% | 193,883 | 194,952 | 221,457 |

## Deviations from the skill spec (read first)

| # | Spec says | What ran instead | Why | Impact |
|---|---|---|---|---|
| 1 | `mcp__tradingview-advanced__stock_extended_hours(ticker)` per ticker (≤ 12 calls) | Nasdaq public quote API, 2 HTTP calls per ticker (24 requests per snapshot) | The entire MCP tier is **unbound in this Cloud session**. `mcp__tradingview__*`, `mcp__tradingview-advanced__*` and `mcp__shibui-finance__*` are not registered, and the published MCP bridge (`mcp_bridge.py`) exposes only `stocktwits` and `shibui` — no tradingview server. | Primary source unavailable. |
| 2 | Tier-2 fallback: `finviz_premarket_gap_url(tickers)` → one `web_fetch` | Not attempted this run; the Nasdaq API worked directly and the zero-fallback policy stops at the first tier that returns real data. (On 2026-10-27 the same fallback returned HTTP 403 — Cloudflare challenge — from this egress.) | Finviz bot-blocks this sandbox's IP. | Tier 2 known-unusable; the Nasdaq API is the working substitute. |
| 3 | Flag `gap_pct > 4` AND `pre_market_volume > 50_000` | Same thresholds, same semantics | — | None. |
| 4 | Run at 09:00 ET | Cron fired 08:30 ET; snapshots at 08:34, 08:37 and 08:58 ET | This cron's deployed schedule is 08:30 ET weekdays. | The 08:58 snapshot lands inside the spec's intended window, so the reported figures are directly comparable to a 09:00 ET run. |
| 5 | "One chat line per flagged name" | No chat lines emitted (0 flags) | Cron spec: quiet if no flags. | — |

**Fallback chain terminated at the working substitute.** No MCP call was retried and no deeper tier was chained, per the zero-fallback policy.

## Method & caveats

- **Focus list:** the 12 names from the 2026-10-27 18:30 ET sweep (`daily-screens/2026-10-27/focus.md`), capped at 12 per the spec. All 12 were scanned; none were dropped.
- **Gap %** = (pre-market consolidated last ÷ prior regular close − 1) × 100, with the prior close taken from the Nasdaq `secondaryData` field ("Closed at Oct 27, 2026 4:00 PM ET") and cross-checked against the sweep's `focus.csv` close. All 12 agreed to the cent (delta 0.00).
- **Pre-market volume** is the Nasdaq `extended-trading` `infoTable` cumulative pre-market share volume, sampled at snapshot time. It is a running counter, not a per-print figure. This field was used rather than the `info` endpoint's `primaryData.volume`, which returns a non-share-count value (e.g. `253,595.484401`) for some names and is not directly comparable to the 50,000-share threshold.
- **Independent price cross-check.** `web_search` on GLXY independently returned a prior close of $17.18 ("Galaxy Digital last closed at $17.18") and an early pre-market print of $17.46 at 06:29 ET, which sits on the same rising path as the Nasdaq tape. The Nasdaq pre-market reads are real, not stale prints.
- **Three snapshots** were taken to confirm quotes were live rather than stale, and to track the name sitting nearest the gap threshold. The reported table is the final (08:58 ET) snapshot.
- **No session lag on the reference price.** Unlike the shibui-dependent sweeps, this scan's prior close is the settled 2026-10-27 regular session, confirmed independently by the Nasdaq close timestamp.
- **Errors:** 0 failed ticker fetches, across all three snapshots. All 12 names returned a usable quote, a gap figure and a pre-market tape.

## Source health

| Source | URL / query | HTTP status | Result |
|---|---|---|---|
| Nasdaq quote `info` | `https://api.nasdaq.com/api/quote/{SYM}/info?assetclass=stocks` | 200 | ok — 12/12 tickers; live `primaryData.lastSalePrice` + prior close `secondaryData.lastSalePrice` |
| Nasdaq quote `extended-trading` | `https://api.nasdaq.com/api/quote/{SYM}/extended-trading?assetclass=stocks&markettype=pre` | 200 | ok — 12/12 tickers; `infoTable` pre-market row + `tradeDetailTable` tape |
| MCP bridge (`stocktwits` / `shibui`) | `mcp_bridge.py` published MCP-over-HTTP bridge | n/a | **not used** — no tradingview server is exposed by the bridge, so the spec's primary `stock_extended_hours` tool is unreachable from this runtime. |
| Yahoo Finance JSON (spark / chart / screener) | `query1`/`query2.finance.yahoo.com` | 429 | **rate-limited** from this egress (persistent, per RUNTIME-CONTRACT.md). Not used — the Nasdaq API returned complete data first. |
| Finviz screener | `finviz.com/screener.ashx?v=170` | 403 | **blocked** (Cloudflare challenge) from this egress. Not used — see deviation 2. |
| `web_search` (cross-check) | GLXY pre-market query, `freshness=day` | 200 | ok — independent confirmation of the prior close and pre-market direction. |

## Files

- `daily-screens/2026-10-28/pre-market-gapper.md` — this report.
- `daily-screens/2026-10-28/pre-market-gapper.csv` — machine-readable per-ticker rows (ticker, prior close, PM last, gap %, PM volume, PM high/low, timestamp, flag, stylists, `_source`).

_source: `nasdaq_public_api` on every row. Scan time: 2026-10-28 08:34–08:58 ET._
