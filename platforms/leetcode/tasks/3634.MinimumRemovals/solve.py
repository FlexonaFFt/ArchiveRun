from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        best, i = 1, 0
        for j in range(n):
            while i <= j and nums[j] > k * nums[i]:
                i += 1
            best = max(best, j - i + 1)
        return n - best
