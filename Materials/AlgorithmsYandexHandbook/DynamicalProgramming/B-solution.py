n, m = map(int, input().split())

max_n = n
max_m = m

# Инициализация таблицы dp
dp = [[False] * (max_m + 1) for _ in range(max_n + 1)]

for i in range(max_n + 1):
    for j in range(max_m + 1):
        if i == 0 and j == 0:
            dp[i][j] = False
            continue

        found = False

        # Проверяем все возможные ходы
        # 1. Взять 1 из первого набора
        if i >= 1 and not dp[i-1][j]:
            found = True
        # 2. Взять 1 из второго набора
        if not found and j >= 1 and not dp[i][j-1]:
            found = True
        # 3. Взять 2 из первого набора
        if not found and i >= 2 and not dp[i-2][j]:
            found = True
        # 4. Взять 2 из второго набора
        if not found and j >= 2 and not dp[i][j-2]:
            found = True
        # 5. Взять 2 из первого и 1 из второго
        if not found and i >= 2 and j >= 1 and not dp[i-2][j-1]:
            found = True
        # 6. Взять 1 из первого и 2 из второго
        if not found and i >= 1 and j >= 2 and not dp[i-1][j-2]:
            found = True

        dp[i][j] = found

print("Win" if dp[n][m] else "Lose")
