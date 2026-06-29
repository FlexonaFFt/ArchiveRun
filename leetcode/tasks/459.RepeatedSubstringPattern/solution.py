class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled_s = (s + s)[1:-1]
        return s in doubled_s

# Runtime 0 ms, 100 %
# Memory 17.72 mb, 76.12 %
def main():
    solve = Solution()
    print(solve.repeatedSubstringPattern('abab'))
    print(solve.repeatedSubstringPattern('aba'))
    print(solve.repeatedSubstringPattern('abcabcabcabc'))

if __name__ == '__main__':
    main()
