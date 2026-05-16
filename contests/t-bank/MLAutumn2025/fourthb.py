class Solution:
    def maxWater(self, n, data):
        l = [0]*n
        r = [0]*n
        a = [0]*n
        for i in range(n):
            l[i], r[i], a[i] = data[i]

        left_fill = [0]*n
        left_fill[0] = a[0]
        for i in range(1, n):
            left_fill[i] = min(a[i], r[i-1], a[i] + left_fill[i-1] - a[i-1])

        right_fill = [0]*n
        right_fill[n-1] = a[n-1]
        for i in range(n-2, -1, -1):
            right_fill[i] = min(a[i], l[i+1], a[i] + right_fill[i+1] - a[i+1])

        best = 0
        for i in range(n):
            total = a[i]
            flow = a[i]
            for j in range(i-1, -1, -1):
                flow = min(flow, l[j+1])
                if flow == 0:
                    break
                total += min(a[j], flow)

            flow = a[i]
            for j in range(i+1, n):
                flow = min(flow, r[j-1])
                if flow == 0:
                    break
                total += min(a[j], flow)

            best = max(best, total)

        return best


if __name__ == "__main__":
    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    sol = Solution()
    print(sol.maxWater(n, data))
