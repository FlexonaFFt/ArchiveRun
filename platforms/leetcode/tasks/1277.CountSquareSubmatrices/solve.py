class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        dp, total = [[0] * n for _ in range(m)], 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0: dp[i][j] = 1
                    else:
                        dp[i][j] = min(
                                dp[i-1][j],
                                dp[i][j-1],
                                dp[i-1][j-1]
                                ) + 1
                    total += dp[i][j]

        return total 


def test():
    solve = Solution()
    print(solve.countSquares(matrix=[[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
    print(solve.countSquares(matrix=[[1,0,1],[1,1,0],[1,1,0]]))

if __name__ == '__main__':
    test()
