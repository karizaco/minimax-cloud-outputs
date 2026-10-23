#!/usr/bin/env python3
"""Cron #9 stock-screener-daily-sweep — stage 1 derivation.
Source: TradingView public scanner (fallback tier 2). Session date 2026-10-22.
Every substitution away from the shibui SQL spec is recorded in data/substitutions.json
and surfaced in the artifact. No number here is invented; unavailable fields are None.
"""
import json, statistics, collections, datetime

RAW = json.load(open('data/us_raw.json'))
DATA_DATE = '2026-10-22'
CRON_DATE = '2026-10-23'

def f(x):
    return float(x) if isinstance(x, (int, float)) else None

# ---------------------------------------------------------------- prefilter
pre = []
for r in RAW:
    c, mc, av = f(r['close']), f(r['market_cap_basic']), f(r['average_volume_30d_calc'])
    if c is None or mc is None or av is None:
        continue
    if c > 3 and mc > 300_000_000 and av > 100_000 and r['exchange'] in ('NYSE', 'NASDAQ', 'AMEX'):
        pre.append(r)

def atr_pct(r):
    a, c = f(r['ATR']), f(r['close'])
    return (a / c * 100) if (a and c) else None

def adv_dollar(r):
    v, c = f(r['average_volume_30d_calc']), f(r['close'])
    return (v * c) if (v and c) else None

def prev_close(r):
    c, ch = f(r['close']), f(r['change'])
    return c / (1 + ch / 100.0) if (c and ch is not None and ch != -100) else None

def gap_pct(r):
    o, pc = f(r['open']), prev_close(r)
    return (o / pc - 1) * 100 if (o and pc) else None

for r in pre:
    r['_atr_pct'] = atr_pct(r)
    r['_adv_d'] = adv_dollar(r)
    r['_gap'] = gap_pct(r)
    r['_dist_sma200'] = ((f(r['close']) / f(r['SMA200']) - 1) * 100) if (f(r['close']) and f(r['SMA200'])) else None

atrs = sorted(x['_atr_pct'] for x in pre if x['_atr_pct'] is not None)
ATR_MED = statistics.median(atrs)
ATR_P25 = atrs[len(atrs) // 4] if atrs else None

def order(rows, key, desc=True, n=None):
    r = [x for x in rows if x.get(key) is not None]
    r.sort(key=lambda x: x[key], reverse=desc)
    return r[:n] if n else r

# ---------------------------------------------------------------- A. Bonde 4% breakout
A = [r for r in pre if (f(r['change']) or -99) >= 4.0
     and f(r['volume']) and f(r['average_volume_10d_calc'])
     and f(r['volume']) > f(r['average_volume_10d_calc'])]

# ---------------------------------------------------------------- B. Stockbee EP9 Million
B = [r for r in pre if (f(r['volume']) or 0) >= 8_900_000 and (f(r['close']) or 0) >= 3]
for r in B:
    h, l, c, o = f(r['high']), f(r['low']), f(r['close']), f(r['open'])
    r['_range_pct'] = (h - l) / c * 100 if (h and l and c) else None
    r['_dcr_pct'] = (c - l) / (h - l) * 100 if (h and l and c and h > l) else None

# ---------------------------------------------------------------- C. Qullamagi RS leaders
def stack(r):
    s50, s150, s200 = f(r['SMA50']), f(r['SMA150']), f(r['SMA200'])
    return bool(s50 and s150 and s200 and s50 > s150 > s200)
C = [r for r in pre
     if ((f(r['Perf.1M']) or -99) >= 25 or (f(r['Perf.3M']) or -99) >= 50 or (f(r['Perf.6M']) or -99) >= 150)
     and (r['_atr_pct'] or 0) >= 4.5
     and (r['_adv_d'] or 0) >= 20_000_000
     and (f(r['close']) or 0) > (f(r['SMA200']) or 1e9)
     and stack(r)]

# ---------------------------------------------------------------- D. Qullamagi EP (10%+ gap)
D = [r for r in pre if (r['_gap'] or -99) >= 10.0
     and (f(r['relative_volume_10d_calc']) or 0) >= 10
     and (r['_adv_d'] or 0) >= 50_000_000]

# ---------------------------------------------------------------- E/F. parabolic short / long
E = [r for r in pre if (f(r['Perf.5D']) or -99) >= 25.0
     and (r['_adv_d'] or 0) >= 50_000_000 and (r['_atr_pct'] or 0) >= 5.0]
Fv = [r for r in pre if -50.0 <= (f(r['Perf.5D']) or 0) <= -25.0
      and (r['_adv_d'] or 0) >= 50_000_000 and abs(r['_dist_sma200'] or 99) < 25]

# ---------------------------------------------------------------- G. peoplewish
ACCOUNT = 50000
VWOL_LO = ACCOUNT * 10           # 500k, peoplewish lower bound
G = [r for r in pre if (r['_atr_pct'] or 0) >= 5.0 and (r['_adv_d'] or 0) >= VWOL_LO]

# ---------------------------------------------------------------- H. Jeff Sun CANSLIM
H = [r for r in pre if (f(r['market_cap_basic']) or 0) > 1_000_000_000
     and (f(r['earnings_per_share_diluted_yoy_growth_ttm']) or -999) > 25
     and (f(r['close']) or 0) > 5 and (f(r['change']) or -99) > 0
     and (f(r['RSI']) or -99) <= 80 and (f(r['RSI']) or 999) >= 40]

# ---------------------------------------------------------------- J. Sun compression (PROXY)
J = [r for r in pre if r['_atr_pct'] is not None and ATR_P25 is not None
     and r['_atr_pct'] <= ATR_P25 and (f(r['Perf.3M']) or -99) > 0]

# ---------------------------------------------------------------- K. Bonde anticipation coil (PROXY)
K = []
for r in pre:
    ti, bw, cl = r['_dist_sma200'], None, None
    h1, l1, h3, l3, c = f(r['High.1M']), f(r['Low.1M']), f(r['High.3M']), f(r['Low.3M']), f(r['close'])
    s50, s20 = f(r['SMA50']), f(r['SMA20'])
    if not (h1 and l1 and h1 > l1 and c and s50 and s20):
        continue
    base_w = (h1 - l1) / c * 100
    loc = (c - l1) / (h1 - l1) * 100
    trend_int = (c / s50 - 1) * 100          # PROXY for avg(close,7)/avg(close,65)
    if trend_int >= 5.0 and base_w <= 8.0 and loc >= 50.0 and (f(r['change']) or 99) < 4.0:
        r['_trend_int'] = trend_int; r['_base_w'] = base_w; r['_loc'] = loc
        K.append(r)

# ---------------------------------------------------------------- L. Bonde reversal-bullish (partial)
L = []
for r in pre:
    h, l, c, o = f(r['high']), f(r['low']), f(r['close']), f(r['open'])
    mc, s20 = f(r['market_cap_basic']), f(r['SMA20'])
    if not (h and l and c and o and h > l and mc and s20):
        continue
    rng = h - l
    dcr = (c - l) / rng
    body = abs(c - o)
    tail = (min(o, c) - l)
    if dcr < 0.5 or body / rng > 0.4 or tail < 3 * body or c < 15.0:
        continue
    if c < s20 * 0.92:                       # filter 8, SMA20 proxy for close_20d_ago
        continue
    r['_dcr'], r['_body_ratio'], r['_tail_body'] = dcr, body / rng, (tail / body if body else None)
    L.append(r)

# ---------------------------------------------------------------- I. Hernandez theme -> group
grp = collections.defaultdict(list)
for r in pre:
    if r['sector'] and r['sector'] != 'Other':
        grp[('sector', r['sector'])].append(r)
    if r['industry'] and r['industry'] != 'Other':
        grp[('industry', r['industry'])].append(r)

themes = []
for (kind, name), rs in grp.items():
    if len(rs) < 15:
        continue
    def med(col):
        v = [f(x[col]) for x in rs if f(x[col]) is not None]
        return statistics.median(v) if v else None
    p1, p3, p6 = med('Perf.1M'), med('Perf.3M'), med('Perf.6M')
    if None in (p1, p3, p6):
        continue
    themes.append({'kind': kind, 'name': name, 'n': len(rs), 'perf_1m': p1,
                   'perf_3m': p3, 'perf_6m': p6, 'composite': round(p1 + p3 + p6, 2),
                   'day_med': statistics.median([f(x['change']) or 0 for x in rs])})
themes.sort(key=lambda x: x['composite'], reverse=True)
sector_day = sorted([t for t in themes if t['kind'] == 'sector'], key=lambda x: x['day_med'], reverse=True)

# ---------------------------------------------------------------- breadth
def breadth(denom):
    n = sum(1 for r in denom if (f(r['close']) or 0) > (f(r['SMA20']) or 1e9))
    return round(100.0 * n / len(denom), 1) if denom else None
spx_proxy = [r for r in pre if (f(r['market_cap_basic']) or 0) > 10_000_000_000]
B_SPX = breadth(spx_proxy)
B_ALL = breadth(pre)

# ---------------------------------------------------------------- skip-rule flags
for r in pre:
    r['_atr_shrink'] = bool(r['_atr_pct'] is not None and r['_atr_pct'] < 0.6 * ATR_MED)
    r['_wicky'] = bool((f(r['change']) or 0) >= 4.0 and (f(r['relative_volume_10d_calc']) or 9) < 1.2)

def slim(rs, n=None):
    out = []
    for r in (rs[:n] if n else rs):
        out.append({k: r.get(k) for k in
            ('name', 'description', 'close', 'change', 'volume', 'market_cap_basic', 'sector',
             'industry', 'exchange', 'Perf.5D', 'Perf.1M', 'Perf.3M', 'Perf.6M', 'SMA20',
             'SMA50', 'SMA200', 'RSI', 'relative_volume_10d_calc', 'Volatility.M', 'Recommend.All',
             'earnings_per_share_diluted_yoy_growth_ttm', '_atr_pct', '_adv_d', '_gap',
             '_dist_sma200', '_range_pct', '_dcr_pct', '_dcr', '_body_ratio', '_tail_body',
             '_trend_int', '_base_w', '_loc', '_atr_shrink', '_wicky')})
    return out

res = {
    'data_date': DATA_DATE, 'cron_date': CRON_DATE,
    'universe_raw': len(RAW), 'universe_prefilter': len(pre),
    'atr_median_pct': round(ATR_MED, 3), 'atr_p25_pct': round(ATR_P25, 3) if ATR_P25 else None,
    'A_bonde_4pct': order([dict(r, _sort=f(r['change'])) for r in A], '_sort', n=60),
    'B_ep9m': order([dict(r, _sort=f(r['volume'])) for r in B], '_sort', n=40),
    'C_rs_leaders': order([dict(r, _sort=f(r['Perf.3M'])) for r in C], '_sort', n=40),
    'D_ep_gap': order([dict(r, _sort=r['_gap']) for r in D], '_sort', n=25),
    'E_parabolic_short': order([dict(r, _sort=f(r['Perf.5D'])) for r in E], '_sort', n=30),
    'F_parabolic_long': order([dict(r, _sort=f(r['Perf.5D'])) for r in Fv], '_sort', False, n=30),
    'G_peoplewish': order([dict(r, _sort=f(r['Perf.1M'])) for r in G], '_sort', n=40),
    'H_jeff_sun': order([dict(r, _sort=f(r['earnings_per_share_diluted_yoy_growth_ttm'])) for r in H], '_sort', n=40),
    'J_compression': order([dict(r, _sort=r['_atr_pct']) for r in J], '_sort', n=40),
    'K_anticipation': order([dict(r, _sort=r['_trend_int']) for r in K], '_sort', n=30),
    'L_reversal_partial': order([dict(r, _sort=r['_dcr']) for r in L], '_sort', n=25),
    'themes_top': themes[:14],
    'sector_day': sector_day,
    'breadth_spx_proxy': B_SPX, 'breadth_all': B_ALL,
    'breadth_denoms': {'spx_proxy_mcap_gt_10b': len(spx_proxy), 'all_prefilter': len(pre)},
}
json.dump({k: (v if not isinstance(v, list) else len(v)) for k, v in res.items() if k.startswith(('A_', 'B_', 'C_', 'D_', 'E_', 'F_', 'G_', 'H_', 'J_', 'K_', 'L_'))},
          open('data/counts.json', 'w'), indent=1)
json.dump(res, open('data/derived.json', 'w'), default=str)
json.dump(pre, open('data/universe.json', 'w'))   # enriched universe (carries _atr_pct, _atr_shrink, _wicky, _gap)

sub = {
  'source': 'tradingview_public_scanner (skill fallback tier 2)',
  'session_date': DATA_DATE,
  'mcp_primary_unavailable': ['mcp__shibui-finance__stock_data_query', 'mcp__tradingview__screen_stocks',
                               'mcp__tradingview__screen_etf', 'mcp__tradingview-advanced__volume_breakout_scanner',
                               'mcp__tradingview-advanced__yahoo_price', 'mcp__financekit__sector_rotation',
                               'mcp__yahoo-finance__*'],
  'discovery_evidence': 'mcode-tools connector tools -> partial=false, provider_failures=[], 16 tools (matrix/email only); tool_search returns 0 finance hits',
  'tier3_finviz': 'HTTP 403 blocked',
  'substitutions': {
    'ADR% (filter 4.5/5.0)': 'ATR(14)/close*100 instead of mean 20d (high-low)/close',
    'ADV$': 'average_volume_30d_calc * close',
    'volume > prev_volume (Bonde A)': 'volume > average_volume_10d_calc',
    'adr_pct 20d (Bonde RB filter 6)': 'not evaluated in stage 1; see RB verification pass',
    'RB filter 1 (5-day low) / 5 (2-3 day decline)': 'require price history -> Yahoo 3mo pass on candidates only',
    'RB filter 8 (close vs close_20d_ago)': 'close >= SMA20*0.92 proxy',
    'Sun J contraction_ratio < 0.6': 'NOT COMPUTABLE (needs range history); PROXY = ATR% in bottom quartile & Perf.3M>0',
    'Bonde K avg(close,7)/avg(close,65)': 'PROXY = (close/SMA50 - 1)',
    'Bonde K 10-day base': 'PROXY = 1-month base (High.1M-Low.1M)/close',
    'Jeff Sun sales_growth_quarterly_yoy > 25': 'DROPPED (column null on this source)',
    'Jeff Sun earnings_growth_quarterly_yoy > 25': 'SUBSTITUTED by earnings_per_share_diluted_yoy_growth_ttm (TTM not quarterly)',
    'velocity_14d (peoplewish)': 'SUBSTITUTED by Perf.1M (calendar month not 14 sessions)',
    ' Hernandez ETF RS': 'equal-weight median constituent Perf.1M/3M/6M per sector+industry group',
    'SPX breadth': 'mcap > $10B proxy per skill (no constituents table)',
    'skip-rule day2_no_follow / ma_shrink_5d': 'NOT COMPUTABLE (needs 2+ day range history)',
  },
  'unavailable_fields': ['^VXV and ^VXVCLS both unavailable on Yahoo (0 bars) -> uncertainty flag NOT set'],
}
json.dump(sub, open('data/substitutions.json', 'w'), indent=1)
print(json.dumps(json.load(open('data/counts.json')), indent=1))
print('breadth spx_proxy%:', B_SPX, 'all%:', B_ALL)
print('top themes:', [(t['kind'], t['name'], t['composite']) for t in themes[:5]])