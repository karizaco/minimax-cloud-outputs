#!/usr/bin/env python3
"""Cron #2 — skill-faithful screener with USD market-cap floor.

Yahoo's `marketCap` / `intradaymarketcap` are in LOCAL currency, so the
skill's $2B floor must be converted before it is applied. Also fetches the
skill's "top N by market cap" universe per market.
"""
import json, os, subprocess, time, urllib.parse, datetime

CACHE = "/workspace/.cache/asia"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
CRUMB_FILE = os.path.join(CACHE, "crumb.txt")
COOKIE_FILE = os.path.join(CACHE, "yck.txt")
TARGET = "2026-10-27"

# FX units per USD (Yahoo, 2026-10-27)
FX = {"JPX": 157.746, "TWO": 32.437, "HKG": 7.8442, "KSC": 1328.52, "KOE": 1328.52}
# exchange -> (market key, friendly, top-N by market cap per skill)
MKTS = [("JP", "JPX", "Japan (TSE/JPX)", 100),
        ("TW", "TWO", "Taiwan (TWSE/TPEx)", 60),
        ("HK", "HKG", "Hong Kong (HKEX)", 60),
        ("KSC", "KSC", "Korea KOSPI", 60),
        ("KOE", "KOE", "Korea KOSDAQ", 60)]
USD_FLOOR = 2_000_000_000


def curl(url, method="GET", data=None):
    cmd = ["curl", "-sS", "-L", "--max-time", "25", "-A", UA,
           "-b", COOKIE_FILE, "-c", COOKIE_FILE]
    if method == "POST":
        cmd += ["-X", "POST", "-H", "Content-Type: application/json",
                "--data-binary", data, url]
    else:
        cmd += [url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"curl rc={r.returncode}: {r.stderr[:200]}")
    return r.stdout


def get_crumb():
    c = open(CRUMB_FILE).read().strip()
    if c:
        return c
    curl("https://fc.yahoo.com"); curl("https://finance.yahoo.com/")
    for h in ("query2", "query1"):
        o = curl(f"https://{h}.finance.yahoo.com/v1/test/getcrumb").strip()
        if o and len(o) < 40 and "html" not in o.lower():
            open(CRUMB_FILE, "w").write(o); return o
    raise RuntimeError("no crumb")


def screen(crumb, code, floor_local, direction=None, topn=None):
    """direction: 'up'/'down'/None(all); topn: sort by marketCap desc and cap rows."""
    operands = [{"operator": "EQ", "operands": ["exchange", code]},
                {"operator": "GT", "operands": ["intradaymarketcap", floor_local]}]
    sort_field, sort_type = "percentchange", "DESC"
    if direction == "up":
        operands.append({"operator": "GT", "operands": ["percentchange", 2.0]})
    elif direction == "down":
        operands.append({"operator": "LT", "operands": ["percentchange", -2.0]})
        sort_type = "ASC"
    if topn:
        sort_field, sort_type = "marketCap", "DESC"
    payload = {"size": 100, "offset": 0, "sortField": sort_field, "sortType": sort_type,
               "quoteType": "EQUITY", "userId": "", "userIdType": "guid",
               "lang": "en-US", "region": "US",
               "query": {"operator": "AND", "operands": operands}}
    url = f"https://query1.finance.yahoo.com/v1/finance/screener?crumb={urllib.parse.quote(crumb)}"
    j = json.loads(curl(url, "POST", json.dumps(payload)))
    res = j.get("finance", {}).get("result") or []
    quotes = res[0]["quotes"] if res else []
    total = res[0].get("total", len(quotes)) if res else 0
    if topn:
        quotes = sorted(quotes, key=lambda q: -(q.get("marketCap") or 0))[:topn]
    return quotes, total


def local_date(q):
    t = q.get("regularMarketTime")
    if not t:
        return None
    off = q.get("gmtOffSetMilliseconds") or 0
    return datetime.datetime.utcfromtimestamp(t + off / 1000.0).strftime("%Y-%m-%d")


def main():
    crumb = get_crumb()
    out = {}
    stats = {}
    for key, code, label, topn in MKTS:
        floor = USD_FLOOR * FX[code]
        rec = {"label": label, "code": code, "floor_local": floor,
               "fx": FX[code], "topn": topn, "up": [], "down": [], "universe": []}
        for direction in ("up", "down"):
            try:
                q, tot = screen(crumb, code, floor, direction=direction)
                kept = [x for x in q if local_date(x) == TARGET]
                rec[direction] = kept
                stats[f"{key}_{direction}_total_over_floor"] = tot
                stats[f"{key}_{direction}_kept_session"] = len(kept)
                print(f"{key}/{direction}: total>floor={tot} kept={len(kept)}", flush=True)
            except Exception as e:
                print(f"{key}/{direction}: ERR {e}", flush=True)
                stats[f"{key}_{direction}_error"] = str(e)
            time.sleep(0.8)
        try:
            u, ut = screen(crumb, code, floor, topn=topn)
            rec["universe"] = [x.get("symbol") for x in u]
            stats[f"{key}_universe_total_over_floor"] = ut
            stats[f"{key}_universe_size"] = len(rec["universe"])
            print(f"{key}/universe: over_floor={ut} top{topn}={len(rec['universe'])}", flush=True)
        except Exception as e:
            print(f"{key}/universe: ERR {e}", flush=True)
            stats[f"{key}_universe_error"] = str(e)
        out[key] = rec
        time.sleep(0.8)
    json.dump({"out": out, "stats": stats},
              open(os.path.join(CACHE, "usdfloor.json"), "w"), indent=1, ensure_ascii=False)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
