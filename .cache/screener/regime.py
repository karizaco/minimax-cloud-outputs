#!/usr/bin/env python3
"""Breadth + regime layer for cron #9 (Cloud).

Breadth  : % of S&P 500 constituents above their 20-DMA, as of the settled session.
Regime   : size_cut_pct / uncertainty / late_cycle, per the skill's regime.json contract.
Sector RS: Hernandez theme->group funnel (top-3 sector ETFs by Perf.1M+3M+6M composite).

All inputs are local caches produced earlier in this run:
  data/tv_universe_raw.json (TradingView scanner, 20,095 rows)
  data/yahoo_bars.json     (Yahoo daily bars, short UA + curl)
  data/sp500_tickers.json  (Wikipedia constituent list)
"""
import json
import os
import statistics
import sys
from datetime import datetime, timezone

sys.path.insert(0, "/workspace/data")
from yahoo_enrich import atr14  # noqa: E402

SESSION = os.environ.get("SCREENER_SESSION", "2026-10-27")  # overridable by the runner


def load_tv():
    raw = json.load(open("/workspace/data/tv_universe_raw.json"))
    cols = raw["columns"]
    idx = {c: i for i, c in enumerate(cols)}
    out = {}
    for r in raw["rows"]:
        d = r["d"]
        out.setdefault(d[idx["name"]], []).append({
            "id": r["s"], "type": d[idx["type"]], "exchange": d[idx["exchange"]],
            "close": d[idx["close"]], "change": d[idx["change"]],
            "sma20": d[idx["SMA20"]], "sma50": d[idx["SMA50"]], "sma200": d[idx["SMA200"]],
            "atr": d[idx["ATR"]], "p1m": d[idx["Perf.1M"]], "p3m": d[idx["Perf.3M"]],
            "p6m": d[idx["Perf.6M"]], "py": d[idx["Perf.Y"]],
            "sector": d[idx["sector"]], "industry": d[idx["industry"]],
            "mcap": d[idx["market_cap_basic"]], "pe": d[idx["price_earnings_ttm"]],
            "eps_growth": d[idx["earnings_per_share_diluted_yoy_growth_ttm"]],
            "vol": d[idx["volume"]], "avgv30": d[idx["average_volume_30d_calc"]],
            "rvol10": d[idx["relative_volume_10d_calc"]],
            "high5": d[idx["High.5D"]], "low5": d[idx["Low.5D"]],
            "high1m": d[idx["High.1M"]], "low1m": d[idx["Low.1M"]],
        })
    return out


def main():
    tv = load_tv()
    bars = json.load(open("/workspace/data/yahoo_bars.json"))
    sp500 = json.load(open("/workspace/data/sp500_tickers.json"))

    # ---------- breadth ----------
    above = below = nodata = 0
    missing = []
    for t in sp500:
        rows = [r for r in tv.get(t, []) if r["type"] == "stock"]
        if not rows:
            rows = tv.get(t, [])
        r = rows[0] if rows else None
        if r and r["sma20"] and r["close"]:
            if r["close"] > r["sma20"]:
                above += 1
            else:
                below += 1
        else:
            nodata += 1
            missing.append(t)
    breadth_pct = round(100 * above / max(1, above + below), 2)
    print(f"BREADTH above20dma={above} below={below} nodata={nodata} pct={breadth_pct}")

    # breadth cross-check on a Yahoo sample (true SMA20 from bars)
    import random
    random.seed(7)
    sample = [t for t in sp500 if t in bars and bars[t].get("bars")][:0]
    pool = [t for t in sp500 if t in bars and bars[t].get("bars")]
    sample = random.sample(pool, min(40, len(pool)))
    agree = tot = 0
    for t in sample:
        b = bars[t]["bars"]
        if len(b) < 20:
            continue
        closes = [x[4] for x in b]
        y_sma20 = sum(closes[-20:]) / 20
        y_above = closes[-1] > y_sma20
        rows = [r for r in tv.get(t, []) if r["type"] == "stock"] or tv.get(t, [])
        if not rows or not rows[0]["sma20"]:
            continue
        tv_above = rows[0]["close"] > rows[0]["sma20"]
        tot += 1
        agree += (y_above == tv_above)
    print(f"BREADTH_XCHECK agree={agree}/{tot}")

    # ---------- index ATR extension ----------
    index_rows = []
    for sym in ("SPY", "RSP", "QQQ", "QQQE", "IWM"):
        d = bars.get(sym, {})
        bl = d.get("bars", [])
        if not bl:
            index_rows.append({"symbol": sym, "error": d.get("error", "no bars")})
            continue
        closes = [b[4] for b in bl]
        a14, _ = atr14(bl)
        # median of the ATR% SERIES (not of rolling ATR), per prior-run bug note
        trs = []
        for i in range(1, len(bl)):
            h, l, pc = bl[i][2], bl[i][3], bl[i - 1][4]
            trs.append(max(h - l, abs(h - pc), abs(l - pc)))
        atr_series = [sum(trs[max(0, i - 13):i + 1]) / min(14, i + 1) / closes[i + 1] * 100
                      for i in range(len(trs)) if i + 1 < len(closes)]
        med = statistics.median(atr_series[-252:]) if len(atr_series) >= 30 else None
        atr_pct = a14 / closes[-1] * 100 if a14 else None
        ext = (atr_pct / med) if (atr_pct and med) else None
        index_rows.append({
            "symbol": sym, "close": closes[-1], "sma50": sum(closes[-50:]) / 50,
            "atr_pct": atr_pct, "median_atr_pct_252": med, "extension_x": ext,
            "bars": len(bl), "last_bar_utc": datetime.fromtimestamp(
                bl[-1][0], tz=timezone.utc).strftime("%Y-%m-%d"),
        })
    for r in index_rows:
        print("INDEX", json.dumps(r))

    # ---------- VIX / VXV ----------
    def yq(sym):
        d = bars.get(sym, {})
        bl = d.get("bars", [])
        if not bl:
            return {"symbol": sym, "error": d.get("error", "no bars"), "price": None}
        closes = [b[4] for b in bl]
        return {"symbol": sym, "price": closes[-1], "prev": closes[-2] if len(closes) > 1 else None,
                "change_pct": (closes[-1] / closes[-2] - 1) * 100 if len(closes) > 1 else None,
                "last_bar_utc": datetime.fromtimestamp(bl[-1][0], tz=timezone.utc).strftime("%Y-%m-%d")}
    vix = yq("^VIX")
    vxv = yq("^VXV")
    print("VIX", json.dumps(vix), "VXV", json.dumps(vxv))

    # ---------- sector ETF RS (Hernandez) ----------
    sector_etfs = {"XLB": "Basic Materials", "XLC": "Communication Services",
                    "XLE": "Energy", "XLF": "Financial", "XLI": "Industrial",
                    "XLK": "Electronic Technology", "XLP": "Consumer Defensive",
                    "XLRE": "Real Estate", "XLU": "Utilities", "XLV": "Healthcare",
                    "XLY": "Consumer Cyclical"}
    etf_rs = []
    for t, sec in sector_etfs.items():
        rows = [r for r in tv.get(t, []) if r["type"] == "fund"] or tv.get(t, [])
        if not rows:
            etf_rs.append({"etf": t, "sector": sec, "error": "not in scanner universe"})
            continue
        r = rows[0]
        comp = (r["p1m"] or 0) + (r["p3m"] or 0) + (r["p6m"] or 0)
        etf_rs.append({"etf": t, "sector": sec, "close": r["close"], "perf_1m": r["p1m"],
                       "perf_3m": r["p3m"], "perf_6m": r["p6m"], "perf_y": r["py"],
                       "composite": round(comp, 3), "above_sma20": bool(r["sma20"] and r["close"] > r["sma20"])})
    etf_rs.sort(key=lambda x: (x.get("composite") is None, -(x.get("composite") or 0)))
    for e in etf_rs:
        print("ETF_RS", json.dumps(e))

    out = {
        "session": SESSION,
        "breadth": {"sp500_members": len(sp500), "above_20dma": above, "below_20dma": below,
                    "no_data": nodata, "pct_above_20dma": breadth_pct,
                    "missing": missing, "yahoo_crosscheck": {"agree": agree, "of": tot}},
        "index_atr": index_rows,
        "vix": vix, "vxv": vxv,
        "sector_etf_rs": etf_rs,
        "sector_etf_source": "TradingView scanner (Perf.1M/3M/6M) -- MCP ETF screener unbound",
    }
    json.dump(out, open("/workspace/data/regime_raw.json", "w"), indent=1)
    print("wrote /workspace/data/regime_raw.json")


if __name__ == "__main__":
    main()
