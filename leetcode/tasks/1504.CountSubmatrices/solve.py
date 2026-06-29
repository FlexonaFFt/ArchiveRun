class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_ones = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if j == 0:
                        row_ones[i][j] = 1
                    else:
                        row_ones[i][j] = row_ones[i][j-1] + 1

        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                min_width = row_ones[i][j]
                for k in range(i, -1, -1):
                    if row_ones[k][j] == 0:
                        break
                    min_width = min(min_width, row_ones[k][j])
                    res += min_width
        return res

