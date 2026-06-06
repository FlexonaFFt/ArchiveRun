def main(n, m, k, A, B):
    # сразу работаем в матрице output
    for i in range(n - k + 1):
        curr_row = []

        for j in range(m - k + 1):
            element = 0
            for t in range(k):
                for l in range(k):
                    element += A[i + t][j + l] * B[t][l]
            curr_row.append(str(element))
        print(' '.join(curr_row))


def function() -> None:
    n, m = map(int, input().split())
    A, B = [], []

    for _ in range(n):
        A.append(list(map(int, input().split())))

    k = int(input())
    for _ in range(k):
        B.append(list(map(int, input().split())))

    main(n, m, k, A, B)


if __name__ == '__main__':
    function()
