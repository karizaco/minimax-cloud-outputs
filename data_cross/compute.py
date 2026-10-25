import json, datetime
import numpy as np
from zoneinfo import ZoneInfo
NY = ZoneInfo("America/New_York")

SYMS = ["SPY","QQQ","IWM","TLT","GLD","UUP","EEM","VIX"]
NICE = {"VIX":"^VIX"}
series = {}; meta = {}
for s in SYMS:
    d = json.load(open(f"data_cross/{s}.json"))
    res = d["chart"]["result"][0]
    ts = res["timestamp"]
    q = res["indicators"]["quote"][0]
    closes = q["close"]
    adj = res["indicators"].get("adjclose")
    if adj: closes = adj[0]["adjclose"]
    vals = {}
    for t,c in zip(ts, closes):
        if c is None: continue
        day = datetime.datetime.fromtimestamp(t, NY).strftime("%Y-%m-%d")
        vals[day] = c
    series[s] = vals
    m = res["meta"]
    meta[s] = {"symbol": NICE.get(s,s), "exchange": m.get("fullExchangeName"), "currency": m.get("currency"),
               "n": len(vals), "last_date": max(vals), "last_close": round(vals[max(vals)],4),
               "regularMarketPrice": m.get("regularMarketPrice"), "regularMarketChangePercent": m.get("regularMarketChangePercent")}

# align on common NY calendar dates
common = sorted(set.intersection(*[set(v) for v in series.values()]))
print("common dates:", len(common), common[0], "->", common[-1])
for s in SYMS:
    missing = sorted(set(series[s]) - set(common))
    print(f"{s}: n={len(series[s])} last={meta[s]['last_date']} close={meta[s]['last_close']} dropped_dates={missing}")

arr = {s: np.array([series[s][t] for t in common]) for s in SYMS}
rets = {s: np.diff(np.log(arr[s])) for s in SYMS}

def mat(d):
    M = np.zeros((len(SYMS), len(SYMS)))
    for i,a in enumerate(SYMS):
        for j,b in enumerate(SYMS):
            M[i,j] = np.corrcoef(d[a], d[b])[0,1]
    return M
MR = mat(rets); ML = mat(arr)

print("\n=== RETURNS CORR (daily log returns, %d obs) ===" % (len(common)-1))
print("      " + " ".join(f"{NICE.get(s,s):>6}" for s in SYMS))
for i,s in enumerate(SYMS):
    print(f"{NICE.get(s,s):>5} " + " ".join(f"{MR[i,j]:6.2f}" for j in range(len(SYMS))))
print("\n=== LEVELS CORR (price levels, %d obs) ===" % len(common))
print("      " + " ".join(f"{NICE.get(s,s):>6}" for s in SYMS))
for i,s in enumerate(SYMS):
    print(f"{NICE.get(s,s):>5} " + " ".join(f"{ML[i,j]:6.2f}" for j in range(len(SYMS))))

json.dump({"syms":[NICE.get(s,s) for s in SYMS],"ret":MR.round(4).tolist(),"lvl":ML.round(4).tolist(),
           "n_common":len(common),"start":common[0],"end":common[-1],"meta":meta,
           "levels_last":{s:round(arr[s][-1],4) for s in SYMS},
           "six_mo_return_pct":{s: round((arr[s][-1]/arr[s][0]-1)*100,2) for s in SYMS}},
          open("data_cross/mats.json","w"), indent=2)
print("\nwrote data_cross/mats.json")
