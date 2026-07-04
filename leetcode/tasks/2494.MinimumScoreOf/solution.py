from typing import List 
from collections import defaultdict, deque 

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph, queue = defaultdict(list), deque([1])
        visited, answer = set(), float('inf')

        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))

        while queue:
            city = queue.popleft()
            if city in visited: continue

            visited.add(city)
            for neighbor, distance in graph[city]:
                answer = min(answer, distance)
                if neighbor not in visited:
                    queue.append(neighbor)

        return answer 
