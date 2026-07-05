class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n + 1)

        if n >= 3: 
            dp[0], dp[1], dp[2] = 0, 1, 1
            for i in range(3, n + 1):
                dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1] 
            return dp[n]

        elif n == 2: return 1
        elif n == 1 or n == 0: return n
