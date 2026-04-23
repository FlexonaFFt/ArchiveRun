from typing import List 

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        output, n = [], len(nums) 

        for idx, curr in enumerate(nums):
            
            current_res = 0
            for i in range(n):

                if i != idx and nums[i] == curr:
                    current_res += abs(idx - i)
            output.append(current_res)

        return output
