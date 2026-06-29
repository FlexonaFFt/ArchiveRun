class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        counter, repeated = 1, a
        if set(b) - set(a): return -1
        while len(repeated) < len(b):
            repeated += a
            counter += 1
        for _ in range(3):
            if b in repeated: return counter
            repeated += a
            counter += 1
        return -1
