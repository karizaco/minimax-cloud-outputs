#!/usr/bin/env python3
"""Cross-check: TradingView scanner closes vs Yahoo Finance settled closes.

Purpose: (1) prove the TV snapshot is the 2026-10-26 settled session, not a stale or
in-progress bar; (2) quantify field agreement so the artifact can state a real agreement
rate rather than asserting the data is correct.
"""
import json
import random
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, "/workspace/data")
from yahoo import chart  # noqa: E402

TV = "/workspace/data/tv_universe_raw.json"
SAMPLE_OUT = "/workspace/data/tv_yahoo_crosscheck.json"

raw = json.load(open(TV))
cols = raw["columns"]
idx = {c: i for i, c in enumerate(cols)}

rows = {}
for r in raw["rows"]:
    d = r["d"]
    rows[r["s"]] = {
        "name": d[idx["name"]],
        "close": d[idx["close"]],
        "change": d[idx["change"]],
        "type": d[idx["type"]],
        "exchange": d[idx["exchange"]],
        "update_mode": d[idx["update_mode"]],
    }

# sample: all SPY/RSP/QQQ/IWM style index funds + a random sample of major-exchange stocks
idxfunds = [k for k, v in rows.items() if v["name"] in ("SPY", "RSP", "QQQ", "IWM", "QQQE", "DIA", "VTI", "VOO")]
stocks = [k for k, v in rows.items() if v["type"] == "stock" and v["exchange"] in ("NYSE", "NASDAQ", "AMEX")
          and v["close"]]
random.seed(20261026)
sample = idxfunds + random.sample(stocks, 40)

results = []
for k in sample:
    sym = rows[k]["name"]
    r = chart(sym, "1mo")
    m = r.get("meta", {})
    bars = r.get("bars", [])
    y_last = bars[-1] if bars else None
    y_close = y_last[4] if y_last else None
    y_date = datetime.fromtimestamp(y_last[0], tz=timezone.utc).strftime("%Y-%m-%d") if y_last else None
    tv_close = rows[k]["close"]
    diff_pct = None
    if y_close and tv_close:
        diff_pct = (tv_close - y_close) / y_close * 100
    results.append({
        "ticker_id": k, "symbol": sym, "tv_close": tv_close, "tv_change_pct": rows[k]["change"],
        "tv_update_mode": rows[k]["update_mode"],
        "yahoo_close": y_close, "yahoo_bar_date": y_date,
        "yahoo_regularMarketTime": m.get("regularMarketTime"),
        "diff_pct": diff_pct,
    })
    time.sleep(0.25)

ok = [r for r in results if r["diff_pct"] is not None and abs(r["diff_pct"]) < 0.005]
bad = [r for r in results if r["diff_pct"] is not None and abs(r["diff_pct"]) >= 0.005]
nodata = [r for r in results if r["diff_pct"] is None]
bar_dates = sorted({r["yahoo_bar_date"] for r in results if r["yahoo_bar_date"]})

summary = {
    "checked": len(results),
    "agree_within_0.005pct": len(ok),
    "mismatch": len(bad),
    "no_data": len(nodata),
    "yahoo_bar_dates_seen": bar_dates,
    "agreement_rate_pct": round(100 * len(ok) / max(1, len(ok) + len(bad)), 2),
    "mismatches": bad,
}
print(json.dumps(summary, indent=2))
json.dump({"summary": summary, "rows": results}, open(SAMPLE_OUT, "w"), indent=2)
print(f"wrote {SAMPLE_OUT}", file=sys.stderr)
