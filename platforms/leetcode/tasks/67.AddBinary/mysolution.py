class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int, b_int = int(a, 2), int(b, 2)
        return bin(a_int + b_int)[2:]
