"""Command-line entry points for staged, offline SIP workflows."""
from __future__ import annotations

import argparse
import json
import sys

from .change_chat import ChatError, compare_snapshots
from .outcomes import MAX_QUOTE_AGE_SECONDS, OutcomeError, ingest


def _read(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m sip.staged_cli")
    commands = parser.add_subparsers(dest="command", required=True)
    outcome = commands.add_parser("outcomes")
    outcome.add_argument("--input", required=True)
    outcome.add_argument("--state-dir", required=True)
    outcome.add_argument(
        "--retention",
        required=True,
        type=float,
        help="gap retention threshold",
    )
    outcome.add_argument(
        "--max-quote-age-seconds",
        type=float,
        default=MAX_QUOTE_AGE_SECONDS,
    )
    chat = commands.add_parser("midday")
    chat.add_argument("--open")
    chat.add_argument("--midday", required=True)
    chat.add_argument(
        "--retention",
        required=True,
        type=float,
        help="gap retention threshold",
    )
    chat.add_argument(
        "--max-open-age-hours",
        type=float,
        default=6.0,
    )
    args = parser.parse_args(argv)
    try:
        if args.command == "outcomes":
            result = ingest(
                _read(args.input),
                args.state_dir,
                args.retention,
                args.max_quote_age_seconds,
            )
            print(
                json.dumps(
                    {
                        "flags": len(result["flags"]),
                        "observations": len(result["observations"]),
                        "status": "ok",
                    },
                    sort_keys=True,
                )
            )
        else:
            opening = _read(args.open) if args.open else None
            print(
                compare_snapshots(
                    opening,
                    _read(args.midday),
                    args.retention,
                    args.max_open_age_hours,
                )
            )
        return 0
    except (
        OSError,
        ValueError,
        json.JSONDecodeError,
        OutcomeError,
        ChatError,
    ) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
