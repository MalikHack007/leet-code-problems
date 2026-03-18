# Word Search

## Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true`
if `word` exists in the grid.

The word can be constructed from sequentially adjacent cells, where adjacent
cells are horizontally or vertically neighboring. The same cell may not be used
more than once.

## Current target case

This folder is preloaded with your requested case:

- `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`
- `word = "ABCCED"`
- expected result: `True`
- pytest case name: `example_abcced`

## Files

- `solution.py`: stub for `Solution.exist`.
- `cases.py`: the reusable local test case definition.
- `test_solution.py`: pytest entrypoint for the case.

## How to debug this case in VS Code

1. Put a breakpoint in `problems/word_search/solution.py`.
2. Open **Run and Debug** in VS Code.
3. Start **Python: Debug named pytest case**.
4. Use `problems/word_search/test_solution.py` as the target.
5. Use `example_abcced` as the case name.

That will run the equivalent of:

```bash
pytest problems/word_search/test_solution.py -k example_abcced -vv -s
```

## Note about the current stub

`Solution.exist` intentionally raises `NotImplementedError` right now because you
asked me not to write the solution. Until you implement it, the pytest case will
show as `xfail` instead of failing the whole test run.
