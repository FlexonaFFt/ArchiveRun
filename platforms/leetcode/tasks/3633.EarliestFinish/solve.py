from typing import List 

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        left, right, res = float('inf'), float('inf'), float('inf')
        n, m = len(landStartTime), len(waterStartTime)

        for i in range(n):
            left = min(left, landStartTime[i] + landDuration[i])
        
        for i in range(m):
            right = min(right, waterStartTime[i] + waterDuration[i])
            res = min(res, max(left, waterStartTime[i]) + waterDuration[i])

        for i in range(n):
            res = min(res, max(right, landStartTime[i]) + landDuration[i])
        return res 
