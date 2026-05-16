class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
