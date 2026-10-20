#!/usr/bin/env python3
"""Cloud re-implementation of the EOD universe pull.

Local Mavis used the `mcp__tradingview_advanced__stock_screener` MCP tool
(per region: country=<x>, limit=2000, exclude_otc=true, stock_type=common).
That MCP binding is not exposed in this Cloud session, so this script talks to
the same upstream TradingView scanner endpoint directly over HTTPS and
re-implements the helper's post-processing (dedupe by primary listing).

Output: /workspace/data/<region>.json  (list of row dicts, full CSV fields)
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
DATA = "/workspace/data"
PAGE = 3000

COLUMNS = ["name", "description", "open", "high", "low", "close", "volume",
           "change", "market_cap_basic", "price_earnings_ttm", "sector",
           "exchange", "currency", "type", "country", "update_mode"]

# region key -> (tv endpoint slug, issuer-country filter, extra exchange filters)
REGIONS = {
    "us":     ("america", None, {"not_in_range": ["OTC"]}),
    "au":     ("australia", "Australia", None),
    "jp":     ("japan", "Japan", None),
    "tw":     ("taiwan", "Taiwan", None),
    "ca":     ("canada", "Canada", None),
    "eu-de":  ("germany", "Germany", None),
    "eu-fr":  ("france", "France", None),
    "eu-it":  ("italy", "Italy", None),
    "eu-es":  ("spain", "Spain", None),
    "eu-nl":  ("netherlands", "Netherlands", None),
    "eu-be":  ("belgium", "Belgium", None),
    "eu-at":  ("austria", "Austria", None),
    "eu-pt":  ("portugal", "Portugal", None),
    "eu-ie":  ("ireland", "Ireland", None),
    "eu-fi":  ("finland", "Finland", None),
    "eu-dk":  ("denmark", "Denmark", None),
    "eu-gr":  ("greece", "Greece", None),
}

# universe_cache.PRIMARY_LISTING — canonical venue per region
PRIMARY_LISTING = {
    "jp": ["TSE", "NAG", "FSE", "SAPSE"],
    "tw": ["TWSE", "TPEx"],
    "ca": ["TSX", "NEO", "TSXV", "CSE"],
    "eu-de": ["XETR", "FWB", "TRADEGATE", "GETTEX", "MUN", "DUS", "HAM",
              "HAN", "SWB", "LSX", "LS", "BER", "STU"],
    "eu-it": ["MIL", "EUROTLX"],
    "eu-nl": ["AMS", "AS", "EURONEXT"],
    "eu-fr": ["EPA", "EURONEXT"],
    "eu-es": ["BME"],
    "eu-be": ["BSE", "BRU"],
    "eu-at": ["VIE"],
    "eu-pt": ["LIS"],
    "eu-ie": ["ISE", "Dublin"],
    "eu-fi": ["HEL"],
    "eu-dk": ["CPH"],
    "eu-gr": ["ATHEX", "ATH"],
    "au": ["ASX"],
}

IDX = {c: i for i, c in enumerate(COLUMNS)}


def scan(slug: str, body: dict, tries: int = 3):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(
                f"https://scanner.tradingview.com/{slug}/scan",
                data=json.dumps(body).encode(),
                headers={"User-Agent": UA, "Content-Type": "application/json",
                         "Origin": "https://www.tradingview.com",
                         "Referer": "https://www.tradingview.com/"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise last


def filters_for(country, exch):
    f = [{"left": "type", "operation": "equal", "right": "stock"}]
    if country:
        f.append({"left": "country", "operation": "equal", "right": country})
    if exch:
        f.append({"left": "exchange", "operation": "not_in_range",
                  "right": exch["not_in_range"]})
    return f


def pull_region(region: str):
    slug, country, exch = REGIONS[region]
    base = {
        "filter": filters_for(country, exch),
        "options": {"lang": "en"},
        "columns": COLUMNS,
        "sort": {"sortBy": "market_cap_basic", "sortOrder": "desc"},
    }
    rows, seen = [], set()
    start = 0
    total = None
    while True:
        body = dict(base)
        body["range"] = [start, start + PAGE]
        res = scan(slug, body)
        total = res.get("totalCount", total)
        data = res.get("data", [])
        if not data:
            break
        for item in data:
            sym = item.get("s", "")
            if not sym or sym in seen:
                continue
            seen.add(sym)
            d = item.get("d", [])
            rows.append({"ticker": sym,
                         "values": [d[IDX[c]] if i < len(d) else None
                                    for i, c in enumerate(COLUMNS)]})
        start += len(data)
        if start >= (total or 0) or len(data) < PAGE:
            break

    # client-side guards: only common stocks, only the target issuer country
    keep, null_country, mismatch = [], 0, 0
    for r in rows:
        v = r["values"]
        if v[IDX["type"]] != "stock":
            continue
        if country:
            if v[IDX["country"]] is None:
                null_country += 1
            elif v[IDX["country"]] != country:
                mismatch += 1
                continue
        keep.append(r)

    # dedupe by primary listing (helper: universe_cache.dedupe_primary_listing)
    prio = {e: i for i, e in enumerate(PRIMARY_LISTING.get(region, []))}
    groups = {}
    for r in keep:
        sym = r["ticker"].split(":", 1)[1] if ":" in r["ticker"] else r["ticker"]
        groups.setdefault(sym, []).append(r)
    deduped, removed = [], 0
    for sym, grp in groups.items():
        if len(grp) == 1:
            deduped.append(grp[0])
            continue
        grp.sort(key=lambda r: (prio.get(r["ticker"].split(":", 1)[0], 999),
                                 r["ticker"]))
        canon = dict(grp[0])
        canon["also_listed_on"] = [g["ticker"] for g in grp[1:]]
        removed += len(grp) - 1
        deduped.append(canon)

    # sort by market cap desc, ticker asc (matches helper ordering)
    def mcap(r):
        v = r["values"][IDX["market_cap_basic"]]
        return -(v if isinstance(v, (int, float)) else 0)
    deduped.sort(key=lambda r: (mcap(r), r["ticker"]))

    os.makedirs(DATA, exist_ok=True)
    with open(f"{DATA}/{region}.json", "w", encoding="utf-8") as fh:
        json.dump({"region": region, "slug": slug, "country": country,
                   "screener_total": total, "raw_rows": len(rows),
                   "kept": len(keep), "deduped_removed": removed,
                   "null_country": null_country, "country_mismatch": mismatch,
                   "rows": deduped}, fh)
    return {"region": region, "total": total, "raw": len(rows),
            "kept": len(keep), "removed": removed, "final": len(deduped),
            "null_country": null_country, "mismatch": mismatch}


if __name__ == "__main__":
    regions = sys.argv[1:] or list(REGIONS)
    out = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(pull_region, r): r for r in regions}
        for f in futs:
            pass
        for f, r in futs.items():
            try:
                out.append(f.result())
            except Exception as e:  # noqa: BLE001
                out.append({"region": r, "error": str(e)[:200]})
    for o in sorted(out, key=lambda x: x["region"]):
        print(o, flush=True)
