# LeetCode Local Workspace

This repository is set up so every LeetCode problem lives in its own folder under `problems/`.
Each folder contains:

- `solution.py` for your `Solution` class.
- `cases.py` for reusable local test cases.
- `test_solution.py` for pytest-based validation.
- `README.md` with problem-specific commands.

## Repository layout

```text
problems/
  two_sum/
    cases.py
    solution.py
    test_solution.py
leetcode/
  testing.py
  debug_case.py
tools/
  new_problem.py
```

## Quick start

### 1. Run the sample tests

```bash
pytest
```

### 2. Run one problem

```bash
pytest problems/two_sum
```

### 3. Run one named case

```bash
pytest problems/two_sum/test_solution.py -k example_2
```

### 4. Debug one named case

This prints the case input and expected output, then drops into `pdb` before the solution method runs.

```bash
python -m leetcode.debug_case problems.two_sum example_2 --breakpoint
```

If you only want to execute the case without stopping in the debugger:

```bash
python -m leetcode.debug_case problems.two_sum example_2
```

## Create a new problem folder

Use the generator script:

```bash
python tools/new_problem.py "Valid Parentheses" --method is_valid
```

That creates:

- `problems/valid_parentheses/solution.py`
- `problems/valid_parentheses/cases.py`
- `problems/valid_parentheses/test_solution.py`
- `problems/valid_parentheses/README.md`

Then replace the starter code with your real solution and cases.

## How test cases work

`cases.py` exports a `TEST_CASES` list of `TestCase` objects. Each case contains:

- `name`: stable identifier you can target with `pytest -k` or the debug runner.
- `input`: keyword arguments passed into a `Solution` method.
- `expected`: expected return value.
- `method`: which method on `Solution` to call.
- `description`: optional notes shown by the debug runner.

Example:

```python
from leetcode.testing import TestCase

TEST_CASES = [
    TestCase(
        name="example_1",
        input={"s": "()[]{}"},
        expected=True,
        method="is_valid",
    )
]
```
