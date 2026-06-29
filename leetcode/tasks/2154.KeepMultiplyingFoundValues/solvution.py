class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        current = original
        while current in nums:
            current = current * 2
        return current

# Runtime 0 ms, 100 %
# Memory 17.93 mb, 35.42 %
