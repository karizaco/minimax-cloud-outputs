#!/usr/bin/env python3
"""Bonde Reversal Bullish — T+1-safe + Bonde-strict verification pass.
Stage 1 could only evaluate 5 of 8 Bonde filters (needs history).
Fetches 3-month daily bars for the <=25 stage-1 candidates only, then applies:
  1. 5-day low      low <= MIN(low, last 5 sessions incl. current)
  2. DCR >= 0.5
  3. tail >= 3x body
  4. body/range <= 0.4
  5. close < close_2d_ago
  6. ADR20 = mean((high-low)/close, 20) >= 0.03
  7. close >= 15
  8. close >= close_20d_ago * 0.92
Universe: mcap > $5B (institutional-ownership proxy, per skill).
"""
import json, time, subprocess, urllib.parse, statistics, datetime

CA = '/etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
D = json.load(open('data/derived.json'))
cands = D['L_reversal_partial']
print(f'stage-1 candidates: {len(cands)}')

def fetch(sym):
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?range=3mo&interval=1d'
    p = subprocess.run(['curl', '-s', '--max-time', '30', '--cacert', CA, '-H', f'User-Agent: {UA}', url],
                       capture_output=True, text=True)
    try:
        j = json.loads(p.stdout)
        r = j['chart']['result'][0]
        q = r['indicators']['quote'][0]
        out = []
        for t, o, h, l, c, v in zip(r['timestamp'], q['open'], q['high'], q['low'], q['close'], q['volume']):
            if None in (o, h, l, c):
                continue
            out.append({'d': datetime.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d'),
                        'o': o, 'h': h, 'l': l, 'c': c, 'v': v or 0})
        return {'sym': sym, 'bars': out, 'date': out[-1]['d'] if out else None}
    except Exception:
        return {'sym': sym, 'bars': [], 'date': None, 'error': True}

hist, fails = {}, []
for c in cands:
    r = fetch(c['name'])
    hist[c['name']] = r
    if not r['bars']:
        fails.append(c['name'])
    time.sleep(0.4)

print('history failures:', fails)

passed, rejected, gated = [], [], []
for c in cands:
    h = hist[c['name']]['bars']
    mc = float(c['market_cap_basic'])
    reasons = []
    if len(h) < 25:
        reasons.append('insufficient_history')
    if mc <= 5_000_000_000:
        reasons.append('mcap<=5B_universe')
    if reasons:
        gated.append({'symbol': c['name'], 'name': c['description'],
                      'mcap_b': round(mc / 1e9, 2), 'bars': len(h),
                      'close': h[-1]['c'] if h else None, 'failed': reasons})
        continue
    if True:
        cur = h[-1]
        lo5 = min(b['l'] for b in h[-5:])
        f1 = cur['l'] <= lo5
        rng = cur['h'] - cur['l']
        f2 = (cur['c'] - cur['l']) / rng >= 0.5 if rng > 0 else False
        body = abs(cur['c'] - cur['o'])
        f3 = (min(cur['o'], cur['c']) - cur['l']) >= 3 * body
        f4 = (body / rng) <= 0.4 if rng > 0 else False
        f5 = cur['c'] < h[-3]['c']
        adr = statistics.mean((b['h'] - b['l']) / b['c'] for b in h[-20:])
        f6 = adr >= 0.03
        f7 = cur['c'] >= 15.0
        f8 = cur['c'] >= h[-21]['c'] * 0.92
        checks = {'f1_5day_low': f1, 'f2_dcr>=0.5': f2, 'f3_tail>=3xbody': f3,
                  'f4_body<=0.4range': f4, 'f5_2day_decline': f5, 'f6_adr>=3pct': f6,
                  'f7_close>=15': f7, 'f8_longterm_trend': f8}
        bad = [k for k, v in checks.items() if not v]
        row = {'symbol': c['name'], 'name': c['description'], 'close': round(cur['c'], 2),
               'open': round(cur['o'], 2), 'high': round(cur['h'], 2), 'low': round(cur['l'], 2),
               'dcr': round((cur['c'] - cur['l']) / rng, 3) if rng > 0 else None,
               'body_ratio': round(body / rng, 3) if rng > 0 else None,
               'tail_body': round((min(cur['o'], cur['c']) - cur['l']) / body, 2) if body else None,
               'adr20_pct': round(adr * 100, 2), 'mcap_b': round(mc / 1e9, 2),
               'body_low_stop': round(min(cur['o'], cur['c']), 2),
               'stop_pct': round((min(cur['o'], cur['c']) / cur['c'] - 1) * 100, 2),
               'checks': checks, 'failed': bad, 'date': hist[c['name']]['date']}
        (rejected if bad else passed).append(row)

print(f'\nPASS all 8: {len(passed)}   REJECTED: {len(rejected)}   GATED OUT (universe/history): {len(gated)}')
print('  account check:', len(passed)+len(rejected)+len(gated), 'of', len(cands))
for g in gated: print(f"   GATED {g['symbol']:6s} mcap=${g['mcap_b']}B bars={g['bars']} failed={g['failed']}")
for p in sorted(passed, key=lambda x: -x['adr20_pct']):
    print(f"  PASS {p['symbol']:6s} close={p['close']:8.2f} dcr={p['dcr']:.2f} tail={p['tail_body']} "
          f"adr20={p['adr20_pct']}% mcap=${p['mcap_b']}B stop={p['body_low_stop']} ({p['stop_pct']}%)")
print('\nreject reasons:')
cnt = {}
for r in rejected:
    for b in r['failed']:
        cnt[b] = cnt.get(b, 0) + 1
print(' ', cnt)

json.dump({'data_date': D['data_date'], 'passed': passed, 'rejected': rejected, 'gated': gated,
           'history_failures': fails, 'n_stage1': len(cands),
           'source': 'yahoo chart 3mo daily + TV scanner stage1'},
          open('data/reversal_bullish.json', 'w'), indent=1)
json.dump({k: v for k, v in hist.items()}, open('data/rb_hist.json', 'w'))