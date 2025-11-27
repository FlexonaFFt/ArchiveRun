from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
    
        best_min = [10**19] * k
        best_min[0], prefix, answer = 0, 0, -10**19

        for i, value in enumerate(nums, start=1):
            prefix += value
            rem = i % k
            candidate = prefix - best_min[rem]
            if candidate > answer: answer = candidate
            if prefix < best_min[rem]: best_min[rem] = prefix

        return answer
