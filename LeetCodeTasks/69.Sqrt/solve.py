class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 0, x
        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result

# Runtime 4 ms, 41 %
# Memory 17.58 mb, 78 %
def main():
    x1, x2, x3 = 4, 8, 9
    solve = Solution()
    print(solve.mySqrt(x1))
    print(solve.mySqrt(x2))
    print(solve.mySqrt(x3))

if __name__ == '__main__':
    main()
