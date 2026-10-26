#!/usr/bin/env python3
"""Assemble the EOD CSVs from the TradingView pull.

Re-implements the local helper's CSV writing (pull_international.py fmt() +
HEADER) and the skill's schema:
  date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange

US  -> /workspace/us-eod/<DATE>.csv
Intl-> /workspace/us-eod/<region>/<DATE>.csv   (16 regions)
"""
from __future__ import annotations

import csv
import json
import os
import sys
from collections import Counter

DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-20"
OUT_ROOT = "/workspace/us-eod"
DATA = "/workspace/data"

HEADER = ["date", "ticker", "name", "open", "high", "low", "close",
          "volume", "change_pct", "market_cap", "pe_ratio", "sector",
          "currency", "exchange"]

INTL_REGIONS = ["au", "jp", "tw", "ca", "eu-de", "eu-fr", "eu-it", "eu-es",
                "eu-nl", "eu-be", "eu-at", "eu-pt", "eu-ie", "eu-fi", "eu-dk",
                "eu-gr"]


def fmt(v):
    """pull_international.py fmt() — verbatim."""
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


def main() -> int:
    os.makedirs(OUT_ROOT, exist_ok=True)
    stats = {}
    for region in ["us"] + INTL_REGIONS:
        path = f"{DATA}/{region}.json"
        if not os.path.exists(path):
            print(f"MISS {region}: no data file")
            continue
        blob = json.load(open(path, encoding="utf-8"))
        rows = blob["rows"]
        if region == "us":
            out_path = f"{OUT_ROOT}/{DATE}.csv"
        else:
            os.makedirs(f"{OUT_ROOT}/{region}", exist_ok=True)
            out_path = f"{OUT_ROOT}/{region}/{DATE}.csv"
        if os.path.exists(out_path):
            print(f"SKIP {out_path} (exists — never overwrite)")
            continue

        blank = Counter()
        with open(out_path, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(HEADER)
            for r in rows:
                v = r["values"]
                name = v[1] or ""
                row = [DATE, r["ticker"], name,
                       fmt(v[2]), fmt(v[3]), fmt(v[4]), fmt(v[5]),
                       fmt(v[6]), fmt(v[7]), fmt(v[8]), fmt(v[9]), (v[10] or ""),
                       v[12] or "", v[11] or ""]   # v[12]=currency, v[11]=exchange
                for i, cell in enumerate(row):
                    if cell == "":
                        blank[HEADER[i]] += 1
                w.writerow(row)
        stats[region] = {"rows": len(rows), "path": out_path,
                         "blank": dict(blank),
                         "size_kb": round(os.path.getsize(out_path) / 1024, 1)}
        print(f"WROTE {out_path} rows={len(rows)} "
              f"blanks={ {k: v for k, v in blank.items()} }")
    total = sum(s["rows"] for s in stats.values())
    print(f"TOTAL rows={total} files={len(stats)}")
    json.dump(stats, open(f"{DATA}/_csv_stats.json", "w"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
