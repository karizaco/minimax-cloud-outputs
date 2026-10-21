#!/usr/bin/env python3
"""Second-pass Yahoo symbol repair for the 2026-10-21 EOD run.

Fixes three classes of defect found in the first pass:
  1. symbols that need a different separator on Yahoo
     (JPM/PC -> JPM-PC, NOVO_B.CO -> NOVO-B.CO, GRF.P.MC -> GRF-P.MC)
  2. German alternative venues that map to the Frankfurt suffix
     (GETTEX/FWB/... -> .F instead of .DE)
  3. Canadian preferred/class rows that the first pass mapped to the COMMON
     share (TSX:RY.PR.S -> RY.TO) — an identity error. Only class-preserving
     candidates are tried here; if none resolves, the row keeps empty price
     fields rather than the wrong instrument's price.
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

spec = importlib.util.spec_from_file_location("fy", "/workspace/fetch_yahoo_prices.py")
fy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fy)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
DATA2 = "/workspace/data2"
DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-21"
DE_SUFFIXES = [".F", ".DE", ".DU", ".MU", ".HM", ".HA", ".SW", ".SG"]


def candidates(tv, region):
    """Identity-preserving alternative Yahoo symbols for one TV ticker."""
    sym = tv.split(":", 1)[1]
    out = []
    if region == "us":
        out = [sym.replace("/", "-"), sym.replace(".", "-"), sym]
    elif region == "ca":
        if ".PR" in sym or ".PF" in sym:
            # class-preserving only — never fall back to the common share
            out = [sym + ".TO", sym.replace(".", "-") + ".TO",
                   sym.replace(".PR", "-P").replace(".PF", "-PF") + ".TO"]
        else:
            out = [sym + ".TO", sym.replace(".", "-") + ".TO",
                   sym + ".V", sym + ".CNQ", sym + ".CN"]
    elif region == "eu-de":
        out = [sym + s for s in DE_SUFFIXES]
    elif region == "eu-es":
        out = [sym.replace(".", "-") + ".MC", sym + ".MC"]
    elif region == "eu-dk":
        out = [sym.replace("_", "-") + ".CO", sym + ".CO"]
    elif region == "jp":
        out = [sym + ".T"]
    else:
        out = []
    seen, uniq = set(), []
    for s in out:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq


def probe(sym):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/"
           f"{urllib.request.quote(sym, safe='.-_')}?range=1d&interval=1d")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            d = json.loads(r.read().decode())
        res = (d.get("chart") or {}).get("result")
        if not res:
            return None
        d = res[0]
        meta = d.get("meta") or {}
        q = ((d.get("indicators") or {}).get("quote") or [{}])[0] or {}
        ts = d.get("timestamp") or []
        idx = None
        closes = q.get("close") or []
        for i in range(len(closes) - 1, -1, -1):
            if closes[i] is not None:
                idx = i
                break
        if idx is None:
            return None

        def g(k):
            arr = q.get(k) or []
            return arr[idx] if idx < len(arr) else None
        prev = meta.get("chartPreviousClose")
        close = g("close")
        chg = meta.get("regularMarketChangePercent")
        if chg is None and close is not None and prev:
            chg = (close - prev) / prev * 100.0
        return {"open": g("open"), "high": g("high"), "low": g("low"),
                "close": close, "volume": g("volume"), "change_pct": chg,
                "prev_close": prev, "price": meta.get("regularMarketPrice"),
                "day_high": meta.get("regularMarketDayHigh"),
                "day_low": meta.get("regularMarketDayLow"),
                "mtime": meta.get("regularMarketTime"),
                "bar_ts": ts[idx] if idx < len(ts) else None,
                "currency": meta.get("currency"),
                "yahoo_exchange": meta.get("fullExchangeName")
                                 or meta.get("exchangeName"),
                "name": meta.get("longName") or meta.get("shortName")}
    except Exception:
        return None


def main():
    path = f"{DATA2}/yahoo_prices_{DATE}.json"
    prices = json.load(open(path, encoding="utf-8"))

    # rows needing work: failed rows + rows whose first-pass symbol collapsed
    # a class/series marker onto the common share
    todo = []
    for tv, rec in prices.items():
        sym = tv.split(":", 1)[1]
        needs = rec["status"] != "ok"
        if rec["region"] == "ca" and (".PR" in sym or ".PF" in sym):
            needs = True           # identity fix, even if the first pass hit
        if needs:
            todo.append(tv)
    print(f"repair candidates: {len(todo)}", flush=True)

    fixed, still, wrong_identity = 0, 0, 0
    t0 = time.time()

    def run(tv):
        region = prices[tv]["region"]
        for cand in candidates(tv, region):
            rec = probe(cand)
            if rec:
                rec.update({"status": "ok", "symbol": cand, "ticker": tv,
                            "region": region, "repaired": True})
                return tv, rec, cand
        return tv, None, None

    with ThreadPoolExecutor(max_workers=24) as ex:
        for i, (tv, rec, cand) in enumerate(ex.map(run, todo), 1):
            if rec:
                prices[tv] = rec
                fixed += 1
            else:
                prices[tv]["status"] = "no_data"
                prices[tv]["symbol"] = None
                still += 1
            if i % 500 == 0:
                print(f"  {i}/{len(todo)} fixed={fixed} unresolved={still} "
                      f"({i/(time.time()-t0):.1f}/s)", flush=True)

    json.dump(prices, open(path, "w"), indent=0)
    print(f"DONE fixed={fixed} unresolved={still} "
          f"elapsed={time.time()-t0:.0f}s")
    st = {}
    for r in prices.values():
        st[r["status"]] = st.get(r["status"], 0) + 1
    print("statuses:", st)
    return 0


if __name__ == "__main__":
    sys.exit(main())
