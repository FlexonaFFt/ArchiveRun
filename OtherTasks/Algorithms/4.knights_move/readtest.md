```
def count_knight_paths(N, M):
    # Создаем двумерный массив для хранения количества путей
    dp = [[0] * M for _ in range(N)]
    
    # Начальная позиция
    dp[0][0] = 1
    
    # Перебираем все клетки доски
    for i in range(N):
        for j in range(M):
            # Ход на 2 вниз и 1 вправо
            if i + 2 < N and j + 1 < M:
                dp[i + 2][j + 1] += dp[i][j]
            # Ход на 1 вниз и 2 вправо
            if i + 1 < N and j + 2 < M:
                dp[i + 1][j + 2] += dp[i][j]
        
    # Возвращаем количество путей к правому нижнему углу
    return dp[N - 1][M - 1]

# Чтение входных данных
N, M = map(int, input().split())
# Вывод результата
print(count_knight_paths(N, M))```
