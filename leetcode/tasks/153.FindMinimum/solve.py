from typing import List 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        best, left, right = float('inf'), 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                best = min(best, nums[left])
                left = mid + 1
            else:
                best = min(best, nums[mid])
                right = mid - 1 

        return best
