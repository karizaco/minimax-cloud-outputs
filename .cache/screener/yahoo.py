#!/usr/bin/env python3
"""Yahoo Finance helper for cron #9 (Cloud).

Rules learned the hard way (2026-10-26):
  * User-Agent MUST be the short "Mozilla/5.0" -- the long Chrome UA gets 429'd by Yahoo's edge.
  * Use curl via subprocess, not urllib (urllib's fingerprint is 429'd too).
  * /v8/finance/chart/ does NOT accept comma-separated symbols (404). Use spark for batches.
  * query2 is tried before query1.
"""
import json
import subprocess
import time
import urllib.parse

UA = "Mozilla/5.0"
HOSTS = ["query2", "query1"]


def _curl(url, tries=3):
    for i in range(tries):
        p = subprocess.run(
            ["curl", "-s", "--max-time", "45", "-H", f"User-Agent: {UA}", url],
            capture_output=True, text=True,
        )
        if p.returncode != 0:
            time.sleep(1.0 + i)
            continue
        t = p.stdout.strip()
        if not t:
            time.sleep(1.0 + i)
            continue
        try:
            return json.loads(t)
        except json.JSONDecodeError:
            time.sleep(1.0 + i)
    return None


def chart(symbol, rng="1y", interval="1d"):
    """Return (meta, bars) where bars = [(epoch, o, h, l, c, v), ...]."""
    sym = urllib.parse.quote(symbol, safe="")
    for h in HOSTS:
        url = (f"https://{h}.finance.yahoo.com/v8/finance/chart/{sym}"
               f"?range={rng}&interval={interval}&includePrePost=false")
        j = _curl(url)
        if not j or "chart" not in j:
            continue
        res = j.get("chart", {}).get("result")
        if not res:
            err = j.get("chart", {}).get("error")
            return {"error": err}
        r = res[0]
        meta = r.get("meta", {})
        ts = r.get("timestamp") or []
        q = r.get("indicators", {}).get("quote", [{}])[0]
        o, h2, l, c, v = (q.get(k) or [] for k in ("open", "high", "low", "close", "volume"))
        bars = []
        for i, t in enumerate(ts):
            vals = [o[i] if i < len(o) else None, h2[i] if i < len(h2) else None,
                    l[i] if i < len(l) else None, c[i] if i < len(c) else None,
                    v[i] if i < len(v) else None]
            if vals[3] is None:
                continue
            bars.append((t, *vals))
        return {"meta": meta, "bars": bars}
    return {"error": "chart_unavailable"}


def spark(symbols):
    """Batched quotes. symbols = list of ticker strings."""
    syms = urllib.parse.quote(",".join(symbols), safe=",")
    for h in HOSTS:
        url = (f"https://{h}.finance.yahoo.com/v8/finance/spark?symbols={syms}"
               f"&range=1d&interval=1m")
        j = _curl(url)
        if not j:
            continue
        out = {}
        for s in (j.get("spark", {}) or {}).get("result", []) or []:
            sym = (s.get("symbol") or "")
            resp = s.get("response", [{}])[0]
            meta = resp.get("meta", {})
            out[sym] = {
                "regularMarketPrice": meta.get("regularMarketPrice"),
                "previousClose": meta.get("previousClose") or meta.get("chartPreviousClose"),
                "regularMarketTime": meta.get("regularMarketTime"),
                "gmtoffset": meta.get("gmtoffset"),
                "exchangeTimezoneName": meta.get("exchangeTimezoneName"),
                "currency": meta.get("currency"),
            }
        if out:
            return out
    return {}


if __name__ == "__main__":
    import sys
    if sys.argv[1] == "chart":
        r = chart(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "1y")
        m = r.get("meta", {})
        print(json.dumps({
            "symbol": m.get("symbol"), "price": m.get("regularMarketPrice"),
            "previousClose": m.get("previousClose") or m.get("chartPreviousClose"),
            "regularMarketTime": m.get("regularMarketTime"),
            "gmtoffset": m.get("gmtoffset"),
            "tz": m.get("exchangeTimezoneName"),
            "bars": len(r.get("bars", [])),
            "last_bar": r.get("bars", [None])[-1] if r.get("bars") else None,
        }, indent=2))
    elif sys.argv[1] == "spark":
        print(json.dumps(spark(sys.argv[2].split(",")), indent=2))
