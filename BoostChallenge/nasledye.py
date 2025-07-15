def solution(n, m):
    if m <= n + 1:
        return 1

    center = n // 2
    coeffs = [0] * (n + 1)
    c = 1
    for i in range(1, center + 1):
        c = c * (n - i + 1) // i
    coeffs[center] = c
    for k in range(center, n):
        coeffs[k + 1] = coeffs[k] * (n - k) // (k + 1)
    for k in range(center, 0, -1):
        coeffs[k - 1] = coeffs[k] * k // (n - k + 1)

    total = 0
    k = 0
    used = set()
    for d in range(n + 1):
        for idx in [center + d, center - d]:
            if 0 <= idx <= n and idx not in used:
                cnt = coeffs[idx]
                if total + cnt >= m:
                    return k + 1
                total += cnt
                k += 1
                used.add(idx)
        if len(used) >= n + 1:
            break
    return k





def test():
    print(solution(1, 2))
    print(solution(5, 6))
    print(solution(3, 5))

if __name__ == '__main__':
    test()
