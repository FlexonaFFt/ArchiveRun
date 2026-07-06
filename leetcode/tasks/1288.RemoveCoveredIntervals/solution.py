from typing import List 

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        counter, max_r = 0, 0 

        for left, right in intervals:
            if right > max_r: 
                counter += 1
                max_r = right 

        return counter 
