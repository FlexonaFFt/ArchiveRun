class Solution:
    def removeOccurences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s

# Runtime 0 ms, 100 %
# Memory 17.72 mb, 75.36 %
def main():
    solve = Solution()
    print(solve.removeOccurences(s="daabcbaabcbc", part='abc'))
    print(solve.removeOccurences(s='axxxxyyyyb', part='xy'))

if __name__ == '__main__':
    main()
