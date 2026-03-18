from leetcode.testing import TestCase

TEST_CASES = [
    TestCase(
        name="example_1",
        input={"nums": [2, 7, 11, 15], "target": 9},
        expected=[0, 1],
        method="two_sum",
        description="Classic LeetCode example.",
    ),
    TestCase(
        name="example_2",
        input={"nums": [3, 2, 4], "target": 6},
        expected=[1, 2],
        method="two_sum",
        description="Uses values discovered after the first index.",
    ),
    TestCase(
        name="negative_numbers",
        input={"nums": [-3, 4, 3, 90], "target": 0},
        expected=[0, 2],
        method="two_sum",
        description="Verifies behavior when the answer includes a negative number.",
    ),
]
