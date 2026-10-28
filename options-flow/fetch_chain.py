#!/usr/bin/env python3
"""
Cron #16 - unusual options flow - Yahoo Finance options chain fetcher.

Reproduces `mcp__tradingview-advanced__stock_options_unusual_activity`
semantics locally: top_n=10, min_volume=100, expiries=4.

Auth path (verified 2026-10-21, re-verified 2026-10-28):
  1. GET the quote page with a CLEAN jar (-c only, NO -b) and Accept: text/html
  2. scrape "crumb":"..." from the page bootstrap
  3. GET query2 .../v7/finance/options/<SYM>?crumb=<CRUMB> with -b jar -c jar
     and a Referer. Do NOT send Accept: text/html to the API (HTTP 406).

Writes raw chain JSON to data/ and a normalised row set to data/rows.json
"""
import json, os, re, subprocess, sys, time, datetime, zoneinfo, urllib.parse

ET = zoneinfo.ZoneInfo("America/New_York")
SYM_DATE = sys.argv[1] if len(sys.argv) > 1 else datetime.datetime.now(ET).strftime("%Y-%m-%d")
BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
os.makedirs(DATA, exist_ok=True)

# Pass B universe (watchlist.yaml absent -> Pass B only, per skill hard rule)
TICKERS = ["IWM", "GLD", "TLT", "AAPL", "MSFT", "NVDA", "GOOGL", "AMZN"]
EXCLUDED = ["SPY", "QQQ", "SOXL", "SOXS", "SMH", "TQQQ", "SQQQ", "UVXY", "VXX"]

UA = "Mozilla/5.0"
MIN_VOLUME = 100      # skill's min_volume param
TOP_N = 10            # skill's top_n param
N_EXPIRIES = 4        # skill's expiries param
MAX_DTE = 60          # skill step 6 filter

stats = {"calls": 0, "http_429": 0, "other_errors": 0, "raw_rows": 0, "errors": []}


def curl(url, out, hdrs, jar=None, use_jar=False):
    cmd = ["curl", "-sS", "--compressed", "-H", f"User-Agent: {UA}"]
    for h in hdrs:
        cmd += ["-H", h]
    if jar:
        cmd += ["-c", jar] + (["-b", jar] if use_jar else [])
    cmd += ["-w", "%{http_code}", "-o", out, url]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    code = (p.stdout or "").strip()[-3:]
    return code


def get_crumb(jar):
    """Page fetch MUST use -c only (no -b)."""
    page = os.path.join(DATA, "_page.html")
    code = curl(f"https://finance.yahoo.com/quote/NVDA/options/?date=0", page,
                ["Accept: text/html,application/xhtml+xml"], jar=jar, use_jar=False)
    if code != "200":
        raise RuntimeError(f"quote page HTTP {code}")
    html = open(page, encoding="utf-8", errors="replace").read()
    m = re.search(r'"crumb":"([^"]+)"', html)
    if not m:
        raise RuntimeError("no crumb in page bootstrap")
    return m.group(1)


def fetch_chain(sym, date_epoch, crumb, jar):
    """Returns (result_obj, http_code). date_epoch None -> nearest expiry."""
    url = f"https://query2.finance.yahoo.com/v7/finance/options/{urllib.parse.quote(sym)}"
    qs = []
    if date_epoch:
        qs.append(f"date={date_epoch}")
    qs.append(f"crumb={urllib.parse.quote(crumb, safe='')}")
    url += "?" + "&".join(qs)
    out = os.path.join(DATA, f"chain_{sym}_{date_epoch or 'nearest'}.json")
    code = curl(url, out, ["Referer: https://finance.yahoo.com/quote/%s/options/" % sym],
                jar=jar, use_jar=True)
    stats["calls"] += 1
    if code == "429":
        stats["http_429"] += 1
        return None, code
    if code != "200":
        stats["other_errors"] += 1
        stats["errors"].append(f"{sym} date={date_epoch} HTTP {code}")
        return None, code
    try:
        d = json.load(open(out, encoding="utf-8"))
    except Exception as e:
        stats["other_errors"] += 1
        stats["errors"].append(f"{sym} date={date_epoch} parse {e}")
        return None, code
    r = (d.get("optionChain", {}).get("result") or [])
    if not r:
        stats["other_errors"] += 1
        stats["errors"].append(f"{sym} date={date_epoch} empty result")
        return None, code
    return r[0], code


def main():
    jar = os.path.join(DATA, "jar.txt")
    if os.path.exists(jar):
        os.remove(jar)
    crumb = get_crumb(jar)
    print("crumb ok", flush=True)

    rows = []
    meta = {}
    for sym in TICKERS:
        base, code = fetch_chain(sym, None, crumb, jar)
        if base is None:
            continue
        q = base.get("quote", {})
        price = q.get("regularMarketPrice")
        regtime = q.get("regularMarketTime")
        exp_all = base.get("expirationDates", [])
        expiries = exp_all[:N_EXPIRIES]
        meta[sym] = {
            "price": price,
            "regularMarketTime": regtime,
            "regularMarketTimeET": datetime.datetime.fromtimestamp(regtime, ET).strftime("%Y-%m-%d %H:%M:%S %a") if regtime else None,
            "previousClose": q.get("previousClose"),
            "dayHigh": q.get("regularMarketDayHigh"),
            "dayLow": q.get("regularMarketDayLow"),
            "volume": q.get("regularMarketVolume"),
            "currency": q.get("currency"),
            "nExpiriesAvailable": len(exp_all),
            "expiriesUsed": expiries,
        }
        # nearest expiry chain is in base["options"][0]; fetch the rest
        chains = []
        if base.get("options"):
            chains.append(base["options"][0])
        for e in expiries[1:]:
            res, c2 = fetch_chain(sym, e, crumb, jar)
            if res is None:
                continue
            for o in res.get("options", []):
                chains.append(o)
            time.sleep(0.35)
        for o in chains:
            exp_epoch = o.get("expirationDate")
            if exp_epoch is None:
                continue
            exp_date = datetime.datetime.fromtimestamp(exp_epoch, ET).strftime("%Y-%m-%d")
            dte = (datetime.datetime.fromtimestamp(exp_epoch, ET).date()
                   - datetime.datetime.fromtimestamp(regtime, ET).date()).days
            for side_key, side in (("calls", "call"), ("puts", "put")):
                for c in o.get(side_key, []):
                    vol = c.get("volume") or 0
                    oi = c.get("openInterest")
                    if vol < MIN_VOLUME:
                        continue
                    stats["raw_rows"] += 1
                    if not oi:
                        continue
                    rows.append({
                        "ticker": sym, "side": side, "strike": c.get("strike"),
                        "expiry": exp_date, "expiry_epoch": exp_epoch, "dte": dte,
                        "volume": vol, "open_interest": oi,
                        "v_oi": round(vol / oi, 4) if oi else None,
                        "last_price": c.get("lastPrice"),
                        "iv": c.get("impliedVolatility"),
                        "in_the_money": c.get("inTheMoney"),
                        "underlying_price": price,
                        "moneyness_pct": round((c.get("strike") - price) / price * 100, 2) if price else None,
                    })
        print(f"{sym}: {len(rows)} rows cumulative", flush=True)
        time.sleep(0.35)

    json.dump({"date": SYM_DATE, "meta": meta, "rows": rows, "stats": stats},
              open(os.path.join(DATA, "rows.json"), "w"), indent=1)
    print("raw rows", stats["raw_rows"], "kept", len(rows))
    print("calls", stats["calls"], "429", stats["http_429"], "err", stats["other_errors"])


if __name__ == "__main__":
    main()
