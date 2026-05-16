class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if self.canRob(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return left


    def canRob(self, nums: list[int], k: int, capability: int) -> bool:
        count, i = 0, 0
        while i < len(nums):
            if nums[i] <= capability:
                count += 1
                i += 2
            else:
                i += 1
            if count >= k:
                return True
        return count >= k


# Runtime 370 ms, 39.79 %
# Memory 28.76 mb, 19.96 %
def main():
    solve = Solution()
    print(solve.minCapability([2,3,5,9], 2))
    print(solve.minCapability([2,7,9,3,1], 2))

if __name__ == '__main__':
    main()
