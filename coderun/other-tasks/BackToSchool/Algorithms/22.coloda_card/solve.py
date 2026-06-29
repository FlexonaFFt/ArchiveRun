def solve():
    from itertools import combinations
    values, deck = {
    2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
    11: 11, 12: 12, 13: 13, 14: 14
}, []
    total_combitations, succesfull_combinations = 0, 0
    for suit in range(4):
        for rank in range(2, 15):
            deck.append(rank)

    for combo in combinations(deck, 6):
        total_combitations += 1
        if sum(values[card] for card in combo) == 21:
            succesfull_combinations += 1

    probality = succesfull_combinations / total_combitations
    print(f"{probality:.6f}")

if __name__ == '__main__':
    solve()
