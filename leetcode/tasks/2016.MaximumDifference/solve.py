class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        n, ans, premin = len(nums), -1, nums[0]
        for i in range(1, n):
            if nums[i] > premin:
                ans = max(ans, nums[i] - premin)
            else: premin = nums[i]
        return ans


def main():
    solve = Solution()
    print(solve.maximumDifference(nums=[7,1,5,4]))
    print(solve.maximumDifference(nums=[9,4,3,2]))

if __name__ == '__main__': main()
