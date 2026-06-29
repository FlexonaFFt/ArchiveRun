class Solution:
    def maxPower(self, s: str) -> int:
        max_consecutive, current = 0, 1
        if len(s) == 1: return 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]: current += 1
            else: current = 1
            if current > max_consecutive: 
                max_consecutive = current
        return max_consecutive
