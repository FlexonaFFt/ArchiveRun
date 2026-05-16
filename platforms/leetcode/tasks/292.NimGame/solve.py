class Solution:
    # Nim game LeetCode task
    def canWinNim(self, n: int) -> bool:
        return n % 4 == 0

# Runtime 3 ms, 0.98 %
# Memory 17.82 mb, 36 %

'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
'''
# Runtime 0 ms, 100 %
# Memory 17.78 mb, 57 %

def main():
    solution = Solution()
    print(solution.canWinNim(4))
    print(solution.canWinNim(1))
    print(solution.canWinNim(2))

if __name__ == '__main__':
    main()
