from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD, n = 10**9 + 7, len(complexity)
        if n == 1: return 1

        min_rest = min(complexity[1:])
        if not(complexity[0] < min_rest): return 0

        answer = 1
        for x in range(2, n): answer = (answer * x) % MOD
        return answer
