class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


def test():
    solve = Solution()
    print(solve.strStr("sadbutsad", "sad"))
    print(solve.strStr("leetcode", "leeto"))


if __name__ == '__main__': test()
