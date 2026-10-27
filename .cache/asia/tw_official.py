#!/usr/bin/env python3
"""Build authoritative TWSE + TPEx daily tables and join against Yahoo TW movers."""
import json, os, re

CACHE = "/workspace/.cache/asia"
d = json.load(open(os.path.join(CACHE, "twse_today.json")))
t8 = d["tables"][8]
print("TWSE fields:", t8["fields"])
twse = {}
for row in t8["data"]:
    rec = dict(zip(t8["fields"], row))
    code = str(rec.get("證券代號", "")).strip()
    if not code:
        continue
    _c = str(rec.get("收盤價", "")).strip()
    _d = str(rec.get("漲跌價差", "")).strip()
    try:
        _cf, _df = float(_c.replace(",", "")), float(_d.replace(",", ""))
        _pct = (_df / (_cf - _df) * 100.0) if (_cf - _df) else None
    except Exception:
        _pct = None
    twse[code] = {
        "pct_calc": _pct,
        "name": str(rec.get("證券名稱", "")).strip(),
        "vol": str(rec.get("成交股數", "")).strip(),
        "close": str(rec.get("收盤價", "")).strip(),
        "chg": str(rec.get("漲跌價差", "")).strip(),
        "chg_pct": None,
    }
print("TWSE rows:", len(twse))

tp = json.load(open(os.path.join(CACHE, "tpex.json")))
t0 = tp["tables"][0]
print("TPEx fields:", t0["fields"])
tpex = {}
for row in t0["data"]:
    rec = dict(zip(t0["fields"], row))
    code = str(rec.get("代號", "")).strip()
    if not code:
        continue
    tpex[code] = {
        "name": str(rec.get("名稱", "")).strip(),
        "close": str(rec.get("收盤", "")).strip(),
        "chg": str(rec.get("漲跌", "")).strip(),
        "open": str(rec.get("開盤", "")).strip(),
        "high": str(rec.get("最高", "")).strip(),
        "low": str(rec.get("最低", "")).strip(),
        "vol": str(rec.get("成交股數", "")).strip(),
        "ref_next": str(rec.get("次日 參考價", "")).strip(),
        "up_next": str(rec.get("次日 漲停價", "")).strip(),
        "down_next": str(rec.get("次日 跌停價", "")).strip(),
    }
print("TPEx rows:", len(tpex))
print("TPEx title:", t0.get("title"), "| listedCompanies:", t0.get("listedCompanies"))

# advancing/declining stats
for i in (6, 7):
    tt = d["tables"][i]
    print(f"-- table {i} {tt.get('title')}")
    for row in tt["data"][:8]:
        print("   ", row)

ranked = json.load(open(os.path.join(CACHE, "ranked.json")))
tw = ranked["movers"]["TW"]

def num(s):
    try:
        return float(str(s).replace(",", "").replace("%", "").strip())
    except Exception:
        return None

out = []
for r in tw:
    code = r["symbol"].split(".")[0]
    src = None
    if code in twse:
        src = ("TWSE", twse[code])
    elif code in tpex:
        src = ("TPEX", tpex[code])
    rec = {
        "symbol": r["symbol"], "yahoo_name": r["name"], "yahoo_pct": r["pct"],
        "yahoo_price": r["price"], "yahoo_prev": r["prev_close"],
        "yahoo_vol": r["volume"], "mcap": r["mcap"],
        "venue": "UNKNOWN", "off_name": None, "off_close": None, "off_chg": None,
        "off_pct": None, "ref_next": None, "up_next": None, "down_next": None,
        "off_high": None, "off_low": None, "off_vol": None,
    }
    if src:
        v, rec0 = src
        rec.update({
            "venue": v, "off_name": rec0["name"],
            "off_close": num(rec0["close"]), "off_chg": num(rec0["chg"]),
            "off_high": num(rec0.get("high")), "off_low": num(rec0.get("low")),
            "off_vol": num(rec0.get("vol")),
            "ref_next": num(rec0.get("ref_next")),
            "up_next": num(rec0.get("up_next")), "down_next": num(rec0.get("down_next")),
        })
        if v == "TWSE":
            rec["off_pct"] = rec0.get("pct_calc")
        else:
            # TPEx: pct = chg / (close - chg) * 100
            c, g = rec["off_close"], rec["off_chg"]
            if c is not None and g is not None and (c - g):
                rec["off_pct"] = g / (c - g) * 100.0
    out.append(rec)

json.dump({"twse": twse, "tpex": tpex, "joined": out},
          open(os.path.join(CACHE, "tw_official.json"), "w"), indent=1, ensure_ascii=False)

from collections import Counter
print("\nvenue split of Yahoo TW movers:", dict(Counter(o["venue"] for o in out)))
print()
print(f"{'sym':12s} {'venue':7s} {'yahoo%':>8s} {'off%':>8s} {'offClose':>9s} {'offChg':>8s} {'high':>9s} {'low':>9s}  name")
for o in sorted(out, key=lambda x: -(abs(x["yahoo_pct"]) if x["yahoo_pct"] else 0))[:26]:
    print(f"{o['symbol']:12s} {o['venue']:7s} {o['yahoo_pct']:8.2f} "
          f"{(o['off_pct'] if o['off_pct'] is not None else float('nan')):8.2f} "
          f"{(o['ref_next'] if o['ref_next'] is not None else float('nan')):8} "
          f"{(o['off_close'] if o['off_close'] is not None else float('nan')):9} "
          f"{(o['off_chg'] if o['off_chg'] is not None else float('nan')):8} "
          f"{(o['off_high'] if o['off_high'] is not None else float('nan')):9} "
          f"{(o['off_low'] if o['off_low'] is not None else float('nan')):9}  {str(o['off_name'])[:24]}")
