class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        ans = 1
        for val in range(k):
            dp = [0] * k 
            for x in nums:
                m = x % k
                want = (val - m) % k 
                dp[m] = max(dp[m], dp[want] + 1, 1)
                ans = max(ans, dp[m])

        return ans 
