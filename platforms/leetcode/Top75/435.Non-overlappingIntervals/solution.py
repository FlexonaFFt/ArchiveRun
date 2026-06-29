from typing import List 

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # Сортирую интервалы по end 
        intervals.sort(key=lambda k: k[1])
        removed, last = 0, intervals[0][1]

        # Смотрим на интервалы
        for start, end in intervals[1:]:
            if start >= last: last = end 
            else: removed += 1

        return removed
