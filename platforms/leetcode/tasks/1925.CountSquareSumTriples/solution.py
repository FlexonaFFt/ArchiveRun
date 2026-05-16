class Solution:
    def countTriples(self, n: int) -> int:
        import math
        counter = 0
        for a in range(1, n + 1):
            a2 = a ** 2
            for b in range(1, n + 1):
                s = a2 + b ** 2
                c = math.isqrt(s)
                if c <= n and c ** 2 == s: counter += 1
        return counter
