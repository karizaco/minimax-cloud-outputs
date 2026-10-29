import json, subprocess, os, sys, datetime, time
from urllib.parse import quote

OUT="/workspace/ntrt/_raw"; UA="Mozilla/5.0"
ET=datetime.timezone(datetime.timedelta(hours=-4))

def get(url, timeout=25):
    p=subprocess.run(["curl","-s","-m",str(timeout),"-A",UA,url],capture_output=True,text=True)
    if p.returncode!=0: return {"_error":p.stderr.strip()[:200]}
    t=p.stdout
    if not t.strip(): return {"_error":"empty"}
    try: return json.loads(t)
    except Exception as e: return {"_error":"parse:%s"%e,"_raw":t[:200]}

def _ts(v): return datetime.datetime.fromtimestamp(v, ET)

def chart(sym):
    """Pre-open cross-check pull. Reference close = meta.regularMarketPrice (last completed session close)."""
    u="https://query2.finance.yahoo.com/v8/finance/chart/%s?range=1d&interval=1m&includePrePost=true" % quote(sym)
    r=get(u)
    if isinstance(r,dict) and r.get("_error"): return {"_error":r["_error"],"yahoo_symbol":sym}
    ch=r.get("chart") or {}
    res=ch.get("result") or []
    if not res: return {"_error":(ch.get("error") or {}).get("description","no result"),"yahoo_symbol":sym}
    res=res[0]; meta=res.get("meta") or {}
    ts=res.get("timestamp") or []
    q=((res.get("indicators") or {}).get("quote") or [{}])[0]
    cl=q.get("close") or []; vo=q.get("volume") or []
    vo=vo+[None]*max(0,len(cl)-len(vo))
    pts=[(t,c,v) for t,c,v in zip(ts,cl,vo) if c is not None]
    out={"yahoo_symbol":sym,"previousClose":meta.get("previousClose"),
         "chartPreviousClose":meta.get("chartPreviousClose"),
         "regularMarketPrice":meta.get("regularMarketPrice"),"regularMarketTime":meta.get("regularMarketTime"),
         "gmtoffset_sec":meta.get("gmtoffset"),"tz":meta.get("exchangeTimezoneName"),
         "currency":meta.get("currency"),"exchangeName":meta.get("exchangeName"),
         "fullExchangeName":meta.get("fullExchangeName"),"n_bars":len(pts)}
    if not pts: return {**out,"_error":"no bars"}
    today=_ts(pts[-1][0]).strftime("%Y-%m-%d")
    days={}
    for t,c,v in pts: days.setdefault(_ts(t).strftime("%Y-%m-%d"),[]).append((t,c,v))
    out["days_present"]=sorted(days.keys())
    out["ref_close"]=meta.get("regularMarketPrice")
    if meta.get("regularMarketTime"):
        out["ref_close_et"]=_ts(meta["regularMarketTime"]).strftime("%Y-%m-%d %H:%M ET")
    pre=days.get(today,[])
    # premarket = today's bars before 09:30 ET
    pre=[p for p in pre if _ts(p[0]).strftime("%H:%M") < "09:30"]
    if pre:
        out["pre_n"]=len(pre)
        out["pre_last"]=pre[-1][1]
        out["pre_last_ts"]=pre[-1][0]
        out["pre_last_et"]=_ts(pre[-1][0]).strftime("%Y-%m-%d %H:%M:%S ET")
        out["pre_last_vol"]=pre[-1][2]
        out["pre_high"]=max(p[1] for p in pre); out["pre_low"]=min(p[1] for p in pre)
        if out.get("ref_close"):
            out["pre_pct"]=round((pre[-1][1]/out["ref_close"]-1)*100,4)
            out["pre_pct_hi"]=round((out["pre_high"]/out["ref_close"]-1)*100,4)
            out["pre_pct_lo"]=round((out["pre_low"]/out["ref_close"]-1)*100,4)
    else:
        out["pre_n"]=0
    return out

def spark(sym):
    """Last completed regular session (range=1d resolves to the prior session pre-open)."""
    u="https://query2.finance.yahoo.com/v8/finance/spark?symbols=%s&range=1d&interval=1m" % quote(sym, safe=",")
    r=get(u)
    if isinstance(r,dict) and r.get("_error"): return {"_error":r["_error"]}
    if not isinstance(r,dict): return {"_error":"bad type"}
    s=r.get(sym)
    if not s: return {"_error":"not in response","keys":list(r.keys())[:5]}
    ts=s.get("timestamp") or []; cl=s.get("close") or []
    pts=[(t,c) for t,c in zip(ts,cl) if c is not None]
    o={"previousClose":s.get("previousClose"),"chartPreviousClose":s.get("chartPreviousClose"),
       "fulldayPrice":s.get("fulldayPrice"),"fulldayChangePercent":s.get("fulldayChangePercent"),
       "n_bars":len(pts)}
    if pts:
        o["session_last_close"]=cl[-1]
        o["session_date"]=_ts(pts[-1][0]).strftime("%Y-%m-%d")
        o["session_last_et"]=_ts(pts[-1][0]).strftime("%Y-%m-%d %H:%M ET")
        o["session_open"]=cl[0]
    return o

def resolve(q):
    r=get("https://query2.finance.yahoo.com/v1/finance/search?q=%s&quotesCount=12&newsCount=0" % quote(q))
    if isinstance(r,dict) and r.get("_error"): return []
    out=[]
    for x in (r.get("quotes") or []):
        if x.get("symbol") and x.get("quoteType") in ("EQUITY","ETF"):
            out.append({"symbol":x["symbol"],"exch":x.get("exchDisp"),
                        "name":x.get("longname") or x.get("shortname"),"type":x.get("quoteType")})
    return out

def fetch(tk, alt_query=None):
    """Return dict with best available: chart + spark, plus resolution notes."""
    res={"ticker":tk,"notes":[]}
    c=chart(tk)
    if "_error" in c or c.get("pre_n",0)==0:
        res["notes"].append("chart:%s"%(c.get("_error") or "no premarket bars"))
        s=spark(tk)
        if "_error" not in s: res["spark"]=s
        # try alternates
        cands=[]
        for q in filter(None,[alt_query, tk]):
            for m in resolve(q):
                if m["symbol"]!=tk and m not in cands: cands.append(m)
        for m in cands[:6]:
            if "alt" in res: break
            c2=chart(m["symbol"])
            if "_error" not in c2 and c2.get("pre_n",0)>0:
                res["alt"]=m; res["alt_chart"]=c2; res["notes"].append("alt=%s(%s)"%(m["symbol"],m["exch"]))
                break
            s2=spark(m["symbol"])
            if "_error" not in s2 and s2.get("session_last_close"):
                res["alt"]=m; res["alt_spark"]=s2; res["notes"].append("alt_spark=%s(%s)"%(m["symbol"],m["exch"]))
                break
    else:
        res["chart"]=c
    if "chart" not in res and "alt_chart" in res: res["chart"]=res["alt_chart"]
    if "spark" not in res and "alt_spark" in res: res["spark"]=res["alt_spark"]
    return res

if __name__=="__main__":
    tag=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 30
    rows=json.load(open(os.path.join(OUT,"tv_screen_%s.json"%tag)))["rows"]
    sel=rows[:n]
    ALTS={"VLKPF":"Volkswagen","OSCUF":"Japan Exchange Group","YDES":"YD Bio",
          "ELVR":"Elevra Lithium","BESVF":"BE Semiconductor","ITJTY":"Intrum",
          "AAIGF":"AIA Group","IVBXF":"Innovent","ATEYY":"Advantest"}
    out={}
    for r in sel:
        tk=r["ticker"]
        out[tk]=fetch(tk, ALTS.get(tk))
        time.sleep(0.10)
    payload={"tag":tag,"n":len(sel),
             "utc":datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
             "data":out}
    fn=os.path.join(OUT,"yahoo_%s.json"%tag)
    json.dump(payload,open(fn,"w"),indent=1)
    noref=[t for t,v in out.items() if not v.get("chart") and not v.get("spark")]
    print("wrote",fn,"n",len(out),"no-data:",noref)
    for t,v in out.items():
        if v.get("notes"): print("  ",t,v["notes"])
