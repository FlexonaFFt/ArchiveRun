from typing import List 
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n 

        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)

        for indices in groups.values():
            m = len(indices)
            if m == 1: continue 

            prefix = [0] * m
            prefix[0] = indices[0]
            for i in range(1, m):
                prefix[i] = prefix[i - 1] + indices[i]
            
            total_sum = prefix[-1]
            
            for k, idx in enumerate(indices):

                if k == 0:
                    left = 0
                else:
                    left = idx * k - prefix[k - 1]
                
                right_count = m - 1 - k
                if right_count == 0:
                    right = 0
                else:
                    right_sum = total_sum - prefix[k]
                    right = right_sum - idx * right_count
                
                res[idx] = left + right
        
        return res
