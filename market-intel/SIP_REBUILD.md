# SIP rebuild — shared core + Taiwan pilot (shadow only)

## Goal
New Python package under `sip/` (runnable from `/workspace/market-intel/sip` and mirrored to GitHub `karizaco/minimax-cloud-outputs` path `market-intel/sip/`).

DO NOT modify existing routines, skills, or live digest paths under `/home/box/taiwan-in-play/*.md` (except writing NEW files under `/home/box/taiwan-in-play/shadow/`).

## Package layout
```
sip/
  __init__.py
  schema.py
  config/
    __init__.py
    taiwan.yaml
    defaults.yaml
  tier.py
  midday.py
  overnight.py
  number_trace.py
  templates/
    prompts/
      digest_system.txt
      chat_system.txt
  format_taiwan.py
  draft_mmx.py
  markets/
    taiwan/
      __init__.py
      fetch.py
      parse.py
      adapter.py
      names.py
  shadow.py
  compare.py
  cli.py
  EXIT_CODES.md
tests/
  fixtures/taiwan-2026-11-05-open/
  test_schema.py
  test_tier_taiwan.py
  test_number_trace.py
  test_parse_taiwan.py
  test_compare.py
  test_shadow_paths.py
requirements-sip.txt
README.md
```

## Candidate row schema (required)
ticker, venue (TWSE|TPEx), instrument_type (common|etf|warrant|pref|emerging|tdr|fund_wrapper|other),
last, chg_pct, dollar_vol (TWD session turnover), rvol (nullable float),
catalyst (str|null), catalyst_time (ISO|null), flags (list[str]),
source (str), asof (ISO), tier (A|Soft-A|TECH_WATCH|B|C|null before assign).
Optional: company_en, company_zh, board, mcap_twd, usd_turnover, display_ticker, why.

## Taiwan floors (open) — taiwan.yaml
- price >= 5 NTD hard
- turnover >= 30e6 TWD open / 100e6 midday
- mcap >= 1e9 TWD OR turnover floor
- Soft-A REQUIRES concrete non-empty catalyst
- TECH_WATCH: floors + soft move/gap + soft RVol ~1-2x + no same-session catalyst
- Within-tier sort: dollar_vol TWD desc
- Drop ETF/warrant/pref/emerging/TDR/fund_wrapper from promotion
- FUND_WRAPPER never chat tiers
- BUYOUT_NEAR max 2 chat appearances unless new deal event
- STALE_HALT >~5 sessions annex only
- overnight_carry + midday delta vs open file

## Number-trace checker
Input: run JSON + chat markdown. Every number in chat must match a run JSON value within rounding tolerance. Fail with list of offenders. New module `sip/number_trace.py`. Do not edit check_runs.py.

## Taiwan chat format
- Tier name above each table
- A/Soft-A: Ticker | Company | Move | RelVol | Turnover | Catalyst
- Other: Ticker | Company | Move | RelVol | Turnover
- US$ only, no tilde; bare TWSE; XXXX.TPEX for TPEx
- Skipped line last only if skipped
- Digest has Source health table

## Taiwan adapter
HTTP: Yahoo TW ranks, CMoney, MOPS, TWSE MIS/MI_INDEX, TPEx, rosters, FX.
Accept --tv-dump JSON from Grok (never hit scanner.tradingview.com).
Parsers fail loud into Source health (never silent empty ok).
--fixtures DIR for offline tests.

## Shadow CLI
python -m sip.cli shadow --market taiwan --slot open --date YYYY-MM-DD --fixtures DIR [--tv-dump PATH] --out-root /home/box/taiwan-in-play/shadow
Writes ONLY shadow/YYYY-MM-DD-slot.{json,md,chat.md}

## Compare CLI
python -m sip.cli compare --shadow PATH.md --live PATH.md
Report tier/ticker/why diffs.

## Exit codes
0 ok; 2 usage; 3 mmx quota; 4 mmx rate limit; 5 number-trace/draft fail; 6 all primary fetches dead.

## Codegen rules
Python 3.11+, stdlib+pyyaml; urllib. Think briefly. Emit complete files with path headers like:
### FILE: sip/schema.py
<code>
Do not invent network calls to TradingView scanner.
