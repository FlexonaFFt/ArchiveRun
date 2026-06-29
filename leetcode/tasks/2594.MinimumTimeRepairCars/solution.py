class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        import math
        left, right = 1, min(ranks) * cars * cars
        ans = right

        while left <= right:
            mid = (left + right) // 2
            total_cars = sum(math.floor(math.sqrt(mid // r)) for r in ranks)
            if total_cars >= cars:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

# Runtime 965 ms, 34 %
# Memory 21.90 mb, 49 %
def main():
    solve = Solution()
    print(solve.repairCars([4,2,3,1], 10))
    print(solve.repairCars([5,1,8], 6))

if __name__ == '__main__':
    main()
