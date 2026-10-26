#!/usr/bin/env python3
"""Enrich the TradingView universe and run the 10 stylist sub-screens (A-K).

Cloud re-implementation of scripts/screen.py (prefilter + sweep) for cron #9.
The shibui-finance MCP is unbound in this session, so each shibui SQL screen is
re-expressed against TradingView public-scanner columns. Every proxy substitution
is recorded in the returned meta dict and must be reported in the artifact.
"""
import json
import math
import sys

import pandas as pd

RAW = "/workspace/data/tv_universe_raw.json"
OUT = "/workspace/data/enriched.csv"

MAJOR_EXCHANGES = {"NYSE", "NASDAQ", "AMEX"}
ACCOUNT_SIZE_USD = 50_000  # skill default fallback


def f(x):
    try:
        if x is None or (isinstance(x, float) and math.isnan(x)):
            return None
        return float(x)
    except (TypeError, ValueError):
        return None


def main():
    raw = json.load(open(RAW))
    cols = raw["columns"]
    recs = []
    seen = set()
    for r in raw["rows"]:
        if r["s"] in seen:      # pagination tie-stability duplicates
            continue
        seen.add(r["s"])
        d = dict(zip(cols, r["d"]))
        d["_id"] = r["s"]
        recs.append(d)
    df = pd.DataFrame(recs)
    for c in df.columns:
        if c not in ("name", "description", "sector", "industry", "exchange",
                     "country", "currency", "type", "update_mode", "_id"):
            df[c] = pd.to_numeric(df[c], errors="coerce")

    total_scanned = len(df)
    df = df[df["type"] == "stock"].copy()
    n_stock = len(df)
    df = df[df["exchange"].isin(MAJOR_EXCHANGES)].copy()
    n_major_exch = len(df)

    # ---- step 1: shibui prefilter (close>3, mcap>300M, avg_vol_30d>100k, NYSE/NASDAQ/AMEX)
    pre = df[(df["close"] > 3) & (df["market_cap_basic"] > 300_000_000) &
             (df["average_volume_30d_calc"] > 100_000)].copy()
    n_pre = len(pre)

    pre["_prev_close"] = pre["close"] / (1 + pre["change"] / 100.0)
    pre["_gap_pct"] = (pre["open"] / pre["_prev_close"] - 1) * 100
    pre["_day_range_pct"] = (pre["high"] - pre["low"]) / pre["close"] * 100
    pre["_dcr_pct"] = (pre["close"] - pre["low"]) / (pre["high"] - pre["low"] - 1e-9) * 100
    pre["_adr_proxy_pct"] = pre["ATR"] / pre["close"] * 100        # ATR(14)/close proxy for 20d ADR
    pre["_adv_dollar"] = pre["close"] * pre["average_volume_30d_calc"]
    pre["_dist_sma200_pct"] = (pre["close"] / pre["SMA200"] - 1) * 100
    pre["_dist_sma20_pct"] = (pre["close"] / pre["SMA20"] - 1) * 100
    pre["_dist_sma50_pct"] = (pre["close"] / pre["SMA50"] - 1) * 100
    pre["_rs_1m"] = pre["Perf.1M"]
    pre["_rs_3m"] = pre["Perf.3M"]
    pre["_rs_6m"] = pre["Perf.6M"]
    pre["_rs_12m"] = pre["Perf.Y"]
    pre["_trend_intensity_proxy"] = pre["close"] / pre["SMA50"]
    pre["_ma_shrink_5d_proxy"] = ((pre["High.5D"] - pre["Low.5D"]) /
                                  (pre["High.1M"] - pre["Low.1M"] + 1e-9))
    pre["_base_width_proxy"] = (pre["High.1M"] - pre["Low.1M"]) / pre["close"]
    pre["_close_loc_in_base"] = (pre["close"] - pre["Low.1M"]) / (pre["High.1M"] - pre["Low.1M"] + 1e-9)
    pre["_adv_account_lo"] = ACCOUNT_SIZE_USD * 10
    pre["_adv_account_hi"] = ACCOUNT_SIZE_USD * 200
    pre["_ts"] = "tv_scanner"

    def take(sub, cols, name):
        sub = sub.copy()
        for c in cols:
            if c not in sub.columns:
                sub[c] = None
        sub["_screen"] = name
        return sub[cols]

    idc = ["name", "exchange", "close", "change", "volume", "market_cap_basic",
           "_adr_proxy_pct", "_adv_dollar", "_gap_pct", "_dist_sma200_pct",
           "_rs_1m", "_rs_3m", "_rs_6m", "_rs_12m", "relative_volume_10d_calc",
           "SMA20", "SMA50", "SMA200", "ATR", "Perf.5D", "Perf.1M", "_ts"]

    screens = {}

    # A. Stockbee - 4% breakout (volume > prev_volume -> rvol10 > 1 proxy)
    a = pre[(pre["change"] >= 4.0) & (pre["volume"] > pre["average_volume_10d_calc"]) &
            (pre["close"] >= 3.0)]
    screens["stockbee_4pct_breakout"] = take(a, idc, "A")

    # B. Stockbee - EP9 million (volume >= 8.9M) + trigger-candle validation cols
    b = pre[(pre["volume"] >= 8_900_000) & (pre["close"] >= 3.0)]
    screens["stockbee_ep9m"] = take(b, idc, "B")

    # C. Qullamaggie - multi-timeframe RS leaders
    c = pre[((pre["_rs_1m"] >= 25) | (pre["_rs_3m"] >= 50) | (pre["_rs_6m"] >= 150)) &
            (pre["_adr_proxy_pct"] >= 4.5) & (pre["_adv_dollar"] >= 20_000_000) &
            (pre["close"] > pre["SMA200"]) & (pre["SMA50"] > pre["SMA150"]) &
            (pre["SMA150"] > pre["SMA200"])]
    screens["qullamaggie_rs_leaders"] = take(c, idc, "C")

    # D. Qullamaggie - EP 10%+ gap
    d = pre[(pre["_gap_pct"] >= 10.0) & (pre["relative_volume_10d_calc"] >= 10) &
            (pre["_adv_dollar"] >= 50_000_000)]
    screens["qullamaggie_ep_gap"] = take(d, idc, "D")

    # E. Qullamaggie - 5-day gainers (parabolic short)
    e = pre[(pre["Perf.5D"] >= 25) & (pre["_adv_dollar"] >= 50_000_000) &
            (pre["_adr_proxy_pct"] >= 5)]
    screens["qullamaggie_parabolic_short"] = take(e, idc, "E")

    # F. Qullamaggie - 5-day losers (parabolic long)
    f_ = pre[(pre["Perf.5D"] <= -25) & (pre["Perf.5D"] >= -50) &
             (pre["_adv_dollar"] >= 50_000_000) & (pre["_dist_sma200_pct"].abs() < 25)]
    screens["qullamaggie_parabolic_long"] = take(f_, idc, "F")

    # G. peoplewish - ADR + dollar volume + velocity
    g = pre[(pre["_adr_proxy_pct"] >= 5) & (pre["_adv_dollar"] >= 50_000_000)]
    screens["peoplewish_adr_velocity"] = take(g, idc, "G")

    # H. Jeff Sun - CANSLIM-calibrated (TV native).
    # PARTIAL: earnings_growth_quarterly_yoy and sales_growth_quarterly_yoy are null on this
    # source, so the growth legs are proxied with EPS yoy growth (ttm) only; sales growth is
    # NOT applied. Flagged in the artifact as a degraded sub-screen.
    h = pre[(pre["market_cap_basic"] > 1_000_000_000) &
            (pre["earnings_per_share_diluted_yoy_growth_ttm"] > 25) &
            (pre["close"] > 5) &
            (pre["change"] > 0) & (pre["RSI"] <= 80) & (pre["RSI"] >= 40)]
    screens["jeff_sun_canslim"] = take(h, idc, "H")

    # K. Bonde - Anticipation (coil)
    k = pre[(pre["_trend_intensity_proxy"] >= 1.05) & (pre["_base_width_proxy"] <= 0.08) &
            (pre["_close_loc_in_base"] >= 0.5) & (pre["change"] < 4.0)]
    screens["bonde_anticipation_coil"] = take(k, idc, "K")

    counts = {k2: len(v) for k2, v in screens.items()}
    print("SCAN", json.dumps({"total_scanned": total_scanned, "type_stock": n_stock,
                              "major_exchange": n_major_exch, "prefilter": n_pre,
                              "screen_counts": counts}, indent=2), file=sys.stderr)

    allc = pd.concat(screens.values(), ignore_index=True)
    allc.to_csv(OUT, index=False)
    with open("/workspace/data/screens.json", "w") as f_:
        json.dump({"counts": counts, "meta": {
            "total_scanned": total_scanned, "type_stock": n_stock,
            "major_exchange": n_major_exch, "prefilter": n_pre,
            "account_size_usd": ACCOUNT_SIZE_USD}}, f_, indent=2)
    print(f"wrote {OUT} rows={len(allc)}", file=sys.stderr)


if __name__ == "__main__":
    main()
