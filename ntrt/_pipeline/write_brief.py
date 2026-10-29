# -*- coding: utf-8 -*-
import json, datetime, statistics, sys
sys.path.insert(0,"/workspace/ntrt/_pipeline")
import importlib.util
spec=importlib.util.spec_from_file_location("rb","/workspace/ntrt/_pipeline/render_brief.py")
# reuse helpers by re-implementing minimally here
ET=datetime.timezone(datetime.timedelta(hours=-4))
R="/workspace/ntrt/_raw"
tv=json.load(open(f"{R}/tv_screen_pull4.json")); yh=json.load(open(f"{R}/yahoo_pull4.json"))
def _u(s): return datetime.datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc).astimezone(ET)
NOW=_u(yh["utc"])   # ages are measured AS OF the read, not wall-clock now
rows={r["ticker"]:r for r in tv["rows"]}; Y=yh["data"]
CAT=json.load(open(f"{R}/catalysts.json"))
def f2(x,n=2): return ("%."+str(n)+"f")%x if x is not None else "-"
def fm(x): return "{:,.0f}".format(x) if x is not None else "-"
def status(tk):
    v=Y.get(tk) or {}; c=v.get("chart") or {}; sp=v.get("spark") or {}
    r=rows[tk]; notes=v.get("notes") or []; ys=c.get("yahoo_symbol")
    alt=any(n.startswith("alt") for n in notes)
    yref = c.get("ref_close") if ("chart" in v and not alt) else sp.get("session_last_close")
    refdev=(r["close"]-yref)/yref*100 if (yref and r["close"]) else None
    same=(ys==tk) if ys else False
    ypre=c.get("pre_pct") if same else None
    age=(NOW-datetime.datetime.fromtimestamp(c["pre_last_ts"],ET)).total_seconds()/60 if (same and c.get("pre_last_ts")) else None
    spread=(ypre-r["premarket_change"]) if ypre is not None else None
    if not (v.get("chart") or v.get("spark")): lab="not cross-checked"
    elif not same and not (c.get("pre_last_ts") or (ys==tk)): lab="no second-feed mark"
    elif not same: lab="home-listing only"
    elif refdev is not None and abs(refdev)>0.5: lab="REF MISMATCH"
    elif age is not None and age>45: lab="stale print"
    elif (r["premarket_volume"] or 0)<20000: lab="thin book"
    else: lab="cross-checked"
    return dict(lab=lab,refdev=refdev,ypre=ypre,spread=spread,age=age,ys=ys,alt=alt)
order=sorted(rows.values(), key=lambda r:-abs(r["premarket_change"] or 0))
def tbl(rs,start=1):
    L=["| # | Ticker | Company | Prior close | Pre-open mark | Gap % | Yahoo pre % | Spread (pp) | Print age | Pre-mkt vol | Mcap ($m) | QC |",
       "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for i,r in enumerate(rs,start):
        tk=r["ticker"]; s=status(tk)
        L.append("| %d | **%s** | %s | %s | %s | %+.2f | %s | %s | %s | %s | %s | %s |"%(i,tk,(r["name"] or "")[:30],
          f2(r["close"]),f2(r["premarket_close"]),r["premarket_change"],
          f2(s["ypre"]) if s["ypre"] is not None else "n/a",
          ("%+.2f"%s["spread"]) if s["spread"] is not None else "n/a",
          ("<1 min" if s["age"]<1 else "%.0f min"%s["age"]) if s["age"] is not None else "n/a",
          fm(r["premarket_volume"]), fm(r["market_cap_basic"]/1e6 if r["market_cap_basic"] else None), s["lab"]))
    return "\n".join(L)
json.dump({"top":[r["ticker"] for r in order[:20]],"nxt":[r["ticker"] for r in order[20:40]]}, open(f"{R}/order.json","w"))
print(tbl(order[:20]))
print()
print(tbl(order[20:40],21))
