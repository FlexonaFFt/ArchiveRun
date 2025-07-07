from collections import deque


def solution(n, stones):
    S = set(stones)
    S.add(0)
    S.add(n)

    dist1 = [-1] * (n + 1)
    q = deque()
    dist1[0] = 0
    q.append(0)

    while q:
        cur = q.popleft()
        for step in [1, 2]:
            nxt = cur + step
            if nxt <= n and nxt in S:
                if dist1[nxt] == -1:
                    dist1[nxt] = dist1[cur] + 1
                    q.append(nxt)

    if dist1[n] == -1:
        return [-1]

    dist2 = [-1] * (n + 1)
    q = deque()
    dist2[n] = 0
    q.append(n)

    while q:
        cur = q.popleft()
        for step in [-1, -2]:
            nxt = cur + step
            if nxt >= 0 and nxt in S:
                if dist2[nxt] == -1:
                    dist2[nxt] = dist2[cur] + 1
                    q.append(nxt)

    path = []
    cur = 0
    while cur != n:
        found = False
        for step in [1, 2]:
            nxt = cur + step
            if nxt > n or nxt not in S:
                continue
            if dist1[nxt] != dist1[cur] + 1:
                continue
            if dist2[nxt] == -1:
                continue
            if dist1[n] == dist1[nxt] + dist2[nxt]:
                path.append(step)
                cur = nxt
                found = True
                break
        if not found:
            return [-1]

    return [len(path)] + path










n = 10
words = [
    "a", "ab", "abc", "abcd", "abcde",
    "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij",
    "ax", "abxx", "abcxx", "abcdxx", "abcdexx",
    "abcdefxx", "abcdefgxx", "abcdefghxx", "abcdefghiixx", "abcdefghijxx"
]

res = solution(n, words)
print(sorted(res))


n = 10
words = [
    "a",       #1 короткое
    "ab",      #2 короткое
    "abc",     #3 короткое
    "abcd",    #4 короткое
    "abcde",   #5 короткое
    "abcdef",  #6 короткое
    "abcdefg", #7 короткое
    "abcdefgh",#8 короткое
    "abcdefghi",#9 короткое
    "abcdefghij",#10 короткое

    "ax",      #11 длинное, не префикс от коротких
    "abxx",    #12 длинное, префикс "ab"
    "abcxx",   #13 длинное, префикс "abc"
    "abcdxx",  #14 длинное, префикс "abcd"
    "abcdexx", #15 длинное, префикс "abcde"
    "abcdefxx",#16 длинное, префикс "abcdef"
    "abcdefgxx",#17 длинное, префикс "abcdefg"
    "abcdefghxx",#18 длинное, префикс "abcdefgh"
    "abcdefghiixx",#19 длинное, префикс "abcdefghi"
    "abcdefghijxx" #20 длинное, префикс "abcdefghij"
]


print(solution(n, words))

n = 2
words = ["abac", "abacab", "aba", "abaa"]
print(solution(n, words))

