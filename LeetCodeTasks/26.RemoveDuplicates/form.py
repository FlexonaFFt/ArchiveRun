from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_pointer = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_pointer]:
                unique_pointer += 1
                nums[unique_pointer] = nums[i]

        return unique_pointer + 1

solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = solution.removeDuplicates(nums)
print(f"k = {k}, nums = {nums[:k] + ['_'] * (len(nums) - k)}")
