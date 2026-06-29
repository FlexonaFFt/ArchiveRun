# WA 6
def solution(n: int, m: int) -> int:
    left, right = 1, m
    while left < right:
        mid = (left + right) // 2
        total = 0
        c = 1
        k = 0
        while k <= n and c <= mid:
            total += c
            k += 1
            c = c * (n - k + 1) // k if k <= n else 0
        total += (n + 1 - k) * mid
        if total >= m:
            right = mid
        else:
            left = mid + 1
    return left


def test():
    print(solution(1, 2))
    print(solution(5, 6))
    print(solution(3, 5))

if __name__ == '__main__': test()
