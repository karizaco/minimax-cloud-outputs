#!/usr/bin/env python3
"""Rank + QC the Asia pre-market screens into per-market tables."""
import json, os, datetime, collections

CACHE = "/workspace/.cache/asia"
OFFSET = {"JPX": 9, "TWO": 8, "HKG": 8, "KSC": 9, "KOE": 9}   # hours from UTC
KEEP = {"JPX", "TWO", "HKG", "KSC", "KOE"}
GROUPS = {"JP": ["JPX"], "TW": ["TWO"], "HK": ["HKG"], "KR": ["KSC", "KOE"]}
NAME = {"JP": "Japan (TSE)", "TW": "Taiwan (TWSE)", "HK": "Hong Kong (HKEX)",
        "KR": "Korea (KRX)"}


def load(ex, d):
    p = os.path.join(CACHE, f"scr_{ex}_{d}.json")
    if not os.path.exists(p):
        return []
    try:
        r = (json.load(open(p)).get("finance") or {}).get("result")
        return (r[0].get("quotes") or []) if r else []
    except Exception:
        return []


def session_date(ts, off):
    return (datetime.datetime.utcfromtimestamp(ts) +
            datetime.timedelta(hours=off)).strftime("%Y-%m-%d")


out = {}
qc = {"rows_raw": 0, "dropped_exchange": 0, "dropped_price": 0, "dropped_nomc": 0,
      "dedup_hk": 0, "dedup_other": 0, "session_dates": {}, "cap_rows": 0}

for mk, exs in GROUPS.items():
    rows = []
    for ex in exs:
        for d in ("up", "down"):
            for q in load(ex, d):
                qc["rows_raw"] += 1
                exs_field = q.get("exchange")
                if exs_field not in KEEP:
                    qc["dropped_exchange"] += 1
                    continue
                px = q.get("regularMarketPrice")
                pct = q.get("regularMarketChangePercent")
                mc = q.get("marketCap")
                ts = q.get("regularMarketTime")
                if px is None or pct is None or ts is None:
                    continue
                if px < 5:                      # close floor, local currency
                    qc["dropped_price"] += 1
                    continue
                if not mc or mc < 2_000_000_000:  # $2B market-cap floor
                    qc["dropped_nomc"] += 1
                    continue
                rows.append({
                    "symbol": q.get("symbol"), "name": q.get("shortName"),
                    "long": q.get("longName"), "exch": exs_field,
                    "full": q.get("fullExchangeName"), "px": px, "pct": round(pct, 2),
                    "mc": mc, "cur": q.get("currency"), "ts": ts,
                    "sess": session_date(ts, OFFSET[exs_field]),
                    "vol": q.get("regularMarketVolume"),
                })

    # ---- dedupe: same company appearing twice (HK dual-ticker 5-digit vs 4-digit) ----
    byname = collections.defaultdict(list)
    for r in rows:
        byname[(r["name"] or r["long"] or r["symbol"]).upper()].append(r)
    kept = []
    for nm, grp in byname.items():
        if len(grp) == 1:
            kept.append(grp[0])
            continue
        # keep the shorter numeric ticker (4-digit HK primary) when market caps agree
        grp2 = sorted(grp, key=lambda r: (len(str(r["symbol"]).split(".")[0]), -r["mc"]))
        kept.append(grp2[0])
        if mk == "HK":
            qc["dedup_hk"] += len(grp) - 1
        else:
            qc["dedup_other"] += len(grp) - 1

    up = sorted([r for r in kept if r["pct"] > 0], key=lambda r: -r["pct"])[:15]
    dn = sorted([r for r in kept if r["pct"] < 0], key=lambda r: r["pct"])[:15]
    qc["session_dates"][mk] = collections.Counter(
        [r["sess"] for r in kept]).most_common()
    qc["cap_rows"] += len(up) + len(dn)
    out[mk] = {"name": NAME[mk], "up": up, "down": dn,
               "n_kept": len(kept)}

json.dump({"markets": out, "qc": qc}, open(os.path.join(CACHE, "ranked.json"), "w"),
          indent=1, default=str)

for mk in ("JP", "TW", "HK", "KR"):
    m = out[mk]
    print(f"\n=== {m['name']} | kept={m['n_kept']} | session dates={qc['session_dates'][mk]}")
    for lbl, lst in (("UP", m["up"]), ("DOWN", m["down"])):
        print(f"  --{lbl}--")
        for r in lst:
            print(f"   {r['symbol']:>10} {str(r['name'])[:26]:<26} {r['pct']:>7.2f}% "
                  f"px={r['px']:>10} mc=${r['mc']/1e9:>6.2f}B {r['cur']} [{r['full']}] sess={r['sess']}")
print("\nQC:", json.dumps(qc, default=str))
