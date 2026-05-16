class Solution:
    def min_changes(self, s: str) -> int:
        n = len(s)
        pattern_a = "tbank"
        pattern_b = "study"
        m = n - 4

        costs_a = [0] * m
        costs_b = [0] * m
        for i in range(m):
            a = 0
            b = 0
            for k in range(5):
                if s[i + k] != pattern_a[k]:
                    a += 1
                if s[i + k] != pattern_b[k]:
                    b += 1
            costs_a[i] = a
            costs_b[i] = b

        prefix_min = [0] * m
        cur = 10**9
        for i in range(m):
            if costs_b[i] < cur:
                cur = costs_b[i]
            prefix_min[i] = cur

        suffix_min = [0] * m
        cur = 10**9
        for i in range(m - 1, -1, -1):
            if costs_b[i] < cur:
                cur = costs_b[i]
            suffix_min[i] = cur

        ans = 10**9
        for i in range(m):
            if i - 5 >= 0:
                cand = costs_a[i] + prefix_min[i - 5]
                if cand < ans:
                    ans = cand
            if i + 5 < m:
                cand = costs_a[i] + suffix_min[i + 5]
                if cand < ans:
                    ans = cand

        return ans


if __name__ == "__main__":
    s = input().strip()
    solver = Solution()
    print(solver.min_changes(s))
