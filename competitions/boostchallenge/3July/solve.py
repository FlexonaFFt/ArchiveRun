from collections import deque


def solution(n, stones):
    Set = set(stones)
    Set.add(0)
    Set.add(n)

    dist1 = [-1] * (n + 1)
    queue = deque()
    dist1[0] = 0
    queue.append(0)

    while queue:
        cur = queue.popleft()
        for step in [1, 2]:
            nxt = cur + step
            if nxt <= n and nxt in Set:
                if dist1[nxt] == -1:
                    dist1[nxt] = dist1[cur] + 1
                    queue.append(nxt)
    if dist1[n] == -1: return [-1]

    dist2 = [-1] * (n + 1)
    queue = deque()
    dist2[n] = 0
    queue.append(n)

    while queue:
        current = queue.popleft()
        for step in [-1, -2]:
            nxt = current + step
            if nxt >= 0 and nxt in Set:
                if dist2[nxt] == -1:
                    dist2[nxt] = dist2[current] + 1
                    queue.append(nxt)

    path, current = [], 0
    while current != n:
        found = False
        for step in [1, 2]:
            nxt = current + step
            if nxt > n or nxt not in Set:
                continue
            if dist1[nxt] != dist1[current] + 1:
                continue
            if dist2[nxt] == -1:
                continue
            if dist1[n] == dist1[nxt] + dist2[nxt]:
                path.append(step)
                current = nxt
                found = True
                break
        if not found:
            return [-1]

    return [len(path)] + path


print(solution(2, ['abac', 'abacab', 'aba', 'abaa']))
