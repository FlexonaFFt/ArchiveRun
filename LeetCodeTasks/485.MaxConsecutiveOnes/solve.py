class Solution:
    from typing import List
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx, counter = 0, 0
        for element in nums:
            if element == 1:
                counter += 1
            if element == 0:
                counter = 0
            if mx < counter:
                mx = counter
        return mx


# Runtime 11 ms, 86.53 %
# Memory 20.15 mb, 57 %
def main():
    solution = Solution()
    print(solution.findMaxConsecutiveOnes(nums=[1,1,0,1,1,1]))
    print(solution.findMaxConsecutiveOnes(nums=[1,0,1,1,0,1]))

if __name__ == '__main__':
    main()
