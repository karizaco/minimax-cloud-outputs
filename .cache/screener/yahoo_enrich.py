#!/usr/bin/env python3
"""Yahoo enrichment of the screened candidate set (Cloud cron #9).

For every unique candidate ticker this pulls 1y of daily bars and computes the
fields the TradingView scanner does not expose:
  * true ADR20 = mean((high-low)/close, 20)  -- replaces the ATR/close proxy
  * ATR14 series + median(ATR14, 63d)        -- enables the atr_shrink skip flag
  * 5d / 20d trading ranges                   -- enables the ma_shrink_5d skip flag
  * 14-day velocity                          -- peoplewish's primary sort
  * last bar date                            -- freshness stamp / stale-row filter
  * SMA20/50/200 recomputed from the same bars
Results are cached to data/yahoo_bars.json so re-runs are free.
"""
import json
import math
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0"
CACHE = "/workspace/data/yahoo_bars.json"
OUT = "/workspace/data/yahoo_enriched.csv"

COLS = ["name", "close", "change", "volume", "market_cap_basic", "_adr_proxy_pct",
        "_adv_dollar", "_gap_pct", "_dist_sma200_pct", "_rs_1m", "_rs_3m", "_rs_6m",
        "_rs_12m", "relative_volume_10d_calc", "SMA20", "SMA50", "SMA200", "ATR",
        "Perf.5D", "Perf.1M", "_ts"]


def fetch(sym, tries=3):
    for i in range(tries):
        p = subprocess.run(
            ["curl", "-s", "--max-time", "45", "-H", f"User-Agent: {UA}",
             f"https://query2.finance.yahoo.com/v8/finance/chart/{sym}?range=1y&interval=1d"],
            capture_output=True, text=True)
        if p.returncode == 0 and p.stdout.strip():
            try:
                j = json.loads(p.stdout)
            except json.JSONDecodeError:
                time.sleep(0.8 + i)
                continue
            res = (j.get("chart") or {}).get("result")
            if res:
                r = res[0]
                ts = r.get("timestamp") or []
                q = (r.get("indicators", {}).get("quote") or [{}])[0]
                o = q.get("open") or []
                h = q.get("high") or []
                l = q.get("low") or []
                c = q.get("close") or []
                v = q.get("volume") or []
                bars = [(ts[i], o[i] if i < len(o) else None, h[i] if i < len(h) else None,
                         l[i] if i < len(l) else None, c[i] if i < len(c) else None,
                         v[i] if i < len(v) else None) for i in range(len(ts))
                        if i < len(c) and c[i] is not None]
                if bars:
                    return {"symbol": sym, "bars": bars, "n": len(bars)}
                return {"symbol": sym, "bars": [], "n": 0, "error": "no_close_bars"}
            err = (j.get("chart") or {}).get("error")
            return {"symbol": sym, "bars": [], "n": 0, "error": str(err)[:120]}
        time.sleep(0.8 + i)
    return {"symbol": sym, "bars": [], "n": 0, "error": "fetch_failed"}


def atr14(bars):
    trs = []
    for i in range(1, len(bars)):
        h, l, pc = bars[i][2], bars[i][3], bars[i - 1][4]
        if h is None or l is None or pc is None:
            continue
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    if len(trs) < 14:
        return None, None
    a = sum(trs[-14:]) / 14
    series = [sum(trs[max(0, i - 13):i + 1]) / min(14, i + 1) for i in range(len(trs))]
    med = None
    if len(series) >= 63:
        s = sorted(series[-63:])
        med = s[len(s) // 2]
    return a, med


def compute(d):
    bars = d.get("bars", [])
    out = {"symbol": d["symbol"], "y_bars": len(bars), "y_error": d.get("error")}
    if not bars:
        return out
    import datetime
    last = bars[-1]
    out["y_last_bar_utc"] = datetime.datetime.utcfromtimestamp(last[0]).strftime("%Y-%m-%d")
    out["y_last_bar_et"] = datetime.datetime.utcfromtimestamp(last[0] - 4 * 3600).strftime("%Y-%m-%d")
    out["y_close"] = last[4]
    closes = [b[4] for b in bars]
    highs = [b[2] for b in bars if b[2] is not None]
    lows = [b[3] for b in bars if b[3] is not None]
    # true ADR20
    adr = None
    win = bars[-20:]
    if len(win) >= 20:
        vals = [(b[2] - b[3]) / b[4] for b in win if b[2] is not None and b[3] is not None and b[4]]
        if vals:
            adr = sum(vals) / len(vals) * 100
    out["y_adr20_pct"] = adr
    a14, med = atr14(bars)
    out["y_atr14"] = a14
    out["y_atr14_median63"] = med
    out["y_atr_pct"] = (a14 / last[4] * 100) if a14 else None
    out["y_atr_shrink"] = bool(a14 and med and a14 < 0.6 * med)
    out["y_atr_extension_x"] = (a14 / med) if (a14 and med) else None
    if len(bars) >= 20:
        h5 = max(b[2] for b in bars[-5:] if b[2] is not None)
        l5 = min(b[3] for b in bars[-5:] if b[3] is not None)
        h20 = max(b[2] for b in bars[-20:] if b[2] is not None)
        l20 = min(b[3] for b in bars[-20:] if b[3] is not None)
        out["y_range5_pct"] = (h5 - l5) / last[4] * 100
        out["y_range20_pct"] = (h20 - l20) / last[4] * 100
        out["y_ma_shrink_5d"] = bool((h5 - l5) / last[4] < 0.5 * ((h20 - l20) / last[4]))
    if len(closes) >= 15:
        out["y_velocity_14d_pct"] = (closes[-1] / closes[-15] - 1) * 100
    if len(closes) >= 6:
        out["y_gain_5d_pct"] = (closes[-1] / closes[-6] - 1) * 100
    for n in (20, 50, 200):
        out[f"y_sma{n}"] = (sum(closes[-n:]) / n) if len(closes) >= n else None
    if out.get("y_sma200"):
        out["y_dist_sma200_pct"] = (last[4] / out["y_sma200"] - 1) * 100
    if len(closes) >= 2:
        out["y_prev_close"] = closes[-2]
        out["y_change_pct"] = (last[4] / closes[-2] - 1) * 100
    return out


def main():
    import csv
    rows = list(csv.DictReader(open("/workspace/data/enriched.csv")))
    names = sorted({r["name"] for r in rows if r["name"]})
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    todo = [n for n in names if n not in cache or not cache[n].get("bars")]
    print(f"candidates={len(rows)} unique={len(names)} to_fetch={len(todo)} cached={len(names)-len(todo)}",
          file=sys.stderr)
    if todo:
        with ThreadPoolExecutor(max_workers=6) as ex:
            res = list(ex.map(fetch, todo))
        for d in res:
            cache[d["symbol"]] = d
        json.dump(cache, open(CACHE, "w"))
    fails = [n for n in names if not cache.get(n, {}).get("bars")]
    print(f"fetch_failures={len(fails)} {fails[:12]}", file=sys.stderr)

    comp = {}
    for n in names:
        comp[n] = compute(cache.get(n, {"symbol": n, "bars": []}))

    with open(OUT, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(COLS + ["_screen", "y_bars", "y_last_bar_et", "y_close", "y_change_pct",
                           "y_adr20_pct", "y_atr_pct", "y_atr14", "y_atr14_median63",
                           "y_atr_shrink", "y_atr_extension_x", "y_velocity_14d_pct",
                           "y_gain_5d_pct", "y_range5_pct", "y_range20_pct",
                           "y_ma_shrink_5d", "y_sma20", "y_sma50", "y_sma200",
                           "y_dist_sma200_pct", "y_prev_close", "y_error"])
        for r in rows:
            c = comp.get(r["name"], {})
            w.writerow([r.get(c2, "") for c2 in COLS] + [r.get("_screen", "")] +
                       [c.get(k, "") for k in ("y_bars", "y_last_bar_et", "y_close", "y_change_pct",
                                              "y_adr20_pct", "y_atr_pct", "y_atr14",
                                              "y_atr14_median63", "y_atr_shrink",
                                              "y_atr_extension_x", "y_velocity_14d_pct",
                                              "y_gain_5d_pct", "y_range5_pct", "y_range20_pct",
                                              "y_ma_shrink_5d", "y_sma20", "y_sma50", "y_sma200",
                                              "y_dist_sma200_pct", "y_prev_close", "y_error")])
    json.dump(comp, open("/workspace/data/yahoo_comp.json", "w"), indent=1)
    print(f"wrote {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
