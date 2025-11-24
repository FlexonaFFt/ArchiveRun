class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in counter:
                return [counter[complement], i]
            counter[x] = i
