class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        main = 0
        while len(nums) > 0:
            if len(set(nums)) == len(nums):
                break
            nums = nums[3:]
            main += 1
        return main


def main():
    solution = Solution()
    print(solution.minimumOperations(nums=[1,2,3,4,2,3,3,5,7]))
    print(solution.minimumOperations(nums=[4,5,6,4,4]))
    print(solution.minimumOperations(nums=[6,7,8,9]))

main()
