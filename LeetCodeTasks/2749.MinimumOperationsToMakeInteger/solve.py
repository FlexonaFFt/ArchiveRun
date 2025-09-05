class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_length():
                return k
        return -1
        
def test():
    solve = Solution()
    print(solve.makeTheIntegerZero(num1=3, num2=-2))
    
if __name__ == '__main__':
    test()