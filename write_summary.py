#!/usr/bin/env python3
"""Writes _summary.md + daily-sweep.md (the cron deliverable) + catalysts.md."""
import json, os, datetime

CRON_DATE, DATA_DATE = '2026-10-23', '2026-10-22'
OUT = f'daily-screens/{CRON_DATE}'
D = json.load(open('data/derived.json'))
RB = json.load(open('data/reversal_bullish.json'))
REG = json.load(open('data/regime.json'))
T = json.load(open('data/tiers.json'))
STAMP = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
DEG = open('data/_degradation.md').read().split('-->\n', 1)[1]

tierA = T['tier_a'][0] if T['tier_a'] else None
rbp = RB['passed'][0] if RB['passed'] else None
sec = {t['name']: t for t in D['sector_day']}

CATALYSTS = [
 ('XLAB', 'Exascale Labs Holdings', '+73.16%',
  'An $8.2M contract to supply NVIDIA HGX B300 GPU servers to Sunon, disclosed in an 8-K on 2026-10-15 and '
  'confirmed by a follow-up filing. Against ~$7.0M trailing revenue it is a step-change order, but the news is '
  '**a week old** — the 10/22 move is continuation, not a fresh catalyst. Balance sheet carries negative equity '
  'and large current liabilities; short interest 518,598 shares, 1.0 day to cover, so the squeeze is minor. '
  'Sources: StockSetups 2026-10-22 close scan, StocksToTrade 10/22.'),
 ('MRNA', 'Moderna, Inc.', '−17.57%',
  'Phase 3 INTerpath-001 results for intismeran autogene (personalised mRNA melanoma vaccine) with Merck\'s '
  'Keytruda leaked early via Oncology Central and were pulled, ahead of the 10/24 ESMO presentation. Merck then '
  'confirmed: 42% lower risk of recurrence or death, 38% lower risk of spread or death; 82.2% of combination '
  'patients alive and cancer-free at 2 years vs 70.0% for Keytruda alone, n=1,137. The data were **positive** and '
  'the stock fell anyway — Bernstein calls it a "sell the news" event and kept Market Perform / $45. '
  'Price and percentage confirmed to the cent against Yahoo Finance\'s 10/22 close. Sources: Yahoo Finance, '
  'Investing.com, MarketWatch via Yahoo.'),
]

cat_md = [f'# Catalyst notes — {DATA_DATE}\n',
  'Qualitative attribution for the highest-signal names. Sourced from web research, **not** from the screening '
  'pipeline; each claim carries its source. Prices cross-checked against the screening source.\n']
for sym, name, pct, text in CATALYSTS:
    cat_md.append(f'## {sym} — {name} ({pct})\n\n{text}\n\n')
cat_md.append(f'## Session context — {DATA_DATE}\n\n'
  'The S&P 500 fell 1.21% on the session (source: Yahoo Finance live blog, 10/22). The decline was tech-led: '
  'XLK "plummeted" on AI-trade worries following Tesla (−3%, better-than-expected Q3) and Meta earnings. '
  'This matches the sector medians computed independently in `ariel-hernandez.md` — Electronic Technology '
  f'{sec["Electronic Technology"]["day_med"]:+.2f}% and Non-Energy Minerals {sec["Non-Energy Minerals"]["day_med"]:+.2f}% '
  'were the two weakest sectors, while Consumer Durables '
  f'{sec["Consumer Durables"]["day_med"]:+.2f}%, Consumer Non-Durables {sec["Consumer Non-Durables"]["day_med"]:+.2f}% '
  f'and Utilities {sec["Utilities"]["day_med"]:+.2f}% led — a clear risk-off rotation into defensives.\n')
open(f'{OUT}/catalysts.md', 'w').write(
  f'<!-- cron #9 | cron_date={CRON_DATE} | data_date={DATA_DATE} | generated={STAMP} -->\n' + ''.join(cat_md))

C = D['A_bonde_4pct'][0]['name'] if D['A_bonde_4pct'] else '—'
summary = f"""<!-- cron #9 | cron_date={CRON_DATE} | data_date={DATA_DATE} | generated={STAMP} -->
# Daily screen summary — {DATA_DATE} (cron fired {CRON_DATE})

- **Regime:** risk-off session. Breadth **{REG['breadth_pct_above_sma20_spx_proxy']}%** above the 20-DMA
  ({REG['breadth_denominator_note']}), VIX **{REG['vix']}** (settled {REG['vix_bar_date']}), S&P 500 −1.21%.
  4 of 5 indices sit below their 20-DMA (SPY, QQQ, QQQE, IWM) yet breadth is healthy — narrow index damage, broad
  participation. `late_cycle={REG['late_cycle']}`, `size_cut_pct={REG['size_cut_pct']}` (breadth ≥ 40% blocks it),
  `uncertainty={REG['uncertainty']}` (**not computable** — VXV unavailable).
- **Tier-A (≥4 screens):** **{tierA['symbol']}** — {tierA['name']}, ${tierA['close']}, {tierA['change_pct']:+}% on
  {tierA['n_flags']} independent screens ({tierA['stylist_flags'].replace(';', ', ')}). ADR% {tierA['adr_pct_atr']}.
  Catalyst in `catalysts.md`: a week-old $8.2M NVIDIA/Sunon 8-K, not fresh news.
- **Parabolic short / long:** **{len(D['E_parabolic_short'])} short candidates**, **{len(D['F_parabolic_long'])} long
  candidates.** Both small-number screens are near-empty because the tape is one-directional; see
  `short-candidates.md` / `long-reversal-candidates.md`.
- **3:55 PM reversal-bullish:** **{rbp['symbol']}** — {rbp['name']}, close ${rbp['close']}, DCR {rbp['dcr']},
  tail/body {rbp['tail_body']}, ADR20 {rbp['adr20_pct']}%, body-low stop ${rbp['body_low_stop']} ({rbp['stop_pct']}%).
  **1 of 25** stage-1 candidates passed all eight of Bonde's criteria.

## Screen yield

| Screen | Stylist | Hits |
| --- | --- | ---: |
| A. 4% breakout | Bonde | {len(D['A_bonde_4pct'])} |
| B. EP9 Million | Bonde | {len(D['B_ep9m'])} |
| K. Anticipation (coil, proxy) | Bonde | {len(D['K_anticipation'])} |
| C. Multi-timeframe RS | Kullamägi | {len(D['C_rs_leaders'])} |
| D. EP 10%+ gap | Kullamägi | {len(D['D_ep_gap'])} |
| E. Parabolic short | Kullamägi | {len(D['E_parabolic_short'])} |
| F. Parabolic long | Kullamägi | {len(D['F_parabolic_long'])} |
| H. CANSLIM | Sun | {len(D['H_jeff_sun'])} |
| J. Compression (proxy) | Sun | {len(D['J_compression'])} |
| G. ADR + velocity | peoplewish | {len(D['G_peoplewish'])} |
| L. Reversal bullish (8/8) | Bonde | {len(RB['passed'])} of {RB['n_stage1']} |

Universe: {D['universe_raw']:,} raw → **{D['universe_prefilter']:,}** after the pre-filter
(close>$3, mcap>$300M, 30d avg vol>100k, NYSE/NASDAQ/AMEX). Tiers: master {len(T['master'])},
stalk {len(T['stalk'])}, focus {len(T['focus'])}, tier-a {len(T['tier_a'])}.

## Empty screens — read these before assuming a bug

- **D. EP (10%+ gap) = 0.** Only three names in the entire {D['universe_prefilter']:,}-name universe opened ≥10%
  above the prior close (BHVN +37.0%, XLAB +17.6%, AVEX +13.2%); none cleared the ≥10× RVOL **and** ≥$50M ADV gates.
- **F. Parabolic long = 0.** 38 names fell ≥25% over five sessions, but every liquid one is 30–42% *below* its
  200-DMA (TTMI −42%, CRS −34%). The screen requires a pullback that is still near the 200-DMA; there were none.
{DEG}"""
open(f'{OUT}/_summary.md', 'w').write(summary)

sweep = f"""<!-- cron #9 stock-screener-daily-sweep-18:30 | cron_date={CRON_DATE} | data_date={DATA_DATE} | generated={STAMP} -->
# Daily stock screener sweep — {CRON_DATE}

**Run status: DEGRADED.** The skill's entire primary tier (shibui-finance, tradingview, tradingview-advanced,
financekit, yahoo-finance MCP servers) is **not connected in this Cloud session**. Verified, not assumed:
`mcode-tools connector tools` returns `partial=false, provider_failures=[]` with a 16-tool catalog containing only
`matrix` (multimodal) and `email_workbench`; `tool_search` returns zero finance hits for `shibui`, `tradingview`,
`stock`, and `finance`. Per the zero-fallback policy the chain terminated at **tier 2 (TradingView public screener)**
and stopped — no deeper MCP chaining, no retry loop.

- **Data date is {DATA_DATE}, not {CRON_DATE}.** The cron fired 07:30 ET, roughly two hours *before* the US open,
  so the newest settled session is Thursday 2026-10-22. Treated as the skill's T+1 case: files land in
  `daily-screens/{CRON_DATE}/` per the cron contract, and the lag is recorded in every file header.
- **Source verified, not trusted.** TradingView closes were matched against Yahoo's 2026-10-22 regular-session
  close on 8/8 spot-checked names (NVDA, AAPL, MSFT, GOOGL, AMD, TSLA, PLTR, SMCI) — exact to the cent on all eight.
  Finviz (tier 3) returned HTTP 403 and was not used.
- **All numbers carry a row count.** {D['universe_raw']:,} symbols scanned, 0 duplicates, {D['universe_prefilter']:,}
  after the pre-filter.

## Headline

Risk-off Thursday. S&P 500 −1.21%, XLK-led tech selloff, defensives bid (Consumer Durables
{sec['Consumer Durables']['day_med']:+.2f}%, Utilities {sec['Utilities']['day_med']:+.2f}% median constituent day;
Electronic Technology {sec['Electronic Technology']['day_med']:+.2f}%, Non-Energy Minerals
{sec['Non-Energy Minerals']['day_med']:+.2f}%). Breadth stayed constructive at
**{REG['breadth_pct_above_sma20_spx_proxy']}%** above the 20-DMA and VIX finished at **{REG['vix']}** — index damage
without breadth damage.

**Tier-A: {tierA['symbol']}** ({tierA['name']}, ${tierA['close']}, {tierA['change_pct']:+}%) on
{tierA['n_flags']} screens. **Reversal-bullish: {rbp['symbol']}** ({rbp['name']}, ${rbp['close']}) — the only name
passing all eight of Bonde's published criteria, out of 25 that cleared the five screenable filters.

## Files in this directory

| File | Contents |
| --- | --- |
| `daily-sweep.md` | this report |
| `_summary.md` | machine-read digest (pre-market brief reads this) |
| `_regime.json` | regime payload: size_cut / uncertainty / late_cycle |
| `_source-health.json` | every substitution and unavailable field, machine-read |
| `stockbee.md` / `.csv` | Bonde — 4% breakout, EP9M, anticipation coil |
| `qullamaggie.md` / `.csv` | Kullamägi — RS leaders, EP gap, parabolic short/long |
| `jeff-sun.md` / `.csv` | Sun — CANSLIM, compression |
| `ariel-hernandez.md` / `.csv` | Hernandez — theme→group funnel, sector rotation, skip-rule flags |
| `peoplewish.md` / `.csv` | peoplewish — ADR + dollar volume + velocity |
| `short-candidates.md` | parabolic short |
| `long-reversal-candidates.md` | parabolic long |
| `reversal-bullish-3:55.md` / `.csv` | Bonde 8-criteria reversal bullish + full reject funnel |
| `master.md` / `.csv` | deduped union (capped 200) |
| `stalk.md` / `.csv` | master ∩ near 20/50-DMA |
| `focus.md` / `.csv` | master ∩ ≥3 screens or top-5 velocity |
| `tier-a.md` / `.csv` | master ∩ ≥4 screens |
| `breadth.md` | breadth + regime detail |
| `catalysts.md` | sourced catalyst attribution for the highest-signal names |

## Not produced, and why

- `ipo.md` and `high-short-float.md` — **Sundays only** per the skill. Today is a Friday.
- `uncertainty` regime flag — `^VXV` and `^VXVCLS` both return zero bars from Yahoo. A VIX/VXV ratio needs both
  legs; the field is `null` in `_regime.json`, not guessed.
- Sun's VCP `contraction_ratio` — needs per-session range history that the screener does not carry. Substituted
  with a clearly-labelled volatility proxy, not presented as the published screen.
- Jeff Sun's `sales_growth_quarterly_yoy > 25` filter — column is null on this source; the filter is **dropped**,
  which makes the CANSLIM screen looser than published. `earnings_growth_quarterly_yoy` is substituted by TTM
  EPS growth. Both substitutions are logged in `_source-health.json`.

## Live-only steps not run

The sweep is a screening procedure. Steps 6 (pre-market gapper, 09:00 ET), 7 (intraday RVOL re-rank, 09:45–11:15 ET)
and the reversal-bullish entry window (15:30–16:00 ET) are all either outside this fire time or require a live
feed. `reversal-bullish-3:55.md` is computed on the {DATA_DATE} settled close, so it is valid for next-session
execution, not for an entry that has already passed.
{DEG}"""
open(f'{OUT}/daily-sweep.md', 'w').write(sweep)
print('wrote daily-sweep.md, _summary.md, catalysts.md')
for f in sorted(os.listdir(OUT)): print(' ', f)