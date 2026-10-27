#!/usr/bin/env python3
"""movers_final.py — cron #5 headline movers + session context.

Mover selection (no name/symbol heuristics: the screener's `type=stock`
universe contains genuine secondary listings and ISIN-style symbols, and a
symbol-shape filter was shown to delete real securities — e.g. LSX:121806
Heliad AG, LSX:A11Q13 H&K AG). Liquidity is applied instead:

  mcap_usd   >= 1e9            (approximate, FX-converted)
  turnover   = close*volume/mcap >= 5e-4   (0.05% of the company traded)

Session context: the regional index level and % move from Yahoo, with
today's close taken from meta.regularMarketPrice (index bar-lag rule) and
the prior close from the last populated daily bar.
"""
from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
from datetime import datetime, timezone, timedelta

CA = "/etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt"
UA = "Mozilla/5.0"
DATE = os.environ.get("EOD_DATE", "2026-10-27")
OUT = f"/workspace/international-eod/{DATE}"
DATA = "/workspace/data"
FX = {"EUR": 1.1130, "JPY": 0.0063312, "AUD": 0.7026913,
      "CAD": 0.7117944, "DKK": 0.1488804, "TWD": 0.0308604}
INDEX = {"au": "^AXJO", "jp": "^N225", "tw": "^TWII", "ca": "^GSPTSE",
         "eu-de": "^GDAXI", "eu-fr": "^FCHI", "eu-it": "FTSEMIB", "eu-es": "^IBEX",
         "eu-nl": "^AEX", "eu-be": "^BFX", "eu-at": "^ATX", "eu-pt": "^PSI20",
         "eu-ie": "^ISEQ", "eu-fi": "^OMXH25", "eu-dk": "^OMXC20",
         "eu-gr": "^ATHEX"}


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


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


def index_ctx(sym):
    d = yahoo(sym)
    if not d:
        return None
    meta, bars = d["meta"], d["bars"]
    price = meta.get("regularMarketPrice")
    chg = meta.get("regularMarketChangePercent")
    prior = bars[-1][1] if bars else None
    if prior and price:
        chg_calc = (price - prior) / prior * 100
    else:
        chg_calc = None
    t = meta.get("regularMarketTime")
    local = (datetime.fromtimestamp(t, timezone.utc).isoformat() if t else None)
    return {"symbol": sym, "close": price, "chg_meta": chg,
            "chg_from_last_bar": round(chg_calc, 4) if chg_calc is not None else None,
            "prior_bar_close": prior, "last_bar_utc": local,
            "currency": meta.get("currency"),
            "exchange": meta.get("fullExchangeName")}


def main() -> int:
    out = {}
    for region in sorted(INDEX):
        path = f"{OUT}/{region}.csv"
        if not os.path.exists(path):
            continue
        rows = list(csv.DictReader(open(path, encoding="utf-8")))
        recs = []
        for r in rows:
            close, vol = num(r["close"]), num(r["volume"])
            mcap, chg = num(r["market_cap"]), num(r["change_pct"])
            f = FX.get(r["currency"])
            mcap_usd = mcap * f if (mcap and f) else None
            turn = (close * vol / mcap) if (close and vol and mcap) else None
            recs.append({"ticker": r["ticker"], "name": r["name"],
                         "close": close, "change": chg, "volume": vol,
                         "mcap": mcap, "mcap_usd": mcap_usd, "turnover": turn,
                         "ccy": r["currency"], "sector": r["sector"]})
        liquid = [x for x in recs if x["change"] is not None
                  and (x["mcap_usd"] or 0) >= 1e9
                  and (x["turnover"] or 0) >= 5e-4]
        liquid.sort(key=lambda x: -x["change"])
        allm = [x for x in recs if x["change"] is not None]
        out[region] = {
            "rows": len(rows),
            "with_change": len(allm),
            "up_3": sum(1 for x in allm if x["change"] >= 3),
            "dn_3": sum(1 for x in allm if x["change"] <= -3),
            "liquid_n": len(liquid),
            "liquid_up_3": sum(1 for x in liquid if x["change"] >= 3),
            "liquid_dn_3": sum(1 for x in liquid if x["change"] <= -3),
            "top_up": liquid[:5], "top_dn": liquid[-5:][::-1],
            "index": index_ctx(INDEX[region]),
        }
        i = out[region]["index"]
        print(f"{region:6s} rows={len(rows):5d} liq={len(liquid):4d} "
              f"up3={out[region]['up_3']:4d} dn3={out[region]['dn_3']:4d} "
              f"liq_up3={out[region]['liquid_up_3']:3d} liq_dn3={out[region]['liquid_dn_3']:3d} "
              f"| idx {i['symbol'] if i else '-'} "
              f"{i['close'] if i else '-'} {i['chg_meta'] if i else '-'}%")
        for x in out[region]["top_up"][:3]:
            print(f"        UP   {x['ticker']:16s} {x['change']:+7.2f}%  "
                  f"mcap~${(x['mcap_usd'] or 0)/1e9:.1f}bn {x['name'][:38]}")
        for x in out[region]["top_dn"][:3]:
            print(f"        DOWN {x['ticker']:16s} {x['change']:+7.2f}%  "
                  f"mcap~${(x['mcap_usd'] or 0)/1e9:.1f}bn {x['name'][:38]}")
    json.dump({"date": DATE, "fx": FX, "regions": out},
              open(f"{DATA}/_movers_final.json", "w"), indent=1, default=str)
    return 0


if __name__ == "__main__":
    sys.exit(main())
