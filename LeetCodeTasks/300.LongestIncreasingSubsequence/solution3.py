class Solution:
    from typing import List
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = []
        for num in nums:
            pos = self.binary_search(dp, num)
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
        return len(dp)

    def binary_search(self, dp: List[int], target: int) -> int:
        left, right = 0, len(dp) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if dp[mid] == target:
                return mid
            elif dp[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Runtime 13 ms, 75 %
# Memory 18.04 mb, 54.56 %
def main():
    solution = Solution()
    print(solution.lengthOfLIS(nums=[10,9,2,5,3,7,101,18]))
    print(solution.lengthOfLIS(nums=[0,1,0,3,2,3]))
    print(solution.lengthOfLIS(nums=[7,7,7,7,7,7,7]))
    print(solution.lengthOfLIS(nums=[1,3,6,7,9,4,10,5,6]))
    print(solution.lengthOfLIS(nums=[0,1,0,3,2,3]))

if __name__ == '__main__':
    main()
