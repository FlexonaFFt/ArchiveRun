class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else: i += 2
        return i == n - 1
