from typing import List 

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = nums[k - 1] - nums[0]
        for i in range(len(nums) - k + 1):
            answer = min(answer, nums[i + k - 1] - nums[i])

        return answer 
