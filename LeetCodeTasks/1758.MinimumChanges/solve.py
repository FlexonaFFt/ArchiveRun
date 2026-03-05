class Solution:
    def minOperations(self, s: str) -> int:
        misA, misB = 0, 0 
        for i, ch in enumerate(s):
            expA = '0' if i % 2 == 0 else '1'
            if ch != expA: misA += 1
            else: misB += 1
        return min(misA, misB)
