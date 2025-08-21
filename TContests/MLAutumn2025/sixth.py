from typing import List, Tuple

class Solution:
    def orient_edges(self, n: int, m: int, edges: List[Tuple[int, int]]):
        a = [0] * m
        b = [0] * m
        adj = [[] for _ in range(n + 1)]
        for i, (u, v) in enumerate(edges):
            a[i], b[i] = u, v
            adj[u].append((v, i))
            adj[v].append((u, i))

        need = [0] * (n + 1)
        for i in range(m):
            need[b[i]] ^= 1

        keep = [1] * m
        used_e = [False] * m
        vis = [False] * (n + 1)
        parent = [-1] * (n + 1)
        parent_e = [-1] * (n + 1)
        order: List[int] = []

        def dfs_build(start: int):
            vis[start] = True
            stack = [(start, 0)]
            base = len(order)
            while stack:
                v, it = stack[-1]
                if it < len(adj[v]):
                    to, ei = adj[v][it]
                    stack[-1] = (v, it + 1)
                    if not used_e[ei]:
                        used_e[ei] = True
                        if not vis[to]:
                            vis[to] = True
                            parent[to] = v
                            parent_e[to] = ei
                            stack.append((to, 0))
                        else:
                            need[v] ^= 1
                            need[to] ^= 1
                else:
                    order.append(v)
                    stack.pop()
            return order[base:]

        for s in range(1, n + 1):
            if vis[s] or not adj[s]:
                continue
            comp = dfs_build(s)
            if not comp:
                continue
            for v in comp[:-1]:
                e = parent_e[v]
                keep[e] = need[v]
                p = parent[v]
                if p != -1:
                    need[p] ^= need[v]
                need[v] = 0
            root = comp[-1]
            if need[root] != 0:
                return -1
            need[root] = 0

        ans = []
        for i in range(m):
            if keep[i] == 1:
                ans.append((a[i], b[i]))
            else:
                ans.append((b[i], a[i]))
        return ans


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    sol = Solution()
    ans = sol.orient_edges(n, m, edges)

    if ans == -1:
        print(-1)
    else:
        for u, v in ans:
            print(u, v)
