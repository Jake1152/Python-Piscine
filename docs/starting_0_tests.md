# starting_0 Tests

The smoke tests live in `starting_0/tests/test_starting_0.py`.

Run them from inside `starting_0/`:

```sh
python3 -m unittest discover -s tests
```

Run them from the repository root:

```sh
python3 -m unittest discover -s starting_0/tests
```

## Test Structure

The tests use Python's built-in `unittest` module. The helper `run_python()` executes each exercise as a real Python process and checks `returncode`, `stdout`, and sometimes `stderr`. This is intentional because the subject grades script behavior and exact output formatting.

## Exercise Coverage

`ex00/Hello.py` checks the printed list, tuple, set, and dict greetings. The set output is parsed with `ast.literal_eval()` because set display order is not stable.

`ex01/format_ft_time.py` checks output shape with regular expressions. The current timestamp changes every run, so the test validates formatting instead of exact values.

`ex02/find_ft_type.py` runs subject-style calls to `all_thing_is_obj()` and checks printed type names, string handling, unknown type handling, and return value `42`.

`ex03/NULL_not_found.py` runs subject-style calls for `None`, `NaN`, `0`, empty string, `False`, and a non-null string. It checks both printed labels and the error return value.

`ex04/whatis.py` runs CLI cases for even, odd, no argument, zero, non-integer input, and too many arguments. Any uncaught traceback fails the test through a non-zero return code.

`ex05/building.py` checks both argument input and stdin input. The stdin case verifies that the trailing newline counts as a space, matching the subject note.

`ex06/ft_filter.py` checks that `ft_filter.__doc__` matches `filter.__doc__`, that lambda filtering works, and that `function is None` returns truthy items.

`ex06/filterstring.py` checks valid word filtering and bad argument handling. Valid output must be a printed list, not a generator object.

`ex07/sos.py` checks Morse conversion for `sos` and error handling for unsupported characters such as `$`.

`ex08/Loading.py` checks that `ft_tqdm()` yields all input values and that the progress output reaches `100%` with the final count. It does not compare the full progress bar byte-for-byte because carriage returns and terminal width make that unstable.

## Interpreting Failures

Prefer fixing the exercise code, not relaxing tests, unless the test contradicts `starting_0/en.subject.pdf`. The subject examples are the source of truth for CLI output, error text, argument count behavior, and required return values.
