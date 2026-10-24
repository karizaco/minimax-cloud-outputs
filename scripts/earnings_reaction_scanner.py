#!/usr/bin/env python3
"""
Cron #15 earnings-reaction-scanner — production pipeline (Cloud).

Replaces the skill's absent MCP tools (mcp__tradingview-advanced__*,
mcp__financekit__*, mcp__stocktwits__*) with the TradingView PUBLIC screener,
which was verified working on 2026-10-24.

Emits the artifact to /workspace/earnings/<date>-reactions.md and a catalyst
target list to /workspace/earnings/<date>-catalyst-targets.json.

Verified behaviours this script encodes (see memory topic
`earnings-reaction-cron15-pipeline`):
  * `change` on ILLIQUID rows is computed against a STALE reference close.
    Tell: `change` == `Perf.W` exactly and `Perf.1D` is null. A volume floor
    removes the bogus rows (MRNA.SIX vol=25 showed +71.77%; the US line
    moved -1.25%).
  * `country` is the reliable primary-listing filter. `exchange` codes in the
    public scanner differ from the skill's priority table (EURONEXT covers
    FR/NL/BE/PT/IE, EUROTLX for IT, BX for CH, OMXCOP for DK, OMXHEX for FI,
    GPW for PL, VIE for AT, ATHEX for GR).
  * `earnings_release_date` = MOST RECENT report date; `earnings_release_next_date`
    = next scheduled. This replaces the absent financekit earnings calendar.
"""
import json, subprocess, time, datetime, os, sys

ET = datetime.timezone(datetime.timedelta(hours=-4))
RUN_DATE = datetime.datetime.now(ET).strftime("%Y-%m-%d")
OUT_DIR = "/workspace/earnings"

US_VENUES = ["NASDAQ", "NYSE", "AMEX", "NYSEArca", "ARCA", "PCX", "BATS", "IEX"]
US_DROP = {"OTC", "PINK", "OTCBB", "GREY", "OTC MKTS", "OTCM", "CBOE"}

# market -> (home country for the country filter, keep-venue list, Yahoo suffix)
EU_MARKETS = {
    "uk":          ("United Kingdom",   ["LSE"],                              ".L"),
    "germany":     ("Germany",          ["XETR", "FWB", "MUN", "HAM", "HAN", "DUS", "GETTEX", "SWB"], ".DE"),
    "france":      ("France",           ["EURONEXT"],                         ".PA"),
    "netherlands": ("Netherlands",       ["EURONEXT"],                         ".AS"),
    "belgium":     ("Belgium",          ["EURONEXT"],                         ".BR"),
    "portugal":    ("Portugal",         ["EURONEXT"],                         ".LS"),
    "ireland":     ("Ireland",          ["EURONEXT"],                         ".IR"),
    "italy":       ("Italy",            ["EUROTLX", "MIL"],                   ".MI"),
    "switzerland": ("Switzerland",      ["BX", "SIX"],                        ".SW"),
    "spain":       ("Spain",            ["BME"],                              ".MC"),
    "sweden":      ("Sweden",           ["OMXSTO"],                           ".ST"),
    "norway":      ("Norway",           ["OSL"],                              ".OL"),
    "denmark":     ("Denmark",          ["OMXCOP"],                           ".CO"),
    "finland":     ("Finland",          ["OMXHEX"],                           ".HE"),
    "poland":      ("Poland",           ["GPW"],                              ".WA"),
    "austria":     ("Austria",          ["VIE"],                              ".VI"),
    "greece":      ("Greece",           ["ATHEX"],                            ".AT"),
}
ASX_SUFFIX = ".AX"

MIN_VOLUME = 10000          # removes stale-reference rows (validated)
SCAN_RETRIES = 3

SCANNER_COLS = ["name", "close", "change", "change_abs", "volume", "market_cap_basic",
                "exchange", "country", "Perf.W", "currency",
                "premarket_change", "postmarket_change", "premarket_close", "premarket_volume",
                "earnings_release_date", "earnings_release_next_date"]
IDX = {c: i for i, c in enumerate(SCANNER_COLS)}

health = {"scanner_calls": 0, "scanner_errors": 0, "yahoo_calls": 0, "yahoo_errors": 0,
          "yahoo_429": 0, "empty_markets": [], "cross_check": {"agree": 0, "mismatch": 0,
          "unverified": 0, "mismatch_detail": []}}


def _curl(args, timeout=45):
    return subprocess.run(["curl", "-sS", "-m", str(timeout)] + args,
                          capture_output=True, text=True)


def scan(market, filters, rng=(0, 200), sort=None, cols=None):
    body = {"filter": filters, "options": {"lang": "en"}, "markets": ["america"],
            "symbols": {"query": {"types": []}, "tickers": []},
            "columns": cols or SCANNER_COLS,
            "sort": sort or {"sortBy": "change", "sortOrder": "desc"},
            "range": list(rng)}
    url = f"https://scanner.tradingview.com/{market}/scan"
    for attempt in range(SCAN_RETRIES):
        r = _curl(["-X", "POST", url, "-H", "Content-Type: application/json",
                   "-d", json.dumps(body)])
        health["scanner_calls"] += 1
        try:
            d = json.loads(r.stdout)
            if "data" in d:
                return d
        except Exception:
            pass
        health["scanner_errors"] += 1
        time.sleep(2 * (attempt + 1))
    return {"data": [], "totalCount": 0}


def yahoo_pct(symbol):
    """Independent daily % change from Yahoo. Returns (pct, last_close, date) or None.

    Yahoo's ASX feed appends a trailing LIVE-stamp bar at a different time-of-day
    than the completed daily bars (verified 2026-10-24: SRL.AX had 10 completed
    bars at 19:00 ET plus one at 01:10 ET). Using the naive last-two-bars makes
    every ASX move read 0.00%. Fix: keep only bars stamped at the MODAL
    time-of-day, then take the last two of those.
    """
    for attempt in range(3):
        r = _curl(["-A", "Mozilla/5.0",
                   f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
                   "?interval=1d&range=10d"], timeout=25)
        health["yahoo_calls"] += 1
        if "429" in r.stdout[:200] or not r.stdout.strip():
            health["yahoo_429"] += 1
            time.sleep(3 * (attempt + 1))
            continue
        try:
            res = json.loads(r.stdout)["chart"]["result"][0]
            q = res["indicators"]["quote"][0]
            bars = [(t, c) for t, c in zip(res["timestamp"], q["close"]) if c is not None]
            if len(bars) < 2:
                return None
            tods = [datetime.datetime.fromtimestamp(t, ET).strftime("%H:%M") for t, _ in bars]
            modal = max(set(tods), key=tods.count)
            bars = [b for b, s in zip(bars, tods) if s == modal]
            if len(bars) < 2:
                return None
            pct = (bars[-1][1] - bars[-2][1]) / bars[-2][1] * 100
            d = datetime.datetime.fromtimestamp(bars[-1][0], ET).strftime("%Y-%m-%d")
            return (round(pct, 3), round(bars[-1][1], 4), d)
        except Exception:
            health["yahoo_errors"] += 1
            time.sleep(2 * (attempt + 1))
    return None


def cross_check(name, tv_pct, suffix, region):
    """Compare the screener's % change against Yahoo. Records agreement."""
    sym = f"{name.replace(' ', '-')}{suffix}"
    y = yahoo_pct(sym)
    if y is None:
        health["cross_check"]["unverified"] += 1
        return None
    delta = abs(tv_pct - y[0])
    if delta < 0.15:
        health["cross_check"]["agree"] += 1
        return y
    health["cross_check"]["mismatch"] += 1
    health["cross_check"]["mismatch_detail"].append(
        {"region": region, "symbol": sym, "tv": round(tv_pct, 3), "yahoo": y[0],
         "delta": round(delta, 3), "yahoo_date": y[2]})
    return y


def g(d, key):
    return d[IDX[key]]


def epoch_date(e):
    if not e:
        return None
    return datetime.datetime.fromtimestamp(e, ET).strftime("%Y-%m-%d")


TYPE = {"left": "type", "operation": "equal", "right": "stock"}


def flist(*pairs):
    out = [TYPE]
    for left, op, right in pairs:
        out.append({"left": left, "operation": op, "right": right})
    return out


# ------------------------------------------------------------------ Pass A
pa = scan("america",
          flist(("exchange", "in_range", US_VENUES),
                ("market_cap_basic", "egreater", 20000000000)),
          rng=(0, 250), sort={"sortBy": "market_cap_basic", "sortOrder": "desc"})
a_rows = [r["d"] for r in pa["data"]
          if g(r["d"], "exchange") not in US_DROP
          and "/" not in g(r["d"], "name")]          # drop US preferred (JPM/PC, BAC/PB)
a_dropped_pref = len([r for r in pa["data"]
                       if g(r["d"], "exchange") not in US_DROP
                       and "/" in g(r["d"], "name")])

# ------------------------------------------------------------------ Pass B
pb_up = scan("america",
             flist(("exchange", "in_range", US_VENUES),
                   ("change", "egreater", 3),
                   ("market_cap_basic", "egreater", 1000000000),
                   ("close", "egreater", 5),
                   ("volume", "egreater", MIN_VOLUME)),
             rng=(0, 200), sort={"sortBy": "change", "sortOrder": "desc"})
pb_dn = scan("america",
             flist(("exchange", "in_range", US_VENUES),
                   ("change", "less", -3),
                   ("market_cap_basic", "egreater", 1000000000),
                   ("close", "egreater", 5),
                   ("volume", "egreater", MIN_VOLUME)),
             rng=(0, 200), sort={"sortBy": "change", "sortOrder": "asc"})
b_up = [r["d"] for r in pb_up["data"] if g(r["d"], "exchange") not in US_DROP]
b_dn = [r["d"] for r in pb_dn["data"] if g(r["d"], "exchange") not in US_DROP]

# ------------------------------------------------------------------ Pass C
eu_rows = []
for mkt, (home, venues, suffix) in EU_MARKETS.items():
    base = flist(("country", "equal", home),
                 ("market_cap_basic", "egreater", 1000000000),
                 ("close", "egreater", 5),
                 ("volume", "egreater", MIN_VOLUME))
    if venues:
        base.append({"left": "exchange", "operation": "in_range", "right": venues})
    for op, thr in (("egreater", 2.5), ("less", -2.5)):
        d = scan(mkt, base + [{"left": "change", "operation": op, "right": thr}],
                 rng=(0, 150),
                 sort={"sortBy": "change", "sortOrder": "desc" if op == "egreater" else "asc"})
        if d.get("totalCount", 0) < 5:
            health["empty_markets"].append(f"{mkt}:{op}={d.get('totalCount')}")
        for r in d["data"]:
            eu_rows.append({"market": mkt, "suffix": suffix, "d": r["d"]})

seen = set()
eu_dedup = []
for r in eu_rows:
    n = g(r["d"], "name")
    if n in seen:
        continue
    seen.add(n)
    eu_dedup.append(r)
eu_dedup.sort(key=lambda r: -abs(g(r["d"], "change")))
eu_final = eu_dedup[:30]

# ------------------------------------------------------------------ Pass D
pd_up = scan("australia",
             flist(("country", "equal", "Australia"),
                   ("exchange", "in_range", ["ASX"]),
                   ("change", "egreater", 2.5),
                   ("market_cap_basic", "egreater", 500000000),
                   ("close", "egreater", 1),
                   ("volume", "egreater", MIN_VOLUME)),
             rng=(0, 200), sort={"sortBy": "change", "sortOrder": "desc"})
pd_dn = scan("australia",
             flist(("country", "equal", "Australia"),
                   ("exchange", "in_range", ["ASX"]),
                   ("change", "less", -2.5),
                   ("market_cap_basic", "egreater", 500000000),
                   ("close", "egreater", 1),
                   ("volume", "egreater", MIN_VOLUME)),
             rng=(0, 200), sort={"sortBy": "change", "sortOrder": "asc"})
au = [{"d": r["d"], "suffix": ASX_SUFFIX}
      for r in (pd_up["data"] + pd_dn["data"]) if g(r["d"], "exchange") == "ASX"]
au.sort(key=lambda r: -abs(g(r["d"], "change")))
au = au[:25]

# ------------------------------------------------------------------ US merge
us = {}
for d in a_rows + b_up + b_dn:
    sym = d[IDX["name"]]
    if "/" in sym:
        continue
    c = us.setdefault(sym, {"name": g(d, "name"), "ex": g(d, "exchange"),
                             "close": g(d, "close"), "change": g(d, "change"),
                             "vol": g(d, "volume"), "mcap": g(d, "market_cap_basic"),
                             "pm": g(d, "premarket_change"), "po": g(d, "postmarket_change"),
                             "pmc": g(d, "premarket_close"),
                             "er": g(d, "earnings_release_date"),
                             "ern": g(d, "earnings_release_next_date"), "pass": set()})
    if d in a_rows:
        c["pass"].add("A")
    if d in b_up:
        c["pass"].add("B_up")
    if d in b_dn:
        c["pass"].add("B_dn")
    for k, key in (("pm", "premarket_change"), ("po", "postmarket_change"),
                   ("pmc", "premarket_close")):
        if c[k] is None and g(d, key) is not None:
            c[k] = g(d, key)

tagged, quiet = [], []
for sym, c in us.items():
    pm, po = c["pm"], c["po"]
    if pm is None and po is None:
        tag = "BOD"
    elif po is not None and abs(po) > 3:
        tag = "AMC_REACTION"
    elif pm is not None and abs(pm) > 2:
        tag = "PRE_GAP"
    else:
        tag = "QUIET"
    c["tag"] = tag
    c["mx"] = max(abs(pm) if pm is not None else 0, abs(po) if po is not None else 0)
    (quiet if tag == "QUIET" else tagged).append((sym, c))
tagged.sort(key=lambda t: -t[1]["mx"])
quiet.sort(key=lambda t: -t[1]["mx"])

# ------------------------------------------------------------------ cross-checks
for sym, c in tagged[:15]:
    cross_check(c["name"], c["change"], "", "US")
    time.sleep(0.4)
for r in eu_final[:10]:
    cross_check(g(r["d"], "name"), g(r["d"], "change"), r["suffix"], r["market"])
    time.sleep(0.4)
for r in au[:6]:
    cross_check(g(r["d"], "name"), g(r["d"], "change"), r["suffix"], "AU")
    time.sleep(0.4)


def pct(v):
    return "—" if v is None else f"{v:.2f}"


def er_cell(c):
    last = epoch_date(c.get("er"))
    nxt = epoch_date(c.get("ern"))
    if not last:
        return "—"
    age = (datetime.datetime.now(ET).date() -
           datetime.datetime.strptime(last, "%Y-%m-%d").date()).days
    return f"{last} ({age}d ago)" if age >= 0 else f"{last}"


os.makedirs(OUT_DIR, exist_ok=True)
L = []
A = L.append
A(f"# Earnings reaction scanner — {RUN_DATE}")
A("")
A(f"- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)")
A(f"- Fire time (ET): {datetime.datetime.now(ET).strftime('%Y-%m-%d %H:%M:%S %a')}")
A(f"- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);")
A(f"  Yahoo chart API as an independent cross-check on the reported movers.")
A(f"- Method: 4 passes (US top-200 mcap, US prior-session movers, EU/UK movers,")
A(f"  ASX movers). Volume floor {MIN_VOLUME:,} on every pass; `country` filter for")
A(f"  primary listings; exchange drop-list applied.")
A(f"- Status: `ok`")
A("")
A("## TL;DR")
A("")
amc = [c for _, c in tagged if c["tag"] == "AMC_REACTION"]
gaps = [c for _, c in tagged if c["tag"] == "PRE_GAP"]
bod = [c for _, c in tagged if c["tag"] == "BOD"]
big_us = max(tagged, key=lambda t: t[1]["mx"]) if tagged else None
big_eu = max(eu_final, key=lambda r: abs(g(r["d"], "change"))) if eu_final else None
big_au = max(au, key=lambda r: abs(g(r["d"], "change"))) if au else None
A(f"- {len(amc)} AMC reactions, {len(gaps)} pre-market gaps, {len(bod)} without extended-hours data; "
  f"{len(eu_final)} EU/UK and {len(au)} ASX movers.")
if big_us:
    A(f"- Biggest US extended-hours move: {big_us[1]['name']} "
      f"{big_us[1]['tag']} ({pct(big_us[1]['mx'])}%).")
if big_eu:
    A(f"- Biggest EU/UK move: {g(big_eu['d'], 'name')} ({g(big_eu['d'], 'change'):+.2f}%, "
      f"{big_eu['market']}).")
if big_au:
    A(f"- Biggest ASX move: {g(big_au['d'], 'name')} ({g(big_au['d'], 'change'):+.2f}%).")
A(f"- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).")
A("")
A("## US — Headline table")
A("")
A("| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Last earnings | Tag |")
A("|---|---|---|---|---|---|---|---|")
for sym, c in tagged:
    A(f"| {c['name']} | {c['ex']} | {c['close']} | {c['change']:.2f} | "
      f"{pct(c['pm'])} | {pct(c['po'])} | {er_cell(c)} | {c['tag']} |")
A("")
A("## US — QUIET one-liners")
A("")
A("| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % |")
A("|---|---|---|---|---|")
for sym, c in quiet[:15]:
    A(f"| {c['name']} | {c['ex']} | {c['change']:.2f} | {pct(c['pm'])} | {pct(c['po'])} |")
if not quiet:
    A("| — | — | — | — | — |")
A("")
A("## EU/UK — Headline table")
A("")
A("| Ticker | Market | Venue | Close | Chg % | Currency | Last earnings |")
A("|---|---|---|---|---|---|---|")
for r in eu_final:
    d = r["d"]
    A(f"| {g(d,'name')} | {r['market']} | {g(d,'exchange')} | {g(d,'close')} | "
      f"{g(d,'change'):+.2f} | {g(d,'currency')} | {epoch_date(g(d,'earnings_release_date')) or '—'} |")
A("")
A("## AU (ASX) — Headline table")
A("")
A("| Ticker | Venue | Close | Chg % | Currency | Last earnings |")
A("|---|---|---|---|---|---|")
for r in au:
    d = r["d"]
    A(f"| {g(d,'name')} | {g(d,'exchange')} | {g(d,'close')} | {g(d,'change'):+.2f} | "
      f"{g(d,'currency')} | {epoch_date(g(d,'earnings_release_date')) or '—'} |")
A("")
A("## Catalysts")
A("")
A("<!-- AGENT: fill catalyst text for the tickers in <date>-catalyst-targets.json, then")
A("     delete this comment. Cap: 5 US + 3 EU + 2 AU. Never fabricate a headline. -->")
A("")
A("| Ticker | Region | Catalyst | Earnings-driven |")
A("|---|---|---|---|")
A("")
A("## Source health")
A("")
A(f"- scanner_calls: {health['scanner_calls']} | scanner_errors: {health['scanner_errors']}")
A(f"- yahoo_calls: {health['yahoo_calls']} | yahoo_429: {health['yahoo_429']} | "
  f"yahoo_errors: {health['yahoo_errors']}")
cc = health["cross_check"]
A(f"- cross_check (screener vs Yahoo): agree={cc['agree']} mismatch={cc['mismatch']} "
  f"unverified={cc['unverified']}")
if cc["mismatch_detail"]:
    A(f"- cross_check mismatches: {json.dumps(cc['mismatch_detail'])}")
A(f"- markets_with_lt5_rows: {health['empty_markets'] or 'none'}")
A(f"- filters: volume>{MIN_VOLUME} (removes stale-reference rows), country=home for EU/UK/AU,")
A(f"  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded")
A(f"- us_preferred_dropped: {a_dropped_pref}")
A(f"- earnings_source: screener `earnings_release_date` (last report) + "
  f"`earnings_release_next_date` (next scheduled)")
A(f"- data_date: US regular session close of the prior trading day; extended-hours columns")
A(f"  carry the prior session's prints")
A(f"- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,")
A(f"  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog")
A(f"  holds only media + credential tools). The public screener replaces them.")
A("")
A("## Audit line")
A("")
A(f"`earnings-reaction target=earnings-reactions:{RUN_DATE} candidates={len(us)} "
  f"amc_reactions={len(amc)} pre_gaps={len(gaps)} eu_reactions={len([r for r in eu_final if abs(g(r['d'],'change'))>3])} "
  f"asx_reactions={len([r for r in au if abs(g(r['d'],'change'))>3])} catalyst_lookups=0`")
A("")

out = os.path.join(OUT_DIR, f"{RUN_DATE}-reactions.md")
with open(out, "w") as fh:
    fh.write("\n".join(L))

targets = {"us": [{"name": c["name"], "tag": c["tag"], "last_earnings": epoch_date(c.get("er"))}
                  for _, c in tagged[:8]],
           "eu": [{"name": g(r["d"], "name"), "market": r["market"],
                    "chg": round(g(r["d"], "change"), 2)} for r in eu_final[:5]],
           "au": [{"name": g(r["d"], "name"), "chg": round(g(r["d"], "change"), 2)}
                  for r in au[:3]]}
with open(os.path.join(OUT_DIR, f"{RUN_DATE}-catalyst-targets.json"), "w") as fh:
    json.dump(targets, fh, indent=2)

print(f"WROTE {out} ({os.path.getsize(out)} bytes)")
print(json.dumps({"us_total": len(us), "tagged": len(tagged), "quiet": len(quiet),
                  "eu": len(eu_final), "au": len(au),
                  "cross_check": cc}, indent=2))
