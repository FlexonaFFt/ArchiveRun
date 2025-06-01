class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(x):
            if x < 0: return 0
            return (x + 2) * (x + 1) // 2

        if 3 * limit < n: return 0
        if limit >= n: return comb(n)

        total = comb(n)
        case1 = 3 * comb(n - (limit + 1))
        case2 = 3 * comb(n - 2 * (limit + 1))
        case3 = comb(n - 3 * (limit + 1))
        return total - case1 - case2 - case3

# WA 891 test
def test():
    solution = Solution()
    print(solution.distributeCandies(n=5, limit=2))
    print(solution.distributeCandies(n=3, limit=3))

if __name__ == '__main__':
    test()
