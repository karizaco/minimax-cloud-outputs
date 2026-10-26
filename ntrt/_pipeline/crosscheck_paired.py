#!/usr/bin/env python3
"""Time-matched cross-check: TradingView premarket mark vs Yahoo's own 1-minute print.

Method (drift-proof where it can be, banded where the market is moving):
  1. REFERENCE CLOSE  (drift-proof) -- TV `close` vs Yahoo `previousClose`.
     A mismatch proves the screener's gap was measured against a stale reference.
  2. GAP MAGNITUDE    (time-matched) -- TV `premarket_change` at t vs the Yahoo
     1-minute bar whose timestamp is closest to t, both expressed as a % of
     previousClose. A live book moves between two marks, so this is reported as
     a band, not a pass/fail.

Yahoo access notes (measured on this sandbox):
  * urllib -> HTTP 429 on the same URL where curl returns 200. Use curl.
  * query1 got banned; query2 kept answering. Try query2, then query1.
  * A 16-symbol spark list is rejected ("Too Many Requests"); 8 is fine.
    Use two requests of <=10.
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
SCANNER = "https://scanner.tradingview.com/america/scan"
TV_COLS = ["name", "description", "close", "premarket_close", "premarket_change",
           "market_cap_basic", "volume", "sector", "industry", "relative_volume_10d_calc",
           "average_volume_30d_calc", "premarket_volume", "premarket_change_abs"]


def curl_json(url, tries=3):
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
            last = (p.stdout or p.stderr)[:140].strip()
        time.sleep(10 + 8 * a)
    return {"_error": last}


def spark(symbols):
    out = {}
    for i in range(0, len(symbols), 8):
        chunk = symbols[i:i + 8]
        q = urllib.parse.quote(",".join(chunk), safe=",")
        got = None
        for host in ("query2", "query1"):
            u = (f"https://{host}.finance.yahoo.com/v8/finance/spark?symbols={q}"
                 "&range=1d&interval=1m")
            j = curl_json(u, tries=2)
            if "_error" not in j and any(k in j for k in chunk):
                got = j
                break
            time.sleep(3)
        if got:
            out.update(got)
        else:
            print(f"  spark chunk {i} FAILED -- retrying once", flush=True)
            time.sleep(8)
            for host in ("query1", "query2"):
                u = (f"https://{host}.finance.yahoo.com/v8/finance/spark?symbols={q}"
                     "&range=1d&interval=1m")
                j = curl_json(u, tries=2)
                if "_error" not in j and any(k in j for k in chunk):
                    out.update(j)
                    break
                time.sleep(8)
        time.sleep(8)
    return out


def tv_fetch(tickers):
    tl = ",".join(f'"{t}"' for t in tickers)
    body = {"filter": [{"left": "name", "operation": "in_range", "right": json.loads(f"[{tl}]")}],
            "options": {"lang": "en"}, "markets": ["america"],
            "symbols": {"query": {"types": []}, "tickers": []},
            "columns": TV_COLS, "range": [0, 40]}
    req = subprocess.run(
        ["curl", "-s", "-m", "30", "-X", "POST", SCANNER,
         "-H", "Content-Type: application/json", "-H", f"User-Agent: {UA}",
         "-d", json.dumps(body)], capture_output=True, text=True)
    j = json.loads(req.stdout)
    (RAW / "paired_tv.json").write_text(json.dumps(j, indent=1))
    return j


def main():
    pub = json.loads((RAW / "publishable_full.json").read_text())[:20]
    tickers = [r["t"] for r in pub]
    # The PUBLISHED Friday close (from the 09:41 coverage pass). After the open
    # TradingView's `close` column ROLLS to the live price, so the reference
    # test must use the pre-open snapshot, not a post-open fetch.
    pub_close = {r["t"]: r["close"] for r in pub}

    print("cooldown 20s ...", flush=True)
    time.sleep(20)
    t_before = time.time()
    tv = tv_fetch(tickers)
    t_tv = time.time()
    tv_et = datetime.fromtimestamp(t_tv, ET).strftime("%Y-%m-%d %H:%M:%S")
    tv_rows = {r["d"][0]: dict(zip(TV_COLS, r["d"])) for r in tv.get("data", [])}
    print(f"TV fetch at {tv_et} ET -> {len(tv_rows)} rows", flush=True)

    sp = spark(tickers)
    (RAW / "paired_yahoo.json").write_text(json.dumps(sp, indent=1))
    print(f"Yahoo spark -> {len(sp)} symbols", flush=True)

    out = []
    for t in tickers:
        r = tv_rows.get(t)
        s = sp.get(t)
        rec = {"ticker": t, "tv_snapshot_et": tv_et}
        if not r or not s:
            rec["verdict"] = "UNVERIFIED"
            rec["notes"] = ["missing from TV or Yahoo response"]
            out.append(rec)
            continue
        rec["tv_gap_pct"] = r["premarket_change"]
        rec["tv_close_published"] = pub_close.get(t)
        rec["tv_premarket_close"] = r["premarket_close"]
        rec["tv_rolls_to_live"] = (r["close"] is not None and pub_close.get(t) is not None
                                   and abs(r["close"] - pub_close[t]) / pub_close[t] * 100 > 0.5)
        rec["tv_premarket_volume"] = r["premarket_volume"]
        rec["yahoo_previous_close"] = s.get("previousClose")
        notes = []
        pc, yc = pub_close.get(t), s.get("previousClose")
        if pc and yc:
            d = (pc - yc) / yc * 100
            rec["ref_close_diff_pct"] = d
            rec["ref_verdict"] = "FRESH" if abs(d) <= 0.5 else "STALE"
            if abs(d) > 0.5:
                notes.append(f"STALE_REF: TV close {pc} vs Yahoo prior close {yc} ({d:+.3f}%)")
        else:
            rec["ref_verdict"] = "UNKNOWN"
            notes.append("no Yahoo prior close")
        # The OPEN print is the apples-to-apples comparison: TradingView's
        # premarket columns hold the pre-open (or near-open) mark, so the right
        # Yahoo bar is the 09:30 one, not the live one.
        ts = s.get("timestamp") or []
        cl = s.get("close") or []
        bars = [(datetime.fromtimestamp(x, ET), float(c)) for x, c in zip(ts, cl) if c is not None]
        rec["yahoo_n_bars"] = len(bars)
        if bars and yc:
            op = min(bars, key=lambda b: abs((b[0].hour * 60 + b[0].minute) - 570))
            rec["yahoo_open_bar_et"] = op[0].strftime("%H:%M:%S")
            rec["yahoo_open_price"] = op[1]
            rec["yahoo_open_pct"] = (op[1] - yc) / yc * 100
            rec["open_diff_pp"] = rec["yahoo_open_pct"] - r["premarket_change"]
            rec["open_band"] = ("within_1pp" if abs(rec["open_diff_pp"]) <= 1 else
                                "within_3pp" if abs(rec["open_diff_pp"]) <= 3 else
                                "within_6pp" if abs(rec["open_diff_pp"]) <= 6 else "outlier_6pp+")
            last = bars[-1]
            rec["yahoo_now_bar_et"] = last[0].strftime("%H:%M:%S")
            rec["yahoo_now_price"] = last[1]
            rec["yahoo_now_pct"] = (last[1] - yc) / yc * 100
            rec["since_open_pp"] = rec["yahoo_now_pct"] - r["premarket_change"]
        else:
            notes.append("no Yahoo 1-minute bar")
        rec["notes"] = notes
        rec["verdict"] = "MISMATCH" if any(n.startswith("STALE_REF") for n in notes) else (
            "UNVERIFIED" if notes else "AGREE")
        rec["reference_verdict"] = rec.get("ref_verdict")
        out.append(rec)

    fresh = sum(1 for c in out if c.get("ref_verdict") == "FRESH")
    stale = sum(1 for c in out if c.get("ref_verdict") == "STALE")
    bands = {}
    for c in out:
        bands[c.get("band")] = bands.get(c.get("band"), 0) + 1
    summary = {
        "tv_snapshot_et": tv_et,
        "yahoo_fetched_et": datetime.fromtimestamp(time.time(), ET).strftime("%Y-%m-%d %H:%M:%S"),
        "n": len(out), "reference_fresh": fresh, "reference_stale": stale,
        "gap_bands": bands,
        "agree": sum(1 for c in out if c["verdict"] == "AGREE"),
        "mismatch": sum(1 for c in out if c["verdict"] == "MISMATCH"),
        "unverified": sum(1 for c in out if c["verdict"] == "UNVERIFIED"),
        "results": out,
    }
    (RAW / "yahoo_crosscheck_final.json").write_text(json.dumps(summary, indent=1))
    print(f"reference fresh={fresh} stale={stale} | gap bands={bands} | "
          f"agree={summary['agree']} mismatch={summary['mismatch']} unverified={summary['unverified']}")
    for c in out:
        print(f"  {c['ticker']:<6} tvGap={c.get('tv_gap_pct')} yahooOpen@{c.get('yahoo_open_bar_et')}="
              f"{None if c.get('yahoo_open_pct') is None else round(c['yahoo_open_pct'],2)} "
              f"openDiff={None if c.get('open_diff_pp') is None else round(c['open_diff_pp'],2)} "
              f"now@{c.get('yahoo_now_bar_et')}={None if c.get('yahoo_now_pct') is None else round(c['yahoo_now_pct'],2)} "
              f"sinceOpen={None if c.get('since_open_pp') is None else round(c['since_open_pp'],2)} "
              f"ref={c.get('ref_verdict')}({None if c.get('ref_close_diff_pct') is None else round(c['ref_close_diff_pct'],4)})")


if __name__ == "__main__":
    main()
