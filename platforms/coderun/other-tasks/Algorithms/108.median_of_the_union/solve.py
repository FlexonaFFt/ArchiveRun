# Не является решением задачи, так как выводит неправильный ответ
def find_left_median(sequences):
    N = len(sequences)
    medians = []

    # Проходим по всем парам последовательностей
    for i in range(N):
        for j in range(i + 1, N):
            # Объединяем две последовательности
            combined = sequences[i] + sequences[j]
            # Сортируем объединенную последовательность
            combined.sort()
            # Находим левую медиану (элемент на позиции L)
            left_median = combined[L]  # Индекс L соответствует L+1-му элементу
            medians.append(left_median)

    return medians

# Чтение входных данных
N, L = map(int, input().split())
sequences = [list(map(int, input().split())) for _ in range(N)]

# Находим и выводим левую медиану для каждой пары
medians = find_left_median(sequences)
for median in medians:
    print(median)
