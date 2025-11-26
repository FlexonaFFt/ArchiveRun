from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = levels = 0
        n = len(nums)
        nums.sort()

        for i in range(1, n):
            if nums[i] != nums[i - 1]: levels += 1
            counter += levels

        return counter
