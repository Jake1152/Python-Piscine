---
name: python-piscine-starting
description: Use this skill when working on this repository's 42 Python Piscine starting_0 exercises, especially when testing, fixing, or extending ex00 through ex09 against en.subject.pdf and the local unittest smoke tests.
---

# Python Piscine Starting

## Overview

This repository tracks 42 Python Piscine `starting_0` exercises. Use the subject PDF as the source of truth, keep exercise outputs byte-for-byte close to the examples, and validate with the local smoke tests before reporting completion.

## Project Map

- Subject: `starting_0/en.subject.pdf`
- Current smoke tests: `tests/test_starting_0.py`
- Test command: `python3 -m unittest discover -s tests`
- Exercise roots: `starting_0/ex00` through `starting_0/ex09`
- Active issue reference: GitHub issue `#1`, "Add and fix subject smoke tests for starting_0 ex00-ex07"

## Workflow

1. Read the relevant exercise section from `starting_0/en.subject.pdf` before changing behavior.
2. Run `python3 -m unittest discover -s tests` to capture the current baseline.
3. Fix the smallest subject mismatch first, preserving file names and CLI behavior exactly.
4. Re-run the full test command after edits.
5. Report remaining failures explicitly if any test still fails.

## Subject Rules To Enforce

- Use Python 3.10-compatible code.
- No global executable code from `ex05` onward; use `main()` and `if __name__ == "__main__":`.
- Catch required error cases; uncaught exceptions invalidate exercises.
- Functions must have docstrings from `ex05` onward.
- Imports must be explicit; never use wildcard imports.
- Global constants are risky because the subject says global variables are not allowed. Prefer local dictionaries inside `main()` unless an exercise strongly implies otherwise.
- Match error strings closely, especially `AssertionError:` with no space before the colon.

## Current Known Failures

These failures come from issue `#1` and the current smoke test baseline:

- `starting_0/ex04/whatis.py`: non-integer input such as `Hi!` raises uncaught `ValueError`; expected `AssertionError: argument is not an integer`.
- `starting_0/ex06/ft_filter.py`: `ft_filter.__doc__` does not exactly match `filter.__doc__`.
- `starting_0/ex06/filterstring.py`: valid cases print a generator object instead of a list.
- `starting_0/ex06/filterstring.py`: error output uses `AssertionError :` instead of `AssertionError:`.
- `starting_0/ex07/sos.py`: argument count assertion is inverted, so valid input such as `sos` fails.
- `starting_0/ex07/sos.py`: error output includes extra text and spacing instead of `AssertionError: the arguments are bad`.

## Fixing Guidance

For `ex04`, catch `ValueError` from `int(argv[1])` and convert it to the required `AssertionError` message. Do not use `abs()` to determine parity; negative integers already work with `% 2`.

For `ex06`, keep `ft_filter` lazy like built-in `filter`, but make `filterstring.py` print `list(ft_filter(...))`. The subject requires at least one list comprehension expression and one lambda in the program. Keep `ft_filter` implemented without calling built-in `filter`.

For `ex07`, validate `len(argv) == 2`, accept only alphanumeric characters and spaces, uppercase letters for lookup, map spaces to `/`, and join Morse tokens with a single space so the final line has no trailing space.

For `ex08`, `ft_tqdm(lst: range)` must use `yield`. Non-interactive test environments may not provide a terminal size, so code using `os.get_terminal_size()` should handle `OSError` or provide a fallback width.

For `ex09`, create an installable `ft_package` with `count_in_list`, `pyproject.toml`, `README.md`, `LICENSE`, and build artifacts under `dist/` when requested.

## Validation Checklist

- `python3 -m py_compile` passes for edited Python files.
- `python3 -m unittest discover -s tests` is run from the repository root.
- CLI outputs are checked with exact strings, including newlines and spaces.
- No unrelated generated files such as `__pycache__` are committed unless explicitly requested.
