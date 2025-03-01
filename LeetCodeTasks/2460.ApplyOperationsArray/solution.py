class Solution:
    from typing import List
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] and nums[i + 1] is not None:
                nums[i], nums[i + 1] = nums[i] * 2, 0
        for element in nums:
            if element == 0:
                nums.remove(element)
                nums.append(element)
        return nums

# Runtime 19 ms, 9.17 %
# Memory 17.95 mb, 46.47 %
def main():
    solution = Solution()
    print(solution.applyOperations(nums=[1,2,2,1,1,0]))
    print(solution.applyOperations(nums=[0,1]))

if __name__ == "__main__":
    main()
