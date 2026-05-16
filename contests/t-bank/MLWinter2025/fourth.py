from collections import deque


class Solution:
    def shortest_cycle(self, n: int, adj: list[list[int]]) -> int:
        inf = 10**9
        ans = inf
        for start in range(n):
            dist = [-1] * n
            parent = [-1] * n
            dist[start] = 0
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        cycle_len = dist[u] + dist[v] + 1
                        if cycle_len < ans:
                            ans = cycle_len
            if ans == 3:
                break
        return -1 if ans == inf else ans


if __name__ == "__main__":
    n_m = input().split()
    n = int(n_m[0])
    m = int(n_m[1])
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a_str, b_str = input().split()
        a = int(a_str) - 1
        b = int(b_str) - 1
        adj[a].append(b)
        adj[b].append(a)

    solver = Solution()
    print(solver.shortest_cycle(n, adj))
