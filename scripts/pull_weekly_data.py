#!/usr/bin/env python3
"""Cron #6 stock-screener-pattern-study-backlog — weekly data pulls.

Three outputs (per the cron spec + skill filters N, O, and the peoplewish
1000%-in-10-years pattern-study):

  1. IPO weekly refresh          (filter N, adapted to shibui schema)
  2. High short float refresh    (filter O, adapted to shibui schema)
  3. peoplewish 1000%-in-10y     (pattern-study backlog scan)

shibui has no `shibui.reference` table; the equivalents are:
  - IPO date        -> shibui.general_info.ipo_date
  - short % float   -> shibui.ownership_stats.short_percent_float (FRACTION, 0.20 = 20%)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shibui_mcp import bootstrap, query  # noqa: E402

DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-24"
SCRATCH = "/workspace/.scratch"
os.makedirs(SCRATCH, exist_ok=True)

PROMPT = ("weekly pattern-study backlog cron — weekly IPO, high-short-float, and "
          "peoplewish 1000%-in-10-years refresh for " + DATE)

IPO_SQL = """
SELECT g.ticker, g.symbol, g.name, g.exchange, g.ipo_date,
  ROUND(v.market_cap / 1e9, 2) AS market_cap_bil,
  g.gics_sector, g.gics_industry
FROM shibui.general_info g
LEFT JOIN (
  SELECT symbol, market_cap,
    ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY date DESC) AS rn
  FROM shibui.valuation
  WHERE date >= CURRENT_DATE - INTERVAL '7 days'
) v ON g.symbol = v.symbol AND v.rn = 1
WHERE g.ipo_date IS NOT NULL
  AND g.ipo_date >= CURRENT_DATE - INTERVAL '365 days'
  AND g.ipo_date <= CURRENT_DATE
  AND g.type = 'Common Stock'
  AND (v.market_cap > 1e9 OR v.market_cap IS NULL)
ORDER BY g.ipo_date DESC
LIMIT 50
"""

HSF_SQL = """
SELECT g.ticker, g.symbol, g.name, g.exchange, g.gics_sector,
  ROUND(o.short_percent_float * 100, 1) AS short_pct_float,
  ROUND(v.market_cap / 1e9, 2) AS market_cap_bil,
  ROUND(sq.close, 2) AS close_price,
  ROUND(adv.adv_dollar / 1e6, 1) AS adv_dollar_mil
FROM shibui.general_info g
INNER JOIN shibui.ownership_stats o ON g.symbol = o.symbol
LEFT JOIN (
  SELECT symbol, market_cap,
    ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY date DESC) AS rn
  FROM shibui.valuation
  WHERE date >= CURRENT_DATE - INTERVAL '7 days'
) v ON g.symbol = v.symbol AND v.rn = 1
LEFT JOIN (
  SELECT symbol, close,
    ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY date DESC) AS rn
  FROM shibui.stock_quotes
  WHERE date >= CURRENT_DATE - INTERVAL '7 days'
) sq ON g.symbol = sq.symbol AND sq.rn = 1
LEFT JOIN (
  SELECT symbol, AVG(close * volume) AS adv_dollar
  FROM shibui.stock_quotes
  WHERE date >= CURRENT_DATE - INTERVAL '30 days'
  GROUP BY symbol
) adv ON g.symbol = adv.symbol
WHERE o.short_percent_float > 0.20
  AND g.type = 'Common Stock'
ORDER BY o.short_percent_float DESC
LIMIT 30
"""

PATTERN_SQL = """
WITH prefilter AS (
  SELECT sq.symbol, sq.ticker, sq.close, sq.date
  FROM shibui.stock_quotes sq
  WHERE sq.date >= CURRENT_DATE - INTERVAL '10 years'
    AND sq.close > 0
),
latest AS (
  SELECT symbol, ticker, close AS current_close,
    ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY date DESC) AS rn
  FROM prefilter
),
agg AS (
  SELECT symbol, ticker,
    MIN(close) AS min_close_10y,
    MAX(close) AS max_close_10y,
    COUNT(*) AS row_count
  FROM prefilter
  GROUP BY symbol, ticker
  HAVING COUNT(*) >= 1260
)
SELECT a.symbol, a.ticker, g.name, g.exchange, g.gics_sector,
  ROUND(l.current_close, 2) AS current_close,
  ROUND(a.min_close_10y, 2) AS min_close_10y,
  ROUND(a.max_close_10y, 2) AS max_close_10y,
  ROUND((l.current_close / NULLIF(a.min_close_10y, 0) - 1) * 100, 1) AS gain_pct,
  ROUND((a.max_close_10y / NULLIF(a.min_close_10y, 0) - 1) * 100, 1) AS peak_gain_pct
FROM agg a
INNER JOIN latest l ON a.symbol = l.symbol AND l.rn = 1
LEFT JOIN shibui.general_info g ON g.symbol = a.symbol
WHERE (l.current_close / NULLIF(a.min_close_10y, 0) - 1) >= 10.0
  AND a.min_close_10y >= 0.50
  AND a.max_close_10y > 0
ORDER BY gain_pct DESC
LIMIT 200
"""

ENRICH_SQL = """
WITH universe AS (
  SELECT sq.symbol, sq.ticker, sq.close, sq.date
  FROM shibui.stock_quotes sq
  WHERE sq.date >= CURRENT_DATE - INTERVAL '10 years'
    AND sq.close > 0
),
latest AS (
  SELECT symbol, ticker, close AS current_close, date AS latest_date,
    ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY date DESC) AS rn
  FROM universe
),
agg AS (
  SELECT symbol, ticker,
    MIN(close) AS min_close_10y,
    MAX(close) AS max_close_10y
  FROM universe
  GROUP BY symbol, ticker
  HAVING COUNT(*) >= 1260
),
gainers AS (
  SELECT a.symbol, a.ticker, g.name, g.exchange, g.gics_sector, g.type AS sec_type,
    l.current_close, l.latest_date,
    a.min_close_10y, a.max_close_10y,
    (l.current_close / NULLIF(a.min_close_10y, 0) - 1) * 100 AS gain_pct,
    (a.max_close_10y / NULLIF(a.min_close_10y, 0) - 1) * 100 AS peak_gain_pct
  FROM agg a
  INNER JOIN latest l ON a.symbol = l.symbol AND l.rn = 1
  LEFT JOIN shibui.general_info g ON g.symbol = a.symbol
  WHERE (l.current_close / NULLIF(a.min_close_10y, 0) - 1) >= 10.0
    AND a.min_close_10y >= 0.50
    AND a.max_close_10y > 0
  ORDER BY gain_pct DESC
  LIMIT 100
),
recent_60d AS (
  SELECT sq.symbol,
    MAX(sq.close) AS max_high_60d,
    MIN(sq.low) AS min_low_60d,
    AVG((sq.high - sq.low) / NULLIF(sq.close, 0)) AS avg_range_60d
  FROM shibui.stock_quotes sq
  INNER JOIN gainers g ON sq.symbol = g.symbol
  WHERE sq.date >= CURRENT_DATE - INTERVAL '60 days'
  GROUP BY sq.symbol
),
recent_10d AS (
  SELECT sq.symbol,
    AVG((sq.high - sq.low) / NULLIF(sq.close, 0)) AS avg_range_10d,
    MAX(sq.high) AS max_high_10d,
    MIN(sq.low) AS min_low_10d
  FROM shibui.stock_quotes sq
  INNER JOIN gainers g ON sq.symbol = g.symbol
  WHERE sq.date >= CURRENT_DATE - INTERVAL '10 days'
  GROUP BY sq.symbol
),
ytd AS (
  SELECT sq.symbol, MIN(sq.low) AS ytd_low
  FROM shibui.stock_quotes sq
  INNER JOIN gainers g ON sq.symbol = g.symbol
  WHERE sq.date >= DATE_TRUNC('year', CURRENT_DATE)
  GROUP BY sq.symbol
),
latest_px AS (
  SELECT symbol, close, high, low, prev_close FROM (
    SELECT sq.symbol, sq.close, sq.high, sq.low,
      LAG(sq.close) OVER (PARTITION BY sq.symbol ORDER BY sq.date) AS prev_close,
      ROW_NUMBER() OVER (PARTITION BY sq.symbol ORDER BY sq.date DESC) AS rn
    FROM shibui.stock_quotes sq
    INNER JOIN gainers g ON sq.symbol = g.symbol
    WHERE sq.date >= CURRENT_DATE - INTERVAL '5 days'
  ) WHERE rn = 1
)
SELECT ga.ticker, ga.name, ga.exchange, ga.gics_sector, ga.sec_type,
  ga.current_close, ga.min_close_10y, ga.max_close_10y,
  ROUND(ga.gain_pct, 1) AS gain_pct,
  ROUND(ga.peak_gain_pct, 1) AS peak_gain_pct,
  ROUND(r60.max_high_60d, 2) AS high_60d,
  ROUND(r60.min_low_60d, 2) AS low_60d,
  ROUND(r10.max_high_10d, 2) AS high_10d,
  ROUND(r10.min_low_10d, 2) AS low_10d,
  ROUND(r10.avg_range_10d / NULLIF(r60.avg_range_60d, 0), 2) AS contraction_ratio,
  ROUND(y.ytd_low, 2) AS ytd_low,
  ROUND(lp.close, 2) AS last_close,
  ROUND((lp.close - lp.prev_close) / NULLIF(lp.prev_close, 0) * 100, 2) AS last_day_change_pct
FROM gainers ga
LEFT JOIN recent_60d r60 ON ga.symbol = r60.symbol
LEFT JOIN recent_10d r10 ON ga.symbol = r10.symbol
LEFT JOIN ytd y ON ga.symbol = y.symbol
LEFT JOIN latest_px lp ON ga.symbol = lp.symbol
ORDER BY ga.gain_pct DESC
LIMIT 100
"""


def main():
    if not bootstrap():
        print("BOOTSTRAP FAILED", file=sys.stderr)
        return 1
    failures = 0
    for label, sql, fname, pid in [
        ("ipo", IPO_SQL, "ipo.json", 11),
        ("hsf", HSF_SQL, "hsf.json", 12),
        ("pattern_full", PATTERN_SQL, "pattern_full.json", 13),
        ("pattern_enriched", ENRICH_SQL, "pattern_enriched.json", 14),
    ]:
        rows = query(sql, PROMPT + " [" + label + "]", pid)
        if not rows:
            failures += 1
            print(f"EMPTY RESULT for {label}", file=sys.stderr)
        with open(f"{SCRATCH}/{fname}", "w") as f:
            json.dump(rows, f, indent=2)
        print(f"{label}: {len(rows)} rows")
    print(f"MCP_FAILURES={failures}")
    return failures


if __name__ == "__main__":
    sys.exit(main())
