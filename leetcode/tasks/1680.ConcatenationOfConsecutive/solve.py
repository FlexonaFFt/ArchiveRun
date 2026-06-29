class Solution:
    def concatenatedBinary(self, n: int) -> int:
        all_bins = str()

        for i in range(1, n + 1):
            curr = bin(i)[2:]
            all_bins += curr 
        
        integer, MOD = int(all_bins, 2), 10**9 + 7
        return integer % MOD
