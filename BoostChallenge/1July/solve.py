def solution(n: int) -> int:
    import sys
    sys.setrecursionlimit(1000000)
    MOD = 10**9 - 7538
    memo = {0: 1}

    def calc(k):
        if k in memo:
            return memo[k]
        a = calc(k // 2)
        b = calc(k // 3)
        c = calc(k // 4)
        res = (pow(a, b, MOD) + 5 * c + k) % MOD
        memo[k] = res
        return res

    return calc(n)

