from collections import deque, defaultdict
class Solution:
    from typing import List
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # Построим обратный граф и входящую степень
        in_degree, reverse_graph = [0] * n, defaultdict(list)
        for scr in range(n):
            for dest in graph[scr]:
                reverse_graph[dest].append(scr)
                in_degree[scr] += 1

        # Найдём все терминальные вершины (входящая степень = 0)
        queue = deque(i for i in range(n) if in_degree[i] == 0)
        safe = set(queue) # Все терминальные вершины безопасны

        while queue:
            node = queue.popleft()
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    safe.add(neighbor)
                    queue.append(neighbor)
        return sorted(safe)

# Runtime 66 ms, 31.18 %
# Memory 24.09 mb, 19.84 %
def main():
    solve = Solution()
    graph1 = [[1,2],[2,3],[5],[0],[5],[],[]]
    graph2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    print(solve.eventualSafeNodes(graph1))
    print(solve.eventualSafeNodes(graph2))

if __name__ == '__main__':
    main()
