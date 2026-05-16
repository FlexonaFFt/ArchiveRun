class Solution:
    from typing import List
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        row_servers = [0] * rows
        col_servers = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_servers[i] += 1
                    col_servers[j] += 1

        servers_counter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_servers[i] > 1
                    or col_servers[j] > 1):
                    servers_counter += 1
        return servers_counter

# Runtime 16 ms, 66.67 %
# Memory 19.52 mb, 60.67 %
def main():
    grid1 = [[1, 0], [0, 1]]
    grid2 = [[1, 0], [1, 1]]
    solution = Solution()
    print(solution.countServers(grid1))
    print(solution.countServers(grid2))

if __name__ == '__main__':
    main()
