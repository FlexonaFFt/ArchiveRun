import math

class Solution:
    def findSquares(self, n: int):
        for a in range(int(math.sqrt(n)) + 1):
            bs = n - a ** 2
            b = math.isqrt(bs)
            if b ** 2 == bs:
                return a, b
        return "NO"


def main():
    solve = Solution()
    n = int(input())
    res = solve.findSquares(n=n)
    if res == 'NO':
        print(res)
    else:
        a, b = res
        print(a, b)

if __name__ == '__main__':
    main()
