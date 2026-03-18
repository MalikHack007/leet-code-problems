class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], index]
            seen[value] = index

        raise ValueError("No solution found for the provided input")
