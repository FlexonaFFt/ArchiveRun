class Solution:
    def reverse(self, n: int) -> int:
        string_number = str(n)
        return int(string_number[::-1])

    
    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))
