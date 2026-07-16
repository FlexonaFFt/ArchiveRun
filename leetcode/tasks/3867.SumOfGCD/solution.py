import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maximum, out, length = 0, 0, len(nums)

        for i in range(length):
            maximum = max(maximum, nums[i])
            nums[i] = math.gcd(nums[i], maximum)
        nums.sort()

        for i in range(length // 2):
            out += math.gcd(nums[i], nums[~i])

        return out
