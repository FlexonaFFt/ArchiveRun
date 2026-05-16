class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            r = num % 3
            a, b, c = dp
            dp[(0 + r) % 3] = max(a + num, dp[(0 + r) % 3])
            dp[(1 + r) % 3] = max(b + num, dp[(1 + r) % 3])
            dp[(2 + r) % 3] = max(c + num, dp[(2 + r) % 3])
        return dp[0]
