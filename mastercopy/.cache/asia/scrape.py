#!/usr/bin/env python3
"""Cron #2 asia-pre-market-reactions — Yahoo screener REST fetch.

Re-implements the SKILL.md screener semantics (change floor 2%, $2B mcap floor,
primary-listing exchange whitelist) via Yahoo's v1/finance/screener endpoint,
because the TradingView/yahoo MCP layer is absent in this runtime.
"""
import json, os, subprocess, time, urllib.parse

CACHE = "/workspace/.cache/asia"
os.makedirs(CACHE, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
CRUMB_FILE = os.path.join(CACHE, "crumb.txt")
COOKIE_FILE = os.path.join(CACHE, "yck.txt")


def curl(url, method="GET", data=None, headers=None, extra=None, outfile=None):
    cmd = ["curl", "-sS", "-L", "--max-time", "25",
           "-A", UA, "-b", COOKIE_FILE, "-c", COOKIE_FILE]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd += [url]
    if method == "POST":
        cmd = cmd[:-1] + ["-X", "POST", "-H", "Content-Type: application/json", "--data-binary", data, url]
    if extra:
        cmd = cmd[:-1] + extra + [url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"curl rc={r.returncode}: {r.stderr[:300]}")
    return r.stdout


def get_crumb():
    if os.path.exists(CRUMB_FILE):
        c = open(CRUMB_FILE).read().strip()
        if c:
            return c
    # 1. hit fc.yahoo.com for cookies
    curl("https://fc.yahoo.com")
    # 2. hit finance.yahoo.com to complete cookie jar
    curl("https://finance.yahoo.com/")
    for host in ("query2", "query1"):
        out = curl(f"https://{host}.finance.yahoo.com/v1/test/getcrumb").strip()
        if out and " " not in out and len(out) < 40 and "html" not in out.lower():
            open(CRUMB_FILE, "w").write(out)
            return out
    raise RuntimeError("crumb fetch failed")


EXCHANGES = [
    ("JP", "JPX", "Japan (TSE/JPX)"),
    ("TW", "TWO", "Taiwan (TWSE/TPEX)"),
    ("HK", "HKG", "Hong Kong (HKEX)"),
    ("KSC", "KSC", "Korea KOSPI"),
    ("KOE", "KOE", "Korea KOSDAQ"),
]


def screener(crumb, code, direction):
    thr = 2.0 if direction == "up" else -2.0
    op = "GT" if direction == "up" else "LT"
    payload = {
        "size": 100, "offset": 0,
        "sortField": "percentchange",
        "sortType": "DESC" if direction == "up" else "ASC",
        "quoteType": "EQUITY",
        "userId": "", "userIdType": "guid",
        "lang": "en-US", "region": "US",
        "query": {"operator": "AND", "operands": [
            {"operator": "EQ", "operands": ["exchange", code]},
            {"operator": op, "operands": ["percentchange", thr]},
            {"operator": "GT", "operands": ["intradaymarketcap", 2000000000]},
        ]},
    }
    url = f"https://query1.finance.yahoo.com/v1/finance/screener?crumb={urllib.parse.quote(crumb)}"
    body = json.dumps(payload)
    out = curl(url, method="POST", data=body)
    try:
        j = json.loads(out)
    except Exception:
        raise RuntimeError(f"bad json for {code}/{direction}: {out[:300]}")
    if "finance" not in j:
        raise RuntimeError(f"no finance in resp {code}/{direction}: {json.dumps(j)[:300]}")
    res = j["finance"]["result"]
    quotes = res[0]["quotes"] if res else []
    total = res[0].get("total", len(quotes)) if res else 0
    return quotes, total


def main():
    crumb = get_crumb()
    print("crumb ok", flush=True)
    summary = []
    for key, code, label in EXCHANGES:
        for direction in ("up", "down"):
            try:
                quotes, total = screener(crumb, code, direction)
                fn = os.path.join(CACHE, f"scr_{key}_{direction}.json")
                json.dump({"exchange": code, "direction": direction, "total": total,
                           "quotes": quotes}, open(fn, "w"))
                print(f"{key}/{code}/{direction}: total={total} returned={len(quotes)}", flush=True)
                summary.append({"key": key, "code": code, "direction": direction,
                                "total": total, "returned": len(quotes)})
            except Exception as e:
                print(f"{key}/{code}/{direction}: ERROR {e}", flush=True)
                summary.append({"key": key, "code": code, "direction": direction,
                                "total": 0, "returned": 0, "error": str(e)})
            time.sleep(1.0)
    json.dump(summary, open(os.path.join(CACHE, "scr_summary.json"), "w"), indent=2)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
