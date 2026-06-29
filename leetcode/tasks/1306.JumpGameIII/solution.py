from typing import List 
from collections import deque 

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n, q = len(arr), deque([start])
        visited = [False] * n
        visited[start] = True 

        while q:
            curr = q.popleft()
            if arr[curr] == 0: return True 

            for nxt in (curr + arr[curr], curr - arr[curr]):
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True 
                    q.append(nxt)

        return False
