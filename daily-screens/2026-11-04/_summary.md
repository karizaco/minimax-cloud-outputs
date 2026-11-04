# Sweep summary — 2026-11-04 (cron #09, 18:30 ET)

- **Regime state:** `size_cut_pct=0`, `uncertainty=false`, `late_cycle=false`. Breadth is strong (71.0% of 1,001 large caps above their 20-DMA; 756 adv / 243 dec) but the index is below its 20-DMA (only RSP and IWM of the 5 index ETFs are above it), so the size-cut rule — which needs BOTH the index below AND breadth under 40% — does not fire. VIX 16.61 / VIX3M 18.80 = 0.8835 → no front-end stress premium; max ATR extension from 50-DMA is RSP +3.88%, well under the 6% late-cycle line.
- **Tier-A names (≥ 3 distinct stylists, cap 8 — pool was 13, so the list is truncated):** LSCC (4), GKOS, CDNA, KVYO, FTAI, MRNA, FISV, GPK.
- **Parabolic short candidates (5-day gainers ≥ +25%, 11 names):** ADT +43.4%, AXGN +32.1%, WING +30.8%, GPK +30.1%, CPRI +30.1%, FMC +29.3%, GKOS +28.6%, CROX +28.5%, HAYW +26.6%, FTAI +26.5%, CDNA +25.4%.
- **3:55 PM reversal-bullish list:** not produced by this routine — the Bonde reversal-bullish scan belongs to cron #91 (15:55 ET), which reads the live session bar. This is the 18:30 ET end-of-day sweep.

## Counts

| Set | Count |
|---|---|
| Unique candidates (all screens) | 848 |
| Master (deduped union, capped) | 200 |
| Stalk (Master within 2% of 10/20-DMA) | 17 |
| Focus (≥ 2 distinct stylists, cap 12) | 12 |
| Tier-A (≥ 3 distinct stylists, cap 8) | 8 (pool 13, `tier_a_truncated: true`) |

| Stylist | Bucket | Candidates |
|---|---|---|
| Stockbee (Bonde) | `stockbee` | 122 |
| Qullamägi | `qullamaggie` | 68 |
| Jeff Sun | `jeff_sun` | 538 |
| Ariel Hernandez | `hernandez` | 30 |
| peoplewish | `peoplewish` | 200 |

## Screen origins and row counts

`A_stockbee_4pct` 50 · `B_stockbee_ep9m` 50 · `K_stockbee_anticipation` 30 · `C_qullamaggie_rs` 44 · `D_qullamaggie_ep` 6 · `E_qullamaggie_5d_gainers` 11 · `F_qullamaggie_5d_losers` 12 · `G_peoplewish` 200 · `jeff_sun_canslim` 85 · `TV_volume_breakout` 462 · `H_hernandez_theme` 30.

## Data-date note

**shibui T+1: this sweep's screen metrics are for `2026-11-03`, cron fired `2026-11-04`.** shibui's newest settled session at fire time was 2026-11-03 (`SELECT MAX(date) FROM shibui.stock_quotes WHERE date <= '2026-11-04'` → `2026-11-03`). Every "today" column in the CSV/Markdown outputs is the **2026-11-04 settled close** from TradingView, verified against Nasdaq's official 4:00 PM close on 15/15 sampled names.

## Source health

| Source | Status | Note |
|---|---|---|
| MCP availability probe | `catalog_ok total=135 finance_tools=0` | no finance MCP registered; the MCP-over-HTTP bridge is the finance path |
| shibui via bridge (6 SQL calls) | ok | resolve_date + 3 sweeps + breadth + CANSLIM rebuild; all returned rows |
| TradingView scanner (11 calls) | ok | large-cap universe 1,001/1,001 unique; volume breakout 462/462; no paging loss (explicit sort, de-duplicated by ticker) |
| Cboe delayed-quote CDN | ok | VIX/VIX3M stamped 2026-11-04T16:15:01 ET |
| Nasdaq `/info` | ok, 15/15 | official-close cross-check only |
| Finviz | not attempted | Cloudflare 403 from this egress (known) |
| Yahoo JSON | not used | — |

**errors: 0 source failures.** Degradations (documented, not errors): 5 of the 6 skip-rule flags are not computable from the available feeds; TradingView's relative volume is a ranking proxy; the breadth universe is a market-cap proxy rather than an index membership list.
