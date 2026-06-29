class Solution:
    def triangleType(self, nums: list[int]) -> str:
        nums.sort()
        if len(nums) < 3:
            return 'none'

        if nums[0] + nums[1] <= nums[2]:
            return 'none'

        if nums[0] == nums[1] == nums[2]:
            return 'equilateral'

        if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return 'isosceles'

        if nums[0] != nums[1] != nums[2]:
            return 'scalene'

# Runtime 0 ms, 100 %
# Memory 17.64 mb, 80.27 %
def test():
    solution = Solution()
    print(solution.triangleType(nums=[3,3,3]))
    print(solution.triangleType(nums=[3,4,5]))

if __name__ == '__main__':
    test()
