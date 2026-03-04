def main() -> None:
    n = int(input().strip())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    opinion = [0] + list(map(int, input().split()))

    bad_incident = [0] * (n + 1)
    total_bad = 0

    for u, v in edges:
        if opinion[u] != opinion[v]:
            total_bad += 1
            bad_incident[u] += 1
            bad_incident[v] += 1

    answer = -1
    for employee in range(1, n + 1):
        if bad_incident[employee] == total_bad:
            answer = employee

    if answer == -1:
        print("NO")
    else:
        print("YES")
        print(answer)


if __name__ == "__main__":
    main()
