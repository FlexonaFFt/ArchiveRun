# Runtime 178 ms, 42.89%
# Memory 19.65 mb, 14.21 %
class Solution:
    def numberisPrime(self, num: int) -> bool:
        if num < 2: return False 
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                return False 
        return True 
    
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primeCounter = 0
        for curr in range(left, right + 1):
            bitwize = bin(curr)[2:]
            counter = bitwize.count('1')
            if self.numberisPrime(counter):
                primeCounter += 1
        return primeCounter