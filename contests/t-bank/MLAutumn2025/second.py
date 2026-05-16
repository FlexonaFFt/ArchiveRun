t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    ok = True
    for i in range(n):
        if a[i] > i + 1:
            ok = False
            break

    if not ok:
        print("Second")
        continue

    moves = 0
    for i in range(n):
        moves += (i + 1) - a[i]

    if moves % 2 == 1:
        print("First")
    else:
        print("Second")
