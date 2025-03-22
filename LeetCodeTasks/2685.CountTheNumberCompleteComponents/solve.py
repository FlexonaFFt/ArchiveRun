from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        components = defaultdict(int)

        for vertex in range(n):
            graph[vertex] = [vertex]

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        for vertex in range(n):
            neighbor = tuple(sorted(graph[vertex]))
            components[neighbor] += 1

        return sum(
            1 for neighbor, freq in components.items()
            if len(neighbor) == freq
        )

# Runtime 43 ms, 71.70 %
# Memory 18.51 mb, 16.83 %
def main():
    solution = Solution()
    print(solution.countCompleteComponents(n=6, edges=[[0,1],[0,2],[1,2],[3,4]]))
    print(solution.countCompleteComponents(n=6, edges=[[0,1],[0,2],[1,2],[3,4],[3,5]]))

main()
