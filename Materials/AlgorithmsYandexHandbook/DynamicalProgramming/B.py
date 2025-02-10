class Solution:
    def stonesGame(self, n: int, m: int) -> str:
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[i][j] = False
                    continue

                moves = [(i - 1, j), (i, j - 1), (i - 2, j), (i, j - 2),
                        (i - 1, j - 1), (i - 2, j - 2), (i - 1, j - 2)]

                dp[i][j] = any(0 <= ni <= n and 0 <= nj <= m and not dp[ni][nj] for ni, nj in moves)
        return "Win" if dp[n][m] else "Lose"

def test():
    solve = Solution()
    test_cases = [(4, 4), (17, 72), (7, 5)]
    result = [solve.stonesGame(n, m) for n, m in test_cases]
    print(result)

def main():
    solve = Solution()
    n, m = map(int, input().split())
    print(solve.stonesGame(n=n, m=m))

if __name__ == '__main__':
    test()
