class Solution:
    def reverseBits(self, n: int) -> int:
        bits = format(n, '032b')
        reverse = bits[::-1]
        return int(reverse, 2)
