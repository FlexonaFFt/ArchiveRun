from collections import defaultdict

def min_diff(a):
    n = len(a)
    a.sort()

    def is_biparate(delta):
        color = [-1] * n
        queue = []
        for i in range(n):
            if color[i] == -1:
                color[i] = 0
                queue.append(i)

                while queue:
                    u = queue.pop(0)
                    for j in range(n):
                        if (a[u] ^ a[j]) <= delta:
                            if color[j] == -1:
                                color[j] = 1 - color[u]
                                queue.append(j)
                            elif color[j] == color[i]:
                                return False
        return True

    left, right = 0, sum(a[i] ^ a[i + 1] for i in range(n - 1))
    while left <= right:
        mid = (left + right) // 2
        if is_biparate(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        print(min_diff(a))

if __name__ == '__main__':
    main()
