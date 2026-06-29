'''class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        maxDiff = 0
        for i in range(len(nums) - 1):
            if i == len(nums) - 1:
                if nums[i] > nums[0]: result = nums[i] - nums[0]
                else: result = nums[0] - nums[i]
            else:
                if nums[i] > nums[i + 1]: result = nums[i] - nums[i + 1]
                else: result = nums[i + 1] - nums[i]
            if maxDiff < result: maxDiff = result
        return maxDiff'''


class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        maxDiff, lres, rres = 0, 0, 0
        nums.append(nums[0])
        nums.insert(0, nums[len(nums) - 1])

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]: rres = nums[i] - nums[i + 1]
            if nums[i] < nums[i + 1]: rres = nums[i + 1] - nums[i]
            if nums[i] > nums[i - 1]: lres = nums[i] - nums[i - 1]
            if nums[i] < nums[i - 1]: lres = nums[i - 1] - nums[i]

        maxDiff = max(maxDiff, lres, rres)
        return maxDiff

# WA 426
def main():
    solve = Solution()
    print(solve.maxAdjacentDistance(nums=[1,2,4]))
    print(solve.maxAdjacentDistance(nums=[-5,-10,-5]))

if __name__ == '__main__': main()
