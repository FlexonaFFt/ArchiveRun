def find_missing_cards(N, sums):
    # Calculate theoretical sums
    total_sum = N * (N + 1) // 2
    total_sum_squares = N * (N + 1) * (2 * N + 1) // 6
    total_sum_cubes = (total_sum ** 2)

    # Given sums
    sum_cards, sum_squares, sum_cubes = sums

    # Calculate the sums of the missing numbers
    missing_sum = total_sum - sum_cards
    missing_sum_squares = total_sum_squares - sum_squares
    missing_sum_cubes = total_sum_cubes - sum_cubes

    # Since we know that the missing numbers are consecutive integers,
    # we can use the properties of arithmetic sequences to solve this.
    # However, for simplicity and given the constraints, we'll use a direct approach.

    # We know that the sum of three consecutive integers is the middle number times 3.
    # Let's denote the middle number as 'm'.
    # Then, m * 3 = missing_sum

    m = missing_sum // 3
    if m * 3 != missing_sum:
        raise ValueError("No valid solution")

    # The missing numbers are m-1, m, m+1
    missing_numbers = [m - 1, m, m + 1]

    # Verify that these numbers satisfy the sum of squares and cubes
    if (sum(x ** 2 for x in missing_numbers) == missing_sum_squares and
        sum(x ** 3 for x in missing_numbers) == missing_sum_cubes):
        return missing_numbers
    else:
        raise ValueError("No valid solution")

def main():
    N = int(input())
    sums = list(map(int, input().split()))
    try:
        missing_cards = find_missing_cards(N, sums)
        print(*missing_cards)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
