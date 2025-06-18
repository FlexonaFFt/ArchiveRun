class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        peremeter, cols, rows = 0, len(grid), len(grid[0])
        for i in range(cols):
            for j in range(rows):
                if grid[i][j] == 1:
                    peremeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        peremeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        peremeter -= 2
        return peremeter

# Rutime 33 ms, 75.97 %
# Memory 18.34 mb, 56.27 %
def main():
    solve = Solution()
    print(solve.islandPerimeter(grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(solve.islandPerimeter(grid=[[1,0]]))
    print(solve.islandPerimeter(grid=[[1]]))

if __name__ == '__main__': main()
