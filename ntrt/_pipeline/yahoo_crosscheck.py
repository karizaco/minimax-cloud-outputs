#!/usr/bin/env python3
"""Cron #25 ntrt-gap-brief — independent Yahoo cross-check of TradingView premarket rows.

Two drift-proof checks per row (shared-repo lessons from cron #15, 2026-10-26):

  1. REFERENCE-CLOSE FRESHNESS
     TV `close` (the last regular-session close the premarket % is measured against)
     vs Yahoo's own last COMPLETED daily bar close. A match proves the reference is
     the true prior close; a mismatch proves a STALE reference (a phantom gap).

  2. GAP MAGNITUDE
     TV premarket_change vs Yahoo's own premarket print (last 1m bar stamped
     04:00-09:30 ET from the includePrePost feed). Thin books drift a couple of
     points, so the tolerance is a band, not equality.

Yahoo daily/1m endpoints do NOT accept comma-separated symbols -> one call each.
"""
from __future__ import annotations

import json
import ssl
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
RAW = Path("/workspace/ntrt/_raw")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
CTX = ssl.create_default_context()


def get(url: str, tries: int = 3):
    last = None
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=25, context=CTX) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
            time.sleep(1.5 * (a + 1))
    return {"_error": last}


def yahoo_symbol(tv_symbol: str) -> str:
    s = tv_symbol.split(":")[-1]
    return s.replace(" ", "-").replace("_", "-")


def daily_ref(sym: str):
    """Last completed daily bar -> (et_date, close, prev_close)."""
    u = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}"
         "?interval=1d&range=10d")
    j = get(u)
    if "_error" in j:
        return {"error": j["_error"]}
    res = (j.get("chart") or {}).get("result")
    if not res:
        return {"error": "no result"}
    r = res[0]
    ts = r.get("timestamp") or []
    q = ((r.get("indicators") or {}).get("quote") or [{}])[0]
    closes = q.get("close") or []
    bars = []
    for t, c in zip(ts, closes):
        if c is None:
            continue
        bars.append((datetime.fromtimestamp(t, ET).date().isoformat(), float(c)))
    if not bars:
        return {"error": "no bars"}
    ref_date, ref_close = bars[-1]
    prev_close = bars[-2][1] if len(bars) > 1 else None
    return {"ref_date": ref_date, "ref_close": ref_close, "prev_close": prev_close,
            "n_bars": len(bars)}


def premarket(sym: str, today_iso: str):
    """Last 1m bar stamped 04:00-09:30 ET today -> (price, ts_et, n_bars)."""
    u = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}"
         "?interval=1m&range=1d&includePrePost=true")
    j = get(u)
    if "_error" in j:
        return {"error": j["_error"]}
    res = (j.get("chart") or {}).get("result")
    if not res:
        return {"error": "no result"}
    r = res[0]
    ts = r.get("timestamp") or []
    q = ((r.get("indicators") or {}).get("quote") or [{}])[0]
    closes = q.get("close") or []
    bars = []
    for t, c in zip(ts, closes):
        if c is None:
            continue
        dt = datetime.fromtimestamp(t, ET)
        if dt.date().isoformat() != today_iso:
            continue
        if not (4 <= dt.hour < 9 or (dt.hour == 9 and dt.minute < 30)):
            continue
        bars.append((dt, float(c)))
    if not bars:
        return {"error": "no premarket bars", "n_bars": 0}
    dt, price = bars[-1]
    return {"price": price, "ts_et": dt.strftime("%Y-%m-%d %H:%M"), "n_bars": len(bars)}


def check(row: dict, today_iso: str) -> dict:
    sym = yahoo_symbol(row["symbol"])
    out = {"ticker": row["ticker"], "yahoo_symbol": sym}
    d = daily_ref(sym)
    p = premarket(sym, today_iso)
    out["daily"] = d
    out["premarket"] = p
    notes = []
    tv_close = row["close"]
    if "ref_close" in d and tv_close:
        diff_pct = (tv_close - d["ref_close"]) / d["ref_close"] * 100
        out["ref_close_diff_pct"] = diff_pct
        if abs(diff_pct) > 0.5:
            notes.append(f"STALE_REF: TV close {tv_close} vs Yahoo ref {d['ref_close']} ({diff_pct:+.2f}%)")
    else:
        notes.append("no yahoo daily ref")
    if "price" in p and "ref_close" in d and d["ref_close"]:
        y_pct = (p["price"] - d["ref_close"]) / d["ref_close"] * 100
        out["yahoo_gap_pct"] = y_pct
        out["gap_diff_pp"] = y_pct - row["premarket_change_pct"]
    else:
        notes.append("no yahoo premarket bar")
    out["notes"] = notes
    out["verdict"] = "MISMATCH" if any(n.startswith("STALE_REF") for n in notes) else (
        "UNVERIFIED" if notes else "AGREE")
    return out


def main():
    today_iso = datetime.now(ET).date().isoformat()
    payload = json.loads((RAW / "screen_rows.json").read_text())
    rows = payload["rows"]
    # Cross-check the names a reader will actually act on: top 8 by |gap| each direction.
    up = sorted([r for r in rows if r["premarket_change_pct"] > 0],
                key=lambda r: -r["premarket_change_pct"])[:8]
    dn = sorted([r for r in rows if r["premarket_change_pct"] < 0],
                key=lambda r: r["premarket_change_pct"])[:8]
    target = up + dn
    with ThreadPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(lambda r: check(r, today_iso), target))
    (RAW / "yahoo_crosscheck.json").write_text(json.dumps(
        {"checked_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "today_et": today_iso, "results": res}, indent=1))
    agree = sum(1 for r in res if r["verdict"] == "AGREE")
    mism = sum(1 for r in res if r["verdict"] == "MISMATCH")
    unver = sum(1 for r in res if r["verdict"] == "UNVERIFIED")
    print(f"agree={agree} mismatch={mism} unverified={unver} (of {len(res)})")
    tv = {r["ticker"]: r for r in rows}
    for r in res:
        t = tv.get(r["ticker"], {})
        gap = t.get("premarket_change_pct")
        yg = r.get("yahoo_gap_pct")
        print(f"  {r['ticker']:<6} tv={gap if gap is None else round(gap,2)!s:>8} "
              f"yahoo={None if yg is None else round(yg,2)!s:>8} "
              f"diff={None if r.get('gap_diff_pp') is None else round(r['gap_diff_pp'],2)!s:>7} "
              f"ref={r['daily'].get('ref_date')} {r['daily'].get('ref_close')} "
              f"pm={r['premarket'].get('ts_et')} {r['premarket'].get('price')} {r['verdict']} "
              f"{'; '.join(r['notes'])}")


if __name__ == "__main__":
    main()
