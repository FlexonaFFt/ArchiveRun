# TL 17 закрытый тест (id: 19)
def find_missing_cards(N, sums):
    total_sum = N * (N + 1) // 2
    total_sum_squares = N * (N + 1) * (2 * N + 1) // 6
    total_sum_cubes = (total_sum ** 2)

    sum_cards, sum_squares, sum_cubes = sums
    missing_sum = total_sum - sum_cards
    missing_sum_squares = total_sum_squares - sum_squares
    missing_sum_cubes = total_sum_cubes - sum_cubes

    for x in range(1, N + 1):
        for y in range(x + 1, N + 1):
            z = missing_sum - x - y
            if z > y and z <= N:
                if (x ** 2 + y ** 2 + z ** 2 == missing_sum_squares
                    and x ** 3 + y ** 3 + z ** 3 == missing_sum_cubes):
                        return x, y, z

def main():
    N = int(input())
    sums = list(map(int, input().split()))
    missing_cards = find_missing_cards(N, sums)
    print(*missing_cards)

if __name__ == '__main__':
    main()
