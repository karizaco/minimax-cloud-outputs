---
date: 2026-10-19
degraded: true
degraded_reason: "All five financial MCPs (shibui-finance, tradingview, tradingview-advanced, yahoo-finance, financekit) are not registered in this cloud sandbox. Tier-2 Finviz fallback returned Cloudflare 403. Tier-3/4 not attempted per zero-fallback policy."
mcp_errors: 4
data_lag: "T+1 (latest available close = Fri 2026-10-16)"
---

# Daily Sweep Summary — 2026-10-19 (Mon)

## Top 4 bullets (for 07:37 ET pre-market brief)

1. **Regime:** mixed-breadth, VIX 18.5, no size cut, no late-cycle flag. S&P 500 last close 7,659.44 (−1.09 % Fri). 68 % > 20-DMA, 45 % > 50-DMA, 52 % > 200-DMA.
2. **Tier-A names:** **none** — degraded run, no stylist data. Pre-market leaders / laggers captured in `daily-sweep.md` (AAME/IRON/XLAB up; SKDD/SNDQ/SOXS down).
3. **Parabolic short / long candidates:** **none** — degraded run. Sector skew (XLK −6.3 % / SOXX −12.7 % since 10/06) suggests mean-reversion candidates in semis, but per-name list not available without shibui.
4. **3:55 PM reversal-bullish:** not produced this cron (separate reversal-bullish cron; this is the 18:30 daily-sweep).

## Files in this directory

| File | Status |
|---|---|
| `daily-sweep.md` | full degraded sweep narrative + tables |
| `_regime.json` | breadth / VIX / sector-rotation payload |
| `_summary.md` | this file |
| `stockbee.md`, `qullamaggie.md`, `jeff-sun.md`, `ariel-hernandez.md`, `peoplewish.md` | stub files (degraded) |
| `short-candidates.md`, `long-reversal-candidates.md` | stub (degraded) |
| `ipo.md`, `high-short-float.md` | stub (degraded; weekly refresh anyway) |
| `master.md`, `stalk.md`, `focus.md`, `tier-a.md` | empty (no stylist input rows) |

## What downstream should do

- Pre-market brief (07:37 ET): use the regime table + pre-market mover list from `daily-sweep.md` instead of the usual Tier-A names. Note `degraded=true` in the brief header.
- Weekly recap (Sun 17:47 ET): will rerun with hopefully-working MCPs and overwrite this directory.
- Setup-journal: no entries generated (no candidates).

## Cron timing note

Intended fire 18:30 ET. Actual fire 07:32 ET — 11 hours early. Window flags do not catch time-of-day drift in the cloud scheduler; cron ran anyway. Data shown is from prior close (Fri 10/16), not today's session.
