# Работат неправильно
def min_fives(a, b, c):
    total_scores = a * 2 + b * 3 + c * 4
    total_lessons = a + b + c

    fives_needed = max(0, (4 * total_lessons - total_scores + 4) // 5)
    return fives_needed

# Считываем входные данные
a = int(input())
b = int(input())
c = int(input())

# Вызываем функцию и выводим результат
print(min_fives(a, b, c))
