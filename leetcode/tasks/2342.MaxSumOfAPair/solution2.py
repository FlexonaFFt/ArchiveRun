class Solution:
    from typing import List
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(x):
            return sum(int(char) for char in str(x))

        maxSum, sumDict = -1, {}
        for num in nums:
            currentSum = digitSum(num)
            if currentSum in sumDict:
                maxSum = max(maxSum, sumDict[currentSum] + num)
                if num > sumDict[currentSum]:
                    sumDict[currentSum] = num
            else:
                sumDict[currentSum] = num
        return maxSum

# Runtime 558 ms, 17.20 %
# Memory 34.02 mb, 8.34 %
def main():
    solution = Solution()
    print(solution.maximumSum(nums=[18,43,36,13,7]))
    print(solution.maximumSum(nums=[10,12,19,14]))

if __name__ == '__main__':
    main()
