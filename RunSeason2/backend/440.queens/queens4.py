# Решение прошло все тесты
def min_liars(queens_claim):
    total_claimed = sum(queens_claim)
    min_liars_count = float('inf')

    if total_claimed < 2:
        return 1

    for discarded_queens in range(3):
        real_queens_in_hand = 4 - discarded_queens
        liars_count = 0

        if total_claimed > real_queens_in_hand:
            excess_claim = total_claimed - real_queens_in_hand
            for claim in sorted(queens_claim, reverse=True):
                if excess_claim <= 0:
                    break
                excess_claim -= claim
                liars_count += 1
        min_liars_count = min(min_liars_count, liars_count)

    return min_liars_count

def main():
    queens = list(map(int, input().split()))
    print(min_liars(queens))

if __name__ == '__main__':
    main()
