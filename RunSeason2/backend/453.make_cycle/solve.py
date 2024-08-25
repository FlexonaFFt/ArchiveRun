# Решение ломается на первом закрытом тесте
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootX] = rootY
            rank[rootX] += 1

def count_ways_to_add_tunnel(n, m, edges):
    parent = list(range(n))
    rank = [0] * n

    for u, v in edges:
        union(parent, rank, u - 1, v - 1)

    component_size = [0] * n
    for i in range(n):
        root = find(parent, i)
        component_size[root] += 1

    rezult = 0
    for i in range(n):
        if component_size[i] > 1:
            rezult += component_size[i] * (component_size[i] - 1) // 2

    return rezult - m

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        iter = tuple(map(int, input().split()))
        edges.append(iter)
    print(count_ways_to_add_tunnel(n, m, edges))

if __name__ == '__main__':
    main()
