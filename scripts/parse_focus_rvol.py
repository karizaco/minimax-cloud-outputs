#!/usr/bin/env python3
"""Parse Yahoo 5m intraday bars -> cumulative session volume -> RVOL vs TV average_volume_10d_calc.

Method (per cron #7 Step 5):
  RVOL = cumulative volume today (regular session, 5m bars)
         / average daily volume over 10 days (TradingView scanner average_volume_10d_calc)
"""
import json, os, datetime, zoneinfo

ET = zoneinfo.ZoneInfo("America/New_York")
D = "/workspace/data/rvol"
SNAP = os.path.join(D, "snap2")
OUTJSON = os.path.join(D, "parsed.json")

# TradingView public scanner, fetched 2026-10-26 ~09:55 ET (2nd pull; denominator column only)
tv = json.load(open(os.path.join(D, "tvscan2.json")))
TV = {}
for row in tv["data"]:
    sym = row["d"][0]
    TV[sym] = {"name": row["d"][5], "close_tv": row["d"][1], "avg10d": row["d"][2],
               "tv_rvol_proxy": row["d"][3], "tv_volume": row["d"][4]}

# Prior RVOL from upstream focus.md (data_date 2026-10-22) for the crossing test
PRIOR_RVOL = {"XLAB": 2.51, "MRNA": 2.50, "KOD": 0.43, "TJGC": 1.18, "CD": 0.74}
# Prior close from upstream focus.md (2026-10-22 session close) for continuity check
PRIOR_CLOSE = {"XLAB": 4.71, "MRNA": 202.63, "KOD": 85.78, "TJGC": 31.89, "CD": 8.205}

SYMS = ["XLAB", "MRNA", "KOD", "TJGC", "CD"]
now = datetime.datetime.now(ET)
results = []

for sym in SYMS:
    rec = {"symbol": sym, "name": TV[sym]["name"], "avg10d": TV[sym]["avg10d"],
           "prior_rvol": PRIOR_RVOL[sym], "prior_close": PRIOR_CLOSE[sym],
           "tv_rvol_proxy_daily": round(TV[sym]["tv_rvol_proxy"], 4),
           "tv_close": TV[sym]["close_tv"]}
    p = os.path.join(SNAP, sym + ".json")
    if not os.path.exists(p):
        rec.update(status="no_intraday_bars", error="fetch_failed")
        results.append(rec); continue
    j = json.load(open(p))
    r = (j.get("chart") or {}).get("result")
    if not r:
        rec.update(status="no_intraday_bars", error=f"api_error:{(j.get('chart') or {}).get('error')}")
        results.append(rec); continue

    res = r[0]
    meta = res.get("meta", {})
    ts = res.get("timestamp") or []
    q = ((res.get("indicators") or {}).get("quote") or [{}])[0]
    vols = q.get("volume") or []
    closes = q.get("close") or []

    rec["venue"] = meta.get("exchangeName")
    rec["prev_close_yahoo"] = meta.get("previousClose", meta.get("chartPreviousClose"))
    rec["regularMarketPrice"] = meta.get("regularMarketPrice")
    rmt = meta.get("regularMarketTime")
    rec["regularMarketTime_et"] = (datetime.datetime.fromtimestamp(rmt, ET).strftime("%Y-%m-%d %H:%M:%S %Z")
                                   if rmt else None)

    rows, dropped_future, dropped_pre = [], [], []
    for i, t in enumerate(ts):
        dt = datetime.datetime.fromtimestamp(t, ET)
        v = vols[i] if i < len(vols) else None
        c = closes[i] if i < len(closes) else None
        if v is None:
            continue
        if dt.date() > now.date():
            dropped_future.append((dt, v)); continue          # future-dated bar
        if dt.date() < now.date() or dt.time() < datetime.time(9, 30) or dt.time() > datetime.time(16, 0):
            dropped_pre.append((dt, v)); continue               # pre-market / prior session
        rows.append((dt, v, c))

    if not rows:
        rec.update(status="no_intraday_bars", error="no_regular_session_bars_today",
                   raw_bar_count=len(ts),
                   dropped_detail=[(d.strftime("%Y-%m-%d %H:%M"), v) for d, v in (dropped_future + dropped_pre)[:6]])
        results.append(rec); continue

    rows.sort(key=lambda x: x[0])
    last_c = rows[-1][2]
    quote_dt = datetime.datetime.fromtimestamp(rmt, ET) if rmt else now
    cum = sum(v for _, v, _ in rows if v is not None)
    # the newest bar is "in progress" if the quote stamp falls inside its 5-minute window
    last_bar_start = rows[-1][0]
    in_progress = (quote_dt - last_bar_start).total_seconds() < 300
    null_bars = [dt.strftime("%H:%M:%S") for dt, v, _ in rows if v is None]
    # last bar that is fully closed (its window ended at or before the quote stamp)
    closed = [dt for dt, v, _ in rows if v is not None and dt + datetime.timedelta(minutes=5) <= quote_dt]
    last_closed = closed[-1] if closed else None
    elapsed_min = (quote_dt - quote_dt.replace(hour=9, minute=30, second=0, microsecond=0)).total_seconds() / 60
    session_frac = max(min(elapsed_min / 390.0, 1.0), 1e-9)

    rec.update(status="ok",
               bar_count=len(rows),
               cum_volume=cum,
               in_progress_bar=bool(in_progress),
               in_progress_bar_start=last_bar_start.strftime("%H:%M:%S") if in_progress else None,
               in_progress_bar_vol=(rows[-1][1] if rows[-1][1] is not None else 0) if in_progress else 0,
               null_volume_bars=null_bars,
               data_timestamp_et=quote_dt.strftime("%Y-%m-%d %H:%M:%S %Z"),
               last_bar_start_et=last_bar_start.strftime("%H:%M:%S"),
               last_closed_bar_start=last_closed.strftime("%H:%M:%S") if last_closed else None,
               session_minutes_elapsed=round(elapsed_min, 1),
               session_fraction_elapsed=round(session_frac, 4),
               close=last_c,
               previous_close=meta.get("previousClose", meta.get("chartPreviousClose")),
               dropped_future_bars=len(dropped_future),
               dropped_outside_session_bars=len(dropped_pre),
               dropped_detail=[(d.strftime("%Y-%m-%d %H:%M"), v) for d, v in dropped_future[:6]],
               rvol=round(cum / TV[sym]["avg10d"], 4) if TV[sym]["avg10d"] else None,
               rvol_pace_adjusted=round((cum / TV[sym]["avg10d"]) / session_frac, 3) if TV[sym]["avg10d"] else None)
    results.append(rec)

json.dump(results, open(OUTJSON, "w"), indent=1)
for r in results:
    print(f"{r['symbol']:6} {r['status']:22} rvol={str(r.get('rvol')):8} cum={str(r.get('cum_volume')):>12} "
          f"avg10d={r['avg10d']:>14,.0f} ts={str(r.get('data_timestamp_et')):30} close={r.get('close')} "
          f"prevC={r.get('previous_close')} ts={r.get('data_timestamp_et')} lastClosed={r.get('last_closed_bar_start')} inprog={r.get('in_progress_bar')} pace={r.get('rvol_pace_adjusted')}")
    if r.get("in_progress"):
        print(f"       in-progress bar {r['in_progress_bar_ts']} vol={r['in_progress_bar_vol']} excluded from cum")
    if r.get("dropped_detail"):
        print(f"       dropped: {r['dropped_detail']}")
    if r.get("error"):
        print(f"       error: {r['error']} (raw_ts={r.get('raw_bar_count')})")
