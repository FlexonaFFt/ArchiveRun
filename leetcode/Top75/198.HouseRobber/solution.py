from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for money in nums: prev2, prev1 = prev1, max(prev1, prev2 + money)
        return prev1

class SecondSolution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[-1]


if __name__ == '__main__':
    print(Solution().rob([1,2,3,1]))
    print(Solution().rob([2,7,9,3,1]))
