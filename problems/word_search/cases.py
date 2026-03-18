from leetcode.testing import TestCase

TEST_CASES = [
    TestCase(
        name="example_abcced",
        input={
            "board": [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "word": "ABCCED",
        },
        expected=True,
        method="exist",
        description=(
            "Target case: the word ABCCED should be found by walking through "
            "adjacent cells without reusing a cell."
        ),
        metadata={
            "problem": "Word Search",
            "source": "LeetCode 79",
        },
    ),
]
