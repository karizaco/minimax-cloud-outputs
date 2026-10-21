#!/usr/bin/env python3
"""Assemble the 2026-10-21 EOD CSVs from the Yahoo refresh + prior-day file.

Field provenance (2026-10-21 run, TradingView screener unavailable):
  date, ticker, name, currency, exchange -> cached universe (TV screener pull
                                             of 2026-10-20, 7-day cache TTL)
  open, high, low, close, volume, change_pct -> fresh Yahoo /v8/finance/chart
  market_cap, pe_ratio, sector            -> carried forward from 2026-10-20
                                             (skill enrichment-cache TTL:
                                              pe/sector 30d, mcap n/a)

Rows whose Yahoo symbol does not resolve, or whose last daily bar predates the
2026-10-21 session, are written with empty numeric fields (skill rule: never
write "N/A", never invent values).
"""
from __future__ import annotations

import csv
import json
import os
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

DATA = "/workspace/data"
DATA2 = "/workspace/data2"
OUT_ROOT = "/workspace/us-eod"
DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-21"
PRIOR = "2026-10-20"
INTL = ["au", "jp", "tw", "ca", "eu-de", "eu-fr", "eu-it", "eu-es", "eu-nl",
        "eu-be", "eu-at", "eu-pt", "eu-ie", "eu-fi", "eu-dk", "eu-gr"]
TZMAP = {"us": "America/New_York", "au": "Australia/Sydney", "jp": "Asia/Tokyo",
         "tw": "Asia/Taipei", "ca": "America/Toronto",
         "eu-de": "Europe/Berlin", "eu-fr": "Europe/Paris", "eu-it": "Europe/Rome",
         "eu-es": "Europe/Madrid", "eu-nl": "Europe/Amsterdam",
         "eu-be": "Europe/Brussels", "eu-at": "Europe/Vienna",
         "eu-pt": "Europe/Lisbon", "eu-ie": "Europe/Dublin",
         "eu-fi": "Europe/Helsinki", "eu-dk": "Europe/Copenhagen",
         "eu-gr": "Europe/Athens"}
HEADER = ["date", "ticker", "name", "open", "high", "low", "close", "volume",
          "change_pct", "market_cap", "pe_ratio", "sector", "currency", "exchange"]


def fmt(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return str(v).lower()
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        if v == int(v):
            return str(int(v))
        return f"{v:.4f}".rstrip("0").rstrip(".")
    return str(v)


def sanitize_ohlc(o, h, l, c, eps=1e-9):
    """Drop fields that contradict the rest of the bar. Never invents values.

    Yahoo's daily bar for an in-progress session carries a stale `open`
    (often the previous close) and, for thin names, a stale day high/low.
    The bar `close` is the live price (it matches meta regularMarketPrice),
    so the contradictory side is dropped, not the close.
    """
    if c is not None and h is not None and c > h + eps:
        h = None                     # high is behind the live price
    if c is not None and l is not None and c < l - eps:
        l = None                     # low is ahead of the live price
    if o is not None and h is not None and o > h + eps:
        o = None
    if o is not None and l is not None and o < l - eps:
        o = None
    return o, h, l, c


def prior_rows(region):
    p = (f"{OUT_ROOT}/{PRIOR}.csv" if region == "us"
         else f"{OUT_ROOT}/{region}/{PRIOR}.csv")
    if not os.path.exists(p):
        return {}
    with open(p, newline="", encoding="utf-8") as fh:
        return {r["ticker"]: r for r in csv.DictReader(fh)}


def main():
    prices = json.load(open(f"{DATA2}/yahoo_prices_{DATE}.json", encoding="utf-8"))
    stats = {}
    stale_log = []
    for region in ["us"] + INTL:
        uni = json.load(open(f"{DATA}/{region}.json", encoding="utf-8"))["rows"]
        if region != "us":
            # apply the same venue-duplicate collapse used by the fetcher
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "fy", "/workspace/fetch_yahoo_prices.py")
            fy = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(fy)
            uni = fy.build_universe()[region]
        prior = prior_rows(region)
        tz = ZoneInfo(TZMAP[region])
        out_path = (f"{OUT_ROOT}/{DATE}.csv" if region == "us"
                    else f"{OUT_ROOT}/{region}/{DATE}.csv")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        if os.path.exists(out_path):
            print(f"SKIP {out_path} (exists — never overwrite)")
            continue
        n_ok = n_nodata = n_stale = n_blank = 0
        with open(out_path, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(HEADER)
            for r in uni:
                tv = r["ticker"]
                pr = prices.get(tv) or {}
                st = pr.get("status", "missing")
                p_row = prior.get(tv, {})
                v = r["values"]
                name = v[1] or p_row.get("name", "") or pr.get("name", "")
                o = h = l = c = vol = chg = None
                if st == "ok":
                    bar = pr.get("bar_ts")
                    same_session = True
                    if bar:
                        same_session = (datetime.fromtimestamp(bar, timezone.utc)
                                        .astimezone(tz).date().isoformat() == DATE)
                    if same_session:
                        o, h, l, c = sanitize_ohlc(pr.get("open"),
                                                   pr.get("high"),
                                                   pr.get("low"),
                                                   pr.get("close"))
                        vol, chg = pr.get("volume"), pr.get("change_pct")
                        n_ok += 1
                    else:
                        n_stale += 1
                        stale_log.append((tv, pr.get("symbol"),
                                          datetime.fromtimestamp(bar, timezone.utc)
                                          .astimezone(tz).isoformat()))
                elif st == "no_data":
                    n_nodata += 1
                else:
                    n_nodata += 1
                row = [DATE, tv, name, fmt(o), fmt(h), fmt(l), fmt(c), fmt(vol),
                       fmt(chg),
                       p_row.get("market_cap", "") or "",
                       p_row.get("pe_ratio", "") or "",
                       p_row.get("sector", "") or (v[10] or ""),
                       pr.get("currency") or v[12] or "",
                       v[11] or ""]
                if not row[3]:
                    n_blank += 1
                w.writerow(row)
        stats[region] = {"rows": len(uni), "fresh": n_ok, "stale_bar": n_stale,
                         "no_data": n_nodata, "no_price_cells": n_blank,
                         "file": out_path,
                         "kb": round(os.path.getsize(out_path) / 1024, 1)}
        print(f"WROTE {out_path} rows={len(uni)} fresh={n_ok} stale={n_stale} "
              f"nodata={n_nodata}", flush=True)
    json.dump(stats, open(f"{DATA2}/_assemble_stats.json", "w"), indent=1)
    json.dump(stale_log, open(f"{DATA2}/_stale_bars.json", "w"), indent=1)
    tot = sum(s["rows"] for s in stats.values())
    fresh = sum(s["fresh"] for s in stats.values())
    print(f"TOTAL rows={tot} fresh_priced={fresh} "
          f"({100*fresh/tot:.1f}%) stale_bar_rows={len(stale_log)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
