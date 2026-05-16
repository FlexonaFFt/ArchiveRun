class Solution:
    def sumZero(self, n: int) -> list[int]:
        answer = []
        for num in range(1, n // 2 + 1):
            answer.append(num)
            answer.append(-num)
        
        if n % 2 == 1:
            answer.append(0)
        
        return sorted(answer)
        
# Runtime 0 ms, 100 %
# Memory 17.67 mb, 97.57 %
def test():
    solve = Solution()
    print(solve.sumZero(n=5))
    print(solve.sumZero(n=3))
    print(solve.sumZero(n=0))
    
if __name__ == '__main__':
    test()