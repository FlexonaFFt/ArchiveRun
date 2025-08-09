import math 

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False 
        return math.log2(n).is_integer()


def test():
    solve = Solution()
    print(solve.isPowerOfTwo(n=1))
    print(solve.isPowerOfTwo(n=16))
    print(solve.isPowerOfTwo(n=3))

if __name__ == '__main__':
    test()
