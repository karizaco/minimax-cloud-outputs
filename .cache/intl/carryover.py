#!/usr/bin/env python3
"""carryover.py — build the carry-over index and the final movers list.

A screener row for an instrument that did not trade on 2026-10-26 carries
the LAST session's close and change, dated today. That is a true statement
about the instrument but a false statement about the day, so it is
published as a separate index rather than silently mixed into the CSVs
(the CSV schema is fixed at 14 columns by the skill).

Carry-over classification:
  confirmed  - TV volume == Yahoo's volume for Yahoo's last session
               (both feeds carry the same earlier session)
  unconfirmed- TV volume != Yahoo's volume, and Yahoo's last trade is
               before today (probably still a carry-over; a few may be
               Yahoo coverage gaps)
"""
from __future__ import annotations

import csv
import json
import os
import subprocess
from datetime import datetime, timezone

CA = "/etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt"
UA = "Mozilla/5.0"
DATE = os.environ.get("EOD_DATE", "2026-10-27")
OUT = f"/workspace/international-eod/{DATE}"
DATA = "/workspace/data"
FX = {"EUR": 1.1130, "JPY": 0.0063312, "AUD": 0.7026913,
      "CAD": 0.7117944, "DKK": 0.1488804, "TWD": 0.0308604}
INDEX = {"au": ("^AXJO", 10), "jp": ("^N225", 9), "tw": ("^TWII", 3),
         "ca": ("^GSPTSE", -4), "eu-de": ("^GDAXI", 2), "eu-fr": ("^FCHI", 2),
         "eu-it": ("FTSEMIB.MI", 2), "eu-es": ("^IBEX", 2),
         "eu-nl": ("^AEX", 2), "eu-be": ("^BFX", 2),
         "eu-at": ("^ATX", 2), "eu-pt": ("PSI20.LS", 1),
         "eu-ie": ("^ISEQ", 1), "eu-fi": ("^OMXH25", 2),
         "eu-dk": ("^OMXC20", 2), "eu-gr": (None, 3)}


def yahoo(sym):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
           f"?range=10d&interval=1d")
    p = subprocess.run(["curl", "-sS", "--max-time", "25", "--cacert", CA,
                        "-A", UA, url], capture_output=True, text=True)
    if p.returncode != 0:
        return None
    try:
        res = json.loads(p.stdout)["chart"]["result"][0]
    except Exception:  # noqa: BLE001
        return None
    meta = res.get("meta") or {}
    ts = res.get("timestamp") or []
    cl = ((res.get("indicators") or {}).get("quote") or [{}])[0].get("close") or []
    bars = [(t, c) for t, c in zip(ts, cl) if c is not None]
    return {"meta": meta, "bars": bars}


def index_ctx(region):
    sym, off = INDEX[region]
    if not sym:
        return None
    d = yahoo(sym)
    if not d:
        return None
    meta, bars = d["meta"], d["bars"]
    price = meta.get("regularMarketPrice")
    chg = meta.get("regularMarketChangePercent")
    prior = bars[-1][1] if bars else None
    t = meta.get("regularMarketTime")
    local = None
    if t:
        local = (datetime.fromtimestamp(t, timezone.utc)
                 .replace(tzinfo=timezone.utc)).isoformat()
    return {"symbol": sym, "close": price, "chg_pct": chg,
            "prior_bar_close": prior, "regular_market_time_utc": local,
            "currency": meta.get("currency"),
            "exchange": meta.get("fullExchangeName")}


def main() -> int:
    census = json.load(open(f"{DATA}/_census.json", encoding="utf-8"))
    rows_by_ticker = {}
    for fn in sorted(os.listdir(OUT)):
        if not fn.endswith(".csv"):
            continue
        region = fn[:-4]
        recs = list(csv.DictReader(open(f"{OUT}/{fn}", encoding="utf-8")))
        for r in recs:
            rows_by_ticker[(region, r["ticker"])] = r

    carry = {}
    for x in census["rows"]:
        if x.get("status") != "not_today":
            continue
        r = rows_by_ticker.get((x["region"], x["ticker"]))
        if not r:
            continue
        try:
            tv_vol = float(r["volume"])
        except (TypeError, ValueError):
            tv_vol = None
        yh_vol = x.get("yh_volume")
        confirmed = (tv_vol is not None and yh_vol is not None
                     and abs(tv_vol - float(yh_vol)) < max(1, 0.001 * tv_vol))
        carry.setdefault(x["region"], {})[x["ticker"]] = {
            "last_trade": x.get("yh_local_date"),
            "confirmed": bool(confirmed),
            "close": r["close"], "change_pct": r["change_pct"],
            "volume": r["volume"], "name": r["name"]}

    # ---- final movers, excluding carry-over rows ----------------------
    movers = {}
    for fn in sorted(os.listdir(OUT)):
        if not fn.endswith(".csv"):
            continue
        region = fn[:-4]
        recs = list(csv.DictReader(open(f"{OUT}/{fn}", encoding="utf-8")))
        cset = set(carry.get(region, {}))
        rows = []
        for r in recs:
            def num(s):
                try:
                    return float(s)
                except (TypeError, ValueError):
                    return None
            close, vol = num(r["close"]), num(r["volume"])
            mcap, chg = num(r["market_cap"]), num(r["change_pct"])
            f = FX.get(r["currency"])
            rows.append({"ticker": r["ticker"], "name": r["name"],
                         "close": close, "change": chg, "volume": vol,
                         "mcap_usd": mcap * f if (mcap and f) else None,
                         "turnover": (close * vol / mcap) if (close and vol and mcap) else None,
                         "carryover": r["ticker"] in cset,
                         "sector": r["sector"], "ccy": r["currency"]})
        liq = [x for x in rows if x["change"] is not None
               and not x["carryover"]
               and (x["mcap_usd"] or 0) >= 1e9
               and (x["turnover"] or 0) >= 5e-4]
        liq.sort(key=lambda x: -x["change"])
        allm = [x for x in rows if x["change"] is not None]
        movers[region] = {
            "rows": len(rows),
            "carryover": len(cset),
            "carryover_confirmed": sum(1 for v in carry.get(region, {}).values()
                                       if v["confirmed"]),
            "with_change": len(allm),
            "up_3": sum(1 for x in allm if x["change"] >= 3),
            "dn_3": sum(1 for x in allm if x["change"] <= -3),
            "liquid_n": len(liq),
            "liquid_up_3": sum(1 for x in liq if x["change"] >= 3),
            "liquid_dn_3": sum(1 for x in liq if x["change"] <= -3),
            "top_up": liq[:5], "top_dn": liq[-5:][::-1],
            "index": index_ctx(region),
        }
        if movers[region]["index"] is None and region == "eu-gr":
            # no Yahoo index symbol for ATHEX -> equal-weight median of the
            # region's liquid names as a session proxy
            med = sorted(x["change"] for x in liq)
            movers[region]["index"] = {
                "symbol": "ATHEX (no Yahoo index symbol)",
                "close": None, "chg_pct": round(med[len(med) // 2], 4) if med else None,
                "note": "median move of the region's liquid names"}

    out = {"date": DATE, "generated_at_utc": datetime.now(timezone.utc).isoformat(),
           "fx": FX, "regions": movers,
           "carryover": {r: {t: v["last_trade"] for t, v in d.items()}
                         for r, d in carry.items()}}
    json.dump(out, open(f"{DATA}/_final.json", "w"), indent=1, default=str)

    # companion index file next to the CSVs
    with open(f"{OUT}/_carryover.json", "w", encoding="utf-8") as fh:
        json.dump({
            "_note": ("Rows whose screener close/change belong to an EARLIER "
                      "session (the instrument did not trade on 2026-10-26). "
                      "The CSV schema is fixed at 14 columns, so this index "
                      "lists them separately. last_trade = the instrument's "
                      "last Yahoo trade date; confirmed = the screener volume "
                      "matches Yahoo's volume for that session."),
            "date": DATE,
            "regions": {r: {t: {"last_trade": v["last_trade"],
                                "confirmed": v["confirmed"],
                                "close": v["close"],
                                "change_pct": v["change_pct"]}
                        for t, v in d.items()}
                        for r, d in carry.items()},
        }, fh, indent=1)

    for region in sorted(movers):
        m = movers[region]
        i = m["index"] or {}
        print(f"{region:6s} rows={m['rows']:5d} carryover={m['carryover']:5d} "
              f"liq={m['liquid_n']:4d} up3={m['up_3']:4d} dn3={m['dn_3']:4d} "
              f"liq_up3={m['liquid_up_3']:3d} liq_dn3={m['liquid_dn_3']:3d} | "
              f"{i.get('symbol')} {i.get('close')} {i.get('chg_pct')}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
