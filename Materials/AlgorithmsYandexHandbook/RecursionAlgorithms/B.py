def hanoi4(n):
    def hanoi3(m):
        return (1 << m) - 1

    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = float('inf')
        for k in range(1, i):
            moves = 2 * dp[k] + hanoi3(i - k)
            if moves < dp[i]:
                dp[i] = moves
    return dp[n]

n = int(input())
print(hanoi4(n))
