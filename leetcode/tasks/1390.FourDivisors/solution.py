class Solution:
    def isPrime(self, n: int) -> bool:
        if n < 2: return False 
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: return False 
        return True
    
    def sumOne(self, n: int) -> int:
        p = round(n ** (1 / 3))
        if p ** 3 == n and self.isPrime(p):
            return 1 + p + p**2 + p**3

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                a, b = i, n // i
                if a != b and self.isPrime(a) and self.isPrime(b):
                    return 1 + a + b + n
                return -1
        return -1
    
    def sumFourDivisors(self, nums: list[int]) -> int:
        result = 0
        for n in nums:
            value = self.sumOne(n)
            if value != -1: result += value
        return result
