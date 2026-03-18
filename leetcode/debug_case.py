from __future__ import annotations

import argparse
import importlib
from pprint import pprint

from leetcode.testing import execute_case, get_case


parser = argparse.ArgumentParser(
    description="Run or debug a single LeetCode test case by name."
)
parser.add_argument("problem", help="Problem package path, for example problems.two_sum")
parser.add_argument("case_name", help="Name of the case defined in cases.py")
parser.add_argument(
    "--breakpoint",
    action="store_true",
    dest="use_breakpoint",
    help="Pause before executing the solution so you can inspect state with pdb.",
)


def main() -> None:
    args = parser.parse_args()
    solution_module = importlib.import_module(f"{args.problem}.solution")
    cases_module = importlib.import_module(f"{args.problem}.cases")
    case = get_case(cases_module.TEST_CASES, args.case_name)

    print(f"Running {args.problem}:{case.name}")
    if case.description:
        print(case.description)

    print("\nInput:")
    pprint(case.input)
    print("\nExpected:")
    pprint(case.expected)

    if args.use_breakpoint:
        breakpoint()

    actual = execute_case(solution_module.Solution, case)
    print("\nActual:")
    pprint(actual)


if __name__ == "__main__":
    main()
