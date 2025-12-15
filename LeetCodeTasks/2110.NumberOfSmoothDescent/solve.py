from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n, counter, run_len = len(prices), 0, 1
        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1: run_len += 1
            else: run_len = 1
            counter += run_len
        return counter + 1

