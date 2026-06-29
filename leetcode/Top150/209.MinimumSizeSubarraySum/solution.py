from typing import List 

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, best, current = 0, float('inf'), 0

        for right, value in enumerate(nums):
            current += value 

            while current >= target:
                best = min(best, right - left + 1)
                current -= nums[left]
                left += 1

        return 0 if best == float('inf') else best 
