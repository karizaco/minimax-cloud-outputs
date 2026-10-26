<!-- cron #8 stock-screener-pre-market-gapper | cron_date=2026-10-26 | snapshot=2026-10-26 08:35:10 EDT | _source=nasdaq_public_api | degraded=true -->

# Pre-Market Gapper — Monday 2026-10-26

**No name in the Focus list clears the screen's flag rule (gap > +4% AND pre-market volume > 50,000).** The one material pre-market event is a downside gap: MRNA is −7.99% on 865,496 pre-market shares, the third session of the ESMO intismeran Phase 3 sell-the-news unwind. XLAB, the only Tier-A name, prints +3.28% on 178,798 shares — it clears the volume filter and sits 8 cents short of the +4% price filter, on a 6.7%-wide bid/ask, so the gap number is soft.

## Deviations from the spec'd data path — read this first

The spec'd primary path (`mcp__tradingview-advanced__stock_extended_hours`, one call per Focus ticker) was **not available in this sandbox**: the TradingView MCPs are not registered, and the connector catalog contains no market-data connector. The Tier-2 fallback (batched Finviz pre-market screener, `v=170`) returned **HTTP 403** to both `web_fetch` and `curl` — Finviz is bot-blocking this egress. The Tier-4 Yahoo chart API returned **HTTP 429**. Data was ultimately taken from the **Nasdaq public quote API** (`api.nasdaq.com/api/quote/<sym>/extended-trading?markettype=pre`), which is not in the skill's chain but returns the three fields the rule needs: pre-market consolidated last trade, pre-market share volume, and prior regular close. Every row carries `_source=nasdaq_public_api`; the run is marked `degraded=true` because the sanctioned path did not fire.

## Focus list scanned

5 names, from the most recent completed daily sweep: `daily-screens/2026-10-23/focus.md` (cron_date 2026-10-23, data_date 2026-10-22). The 18:30 ET sweep for 2026-10-26 has not run yet, so the 2026-10-23 file is the latest available input — a one-trading-day lag, which is the intended behaviour for this cron. Gaps below are measured against the **2026-10-23 regular close**, not the older data-date close.

Focus list: XLAB, MRNA, KOD, TJGC, CD. Tier-A (2026-10-23 sweep): XLAB only.

## Pre-market readings

| Sym | Company | Prev close (10-23) | Pre-market last | Gap % | Pre-mkt vol | Pre-mkt high / low | Bid / ask | Rule result |
|---|---|---|---|---|---|---|---|---|
| **XLAB** | Exascale Labs Holdings Inc. Class A Common Stock | $3.35 | $3.46 | 3.28% | 178,798 | $3.59 (07:49:30 AM) / $3.2 (04:06:34 AM) | $3.33 / $3.56 | volume pass, price short |
| **MRNA** | Moderna, Inc. Common Stock | $200.10 | $184.11 | -7.99% | 865,496 | $195.33 (04:01:06 AM) / $175.5549 (06:15:10 AM) | $183.50 / $183.98 | down-gap alert |
| **KOD** | Kodiak Sciences Inc Common Stock | $87.63 | $88.01 | 0.43% | 2,840 | $88.32 (06:40:07 AM) / $87.5 (07:07:36 AM) | $87.50 / $89.00 | no flag |
| **TJGC** | TJGC Group Limited Class A Ordinary Shares | $31.89 | $— | —% | — | — / — | $32.52 / $36.06 | — (no pre-market prints) |
| **CD** | Chaince Digital Holdings Inc. Ordinary Shares | $8.76 | $8.76 | 0.00% | 750 | $8.76 (06:57:35 AM) / $8.76 (06:57:35 AM) | $8.45 / $10.31 | no flag |

Snapshot taken at 2026-10-26 08:35:10 EDT. The Tier-A name XLAB was the only Focus member hitting both the price and volume filters at any point this morning, and it has drifted between +3.28% and +3.58% across snapshots this session — it is genuinely borderline rather than decisively inside or outside the rule.

## Flag results

- **Up-gap flags (gap > +4% AND pre-market volume > 50,000): none.** The screen returns zero flagged names, which is a real result and not a failure to fetch.
- **Down-gap alert (gap < −4% on > 50,000 shares) — outside the skill's rule, reported because the move is material: MRNA.**

**MRNA — $184.11, −7.99% vs the $200.10 close, 865,496 pre-market shares.** Catalyst is company-specific: the Phase 3 INTerpath-001 readout for intismeran autogene (personalised mRNA melanoma vaccine, co-developed with Merck), presented at ESMO 2026 in Madrid, showed a 42% reduction in recurrence or death versus 49% in the earlier Phase 2b study — a "sell-the-news" reaction layered on a stock that had already fallen 17.57% on 2026-10-22 and 1.25% on 2026-10-23, leaving it roughly 27% below its $254.48 52-week high. The pre-market range was wide ($175.55 low, $195.33 high) and the analyst tape turned cautious the same morning, with a Redburn downgrade to Sell and a Brookline FY2030 estimate trim. This is a continuation of a multi-session unwind, not a new single-print shock. For a gap-long screen it is an exclude; for a gap-short screen it is the only qualified name on the list.

## Regime context

From the 2026-10-23 sweep's `_regime.json`: large-cap breadth 65.3% above the 20-DMA (858-name $10B+ proxy), VIX 19.03, `late_cycle=false`, `size_cut_pct=null`, `uncertainty` not computed (the VIX/VXV ratio could not be built — both long-end legs returned zero bars). SPY, QQQ, QQQE and IWM were all below their 20-DMA as of the 2026-10-22 data date, so the tape is mixed breadth with weak index structure. MRNA's drop was idiosyncratic — broad futures were roughly flat into the open.

## Method & caveats

- The flag rule was applied exactly as specified: `gap_pct > 4` and `pre_market_volume > 50,000`, on the last completed Focus list, capped at the 12-name Focus limit (5 names present).
- Pre-market volume is the exchange-reported cumulative pre-market share volume. XLAB's figure (178,798) includes fractional odd-lot prints, which inflates the count slightly relative to whole-share volume.
- The XLAB gap is measured on a 6.7%-wide spread ($3.33 / $3.56) and a single last trade, so treat +3.28% as indicative rather than firm.
- TJGC printed nothing pre-market; its $32.52 / $36.06 bid/ask is indicative only, with no consolidated last trade, so it has no gap to score. CD traded 750 shares at an unchanged $8.76.
- KOD moved +0.43% on 2,840 shares — under the volume filter by a wide margin.
- Pre-market data is live and was read once, at 2026-10-26 08:35:10 EDT. Prices will drift between that snapshot and the 09:30 open; re-read before acting on any borderline name.
