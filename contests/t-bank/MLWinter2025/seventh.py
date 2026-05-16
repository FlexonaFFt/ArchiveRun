MOD = 10**9 + 7


class Solution:
    def count_placements(self, n: int, k: int) -> int:
        if n == 1:
            return 1 if k in (0, 1) else 0
        if k > 2 * n - 2:
            return 0

        lens0 = []
        lens1 = []
        for d in range(2 * n - 1):
            length = n - abs(d - (n - 1))
            if (d - (n - 1)) % 2 == 0:
                lens0.append(length)
            else:
                lens1.append(length)

        def dp_for(lens):
            maxb = min(k, n - 1)
            dp = [0] * (maxb + 1)
            dp[0] = 1
            for L in sorted(lens):
                for j in range(maxb, 0, -1):
                    available = L - (j - 1)
                    if available > 0:
                        dp[j] = (dp[j] + dp[j - 1] * available) % MOD
            return dp

        dp0 = dp_for(lens0)
        dp1 = dp_for(lens1)

        ans = 0
        for i in range(min(k, len(dp0) - 1) + 1):
            j = k - i
            if 0 <= j <= len(dp1) - 1:
                ans = (ans + dp0[i] * dp1[j]) % MOD
        return ans


if __name__ == "__main__":
    n_str, k_str = input().split()
    n = int(n_str)
    k = int(k_str)
    solver = Solution()
    print(solver.count_placements(n, k))
