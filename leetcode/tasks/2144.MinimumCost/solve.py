class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        value = 0 

        for idx, price in enumerate(cost): 
            if idx % 3 != 2: value += price 
        return value
