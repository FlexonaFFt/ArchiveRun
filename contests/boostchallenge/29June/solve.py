def solution(n: int, m: int, p: list[int]) -> list[int]:
    restored = p[:]
    for i in range(n):
        if restored[i] == -1:
            if i == 0:
                restored[i] = m
            else:
                restored[i] = restored[i - 1] + m
        else:
            if i > 0 and restored[i] - restored[i - 1] < m:
                return [-1]
    earned = [restored[0]]
    for i in range(1, n):
        earned.append(restored[i] - restored[i - 1])
    return earned
