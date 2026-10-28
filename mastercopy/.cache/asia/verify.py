#!/usr/bin/env python3
"""Verify screener % changes against Yahoo chart close series.

For single stocks the daily close series DOES include today's bar, so
pct = (close[-1] / close[-2] - 1) * 100 is the true session move.
Flags rows where screener pct and chart pct disagree by > 0.5pp.
"""
import json, os, subprocess, time, datetime
from concurrent.futures import ThreadPoolExecutor

CACHE = "/workspace/.cache/asia"
UA = "Mozilla/5.0"
OUT = os.path.join(CACHE, "verify.json")
TARGET = "2026-10-27"
PER_DIR = 10  # top N per direction per market to verify

ranked = json.load(open(os.path.join(CACHE, "ranked.json")))
movers = ranked["movers"]


def chart(sym):
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/{sym}?range=10d&interval=1d"
    r = subprocess.run(["curl", "-sS", "--max-time", "20", "-A", UA, url],
                       capture_output=True, text=True)
    try:
        j = json.loads(r.stdout)
        res = j["chart"]["result"][0]
    except Exception:
        return None
    ts = res.get("timestamp") or []
    close = res["indicators"]["quote"][0].get("close") or []
    meta = res.get("meta", {})
    off = meta.get("gmtoffset") or 0
    pairs = []
    for t, c in zip(ts, close):
        if c is None:
            continue
        loc = datetime.datetime.utcfromtimestamp(t + off)
        pairs.append((loc.strftime("%Y-%m-%d"), c))
    return {"pairs": pairs, "meta": {
        "price": meta.get("regularMarketPrice"),
        "prevClose": meta.get("previousClose"),
        "chartPreviousClose": meta.get("chartPreviousClose"),
        "exchange": meta.get("fullExchangeName"),
        "time": meta.get("regularMarketTime"),
    }}


def verify_row(r):
    c = chart(r["symbol"])
    if not c:
        r["chart"] = None
        r["verdict"] = "CHART_FAIL"
        return r
    pairs = c["pairs"]
    dates = [p[0] for p in pairs]
    last_date = dates[-1] if dates else None
    r["chart"] = {"last_date": last_date, "last_close": pairs[-1][1] if pairs else None,
                  "prev_close": pairs[-2][1] if len(pairs) > 1 else None,
                  "n_bars": len(pairs), "dates": dates[-4:]}
    if len(pairs) >= 2 and last_date == TARGET:
        pc = pairs[-2][1]
        r["chart_pct"] = (pairs[-1][1] / pc - 1) * 100
        r["chart_prev_close"] = pc
        if abs(r["chart_pct"] - r["pct"]) > 0.5:
            r["verdict"] = "MISMATCH"
        else:
            r["verdict"] = "AGREE"
    else:
        r["chart_pct"] = None
        r["verdict"] = "NO_TODAY_BAR"
    return r


targets = []
for mk, rows in movers.items():
    up = [r for r in rows if r["pct"] > 0][:PER_DIR]
    dn = [r for r in rows if r["pct"] < 0][:PER_DIR]
    targets += up + dn

print(f"verifying {len(targets)} symbols", flush=True)
with ThreadPoolExecutor(max_workers=5) as ex:
    results = list(ex.map(verify_row, targets))

json.dump(results, open(OUT, "w"), indent=1, ensure_ascii=False)

from collections import Counter
print(Counter(r["verdict"] for r in results), flush=True)
print()
for mk in movers:
    print(f"=== {mk} ===")
    for r in sorted([x for x in results if x["symbol"].endswith(mk[-2:]) or True][:0]):
        pass
    mkrows = [r for r in results if r["symbol"] in {x["symbol"] for x in movers[mk]}]
    for r in sorted(mkrows, key=lambda x: -abs(x["pct"])):
        flag = "" if r["verdict"] == "AGREE" else f"  <<< {r['verdict']}"
        cp = f"{r['chart_pct']:.2f}" if r.get("chart_pct") is not None else "n/a"
        print(f"  {r['symbol']:13s} {str(r['name'])[:24]:24s} scr={r['pct']:8.2f}% "
              f"chart={cp:>8}% prevScr={r['prev_close']} prevChart={r.get('chart_prev_close')} "
              f"lastDate={r['chart']['last_date']} bars={r['chart']['n_bars']}{flag}")
    print()
