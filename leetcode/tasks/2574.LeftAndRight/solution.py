from typing import List 

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * n 

        left_sum, right_sum = 0, 0
        for i in range(n):
            out[i] = left_sum
            left_sum += nums[i]

        for i in range(n - 1, -1, -1):
            out[i] = abs(out[i] - right_sum)
            right_sum += nums[i]

        return out
