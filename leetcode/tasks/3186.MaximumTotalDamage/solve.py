from collections import Counter
import bisect

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        values = sorted(freq.keys())
        sums = [v * freq[v] for v in values]
        m = len(values)
        if m == 0:
            return 0

        dp = [0] * m
        dp[0] = sums[0]

        for i in range(1, m):
            limit = values[i] - 3
            pos = bisect.bisect_right(values, limit)
            p = pos - 1  

            take = (dp[p] if p >= 0 else 0) + sums[i]
            skip = dp[i - 1]
            dp[i] = max(skip, take)

        return dp[-1]
