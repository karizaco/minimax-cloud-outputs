#!/usr/bin/env python3
"""test_hooks.py — regression tests for the git hooks and the installer.

Why: the hooks failed TWICE in one session, and both failures were SILENT.
A hook that reports success while doing nothing is worse than no hook, because
it removes the check without removing the confidence.

  - the hook called `python3`, which does not exist on the Windows box, and
    because the call was piped into `tail` the failure was invisible;
  - the hook used `git commit --only -- derived/`, a PARTIAL commit, which git
    refuses while a merge is in progress - and MERGE_HEAD is present exactly
    when post-merge runs. The hook printed "committed" and committed nothing.

These tests run the real hook against a real scratch repository, because the
thing that failed was the interaction between the hook and git, not the hook's
own logic.

Offline and dependency-free: the Cloud sandbox has no PyPI access, and git is
already present - it is how this repo is version-controlled.

  python3 scripts/test_hooks.py
Exit: 0 = all passed, 1 = a test failed.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import install_hooks  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOKS_SOURCE = os.path.join(REPO, "scripts", "hooks")


def run(cmd, cwd=None, env=None):
    """Run a command, returning (rc, stdout, stderr)."""
    e = dict(os.environ)
    e.update({
        "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
        "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t",
    })
    if env:
        e.update(env)
    r = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, env=e)
    return r.returncode, r.stdout, r.stderr


def sh(cmd, cwd=None, check=True):
    rc, out, err = run(cmd, cwd=cwd)
    if check and rc != 0:
        raise AssertionError("command failed: %s\n%s%s" % (cmd, out, err))
    return out


class ScratchRepo(unittest.TestCase):
    """A bare origin, a working clone, and a hook."""

    def setUp(self):
        self.base = tempfile.mkdtemp(prefix="hooktest-")
        self.origin = os.path.join(self.base, "origin.git")
        self.work = os.path.join(self.base, "work")
        self.other = os.path.join(self.base, "other")
        sh("git init -q --bare -b main %s" % self.origin)
        sh("git clone -q %s %s" % (self.origin, self.work))
        sh("git clone -q %s %s" % (self.origin, self.other))
        for d in (self.work, self.other):
            sh("git config user.email t@t", cwd=d)
            sh("git config user.name t", cwd=d)
            # Without this, a staged file's worktree copy differs from the index
            # (CRLF) and `git merge` refuses, so the hook never runs.
            sh("git config core.autocrlf false", cwd=d)
        with open(os.path.join(self.work, "a.txt"), "w") as fh:
            fh.write("a\n")
        sh("git add -A && git commit -q -m base", cwd=self.work)
        sh("git push -q origin main", cwd=self.work)
        self._install_hook()

    def tearDown(self):
        shutil.rmtree(self.base, ignore_errors=True)

    def _install_hook(self):
        # The hook exits early unless `scripts/build_derived.py` exists, so the
        # scratch repo needs one. It is a stub - the hook's BUILD step is
        # replaced below, and the commit path under test is the hook's own.
        os.makedirs(os.path.join(self.work, "scripts"), exist_ok=True)
        with open(os.path.join(self.work, "scripts", "build_derived.py"), "w") as fh:
            fh.write("# stub\n")

        hook = os.path.join(self.work, ".git", "hooks", "post-merge")
        with open(os.path.join(HOOKS_SOURCE, "post-merge"), "rb") as fh:
            original = fh.read()
        data = original
        # The real hook runs the real builder, which needs the real scripts. A
        # The real hook runs the real builder, which needs the real scripts. A
        # scratch repo has none, so the hook's BUILD step is replaced by a
        # stand-in that writes into derived/ - the commit path under test is
        # the hook's own, unchanged.
        #
        # The replacement keeps the hook's `if ! ...; then` shape so the
        # failure branch still exists, which is what the failing-build test
        # exercises.
        data = data.replace(
            b'if ! "$PY" scripts/build_derived.py >"$LOG" 2>&1; then',
            b'mkdir -p derived; printf "x\\n" > derived/new.txt; '
            b'if ! "$PY" -c "pass" >"$LOG" 2>&1; then')
        self.assertNotEqual(
            data, original,
            "the hook's build step was not replaced - the test would run the "
            "real builder against a scratch repo")
        with open(hook, "wb") as fh:
            fh.write(data)
        os.chmod(hook, 0o755)

    def upstream_commit(self, name):
        # `other` was cloned before `work` pushed its first commit, so it has
        # no origin/main until it fetches. And `work`'s origin/main is stale
        # until IT fetches - merging the stale ref is "Already up to date"
        # and the hook never runs.
        sh("git fetch -q origin main", cwd=self.other)
        sh("git checkout -q -B main FETCH_HEAD", cwd=self.other)
        with open(os.path.join(self.other, name), "w") as fh:
            fh.write(name + "\n")
        sh("git add -A && git commit -q -m up-%s" % name, cwd=self.other)
        sh("git push -q origin main", cwd=self.other)

    def merge_upstream(self):
        sh("git fetch -q origin", cwd=self.work)
        return run("git merge --no-ff origin/main -m merge", cwd=self.work)


class PostMergeHook(ScratchRepo):
    def test_the_hook_commits_successfully(self):
        """The commit must EXIT 0.

        It used to be `git commit --only -- derived/`, a partial commit, which
        git refuses while MERGE_HEAD is present - and MERGE_HEAD IS present
        when post-merge runs.
        """
        self.upstream_commit("b.txt")
        rc, out, err = self.merge_upstream()
        self.assertEqual(rc, 0, "the merge failed:\n%s%s" % (out, err))
        combined = out + err
        self.assertIn("post-merge: derived/ updated and committed.", combined,
                      "the hook did not report a successful commit:\n%s" % combined)

    def test_the_hook_leaves_no_staged_residue(self):
        """The silent failure: it printed 'committed' and committed nothing."""
        self.upstream_commit("c.txt")
        self.merge_upstream()
        rc, out, _err = run("git status --porcelain", cwd=self.work)
        self.assertEqual(rc, 0)
        staged = [l for l in out.splitlines() if l[:1] in ("M", "A", "D")]
        self.assertEqual(staged, [],
                         "the hook left changes staged but uncommitted: %r" % staged)

    def test_the_new_file_is_actually_committed(self):
        """`git add -u` only stages TRACKED files.

        A merge bringing a NEW session's artifacts left that session's derived
        views untracked and out of the commit entirely.
        """
        self.upstream_commit("d.txt")
        self.merge_upstream()
        rc, out, _err = run("git ls-tree -r --name-only HEAD", cwd=self.work)
        self.assertIn("derived/new.txt", out,
                      "the new derived file was not committed")

    def test_the_hook_does_not_sweep_unrelated_staged_content(self):
        """A file staged beside the hook's commit must not ride along in it.

        `git merge` itself refuses to start while a new file is staged, so this
        drives the hook in the state it actually runs in: MERGE_HEAD present,
        and something else already in the index.
        """
        parent = sh("git rev-parse HEAD", cwd=self.work).strip()
        with open(os.path.join(self.work, ".git", "MERGE_HEAD"), "w", newline="\n") as fh:
            fh.write(parent + "\n")
        with open(os.path.join(self.work, "other.txt"), "w") as fh:
            fh.write("other\n")
        sh("git add other.txt", cwd=self.work)
        rc, out, err = run("sh .git/hooks/post-merge", cwd=self.work)
        self.assertEqual(rc, 0, "hook failed:\n%s%s" % (out, err))
        rc, show, _err = run("git show --name-only --pretty=format: HEAD", cwd=self.work)
        self.assertIn("derived/new.txt", show, show)
        self.assertNotIn("other.txt", show,
                         "the hook swept unrelated staged content into its commit:\n%s" % show)
        rc, staged, _err = run("git diff --cached --name-only", cwd=self.work)
        self.assertIn("other.txt", staged,
                      "the unrelated file was not put back in the index:\n%s" % staged)

    def test_a_failing_builder_is_not_reported_as_success(self):
        """The hook must not swallow a failing build."""
        hook = os.path.join(self.work, ".git", "hooks", "post-merge")
        with open(hook, "rb") as fh:
            original = fh.read()
        data = original.replace(
            b'mkdir -p derived; printf "x\\n" > derived/new.txt; '
            b'if ! "$PY" -c "pass" >"$LOG" 2>&1; then',
            b'mkdir -p derived; printf "x\\n" > derived/new.txt; '
            b'if ! "$PY" -c "import sys; sys.exit(3)" >"$LOG" 2>&1; then')
        self.assertNotEqual(
            data, original,
            "the failing-build replacement did not apply - the test is vacuous")
        with open(hook, "wb") as fh:
            fh.write(data)
        self.upstream_commit("f.txt")
        rc, out, err = self.merge_upstream()
        self.assertNotIn("post-merge: derived/ updated and committed.", out,
                         "a failing build was reported as a success")
        # The hook reports the failure on stderr, so stderr is where the
        # message must be. Checking stdout alone would pass vacuously.
        self.assertIn("FAILED", err,
                      "the failing build was not reported:\n%s%s" % (out, err))


class Installer(unittest.TestCase):
    """The installer, exercised IN-PROCESS against a scratch repo.

    The installer is bound to the real repo by a module-level REPO, so running
    it as a subprocess from a scratch directory would install into the REAL
    .git/hooks and clear the REAL core.hooksPath. Every test here patches the
    module's REPO instead, so the real repository is never touched.
    """

    def setUp(self):
        self.base = tempfile.mkdtemp(prefix="install-hooks-")
        self.work = os.path.join(self.base, "work")
        sh("git init -q -b main %s" % self.work)
        self._real_repo = install_hooks.REPO
        self._real_source = install_hooks.SOURCE
        self._real_target = install_hooks.TARGET
        install_hooks.REPO = self.work
        install_hooks.SOURCE = os.path.join(self.work, "scripts", "hooks")
        install_hooks.TARGET = os.path.join(self.work, ".git", "hooks")
        os.makedirs(install_hooks.SOURCE, exist_ok=True)
        for name in ("pre-commit", "post-merge"):
            shutil.copy(os.path.join(HOOKS_SOURCE, name),
                        os.path.join(install_hooks.SOURCE, name))

    def tearDown(self):
        install_hooks.REPO = self._real_repo
        install_hooks.SOURCE = self._real_source
        install_hooks.TARGET = self._real_target
        shutil.rmtree(self.base, ignore_errors=True)

    def test_a_scratch_hooks_path_is_reported_as_scratch(self):
        """A `core.hooksPath` outside the repo disables `.git/hooks/` entirely.

        A scratch directory in temp space can be cleaned up at any moment,
        silently disabling every check.
        """
        sh('git config core.hooksPath "C:/tmp/gitrun"', cwd=self.work)
        self.assertTrue(install_hooks.is_scratch("C:/tmp/gitrun"))
        self.assertFalse(install_hooks.is_scratch(".githooks"))
        self.assertFalse(install_hooks.is_scratch(""))

    def test_installing_clears_a_scratch_hooks_path(self):
        sh('git config core.hooksPath "C:/tmp/gitrun"', cwd=self.work)
        installed, cleared = install_hooks.do_install(False)
        self.assertIn("pre-commit", installed)
        self.assertIn("post-merge", installed)
        self.assertEqual(cleared, "C:/tmp/gitrun")
        rc, _out, _err = run("git config --local --get core.hooksPath", cwd=self.work)
        self.assertNotEqual(rc, 0, "core.hooksPath was not cleared")

    def test_a_hooks_path_inside_the_repo_is_left_alone(self):
        """A deliberate choice is not a scratch path."""
        sh('git config core.hooksPath ".githooks"', cwd=self.work)
        installed, cleared = install_hooks.do_install(False)
        self.assertIn("pre-commit", installed)
        self.assertIsNone(cleared, "a deliberate hooksPath was cleared")
        rc, out, _err = run("git config --local --get core.hooksPath", cwd=self.work)
        self.assertEqual(rc, 0, "a deliberate hooksPath was removed")
        self.assertIn(".githooks", out)

    def test_the_installed_hook_is_byte_identical_to_the_tracked_one(self):
        """The tracked file is the source of truth.

        If they drift, the hook that runs is not the hook that was reviewed.
        """
        install_hooks.do_install(False)
        for name in ("pre-commit", "post-merge"):
            installed = os.path.join(install_hooks.TARGET, name)
            tracked = os.path.join(HOOKS_SOURCE, name)
            with open(installed, "rb") as fh:
                got = fh.read()
            with open(tracked, "rb") as fh:
                want = fh.read()
            self.assertEqual(got, want,
                             "the installed %s differs from the tracked copy" % name)

    def test_the_installed_hook_is_executable(self):
        """On the Linux sandbox the executable bit is what runs the hook."""
        install_hooks.do_install(False)
        for name in ("pre-commit", "post-merge"):
            path = os.path.join(install_hooks.TARGET, name)
            self.assertTrue(os.path.exists(path), "%s was not installed" % name)
            self.assertTrue(os.access(path, os.X_OK),
                            "%s is not executable" % name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
