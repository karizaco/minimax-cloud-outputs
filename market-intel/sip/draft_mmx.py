from __future__ import annotations

import json
import os
import re
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
Write relative volume with a unit, such as RelVol 5.0x or 5.01x.
"""


def resolve_mmx_bin(mmx_bin: str | Path | None = None) -> Path:
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
    return [sys.executable, binary] if binary.endswith(".py") else [binary]


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
        if isinstance(container, dict):
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


def _usage_meta(stdout: str, stderr: str) -> dict[str, Any] | None:
    for line in (stdout + "\n" + stderr).splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict) and (
            "tokens_out" in value or "lane" in value or "model" in value
        ):
            return value
    return None


def _rvol_values(run_data: Any) -> list[float]:
    if not isinstance(run_data, dict):
        return []
    candidates = run_data.get("candidates")
    if not isinstance(candidates, list):
        return []
    values: list[float] = []
    for candidate in candidates:
        if isinstance(candidate, dict):
            try:
                value = float(candidate.get("rvol"))
            except (TypeError, ValueError):
                continue
            if value > 0:
                values.append(value)
    return values


def _normalize_rvol_draft(content: str, run_data: Any) -> str:
    """Rewrite only a labelled bare rvol token, using candidate rvol as ground."""
    rvol_values = _rvol_values(run_data)
    if not rvol_values:
        return content
    pattern = re.compile(
        r"(?i)(?P<label>\b(?:RelVol|rvol)\s*|\b相對成交量\s*)"
        r"(?P<open>\*\*)?(?P<number>\d+(?:\.\d+)?)"
        r"(?![.0-9x×X%$US億元mbnA-Za-z0-9])(?P<close>\*\*)?"
    )
    for match in pattern.finditer(content):
        if bool(match.group("open")) != bool(match.group("close")):
            continue
        try:
            token = float(match.group("number"))
        except ValueError:
            continue
        for value in rvol_values:
            if token in {round(value, 1), round(value, 2), value}:
                replacement = match.group("label") + f"{value:.1f}x"
                if match.group("open"):
                    replacement = (match.group("label") + match.group("open")
                                   + f"{value:.1f}x" + match.group("close"))
                return content[:match.start()] + replacement + content[match.end():]
    return content


def draft_chat(run_json_path: str | Path, out_chat_path: str | Path, *,
               mmx_bin: str | Path = resolve_mmx_bin(),
               chat_system_text: str = DEFAULT_CHAT_SYSTEM) -> int:
    """Generate a chat draft with mmx_chat and atomically publish it on success."""
    source = Path(run_json_path).expanduser().resolve()
    output = assert_safe_out_path(out_chat_path, label="draft output")
    prompt_path = assert_safe_out_path(output.with_suffix(output.suffix + ".prompt.txt"),
                                       label="draft prompt")
    output.parent.mkdir(parents=True, exist_ok=True)
    resolved_mmx = resolve_mmx_bin(mmx_bin)
    if not resolved_mmx.is_file():
        return 2
    try:
        run_data = _load_run(source)
    except (OSError, ValueError, json.JSONDecodeError):
        return 2
    user_prompt = chat_system_text.strip() + "\n\nRUN_JSON:\n" + _compact_json(run_data)
    prompt_path.write_text(user_prompt, encoding="utf-8")
    failed_path = output.with_suffix(output.suffix + ".failed")
    failed_body_path = output.with_suffix(output.suffix + ".failed.md")
    failed_meta_path = output.with_suffix(output.suffix + ".failed.meta.json")
    temp_path = output.with_suffix(output.suffix + ".tmp")
    for path in (failed_path, failed_body_path, failed_meta_path, temp_path):
        path.unlink(missing_ok=True)

    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                         prefix=".mmx-chat-", suffix=".md",
                                         dir=output.parent, delete=False) as handle:
            generated_path = Path(handle.name)
        command = [*_executable_for(resolved_mmx), "--system", chat_system_text,
                   "--user", user_prompt, "--lane", "bulk",
                   "--reasoning-effort", "low", "--out", str(generated_path)]
        completed = subprocess.run(command, check=False, capture_output=True, text=True)
        if completed.returncode != 0:
            generated_path.unlink(missing_ok=True)
            temp_path.unlink(missing_ok=True)
            return int(completed.returncode)
        content = generated_path.read_text(encoding="utf-8")
        generated_path.unlink(missing_ok=True)
        if not content.strip():
            temp_path.unlink(missing_ok=True)
            failed_path.write_text(completed.stdout + ("\n" + completed.stderr if completed.stderr else ""),
                                   encoding="utf-8")
            return 5
        temp_path.write_text(content, encoding="utf-8")
        result = check_chat(run_data, content, fx_rate=_run_fx(run_data))
        if not result.get("ok", False):
            normalized = _normalize_rvol_draft(content, run_data)
            if normalized != content:
                temp_path.write_text(normalized, encoding="utf-8")
                retry = check_chat(run_data, normalized, fx_rate=_run_fx(run_data))
                if retry.get("ok", False):
                    os.replace(temp_path, output)
                    return 0
                result = retry
                content = normalized
            temp_path.unlink(missing_ok=True)
            failed_path.write_text(json.dumps(result, ensure_ascii=False, indent=2),
                                   encoding="utf-8")
            failed_body_path.write_text(content, encoding="utf-8")
            meta = _usage_meta(completed.stdout, completed.stderr)
            if meta is not None:
                failed_meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2),
                                            encoding="utf-8")
            return 5
        os.replace(temp_path, output)
        return 0
    except Exception:
        temp_path.unlink(missing_ok=True)
        return 2


def draft_mmx(run_dict: dict[str, Any]) -> str:
    return json.dumps(run_dict, ensure_ascii=False, indent=2, default=str)


__all__ = ["DEFAULT_CHAT_SYSTEM", "draft_chat", "draft_mmx", "resolve_mmx_bin"]
