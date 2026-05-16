class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for i in range(0, n - length):
                j = i + length
                best = float('inf')

                for k in range(i + 1, j):
                    triangle_cost = values[i] * values[k] * values[j]
                    total_cost = dp[i][k] + dp[k][j] + triangle_cost
                    if total_cost < best: best = total_cost
                dp[i][j] = best

        return dp[0][n - 1]
