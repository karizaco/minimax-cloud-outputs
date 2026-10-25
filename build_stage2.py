#!/usr/bin/env python3
"""Cron #9 — final tiering, regime, and artifact writer.
Directory: /workspace/daily-screens/2026-10-23/  (cron_date)
Data date : 2026-10-22 (settled close; cron fired 07:30 ET pre-open)
"""
import json, os, csv, statistics, datetime, subprocess, urllib.parse

CA = '/etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
CRON_DATE, DATA_DATE = '2026-10-23', '2026-10-22'
OUT = f'daily-screens/{CRON_DATE}'
os.makedirs(OUT, exist_ok=True)

D = json.load(open('data/derived.json'))
SUB = json.load(open('data/substitutions.json'))
RB = json.load(open('data/reversal_bullish.json'))

def f(x):
    try: return float(x)
    except (TypeError, ValueError): return None

# ---------------------------------------------------------------- regime
def hist(sym, rng='1y'):
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?range={rng}&interval=1d'
    p = subprocess.run(['curl', '-s', '--max-time', '35', '--cacert', CA, '-H', f'User-Agent: {UA}', url],
                       capture_output=True, text=True)
    try:
        r = json.loads(p.stdout)['chart']['result'][0]
        q = r['indicators']['quote'][0]
        # Drop any bar dated AFTER the sweep session date. ^VIX (and other near-24h symbols)
        # carry an in-progress overnight bar at a pre-open cron fire; that is not a settled close.
        keep = [i for i, t in enumerate(r['timestamp'])
                if (datetime.datetime.utcfromtimestamp(t) - datetime.timedelta(hours=4)).strftime('%Y-%m-%d') <= DATA_DATE]
        if not keep:
            return None
        n = keep[-1] + 1
        return {'c': [x for x in q['close'][:n] if x is not None],
                'h': [x for x in q['high'][:n] if x is not None],
                'l': [x for x in q['low'][:n] if x is not None],
                'last_bar': (datetime.datetime.utcfromtimestamp(r['timestamp'][n - 1]) - datetime.timedelta(hours=4)).strftime('%Y-%m-%d')}
    except Exception:
        return None

idx = {}
for s in ['SPY', 'RSP', 'QQQ', 'QQQE', 'IWM']:
    h = hist(s)
    if not h or len(h['c']) < 60:
        idx[s] = None; continue
    c, hh, ll = h['c'], h['h'], h['l']
    trs = [max(hh[i] - ll[i], abs(hh[i] - c[i-1]), abs(ll[i] - c[i-1])) for i in range(1, len(c))]
    atr14 = statistics.mean(trs[-14:])
    # ATR% series aligned to closes, median over trailing 252 sessions
    apct = []
    for i in range(14, len(c)):
        w = trs[i - 13:i + 1]
        apct.append(statistics.mean(w) / c[i] * 100)
    med = statistics.median(apct[-252:]) if len(apct) >= 60 else None
    idx[s] = {'close': round(c[-1], 2), 'sma20': round(statistics.mean(c[-20:]), 2),
              'sma50': round(statistics.mean(c[-50:]), 2),
              'ext_from_50_pct': round((c[-1] / statistics.mean(c[-50:]) - 1) * 100, 2),
              'atr_pct': round(atr14 / c[-1] * 100, 2),
              'atr_x_median': round((atr14 / c[-1] * 100) / med, 2) if med else None,
              'bars': len(c)}

vixh = hist('^VIX', '1y')
vix = round(vixh['c'][-1], 2) if vixh else None
vix_bar_date = vixh.get('last_bar') if vixh else None
print(f'VIX settled close (bar {vix_bar_date}): {vix}')
vxv = None   # ^VXV and ^VXVCLS both return 0 bars -> NOT computed, do not invent

breadth = D['breadth_spx_proxy']
below20 = [s for s, v in idx.items() if v and v['close'] < v['sma20']]
size_cut = bool(below20) and breadth < 40
late_cycle = bool([s for s, v in idx.items() if v and (v['atr_x_median'] or 0) > 6])
regime = {
    'cron_date': CRON_DATE, 'data_date': DATA_DATE,
    'size_cut_pct': 50 if size_cut else None,
    'uncertainty': None,
    'uncertainty_note': 'NOT COMPUTED — ^VXV and ^VXVCLS both return 0 bars from Yahoo; VIX/VXV ratio requires both legs.',
    'late_cycle': late_cycle,
    'vix': vix, 'vix_bar_date': vix_bar_date, 'vxv': None,
    'breadth_pct_above_sma20_spx_proxy': breadth,
    'breadth_denominator_note': f"mcap > $10B proxy ({D['breadth_denoms']['spx_proxy_mcap_gt_10b']} names); no SPX constituents table on this source",
    'indices_below_sma20': below20,
    'index_detail': idx,
}
json.dump(regime, open('data/regime.json', 'w'), indent=1)

# ---------------------------------------------------------------- stylist flags
SCREENS = {
    'A_bonde_4pct': 'bonde_4pct', 'B_ep9m': 'bonde_ep9m', 'K_anticipation': 'bonde_coil',
    'C_rs_leaders': 'qull_rs', 'D_ep_gap': 'qull_ep', 'E_parabolic_short': 'qull_parabolic_short',
    'F_parabolic_long': 'qull_parabolic_long',
    'H_jeff_sun': 'sun_canslim', 'J_compression': 'sun_vcp',
    'G_peoplewish': 'peoplewish_adr_velocity',
}
flags = {}
def add(sym, flag):
    flags.setdefault(sym, {'symbol': sym, 'flags': []})['flags'].append(flag)

for key, flag in SCREENS.items():
    for r in D[key]:
        add(r['name'], flag)

# reversal-bullish passes are an independent signal -> counted as its own stylist flag
for r in RB['passed']:
    add(r['symbol'], 'bonde_reversal_bullish')

uni = {r['name']: r for r in D['themes_top']}  # unused placeholder, keep universe lookup below
UNI = {r['name']: r for r in json.load(open('data/universe.json'))}   # enriched: _atr_pct/_atr_shrink/_wicky present
for r in RB['passed']:
    if r['symbol'] in UNI:
        UNI[r['symbol']]['_rb_pass'] = True

def near_ma(r):
    """Stalk: within 2% of 20-DMA or 50-DMA. SMA10 is not a column on this source."""
    c = f(r.get('close'))
    out = []
    for k in ('SMA20', 'SMA50'):
        v = f(r.get(k))
        if c and v and v > 0 and abs(c / v - 1) * 100 <= 2.0:
            out.append(k)
    return out

velocity_rank = {r['name']: i for i, r in enumerate(D['G_peoplewish'][:5])}

master = []
for sym, rec in flags.items():
    r = UNI.get(sym, {})
    fl = sorted(set(rec['flags']))
    row = {
        'symbol': sym, 'name': r.get('description'), 'close': f(r.get('close')),
        'change_pct': round(f(r.get('change')), 2) if f(r.get('change')) is not None else None,
        'volume': r.get('volume'),
        'avg_vol_30d': r.get('average_volume_30d_calc'),
        'rvol_10d': round(f(r.get('relative_volume_10d_calc')), 2) if f(r.get('relative_volume_10d_calc')) else None,
        'market_cap_m': round((f(r.get('market_cap_basic')) or 0) / 1e6, 1) or None,
        'adr_pct_atr': round(f(r['_atr_pct']), 2) if r.get('_atr_pct') else None,
        'perf_5d': round(f(r.get('Perf.5D')), 2) if f(r.get('Perf.5D')) is not None else None,
        'perf_1m': round(f(r.get('Perf.1M')), 2) if f(r.get('Perf.1M')) is not None else None,
        'perf_3m': round(f(r.get('Perf.3M')), 2) if f(r.get('Perf.3M')) is not None else None,
        'sector': r.get('sector'), 'industry': r.get('industry'), 'exchange': r.get('exchange'),
        'rsi': round(f(r.get('RSI')), 1) if f(r.get('RSI')) is not None else None,
        'sma20': round(f(r.get('SMA20')), 2) if f(r.get('SMA20')) else None,
        'sma50': round(f(r.get('SMA50')), 2) if f(r.get('SMA50')) else None,
        'eps_growth_ttm_yoy': round(f(r.get('earnings_per_share_diluted_yoy_growth_ttm')), 1)
                               if r.get('earnings_per_share_diluted_yoy_growth_ttm') is not None else None,
        'stylist_flags': ';'.join(fl), 'n_flags': len(fl),
        'near_ma': ';'.join(near_ma(r)) if r else '',
        'atr_shrink': bool(r.get('_atr_shrink')), 'wicky_breakout': bool(r.get('_wicky')),
        'reversal_bullish_pass': bool(r.get('_rb_pass')),
    }
    master.append(row)
master.sort(key=lambda x: (-x['n_flags'], -(x['change_pct'] or -99)))
master = master[:200]
print('master:', len(master), 'max flags:', max(x['n_flags'] for x in master))

stalk = [x for x in master if x['near_ma']]
focus = [x for x in master if x['n_flags'] >= 3 or x['symbol'] in velocity_rank]
tierA = [x for x in master if x['n_flags'] >= 4]
print('stalk:', len(stalk), 'focus:', len(focus), 'tier-a:', len(tierA))
json.dump({'master': master, 'stalk': stalk, 'focus': focus, 'tier_a': tierA},
          open('data/tiers.json', 'w'), default=str)
print('tiers written')
print('TIER-A:', [(x['symbol'], x['stylist_flags']) for x in tierA])
print('FOCUS :', [(x['symbol'], x['n_flags']) for x in focus])
