#!/usr/bin/env python3
"""Detect limit-up/limit-down closes (close == day high/low) and check the
KOSPI preferred anomaly. Limit detection: close at the session extreme AND the
move is at the statutory band edge."""
import json, os, subprocess, datetime

CACHE = "/workspace/.cache/asia"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

GROUPS = {"JP": ["JPX"], "TW": ["TWO"], "HK": ["HKG"], "KR": ["KSC", "KOE"]}
ranked = json.load(open(os.path.join(CACHE, "ranked.json")))["markets"]

# statutory daily-limit band (JPY) for TSE Standard/Prime/Growth, MLT table
def jp_band(prev):
    if prev < 100: return 20
    if prev < 200: return 50
    if prev < 500: return 100
    if prev < 3000: return 300
    if prev < 5000: return 500
    if prev < 10000: return 1000
    return 2000

# statutory band (KRW) KOSPI / KOSDAQ
def kr_band(prev, kospi):
    if kospi: lo, hi = 300, 15
    else: lo, hi = 300, 30
    if prev < 5000: return 300
    if prev < 10000: return 1000
    if prev < 50000: return 2000
    if prev < 200000: return 5000
    if prev < 500000: return 10000
    return 20000

out = {}
for mk, exs in GROUPS.items():
    hits = []
    for ex in exs:
        for d in ("up", "down"):
            p = os.path.join(CACHE, f"scr_{ex}_{d}.json")
            if not os.path.exists(p): continue
            r = (json.load(open(p)).get("finance") or {}).get("result")
            if not r: continue
            for q in (r[0].get("quotes") or []):
                px = q.get("regularMarketPrice"); pct = q.get("regularMarketChangePercent")
                hi = q.get("regularMarketDayHigh"); lo = q.get("regularMarketDayLow")
                if px is None or pct is None: continue
                prev = px / (1 + pct / 100) if pct != -100 else None
                if prev is None: continue
                if mk == "JP":
                    band = jp_band(prev)
                elif mk == "KR":
                    band = kr_band(prev, ex == "KSC")
                else:
                    band = None
                if band is None: continue
                at_up = hi is not None and abs(px - hi) < 1e-6 and abs(pct - band / prev * 100) < 0.6
                at_dn = lo is not None and abs(px - lo) < 1e-6 and abs(pct + band / prev * 100) < 0.6
                if at_up or at_dn:
                    hits.append({"sym": q.get("symbol"), "name": q.get("shortName"),
                                 "px": px, "pct": round(pct, 2), "prev": round(prev, 2),
                                 "band": band, "dir": "UP" if at_up else "DOWN",
                                 "exch": ex})
    out[mk] = sorted(hits, key=lambda h: -abs(h["pct"]))
    print(f"\n=== {mk} limit-touch closes (n={len(hits)}) ===")
    for h in out[mk][:14]:
        print(f"  {h['sym']:>10} {str(h['name'])[:26]:<26} {h['pct']:>7.2f}%  "
              f"px={h['px']:>9} prev={h['prev']:>9} band=±{h['band']} {h['dir']}")

json.dump(out, open(os.path.join(CACHE, "limits.json"), "w"), indent=1)
