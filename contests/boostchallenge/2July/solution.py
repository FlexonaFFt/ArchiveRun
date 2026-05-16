def solution(n: int, q: int, a: list[int], queries: list[list[int]]) -> int:
    freq = [0] * (n + 1)
    for l, r in queries:
        freq[l - 1] += 1
        freq[r] -= 1

    for i in range(1, n):
        freq[i] += freq[i - 1]

    freq = freq[:n]
    a.sort(reverse=True)
    freq.sort(reverse=True)

    return sum(x * y for x, y in zip(a, freq))


def test():
    print(solution(3,4,[7,3,1],[[1, 3], [2, 3], [3, 3], [2, 2]]))
    print(solution(4,4,[1, 100, 10000, 10101010], [[1, 4], [2, 3], [2, 2], [1, 2]]))

if __name__ == '__main__': test()
