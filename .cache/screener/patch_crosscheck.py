#!/usr/bin/env python3
"""Patch crosscheck.py: fresh random seed for today's session, larger sample, and a
drift distribution summary (mean/median/max |gap| and the share of rows off by >0.5%).

The TV US feed is a ~900s delayed stream, so "TV close == Yahoo official close" is the
test that decides whether the whole sweep is measuring the settled session. The prior
cron (#20, 2026-10-27) measured a 0.43% mean gap when reading TV at 16:0x ET; this
sweep reads at ~18:40 ET, well after the delay window, so the gap should collapse.
"""
import statistics

D = "/workspace/data"
P = f"{D}/crosscheck.py"

s = open(P).read()
s = s.replace("random.seed(20261026)", "random.seed(20261027)")
s = s.replace("random.sample(stocks, 40)", "random.sample(stocks, 120)")
s = s.replace("time.sleep(0.25)", "time.sleep(0.1)")

old = '''summary = {
    "checked": len(results),
    "agree_within_0.005pct": len(ok),
    "mismatch": len(bad),
    "no_data": len(nodata),
    "yahoo_bar_dates_seen": bar_dates,
    "agreement_rate_pct": round(100 * len(ok) / max(1, len(ok) + len(bad)), 2),
    "mismatches": bad,
}'''
new = '''gaps = [abs(r["diff_pct"]) for r in results if r["diff_pct"] is not None]
signed = [r["diff_pct"] for r in results if r["diff_pct"] is not None]
summary = {
    "checked": len(results),
    "agree_within_0.005pct": len(ok),
    "mismatch": len(bad),
    "no_data": len(nodata),
    "yahoo_bar_dates_seen": bar_dates,
    "agreement_rate_pct": round(100 * len(ok) / max(1, len(ok) + len(bad)), 2),
    "gap_abs_mean_pct": round(statistics.mean(gaps), 4) if gaps else None,
    "gap_abs_median_pct": round(statistics.median(gaps), 4) if gaps else None,
    "gap_abs_max_pct": round(max(gaps), 4) if gaps else None,
    "gap_signed_mean_pct": round(statistics.mean(signed), 4) if signed else None,
    "rows_off_by_gt_0.5pct": sum(1 for g in gaps if g > 0.5),
    "rows_off_by_gt_0.1pct": sum(1 for g in gaps if g > 0.1),
    "mismatches": bad,
}'''
assert old in s
s = s.replace(old, new)
open(P, "w").write(s)
print("patched crosscheck.py (seed 20261027, sample 120, gap distribution stats)")
