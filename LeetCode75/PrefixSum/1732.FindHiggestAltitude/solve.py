class Solution:
    from typing import List
    def largestAltitude(self, nums: List[int]) -> int:
        currentValue, answerList, maxElement = 0, [0], 0
        for element in nums:
            currentValue += element
            answerList.append(currentValue)
            maxElement = max(maxElement, currentValue)
        return maxElement

# Runtime 4 ms, 2.52 %
# Memory 17.71 mb, 31.54 %
def main():
    nums = [-5,1,5,0,-7]
    nums1 = [-4,-3,-2,-1,4,3,2]
    solution = Solution()
    print(solution.largestAltitude(nums))
    print(solution.largestAltitude(nums1))

if __name__ == '__main__':
    main()
