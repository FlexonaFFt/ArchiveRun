import sys

def ceil_div(x, y):
    return (x + y - 1) // y

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 4:
        return
    L, W, A, B = map(int, data[:4])

    half_L = (L + 1) // 2
    half_W = (W + 1) // 2

    if A >= half_L and B >= half_W:
        print(1)
        return

    ans = ceil_div(L, A) + ceil_div(W, B)
    print(ans)

if __name__ == '__main__':
    main()
