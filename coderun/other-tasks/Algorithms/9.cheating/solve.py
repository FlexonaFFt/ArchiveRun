# Решение не проходит второй открытый тест
# У меня так и не получилось разобраться к
# ак решать эту задачу, вернусь к ней позже
def can_divide_students(n, pairs):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in pairs:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, color):
        visited[node] = color
        for neighbor in graph[node]:
            if neighbor not in visited:
                if not dfs(neighbor, 1 - color):
                    return False
                elif visited[neighbor] == visited[node]:
                    return False
        return True

    visited = {}
    for node in range(1, n + 1):
        if node not in visited:
            if not dfs(node, 0):
                return "NO"
    return "YES"

def main():
    n, m = map(int, input().split())
    pairs = []
    for _ in range(m):
        u, v = map(int, input().split())
        pairs.append((u, v))
    print(can_divide_students(n, pairs))

if __name__ == '__main__':
    main()
