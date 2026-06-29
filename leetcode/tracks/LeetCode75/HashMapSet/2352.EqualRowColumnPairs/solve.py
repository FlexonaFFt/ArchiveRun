class Solution:
    from typing import List
    def equalPairs(self, grid: List[List[int]]) -> int:
        n, count = len(grid), 0
        for i in range(n):
            for j in range(n):
                if grid[i] == [grid[k][j] for k in range(n)]:
                    count += 1
        return count

# Runtime 2031 ms, 5.01 %
# Memory 21.92 mb, 47.67 %
def main():
    solve = Solution()
    grid1 = [[3,2,1],[1,7,6],[2,7,7]]
    grid2 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(solve.equalPairs(grid1))
    print(solve.equalPairs(grid2))

if __name__ == '__main__':
    main()
