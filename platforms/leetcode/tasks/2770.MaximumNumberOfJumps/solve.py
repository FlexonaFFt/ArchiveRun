from typing import List
from functools import cache

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        answer = self.dfs(0)
        return -1 if answer < 0 else answer

    @cache
    def dfs(self, i: int) -> int:
        nums = self.nums
        target = self.target

        if i == len(nums) - 1:
            return 0

        output = float("-inf")
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) <= target:
                output = max(output, self.dfs(j) + 1)
        return output

