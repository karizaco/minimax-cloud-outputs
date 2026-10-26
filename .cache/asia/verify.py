#!/usr/bin/env python3
"""Cross-verify screener %change against the Yahoo chart endpoint + fetch names.

Defect rule from the pipeline memory: for INDICES the last populated bar in the
close series is the PREVIOUS session, and meta.regularMarketPrice carries
today's close. For single STOCKS the series does include today's bar, so
pairs[-1] vs pairs[-2] is valid -- but the series must be filtered to non-None
closes first.
"""
import json, os, subprocess, datetime, sys

CACHE = "/workspace/.cache/asia"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
OFFSET = {"JP": 9, "TW": 8, "HK": 8, "KR": 9}


def curl(url, out):
    subprocess.run(["curl", "-s", "--max-time", "20", "-A", UA, url, "-o", out],
                   capture_output=True)


def chart(sym):
    p = os.path.join(CACHE, f"ch_{sym.replace('^','IDX_').replace('.','_')}.json")
    if not os.path.exists(p):
        curl(f"https://query1.finance.yahoo.com/v8/finance/chart/"
             f"{sym.replace('^','%5E')}?range=10d&interval=1d", p)
    try:
        r = json.load(open(p))["chart"]["result"][0]
    except Exception as e:
        return {"err": str(e)}
    m = r["meta"]
    closes = [c for c in r["indicators"]["quote"][0]["close"] if c is not None]
    ts = r.get("timestamp") or []
    pairs = [(t, c) for t, c in zip(ts, r["indicators"]["quote"][0]["close"])
             if c is not None]
    out = {
        "sym": sym, "price": m.get("regularMarketPrice"),
        "pct_meta": m.get("regularMarketChangePercent"),
        "prev_close": m.get("chartPreviousClose") or m.get("previousClose"),
        "time": m.get("regularMarketTime"),
        "currency": m.get("currency"),
        "name": m.get("shortName") or m.get("longName"),
        "n_bars": len(pairs),
        "last_bar_date": (datetime.datetime.utcfromtimestamp(pairs[-1][0]).strftime("%Y-%m-%d")
                          if pairs else None),
        "last_bar_close": pairs[-1][1] if pairs else None,
        "prev_bar_close": pairs[-2][1] if len(pairs) > 1 else None,
    }
    if len(pairs) > 1 and out["prev_bar_close"]:
        out["pct_series"] = round((out["last_bar_close"] / out["prev_bar_close"] - 1) * 100, 2)
    return out


def name_of(sym):
    p = os.path.join(CACHE, f"nm_{sym.replace('.','_').replace('^','IDX_')}.json")
    if not os.path.exists(p):
        curl(f"https://query2.finance.yahoo.com/v1/finance/search?q={sym}"
             f"&quotesCount=1&newsCount=0", p)
    try:
        q = json.load(open(p))["quotes"][0]
        return {"shortname": q.get("shortname"), "longname": q.get("longname"),
                "exchange": q.get("exchDisp"), "sector": q.get("sector"),
                "industry": q.get("industry")}
    except Exception as e:
        return {"err": str(e)}


if __name__ == "__main__":
    for sym in sys.argv[1:]:
        c = chart(sym)
        n = name_of(sym)
        print(json.dumps({"chart": c, "name": n}, default=str))
