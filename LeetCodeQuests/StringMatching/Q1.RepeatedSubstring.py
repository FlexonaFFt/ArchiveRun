class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        if length <= 1: return False

        for k in range(1, length // 2 + 1):
            if length % k != 0: continue
            pattern, repeats = s[:k], length // k

            if pattern * repeats == s: return True 
        return False 
