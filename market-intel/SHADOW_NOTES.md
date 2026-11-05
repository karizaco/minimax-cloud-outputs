# SIP shadow notes (Taiwan pilot)

- Live digests and routines are untouched. Shadow writes only under `/home/box/taiwan-in-play/shadow/`.
- Tests: `cd market-intel && PYTHONPATH=. pytest tests/ -q` (needs pyyaml, pytest).
- Shadow dry-run: `scripts/shadow_dry_taiwan.sh` or `python -m sip.cli shadow --market taiwan --slot open --date 2026-11-05 --fixtures tests/fixtures/taiwan-2026-11-05-open --out-root /home/box/taiwan-in-play/shadow`
- Compare: `python -m sip.cli compare --shadow .../YYYY-MM-DD-open.md --live /home/box/taiwan-in-play/YYYY-MM-DD-open.md`
- TradingView: pass `--tv-dump` JSON from Grok MCP; never call scanner.tradingview.com from scripts.
- Known gaps vs live 2026-11-05 open (for Developer): catalyst attach/MOPS→Soft-A/A still weak; chat missing Company/Catalyst columns and `.TPEX` suffix; compare headings (`###` vs `##`); digest is a flat Movers table not full locked digest layout. Tier engine + number_trace + shadow path isolation are covered by tests.
