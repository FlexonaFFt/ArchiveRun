from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs: return 0
        n, m = len(strs), len(strs[0])
        ok, deletions = [False] * (n - 1), 0

        for c in range(m):
            conflict = False 
            for i in range(n - 1):
                if not ok[i]:
                    if strs[i][c] > strs[i + 1][c]:
                        conflict = True 
                        break 
            
            if conflict: 
                deletions += 1
                continue

            for i in range(n - 1):
                if not ok[i] and strs[i][c] < strs[i + 1][c]:
                    ok[i] = True 

        return deletions
