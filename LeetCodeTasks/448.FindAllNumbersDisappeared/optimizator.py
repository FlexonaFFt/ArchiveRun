class Solution:
    from typing import List
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result

# Runtime 40 ms, 34.48 %
# Memory 30 mb, 71.11 %
def main():
    solution = Solution()
    print(solution.findDisappearedNumbers(nums=[4,3,2,7,8,2,3,1]))
    print(solution.findDisappearedNumbers(nums=[1,1]))

if __name__ == '__main__':
    main()
