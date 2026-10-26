#!/usr/bin/env python3
"""fetch_tv.py — international EOD universe pull from the TradingView screener.

Re-implementation (Cloud) of the skill's `pull_international.py` screener step.
The TradingView MCP tools are not bound in Cloud sessions, so the public
scanner HTTP API is used directly. One POST per 3000-row page.

Output: /workspace/data/<region>.json  (raw screener rows, sorted by market cap)
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

CA = "/etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt"
DATA = "/workspace/data"
PAGE = 3000

COLUMNS = ["name", "description", "open", "high", "low", "close", "volume",
           "change", "market_cap_basic", "price_earnings_ttm", "sector",
           "exchange", "currency", "type", "country", "update_mode"]

# region -> (country name used by the screener, endpoint slug, exchange slug for reference)
REGIONS = {
    "au":    ("Australia",    "australia"),
    "jp":    ("Japan",        "japan"),
    "tw":    ("Taiwan",       "taiwan"),
    "ca":    ("Canada",       "canada"),
    "eu-de": ("Germany",      "germany"),
    "eu-fr": ("France",       "france"),
    "eu-it": ("Italy",        "italy"),
    "eu-es": ("Spain",        "spain"),
    "eu-nl": ("Netherlands",  "netherlands"),
    "eu-be": ("Belgium",      "belgium"),
    "eu-at": ("Austria",      "austria"),
    "eu-pt": ("Portugal",     "portugal"),
    "eu-ie": ("Ireland",      "ireland"),
    "eu-fi": ("Finland",      "finland"),
    "eu-dk": ("Denmark",      "denmark"),
    "eu-gr": ("Greece",       "greece"),
}

SKIP = set(json.loads(os.environ.get("SKIP_REGIONS", "[]")))


def curl(url: str, payload: dict | None = None, timeout: int = 60) -> str:
    cmd = ["curl", "-sS", "--max-time", str(timeout), "--cacert", CA]
    if payload is None:
        cmd += ["-A", "Mozilla/5.0", url]
    else:
        cmd += ["-X", "POST", url, "-H", "Content-Type: application/json",
                "-A", "Mozilla/5.0", "--data-binary", json.dumps(payload)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"curl exit {p.returncode}: {p.stderr[:200]}")
    return p.stdout


def fetch_region(region: str) -> dict:
    country, ep = REGIONS[region]
    url = f"https://scanner.tradingview.com/{ep}/scan"
    rows: list[dict] = []
    total = None
    start = 0
    pages = 0
    err = None
    while True:
        body = {
            "filter": [
                {"left": "type", "operation": "equal", "right": "stock"},
                {"left": "country", "operation": "equal", "right": country},
            ],
            "options": {"lang": "en"},
            "columns": COLUMNS,
            "range": [start, start + PAGE],
            "sort": {"sortBy": "market_cap_basic", "sortOrder": "desc"},
        }
        try:
            raw = curl(url, body)
            doc = json.loads(raw)
        except Exception as e:  # noqa: BLE001
            err = f"{type(e).__name__}: {e}"
            break
        if total is None:
            total = doc.get("totalCount")
        data = doc.get("data") or []
        if not data:
            break
        for item in data:
            vals = item.get("d") or []
            rec = {"symbol": item.get("s")}
            for i, c in enumerate(COLUMNS):
                rec[c] = vals[i] if i < len(vals) else None
            rows.append(rec)
        pages += 1
        if len(data) < PAGE:
            break
        start += PAGE
        if start > 60000:
            break
    out = {
        "region": region,
        "country": country,
        "endpoint": ep,
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "reported_totalCount": total,
        "pages": pages,
        "rows_raw": len(rows),
        "error": err,
        "rows": rows,
    }
    os.makedirs(DATA, exist_ok=True)
    with open(f"{DATA}/{region}.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh)
    return out


def main() -> int:
    regions = [r for r in REGIONS if r not in SKIP]
    print(f"fetching {len(regions)} regions: {regions}", flush=True)
    with ThreadPoolExecutor(max_workers=6) as ex:
        for out in ex.map(fetch_region, regions):
            print(f"{out['region']:6s} rows={out['rows_raw']:6d} pages={out['pages']} "
                  f"total={out['reported_totalCount']} err={out['error']}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
