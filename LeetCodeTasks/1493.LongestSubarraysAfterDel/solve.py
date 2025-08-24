class Solution:
    def longestSubarrays(self, nums: list[int]) -> int:
        left = zeros = res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1 

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            res = max(res, right - left)

        return res

if __name__ == '__main__':
    solve = Solution()
    print(solve.longestSubarrays([1,1,0,1]))
    print(solve.longestSubarrays([0,1,1,1,0,1,1,0,1]))
    print(solve.longestSubarrays([1,1,1]))
