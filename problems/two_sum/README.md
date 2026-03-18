# Two Sum

This folder shows the expected layout for each LeetCode problem.

## Files

- `solution.py`: your LeetCode `Solution` class.
- `cases.py`: local test data you want to run repeatedly.
- `test_solution.py`: pytest entrypoint that runs every case in `cases.py`.

## Commands

Run every Two Sum test:

```bash
pytest problems/two_sum
```

Run just one case with pytest:

```bash
pytest problems/two_sum/test_solution.py -k example_2
```

Debug one case interactively:

```bash
python -m leetcode.debug_case problems.two_sum example_2 --breakpoint
```
