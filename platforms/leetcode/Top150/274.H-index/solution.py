from typing import List 

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        status = 0 

        for i in range(len(citations)):
            if citations[i] >= status + 1: status += 1
            else: return status
        return status
