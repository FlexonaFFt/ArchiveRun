from typing import List 

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0 
        for c in cost: 
            a, b = b, c + min(a, b)

        return min(a, b)
