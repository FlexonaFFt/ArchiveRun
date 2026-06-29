from typing import List 

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = [] 

        for curr in nums:
            if ranges and ranges[-1][1] == curr - 1:
                ranges[-1][1] = curr 
            else: ranges.append([curr, curr])
        return [f"{x}->{y}" if x != y else f"{x}" for x, y in ranges]
