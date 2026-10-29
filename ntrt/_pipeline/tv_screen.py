import json, subprocess, sys, os, datetime

OUT = "/workspace/ntrt/_raw"
STAMP = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

COLS = ["name","description","close","change","premarket_close","premarket_change",
        "premarket_volume","volume","market_cap_basic","exchange","sector",
        "price_earnings_ttm","relative_volume_10d_calc","Perf.W","Perf.1M","Perf.Y"]
IDX = {c:i for i,c in enumerate(COLS)}

def post(url, body, timeout=30):
    p = subprocess.run(["curl","-s","-m",str(timeout),"-X","POST",url,
        "-H","Content-Type: application/json","-H","User-Agent: Mozilla/5.0",
        "-H","Origin: https://www.tradingview.com",
        "--data-binary","@-"], input=json.dumps(body), capture_output=True, text=True)
    if p.returncode != 0:
        return {"_error": p.stderr.strip()[:300], "_rc": p.returncode}
    try:
        return json.loads(p.stdout)
    except Exception as e:
        return {"_error": "json parse: %s" % e, "_raw": p.stdout[:300]}

def g(d, col):
    i = IDX[col]
    return d[i] if d and len(d) > i else None

def scan(flt, sort_order, n=60, cols=None):
    body = {"filter": flt, "options": {"lang":"en"}, "markets":["america"],
            "symbols":{"query":{"types":[]},"tickers":[]},
            "columns": cols or COLS,
            "sort":{"sortBy":"premarket_change","sortOrder":sort_order},
            "range":[0,n]}
    return post("https://scanner.tradingview.com/america/scan", body)

MC = {"left":"market_cap_basic","operation":"greater","right":200000000}

def run(tag, n=60):
    out = {"tag":tag,"utc":STAMP,"rows":[],"errors":[],
           "screen": {"premarket_change_in":[3,1000],"market_cap_basic_gt":200000000,
                      "markets":["america"],"sort":"premarket_change"}}
    for label, rng, so in [("up",[3,1000],"desc"),("down",[-1000,-3],"asc")]:
        flt = [{"left":"premarket_change","operation":"in_range","right":rng}, MC]
        r = scan(flt, so, n)
        if not isinstance(r, dict) or "data" not in r or r.get("error"):
            out["errors"].append({"side":label,"resp":str(r)[:300]}); continue
        out[label+"_totalCount"] = r.get("totalCount")
        for d in (r.get("data") or []):
            if not d.get("s"): continue
            v = d.get("d") or []
            out["rows"].append({
              "tv_symbol": d["s"], "ticker": g(v,"name"),
              "name": g(v,"description"), "close": g(v,"close"), "change": g(v,"change"),
              "premarket_close": g(v,"premarket_close"), "premarket_change": g(v,"premarket_change"),
              "premarket_volume": g(v,"premarket_volume"), "volume": g(v,"volume"),
              "market_cap_basic": g(v,"market_cap_basic"), "exchange": g(v,"exchange"),
              "sector": g(v,"sector"), "pe_ttm": g(v,"price_earnings_ttm"),
              "relative_volume_10d": g(v,"relative_volume_10d_calc"),
              "perf_week": g(v,"Perf.W"), "perf_month": g(v,"Perf.1M"), "perf_year": g(v,"Perf.Y"),
              "side": label})
    # universe census (no filters except premarket screen absent)
    r = scan([], "desc", 1, cols=["name"])
    out["universe_total"] = r.get("totalCount") if isinstance(r, dict) else None
    # market cap census for reference
    r2 = scan([MC], "desc", 1, cols=["name"])
    out["universe_over_200m_cap"] = r2.get("totalCount") if isinstance(r2, dict) else None

    best = {}
    for r in out["rows"]:
        t = r["ticker"]
        if t not in best or abs(r.get("premarket_change") or 0) > abs(best[t].get("premarket_change") or 0):
            best[t] = r
    out["rows"] = sorted(best.values(), key=lambda r: -abs(r.get("premarket_change") or 0))
    out["row_count"] = len(out["rows"])
    fn = os.path.join(OUT, "tv_screen_%s.json" % tag)
    with open(fn,"w") as f: json.dump(out,f,indent=1)
    print("%s -> %s rows=%d universe=%s cap>200m=%s up_tc=%s down_tc=%s errors=%d" % (
        tag, fn, out["row_count"], out["universe_total"], out["universe_over_200m_cap"],
        out.get("up_totalCount"), out.get("down_totalCount"), len(out["errors"])))
    return out

if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv)>1 else "pull1", int(sys.argv[2]) if len(sys.argv)>2 else 60)
