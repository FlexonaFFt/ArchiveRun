def solve(n: int, k: int, a: list[int]) -> list[int]:
    from collections import deque

    stones = set(a)
    stones.add(0)
    stones.add(n)
    stones = sorted(stones)
    stone_set = set(stones)

    if n not in stone_set:
        return [-1]

    prev = {}
    jump = {}
    queue = deque()
    queue.append(0)
    prev[0] = -1  

    while queue:
        pos = queue.popleft()
        for d in [1, 2]: 
            nxt = pos + d
            if nxt in stone_set and nxt not in prev:
                prev[nxt] = pos
                jump[nxt] = d
                queue.append(nxt)
                if nxt == n:
                    break

    if n not in prev:
        return [-1]

    res = []
    cur = n
    while prev[cur] != -1:
        res.append(jump[cur])
        cur = prev[cur]
    res.reverse()
    return [len(res)] + res
