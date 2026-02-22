class Solution:
    def binaryGap(self, n: int) -> int:
        last, max_gap, pos = -1, 0, 0

        while n > 0:
            if n & 1:
                if last != -1:
                    max_gap = max(max_gap, pos - last)
                last = pos 
            n >>= 1
            pos += 1
        
        return max_gap
