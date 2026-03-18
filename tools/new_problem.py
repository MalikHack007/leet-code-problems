from __future__ import annotations

import argparse
from pathlib import Path

TEMPLATE = '''from leetcode.testing import TestCase

TEST_CASES = [
    TestCase(
        name="starter_case",
        input={{}},
        expected=None,
        method="{method_name}",
        description="Replace this starter case with a real LeetCode example.",
    ),
]
'''

TEST_TEMPLATE = '''import pytest

from leetcode.testing import assert_case
from .cases import TEST_CASES
from .solution import Solution


@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case.name)
def test_solution(case):
    assert_case(Solution, case)
'''

SOLUTION_TEMPLATE = '''class Solution:
    def {method_name}(self, **kwargs):
        """Replace this stub with your real LeetCode solution."""
        return None
'''

README_TEMPLATE = '''# {title}

- Put your LeetCode solution in `solution.py`.
- Define local test cases in `cases.py`.
- Run all tests for this problem with:
  - `pytest {folder_name}`
- Debug a single case with:
  - `python -m leetcode.debug_case problems.{module_name} starter_case --breakpoint`
'''


def slugify(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new LeetCode problem folder")
    parser.add_argument("name", help="Human-readable problem name, e.g. 'Two Sum'")
    parser.add_argument(
        "--method",
        default="two_sum",
        help="Method name to place on the Solution class",
    )
    args = parser.parse_args()

    module_name = slugify(args.name)
    folder = Path("problems") / module_name
    folder.mkdir(parents=True, exist_ok=False)

    (folder / "__init__.py").write_text("", encoding="utf-8")
    (folder / "cases.py").write_text(
        TEMPLATE.format(method_name=args.method), encoding="utf-8"
    )
    (folder / "solution.py").write_text(
        SOLUTION_TEMPLATE.format(method_name=args.method), encoding="utf-8"
    )
    (folder / "test_solution.py").write_text(TEST_TEMPLATE, encoding="utf-8")
    (folder / "README.md").write_text(
        README_TEMPLATE.format(
            title=args.name,
            folder_name=folder.as_posix(),
            module_name=module_name,
        ),
        encoding="utf-8",
    )

    print(f"Created {folder}")


if __name__ == "__main__":
    main()
