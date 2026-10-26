#!/usr/bin/env python3
"""census.py — full-universe Yahoo cross-check + staleness census (cron #5).

Uses the Yahoo spark endpoint (batches of 12) to test every row we wrote:

  resolvable  — a Yahoo symbol could be built for the TV ticker
  agree       — |TV close - Yahoo price| < 0.3% AND
                 |TV change - Yahoo change%| < 0.3pp, same session
  chg_only    — close agrees, change differs (dividend/split adjustment)
  px_only     — change agrees, close differs
  not_today   — Yahoo's last trade (regularMarketTime, in the exchange's own
                 local zone) is NOT 2026-10-26: the screener row is a
                 carry-over from an earlier session
  mismatch    — both differ materially

Batches of 12 (the spark URL-length limit). Yahoo's own gmtoffset is used
for the local-date test, so no hand-rolled offsets.
"""
from __future__ import annotations

import csv
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

CA = "/etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt"
UA = "Mozilla/5.0"
DATE = os.environ.get("EOD_DATE", "2026-10-26")
OUT = f"/workspace/international-eod/{DATE}"
DATA = "/workspace/data"

# region -> {TV venue -> Yahoo suffix}. None = cannot be mapped reliably.
VENUES = {
    "au":    {"ASX": ".AX"},
    "jp":    {"TSE": ".T", "NAG": ".T", "FSE": ".T", "SAPSE": ".T"},
    "ca":    {"TSX": ".TO", "NEO": ".NE", "TSXV": ".V", "CSE": ".CN"},
    "eu-de": {"XETR": ".DE", "LSX": ".L"},
    "eu-fr": {"EURONEXT": ".PA"},
    "eu-nl": {"EURONEXT": ".AS"},
    "eu-be": {"EURONEXT": ".BR"},
    "eu-pt": {"EURONEXT": ".LS"},
    "eu-fi": {"OMXHEX": ".HE"},
    "eu-dk": {"OMXCOP": ".CO"},
    "eu-es": {"BME": ".MC"},
    "eu-it": {"MIL": ".MI"},
    "eu-gr": {"ATHEX": ".AT", "ATH": ".AT"},
}
BATCH = 12


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def yahoo_symbol(tv: str, venues: dict) -> str | None:
    if ":" not in tv:
        return None
    venue, sym = tv.split(":", 1)
    suf = venues.get(venue)
    if not suf:
        return None
    if "." in sym:          # class suffix (BCE.PR, DRAX.P) - no reliable map
        return None
    sym = sym.replace("_", "-").replace(".", "-")
    return f"{sym}{suf}"


def spark(symbols: list[str]):
    url = ("https://query1.finance.yahoo.com/v7/finance/spark?symbols="
           + ",".join(symbols) + "&range=1d&interval=1d")
    p = subprocess.run(["curl", "-sS", "--max-time", "30", "--cacert", CA,
                        "-A", UA, url], capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"curl {p.returncode}")
    doc = json.loads(p.stdout)
    if doc.get("spark", {}).get("error"):
        raise RuntimeError(str(doc["spark"]["error"])[:80])
    out = {}
    for r in (doc.get("spark", {}).get("result") or []):
        resp = r.get("response") or [{}]
        meta = (resp[0] or {}).get("meta") or {}
        if meta.get("symbol"):
            out[meta["symbol"]] = meta
    return out


def main() -> int:
    rows_by_region, tasks = {}, []
    for region, venues in VENUES.items():
        path = f"{OUT}/{region}.csv"
        if not os.path.exists(path):
            continue
        recs = list(csv.DictReader(open(path, encoding="utf-8")))
        rows_by_region[region] = recs
        for r in recs:
            ys = yahoo_symbol(r["ticker"], venues)
            if ys:
                tasks.append((region, r["ticker"], ys, num(r["close"]),
                              num(r["change_pct"]), r["name"]))
    print(f"rows={sum(len(v) for v in rows_by_region.values())} "
          f"mappable={len(tasks)} unmappable={sum(len(v) for v in rows_by_region.values())-len(tasks)}")

    batches = [tasks[i:i + BATCH] for i in range(0, len(tasks), BATCH)]
    print(f"batches={len(batches)}")

    def run(batch):
        syms = [t[2] for t in batch]
        try:
            metas = spark(syms)
        except Exception as e:  # noqa: BLE001
            return [{"error": str(e)[:80], "batch": syms[:3]} for _ in batch]
        out = []
        for (region, ticker, ys, close, change, name) in batch:
            m = metas.get(ys)
            if not m:
                out.append({"region": region, "ticker": ticker, "yahoo": ys,
                            "status": "unresolved"})
                continue
            t = m.get("regularMarketTime")
            local = None
            if t:
                local = (datetime.fromtimestamp(t, timezone.utc)
                         + __import__("datetime").timedelta(
                             seconds=m.get("gmtoffset") or 0)).date().isoformat()
            ypx = m.get("regularMarketPrice")
            ychg = m.get("regularMarketChangePercent")
            rec = {"region": region, "ticker": ticker, "yahoo": ys,
                   "name": name, "tv_close": close, "tv_change": change,
                   "yh_close": ypx, "yh_change": ychg, "yh_local_date": local,
                   "yh_volume": m.get("regularMarketVolume"),
                   "yh_name": m.get("longName") or m.get("shortName")}
            if local and local != DATE:
                rec["status"] = "not_today"
            elif ypx and close:
                px_ok = abs(close - ypx) / ypx * 100 < 0.3
                chg_ok = (ychg is not None and change is not None
                          and abs(change - ychg) < 0.3)
                if px_ok and chg_ok:
                    rec["status"] = "agree"
                elif px_ok:
                    rec["status"] = "chg_only"
                elif chg_ok:
                    rec["status"] = "px_only"
                else:
                    rec["status"] = "mismatch"
            else:
                rec["status"] = "no_price"
            out.append(rec)
        return out

    results = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        for chunk in ex.map(run, batches):
            results.extend(chunk)

    per = {}
    for r in results:
        if "error" in r:
            continue
        p = per.setdefault(r["region"], {"n": 0, "agree": 0, "chg_only": 0,
                                         "px_only": 0, "mismatch": 0,
                                         "not_today": 0, "no_price": 0,
                                         "unresolved": 0, "examples": []})
        p["n"] += 1
        st = r["status"]
        p[st] = p.get(st, 0) + 1
        if st in ("mismatch", "chg_only") and len(p["examples"]) < 8:
            p["examples"].append(r)

    for region in sorted(rows_by_region):
        p = per.get(region, {})
        total = len(rows_by_region[region])
        cov = p.get("n", 0)
        p["rows"] = total
        p["coverage_pct"] = round(cov / total * 100, 1) if total else 0
        p["not_today_pct_of_cov"] = round(p.get("not_today", 0) / cov * 100, 1) if cov else 0

    json.dump({"date": DATE, "per_region": per, "rows": results},
              open(f"{DATA}/_census.json", "w"), indent=1, default=str)
    tot = {}
    for p in per.values():
        for k, v in p.items():
            if isinstance(v, int):
                tot[k] = tot.get(k, 0) + v
    print("TOTAL:", tot)
    for region in sorted(per):
        p = per[region]
        print(f"  {region:6s} rows={p['rows']:5d} cov={p['coverage_pct']:5.1f}% "
              f"agree={p.get('agree',0):5d} chg_only={p.get('chg_only',0):4d} "
              f"px_only={p.get('px_only',0):4d} mismatch={p.get('mismatch',0):4d} "
              f"not_today={p.get('not_today',0):5d} ({p['not_today_pct_of_cov']}%) "
              f"unresolved={p.get('unresolved',0):4d}")
        for ex in p["examples"][:3]:
            print(f"        {ex['status']}: {ex['ticker']} tv_c={ex.get('tv_close')} "
                  f"tv_chg={ex.get('tv_change')} yh_c={ex.get('yh_close')} "
                  f"yh_chg={ex.get('yh_change')} date={ex.get('yh_local_date')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
