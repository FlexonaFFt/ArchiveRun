class Solution:
    def minPair(self, v: list[int]) -> int:
        min_sum = 10**9
        pos = -1
        for i in range(len(v) - 1):
            if v[i] + v[i + 1] < min_sum:
                min_sum = v[i] + v[i + 1]
                pos = i
        return pos

    def mergePair(self, nums: list[int], pos: int) -> None:
        nums[pos] += nums[pos + 1]
        del nums[pos + 1]

    def minimumPairRemoval(self, nums: list[int]) -> int:
        ops = 0 
        while nums != sorted(nums):
            self.mergePair(nums, self.minPair(nums))
            ops += 1
        return ops 
