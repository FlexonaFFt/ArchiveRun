class Solution:
    from typing import List
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maxElement, resultArr = max(nums), []
        for i in range(1, maxElement):
            if i not in nums:
                resultArr.append(i)
        return resultArr


def main():
    solution = Solution()
    print(solution.findDisappearedNumbers(nums=[4,3,2,7,8,2,3,1]))
    print(solution.findDisappearedNumbers(nums=[1,1]))

if __name__ == '__main__':
    main()
