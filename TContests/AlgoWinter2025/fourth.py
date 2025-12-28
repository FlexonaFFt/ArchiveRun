import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]

    dq_min = []
    dq_max = []
    left = 0
    ans = 0

    for right in range(n):
        while dq_min and a[dq_min[-1]] >= a[right]:
            dq_min.pop()
        dq_min.append(right)

        while dq_max and a[dq_max[-1]] <= a[right]:
            dq_max.pop()
        dq_max.append(right)

        while a[dq_max[0]] - a[dq_min[0]] > k:
            if dq_min[0] == left:
                dq_min.pop(0)
            if dq_max[0] == left:
                dq_max.pop(0)
            left += 1

        ans += right - left + 1

    print(ans)

if __name__ == "__main__":
    main()