def sochetanya(n: int, k: int) -> int:
    from math import factorial
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    return factorial(n) // (factorial(k) * factorial(n - k))

def main():
    n, k = map(int, input().split())
    print(sochetanya(n, k))

if __name__ == '__main__':
    main()
