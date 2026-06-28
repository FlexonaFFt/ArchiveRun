from typing import List 
from collections import deque 

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, visited, provinces = len(isConnected), set(), 0

        for city in range(n):
            if city in visited: continue 
            provinces += 1

            queue = deque([city])
            visited.add(city)

            while queue:
                current = queue.popleft()

                for neighbor in range(n):
                    if isConnected[current][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return provinces
