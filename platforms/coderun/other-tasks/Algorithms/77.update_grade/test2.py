# Решение не проходит закрытый тест (id: 18)
def is_passed(a, b, c, fives):
    total_scores = a * 2 + b * 3 + c * 4 + fives * 5
    total_lessons = a + b + c + fives
    average_score = total_scores / total_lessons
    rounded_score = round(average_score)
    return rounded_score >= 4

def min_fives(a, b, c):
    left, right = 0, 100  # Устанавливаем границы для бинарного поиска
    answer = right  # Начальное значение для ответа

    while left <= right:
        mid = (left + right) // 2
        if is_passed(a, b, c, mid):
            answer = mid  # Если возможно достичь 4, обновляем ответ
            right = mid - 1  # Ищем меньшее количество пятёрок
        else:
            left = mid + 1  # Ищем большее количество пятёрок

    return answer

# Считываем входные данные
a = int(input())
b = int(input())
c = int(input())

# Вызываем функцию и выводим результат
print(min_fives(a, b, c))
