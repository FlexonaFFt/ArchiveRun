class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.isqrt(c)) + 1):
            b2 = c - a*a
            b = int(math.isqrt(b2))
            if b*b == b2:
                return True
        return False
