class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = 0
        for x in range(len(nums)):
            counter += min(nums[x] % 3, 3 - nums[x] % 3)
        return counter
