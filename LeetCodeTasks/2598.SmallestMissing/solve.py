from collections import Counter 

class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        mp, mex = Counter(x % value for x in nums), 0
        while mp[mex % value] > 0:
            mp[mex % value] -= 1
            mex += 1
        return mex
