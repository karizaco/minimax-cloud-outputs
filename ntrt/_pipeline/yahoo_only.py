#!/usr/bin/env python3
"""Yahoo cross-check only: one single-symbol spark request per ticker, long gaps.

Yahoo's rate limiter on this sandbox is tight (bursts -> HTTP 429 "Too Many
Requests"; a 16-symbol spark list is rejected outright). Recipe that works:
  * single symbol per request
  * >= 8 s between requests
  * >= 150 s cooldown before the first request
  * curl, not urllib (urllib's client fingerprint gets 429 on the same IP)
"""
from __future__ import annotations

import json
import subprocess
import time
import urllib.parse
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
RAW = Path("/workspace/ntrt/_raw")
UA = "Mozilla/5.0"   # short UA: Yahoo 429s the long Chrome UA on this edge


def curl_json(url, tries=2):
    last = "unknown"
    for a in range(tries):
        p = subprocess.run(["curl", "-s", "-m", "25", "-A", UA, url],
                           capture_output=True, text=True)
        if p.returncode == 0 and p.stdout.strip().startswith("{"):
            try:
                return json.loads(p.stdout)
            except Exception as e:  # noqa: BLE001
                last = f"json: {e}"
        else:
            last = (p.stdout or p.stderr)[:120].strip()
        time.sleep(12 + 10 * a)
    return {"_error": last}


def spark_one(sym):
    """query2 first: it kept answering 429-free while query1 was banned."""
    for host in ("query2", "query1"):
        u = (f"https://{host}.finance.yahoo.com/v8/finance/spark?symbols={urllib.parse.quote(sym, safe=",")}"
             "&range=1d&interval=1m")
        j = curl_json(u, tries=2)
        if "_error" not in j and sym in j:
            return j[sym], host
        time.sleep(3)
    return {}, "none"


def main():
    pub = json.loads((RAW / "publishable_full.json").read_text())
    rows = [{"ticker": r["t"], "close": r["close"], "premarket_change_pct": r["gap"], "premarket_close": r["pmc"]} for r in pub]
    up = sorted([r for r in rows if r["premarket_change_pct"] > 0],
                key=lambda r: -r["premarket_change_pct"])[:5]
    dn = sorted([r for r in rows if r["premarket_change_pct"] < 0],
                key=lambda r: r["premarket_change_pct"])[:5]
    target = up + dn
    print("cooldown 45s for Yahoo rate-limit window ...", flush=True)
    time.sleep(45)
    xc = []
    for r in target:
        sym = r["ticker"]
        s, host = spark_one(sym)
        rec = {"ticker": sym, "tv_gap_pct": r["premarket_change_pct"],
               "tv_close": r["close"], "tv_premarket_close": r["premarket_close"]}
        notes = []
        if not s or sym not in s:
            rec["verdict"] = "UNVERIFIED"
            rec["notes"] = [str(s.get("_error") if isinstance(s, dict) else "symbol absent")[:140]]
            xc.append(rec)
            print(f"  {sym:<6} UNVERIFIED {rec['notes']}", flush=True)
            time.sleep(9)
            continue
        s = s[sym]
        rec["yahoo_host"] = host
        rec["yahoo_previous_close"] = s.get("previousClose")
        rec["yahoo_fullday_price"] = s.get("fulldayPrice")
        rec["yahoo_gap_pct"] = s.get("fulldayChangePercent")
        ts = s.get("timestamp") or []
        if ts:
            rec["yahoo_snapshot_et"] = datetime.fromtimestamp(ts[-1], ET).strftime("%Y-%m-%d %H:%M")
        pc, yc = r["close"], s.get("previousClose")
        if pc and yc:
            d = (pc - yc) / yc * 100
            rec["ref_close_diff_pct"] = d
            if abs(d) > 0.5:
                notes.append(f"STALE_REF: TV close {pc} vs Yahoo prior close {yc} ({d:+.2f}%)")
        yg = s.get("fulldayChangePercent")
        if yg is not None:
            rec["gap_diff_pp"] = yg - r["premarket_change_pct"]
            rec["band"] = ("within_1pp" if abs(rec["gap_diff_pp"]) <= 1 else
                           "within_3pp" if abs(rec["gap_diff_pp"]) <= 3 else "outlier_3pp+")
        else:
            notes.append("yahoo fullday pct unavailable")
        rec["notes"] = notes
        rec["verdict"] = "MISMATCH" if any(n.startswith("STALE_REF") for n in notes) else (
            "UNVERIFIED" if notes else "AGREE")
        xc.append(rec)
        print(f"  {sym:<6} tv={rec['tv_gap_pct']:>8.2f} yahoo={rec.get('yahoo_gap_pct')} "
              f"diff_pp={None if rec.get('gap_diff_pp') is None else round(rec['gap_diff_pp'],2)} "
              f"refdiff={None if rec.get('ref_close_diff_pct') is None else round(rec['ref_close_diff_pct'],3)} "
              f"band={rec.get('band')} {rec['verdict']}", flush=True)
        time.sleep(9)

    # reference-session stamp for the top 3 names
    stamps = {}
    for r in target[:3]:
        u = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(r['ticker'])}"
             "?interval=1d&range=10d")
        j = curl_json(u, tries=2)
        res = (j.get("chart") or {}).get("result")
        if res:
            rr = res[0]
            ts = rr.get("timestamp") or []
            q = ((rr.get("indicators") or {}).get("quote") or [{}])[0]
            bars = [(datetime.fromtimestamp(t, ET).date().isoformat(), float(c))
                    for t, c in zip(ts, q.get("close") or []) if c is not None]
            stamps[r["ticker"]] = {
                "reference_session_et": bars[-1][0] if bars else None,
                "reference_close": bars[-1][1] if bars else None,
                "prior_session_et": bars[-2][0] if len(bars) > 1 else None,
                "prior_close": bars[-2][1] if len(bars) > 1 else None,
                "n_daily_bars": len(bars),
            }
        else:
            stamps[r["ticker"]] = {"error": "unavailable"}
        time.sleep(9)

    out_xc = {
        "checked_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "checked_at_et": datetime.now(ET).strftime("%Y-%m-%d %H:%M:%S %Z"),
        "agree": sum(1 for c in xc if c["verdict"] == "AGREE"),
        "mismatch": sum(1 for c in xc if c["verdict"] == "MISMATCH"),
        "unverified": sum(1 for c in xc if c["verdict"] == "UNVERIFIED"),
        "reference_stamps": stamps, "results": xc,
    }
    (RAW / "yahoo_crosscheck_final.json").write_text(json.dumps(out_xc, indent=1))
    print(json.dumps(out_xc, indent=1))


if __name__ == "__main__":
    main()
