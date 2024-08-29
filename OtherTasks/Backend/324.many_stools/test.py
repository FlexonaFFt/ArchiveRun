def find_max_profit(n, m, a, b):
    a.sort()
    b.sort(reverse=True)
    i, j = 0, 0
    profit = 0
    while i < n and j < m:
        if b[j] >= a[i]:
            profit += b[j] - a[i]
            i += 1
            j += 1
        else:
            j += 1

    return profit

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(find_max_profit(n, m, a, b))

if __name__ == "__main__":
    main()
