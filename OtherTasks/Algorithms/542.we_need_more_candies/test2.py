# Превышает лимит времени на закрытом тесте (id: 10)
from collections import Counter

def min_candies_to_make_pretty(n, a):
    # Подсчитываем количество каждой группы конфет
    freq = Counter(a)

    # Если только одна уникальная группа, то всё уже симпатично
    if len(freq) == 1:
        return 0

    # Если есть хотя бы 3 уникальные группы конфет
    # Нам нужно свести их к двум группам с одинаковым количеством конфет
    # Считаем, сколько нужно будет добавить конфет для каждой уникальной группы
    additions_needed = float('inf')

    # Перебираем все возможные уникальные количества конфет
    unique_counts = list(freq.keys())

    # Пробуем объединить банки в две группы, чтобы минимизировать добавления
    for x in unique_counts:
        for y in unique_counts:
            if x == y:
                continue
            # Подсчитаем, сколько конфет нужно добавить, чтобы все банки привели к x и y
            additions = 0
            for count in a:
                # Если текущее количество конфет не равно ни x, ни y, то нужно добавить
                if count != x and count != y:
                    additions += min(abs(count - x), abs(count - y))
            additions_needed = min(additions_needed, additions)

    return additions_needed

# Чтение входных данных
n = int(input())  # количество банок
a = list(map(int, input().split()))  # количество конфет в каждой банке

# Вывод результата
print(min_candies_to_make_pretty(n, a))
