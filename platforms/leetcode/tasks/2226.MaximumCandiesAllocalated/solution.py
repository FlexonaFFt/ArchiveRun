class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if k > sum(candies):
            return 0

        left, right, result = 1, max(candies), 0
        while left <= right:
            mid = (left + right) // 2
            child_count = sum(pile // mid for pile in candies)

            if child_count >= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result

# Runtime 437 ms, 32.75 %
# Memory 29.77 mb, 54 %
def main():
    solution = Solution()
    print(solution.maximumCandies(candies=[5,8,6], k=3))
    print(solution.maximumCandies(candies=[2,5], k=11))

if __name__ == '__main__':
    main()
