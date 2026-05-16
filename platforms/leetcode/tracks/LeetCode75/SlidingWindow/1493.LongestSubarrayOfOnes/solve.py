class Solution:
    from typing import List
    def longestSubarray(self, nums: List[int]) -> int:
        left, maxLength, zeroCount = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxLength = max(maxLength, right - left)
        return maxLength

# Runtime 56 ms, 66.06 %
# Memory 21.89 mb, 19.58 %
def main():
    nums, nums3 = [1,1,0,1], [1,1,1]
    nums2 = [0,1,1,1,0,1,1,0,1]
    solution = Solution()
    print(solution.longestSubarray(nums))
    print(solution.longestSubarray(nums2))
    print(solution.longestSubarray(nums3))

if __name__ == '__main__':
    main()
