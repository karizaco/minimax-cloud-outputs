from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def _load_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="sip")
    sub = parser.add_subparsers(dest="command", required=True)

    shadow = sub.add_parser("shadow")
    shadow.add_argument("--market", required=True)
    shadow.add_argument("--slot", required=True)
    shadow.add_argument("--date", required=True)
    shadow.add_argument("--fixtures", required=True)
    shadow.add_argument("--out-root", default="/home/box/taiwan-in-play/shadow")
    shadow.add_argument("--tv-dump")
    shadow.add_argument("--require-mmx-chat", action="store_true")

    compare = sub.add_parser("compare")
    compare.add_argument("--shadow", required=True)
    compare.add_argument("--live", required=True)
    compare.add_argument("--json-out")

    check = sub.add_parser("check-numbers")
    check.add_argument("--run", required=True)
    check.add_argument("--chat", required=True)
    check.add_argument("--fx", type=float, default=32.824)

    args = parser.parse_args(argv)

    try:
        if args.command == "shadow":
            from sip.shadow import run_shadow

            paths = run_shadow(
                market=args.market,
                slot=args.slot,
                date=args.date,
                fixtures_dir=args.fixtures,
                out_root=args.out_root,
                tv_dump=args.tv_dump,
                require_mmx_chat=args.require_mmx_chat,
            )
            for name, path in paths.items():
                print(f"{name}: {path}")
            return 0

        if args.command == "compare":
            from sip.compare import compare, print_report

            result = compare(args.shadow, args.live)
            print_report(result)
            if args.json_out:
                path = Path(args.json_out)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(
                    json.dumps(result, ensure_ascii=False, indent=2, default=str),
                    encoding="utf-8",
                )
            return 0

        from sip.number_trace import check_chat

        run_data = _load_json(args.run)
        chat_text = Path(args.chat).read_text(encoding="utf-8")
        check_result = check_chat(run_data, chat_text)
        if isinstance(check_result, tuple):
            ok, report = check_result
        elif isinstance(check_result, dict):
            report = check_result
            ok = bool(report.get("ok", not report.get("errors")))
        else:
            ok = bool(check_result)
            report = {"ok": ok}

        print(json.dumps(report, ensure_ascii=False, indent=2, default=str))
        return 0 if ok else 1
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
