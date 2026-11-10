#!/usr/bin/env python3
"""run_tests.py — run every test suite in this directory and report one verdict.

Why this exists: the migration repo's tests are standalone scripts with their
own exit codes, and this repo's `pre-commit` hook needs ONE command to call
so a regression blocks the commit rather than shipping.

Each suite is run as a subprocess, so a suite that crashes takes its own exit
code with it and cannot take the others down. A suite that cannot run is a
FAILURE, not a skip: a test that does not run proves nothing.

  python3 scripts/run_tests.py            # run every suite
  python3 scripts/run_tests.py joinlib    # run the suites whose name matches
  python3 scripts/run_tests.py --verbose  # show each test's name

Exit: 0 = every suite passed, 1 = something failed.
"""
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def suites(pattern=None):
    out = []
    for path in sorted(glob.glob(os.path.join(HERE, "test_*.py"))):
        name = os.path.basename(path)[len("test_"):-len(".py")]
        if pattern and pattern not in name:
            continue
        out.append((name, path))
    return out


def main(argv):
    verbose = "--verbose" in argv
    patterns = [a for a in argv if not a.startswith("--")]
    pattern = patterns[0] if patterns else None

    found = suites(pattern)
    if not found:
        print("no test suite found%s" % (" matching %r" % pattern if pattern else ""))
        return 1

    failed = []
    for name, path in found:
        print("=== %s ===" % name)
        cmd = [sys.executable, path]
        if verbose:
            cmd.append("-v")
        r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True)
        out = r.stdout or ""
        err = r.stderr or ""
        if out:
            print(out.rstrip())
        if err and r.returncode != 0:
            print(err.rstrip())
        if r.returncode != 0:
            failed.append(name)
            print("--- %s FAILED (exit %d)" % (name, r.returncode))
        else:
            print("--- %s ok" % name)

    print()
    if failed:
        print("FAILED: %s" % ", ".join(failed))
        return 1
    print("all %d suite(s) passed" % len(found))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
