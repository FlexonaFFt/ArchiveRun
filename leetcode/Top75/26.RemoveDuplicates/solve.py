from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0 

        for curr in range(1, len(nums)):
            if nums[cnt] != nums[curr]:
                cnt += 1
                nums[cnt] = nums[curr]

        return cnt + 1
