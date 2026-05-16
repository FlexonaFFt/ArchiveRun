import math 

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False 
        log_val = math.log(n, 4)
        return log_val.is_integer()

# Runtimr 0 ms, 100 %
# Memory 18.08 mb, 18.57 %
if __name__ == '__main__':
    solve = Solution()
    print(solve.isPowerOfFour(n=16))
    print(solve.isPowerOfFour(n=5))
    print(solve.isPowerOfFour(n=1))
