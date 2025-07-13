import sys

class FastInput:
    def __init__(self):
        self.stdin = sys.stdin

    def read_line(self):
        return sys.stdin.readline().strip()

    def read_tokens(self):
        return self.read_line().split()

    def read_int(self):
        return int(self.read_line())

    def read_ints(self):
        return map(int, self.read_tokens())

def solution():
    import sys
    input = sys.stdin.readline
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        visited = [False] * n
        mins = []
        for i in range(n):
            if not visited[i]:
                cur = i
                mn = b[cur]
                while not visited[cur]:
                    visited[cur] = True
                    cur = a[cur] - 1
                    mn = min(mn, b[cur])
                mins.append(mn)
        if len(mins) == 1:
            results.append("0")
        else:
            results.append(str(sum(mins)))
    print('\n'.join(results))

