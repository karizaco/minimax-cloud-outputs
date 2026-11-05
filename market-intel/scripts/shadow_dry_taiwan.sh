#!/usr/bin/env bash
set -euo pipefail

ROOT="/workspace/market-intel"
export PYTHONPATH="/workspace/market-intel${PYTHONPATH:+:$PYTHONPATH}"

FIXTURES="${FIXTURES:-$ROOT/tests/fixtures/taiwan-2026-11-05-open}"
OUT_ROOT="${OUT_ROOT:-/home/box/taiwan-in-play/shadow}"
DATE="${DATE:-$(TZ=Asia/Taipei date +%F)}"
SLOT="${SLOT:-open}"
LIVE_DIGEST="${LIVE_DIGEST:-/home/box/taiwan-in-play/$DATE-$SLOT.md}"

if [[ -x "/workspace/sip-rebuild/.venv/bin/python" ]]; then
    PYTHON="/workspace/sip-rebuild/.venv/bin/python"
elif [[ -x "$ROOT/.venv/bin/python" ]]; then
    PYTHON="$ROOT/.venv/bin/python"
elif [[ -x "$ROOT/venv/bin/python" ]]; then
    PYTHON="$ROOT/venv/bin/python"
else
    PYTHON="python3"
fi

mkdir -p "$OUT_ROOT"

"$PYTHON" -m sip.cli shadow \
    --market taiwan \
    --slot "$SLOT" \
    --date "$DATE" \
    --fixtures "$FIXTURES" \
    --out-root "$OUT_ROOT"

if [[ -f "$LIVE_DIGEST" ]]; then
    "$PYTHON" -m sip.cli compare \
        --shadow "$OUT_ROOT/$DATE-$SLOT.md" \
        --live "$LIVE_DIGEST"
else
    printf 'live digest not found: %s\n' "$LIVE_DIGEST" >&2
fi
