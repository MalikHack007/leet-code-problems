import pytest

from leetcode.testing import assert_case
from .cases import TEST_CASES
from .solution import Solution


@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case.name)
def test_solution(case):
    assert_case(Solution, case)
