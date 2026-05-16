from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        counter, n = 0, len(nums)
        for i in range(n - 1):
            right, left = nums[:i+1], nums[i+1:]
            if (sum(left) - sum(right)) % 2 == 0:
                counter += 1
        return counter
