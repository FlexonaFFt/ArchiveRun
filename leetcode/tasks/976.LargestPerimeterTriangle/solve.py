from typing import List 

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for x,y,z in zip(nums, nums[1:], nums[2:]):
            if x < y + z: return x + y + z
        return 0
