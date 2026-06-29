class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        n, res, current = len(s), [], 0
        while current < n:
            res.append(s[current:current + k])
            current += k
        res[-1] += fill * (k - len(res[-1]))
        return res 


def test():
    solve = Solution()
    print(solve.divideString("abcdefghi", 3, "x"))
    print(solve.divideString("abcdefghij", 3, "x"))

if __name__ == '__main__': test()
