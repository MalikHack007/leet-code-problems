import pytest

from leetcode.testing import assert_case
from .cases import TEST_CASES
from .solution import Solution


@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case.name)
def test_solution(case):
    try:
        assert_case(Solution, case)
    except NotImplementedError:
        pytest.xfail("Solution.exist is still a stub; implement it when you are ready")
