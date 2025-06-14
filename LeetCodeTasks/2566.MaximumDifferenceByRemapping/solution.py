class Solution:
    def minMaxDifference(self, num: int) -> int:
        string = str(num)
        t, pos = string, 0
        while pos < len(string) and string[pos] == '9':
            pos += 1
        if pos < len(string): string = string.replace(string[pos], "9")
        t = t.replace(t[0], "0")
        return int(string) - int(t)

# Runtime 0 ms, 100 %
# Memory 17.73 mb, 45.89 %
def test():
    solve = Solution()
    print(solve.minMaxDifference(num=11891))
    print(solve.minMaxDifference(num=90))

if __name__ == '__main__': test()
