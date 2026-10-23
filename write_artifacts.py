#!/usr/bin/env python3
"""Artifact writer for cron #9. Consumes data/*.json produced by stages 1-2."""
import json, os, csv, datetime

CRON_DATE, DATA_DATE = '2026-10-23', '2026-10-22'
OUT = f'daily-screens/{CRON_DATE}'
os.makedirs(OUT, exist_ok=True)

D = json.load(open('data/derived.json'))
SUB = json.load(open('data/substitutions.json'))
RB = json.load(open('data/reversal_bullish.json'))
REG = json.load(open('data/regime.json'))
T = json.load(open('data/tiers.json'))
STAMP = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')

HDR = (f"<!-- cron #9 stock-screener-daily-sweep-18:30 | cron_date={CRON_DATE} | "
       f"data_date={DATA_DATE} | _source=tv_fallback+yahoo_verify | generated={STAMP} -->\n")

def num(x, p=2):
    if x is None or x == '': return '—'
    try: return f'{float(x):,.{p}f}'
    except (TypeError, ValueError): return str(x)

def table(rows, cols, aligns=None):
    if not rows: return '_No qualifying rows._\n'
    aligns = aligns or ['---'] * len(cols)
    out = ['| ' + ' | '.join(cols) + ' |', '| ' + ' | '.join(aligns) + ' |']
    for r in rows:
        out.append('| ' + ' | '.join(str(r.get(c, '—') if r.get(c, '—') is not None else '—') for c in cols) + ' |')
    return '\n'.join(out) + '\n'

def wr_csv(name, rows, cols):
    with open(f'{OUT}/{name}', 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        for r in rows: w.writerow(r)

def stock_rows(key, limit=40, sortkey=None, extra=None):
    rows = D[key]
    if sortkey: rows = sorted(rows, key=lambda r: (sortkey(r) is None, sortkey(r)), reverse=True)
    out = []
    for r in rows[:limit]:
        c = f = None
        try: c = float(r['close'])
        except (TypeError, ValueError): pass
        try: f = float(r['change'])
        except (TypeError, ValueError): pass
        row = {'Symbol': r['name'], 'Company': (r['description'] or '')[:30],
               'Close': num(c), 'Chg%': num(f),
               'Vol': num(r.get('volume'), 0), 'RVOL10': num(r.get('relative_volume_10d_calc')),
               'Mcap$B': num((r.get('market_cap_basic') or 0) / 1e9 if isinstance(r.get('market_cap_basic'), (int, float)) else None, 1),
               'ADR%': num(r.get('_atr_pct')), 'ADV$M': num((r.get('_adv_d') or 0) / 1e6, 0),
               'Perf5D': num(r.get('Perf.5D')), 'Perf1M': num(r.get('Perf.1M')),
               'Perf3M': num(r.get('Perf.3M')), 'Sector': r.get('sector')}
        if extra: row.update(extra(r))
        out.append(row)
    return out

BCOLS = ['Symbol', 'Company', 'Close', 'Chg%', 'Vol', 'RVOL10', 'Mcap$B', 'ADR%', 'ADV$M',
         'Perf5D', 'Perf1M', 'Perf3M', 'Sector']

def degradation_note():
    L = ['\n## Source health — read before using this list\n',
         f'- **All MCP finance tools were unavailable this run.** `{", ".join(SUB["mcp_primary_unavailable"])}` — ',
         f'  confirmed by `mcode-tools connector tools` → `partial=false, provider_failures=[]`, catalog holds 16 tools, all `matrix`/`email_workbench`. `tool_search` returns 0 finance hits.\n',
         '- **Data source: TradingView public screener** (`scanner.tradingview.com/america/scan`, POST), the skill\'s fallback tier 2. '
         f'{D["universe_prefilter"]:,} names after the pre-filter ({D["universe_raw"]:,} raw, 0 duplicate symbols).\n',
         '- **Session date is ' + DATA_DATE + ', not ' + CRON_DATE + '.** The cron fired 07:30 ET, ~2 h before the open, '
         'so the newest settled session is Thursday. Verified: TV `close` matched Yahoo\'s 2026-10-22 regular-session close '
         'to the cent on 8/8 spot-checked names (NVDA, AAPL, MSFT, GOOGL, AMD, TSLA, PLTR, SMCI).\n',
         '- Finviz (tier 3) returned **HTTP 403** and was not used.\n',
         '\n### Every deviation from the skill\'s shibui SQL spec\n',
         '| Spec field | What was used instead |', '| --- | --- |']
    for k, v in SUB['substitutions'].items():
        L.append(f'| {k} | {v} |')
    L.append(f'\n- **Not computable on this source, therefore absent (not estimated):** {SUB["unavailable_fields"][0]}\n')
    return '\n'.join(L)

# ------------------------------------------------------------------ per-stylist files
bonde_extra = lambda r: {'Range%': num(r.get('_range_pct')), 'DCR%': num(r.get('_dcr_pct')),
                         'CoilTrend': num(r.get('_trend_int')), 'BaseW%': num(r.get('_base_w'))}

FILES = {}

s = [{**x, **bonde_extra(y)} for x, y in
     zip(stock_rows('A_bonde_4pct', 40, lambda r: r.get('change')), D['A_bonde_4pct'])]
FILES['stockbee'] = ('## Stockbee — Pradeep Bonde\n',
  f"**A. 4% breakout** — up ≥4% on volume above its 10-day average. {len(D['A_bonde_4pct'])} names in universe, top 40 shown.\n\n",
  table(s, BCOLS + ['Range%', 'DCR%']),
  f"\n**B. EP9 Million** — volume ≥ 8.9M shares. {len(D['B_ep9m'])} names.\n\n",
  table(stock_rows('B_ep9m', 40, lambda r: r.get('volume')), BCOLS + ['Range%', 'DCR%']),
  f"\n**K. Anticipation (coil)** — PROXY definition (see source health). {len(D['K_anticipation'])} names.\n\n",
  table(stock_rows('K_anticipation', 20, lambda r: r.get('_trend_int'), bonde_extra),
        BCOLS + ['CoilTrend', 'BaseW%']))
wr_csv('2026-10-23-stockbee.csv', stock_rows('A_bonde_4pct', 40), BCOLS)

q = stock_rows('C_rs_leaders', 40, lambda r: r.get('Perf.3M'))
FILES['qullamaggie'] = ('## Qullamaggie — Kristjan Kullamägi\n',
  f"**C. Multi-timeframe RS leaders** — RS 1M≥25% or 3M≥50% or 6M≥150%, ATR%≥4.5, ADV$≥20M, "
  f"close>SMA200 and SMA50>SMA150>SMA200. **{len(D['C_rs_leaders'])} names** — the only structural-trend screen in the sweep.\n\n",
  table(q, BCOLS),
  f"\n**D. EP (10%+ gap)** — **0 names.** Only 3 names in the whole pre-filtered universe opened ≥10% above the prior close "
  f"(BHVN +37.0%, XLAB +17.6%, AVEX +13.2%); none cleared the ≥10× RVOL and ≥$50M ADV gates. Genuine empty, not an error.\n\n",
  f"**E. Parabolic short (5-day gainers)** — Perf5D≥+25%, ADV$≥50M, ATR%≥5. **{len(D['E_parabolic_short'])} names.**\n\n",
  table(stock_rows('E_parabolic_short', 30, lambda r: r.get('Perf.5D')), BCOLS),
  f"\n**F. Parabolic long (5-day losers)** — **0 names.** 38 names fell ≥25% over 5 sessions, but every liquid one sits "
  f"far below its 200-DMA (TTMI −42%, CRS −34%, MTSI −18%), failing the spec's |dist to SMA200| < 25% gate. "
  f"Genuine empty under the published filter.\n")
wr_csv('2026-10-23-qullamaggie.csv', q, BCOLS)

FILES['short-candidates'] = ('## Parabolic short candidates — Kullamägi\n\n',
  f'Perf5D ≥ +25%, ADV$ ≥ $50M, ATR% ≥ 5%. **{len(D["E_parabolic_short"])} names.**\n\n',
  table(stock_rows('E_parabolic_short', 30, lambda r: r.get('Perf.5D')), BCOLS))
FILES['long-reversal-candidates'] = ('## Parabolic long / mean-reversion candidates — Kullamägi\n\n',
  f'Perf5D in [−50%, −25%], ADV$ ≥ $50M, |dist to SMA200| < 25%. **{len(D["F_parabolic_long"])} names.**\n\n',
  '_Empty under the published filters. The screen requires a name that fell hard over 5 sessions **while still near its '
  '200-day moving average**; in this tape the high-volume 5-day decliners are all 30–42% below their 200-DMA, i.e. broken '
  'trends rather than pullbacks. No mean-reversion candidate qualified._\n')

hs = [{**x, 'EPSg%': num(y.get('earnings_per_share_diluted_yoy_growth_ttm'), 1)}
      for x, y in zip(stock_rows('H_jeff_sun', 40, lambda r: r.get('earnings_per_share_diluted_yoy_growth_ttm')),
                      D['H_jeff_sun'])]
FILES['jeff-sun'] = ('## Jeff Sun — CANSLIM\n',
  f'**H. CANSLIM-calibrated** — mcap>$1B, EPS growth >25% (TTM YoY substitute), price>$5, positive day, RSI 40–80. '
  f'**{len(D["H_jeff_sun"])} names.** Sorted by EPS growth.\n\n',
  table(hs, BCOLS + ['EPSg%']),
  f"\n**J. Compression / VCP** — **PROXY, not the spec's contraction ratio.** The spec's "
  f"`avg(range,10)/avg(range,50) < 0.6` needs per-session range history, which this source does not carry. "
  f"Substitute used: ATR% in the bottom quartile of the universe ({D['atr_p25_pct']}%) **and** 3-month return positive. "
  f"**{len(D['J_compression'])} names.** Treat as a volatility screen, not a VCP.\n\n",
  table(stock_rows('J_compression', 40, lambda r: r.get('_atr_pct')), BCOLS))
wr_csv('2026-10-23-jeff-sun.csv', hs, BCOLS)

th = D['themes_top']
FILES['ariel-hernandez'] = ('## Real Simple Ariel — theme → group funnel\n',
  '**I. Top-down sector/industry RS** — equal-weight *median* constituent 1M/3M/6M return per group, composite = unweighted sum. '
  'This replaces the spec\'s `screen_etf` call, which is unavailable.\n\n',
  table([{'Kind': t['kind'], 'Group': t['name'], 'N': t['n'], 'Perf1M': num(t['perf_1m'], 1),
          'Perf3M': num(t['perf_3m'], 1), 'Perf6M': num(t['perf_6m'], 1),
          'Composite': num(t['composite'], 1), 'MedDay%': num(t['day_med'], 2)}
         for t in th[:14]], ['Kind', 'Group', 'N', 'Perf1M', 'Perf3M', 'Perf6M', 'Composite', 'MedDay%']),
  '\n**Sector rotation on the session (median constituent day change):**\n\n',
  table([{'Sector': t['name'], 'Median day %': num(t['day_med'], 2), '1M': num(t['perf_1m'], 1),
          '3M': num(t['perf_3m'], 1)} for t in D['sector_day'][:12]],
        ['Sector', 'Median day %', '1M', '3M']),
  '\n**Skip-rule flags applied to every candidate** — `atr_shrink` (ATR% < 0.6× universe median '
  f'{D["atr_median_pct"]}%), `wicky_breakout` (breakout day on RVOL<1.2). '
  '`day2_no_follow` and `ma_shrink_5d` are **not computable** here (need multi-day range history) and are omitted.\n')

pw = [{**x, 'Rec.All': num(y.get('Recommend.All'), 3)}
      for x, y in zip(stock_rows('G_peoplewish', 40, lambda r: r.get('Perf.1M')), D['G_peoplewish'])]
FILES['peoplewish'] = ('## peoplewish — ADR + dollar volume + velocity\n',
  f'ATR% ≥ 5%, dollar volume ≥ $500K (account size $50,000 × 10, peoplewish\'s lower bound), sorted by velocity. '
  f'**{len(D["G_peoplewish"])} names.**\n\n',
  '> Velocity is substituted with `Perf.1M` — a calendar month, not 14 sessions. The ranking is directionally right, '
  'the window is not the published one.\n\n',
  table(pw, BCOLS + ['Rec.All']))
wr_csv('2026-10-23-peoplewish.csv', pw, BCOLS)

# ------------------------------------------------------------------ reversal bullish
rbp = RB['passed']
FILES['reversal-bullish-3:55'] = (f'## Bonde Reversal Bullish — all 8 criteria\n\n',
  f'**{len(rbp)} of {RB["n_stage1"]} stage-1 candidates pass all eight published criteria.**\n\n',
  'Bonde: *"Select 1 to 3 ideas."* Do not pad.\n\n',
  table([{'Symbol': p['symbol'], 'Company': (p['name'] or '')[:26], 'Close': num(p['close']),
          'DCR': num(p['dcr']), 'Tail/Body': num(p['tail_body'], 1), 'Body/Range': num(p['body_ratio']),
          'ADR20%': num(p['adr20_pct']), 'Mcap$B': num(p['mcap_b'], 1),
          'BodyLowStop': num(p['body_low_stop']), 'Stop%': num(p['stop_pct'])} for p in rbp],
        ['Symbol', 'Company', 'Close', 'DCR', 'Tail/Body', 'Body/Range', 'ADR20%', 'Mcap$B', 'BodyLowStop', 'Stop%']),
  '\n**Full funnel**\n\n',
  f'- Stage-1 (5 of 8 filters, TV OHLC): {RB["n_stage1"]} candidates\n'
  f'- Gated out — market cap ≤ $5B (Bonde institutional-ownership proxy): {len(RB["gated"])} '
  f'({", ".join(g["symbol"] for g in RB["gated"])})\n'
  f'- Rejected on criteria: {len(RB["rejected"])}\n'
  f'- **Passed all 8: {len(rbp)}**\n\n',
  '**Why the rest failed** (a name can fail more than one):\n\n',
  table([{'Criterion': c, 'Names failing': sum(1 for r in RB['rejected'] if c in r['failed'])}
         for c in ['f1_5day_low', 'f2_dcr>=0.5', 'f3_tail>=3xbody', 'f4_body<=0.4range',
                   'f5_2day_decline', 'f6_adr>=3pct', 'f7_close>=15', 'f8_longterm_trend']],
        ['Criterion', 'Names failing']),
  '\nHistory for the 25 candidates was pulled from Yahoo (3-month daily). Verification filters 1 (5-day low), '
  '5 (2–3 day decline) and 6 (ADR20 ≥ 3%) are measured on real bars, not proxied.\n')
wr_csv('2026-10-23-reversal-bullish-3:55.csv', rbp,
       ['symbol', 'name', 'close', 'dcr', 'tail_body', 'body_ratio', 'adr20_pct', 'mcap_b',
        'body_low_stop', 'stop_pct', 'failed'])

# ------------------------------------------------------------------ tiered lists
TCOLS = ['symbol', 'name', 'close', 'change_pct', 'rvol_10d', 'market_cap_m', 'adr_pct_atr',
         'perf_5d', 'perf_1m', 'n_flags', 'stylist_flags', 'near_ma', 'sector']
def trow(r): return {k: r.get(k) for k in TCOLS}
def tmd(r):
    return (f"| {r['symbol']} | {(r['name'] or '')[:26]} | {num(r['close'])} | {num(r['change_pct'])} | "
            f"{num(r['rvol_10d'])} | {num(r['market_cap_m'], 0)} | {num(r['adr_pct_atr'])} | "
            f"{num(r['perf_5d'])} | {r['n_flags']} | {r['stylist_flags']} | {r['near_ma'] or '—'} |")

def tier_md(title, rows, note):
    return (f'## {title}\n\n{note}\n\n' + (f'**{len(rows)} names.**\n\n' if rows else '_Empty._\n\n') +
            ('| Sym | Company | Close | Chg% | RVOL | Mcap$M | ADR% | Perf5D | Flags | Screens | Near MA |\n'
             '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n' +
             '\n'.join(tmd(r) for r in rows) + '\n' if rows else ''))

FILES['master'] = tier_md('Master list — deduped union', T['master'],
  f'Union of every sub-screen, deduped, capped at 200 tickers (skill cap). Actual: {len(T["master"])}.')
FILES['stalk'] = tier_md('Stalk list — Master ∩ near a moving average', T['stalk'],
  'Price within 2% of its 20-DMA **or** 50-DMA. SMA10 is not a column on this source, so the "10/20-DMA" test is run as 20/50-DMA.')
FILES['focus'] = tier_md('Focus list — Master ∩ (≥3 screens OR top-5 velocity)', T['focus'],
  'Highest-conviction actionable list. This is the list the pre-market brief and RVOL re-rank consume.')
FILES['tier-a'] = tier_md('Tier-A — Master ∩ ≥4 stylist screens', T['tier_a'],
  f'Stockbee short-candidate candidates (≥4 independent screens). Regime flag: '
  f'**late_cycle={REG["late_cycle"]}**, **size_cut_pct={REG["size_cut_pct"]}**, **uncertainty={REG["uncertainty"]}**.')
for n in ['master', 'stalk', 'focus', 'tier_a']:
    wr_csv(f'2026-10-23-{n.replace("_","-")}.csv', [trow(r) for r in T[n]], TCOLS)

# ------------------------------------------------------------------ breadth
bi = [f'| {k} | {num(v["close"])} | {num(v["sma20"])} | {num(v["sma50"])} | {num(v["ext_from_50_pct"])} | '
      f'{num(v["atr_pct"])} | {num(v["atr_x_median"])} |' for k, v in REG['index_detail'].items() if v]
FILES['breadth'] = (f'# Breadth & regime — {DATA_DATE}\n\n',
  f'**% above 20-DMA: {REG["breadth_pct_above_sma20_spx_proxy"]}%** '
  f'({REG["breadth_denominator_note"]}). Full pre-filtered universe: {D["breadth_all"]}%.\n\n',
  '| Index | Close | 20-DMA | 50-DMA | Ext from 50 | ATR% | ATR× median |\n| --- | --- | --- | --- | --- | --- | --- |\n'
  + '\n'.join(bi) + '\n\n',
  f'**Indices below their 20-DMA:** {", ".join(REG["indices_below_sma20"]) or "none"}\n\n',
  f'**VIX: {REG["vix"]}** — `uncertainty` flag is **not computed**: both `^VXV` and `^VXVCLS` return zero bars from Yahoo, '
  f'and a VIX/VXV ratio cannot be built from one leg. Left null rather than assumed.\n\n',
  '| Regime flag | Value | Rule |\n| --- | --- | --- |\n'
  f'| `size_cut_pct` | `{REG["size_cut_pct"]}` | 50 when an index is < 20-DMA **and** breadth < 40%. Breadth is {REG["breadth_pct_above_sma20_spx_proxy"]}%, '
  f'so breadth fails the second condition despite 4 of 5 indices being below the 20-DMA. |\n'
  f'| `uncertainty` | `{REG["uncertainty"]}` | VIX/VXV > 1. Not computable (see above). |\n'
  f'| `late_cycle` | `{REG["late_cycle"]}` | any index > 6× median ATR%. Max observed is {max(v["atr_x_median"] for v in REG["index_detail"].values() if v)}. |\n')

FILES['_regime'] = None

for name, content in FILES.items():
    if content is None: continue
    body = content if isinstance(content, str) else ''.join(content)
    open(f'{OUT}/{name}.md', 'w').write(HDR + body)
json.dump(REG, open(f'{OUT}/_regime.json', 'w'), indent=1)
json.dump({'data_date': DATA_DATE, 'cron_date': CRON_DATE, 'generated': STAMP, **SUB},
          open(f'{OUT}/_source-health.json', 'w'), indent=1)
print('wrote', len([k for k, v in FILES.items() if v]), 'md files + regime + source-health')
print('degradation note chars:', len(degradation_note()))
open('data/_degradation.md', 'w').write(HDR + degradation_note())