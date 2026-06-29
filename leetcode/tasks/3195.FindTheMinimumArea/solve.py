class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        min_row, max_row = float('inf'), float('-inf')
        min_col, max_col = float('inf'), float('-inf')

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        return (max_row - min_row + 1) * (max_col - min_col + 1)

def test():
    solve = Solution()
    print(solve.minimumArea([[0,1,0],[1,0,1]]))
    print(solve.minimumArea([[1,0],[0,0]]))


if __name__ == '__main__':
    test()
