class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = high - low + 1
        base = n // 2
        return base + (n % 2 and (low % 2 == 1 or high % 2 == 1))
