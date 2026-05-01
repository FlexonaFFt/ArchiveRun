from typing import List 

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        def calc_k(k: int) -> int:
            return sum(i * nums[(i - k) % n] for i in range(n))

        max_f = float("-inf")
        for k in range(n):
            max_f = max(max_f, calc_k(k))

        return max_f
