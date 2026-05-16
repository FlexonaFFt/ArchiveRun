class Solution:
    def min_rounds_for_each(self, a: list[int]) -> list[int]:
        n = len(a)
        max_val = max(a)
        counts = [0] * (max_val + 1)
        good = [False] * (max_val + 1)

        for x in a:
            counts[x] += 1

        for i in range(n):
            x = a[i]
            y = a[(i + 1) % n]
            z = a[(i + 2) % n]
            mn = min(x, y, z)
            mx = max(x, y, z)
            good[mn] = True
            good[mx] = True

        res = []
        for x in a:
            extra = 0 if good[x] else 1
            res.append(n - counts[x] + extra)
        return res


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().split()))
    solver = Solution()
    ans = solver.min_rounds_for_each(a)
    print(" ".join(map(str, ans)))
