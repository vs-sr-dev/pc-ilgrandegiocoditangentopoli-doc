#!/usr/bin/env python3
"""dirguard.py -- one guard for readers handed a directory, and a survey that
says how big the class is.

THE DEFECT, IN TWO INSTANCES AND THEREFORE A CLASS
--------------------------------------------------
`pc-rpgmaker2003-doc/docs/14`, correction 27, recorded that `ne.py` handed a
directory raises an uncaught `PermissionError` instead of refusing. It was
found **after publication**, while pointing the same box at the object this
repository documents. On that object `jpeg.py` does exactly the same thing.

Two instances make a class, and a class gets one repair rather than two:

    import dirguard
    dirguard.want_file(path, "ne")

`want_file` exits with a message and a non-zero status when the path is a
directory, is missing, or is not a regular file. It never raises. That turns a
five-line traceback carrying an absolute path -- which is also a rule-7
hazard, because a traceback captured into `notes/` publishes this machine's
directory layout -- into one line that names the tool, the path and what the
tool wanted instead.

THE SURVEY, WHICH IS WHY THIS IS A TOOL AND NOT A THREE-LINE FUNCTION
--------------------------------------------------------------------
"Two tools do this" is a count of the two that were noticed. `--survey` runs
every Python file in a tool box with **one empty directory** as its only
argument and classifies what comes back:

    raised        a traceback reached the user -- the defect
    refused       a non-zero exit with no traceback -- the tool working
    exit 0        it accepted a directory and printed something

The directory is empty so that no tool does real work on it and the survey is
quick; the question being asked is about the tool's front door and not about
its output.

    python tools/dirguard.py --survey --tools tools
    python tools/dirguard.py --selftest
"""
import argparse
import os
import subprocess
import sys
import tempfile


def want_file(path, tool="reader"):
    """Refuse, out loud and without a traceback, anything that is not a file."""
    if os.path.isdir(path):
        sys.exit("%s: %s is a directory; this reader wants one file. "
                 "Point it at a file, or use a census tool that walks a tree."
                 % (tool, path))
    if not os.path.exists(path):
        sys.exit("%s: no such file: %s" % (tool, path))
    if not os.path.isfile(path):
        sys.exit("%s: %s is not a regular file" % (tool, path))
    return path


def classify(rc, out):
    if "Traceback (most recent call last)" in out:
        return "raised"
    if rc != 0:
        return "refused"
    return "exit 0"


def survey(toolsdir, timeout):
    names = sorted(n for n in os.listdir(toolsdir) if n.endswith(".py"))
    if not names:
        sys.exit("dirguard: no .py under %r -- refusing to report a clean "
                 "table over an empty population" % toolsdir)
    counts = {"raised": [], "refused": [], "exit 0": [], "timed out": []}
    with tempfile.TemporaryDirectory() as empty:
        for n in names:
            if n == "dirguard.py":
                continue
            argv = [sys.executable, os.path.join(toolsdir, n), empty]
            try:
                p = subprocess.run(argv, capture_output=True, timeout=timeout)
                out = (p.stdout + p.stderr).decode("utf-8", "replace")
                counts[classify(p.returncode, out)].append(n)
            except subprocess.TimeoutExpired:
                counts["timed out"].append(n)
    total = sum(len(v) for v in counts.values())
    print("tool box              : %s" % toolsdir)
    print("Python files surveyed : %d" % total)
    print("each was handed ONE EMPTY DIRECTORY as its only argument.")
    print()
    for k in ("raised", "refused", "exit 0", "timed out"):
        print("  %-10s %4d" % (k, len(counts[k])))
    print()
    print("  RAISED -- a traceback reached the user. This is the defect:")
    for n in counts["raised"]:
        print("     %s" % n)
    print()
    print("  timed out (not classified, and not counted as either):")
    for n in counts["timed out"]:
        print("     %s" % n)
    return 0


def selftest():
    checks = []

    def ok(label, cond, note=""):
        checks.append((label, bool(cond), note))

    here = os.path.dirname(os.path.abspath(__file__))
    ok("a directory is refused and not raised on",
       _exits(lambda: want_file(here, "t")))
    ok("a missing path is refused", _exits(lambda: want_file(
        os.path.join(here, "no-such-file-at-all"), "t")))
    ok("a real file passes through unchanged",
       want_file(os.path.abspath(__file__), "t") == os.path.abspath(__file__))
    # The NOTE column deliberately prints only the first word of the message.
    # Printing the whole of it put this machine's absolute path into
    # `notes/selftests.txt`, which rule 7 forbids and `pathcheck.py` caught.
    ok("the message names the tool",
       _message(lambda: want_file(here, "mytool")).startswith("mytool:"),
       _message(lambda: want_file(here, "mytool")).split()[0])
    ok("the message says what to do instead",
       "wants one file" in _message(lambda: want_file(here, "t")))
    ok("and it does not print anything but the path it was given",
       _message(lambda: want_file(here, "t")).count(here) == 1)
    ok("a traceback is classified as raised",
       classify(1, "Traceback (most recent call last):\n  ...") == "raised")
    ok("a non-zero exit with no traceback is a refusal",
       classify(1, "ne: x is a directory") == "refused")
    ok("exit 0 is neither", classify(0, "a table") == "exit 0")

    width = max(len(c[0]) for c in checks)
    failed = 0
    for label, good, note in checks:
        print("  %-*s  %s   %s" % (width, label, "ok  " if good else "FAIL",
                                   note))
        if not good:
            failed += 1
    print()
    print("%d checks, %d failures" % (len(checks), failed))
    return 1 if failed else 0


def _exits(fn):
    try:
        fn()
    except SystemExit:
        return True
    return False


def _message(fn):
    try:
        fn()
    except SystemExit as e:
        return str(e)
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--survey", action="store_true")
    ap.add_argument("--tools", default="tools")
    ap.add_argument("--timeout", type=float, default=20.0)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if args.survey:
        return survey(args.tools, args.timeout)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
