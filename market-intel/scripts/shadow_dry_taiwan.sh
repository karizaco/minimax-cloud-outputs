#!/usr/bin/env bash
set -euo pipefail

ROOT="${ROOT:-/workspace/market-intel}"
export PYTHONPATH="$ROOT${PYTHONPATH:+:$PYTHONPATH}"

FIXTURES="${FIXTURES:-$ROOT/tests/fixtures/taiwan-2026-11-05-open}"
OUT_ROOT="${OUT_ROOT:-/home/box/taiwan-in-play/shadow}"
SLOT="${SLOT:-open}"

if [[ -z "${DATE:-}" ]]; then
    if [[ "$(basename "$FIXTURES")" =~ taiwan-([0-9]{4}-[0-9]{2}-[0-9]{2})- ]]; then
        DATE="${BASH_REMATCH[1]}"
    else
        printf 'DATE is required when it cannot be derived from FIXTURES (%s)\n' \
            "$FIXTURES" >&2
        exit 2
    fi
fi

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
