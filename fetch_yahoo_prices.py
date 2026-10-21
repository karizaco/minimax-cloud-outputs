#!/usr/bin/env python3
"""EOD price refresh for 2026-10-21 — Yahoo Finance fallback path.

TradingView's screener (scanner.tradingview.com) is unreachable from this
sandbox today: the TLS handshake is reset by every CloudFront edge
(18.165.83.23/.27/.74/.125) — 000 / SSL_ERROR_SYSCALL on every retry, while
www.tradingview.com still returns 200. Yahoo's authenticated endpoints
(quote/quoteSummary, crumb) are also blocked (fc.yahoo.com and
finance.yahoo.com are unreachable), so only the unauthenticated
/v8/finance/chart endpoint is usable.

Plan (single fallback, then stop):
  universe  = cached screener pull from 2026-10-20 (skill's 7-day universe
              cache TTL) with venue-duplicate rows collapsed per region
  prices    = fresh Yahoo /v8/finance/chart per symbol (OHLCV + change%)
  mcap/pe/sector = carried forward from the 2026-10-20 file (skill's
              enrichment-cache TTL: pe/sector 30d, volume 1d)
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

spec = importlib.util.spec_from_file_location("vy", "/workspace/verify_yahoo.py")
vy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vy)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
DATA = "/workspace/data"
OUT = "/workspace/data2"
DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-21"
WORKERS = 24

PRIMARY_LISTING = {
    "jp": ["TSE", "NAG", "FSE", "SAPSE"], "tw": ["TWSE", "TPEx"],
    "ca": ["TSX", "NEO", "TSXV", "CSE"],
    "eu-de": ["XETR", "FWB", "TRADEGATE", "GETTEX", "MUN", "DUS", "HAM",
              "HAN", "SWB", "LSX", "LS", "BER", "STU"],
    "eu-it": ["MIL", "EUROTLX"], "eu-nl": ["AMS", "AS", "EURONEXT"],
    "eu-fr": ["EPA", "EURONEXT"], "eu-es": ["BME"], "eu-be": ["BSE", "BRU"],
    "eu-at": ["VIE"], "eu-pt": ["LIS"], "eu-ie": ["ISE", "Dublin"],
    "eu-fi": ["HEL"], "eu-dk": ["CPH"], "eu-gr": ["ATHEX", "ATH"], "au": ["ASX"],
}
INTL = ["au", "jp", "tw", "ca", "eu-de", "eu-fr", "eu-it", "eu-es", "eu-nl",
        "eu-be", "eu-at", "eu-pt", "eu-ie", "eu-fi", "eu-dk", "eu-gr"]

_lock = threading.Lock()
_done = [0]
_seen = {}
_t0 = time.time()


def norm(n):
    return re.sub(r"[^a-z0-9]", "", (n or "").lower())


def build_universe():
    """Cached universe -> final row list per region (venue dupes collapsed)."""
    out = {}
    for region in ["us"] + INTL:
        rows = json.load(open(f"{DATA}/{region}.json", encoding="utf-8"))["rows"]
        if region in PRIMARY_LISTING:
            # one canonical row per company per region (skill's dedupe intent,
            # extended to issuers whose symbol differs across venues)
            prio = {e: i for i, e in enumerate(PRIMARY_LISTING[region])}
            groups = {}
            for r in rows:
                key = norm(r["values"][1]) or r["ticker"]
                groups.setdefault(key, []).append(r)
            kept = []
            for g in groups.values():
                g.sort(key=lambda r: (prio.get(r["ticker"].split(":")[0], 999),
                                      r["ticker"]))
                kept.append(g[0])
        else:
            kept = rows
        out[region] = kept
    return out


def fetch(sym):
    """One Yahoo chart call. Returns dict of parsed fields or a status."""
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
           f"?range=1d&interval=1d")
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                payload = json.loads(r.read().decode())
            res = (payload.get("chart") or {}).get("result")
            if not res:
                return {"status": "no_data", "symbol": sym}
            d = res[0]
            meta = d.get("meta") or {}
            q = ((d.get("indicators") or {}).get("quote") or [{}])[0] or {}
            ts = d.get("timestamp") or []
            # last non-null bar
            idx = None
            for i in range(len(q.get("close") or []) - 1, -1, -1):
                if (q.get("close") or [None] * 99)[i] is not None:
                    idx = i
                    break
            def g(k):
                if idx is None:
                    return None
                arr = q.get(k) or []
                return arr[idx] if idx < len(arr) else None
            prev = meta.get("chartPreviousClose")
            close = g("close")
            chg = meta.get("regularMarketChangePercent")
            if chg is None and close is not None and prev:
                chg = (close - prev) / prev * 100.0
            return {
                "status": "ok", "symbol": sym,
                "open": g("open"), "high": g("high"), "low": g("low"),
                "close": close, "volume": g("volume"),
                "change_pct": chg, "prev_close": prev,
                "price": meta.get("regularMarketPrice"),
                "day_high": meta.get("regularMarketDayHigh"),
                "day_low": meta.get("regularMarketDayLow"),
                "mtime": meta.get("regularMarketTime"),
                "bar_ts": ts[idx] if idx is not None and idx < len(ts) else None,
                "currency": meta.get("currency"),
                "yahoo_exchange": meta.get("fullExchangeName")
                                 or meta.get("exchangeName"),
                "name": meta.get("longName") or meta.get("shortName"),
            }
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return {"status": "no_data", "symbol": sym}
            if e.code == 429:
                last = e
                time.sleep(2.0 + attempt)
                continue
            last = e
            time.sleep(1.0 + attempt)
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.0 + attempt)
    return {"status": "error", "symbol": sym, "error": str(last)[:120]}


def main():
    os.makedirs(OUT, exist_ok=True)
    uni = build_universe()
    jobs = []
    for region, rows in uni.items():
        for r in rows:
            ys = vy.to_yahoo(r["ticker"], region)
            if ys:
                jobs.append((r["ticker"], ys, region))
    print(f"universe rows={sum(len(v) for v in uni.values())} fetch_jobs={len(jobs)}",
          flush=True)

    results = {}

    def run(job):
        tv, ys, region = job
        rec = fetch(ys)
        rec["ticker"] = tv
        rec["region"] = region
        with _lock:
            _done[0] += 1
            n = _done[0]
            if n % 1000 == 0:
                el = time.time() - _t0
                rate = n / el if el else 0
                left = (len(jobs) - n) / rate if rate else 0
                st = _seen.get(rec["status"], 0) + 1
                _seen[rec["status"]] = st
                print(f"  {n}/{len(jobs)} ({rate:.1f}/s, eta {left/60:.1f} min) "
                      f"status={rec['status']}", flush=True)
        return rec

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for rec in ex.map(run, jobs):
            results[rec["ticker"]] = rec

    json.dump(results, open(f"{OUT}/yahoo_prices_{DATE}.json", "w"), indent=0)
    st = {}
    for r in results.values():
        st[r["status"]] = st.get(r["status"], 0) + 1
    print("DONE statuses:", st, "elapsed", round(time.time() - _t0, 1), "s")
    for region in ["us"] + INTL:
        n = sum(1 for r in results.values() if r["region"] == region)
        ok = sum(1 for r in results.values()
                 if r["region"] == region and r["status"] == "ok")
        print(f"  {region:6s} {ok}/{n} ok", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
