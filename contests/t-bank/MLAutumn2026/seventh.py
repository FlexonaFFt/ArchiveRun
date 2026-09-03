import sys

input = sys.stdin.buffer.readline

n, q = map(int, input().split())
dsu = [[-1] * n for _ in range(9)]


def unite(parent, a, b):
    while parent[a] >= 0:
        if parent[parent[a]] >= 0:
            parent[a] = parent[parent[a]]
        a = parent[a]

    while parent[b] >= 0:
        if parent[parent[b]] >= 0:
            parent[b] = parent[parent[b]]
        b = parent[b]

    if a == b:
        return 0

    if parent[a] > parent[b]:
        a, b = b, a

    parent[a] += parent[b]
    parent[b] = a
    return 1


answer = 0

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    answer += w

    for level in range(w - 1, 9):
        unite(dsu[level], a, b)

output = []

for _ in range(q):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1

    for level in range(w - 1, 9):
        answer -= unite(dsu[level], u, v)

    output.append(str(answer))

sys.stdout.write("\n".join(output))
