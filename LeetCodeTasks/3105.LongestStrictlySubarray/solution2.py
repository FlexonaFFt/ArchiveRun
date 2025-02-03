class Solution:
    from typing import List
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def longestIncreasing(nums):
            max_len, current_len = 1, 1
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    current_len += 1
                    max_len = max(max_len, current_len)
                else:
                    current_len = 1
            return max_len

        def longestDecreasing(nums):
            max_len = 1
            current_len = 1
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    current_len += 1
                    max_len = max(max_len, current_len)
                else:
                    current_len = 1
            return max_len

        return max(longestIncreasing(nums), longestDecreasing(nums))

# Runtime 0 ms, 100 %
# Memory 17.72 mb, 47.33 %
def main():
    solve = Solution()
    primer1 = [1,4,3,3,2]
    primer2 = [3,3,3,3]
    primer3 = [3,2,1]
    print(solve.longestMonotonicSubarray(primer1))
    print(solve.longestMonotonicSubarray(primer2))
    print(solve.longestMonotonicSubarray(primer3))

if __name__ == '__main__':
    main()
