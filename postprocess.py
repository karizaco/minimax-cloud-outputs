#!/usr/bin/env python3
"""Post-processing for the EOD snapshot:

1. lag attribution — compare the TradingView close against Yahoo 5-minute
   intraday bars to measure how far behind the screener feed is.
2. blank fill   — patch change_pct cells the screener left empty with the
   Yahoo value (the skill's enrichment fallback).
3. movers       — top gainers / losers per region for the run report.
"""
from __future__ import annotations

import csv
import json
import os
import statistics
import sys
import time
import urllib.request
from datetime import datetime, timezone

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
DATA = "/workspace/data"
OUT_ROOT = "/workspace/us-eod"
DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-20"
INTL = ["au", "jp", "tw", "ca", "eu-de", "eu-fr", "eu-it", "eu-es", "eu-nl",
        "eu-be", "eu-at", "eu-pt", "eu-ie", "eu-fi", "eu-dk", "eu-gr"]


def chart(symbol, interval="5m", rng="1d"):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
           f"?range={rng}&interval={interval}")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as r:
        d = json.loads(r.read().decode())["chart"]["result"][0]
    ts = d.get("timestamp", [])
    close = (d.get("indicators", {}).get("quote", [{}])[0] or {}).get("close", [])
    return list(zip(ts, close))


def lag_check(n=8):
    """How many minutes behind is the TV close vs the Yahoo live price?"""
    blob = json.load(open(f"{DATA}/us.json", encoding="utf-8"))
    rows = sorted(blob["rows"], key=lambda r: -(r["values"][8] or 0)
                  if isinstance(r["values"][8], (int, float)) else 0)[:n]
    offsets = []
    for r in rows:
        tv_close = r["values"][5]
        sym = r["ticker"].split(":", 1)[1].replace(".", "-")
        try:
            bars = [(t, c) for t, c in chart(sym) if c]
        except Exception as e:  # noqa: BLE001
            print(f"  lag check {sym}: {str(e)[:60]}")
            continue
        if not bars or not isinstance(tv_close, (int, float)):
            continue
        best = min(bars, key=lambda b: abs(b[1] - tv_close))
        now = bars[-1][0]
        off = (now - best[0]) / 60.0
        offsets.append(off)
        print(f"  {sym}: tv_close={tv_close} matched bar "
              f"{datetime.fromtimestamp(best[0], timezone.utc):%H:%M}Z "
              f"close={best[1]} lag={off:.0f}min")
        time.sleep(0.2)
    return offsets


def fill_blanks():
    """Patch blank change_pct cells using the Yahoo verification values."""
    yh = json.load(open(f"{DATA}/_yahoo_values.json", encoding="utf-8"))
    patched = []
    for region in ["us"] + INTL:
        path = (f"{OUT_ROOT}/{DATE}.csv" if region == "us"
                else f"{OUT_ROOT}/{region}/{DATE}.csv")
        if not os.path.exists(path):
            continue
        with open(path, newline="", encoding="utf-8") as fh:
            rows = list(csv.reader(fh))
        head, body = rows[0], rows[1:]
        ci = head.index("change_pct")
        ti = head.index("ticker")
        n = 0
        for row in body:
            if row[ci].strip() == "":
                rec = yh.get(row[ti])
                if rec and isinstance(rec.get("change_pct"), (int, float)):
                    row[ci] = f"{rec['change_pct']:.4f}".rstrip("0").rstrip(".")
                    n += 1
        if n:
            with open(path, "w", newline="", encoding="utf-8") as fh:
                w = csv.writer(fh)
                w.writerow(head)
                w.writerows(body)
        patched.append((region, n))
    return patched


def movers():
    out = {}
    for region in ["us"] + INTL:
        path = (f"{OUT_ROOT}/{DATE}.csv" if region == "us"
                else f"{OUT_ROOT}/{region}/{DATE}.csv")
        if not os.path.exists(path):
            continue
        with open(path, newline="", encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        vals = []
        for r in rows:
            try:
                c = float(r["change_pct"])
            except (TypeError, ValueError):
                continue
            vals.append((c, r["ticker"], r["name"], r["close"], r["market_cap"]))
        vals.sort(key=lambda v: -v[0])
        out[region] = {
            "n": len(vals),
            "top": vals[:5],
            "bottom": vals[-5:][::-1],
            "movers_up": sum(1 for v in vals if v[0] >= 3),
            "movers_dn": sum(1 for v in vals if v[0] <= -3),
        }
    return out


if __name__ == "__main__":
    print("== lag attribution (US, top names) ==")
    offs = lag_check()
    if offs:
        print(f"  median lag = {statistics.median(offs):.0f} min")
    print("== blank fill (change_pct from Yahoo) ==")
    for region, n in fill_blanks():
        if n:
            print(f"  {region}: patched {n}")
    print("== movers ==")
    mv = movers()
    json.dump(mv, open(f"{DATA}/_movers.json", "w"), indent=1)
    for region in ["us"] + INTL:
        if region in mv:
            m = mv[region]
            t = ", ".join(f"{v[1]} {v[0]:+.2f}%" for v in m["top"][:3])
            b = ", ".join(f"{v[1]} {v[0]:+.2f}%" for v in m["bottom"][:3])
            print(f"  {region:6s} n={m['n']:5d} up>=3%: {m['movers_up']:4d} "
                  f"dn<=-3%: {m['movers_dn']:4d} | top {t} | bot {b}")
