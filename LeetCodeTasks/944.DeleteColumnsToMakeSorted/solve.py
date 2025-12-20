from typing import List 

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, deletions = len(strs), 0
        m = len(strs[0]) if n > 0 else 0

        for col in range(m):
            col_chars = [strs[row][col] for row in range(n)]
            if self.sorted_string(col_chars): deletions += 1
        return deletions

    def sorted_string(self, string: str) -> bool:
        return any(string[i] > string[i + 1] for i in range(len(string) - 1))
