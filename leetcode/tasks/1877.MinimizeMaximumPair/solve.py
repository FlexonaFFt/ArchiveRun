from typing import List 

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output = 0

        for i in range(len(nums) // 2):
            output = max(output, nums[i] + nums[-1 - i])

        return output
