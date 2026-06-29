def solution(n, m, swaps):
    positions = [i + 1 for i in range(2 * n)]
    methods_left = n
    result = []

    for i in range(m):
        a = swaps[2 * i] - 1
        b = swaps[2 * i + 1] - 1

        was_a_left = (a < n) and (1 <= positions[a] <= n)
        was_b_left = (b < n) and (1 <= positions[b] <= n)

        positions[a], positions[b] = positions[b], positions[a]

        now_a_left = (a < n) and (1 <= positions[a] <= n)
        now_b_left = (b < n) and (1 <= positions[b] <= n)

        methods_left += now_a_left - was_a_left
        methods_left += now_b_left - was_b_left

        result.append(methods_left)

    return result


def test():
    n, m, swaps = 3, 2, [1, 4, 2, 5]
    print(solution(n=n, m=m, swaps=swaps))


if __name__ == '__main__': test()
