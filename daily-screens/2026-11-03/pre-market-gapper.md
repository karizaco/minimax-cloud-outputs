# Pre-Market Gapper — 2026-11-03 (US/Eastern)

**Session:** Tuesday 2026-11-03 pre-market. **Cron:** #08 `stock-screener-pre-market-gapper` (scheduled 08:30 ET; five snapshots taken at 08:34, 08:51, 09:07, 09:11 and 09:12 ET, the last just before the 09:30 open).
**Focus-list source:** `daily-screens/2026-11-02/focus.md` — the most recent completed 18:30 ET sweep (Monday 2026-11-02; 12 names). **Reference close:** settled 2026-11-02 regular-session close, taken from that sweep's own `focus.csv` and confirmed on **12/12 names** by the TradingView scanner `close` and the MCP-bridge `market-recap` `price` (and by Nasdaq's `/info` secondary data on 11/12 — see data-quality finding 1).
**Data source:** Nasdaq public quote API (`/info` + `/extended-trading?markettype=pre&assetclass=stocks`) per ticker, cross-checked against the TradingView america scanner and the Yahoo quote page. `_source=nasdaq_public_api`.

## Result

**0 of 12 Focus names cleared the strict gate** (|gap| > 4% AND pre-market volume > 50,000 shares) on the consolidated tape. **One name touched the trigger: PURR.**

PURR is the only Focus name with both real pre-market liquidity and a gap at the bar — it traded **$10.0083 (+3.07%) on 595,761 shares** on the consolidated tape, with a live last sale of **$10.14 (+4.43%)** and a quote band of **$10.04 x $10.14**. It touched **$10.28 (+5.87%) at 09:02 ET** and then faded. So the honest read is *one print from the bar*: above 4% if you take the live last sale or the offer, below it on the last consolidated trade.

**The result does not depend on which source you believe.** Only three Focus names cleared 50,000 pre-market shares at all — **PURR (595,761), NOW (1,107,335) and MRNA (94,485)** — and neither NOW (-1.19%) nor MRNA (+0.33%) is anywhere near a 4% gap. Every name that *did* breach 4% at some point this morning breached it on trivial size: CAI printed +5.53% on a 10-share print at 08:49 and was back at -1.25% by 09:12; CVI printed -6.99% on a 1-share print and -5.92% on 25-share prints and recovered to -2.54%; MTZ printed +3.93% on a series of 1-share prints and settled at +2.94% on 2,494 shares. A gap on one share is a quote, not a market.

### The one name on the trigger

- **PURR** +3.07% on the consolidated tape / +4.43% on the live last sale — 595,761 pre-market shares (~3.5% of Monday's 17.2M regular-session volume). Quote band $10.04 x $10.14; pre-market range $9.58 - $10.28, with the high at 09:02 ET.
  Context: a bounce off Monday's -11.81% ($9.71) session, and **not** a crypto-led bid — HYPE itself was **$84.41, -1.30% on 24h** with the ICE US-futures plan still awaiting CFTC approval and a 180,000-HYPE distribution on Nov 6. PURR reports Q1 FY2027 on **Nov 5** after the close.

### Volume cleared, gap did not

- **NOW** -1.19% on 1,107,335 shares — the largest pre-market liquidity in the list by far, and it is drifting lower. Post-Q3 de-rating on AI-disruption fears after the Oct 28 report (Q3 subscription revenue +20.5% cc, 50bp above guidance; 2026 AI ACV target raised to >$1.7B), with a 24/7 Wall St. piece noting the stock "shed a third of its value in a single week".
- **MRNA** +0.33% on 94,485 shares — quiet.

## Full Focus scan (all 12)

Sorted by absolute gap, largest first. `PM tape last` is the Nasdaq extended-trading **consolidated last trade** and is the published gap field; `Nasdaq real-time last` is the `/info` `primaryData` last sale, which can be a different (and sometimes trivial-size) print. `PM vol` is cumulative pre-market share volume.

| Ticker | Ref close (11-02) | PM tape last | Gap % | PM vol | PM high | PM low | Nasdaq real-time last | Real-time % | TV pm % | TV pm vol | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PURR | $9.71 | $10.0083 | **+3.07%** | 595,761 | $10.28 | $9.58 | $10.14 | +4.43% | +2.99% | 312,927 | volume only |
| MTZ | $193.77 | $199.46 | **+2.94%** | 2,494 | $200.56 | $197.26 | $198.99 | +2.69% | +3.00% | 1,141 | — |
| CVI | $55.92 | $54.5 | **-2.54%** | 15,385 | $59.00 | $52.01 | $54.45 | -2.63% | -2.56% | 11,544 | — |
| ABCL | $11.12 | $11.36 | **+2.16%** | 28,121 | $11.39 | $11.06 | $11.38 | +2.34% | +2.16% | 19,759 | — |
| CAI | $32.10 | $31.7 | **-1.25%** | 20,267 | $32.65 | $31.90 | $31.7 | -1.25% | +1.25% | 19,353 | — |
| NOW | $106.01 | $104.75 | **-1.19%** | 1,107,335 | $105.67 | $103.70 | $105.01 | -0.94% | -1.14% | 253,343 | volume only |
| KOD | $97.62 | $98.5764 | **+0.97%** | 6,739 | $98.35 | $97.54 | $98.19 | +0.58% | +0.59% | 6,170 | — |
| CDNA | $85.88 | $86.65 | **+0.90%** | 3,350 | $86.41 | $85.75 | $86.12 | +0.28% | +0.62% | 3,086 | — |
| HTFL | $54.49 | $54.15 | **-0.62%** | 3,526 | $55.05 | $53.60 | $54.46 | -0.06% | +1.03% | 2,159 | — |
| QLYS | $207.60 | $208.69 | **+0.53%** | 2,040 | $207.95 | $206.25 | $206.81 | -0.38% | -0.65% | 966 | — |
| MRNA | $220.83 | $221.55 | **+0.33%** | 94,485 | $223.58 | $218.00 | $221.7 | +0.39% | +0.32% | 38,510 | volume only |
| LQDA | $41.85 | $41.95 | **+0.24%** | 29,424 | $42.83 | $41.00 | $41.95 | +0.24% | +1.55% | 28,479 | — |

**Note on the high/low columns:** Nasdaq's `highPrice` / `lowPrice` fields lag the consolidated row, so for CDNA, QLYS and KOD the tape last sits a few cents above the reported pre-market high. The gap column is computed from the tape last trade only; the high/low columns are as-reported and are not re-derived.

## Flags by test

| Ticker | Gap % | PM vol | \|gap\| > 4% | vol > 50k | Flagged | Note |
|---|---|---|---|---|---|---|
| PURR | +3.07% | 595,761 | no | yes | no | borderline — live last sale +4.43% clears the bar, consolidated tape does not |
| MTZ | +2.94% | 2,494 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| CVI | -2.54% | 15,385 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| ABCL | +2.16% | 28,121 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| CAI | -1.25% | 20,267 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| NOW | -1.19% | 1,107,335 | no | yes | no | volume only, no gap |
| KOD | +0.97% | 6,739 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| CDNA | +0.90% | 3,350 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| HTFL | -0.62% | 3,526 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| QLYS | +0.53% | 2,040 | no | no | no | abs(gap)<=4 and pm_vol<=50k |
| MRNA | +0.33% | 94,485 | no | yes | no | volume only, no gap |
| LQDA | +0.24% | 29,424 | no | no | no | abs(gap)<=4 and pm_vol<=50k |

## Snapshot trend — liveness confirmation

Five pulls from 08:34 to 09:12 ET (the final one just before the open). Every column moves, so the quotes are live rather than stale.

### PURR (the name on the trigger)

| Snapshot (ET) | Tape last | Tape % | Tape vol | TV pm % |
|---|---|---|---|---|
| 2026-11-03T13:34:46Z | $9.88 | +1.75% | 245,692 | +1.75% |
| 2026-11-03T13:52:46Z | $10.025 | +3.24% | 341,500 | +3.30% |
| 2026-11-03T14:07:49Z | $10.0211 | +3.20% | 577,211 | +3.45% |
| 2026-11-03T14:11:02Z | $10.0083 | +3.07% | 591,942 | +3.08% |
| 2026-11-03T14:12:22Z | $10.0083 | +3.07% | 595,761 | +2.99% |

### Gap % at every snapshot, all 12 names

| Ticker | 08:34 | 08:51 | 09:07 | 09:11 | 09:12 (final) |
|---|---|---|---|---|---|
| CDNA | +0.26% | +2.26% | -0.15% | +0.90% | +0.90% |
| HTFL | -0.55% | -0.70% | -0.62% | -0.62% | -0.62% |
| CAI | -1.13% | +1.25% | +5.53% | +5.53% | -1.25% |
| QLYS | -0.77% | +0.33% | +0.40% | +0.53% | +0.53% |
| PURR | +1.75% | +3.24% | +3.20% | +3.07% | +3.07% |
| MRNA | +0.33% | +0.71% | +0.53% | +0.43% | +0.33% |
| NOW | -1.52% | -1.33% | -1.01% | -1.12% | -1.19% |
| CVI | -0.30% | -5.92% | -5.30% | -5.30% | -2.54% |
| KOD | +0.01% | +0.01% | +0.97% | -0.10% | +0.97% |
| ABCL | +0.72% | +2.25% | +2.07% | +2.16% | +2.16% |
| MTZ | +2.18% | +2.64% | +2.65% | +2.94% | +2.94% |
| LQDA | +1.00% | -2.99% | +0.24% | +0.24% | +0.24% |

## Data-quality findings (this run)

Four field-level defects in the Nasdaq public API were caught and corrected against independent sources. Each one would have produced a wrong gap for the name involved, so each is documented rather than silently absorbed.

1. **`/info` `secondaryData.lastSalePrice` is not always the settled close.** For **QLYS** it returned **$206.00** while the true 2026-11-02 close is **$207.60** — confirmed by Nasdaq's own `/historical` table (11/02/2026 close $207.60), the TradingView scanner `close`, the bridge `market-recap` `price`, and the sweep's own `focus.csv` (four sources agree on 207.60). Using 206.00 would have moved QLYS's gap from +0.53% to -0.01%.
2. **The same field flips mid-session.** For **KOD** it read $97.625 at 08:34 and $98.5764 at 09:07 — the latter is a stale *pre-market* print, not a close. The settled close is $97.625 (focus.csv, TV, bridge all agree); the field was ignored for the reference price.
3. **`/info` `primaryData.lastSalePrice` can be a trivial-size print.** For **CAI** it read $33.8747 (+5.53%) at 08:49 on a **10-share** print while the consolidated tape was $32.50 (+1.25%); by 09:12 the name was -1.25%. The same pattern hit CVI (-6.99% on 1 share) and MTZ (+3.93% on 1-share prints). **Rule applied: a gap must be confirmed on the consolidated tape with size behind it.**
4. **The bridge is not a pre-market print source.** `market-recap get_quotes` returns `market_state: "pre"` but serves the **2026-11-02 regular close** (`as_of` 21:00 UTC, `price` = the settled close, `previous_close` = Oct 30). It is excellent for confirming reference closes — all 12 matched to the cent — and useless for the pre-market print. Yahoo was therefore used only as a third cross-check, not as the source of record.

Additionally: **the TradingView scanner's `premarket_volume` undercounts** — PURR 320,722 vs Nasdaq 595,761; NOW 253,343 vs 1,107,335. Both still clear 50,000, so the gate outcome is source-robust, but TV volume must not be used for the liquidity test on its own. TV's `premarket_price` is null for every name, and its `premarket_time` is a static session-bar label (04:00 ET) that does not move between snapshots.

## Catalysts (sourced, not inferred)

- **PURR** — bounce off Monday's -11.81% session; **not** crypto-led (HYPE $84.41, -1.30% 24h). Q1 FY2027 earnings Nov 5 after the close.
- **CVI** — **Q3 2026 reported before the open today**: profit $570M, EPS $5.67, adjusted EPS $4.00, revenue $3.28B. UBS's price target is $53 (raised from $35, Neutral). Stock -2.54% pre-market on only 15,385 shares.
- **NOW** — drifting after the Oct 28 Q3 report (beat and raised) on AI-disruption fears.
- **CAI** — reports Q3 2026 tomorrow, Nov 4 after the close.

No catalyst is claimed for any other name, because none was sourced.

## Source health

| Source | Query / URL | Status | Use |
|---|---|---|---|
| Nasdaq public quote API | `api.nasdaq.com/api/quote/{SYM}/info?assetclass=stocks` + `/extended-trading?markettype=pre&assetclass=stocks` | ok (24 requests; NOW `/info` returned an empty payload twice and recovered on retry) | **source of record** — PM price, PM volume, PM high/low |
| Nasdaq historical | `api.nasdaq.com/api/quote/QLYS/historical` | ok | resolved the QLYS reference close |
| TradingView america scanner | `POST scanner.tradingview.com/america/scan` (filter `name in_range`, explicit `sort`, range 0-200) | ok (12/12 rows) | cross-check: settled close, PM range, PM % |
| Yahoo quote page | `finance.yahoo.com/quote/PURR/` | ok | third cross-check on the PURR print ($10.06, +3.58%) |
| MCP bridge `market-recap` | `get_quotes` for 12 symbols | ok | confirmed all 12 reference closes; **not** a pre-market print source |
| MCP bridge `shibui` / `stocktwits` | — | not used | not required for this routine |
| Connector catalog probe | `probe_mcp.py` | `catalog_ok total=135 finance_tools=0` | no finance MCP registered (expected) |
| `preopen-feed/` catalyst tape | `karizaco/minimax-cloud-outputs` | **not found** (directory absent) | cron #92a has not published a feed for 2026-11-03; catalysts sourced from the wire instead |

## Provenance

- Fire: cron #08 `stock-screener-pre-market-gapper`, task_id 457578163015913, `scheduled_at_ms` 1793712600000 = 2026-11-03 08:30 ET. **Live fire, not a delayed replay.**
- Snapshots: 2026-11-03 13:34:46Z, 13:52:46Z, 14:07:49Z, 14:11:02Z and 14:12:22Z UTC = 08:34, 08:51, 09:07, 09:11 and 09:12 ET.
- `_source=nasdaq_public_api`; gaps measured against the settled 2026-11-02 close.
- Companion CSV: `daily-screens/2026-11-03/pre-market-gapper.csv`.
