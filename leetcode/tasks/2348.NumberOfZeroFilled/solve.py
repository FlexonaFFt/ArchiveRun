class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        streak = ans = 0
        for element in nums:
            if element == 0:
                streak += 1
                ans += streak
            else: streak = 0

        return ans 


def test():
    solve = Solution()
    print(solve.zeroFilledSubarray(nums=[1,3,0,0,2,0,0,4]))
    print(solve.zeroFilledSubarray(nums=[0,0,0,2,0,0]))


if __name__ == '__main__':
    test()
