from typing import List 

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)
        n = nums_sorted[-1]         

        if len(nums_sorted) != n + 1:
            return False

        base_n = list(range(1, n)) + [n, n]
        return nums_sorted == base_n
