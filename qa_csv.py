#!/usr/bin/env python3
"""Final QA over the written EOD CSVs + headline stats for the run report."""
from __future__ import annotations

import csv
import json
import os
import re

OUT_ROOT = "/workspace/us-eod"
DATA = "/workspace/data"
DATE = os.environ.get("EOD_DATE", "2026-10-20")
INTL = ["au", "jp", "tw", "ca", "eu-de", "eu-fr", "eu-it", "eu-es", "eu-nl",
        "eu-be", "eu-at", "eu-pt", "eu-ie", "eu-fi", "eu-dk", "eu-gr"]
HEADER = ["date", "ticker", "name", "open", "high", "low", "close", "volume",
          "change_pct", "market_cap", "pe_ratio", "sector", "currency", "exchange"]
NUMERIC = {"open", "high", "low", "close", "volume", "change_pct", "market_cap",
           "pe_ratio"}
NA_TOKENS = {"n/a", "na", "none", "null", "-", "--"}


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def main():
    problems = []
    summary = {}
    for region in ["us"] + INTL:
        path = (f"{OUT_ROOT}/{DATE}.csv" if region == "us"
                else f"{OUT_ROOT}/{region}/{DATE}.csv")
        if not os.path.exists(path):
            problems.append(f"{region}: MISSING {path}")
            continue
        with open(path, newline="", encoding="utf-8") as fh:
            rd = csv.reader(fh)
            head = next(rd)
            rows = list(rd)
        if head != HEADER:
            problems.append(f"{region}: header mismatch {head}")
        bad_width = [i for i, r in enumerate(rows) if len(r) != len(HEADER)]
        if bad_width:
            problems.append(f"{region}: {len(bad_width)} rows with wrong width")
        na_cells = [(i, j) for i, r in enumerate(rows) for j, c in enumerate(r)
                    if c.strip().lower() in NA_TOKENS]
        if na_cells:
            problems.append(f"{region}: {len(na_cells)} N/A-style cells")
        d = {h: i for i, h in enumerate(head)}
        dupes = len(rows) - len({r[d["ticker"]] for r in rows})
        if dupes:
            problems.append(f"{region}: {dupes} duplicate tickers")
        # ohlc sanity
        bad_ohlc = 0
        for r in rows:
            o, h, l, c = (num(r[d[k]]) for k in ("open", "high", "low", "close"))
            if None in (o, h, l, c):
                continue
            if h < max(o, l, c) - 1e-9 or l > min(o, h, c) + 1e-9:
                bad_ohlc += 1
        if bad_ohlc:
            problems.append(f"{region}: {bad_ohlc} rows with inconsistent OHLC")
        # movers with a market-cap floor (meaningful names only)
        rows_mc = []
        for r in rows:
            ch, mc = num(r[d["change_pct"]]), num(r[d["market_cap"]])
            if ch is None:
                continue
            rows_mc.append((ch, r[d["ticker"]], r[d["name"]], mc or 0,
                            r[d["close"]], r[d["sector"]]))
        liquid = [x for x in rows_mc if x[3] >= 10e9]      # >= $10B cap
        liquid.sort(key=lambda x: -x[0])
        summary[region] = {
            "rows": len(rows), "dupes": dupes, "bad_ohlc": bad_ohlc,
            "with_change": len(rows_mc), "liquid_rows": len(liquid),
            "up_3": sum(1 for x in rows_mc if x[0] >= 3),
            "dn_3": sum(1 for x in rows_mc if x[0] <= -3),
            "up_3_liquid": sum(1 for x in liquid if x[0] >= 3),
            "dn_3_liquid": sum(1 for x in liquid if x[0] <= -3),
            "top_liquid_up": liquid[:5],
            "top_liquid_dn": liquid[-5:][::-1],
            "file_kb": round(os.path.getsize(path) / 1024, 1),
        }
    json.dump(summary, open(f"{DATA}/_qa_summary.json", "w"), indent=1)

    total = sum(v["rows"] for v in summary.values())
    print(f"files={len(summary)} total_rows={total}")
    print("PROBLEMS:" if problems else "PROBLEMS: none")
    for p in problems:
        print("  -", p)
    for region in ["us"] + INTL:
        s = summary.get(region)
        if not s:
            continue
        up = ", ".join(f"{x[1].split(':')[-1]} {x[0]:+.2f}%" for x in s["top_liquid_up"][:3])
        dn = ", ".join(f"{x[1].split(':')[-1]} {x[0]:+.2f}%" for x in s["top_liquid_dn"][:3])
        print(f"  {region:6s} rows={s['rows']:5d} liq={s['liquid_rows']:5d} "
              f"up>=3%={s['up_3']:4d} dn<=-3%={s['dn_3']:4d} | up(liq) {up} | dn(liq) {dn}")


if __name__ == "__main__":
    main()
