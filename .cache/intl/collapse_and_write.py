#!/usr/bin/env python3
"""collapse_and_write.py — cron #5 international EOD CSV writer.

Re-implements the skill's universe post-processing on Cloud:
  1. symbol dedupe (exact TV symbol)
  2. primary-listing dedupe (same symbol on several venues -> canonical venue)
  3. venue-duplicate collapse (same normalised company name on different
     venues -> one canonical row per company per region)

Then writes the 14-column skill schema per region:
  date,ticker,name,open,high,low,close,volume,change_pct,market_cap,
  pe_ratio,sector,currency,exchange

Output: /workspace/international-eod/<DATE>/<region>.csv
Never overwrites an existing file (skill hard rule).
"""
from __future__ import annotations

import csv
import json
import os
import re
from datetime import date

DATE = os.environ.get("EOD_DATE", date.today().isoformat())
DATA = "/workspace/data"
OUT_ROOT = "/workspace/international-eod"

HEADER = ["date", "ticker", "name", "open", "high", "low", "close",
          "volume", "change_pct", "market_cap", "pe_ratio", "sector",
          "currency", "exchange"]

# universe_cache.PRIMARY_LISTING — canonical venue per region
PRIMARY_LISTING = {
    "jp": ["TSE", "NAG", "FSE", "SAPSE"],
    "tw": ["TWSE", "TPEX"],
    "ca": ["TSX", "NEO", "TSXV", "CSE"],
    "eu-de": ["XETR", "FWB", "TRADEGATE", "GETTEX", "MUN", "DUS", "HAM",
              "HAN", "SWB", "LSX", "LS", "BER", "STU"],
    "eu-it": ["MIL", "EUROTLX"],
    "eu-nl": ["EURONEXT"],
    "eu-fr": ["EURONEXT"],
    "eu-es": ["BME"],
    "eu-be": ["EURONEXT"],
    "eu-at": ["VIE"],
    "eu-pt": ["EURONEXT"],
    "eu-ie": ["EURONEXT"],
    "eu-fi": ["OMXHEX"],
    "eu-dk": ["OMXCOP"],
    "eu-gr": ["ATHEX", "ATH"],
    "au": ["ASX"],
}


def fmt(v):
    """pull_international.py fmt() — verbatim from the skill helper."""
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


def norm_name(n: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (n or "").lower())


def collapse(rows: list[dict], region: str) -> tuple[list[dict], int, int]:
    """Returns (collapsed_rows, symbol_dupes_removed, venue_dupes_removed)."""
    prio = {e: i for i, e in enumerate(PRIMARY_LISTING.get(region, []))}

    # 1) exact symbol dedupe
    seen: set[str] = set()
    stage1 = []
    for r in rows:
        if r["symbol"] in seen:
            continue
        seen.add(r["symbol"])
        stage1.append(r)

    # 2) same bare symbol on several venues -> canonical venue
    groups: dict[str, list[dict]] = {}
    for r in stage1:
        sym = r["symbol"].split(":", 1)[1] if ":" in r["symbol"] else r["symbol"]
        groups.setdefault(sym, []).append(r)
    stage2, removed_sym = [], 0
    for sym, grp in groups.items():
        if len(grp) == 1:
            stage2.append(grp[0])
            continue
        grp.sort(key=lambda r: (prio.get(r["symbol"].split(":", 1)[0], 999),
                                 r["symbol"]))
        canon = dict(grp[0])
        canon["also_listed_on"] = [g["symbol"] for g in grp[1:]]
        removed_sym += len(grp) - 1
        stage2.append(canon)

    # 3) venue-duplicate collapse on normalised company name (intl only)
    if region in PRIMARY_LISTING:
        by_company: dict[str, list[dict]] = {}
        for r in stage2:
            key = norm_name(r.get("description") or "") or r["symbol"]
            by_company.setdefault(key, []).append(r)
        stage3, removed_venue = [], 0
        for grp in by_company.values():
            if len(grp) == 1:
                stage3.append(grp[0])
                continue
            grp.sort(key=lambda r: (prio.get(r["symbol"].split(":", 1)[0], 999),
                                    r["symbol"]))
            canon = dict(grp[0])
            canon["also_listed_on"] = [x["symbol"] for x in grp[1:]]
            removed_venue += len(grp) - 1
            stage3.append(canon)
        stage2 = stage3
    else:
        removed_venue = 0

    def mcap(r):
        v = r.get("market_cap_basic")
        return -(v if isinstance(v, (int, float)) else 0)

    stage2.sort(key=lambda r: (mcap(r), r["symbol"]))
    return stage2, removed_sym, removed_venue


def main() -> int:
    outdir = os.path.join(OUT_ROOT, DATE)
    os.makedirs(outdir, exist_ok=True)
    stats, collapse_map = {}, {}
    total = 0
    for fn in sorted(os.listdir(DATA)):
        if not fn.endswith(".json") or fn.startswith("_"):
            continue
        region = fn[:-5]
        blob = json.load(open(os.path.join(DATA, fn), encoding="utf-8"))
        rows = blob["rows"]
        if not rows:
            print(f"MISS {region}: empty pull")
            continue
        # guard: only rows whose country matches the requested issuer country
        country = blob.get("country")
        rows = [r for r in rows if r.get("country") == country]
        collapsed, rm_sym, rm_venue = collapse(rows, region)
        out_path = os.path.join(outdir, f"{region}.csv")
        if os.path.exists(out_path):
            print(f"SKIP {out_path} (exists — never overwrite)")
            continue
        blanks = {h: 0 for h in HEADER}
        with open(out_path, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(HEADER)
            for r in collapsed:
                row = [DATE, r["symbol"], r.get("description") or "",
                       fmt(r.get("open")), fmt(r.get("high")), fmt(r.get("low")),
                       fmt(r.get("close")), fmt(r.get("volume")), fmt(r.get("change")),
                       fmt(r.get("market_cap_basic")), fmt(r.get("price_earnings_ttm")),
                       r.get("sector") or "", r.get("currency") or "",
                       r.get("exchange") or ""]
                for i, cell in enumerate(row):
                    if cell == "":
                        blanks[HEADER[i]] += 1
                w.writerow(row)
        stats[region] = {
            "rows": len(collapsed), "raw_rows": blob.get("rows_raw"),
            "screener_total": blob.get("reported_totalCount"),
            "removed_symbol_dupes": rm_sym, "removed_venue_dupes": rm_venue,
            "file": out_path, "size_kb": round(os.path.getsize(out_path) / 1024, 1),
            "blanks": {k: v for k, v in blanks.items() if v},
        }
        collapse_map[region] = {
            r["symbol"]: r.get("also_listed_on", [])
            for r in collapsed if r.get("also_listed_on")
        }
        total += len(collapsed)
        print(f"WROTE {out_path} rows={len(collapsed)} raw={blob.get('rows_raw')} "
              f"rm_sym={rm_sym} rm_venue={rm_venue} blanks="
              f"{ {k: v for k, v in blanks.items() if v} }")
    json.dump({"date": DATE, "regions": stats, "total_rows": total,
               "collapse_map": collapse_map},
              open(f"{DATA}/_intl_stats.json", "w"), indent=1)
    print(f"TOTAL rows={total} files={len(stats)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
