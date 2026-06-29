def find_nearest_stop(stops, x):
    left, right = 0, len(stops) - 1

    # Найти ближайшую остановку слева
    while left <= right:
        mid = (left + right) // 2
        if stops[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    left_stop = right  # Максимальный индекс остановки слева

    # Найти ближайшую остановку справа
    left, right = 0, len(stops) - 1
    while left <= right:
        mid = (left + right) // 2
        if stops[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    right_stop = left  # Минимальный индекс остановки справа

    # Обработка условий
    if left_stop >= 0 and stops[left_stop] == x:
        return left_stop + 1  # Остановка совпадает с x
    elif left_stop >= 0 and right_stop < len(stops):
        return left_stop + 1  # Остановки слева и справа
    elif left_stop >= 0:
        return left_stop + 1  # Только остановки слева
    else:
        return right_stop + 1  # Только остановки справа

# Ввод данных
n, k = map(int, input().split())
stops = list(map(int, input().split()))
queries = list(map(int, input().split()))

# Решение задачи
for x in queries:
    print(find_nearest_stop(stops, x))
