from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD, n = 1_000_000_007, len(nums)
        dp, pref = [0] * (n + 1), [0] * (n + 1)
        dp[0], pref[0], L = 1, 1, 0
        min_dq, max_dq = deque(), deque()

        for r in range(1, n + 1):
            idx = r - 1
            
            while max_dq and nums[max_dq[-1]] < nums[idx]:
                max_dq.pop()
            max_dq.append(idx)

            while min_dq and nums[min_dq[-1]] > nums[idx]:
                min_dq.pop()
            min_dq.append(idx)

            while max_dq and min_dq and nums[max_dq[0]] - nums[min_dq[0]] > k:
                if max_dq and max_dq[0] == L: max_dq.popleft()
                if min_dq and min_dq[0] == L: min_dq.popleft()
                L += 1

            if L == 0: dp[r] = pref[r - 1] % MOD
            else: dp[r] = (pref[r - 1] - pref[L - 1]) % MOD
            pref[r] = (pref[r - 1] + dp[r]) % MOD
        
        return dp[n] % MOD
