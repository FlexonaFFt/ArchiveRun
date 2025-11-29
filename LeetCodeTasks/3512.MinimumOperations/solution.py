from typing import List 

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        summa = sum(nums)
        while summa % k != 0:
            summa -= 1
            counter += 1
        return counter
