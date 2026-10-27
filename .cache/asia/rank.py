#!/usr/bin/env python3
"""Rank Asia movers: session-date filter, exchange whitelist, dedupe, anomaly flags."""
import json, os, datetime, collections

CACHE = "/workspace/.cache/asia"
TARGET = "2026-10-27"

MARKETS = [
    ("JP", "JPX", "Japan", 9),
    ("TW", "TWO", "Taiwan", 8),
    ("HK", "HKG", "Hong Kong", 8),
    ("KSC", "KSC", "Korea KOSPI", 9),
    ("KOE", "KOE", "Korea KOSDAQ", 9),
]

DROP_EXCHANGES = {"OTC", "PINK", "OTCBB", "GREY", "LSE", "LSX", "NASDAQ", "NYSE", "AMEX", "BATS"}


def local_date(q):
    t = q.get("regularMarketTime")
    if not t:
        return None, None
    off = q.get("gmtOffSetMilliseconds") or 0
    loc = datetime.datetime.utcfromtimestamp(t + off / 1000.0)
    return loc.strftime("%Y-%m-%d"), loc.isoformat()


def load(key, code, direction):
    fn = os.path.join(CACHE, f"scr_{key}_{direction}.json")
    if not os.path.exists(fn):
        return [], 0
    d = json.load(open(fn))
    return d["quotes"], d["total"]


stats = collections.Counter()
rows_out = {}
market_meta = {}

for key, code, name, tzoff in MARKETS:
    allrows = []
    for direction in ("up", "down"):
        quotes, total = load(key, code, direction)
        stats[f"{key}_total_{direction}"] = total
        for q in quotes:
            ex = (q.get("exchange") or "").upper()
            fen = (q.get("fullExchangeName") or "")
            if ex in DROP_EXCHANGES:
                stats[f"{key}_dropped_exch"] += 1
                continue
            sd, loctime = local_date(q)
            if sd != TARGET:
                stats[f"{key}_dropped_stale"] += 1
                continue
            pct = q.get("regularMarketChangePercent")
            if pct is None:
                stats[f"{key}_dropped_nopct"] += 1
                continue
            mcap = q.get("marketCap") or 0
            price = q.get("regularMarketPrice")
            prev = q.get("regularMarketPreviousClose")
            sym = q.get("symbol", "")
            flags = []
            # KOSPI 1형 preferred shares: no daily limit, capital-action moves
            if sym.endswith("(1P)") or "(1P)" in sym or sym.endswith(".KS") and "P)" in sym:
                flags.append("PREFERRED_NO_LIMIT")
            # TWSE: keep primary tier only per skill whitelist
            if key == "TW" and fen and "Taipei" in fen and "Exchange" in fen:
                flags.append("TPEX_SECONDARY")
            allrows.append({
                "symbol": sym, "name": q.get("shortName"), "longname": q.get("longName"),
                "exchange": ex, "full_exchange": fen, "currency": q.get("currency"),
                "price": price, "prev_close": prev, "pct": pct,
                "mcap": mcap, "time_local": loctime, "session_date": sd,
                "day_high": q.get("regularMarketDayHigh"), "day_low": q.get("regularMarketDayLow"),
                "volume": q.get("regularMarketVolume"),
                "avgvol3m": q.get("averageDailyVolume3Month"),
                "market_state": q.get("marketState"),
                "direction": direction, "flags": flags,
                "quote_type": q.get("quoteType"),
            })
    # dedupe by symbol, then by (name, mcap) for dual-ticker
    bysym = {}
    for r in allrows:
        if r["symbol"] not in bysym or abs(r["pct"]) > abs(bysym[r["symbol"]]["pct"]):
            bysym[r["symbol"]] = r
    seen_name = set()
    dedup = []
    for r in sorted(bysym.values(), key=lambda x: -abs(x["pct"])):
        k = (r["name"], round((r["mcap"] or 0) / 1e6))
        if r["name"] and k in seen_name:
            stats[f"{key}_dedup_dupticker"] += 1
            continue
        seen_name.add(k)
        dedup.append(r)
    rows_out[key] = dedup
    market_meta[key] = {"name": name, "code": code, "n": len(dedup)}

# exclude preferred-share / TPEX-secondary rows from movers
movers = {}
for key, rows in rows_out.items():
    keep = [r for r in rows if "PREFERRED_NO_LIMIT" not in r["flags"]]
    stats[f"{key}_excl_preferred"] = len(rows) - len(keep)
    movers[key] = keep

json.dump({"movers": movers, "all_rows": rows_out, "stats": dict(stats),
           "meta": market_meta},
          open(os.path.join(CACHE, "ranked.json"), "w"), indent=2, ensure_ascii=False)

print("STATS:", json.dumps(dict(stats), indent=1))
print()
for key, rows in movers.items():
    print(f"=== {key} {market_meta[key]['name']} ({market_meta[key]['n']} rows) ===")
    for r in rows[:12]:
        hi = r["day_high"] == r["price"]
        lo = r["day_low"] == r["price"]
        lim = "AT-HI" if hi else ("AT-LO" if lo else "")
        print(f"  {r['symbol']:14s} {str(r['name'])[:26]:26s} {r['pct']:8.2f}%  "
              f"px={r['price']:>10} prev={r['prev_close']:>10} mcap={r['mcap']/1e9:7.2f}B "
              f"{r['full_exchange'][:18]:18s} {lim} vol={r['volume']} {r['flags']}")
    print()
