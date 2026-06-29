from typing import List 

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counter = 0
        costs.sort()
        for curr in costs:
            if curr <= coins:
                counter += 1
                coins -= curr 

            else: return counter 

        return counter
