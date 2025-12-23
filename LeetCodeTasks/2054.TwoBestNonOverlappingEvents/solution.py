from typing import List 

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sorted_by_start = sorted_by_end = events
        sorted_by_start.sort(key=lambda e: e[0])
        sorted_by_end.sort(key=lambda e: e[1])

        j, maxVal, answer, n = 0, 0, 0, len(events)
        for event in sorted_by_start:
            s = event[0]
            e = event[1]
            v = event[2]

            while j < n and sorted_by_end[j][1] < s:
                maxVal = max(maxVal, sorted_by_end[j][2])
                j += 1
            
            answer = max(answer, v)
            answer = max(answer, v + maxVal)

        return answer
