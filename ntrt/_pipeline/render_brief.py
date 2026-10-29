# -*- coding: utf-8 -*-
import json, datetime, statistics, os
ET=datetime.timezone(datetime.timedelta(hours=-4))
NOW=datetime.datetime.now(ET)
R="/workspace/ntrt/_raw"

tv=json.load(open(f"{R}/tv_screen_pull4.json"))
tv3=json.load(open(f"{R}/tv_screen_pull3.json"))
yh=json.load(open(f"{R}/yahoo_pull4.json"))
rows={r["ticker"]:r for r in tv["rows"]}
m3={r["ticker"]:r for r in tv3["rows"]}
Y=yh["data"]

CAT={
 "BRAI":("No company release found. Technical/AI-narrative rebound off Monday's -40.28% washout (closed $2.12 after a $4.28 open, $5.05 high, ~$2.10 low).","StocksToTrade 10-27 07:48/08:32 ET; Simply Wall St 10-27"),
 "ARTV":("Permanently discontinued AlloNK (AB-101) allogeneic NK cell therapy after two Grade 5 safety events (fatal leukoencephalopathy assessed as likely fludarabine neurotoxicity; a second death assessed unrelated); ~94% workforce cut; Leerink Partners engaged on strategic alternatives incl. merger, asset sale, licensing or liquidation; Nov 9 webcast cancelled; ~$319.1m cash at Sep 30.","Reuters 10-27; GlobeNewswire 10-27"),
 "MFIC":("Ares Capital (ARCC) definitive merger agreement, $10.88/share ($1.21 cash + $9.67 ARCC stock), ~$2.6bn EV, a 30.1% premium to the Oct 26 close and 25.8% to 30-day VWAP; MFIC preliminary NAV $12.86 (Sep 30); special dividend of undistributed taxable income expected before closing; buyback suspended; close expected 1H27.","BusinessWire 10-27 06:39 ET; MFIC 8-K"),
 "KNSA":("Q3-26 results pre-market: revenue $286.0m (+58% y/y), net income $47.3m / $0.56 EPS, adj. EBITDA margin up; 2026 ARCALYST guidance raised to $1.045-1.050bn from $980-995m; KPL-387 Phase 3 data 2H27; $568.8m cash, no debt.","GlobeNewswire 10-27; call 08:30 ET"),
 "JBLU":("Q3 reported a day early (Oct 26): adj. loss $0.60 vs $0.54 expected, revenue $2.81bn (+21.1%), RASM +18.4%, Q4 RASM guided +18-22%, operating margin +1-2pp, targets >=$1 EPS and positive FCF in 2028. Monday closed at an all-time low after senior creditors hired a restructuring adviser.","JetBlue IR 10-26; Bloomberg 10-27"),
 "INIO":("Q3 record results: revenue $1.2bn (+57%), net income $109.2m (+176%), adj. EBITDA $245.4m (+70%); FY26 revenue guide raised to $3.9-4.0bn, adj. EBITDA to $780-800m; record $8.0bn equipment backlog (+142%); 620MW follow-on and a 450MW Liberty Energy order.","GlobeNewswire 10-27 06:30 ET; 8-K"),
 "INOD":("No company press release found. Leading candidate: a report that InnoData laid off ~550 employees in India on Oct 26, with further cuts reported in the Philippines - NOT publicly confirmed by the company. Q3 due Nov 5.","news24online 10-27 13:49 IST; Benzinga premarket movers"),
 "CLS":("Q3 revenue $5.83bn (+83%), adj. EPS $3.30 vs ~$2.96-3.02 est., record adj. op margin 8.5%; FY26 revenue raised to $21.0bn and adj. EPS to $11.55; initial FY27 outlook revenue $40.0bn (+90%), adj. margin 9.0%, adj. EPS $21.50; 2028 demand seen 'meaningfully higher'; $3.45bn equity offering completed in Q3.","Celestica 8-K / GlobeNewswire 10-26 16:17 ET"),
 "SOFI":("Q3 record adjusted net revenue $1.4bn (+44%), adj. EBITDA $469.8m (+70%), GAAP net income $241.0m / $0.18 EPS, 12th straight profitable quarter, Rule of 40 score 79; members 17.1m (+35%), originations $16.9bn (+71%); FY26 guidance raised to $5.04bn / $1.66bn / $0.61 EPS; 2027 outlook $6.4bn / $2.24bn / $0.90 EPS.","SoFi IR 10-27; Reuters 10-27"),
 "WSO":("Q3 results (Oct 27): record revenue $2.22bn (+7%, +4% same-store), gross margin 26.4% vs 27.5% LY, operating income -4% to $225m (margin 10.1% vs 11.4%), EPS -5% to $3.77; 9M operating cash flow +79% to $304m; Jackson Supply and The Granite Group acquisitions. Call 10:00 ET.","Watsco 8-K / GlobeNewswire 10-27"),
 "FER":("Ferrovial ADR. Cited in Barron's premarket movers at +9.1%. No company release located in this run - not researched in depth.","Barron's 10-27 07:30 ET"),
 "ITJTY":("NOT CORROBORATED - do not trade the mark. Home listing INTRUM.ST was ~1.712 SEK vs 1.714 prior close at 09:08 ET (flat). Q3 (Oct 23) missed on adjusted operating profit; SEB, UBS, ABG Sundal Collier and SB1 Markets all cut price targets Oct 23-26; CFO bought 300,000 shares at SEK 1.72 on Oct 27.","MarketScreener 10-27; CNBC IJU-DE"),
}
RESEARCHED=set(CAT.keys())

def f2(x,n=2):
    return ("%."+str(n)+"f")%x if x is not None else "-"
def fm(x):
    if x is None: return "-"
    return "{:,.0f}".format(x)

def yrow(tk):
    v=Y.get(tk) or {}
    c=v.get("chart") or {}
    sp=v.get("spark") or {}
    notes=v.get("notes") or []
    # listing of the Yahoo symbol actually used
    ys=c.get("yahoo_symbol") or sp.get("yahoo_symbol")
    home = any(k.startswith("alt") for k in notes) and ys and not any(ys==t for t in [tk])
    return v,c,sp,ys,home

def status(tk):
    """(label, refdev%, ypre%, spread, age_min, note)"""
    v=Y.get(tk) or {}; c=v.get("chart") or {}; sp=v.get("spark") or {}
    r=rows[tk]
    notes=v.get("notes") or []
    ys=c.get("yahoo_symbol")
    # reference close check
    yref=c.get("ref_close") if "chart" in v and not any(n.startswith("alt") for n in notes) else sp.get("session_last_close")
    refdev=None
    if yref and r["close"]:
        refdev=(r["close"]-yref)/yref*100
    # yahoo premarket pct, only if the Yahoo symbol is the SAME listing as the TV row
    same_listing = (ys==tk) if ys else False
    ypre=c.get("pre_pct") if same_listing else None
    age=None
    if same_listing and c.get("pre_last_ts"):
        age=(NOW-datetime.datetime.fromtimestamp(c["pre_last_ts"],ET)).total_seconds()/60
    spread=(ypre-r["premarket_change"]) if (ypre is not None) else None
    if not (v.get("chart") or v.get("spark")):
        lab="not cross-checked (outside top 30)"
    elif not same_listing:
        lab="home-listing only"
    elif refdev is not None and abs(refdev)>0.5:
        lab="REF MISMATCH"
    elif age is not None and age>45:
        lab="stale print"
    elif r["premarket_volume"] is not None and r["premarket_volume"]<20000:
        lab="thin book"
    else:
        lab="cross-checked"
    return lab,refdev,ypre,spread,age,ys

order=sorted(rows.values(), key=lambda r:-abs(r["premarket_change"] or 0))
TOP=order[:20]; NEXT=order[20:40]

def tbl(rs):
    out=[]
    out.append("| # | Ticker | Company | Prior close | Pre-open mark | Gap % | Yahoo pre % | Spread (pp) | Print age | Pre-mkt vol | Mcap ($m) | QC |")
    out.append("|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    for i,r in enumerate(rs,1):
        tk=r["ticker"]
        lab,refdev,ypre,spread,age,ys=status(tk)
        gap=r["premarket_change"]
        s="" if spread is None else "%+.2f"%spread
        out.append("| %d | **%s** | %s | %s | %s | %+.2f | %s | %s | %s | %s | %s | %s |"%(
            i,tk,(r["name"] or "")[:30],
            f2(r["close"],2),f2(r["premarket_close"],2),gap,
            f2(ypre) if ypre is not None else "n/a", s,
            ("%.0f min"%age) if age is not None else "n/a",
            fm(r["premarket_volume"]),fm(r["market_cap_basic"]/1e6 if r["market_cap_basic"] else None),
            lab))
    return "\n".join(out)

# spreads across the 4 TV reads
files=[f"{R}/tv_screen_pull{i}.json" for i in (1,2,3,4)]
ms=[{r["ticker"]:r for r in json.load(open(f))["rows"]} for f in files]
def tv_range(tk):
    vals=[m[tk]["premarket_change"] for m in ms if tk in m and m[tk]["premarket_change"] is not None]
    return (max(vals)-min(vals)) if len(vals)>=2 else None
pair=[]
for i,(a,b) in enumerate(zip(ms,ms[1:]),1):
    d=[abs(b[t]["premarket_change"]-a[t]["premarket_change"]) for t in a if t in b
       and a[t]["premarket_change"] is not None and b[t]["premarket_change"] is not None]
    pair.append((i,len(d),statistics.median(d),max(d)))
yp=[]
for i,(a,b) in enumerate([(json.load(open(f"{R}/yahoo_pull1.json"))["data"],json.load(open(f"{R}/yahoo_pull3.json"))["data"]),
                           (json.load(open(f"{R}/yahoo_pull3.json"))["data"],yh["data"])],1):
    d=[]
    for t,v in a.items():
        c1=(v.get("chart") or {}); c2=((b.get(t) or {}).get("chart") or {})
        if "pre_pct" in c1 and "pre_pct" in c2 and c1.get("yahoo_symbol")==c2.get("yahoo_symbol")==t:
            d.append(abs(c1["pre_pct"]-c2["pre_pct"]))
    yp.append((i,len(d),statistics.median(d) if d else 0,max(d) if d else 0))

flags=[]
for r in order:
    tk=r["ticker"]
    lab,refdev,ypre,spread,age,ys=status(tk)
    if lab!="cross-checked":
        flags.append((tk,lab,refdev,age,r["premarket_volume"]))

# largest cross-feed divergence among live same-listing rows
div=[]
for r in order[:30]:
    tk=r["ticker"]; lab,refdev,ypre,spread,age,ys=status(tk)
    if spread is not None: div.append((abs(spread),tk,spread,r["premarket_change"],ypre))
div.sort(reverse=True)

json.dump({"flags":flags,"div":div,"pair":pair,"yp":yp}, open(f"{R}/qc_summary.json","w"), indent=1, default=str)
print("\n".join(tbl(TOP)))
print()
print("FLAGS:")
for f in flags: print("  ",f)
print("\nDIVERGENCE:",div[:6])
print("TV read pairs:",pair)
print("Yahoo read pairs:",yp)
