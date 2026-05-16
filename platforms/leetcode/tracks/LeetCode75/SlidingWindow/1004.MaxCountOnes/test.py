class Solution:
    def longestOnes(self, nums, k):
        left, maxLength, zeroCount = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength

# Runtime 70 ms, 39.69 %
# Memory 18.28 mb, 46.57 %
def main():
    nums, k = [1,1,1,0,0,0,1,1,1,1,0], 2
    nums2, k2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3
    solution = Solution()
    print(solution.longestOnes(nums, k))
    print(solution.longestOnes(nums2, k2))

if __name__ == '__main__':
    main()
