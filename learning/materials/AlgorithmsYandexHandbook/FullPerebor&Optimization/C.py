def sochetanya(n: int, k: int) -> int:
    from math import comb
    if n < 0 or k < 0:
        return 0
    return comb(n + k - 1, k)

def main():
    n, k = map(int, input().split())
    print(sochetanya(n, k))

if __name__ == '__main__':
    main()
