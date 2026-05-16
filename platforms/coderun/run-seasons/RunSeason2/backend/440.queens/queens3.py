def min_liars(turn):
    total_queens = 4
    queens_in_turn = sum(turn)
    min_liars = float('inf')

    for discarded in range(0, 3):
        max_queens = total_queens - discarded

        if queens_in_turn == max_queens:
            return 0

        if queens_in_turn == 0:
            return 1

        if queens_in_turn > max_queens:
            turn.sort(reverse=True)
            current_queens = queens_in_turn
            liars = 0

            for statement in turn:
                current_queens -= statement
                liars += 1
                if current_queens <= max_queens:
                    break

            min_liars = min(min_liars, liars)

    if min_liars == float('inf'):
        return 0

    return min_liars


if __name__ == '__main__':
    input_data = input()
    turn = list(map(int, input_data.split()))
    print(min_liars(turn))
