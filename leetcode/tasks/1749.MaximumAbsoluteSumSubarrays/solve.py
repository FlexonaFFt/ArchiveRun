from itertools import accumulate

class Solution:
    from typing import List
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(0, max(K:=list(accumulate(nums))))-min(0, min(K))


def main():
    solve = Solution()
    print(solve.maxAbsoluteSum([1,-3,2,3,-4]))
    print(solve.maxAbsoluteSum([2,-5,1,-4,3,-2]))

if __name__ == '__main__':
    main()
