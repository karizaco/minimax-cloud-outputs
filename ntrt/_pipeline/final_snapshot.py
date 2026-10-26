#!/usr/bin/env python3
"""Cron #25 ntrt-gap-brief — final snapshot: screener + independent Yahoo cross-check.

Order matters: the TradingView screen and the Yahoo check are taken seconds apart
so the two premarket marks are comparable (this book is moving fast -- XP went
-51.1% -> -54.7% in ten minutes on 2026-10-26).

Three guards, each able to kill a row alone:

  G1  INTERNAL CONSISTENCY (free, every row)
      TV's own three numbers must agree:
          implied_ref = premarket_close / (1 + premarket_change/100)  ==  close
      A mismatch means the % was measured against a DIFFERENT reference than the
      row's own close -> a phantom gap. (BUUU today: implied ref 53.88 vs a real
      close of 5.39 -- a 10x artifact, not a real move.)

  G2  SCREENER FILTERS (skill spec)
      market_cap_basic >= $200m, volume >= 10,000, type=stock, exchange != OTC.

  G3  INDEPENDENT YAHOO CROSS-CHECK
      Yahoo's /v8/finance/spark returns, in ONE request for all symbols:
          previousClose / chartPreviousClose -> the reference close
          fulldayPrice, fulldayChangePercent   -> Yahoo's own pre+post mark
      Yahoo's fullday % is measured against the same prior close as TV's
      premarket_change, so the two are directly comparable.

Yahoo client note: urllib gets HTTP 429 from Yahoo while curl on the SAME IP
returns 200 (verified 2026-10-26) -- all Yahoo traffic goes through curl.
"""
from __future__ import annotations

import os
import json
import ssl
import subprocess
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
RAW = Path("/workspace/ntrt/_raw")
RAW.mkdir(parents=True, exist_ok=True)
SCANNER = "https://scanner.tradingview.com/america/scan"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
CTX = ssl.create_default_context()

COLUMNS = [
    "name", "description", "close", "change", "premarket_close", "premarket_open",
    "premarket_change", "premarket_change_abs", "premarket_volume",
    "market_cap_basic", "sector", "industry", "exchange", "country", "volume",
    "average_volume_30d_calc", "relative_volume_10d_calc", "Perf.W", "update_mode",
]
CI = {c: i for i, c in enumerate(COLUMNS)}
BASE = [
    {"left": "type", "operation": "equal", "right": "stock"},
    {"left": "exchange", "operation": "not_in_range", "right": ["OTC"]},
]


def post(payload, tries=3):
    for a in range(tries):
        try:
            req = urllib.request.Request(
                SCANNER, data=json.dumps(payload).encode(),
                headers={"Content-Type": "application/json", "User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001
            if a == tries - 1:
                return {"_error": f"{type(e).__name__}: {e}"}
            time.sleep(2 + 2 * a)
    return {"_error": "unreachable"}


def scan(tag, extra, sort_order, n=40):
    res = post({
        "filter": BASE + extra, "options": {"lang": "en"}, "markets": ["america"],
        "symbols": {"query": {"types": []}, "tickers": []}, "columns": COLUMNS,
        "sort": {"sortBy": "premarket_change", "sortOrder": sort_order}, "range": [0, n],
    })
    (RAW / f"{tag}.json").write_text(json.dumps(res, indent=1))
    print(f"[{tag}] totalCount={res.get('totalCount')} returned={len(res.get('data', []))}", flush=True)
    return res.get("data", [])


def norm(rows):
    out = []
    for r in rows:
        d = r["d"]
        g = lambda c: d[CI[c]]  # noqa: E731
        pmc = g("premarket_change")
        if pmc is None:
            continue
        close, pmclose = g("close"), g("premarket_close")
        implied = pmclose / (1 + pmc / 100) if (pmclose is not None and close) else None
        err = (implied - close) / close * 100 if (implied is not None and close) else None
        out.append({
            "symbol": r["s"], "ticker": g("name"), "name": g("description"),
            "close": close, "day_change_pct": g("change"),
            "premarket_close": pmclose, "premarket_open": g("premarket_open"),
            "premarket_change_pct": pmc, "premarket_change_abs": g("premarket_change_abs"),
            "premarket_volume": g("premarket_volume"),
            "market_cap": g("market_cap_basic"), "sector": g("sector"),
            "industry": g("industry"), "exchange": g("exchange"), "country": g("country"),
            "volume": g("volume"), "avg_volume_30d": g("average_volume_30d_calc"),
            "relative_volume_10d": g("relative_volume_10d_calc"),
            "perf_week_pct": g("Perf.W"), "update_mode": g("update_mode"),
            "implied_ref_close": implied, "consistency_err_pct": err,
        })
    return out


def curl_json(url, timeout=25, tries=3):
    last = "unknown"
    for a in range(tries):
        p = subprocess.run(["curl", "-s", "-m", str(timeout), "-A", UA, url],
                           capture_output=True, text=True)
        if p.returncode == 0 and p.stdout.strip():
            try:
                return json.loads(p.stdout)
            except Exception as e:  # noqa: BLE001
                last = f"json: {e} :: {p.stdout[:120]}"
        else:
            last = f"curl rc={p.returncode} {p.stderr[:120]}"
        time.sleep(3 + 3 * a)
    return {"_error": last}


def spark(symbols):
    """Yahoo rejects oversized spark symbol lists (16 -> 'Too Many Requests',
    8 -> fine). Chunk at 6 with a pause between chunks."""
    merged = {}
    chunks = [symbols[i:i + 6] for i in range(0, len(symbols), 6)]
    for ci, ch in enumerate(chunks):
        q = urllib.parse.quote(",".join(ch))
        u = (f"https://query1.finance.yahoo.com/v8/finance/spark?symbols={q}"
             "&range=1d&interval=1m")
        j = curl_json(u)
        if "_error" in j:
            print(f"  spark chunk {ci} ERROR: {j['_error'][:120]}", flush=True)
        else:
            merged.update(j)
        if ci < len(chunks) - 1:
            time.sleep(3.0)
    (RAW / "yahoo_spark.json").write_text(json.dumps(merged, indent=1))
    return merged


def chart_meta(sym):
    """Daily bars -> the reference session (date + close) the premarket % is
    measured against. NOTE: meta.regularMarketTime is NOT the reference stamp
    during premarket -- it moves to the latest print, so the daily bar series
    is the reliable source."""
    u = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}"
         "?interval=1d&range=10d")
    j = curl_json(u, tries=2)
    res = (j.get("chart") or {}).get("result")
    if not res:
        return {"error": str((j.get("chart") or {}).get("error") or j.get("_error"))[:140]}
    r = res[0]
    ts = r.get("timestamp") or []
    q = ((r.get("indicators") or {}).get("quote") or [{}])[0]
    closes = q.get("close") or []
    bars = [(datetime.fromtimestamp(t, ET).date().isoformat(), float(c))
            for t, c in zip(ts, closes) if c is not None]
    m = r.get("meta", {})
    out = {
        "reference_session_et": bars[-1][0] if bars else None,
        "reference_close": bars[-1][1] if bars else None,
        "prior_session_et": bars[-2][0] if len(bars) > 1 else None,
        "prior_close": bars[-2][1] if len(bars) > 1 else None,
        "n_daily_bars": len(bars),
        "exchange": m.get("fullExchangeName"), "currency": m.get("currency"),
        "fifty_two_week_low": m.get("fiftyTwoWeekLow"),
        "fifty_two_week_high": m.get("fiftyTwoWeekHigh"),
    }
    return out


def main():
    t0 = time.time()
    up = scan("final_up", [{"left": "premarket_change", "operation": "egreater", "right": 3}], "desc")
    dn = scan("final_down", [{"left": "premarket_change", "operation": "eless", "right": -3}], "asc")
    rows = norm(up) + norm(dn)

    kept, g1_fail, g2_fail = [], [], []
    for r in rows:
        if r["consistency_err_pct"] is not None and abs(r["consistency_err_pct"]) > 0.5:
            g1_fail.append(r)
            continue
        if (r["market_cap"] or 0) < 200_000_000:
            g2_fail.append({"ticker": r["ticker"], "name": r["name"], "reason": "market cap < $200m",
                            "market_cap": r["market_cap"], "gap": r["premarket_change_pct"]})
            continue
        if (r["volume"] or 0) < 10_000:
            g2_fail.append({"ticker": r["ticker"], "name": r["name"], "reason": "volume < 10,000",
                            "volume": r["volume"], "gap": r["premarket_change_pct"]})
            continue
        kept.append(r)
    kept.sort(key=lambda r: -abs(r["premarket_change_pct"]))
    print(f"G1 failed={len(g1_fail)} G2 excluded={len(g2_fail)} kept={len(kept)}", flush=True)

    # ---- G3 cross-check ----------------------------------------------------
    if os.environ.get("SKIP_YAHOO") == "1":
        snap = {"snapshot_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "snapshot_et": datetime.now(ET).strftime("%Y-%m-%d %H:%M:%S %Z"),
                "elapsed_s": round(time.time() - t0, 1),
                "counts": {"raw_up": len(up), "raw_down": len(dn),
                           "g1_failed": len(g1_fail), "g2_failed": len(g2_fail), "kept": len(kept)},
                "g1_failures": [{"ticker": r["ticker"], "name": r["name"],
                                 "gap_pct": r["premarket_change_pct"], "close": r["close"],
                                 "premarket_close": r["premarket_close"],
                                 "implied_ref": r["implied_ref_close"],
                                 "consistency_err_pct": r["consistency_err_pct"]} for r in g1_fail],
                "g2_exclusions": sorted(g2_fail, key=lambda x: -abs(x["gap"]))[:25],
                "rows": kept, "yahoo_crosscheck": None}
        (RAW / "final_snapshot.json").write_text(json.dumps(snap, indent=1))
        print(f"screener-only snapshot written: kept={len(kept)} at {snap['snapshot_et']}", flush=True)
        return
    print("cooldown 45s for Yahoo rate-limit window ...", flush=True)
    time.sleep(45)
    target = kept[:16]
    sp = spark([r["ticker"] for r in target])
    xc = []
    for r in target:
        s = (sp.get(r["ticker"]) or {}) if isinstance(sp, dict) else {}
        rec = {"ticker": r["ticker"], "tv_gap_pct": r["premarket_change_pct"],
               "tv_close": r["close"], "tv_premarket_close": r["premarket_close"]}
        notes = []
        if not s:
            rec["verdict"] = "UNVERIFIED"
            rec["notes"] = ["not present in Yahoo spark response"]
            xc.append(rec)
            continue
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

    # reference-session stamp for the top 3 names
    stamps = {}
    for r in target[:3]:
        stamps[r["ticker"]] = chart_meta(r["ticker"])
        time.sleep(1.2)

    agree = sum(1 for c in xc if c["verdict"] == "AGREE")
    mism = sum(1 for c in xc if c["verdict"] == "MISMATCH")
    unver = sum(1 for c in xc if c["verdict"] == "UNVERIFIED")
    out = {
        "snapshot_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "snapshot_et": datetime.now(ET).strftime("%Y-%m-%d %H:%M:%S %Z"),
        "elapsed_s": round(time.time() - t0, 1),
        "counts": {"raw_up": len(up), "raw_down": len(dn),
                   "universe_up_totalcount": None, "universe_down_totalcount": None,
                   "g1_failed": len(g1_fail), "g2_failed": len(g2_fail), "kept": len(kept)},
        "g1_failures": [{"ticker": r["ticker"], "name": r["name"],
                         "gap_pct": r["premarket_change_pct"], "close": r["close"],
                         "premarket_close": r["premarket_close"],
                         "implied_ref": r["implied_ref_close"],
                         "consistency_err_pct": r["consistency_err_pct"]} for r in g1_fail],
        "g2_exclusions": sorted(g2_fail, key=lambda x: -abs(x["gap"]))[:25],
        "rows": kept,
        "yahoo_crosscheck": {"agree": agree, "mismatch": mism, "unverified": unver,
                             "reference_stamps": stamps, "results": xc},
    }
    (RAW / "final_snapshot.json").write_text(json.dumps(out, indent=1))
    print(f"\nYahoo spark: agree={agree} mismatch={mism} unverified={unver} ({len(xc)} checked)")
    for c in xc:
        print(f"  {c['ticker']:<6} tv={c['tv_gap_pct']:>8.2f} yahoo={c.get('yahoo_gap_pct')} "
              f"diff_pp={None if c.get('gap_diff_pp') is None else round(c['gap_diff_pp'],2)} "
              f"refdiff={None if c.get('ref_close_diff_pct') is None else round(c['ref_close_diff_pct'],3)} "
              f"band={c.get('band')} {c['verdict']} {'; '.join(c.get('notes', []))}")
    print("\nG1 failures (dropped):")
    for r in g1_fail:
        print(f"  {r['ticker']:<6} gap={r['premarket_change_pct']:>8.2f}% close={r['close']} "
              f"pmc={r['premarket_close']} implied_ref={r['implied_ref_close']:.4f} "
              f"err={r['consistency_err_pct']:+.1f}% | {r['name'][:40]}")
    print("\nreference stamps:", json.dumps(stamps, indent=1))


if __name__ == "__main__":
    main()
