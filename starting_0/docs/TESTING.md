# Testing Guide

## Overview

This project includes a subject-level smoke test suite for exercises `ex00` through `ex08`.
The test entry point is `tests/test_starting_0.py`.

The suite checks:

- script exit status
- expected standard output format
- basic functional behavior for each exercise

## Prerequisites

- Python 3
- run commands from the project root
- no third-party packages are required

The test runner uses the same Python interpreter that launches `unittest`.

## Run Tests

Run the full test suite:

```bash
python3 -m unittest tests/test_starting_0.py -v
```

You can also use test discovery:

```bash
python3 -m unittest discover -s tests -v
```

## Coverage

The current suite validates the following behaviors:

- `ex00/Hello.py`: expected container output
- `ex01/format_ft_time.py`: time string shape and date formatting
- `ex02/find_ft_type.py`: type detection output for supported inputs
- `ex03/NULL_not_found.py`: null-like value reporting
- `ex04/whatis.py`: even/odd handling and argument validation
- `ex05/building.py`: character counting from argv and stdin
- `ex06/ft_filter.py`: compatibility with built-in `filter`
- `ex06/filterstring.py`: filtered word list and invalid argument handling
- `ex07/sos.py`: Morse conversion and invalid input handling
- `ex08/Loading.py`: progress output shape and yielded values

## Notes

- These tests are smoke tests, not exhaustive unit tests.
- Several assertions depend on exact output strings, so small formatting changes can fail the suite.
- `ex08` is validated by matching key progress bar fragments instead of a fully fixed line.
