class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nums = [x for x in str(n) if x != '0']
        if not nums: return 0
        return int(''.join(nums)) * sum(int(x) for x in nums) 
