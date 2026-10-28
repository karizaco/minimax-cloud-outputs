#!/usr/bin/env python3
"""Final assembly: skill-spec universe (USD floor) + below-floor catalyst exceptions."""
import json, os, re, datetime
from collections import Counter

CACHE = "/workspace/.cache/asia"
TARGET = "2026-10-27"
PREF = re.compile(r"\((1P|2P|2PB|1PB|3P|1B|2B)\)")
FX = {"JP": 157.746, "TW": 32.437, "HK": 7.8442, "KSC": 1328.52, "KOE": 1328.52}
MKTS = [("JP", "Japan (TSE/JPX)"), ("TW", "Taiwan (TWSE/TPEx)"),
        ("HK", "Hong Kong (HKEX)"), ("KSC", "Korea KOSPI"), ("KOE", "Korea KOSDAQ")]
REACTION = {"JP": 4.0, "TW": 5.0, "HK": 4.0, "KSC": 4.0, "KOE": 4.0}

uf = json.load(open(os.path.join(CACHE, "usdfloor.json")))
raw = json.load(open(os.path.join(CACHE, "ranked.json")))
tw = json.load(open(os.path.join(CACHE, "tw_official.json")))
tw_join = {o["symbol"]: o for o in tw["joined"]}
twse_codes = set(tw["twse"])
tpex_codes = set(tw["tpex"])


def ld(q):
    t = q.get("regularMarketTime")
    if not t:
        return None
    off = q.get("gmtOffSetMilliseconds") or 0
    return datetime.datetime.utcfromtimestamp(t + off / 1000.0).strftime("%Y-%m-%d")


def norm(q, mk, venue=None):
    sym = q.get("symbol")
    mcap = q.get("marketCap") or 0
    usd = mcap / FX[mk]
    return {
        "symbol": sym, "name": q.get("shortName"), "long": q.get("longName"),
        "pct": q.get("regularMarketChangePercent"), "price": q.get("regularMarketPrice"),
        "prev": q.get("regularMarketPreviousClose"), "mcap_local": mcap, "mcap_usd": usd,
        "currency": q.get("currency"), "venue": venue, "day_high": q.get("regularMarketDayHigh"),
        "day_low": q.get("regularMarketDayLow"), "volume": q.get("regularMarketVolume"),
        "avg3m": q.get("averageDailyVolume3Month"), "session": ld(q),
        "at_high": q.get("regularMarketDayHigh") == q.get("regularMarketPrice"),
        "at_low": q.get("regularMarketDayLow") == q.get("regularMarketPrice"),
        "preferred": bool(PREF.search(q.get("shortName") or "")),
    }


def dedupe(rows):
    bysym = {}
    for r in rows:
        if r["symbol"] not in bysym or abs(r["pct"]) > abs(bysym[r["symbol"]]["pct"]):
            bysym[r["symbol"]] = r
    seen, out = set(), []
    for r in sorted(bysym.values(), key=lambda x: -abs(x["pct"])):
        k = (re.sub(r"[\-(oldnew)新舊 ]", "", (r["name"] or "").lower()),
             round(r["mcap_usd"] / 5e6))
        if r["name"] and k in seen:
            continue
        seen.add(k); out.append(r)
    return out


result = {}
stats = Counter()
for key, label in MKTS:
    rec = uf["out"][key]
    core_all = []
    for direction in ("up", "down"):
        for q in rec[direction]:
            if q.get("quoteType") != "EQUITY":
                continue
            if ld(q) != TARGET:
                stats[f"{key}_stale_dropped"] += 1; continue
            core_all.append(norm(q, key))
    core_all = dedupe(core_all)
    core = [r for r in core_all if not r["preferred"]]
    stats[f"{key}_preferred_excluded"] = len(core_all) - len(core)
    up = sorted([r for r in core if r["pct"] > 0], key=lambda r: -r["pct"])[:15]
    dn = sorted([r for r in core if r["pct"] < 0], key=lambda r: r["pct"])[:15]

    # below-floor pool: from the raw (no USD floor) screener set
    below_all = []
    for r in raw["movers"].get(key, []):
        if r["symbol"] in {c["symbol"] for c in core_all}:
            continue
        if PREF.search(r.get("name") or ""):
            continue
        usd = (r["mcap"] or 0) / FX[key]
        b = dict(r); b["mcap_usd"] = usd
        b["preferred"] = bool(PREF.search(r.get("name") or ""))
        below_all.append(b)
    below_all = sorted(below_all, key=lambda r: -abs(r["pct"]))
    stats[f"{key}_below_floor_count"] = len(below_all)

    # TW venue + official override
    if key == "TW":
        for r in up + dn:
            o = tw_join.get(r["symbol"])
            if o:
                r["venue"] = o["venue"]
                if o["venue"] == "TPEX" and o["off_pct"] is not None:
                    r["pct_official"] = o["off_pct"]
                    if abs(o["off_pct"] - r["pct"]) > 0.5:
                        r["yahoo_pct_disputed"] = True
                if o["venue"] == "TWSE" and o["off_pct"] is not None:
                    r["pct_official"] = o["off_pct"]
                    if abs(o["off_pct"] - r["pct"]) > 0.5:
                        r["yahoo_pct_disputed"] = True
            else:
                r["venue"] = "UNLISTED_IN_TWSE_TPEX"
        for r in below_all:
            o = tw_join.get(r["symbol"])
            r["venue"] = o["venue"] if o else "UNLISTED_IN_TWSE_TPEX"

    result[key] = {"label": label, "up": up, "down": dn,
                   "below_floor": below_all[:25],
                   "n_core": len(core_all),
                   "fx": FX[key]}

json.dump(result, open(os.path.join(CACHE, "final.json"), "w"), indent=1, ensure_ascii=False)

print("STATS:", json.dumps(dict(stats), indent=1))
for key, label in MKTS:
    r = result[key]
    print(f"\n=== {key} {label} (core rows {r['n_core']}, below-floor {len(r['below_floor'])}) ===")
    print("  UP:")
    for x in r["up"][:10]:
        print(f"    {x['symbol']:12s} {str(x['name'])[:26]:26s} {x['pct']:8.2f}% "
              f"px={x['price']:>9} usd_cap=${x['mcap_usd']/1e9:7.3f}B "
              f"{'AT-HI' if x['at_high'] else ('AT-LO' if x['at_low'] else '')}"
              f"{' OFFICIAL:'+format(x['pct_official'],'.2f') if x.get('pct_official') is not None else ''}"
              f"{' DISPUTED' if x.get('yahoo_pct_disputed') else ''}"
              f" {x.get('venue','')}")
    print("  DOWN:")
    for x in r["down"][:10]:
        print(f"    {x['symbol']:12s} {str(x['name'])[:26]:26s} {x['pct']:8.2f}% "
              f"px={x['price']:>9} usd_cap=${x['mcap_usd']/1e9:7.3f}B "
              f"{'AT-HI' if x['at_high'] else ('AT-LO' if x['at_low'] else '')}"
              f"{' OFFICIAL:'+format(x['pct_official'],'.2f') if x.get('pct_official') is not None else ''}"
              f"{' DISPUTED' if x.get('yahoo_pct_disputed') else ''}"
              f" {x.get('venue','')}")
