class Solution:
    def coloredCells(self, n: int) -> int:
        add, bluecells = 4, 1
        while n - 1:
            bluecells += add
            add += 4
            n -= 1
        return bluecells

# Runtime 190 ms, 14.66 %
# Memory 17.84 mb, 30.45 %
def main():
    solve = Solution()
    print(solve.coloredCells(n=1))
    print(solve.coloredCells(n=2))
    print(solve.coloredCells(n=3))

if __name__ == '__main__':
    main()
