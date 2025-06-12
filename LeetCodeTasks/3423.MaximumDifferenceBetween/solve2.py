class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        diff = abs(nums[-1] - nums[0])
        for i in range(1, len(nums)):
            diff = max(diff, abs(nums[i] - nums[i - 1]))
        return diff

# Runtime 0 ms, 100 %
# Memory 17.87 mb, 29.16 %
def main():
    solve = Solution()
    print(solve.maxAdjacentDistance(nums=[1,2,4]))
    print(solve.maxAdjacentDistance(nums=[-5,-10,-5]))

if __name__ == '__main__': main()
