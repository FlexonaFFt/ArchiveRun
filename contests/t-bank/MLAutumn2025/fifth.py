MOD = 10**9 + 7

class Solution:
    def __init__(self, maxn=1000):
        self.maxn = maxn
        self.fact = [1] * (self.maxn + 1)
        self.invfact = [1] * (self.maxn + 1)
        self._prepare()

    def _modpow(self, a, b, mod=MOD):
        res = 1
        while b > 0:
            if b & 1:
                res = res * a % mod
            a = a * a % mod
            b //= 2
        return res

    def _prepare(self):
        for i in range(1, self.maxn + 1):
            self.fact[i] = self.fact[i-1] * i % MOD
        self.invfact[self.maxn] = self._modpow(self.fact[self.maxn], MOD-2)
        for i in range(self.maxn, 0, -1):
            self.invfact[i-1] = self.invfact[i] * i % MOD

    def C(self, n, r):
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.invfact[r] % MOD * self.invfact[n-r] % MOD

    def solve(self, n: int, k: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for num in range(1, n + 1):
            newdp = dp[:]
            for s in range(num, n + 1):
                for m in range(1, s // num + 1):
                    ways = self.C(m + k - 1, k - 1)
                    newdp[s] = (newdp[s] + dp[s - m * num] * ways) % MOD
            dp = newdp
        return dp[n]


if __name__ == "__main__":
    n, k = map(int, input().split())
    sol = Solution()
    print(sol.solve(n, k))
