from bisect import bisect_left
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m, result = len(potions), []

        for spell in spells:
            threshold = (success + spell - 1) // spell
            idx = bisect_left(potions, threshold)
            count = m - idx 
            result.append(count)

        return result
