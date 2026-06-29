def drunkards_game(player1, player2):
    max_rounds, rounds = 10**6, 0

    while player1 and player2 and rounds < max_rounds:
        rounds += 1
        card1 = player1.popleft()
        card2 = player2.popleft()
        if (card1 > card2 and not (card1 == 9 and card2 == 0)) or (card1 == 0 and card2 == 9):
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card1)
            player2.append(card2)

    if rounds == max_rounds:
        return 'botva'
    elif player1:
        return f'first {rounds}'
    else:
        return f'second {rounds}'

def main():
    from collections import deque
    player1 = deque(map(int, input().split()))
    player2 = deque(map(int, input().split()))
    print(drunkards_game(player1, player2))

if __name__ == '__main__':
    main()
