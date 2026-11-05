"""Draft SIP chat with Minimax and validate every numeric claim."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Sequence

from .number_trace import check_chat


def _prompt_template() -> str:
    return (
        Path(__file__).parent
        / "templates"
        / "prompts"
        / "chat_system.txt"
    ).read_text(encoding="utf-8")


def draft_chat(
    run_json_path: str | Path,
    out_chat_path: str | Path,
    *,
    mmx_bin: str | Path = "/workspace/market-intel/bin/mmx_chat.py",
) -> int:
    """Run Minimax, validate its draft, and atomically publish valid output."""
    run_path = Path(run_json_path)
    output_path = Path(out_chat_path)

    try:
        run_json: Any = json.loads(run_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"draft_mmx: unable to read run: {exc}", file=sys.stderr)
        return 2

    prompt = _prompt_template()
    prompt_path = run_path.with_suffix(run_path.suffix + ".prompt.txt")
    try:
        prompt_path.write_text(prompt, encoding="utf-8")
    except OSError as exc:
        print(f"draft_mmx: unable to write prompt: {exc}", file=sys.stderr)
        return 2

    command = [
        str(mmx_bin),
        "--lane",
        "bulk",
        "--run",
        str(run_path),
        "--out",
        str(output_path),
    ]

    try:
        completed = subprocess.run(command, check=False)
    except OSError as exc:
        print(f"draft_mmx: unable to execute Minimax: {exc}", file=sys.stderr)
        return 2

    if completed.returncode != 0:
        failed_path = output_path.with_suffix(output_path.suffix + ".failed")
        if output_path.exists():
            try:
                failed_path.write_text(output_path.read_text(encoding="utf-8"), encoding="utf-8")
                output_path.unlink()
            except OSError:
                pass
        return completed.returncode

    try:
        chat = output_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"draft_mmx: unable to read draft: {exc}", file=sys.stderr)
        return 2

    result = check_chat(run_json, chat)
    if not result["ok"]:
        failed_path = output_path.with_suffix(output_path.suffix + ".failed")
        try:
            failed_path.write_text(chat, encoding="utf-8")
            output_path.unlink()
        except OSError as exc:
            print(f"draft_mmx: unable to preserve invalid draft: {exc}", file=sys.stderr)
        print(json.dumps(result, ensure_ascii=False, indent=2), file=sys.stderr)
        return 5

    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Draft and validate SIP chat with Minimax")
    parser.add_argument("--run", required=True, help="Run JSON path")
    parser.add_argument("--out", required=True, help="Output chat Markdown path")
    parser.add_argument(
        "--mmx-bin",
        default="/workspace/market-intel/bin/mmx_chat.py",
        help="Minimax chat command",
    )
    args = parser.parse_args(argv)
    return draft_chat(args.run, args.out, mmx_bin=args.mmx_bin)


if __name__ == "__main__":
    raise SystemExit(main())
