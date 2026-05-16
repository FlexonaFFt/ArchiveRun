def min_difficulty(n, alice, bob, eve):
    dp = [[float('inf')] * n for _ in range(n)]

    # Заполняем базовые случаи
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                alice_sum = sum(alice[:i + 1])
                bob_sum = sum(bob[i + 1:j + 1])
                eva_sum = sum(eve[j + 1:])

                # Ищем максимальное значение среди Alice, Bob, Eva
                current_max = max(alice_sum, bob_sum, eva_sum)

                # Сравниваем с текущим минимальным значением
                dp[i][j] = min(dp[i][j], current_max)

    # Ищем минимальное значение в dp таблице
    min_total_difficulty = min(min(row) for row in dp)

    return min_total_difficulty

def main():
    n = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    eve = list(map(int, input().split()))
    print(min_difficulty(n, alice, bob, eve))

if __name__ == '__main__':
    main()
