# Решение не проходит закрытый тест (id: 27)
def min_fives(a, b, c):
    total_scores = a * 2 + b * 3 + c * 4
    total_lessons = a + b + c
    fives_needed = 0

    while True:
        # Общее количество уроков с учетом пятёрок
        current_total_lessons = total_lessons + fives_needed
        # Общая сумма оценок с учетом пятёрок
        current_total_scores = total_scores + fives_needed * 5
        # Средняя оценка
        average_score = current_total_scores / current_total_lessons

        # Округляем среднюю оценку
        rounded_score = round(average_score)

        if rounded_score >= 4:
            return fives_needed

        fives_needed += 1

# Считываем входные данные
a = int(input())
b = int(input())
c = int(input())

# Вызываем функцию и выводим результат
print(min_fives(a, b, c))
