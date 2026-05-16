class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        massive = [cell for row in grid for cell in row]
        massive.sort()

        mid, tc = len(massive) // 2, 0
        median = massive[mid]

        for value in massive:
            if abs(value - median) % x != 0:
                return -1
            tc += abs(value - median) // x

        return tc


def main():
    solve = Solution()
    print(solve.minOperations(grid=[[2,4],[6,8]], x=2))
    print(solve.minOperations(grid=[[1,5],[2,3]], x=1))
    print(solve.minOperations(grid=[[1,2],[3,4]], x=2))

main()
