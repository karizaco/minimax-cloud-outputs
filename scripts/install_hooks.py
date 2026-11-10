#!/usr/bin/env python3
"""Install this repo's git hooks, and stop git looking somewhere else for them.

Why this exists: git resolves hooks through `core.hooksPath` when it is set,
and ignores `.git/hooks/` entirely. A clone with `core.hooksPath` pointing at a
scratch directory has NO working hooks - the ones in `.git/hooks/` are dead
files - and a scratch directory in temp space can be cleaned up at any moment,
silently disabling every check.

This installs the tracked hooks from `scripts/hooks/` into `.git/hooks/`, makes
them executable, and clears a `core.hooksPath` that points outside the repo.

  python3 scripts/install_hooks.py          # install and clear the override
  python3 scripts/install_hooks.py --check  # report what is installed
  python3 scripts/install_hooks.py --keep-hooks-path
                                           # install but leave core.hooksPath
"""
import argparse
import os
import shutil
import stat
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(REPO, "scripts", "hooks")
TARGET = os.path.join(REPO, ".git", "hooks")

# A hooksPath outside the repo is a scratch directory by another name.
TEMP_MARKERS = ("\\tmp\\", "\\temp\\", "appdata\\local\\temp")


def run(*args):
    return subprocess.run(args, cwd=REPO, capture_output=True, text=True)


def current_hooks_path():
    r = run("git", "config", "--local", "--get", "core.hooksPath")
    return r.stdout.strip() if r.returncode == 0 else None


def is_scratch(path):
    """A hooksPath outside the repo, in temp space.

    `C:/tmp/gitrun` is the path that actually disabled this clone's hooks.
    Matching is case-insensitive and slash-insensitive, because Windows and
    the Linux sandbox spell the same directory differently.
    """
    if not path:
        return False
    norm = path.replace("/", "\\").lower()
    return any(m in norm for m in TEMP_MARKERS)


def installed_hooks():
    out = {}
    if not os.path.isdir(TARGET):
        return out
    for name in sorted(os.listdir(TARGET)):
        if name.endswith(".sample"):
            continue
        path = os.path.join(TARGET, name)
        if os.path.isfile(path):
            out[name] = path
    return out


def do_install(keep_hooks_path):
    os.makedirs(TARGET, exist_ok=True)
    installed = []
    for name in sorted(os.listdir(SOURCE)):
        src = os.path.join(SOURCE, name)
        if not os.path.isfile(src):
            continue
        dst = os.path.join(TARGET, name)
        # The tracked file is the source of truth. Copy it verbatim, then make
        # it executable - on Windows the executable bit is not what git checks,
        # but on the Linux sandbox it is.
        with open(src, "rb") as fh:
            data = fh.read()
        with open(dst, "wb") as fh:
            fh.write(data)
        mode = os.stat(dst).st_mode
        os.chmod(dst, mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        installed.append(name)

    cleared = None
    hp = current_hooks_path()
    # Only a scratch path is cleared. A hooksPath inside the repo is a
    # deliberate choice (a tracked `.githooks/` directory, for instance) and
    # installing must not undo it.
    if hp and not keep_hooks_path and is_scratch(hp):
        r = run("git", "config", "--local", "--unset", "core.hooksPath")
        cleared = hp if r.returncode == 0 else None

    return installed, cleared


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="report, install nothing")
    ap.add_argument("--keep-hooks-path", action="store_true",
                    help="install into .git/hooks but leave core.hooksPath alone")
    args = ap.parse_args(argv[1:])

    hp = current_hooks_path()
    have = installed_hooks()
    wanted = sorted(n for n in os.listdir(SOURCE)
                    if os.path.isfile(os.path.join(SOURCE, n))) if os.path.isdir(SOURCE) else []

    if args.check:
        print("core.hooksPath: %s" % (hp or "(not set - .git/hooks is used)"))
        if hp:
            print("  %s" % ("SCRATCH - outside the repo, and it overrides .git/hooks"
                            if is_scratch(hp) else "custom path"))
        for name in wanted:
            path = os.path.join(TARGET, name)
            ok = os.path.exists(path)
            same = ok and open(path, "rb").read() == open(
                os.path.join(SOURCE, name), "rb").read()
            print("  %-14s %s%s" % (name, "installed" if ok else "MISSING",
                                     "" if same else " (differs from the tracked copy)"))
        for name in sorted(have):
            if name not in wanted:
                print("  %-14s installed but not tracked in scripts/hooks/" % name)
        return 0

    installed, cleared = do_install(args.keep_hooks_path)
    print("installed into .git/hooks/: %s" % ", ".join(installed))
    if cleared:
        print("cleared core.hooksPath (was %s)" % cleared)
    elif args.keep_hooks_path and hp:
        print("core.hooksPath left at %s - git will NOT use .git/hooks/" % hp)
    elif not hp:
        print("core.hooksPath was not set - .git/hooks was already in use")
    else:
        print("core.hooksPath is %s - git will NOT use .git/hooks/" % hp)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
