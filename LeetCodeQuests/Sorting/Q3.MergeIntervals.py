from typing import List 

class Solution:
    def sort_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        return sorted(intervals, key=lambda x: (x[0], x[1]))
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = self.sort_intervals(intervals)
        current_start, current_end = sorted_intervals[0][0], sorted_intervals[0][1]
        merged: List[List[int]] = []

        for i in range(1, len(sorted_intervals)):
            s, e = sorted_intervals[i]

            if s <= current_end:
                if e > current_end: current_end = e
            
            else:
                merged.append([current_start, current_end])
                current_start, current_end = s, e

        merged.append([current_start, current_end])
        return merged
