class Solution:
    def main(self, n, m, s, t, i, d, sb) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for ii in range(n + 1): dp[ii][0] = ii * d
        for jj in range(m + 1): dp[0][jj] = jj * i
        for ii in range(1, n + 1):
            for jj in range(1, m + 1):
                cost = 0 if s[ii - 1] == t[jj - 1] else sb
                dp[ii][jj] = min(
                    dp[ii - 1][jj] + d,
                    dp[ii][jj - 1] + i,
                    dp[ii - 1][jj - 1] + cost,
                )

        return dp[n][m]

    def func(self) -> None:
        n, m = map(int, input().split())
        s = str(input().strip())
        t = str(input().strip())
        i, d, sb = map(int, input().split())
        print(self.main(n, m, s, t, i, d, sb))


if __name__ == '__main__':
    Solution().func()
