# Не является решением задачи
def min_difficulty(n, alice, bob, eve):
    # Префиксные суммы для каждого участника
    prefix_alice = [0] * (n + 1)
    prefix_bob = [0] * (n + 1)
    prefix_eve = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_alice[i] = prefix_alice[i - 1] + alice[i - 1]
        prefix_bob[i] = prefix_bob[i - 1] + bob[i - 1]
        prefix_eve[i] = prefix_eve[i - 1] + eve[i - 1]

    # Минимальные значения сложности для первого и второго интервалов
    min_difficulty_1 = float('inf')
    result = float('inf')

    for j in range(2, n):
        min_difficulty_1 = min(min_difficulty_1, prefix_alice[j - 1] + prefix_bob[j - 1] - prefix_bob[1])
        total_difficulty = min_difficulty_1 + prefix_bob[j] - prefix_bob[j - 1] + prefix_eve[n] - prefix_eve[j]
        result = min(result, total_difficulty)

    return result

# Пример использования:
n = int(input())
alice = list(map(int, input().split()))
bob = list(map(int, input().split()))
eve = list(map(int, input().split()))

result = min_difficulty(n, alice, bob, eve)
print(result)
