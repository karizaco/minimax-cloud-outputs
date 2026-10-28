#!/usr/bin/env python3
"""Cloud re-implementation of the skill's 8 screener calls (4 markets x up/down).

Original skill used mcp__tradingview__screen_stocks. That MCP is absent in this
runtime, so this hits the Yahoo v1/finance/screener POST endpoint with the same
filter semantics: |change| > 2%, market_cap > $2B, sorted by |change| desc.
"""
import json, os, subprocess, sys, time

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
CRUMB = open("/workspace/.cache/asia/crumb.txt").read().strip()
CACHE = "/workspace/.cache/asia"

# exchange code -> (market key, friendly name, [extra exchange codes])
MARKETS = {
    "JP":  ("JP", "Japan (TSE)", ["JPX"]),
    "TW":  ("TW", "Taiwan (TWSE)", ["TWO"]),
    "HK":  ("HK", "Hong Kong (HKEX)", ["HKG"]),
    "KR":  ("KR", "Korea (KRX)", ["KOSPI", "KOSDAQ"]),
}


def screen(exchange, direction):
    """direction: 'up' | 'down'. Returns list of quote dicts."""
    op = "GT" if direction == "up" else "LT"
    val = 2 if direction == "up" else -2
    body = {
        "size": 100, "offset": 0,
        "sortField": "percentchange",
        "sortType": "DESC" if direction == "up" else "ASC",
        "quoteType": "EQUITY", "userId": "", "userIdType": "guid",
        "lang": "en-US", "region": "US",
        "query": {"operator": "AND", "operands": [
            {"operator": "EQ", "operands": ["exchange", exchange]},
            {"operator": op, "operands": ["percentchange", val]},
            {"operator": "GT", "operands": ["intradaymarketcap", 2000000000]},
        ]},
    }
    out = os.path.join(CACHE, f"scr_{exchange}_{direction}.json")
    cmd = ["curl", "-s", "--max-time", "25", "-b", "/workspace/.cache/asia/yck.txt",
           "-A", UA, "-H", "Content-Type: application/json", "-X", "POST",
           f"https://query1.finance.yahoo.com/v1/finance/screener?crumb={CRUMB}",
           "-d", json.dumps(body), "-o", out]
    subprocess.run(cmd, capture_output=True)
    try:
        d = json.load(open(out))
    except Exception as e:
        return {"error": f"parse: {e}", "quotes": [], "total": 0}
    r = (d.get("finance") or {}).get("result")
    if not r:
        return {"error": json.dumps(d)[:200], "quotes": [], "total": 0}
    res = r[0]
    return {"quotes": res.get("quotes") or [], "total": res.get("total", 0)}


if __name__ == "__main__":
    results = {}
    for ex in sys.argv[1:]:
        for d in ("up", "down"):
            r = screen(ex, d)
            results[f"{ex}_{d}"] = {"total": r["total"], "error": r.get("error"),
                                   "n": len(r["quotes"])}
            print(f"{ex}_{d}: total={r['total']} n={len(r['quotes'])} err={r.get('error')}")
            time.sleep(0.4)
    json.dump(results, open(os.path.join(CACHE, "screen_summary.json"), "w"), indent=1)
