class Solution:
    def climbingStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev1, prev2 = 1, 2
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        return prev2

# Runtime 0 ms, 100 %
# Memory 17.96 mb, 6.69 %
def main():
    solve = Solution()
    print(solve.climbingStairs(2))
    print(solve.climbingStairs(3))
    print(solve.climbingStairs(5))
    print(solve.climbingStairs(10))
    print(solve.climbingStairs(256))

if __name__ == '__main__':
    main()
