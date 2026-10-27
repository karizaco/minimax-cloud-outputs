#!/usr/bin/env python3
"""Cron #7 - QC for the focus RVOL snapshot.

1) Dump the raw 5m bar ladder for a few symbols so the cumulative-volume sum can be
   hand-checked against the in-progress trailing bar.
2) Cross-check the TradingView average_volume_10d_calc denominator against Yahoo's own
   trailing 10-session average volume computed from daily bars.
"""
import datetime as dt
import importlib.util
import json
import time
from zoneinfo import ZoneInfo

spec = importlib.util.spec_from_file_location("pr", "/workspace/parse_rvol.py")
pr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pr)

ET = ZoneInfo("America/New_York")
SESSION = dt.date.today()
SYMS = ["P", "CSCO", "HEI", "ADI"]

y = pr.Yahoo()
y.handshake()

print("=== raw 5m bar ladder ===")
for s in SYMS:
    p = y.chart(s)
    r = p["chart"]["result"][0]
    ts = r.get("timestamp") or []
    q = r["indicators"]["quote"][0]
    vols, closes = q.get("volume") or [], q.get("close") or []
    print(f"-- {s}  prevClose={r['meta'].get('chartPreviousClose')}  rmt={r['meta'].get('regularMarketTime')}")
    tot = 0
    for i, t in enumerate(ts):
        d = dt.datetime.fromtimestamp(t, ET)
        v = vols[i] if i < len(vols) else None
        c = closes[i] if i < len(closes) else None
        tot += float(v or 0)
        print(f"   {d.strftime('%H:%M:%S')}  vol={v}  close={c}")
    print(f"   SUM(all)={tot:,.0f}")
    time.sleep(1)

print()
print("=== denominator cross-check: Yahoo trailing 10 completed sessions vs TV average_volume_10d_calc ===")
snap = json.load(open("/workspace/data/rvol/rvol_2026-10-27.json"))
tv_avg = {r["symbol"]: r.get("avg_volume_10d") for r in snap["results"]}
rows = []
for sym in [r["symbol"] for r in snap["results"]]:
    p = y.chart_daily(sym) if hasattr(y, "chart_daily") else None
    if p is None:
        # inline daily fetch
        base = "https://query1.finance.yahoo.com/v8/finance/chart/" + sym
        url = base + "?interval=1d&range=1mo&crumb=" + pr.urllib.parse.quote(y.crumb)
        st, body = y._get(url)
        p = json.loads(body) if st == 200 else None
    if not p or not p.get("chart", {}).get("result"):
        print(f"  {sym}: daily fetch failed")
        continue
    r = p["chart"]["result"][0]
    ts = r.get("timestamp") or []
    q = r["indicators"]["quote"][0]
    vols = q.get("volume") or []
    daily = []
    for i, t in enumerate(ts):
        d = dt.datetime.fromtimestamp(t, ET).date()
        if d >= SESSION:
            continue
        v = vols[i] if i < len(vols) else None
        if v is not None:
            daily.append((d, float(v)))
    last10 = daily[-10:]
    yavg = sum(v for _d, v in last10) / len(last10) if last10 else None
    tv = tv_avg.get(sym)
    ratio = (tv / yavg) if (tv and yavg) else None
    rows.append({
        "symbol": sym, "yahoo_avg10": yavg, "tv_avg10": tv,
        "tv_over_yahoo": ratio, "n_sessions": len(last10),
        "first": str(last10[0][0]) if last10 else None,
        "last": str(last10[-1][0]) if last10 else None,
    })
    print(f"  {sym:6s} yahoo10={yavg:>14,.0f}  tv10={tv:>14,.0f}  tv/yahoo={ratio:.4f}  n={len(last10)}")
    time.sleep(1)

json.dump(rows, open("/workspace/data/rvol/denominator_check.json", "w"), indent=2)
print("wrote /workspace/data/rvol/denominator_check.json")
