# Pre-Market Gapper — 2026-10-27 (US/Eastern)

**Session:** Tuesday 2026-10-27 pre-market. **Cron:** #8 `stock-screener-pre-market-gapper` (fired 08:30 ET; snapshots taken 08:32 and 08:37 ET).
**Focus-list source:** `daily-screens/2026-10-26/focus.md` — the most recent completed 18:30 ET sweep (12 names). **Reference close:** settled 2026-10-26 regular-session close.
**Data source:** Nasdaq public quote API (`/info` + `/extended-trading?markettype=pre`), per ticker. `_source=nasdaq_public_api`. **Degraded: yes** — see deviations below.

## Result

**0 of 12 Focus names flagged.** No Focus ticker satisfied both conditions (gap > 4% AND pre-market volume > 50,000 shares) at either snapshot. This is a clean no-setup session, not a data failure — every name returned a live quote.

One name cleared the gap test on price but failed on volume:

- **SDGR** — pre-market 5.38% ($25.82 vs $24.50 prior close), pre-market volume 35,295 shares — 14,705 short of the 50,000 bar. Quote timestamp Oct 27, 2026 8:29 AM ET (the trade-detail tape's most recent print is 08:17:42 ET).

  Pre-market volume is a running counter, so this name can still clear the bar before the 09:30 ET open. It does not qualify at the time of this scan.

## Full Focus scan (all 12)

| Ticker | Prior close (10-26) | PM last | Gap % | PM volume | PM high | PM low | PM timestamp | Flag |
|---|---|---|---|---|---|---|---|---|
| SDGR | 24.50 | 25.82 | 5.38% | 35,295 | 25.93 | 24.60 | Oct 27, 2026 8:29 AM ET | gap-only |
| PENG | 54.92 | 55.95 | 1.88% | 23,073 | 56.65 | 54.20 | Oct 27, 2026 8:36 AM ET | — |
| ORKA | 90.33 | 91.96 | 1.80% | 13,353 | 90.81 | 89.90 | Oct 27, 2026 8:36 AM ET | — |
| P | 131.33 | 133.00 | 1.27% | 17,202 | 134.54 | 130.70 | Oct 27, 2026 8:36 AM ET | — |
| CSCO | 110.24 | 111.49 | 1.13% | 607,026 | 111.70 | 109.71 | Oct 27, 2026 8:35 AM ET | — |
| NXPI | 245.83 | 248.11 | 0.93% | 10,173 | 246.91 | 243.25 | Oct 27, 2026 8:32 AM ET | — |
| ADI | 407.93 | 409.50 | 0.38% | 17,014 | 410.02 | 401.82 | Oct 27, 2026 8:26 AM ET | — |
| FIGS | 20.83 | 20.89 | 0.29% | 1,807 | 20.99 | 20.81 | Oct 27, 2026 8:07 AM ET | — |
| HEI | 309.71 | 309.71 | 0.00% | n/a | n/a | n/a | Oct 27, 2026 8:23 AM ET | no pre-market print |
| RNG | 86.31 | 86.30 | -0.01% | 3,345 | 87.66 | 85.79 | Oct 27, 2026 8:27 AM ET | — |
| OKTA | 220.01 | 217.75 | -1.03% | 12,810 | 221.00 | 218.51 | Oct 27, 2026 8:32 AM ET | — |
| TENB | 48.21 | 47.56 | -1.35% | 12,125 | 48.53 | 47.50 | Oct 27, 2026 8:34 AM ET | — |

Sorted by gap, largest first. Every `Prior close` here matches the 2026-10-26 sweep's `focus.md` close to the cent (delta 0.00 for all 12), so the gap is measured against the settled prior regular session — there is no reference-price lag in this run.

## Flags by test

| Ticker | Gap > 4% | PM vol > 50k | Flagged | Note |
|---|---|---|---|---|
| SDGR | yes | no | no | volume short of threshold |
| PENG | no | no | no |  |
| ORKA | no | no | no |  |
| P | no | no | no |  |
| CSCO | no | yes | no | volume qualifies, gap does not |
| NXPI | no | no | no |  |
| ADI | no | no | no |  |
| FIGS | no | no | no |  |
| HEI | no | n/a | no | no consolidated pre-market print |
| RNG | no | no | no |  |
| OKTA | no | no | no |  |
| TENB | no | no | no |  |

## Deviations from the skill spec (read first)

| # | Spec says | What ran instead | Why | Impact |
|---|---|---|---|---|
| 1 | `mcp__tradingview-advanced__stock_extended_hours(ticker)` per ticker (≤ 12 calls) | Nasdaq public quote API, 2 HTTP calls per ticker (24 requests) | The entire MCP tier is **unbound in this Cloud session** — `tool_search` for tradingview/stock/price returns 0 hits, so `mcp__tradingview__*`, `mcp__tradingview-advanced__*` and `mcp__shibui-finance__*` are all absent. | Primary source unavailable. |
| 2 | Tier-2 fallback: `finviz_premarket_gap_url(tickers)` → one `web_fetch` | Attempted once, **HTTP 403** (Cloudflare "Just a moment…" challenge) from this egress | Finviz bot-blocks this sandbox's IP. | Tier 2 unusable; the Nasdaq API was used as the working substitute for extended-hours prints. |
| 3 | Flag `gap_pct > 4` AND `pre_market_volume > 50_000` | Same thresholds, same semantics | — | None. |
| 4 | Run at 09:00 ET | Snapshots at 08:32 and 08:37 ET | This cron's schedule is 08:30 ET weekdays. | ~53 min of pre-market volume was still to accumulate before the 09:30 open, so the volume test is stricter here than it would be at 09:00 ET. |
| 5 | "One chat line per flagged name" | No chat lines emitted (0 flags) | Cron spec: quiet if no flags. | — |

**Fallback chain terminated at the working substitute.** No MCP call was retried and no deeper tier was chained, per the zero-fallback policy.

## Method & caveats

- **Focus list:** the 12 names from the 2026-10-26 18:30 ET sweep (`daily-screens/2026-10-26/focus.md`), capped at 12 per the spec. All 12 were scanned; none were dropped.
- **Gap %** = (pre-market consolidated last ÷ prior regular close − 1) × 100, with the prior close taken from the Nasdaq `secondaryData` field ("Closed at Oct 26, 2026 4:00 PM ET") and cross-checked against the sweep's `focus.md` close. All 12 agreed to the cent.
- **Pre-market volume** is the Nasdaq `extended-trading` `infoTable` cumulative pre-market share volume, sampled at the snapshot time. It is a running counter, not a per-print figure.
- **HEI** returned no consolidated pre-market row (no pre-market print at either snapshot); its last sale equals the prior close, so the gap is 0.00% and the volume is reported as n/a rather than the non-share-count value (6.64) that the `info` endpoint returns for it.
- **Two snapshots** (08:32 and 08:37 ET) were taken to confirm the quotes were live rather than stale. SDGR's price and volume were unchanged between them because no new print landed in that window. CSCO's reported cumulative pre-market volume jumped from 36,446 to 607,026 shares between snapshots, but every print in the visible last-100 pre-market tape is small, so the cumulative figure appears to include a block or off-tape print outside that window; treat CSCO's volume as an upper bound. CSCO's gap is 1.13%, so this does not affect the flag outcome either way.
- **No session lag on the reference price.** Unlike the shibui-dependent sweeps, this scan's prior close is the settled 2026-10-26 regular session, confirmed independently by the Nasdaq close timestamp.
- **Errors:** 0 failed ticker fetches. All 12 names returned a usable quote and a gap figure.

## Files

- `daily-screens/2026-10-27/pre-market-gapper.md` — this report.
- `daily-screens/2026-10-27/pre-market-gapper.csv` — machine-readable per-ticker rows (ticker, prior close, PM last, gap %, PM volume, PM high/low, timestamp, flag, stylists, `_source`).

_source: `nasdaq_public_api` on every row. Scan time: 2026-10-27 08:32–08:37 ET._
