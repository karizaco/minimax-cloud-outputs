from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from .number_trace import check_chat
from .paths import assert_safe_out_path


DEFAULT_CHAT_SYSTEM = """You are the SIP Taiwan-market chat writer.
Summarize the supplied run JSON accurately. Use only facts present in RUN_JSON.
Do not invent prices, catalysts, tickers, or numbers. Preserve exact ticker names.
Session turnover in RUN_JSON is TWD. Never label a TWD 億 figure as 億美元.
For chat turnover, divide TWD by the session FX and show US$ (for example,
US$896.1m). Use 億美元 only for that FX-converted USD-yi amount. If a TWD yi
amount is shown, label it 億元, 億台幣, or TWD; Taiwan chat policy prefers US$.
Return a concise Markdown chat digest. Every numeric claim must be supported by RUN_JSON.
"""


def resolve_mmx_bin(mmx_bin: str | Path | None = None) -> Path:
    """Resolve the chat executable to an absolute path.

    An explicit path or configured environment path takes precedence. The
    resolver itself does not require the file to exist; draft_chat reports a
    missing executable with exit code 2.
    """
    if mmx_bin:
        return Path(mmx_bin).expanduser().resolve()

    configured = os.environ.get("SIP_MMX_CHAT") or os.environ.get("MMX_CHAT_BIN")
    if configured:
        return Path(configured).expanduser().resolve()

    workspace = Path("/workspace/market-intel/bin/mmx_chat.py")
    if workspace.is_file():
        return workspace.resolve()

    return (Path(__file__).resolve().parents[2] / "bin" / "mmx_chat.py").resolve()


def _compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), default=str)


def _load_run(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _executable_for(mmx_bin: str | Path) -> list[str]:
    binary = str(mmx_bin)
    if binary.endswith(".py"):
        return [sys.executable, binary]
    return [binary]


def _run_fx(run_data: Any) -> float | None:
    if not isinstance(run_data, dict):
        return None
    for key in ("fx", "fx_rate"):
        value = run_data.get(key)
        if value is not None:
            try:
                fx = float(value)
            except (TypeError, ValueError):
                continue
            if fx > 0:
                return fx
    for container_name in ("meta", "metadata"):
        container = run_data.get(container_name)
        if not isinstance(container, dict):
            continue
        for key in ("fx", "fx_rate"):
            value = container.get(key)
            if value is not None:
                try:
                    fx = float(value)
                except (TypeError, ValueError):
                    continue
                if fx > 0:
                    return fx
    return None


def draft_chat(
    run_json_path: str | Path,
    out_chat_path: str | Path,
    *,
    mmx_bin: str | Path = resolve_mmx_bin(),
    chat_system_text: str = DEFAULT_CHAT_SYSTEM,
) -> int:
    """Generate a chat draft with mmx_chat and atomically publish it on success."""
    source = Path(run_json_path).expanduser().resolve()
    output = assert_safe_out_path(out_chat_path, label="draft output")
    prompt_path = assert_safe_out_path(
        output.with_suffix(output.suffix + ".prompt.txt"),
        label="draft prompt",
    )
    output.parent.mkdir(parents=True, exist_ok=True)

    resolved_mmx = resolve_mmx_bin(mmx_bin)
    if not resolved_mmx.is_file():
        return 2

    try:
        run_data = _load_run(source)
    except (OSError, ValueError, json.JSONDecodeError):
        return 2

    user_prompt = (
        chat_system_text.strip()
        + "\n\nRUN_JSON:\n"
        + _compact_json(run_data)
    )
    prompt_path.write_text(user_prompt, encoding="utf-8")

    failed_path = output.with_suffix(output.suffix + ".failed")
    temp_path = output.with_suffix(output.suffix + ".tmp")
    failed_path.unlink(missing_ok=True)
    temp_path.unlink(missing_ok=True)

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            prefix=".mmx-chat-",
            suffix=".md",
            dir=output.parent,
            delete=False,
        ) as handle:
            generated_path = Path(handle.name)

        command = [
            *_executable_for(resolved_mmx),
            "--system",
            chat_system_text,
            "--user",
            user_prompt,
            "--lane",
            "bulk",
            "--reasoning-effort",
            "low",
            "--out",
            str(generated_path),
        ]
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            generated_path.unlink(missing_ok=True)
            temp_path.unlink(missing_ok=True)
            return int(completed.returncode)

        content = generated_path.read_text(encoding="utf-8")
        generated_path.unlink(missing_ok=True)

        if not content.strip():
            temp_path.unlink(missing_ok=True)
            failed_path.write_text(
                completed.stdout + ("\n" + completed.stderr if completed.stderr else ""),
                encoding="utf-8",
            )
            return 5

        temp_path.write_text(content, encoding="utf-8")

        result = check_chat(run_data, content, fx_rate=_run_fx(run_data))
        if not result.get("ok", False):
            temp_path.unlink(missing_ok=True)
            failed_path.write_text(
                json.dumps(result, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            return 5

        os.replace(temp_path, output)
        return 0
    except Exception:
        temp_path.unlink(missing_ok=True)
        return 2


def draft_mmx(run_dict: dict[str, Any]) -> str:
    """Compatibility helper for callers that only need a deterministic draft."""
    return json.dumps(run_dict, ensure_ascii=False, indent=2, default=str)


__all__ = [
    "DEFAULT_CHAT_SYSTEM",
    "draft_chat",
    "draft_mmx",
    "resolve_mmx_bin",
]
