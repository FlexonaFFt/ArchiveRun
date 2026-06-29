class Solution():
    def longestSubsequence(self, s: str, k: int) -> int:
        n, ones, value, power = len(s), 0, 0, 1
        zeros = s.count("0")
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if value + power > k: continue
                value += power 
                ones += 1
            power <<= 1
            if power > k:
                break

        return zeros + ones

# Runtime 0 ms, 100 %
# Memory 17.94 mb, 28.78 %
solve = Solution()
print(solve.longestSubsequence(s="1001010", k=5)
print(solve.longestSubsequence(s="00101001", k=1)
