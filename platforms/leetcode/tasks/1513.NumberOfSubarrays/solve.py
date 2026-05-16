class Solution:
    def numSub(self, s: str) -> int:
        MOD, ans, run = 10**9 + 7, 0, 0
        for char in s:
            if char == "1":
                run += 1
                ans = (ans + run) % MOD
            else:
                run = 0
        return ans 
