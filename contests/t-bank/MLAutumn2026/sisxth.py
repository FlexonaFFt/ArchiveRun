import sys

input = sys.stdin.buffer.readline

n = int(input())
m = 1 << n
c = [list(map(int, input().split())) for _ in range(m)]
dp = [0] * m

for level in range(n):
    half = 1 << level
    size = half * 2

    for left in range(0, m, size):
        middle = left + half
        right = left + size

        if level == 0:
            best_left = dp[left]
            best_right = dp[middle]
        else:
            best_left = max(dp[i] + c[i][level - 1] for i in range(left, middle))
            best_right = max(dp[i] + c[i][level - 1] for i in range(middle, right))

        for i in range(left, middle):
            dp[i] += best_right

        for i in range(middle, right):
            dp[i] += best_left

print(max(dp[i] + c[i][n - 1] for i in range(m)))
