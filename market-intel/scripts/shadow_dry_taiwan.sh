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

if [[ -x "/home/box/venvs/sip/bin/python" ]]; then
    PYTHON="/home/box/venvs/sip/bin/python"
elif [[ -x "$ROOT/.venv/bin/python" ]]; then
    PYTHON="$ROOT/.venv/bin/python"
else
    printf 'SIP runtime missing: expected /home/box/venvs/sip/bin/python or %s/.venv/bin/python\n' \
        "$ROOT" >&2
    exit 2
fi

if ! "$PYTHON" -c 'import yaml' >/dev/null 2>&1; then
    printf 'SIP runtime missing required yaml import: %s\n' "$PYTHON" >&2
    exit 2
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
