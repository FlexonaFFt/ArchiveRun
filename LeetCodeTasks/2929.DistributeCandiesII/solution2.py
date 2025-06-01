class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(limit, n) + 1):
            if n - i <= 2 * limit:
                res += min(n - i, limit) - max(0, n - i - limit) + 1
        return res


def test():
    solution = Solution()
    print(solution.distributeCandies(n=5, limit=2))
    print(solution.distributeCandies(n=3, limit=3))

if __name__ == '__main__':
    test()
