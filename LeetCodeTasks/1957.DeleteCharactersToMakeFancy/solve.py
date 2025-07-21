class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for char in s:
            if len(res) >= 2 and res[-1] == res[-2] == char:
                continue
            res.append(char)
        return ''.join(res)


def test():
    solve = Solution()
    print(solve.makeFancyString(s="leeetcode"))
    print(solve.makeFancyString(s="aaabaaaa"))
    print(solve.makeFancyString(s="aab"))

if __name__ == '__main__':
    test()
