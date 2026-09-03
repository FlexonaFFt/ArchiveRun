n = int(input())
a = list(map(int, input().split()))

total = sum(a)

if total % (n - 1):
    print("NO")
else:
    target = total // (n - 1)
    other = [x for x in a if x != target]

    print(
        "YES"
        if len(other) == 2 and other[0] + other[1] == target
        else "NO"
    )
