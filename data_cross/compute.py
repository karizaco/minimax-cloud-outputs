#!/usr/bin/env python3
"""Cron #12 cross-asset-correlation-snapshot — local computation.

Re-implements the skill's `correlation_matrix` (not bound in Cloud sessions) on the
Yahoo Chart API fallback. Run from /workspace/data_cross:  python3 compute.py
"""
import json, math, datetime, zoneinfo, itertools, os, re

NY = zoneinfo.ZoneInfo("America/New_York")
D = "/workspace/data_cross"
SYMS = ["SPY", "QQQ", "IWM", "TLT", "GLD", "UUP", "EEM", "^VIX"]
FILES = {s: os.path.join(D, f"raw_{s.replace('^','')}.json") for s in SYMS}
PRIOR = os.path.join(D, "prior_2026-10-25.md")

RUN_DATE = datetime.date(2026, 10, 26)
PARTIAL_DATE = datetime.date(2026, 10, 26)   # session in progress at run time
CLOSED_END = datetime.date(2026, 10, 23)     # last fully closed session (Friday)
ROLL_END = datetime.date(2026, 10, 16)       # same window rolled back 1 week
# Closed window anchored to the prior snapshot's published session set so the
# week-over-week delta isolates market/data change from window drift.
CLOSED_START = datetime.date(2026, 4, 24)
LIVE_START = datetime.date(2026, 4, 27)      # 6 calendar months back from run date

# ---------------------------------------------------------------- load series
series, meta_out = {}, {}
for s in SYMS:
    j = json.load(open(FILES[s]))
    r = j["chart"]["result"][0]
    ts = r["timestamp"]
    q = r["indicators"]["quote"][0]
    ac = r["indicators"].get("adjclose", [{}])[0].get("adjclose")
    closes = ac if ac else q["close"]
    m, n_null = {}, 0
    for i, t in enumerate(ts):
        dt = datetime.datetime.fromtimestamp(t, NY).date()
        v = closes[i] if i < len(closes) else None
        if v is None:
            n_null += 1
            continue
        m[dt] = float(v)
    series[s] = m
    meta_out[s] = {
        "bars": len(ts), "nulls": n_null,
        "first": min(m).isoformat(), "last": max(m).isoformat(),
        "mkt_time": datetime.datetime.fromtimestamp(r["meta"]["regularMarketTime"], NY).strftime("%Y-%m-%d %H:%M ET"),
        "mkt_price": r["meta"].get("regularMarketPrice"),
        "tz": r["meta"].get("exchangeTimezoneName"),
    }

all_dates = set.intersection(*[set(series[s].keys()) for s in SYMS])

def win(start, end):
    return sorted(d for d in all_dates if start <= d <= end)

def returns(sym, dates):
    s = series[sym]
    return [math.log(s[dates[i]] / s[dates[i-1]]) for i in range(1, len(dates))]

def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs)/n, sum(ys)/n
    sx = math.sqrt(sum((x-mx)**2 for x in xs)); sy = math.sqrt(sum((y-my)**2 for y in ys))
    if sx == 0 or sy == 0: return float("nan")
    return sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / (sx*sy)

def matrix(dates, basis="returns"):
    cols = ({s: returns(s, dates) for s in SYMS} if basis == "returns"
            else {s: [series[s][d] for d in dates] for s in SYMS})
    return {a: {b: pearson(cols[a], cols[b]) for b in SYMS} for a in SYMS}

def pairs(m):
    return [(a, b, m[a][b]) for a, b in itertools.combinations(SYMS, 2)]

# ---------------------------------------------------------------- windows
closed_dates = win(CLOSED_START, CLOSED_END)     # headline: completed sessions only
live_dates   = win(LIVE_START, PARTIAL_DATE)     # sensitivity: adds in-progress session
roll_dates   = win(CLOSED_START, ROLL_END)       # same 6mo length, one week earlier

# ---------------------------------------------------------------- prior file matrix
prior_txt = open(PRIOR).read()
def parse_prior(section, stop=None):
    seg = prior_txt.split(section)[1]
    if stop:
        seg = seg.split(stop)[0]
    tbl = {}
    for a, rest in re.findall(r"^\|\s*\*\*(\S+?)\*\*\s*\|(.+)\|\s*$", seg, re.M):
        vals = [float(v.strip().replace("+", "")) for v in rest.split("|") if v.strip()]
        if len(vals) == len(SYMS):
            tbl[a] = {SYMS[i]: vals[i] for i in range(len(SYMS))}
    return tbl
prior_m = parse_prior("Pearson correlation, daily returns", stop="## Highlights")
prior_lv = parse_prior("Pearson correlation, price levels", stop="## Files")

# ---------------------------------------------------------------- compute
closed_m  = matrix(closed_dates, "returns")
live_m    = matrix(live_dates, "returns")
closed_lv = matrix(closed_dates, "levels")
live_lv   = matrix(live_dates, "levels")
roll_m    = matrix(roll_dates, "returns")

repro = [(a, b, closed_m[a][b], prior_m[a][b], closed_m[a][b]-prior_m[a][b])
         for a, b in itertools.combinations(SYMS, 2) if a in prior_m and b in prior_m]
max_repro = max(abs(r[4]) for r in repro)

# WoW vs prior published file (identical window -> reproducibility + data revision check)
wow = [(a, b, closed_m[a][b], prior_m[a][b], closed_m[a][b]-prior_m[a][b]) for a, b in itertools.combinations(SYMS, 2)]
wow.sort(key=lambda r: -abs(r[4]))

# true week-rolled regime read: window ending 10-23 vs same window ending 10-16
rolled = [(a, b, roll_m[a][b], closed_m[a][b], closed_m[a][b]-roll_m[a][b]) for a, b in itertools.combinations(SYMS, 2)]
rolled.sort(key=lambda r: -abs(r[4]))
max_rolled = max(abs(r[4]) for r in rolled)

# sensitivity: effect of including the in-progress session
sens = [(a, b, live_m[a][b], closed_m[a][b], live_m[a][b]-closed_m[a][b]) for a, b in itertools.combinations(SYMS, 2)]
sens.sort(key=lambda r: -abs(r[4]))
max_sens = max(abs(r[4]) for r in sens)

# drift: early half vs recent half within the closed window
mid = len(closed_dates)//2
split_date = closed_dates[mid]
early_m = matrix(closed_dates[:mid+1], "returns")
recent_m = matrix(closed_dates[mid:], "returns")
drift = [(a, b, early_m[a][b], recent_m[a][b], recent_m[a][b]-early_m[a][b]) for a, b in itertools.combinations(SYMS, 2)]
drift.sort(key=lambda r: -abs(r[4]))

prior_drift = []
seg = prior_txt.split("## Regime drift")[1].split("## Proxy performance")[0]
for m_ in re.finditer(r"^\|\s*(\S+?)–(\S+?)\s*\|\s*([+-][\d.]+)\s*\|\s*([+-][\d.]+)\s*\|\s*([+-][\d.]+)\s*\|", seg, re.M):
    prior_drift.append((m_.group(1), m_.group(2), float(m_.group(3)), float(m_.group(4)), float(m_.group(5))))
drift_wow = []
for a, b, e, r_, dd in drift:
    pr = next((p for p in prior_drift if p[0] == a and p[1] == b), None)
    drift_wow.append((a, b, e, r_, dd, pr[4] if pr else None, (dd-pr[4]) if pr else None))
drift_wow.sort(key=lambda r: -abs(r[6]) if r[6] is not None else 0)

sp = sorted(pairs(closed_m), key=lambda r: -abs(r[2]))
strongest, weakest = sp[:3], sp[-3:][::-1]

perf = []
for s in SYMS:
    s0, s1 = series[s][closed_dates[0]], series[s][closed_dates[-1]]
    live = series[s].get(PARTIAL_DATE)
    perf.append({"sym": s, "start": closed_dates[0].isoformat(), "start_px": s0,
                  "last_closed": closed_dates[-1].isoformat(), "last_closed_px": s1,
                  "live": live, "ret_6mo_pct": (s1/s0-1)*100,
                  "day_pct": (live/s1-1)*100 if live else None})

vix_only = sorted(set(series["^VIX"]) - set.union(*[set(series[x]) for x in SYMS if x != "^VIX"]))

out = {
    "run_et": datetime.datetime.now(NY).strftime("%Y-%m-%d %H:%M ET"),
    "iso_week": RUN_DATE.isocalendar().week, "iso_year": RUN_DATE.isocalendar().year,
    "universe": SYMS, "meta": meta_out, "all_common_dates": len(all_dates),
    "closed_window": {"start": closed_dates[0].isoformat(), "end": closed_dates[-1].isoformat(),
                      "n": len(closed_dates), "ret_obs": len(closed_dates)-1},
    "live_window": {"start": live_dates[0].isoformat(), "end": live_dates[-1].isoformat(),
                    "n": len(live_dates), "ret_obs": len(live_dates)-1},
    "roll_window": {"start": roll_dates[0].isoformat(), "end": roll_dates[-1].isoformat(),
                    "n": len(roll_dates), "ret_obs": len(roll_dates)-1},
    "closed_matrix": closed_m, "live_matrix": live_m, "closed_levels": closed_lv, "live_levels": live_lv,
    "roll_matrix": roll_m, "prior_matrix": prior_m, "prior_levels": prior_lv,
    "max_repro_dev": max_repro, "repro_rows": repro, "wow": wow, "rolled": rolled,
    "max_rolled": max_rolled, "sens": sens, "max_sens": max_sens,
    "drift": drift, "drift_wow": drift_wow, "split_date": split_date.isoformat(),
    "early_n": len(closed_dates[:mid+1]), "recent_n": len(closed_dates[mid:]),
    "strongest": strongest, "weakest": weakest, "perf": perf,
    "vix_only_dates": [d.isoformat() for d in vix_only],
}
json.dump(out, open(os.path.join(D, "mats.json"), "w"), indent=1, default=str)

def fmt(x, n=2): return f"{x:+.{n}f}"
print("run:", out["run_et"], "ISO", out["iso_year"], "-W%02d" % out["iso_week"])
print("closed:", out["closed_window"]); print("live:  ", out["live_window"]); print("roll:  ", out["roll_window"])
print("vix-only:", out["vix_only_dates"], " common dates:", out["all_common_dates"])
print("max |repro dev| vs prior published returns matrix:", fmt(max_repro, 4))
print("\nCLOSED returns matrix (headline)")
print("        " + "".join(f"{s:>8}" for s in SYMS))
for a in SYMS: print(f"{a:>7} " + "".join(f"{closed_m[a][b]:>8.2f}" for b in SYMS))
print("strongest:", [(a,b,round(c,3)) for a,b,c in strongest])
print("weakest:  ", [(a,b,round(c,3)) for a,b,c in weakest])
print("\nWoW vs prior file (max |delta|):", fmt(max(abs(r[4]) for r in wow)))
for a,b,l,p,d in wow[:4]: print(f"   {a}-{b}: {fmt(l)} vs {fmt(p)} -> {fmt(d)}")
print("\nweek-rolled (10-16 window vs 10-23 window), max |delta|:", fmt(max_rolled))
for a,b,o,c,d in rolled[:8]: print(f"   {a}-{b}: {fmt(o)} -> {fmt(c)} delta {fmt(d)}")
print("\nsensitivity (add in-progress session), max |delta|:", fmt(max_sens))
for a,b,l,c,d in sens[:4]: print(f"   {a}-{b}: {fmt(l)} vs {fmt(c)} -> {fmt(d)}")
print("\ndrift early->recent (split", out["split_date"], ")", "early_n",out["early_n"],"recent_n",out["recent_n"])
for a,b,e,r_,dd in drift[:6]: print(f"   {a}-{b}: {fmt(e)} -> {fmt(r_)} delta {fmt(dd)}")
print("drift WoW:")
for row in drift_wow[:5]: print("  ",row[0],row[1],"cur",fmt(row[4]),"prior",fmt(row[5]),"chg",fmt(row[6]))
print("\nperf:")
for p in perf: print(f"   {p['sym']:>5} start {p['start_px']:.2f} last {p['last_closed_px']:.2f} 6mo {p['ret_6mo_pct']:+.2f}% live {p['live']:.2f} day {p['day_pct']:+.2f}%")
print("\nmeta:")
for s in SYMS: print("  ",s,meta_out[s])
