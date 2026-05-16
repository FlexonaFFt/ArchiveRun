class Solution:
    def maxSum(self, nums: list[int]) -> int:
        positiveNumsSet = set([num for num in nums if num > 0])
        return max(nums) if len(positiveNumsSet) == 0 else sum(positiveNumsSet)


def test():
    solve = Solution()
    print(solve.maxSum([1,2,3,4,5]))
    print(solve.maxSum([1,1,0,1,1]))
    print(solve.maxSum([1,2,-1,-2,1,0,-1]))
    print(solve.maxSum([-20, 20]))
    print(solve.maxSum([-100]))

if __name__ == '__main__':
    test()
