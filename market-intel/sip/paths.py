from __future__ import annotations

import os
import sys
from pathlib import Path


ALLOWED_OUT_ROOTS = [
    Path("/home/box/taiwan-in-play/shadow"),
]


def assert_safe_out_path(path: str | Path, *, label: str = "") -> Path:
    """Resolve *path* and ensure it is an allowed shadow or pytest path."""
    try:
        resolved = Path(path).expanduser().resolve()
    except (OSError, RuntimeError) as exc:
        print(
            f"unsafe output path{': ' + label if label else ''}: {exc}",
            file=sys.stderr,
        )
        raise SystemExit(2) from exc

    allowed = False
    for root in ALLOWED_OUT_ROOTS:
        try:
            if resolved == root or root in resolved.parents:
                allowed = True
                break
        except OSError:
            continue

    pytest_env = bool(os.environ.get("PYTEST_CURRENT_TEST"))
    pytest_path = (
        any(part in {"pytest-of-", "pytest-"} for part in resolved.parts)
        or resolved == Path("/tmp")
        or Path("/tmp") in resolved.parents
    )

    if not (allowed or (pytest_env and pytest_path)):
        print(
            f"unsafe output path{': ' + label if label else ''}: {resolved}",
            file=sys.stderr,
        )
        raise SystemExit(2)

    return resolved
