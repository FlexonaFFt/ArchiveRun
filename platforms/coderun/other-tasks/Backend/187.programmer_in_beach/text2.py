def find_min_xor(tests):
    results = []
    for test in tests:
        n, a = test
        a.sort()  # Сортируем массив
        min_xor = float('inf')  # Инициализируем минимальное значение XOR бесконечностью

        # Ищем минимальное XOR среди соседних элементов
        for i in range(n - 1):
            current_xor = a[i] ^ a[i + 1]
            min_xor = min(min_xor, current_xor)

        results.append(min_xor)
    return results

# Чтение данных
T = int(input().strip())
tests = []
for _ in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    tests.append((n, a))

# Выполнение и вывод результатов
results = find_min_xor(tests)
for result in results:
    print(result)

