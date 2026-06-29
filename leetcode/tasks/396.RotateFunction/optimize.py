from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        func, n, summa = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            func += i * num
        
        res = func
        for i in range(n - 1, 0, -1):
            func = func + summa - n * nums[i]
            res = max(res, func)
        return res
