class Solution:
    def max_area(self, s: str) -> int:
        n = len(s)
        if "1" not in s:
            return 0
        if "0" not in s:
            return n * n

        ss = s + s
        max_run = 0
        cur = 0
        for ch in ss:
            if ch == "1":
                cur += 1
                if cur > max_run:
                    max_run = cur
            else:
                cur = 0

        k = max_run + 1
        a = k // 2
        b = k - a
        return a * b


if __name__ == "__main__":
    t = int(input().strip())
    solver = Solution()
    for _ in range(t):
        s = input().strip()
        print(solver.max_area(s))
