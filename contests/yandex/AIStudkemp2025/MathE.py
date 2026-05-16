import math

def maximize_expression(max_n):
    max_value = 0
    best_n = 0
    for n in range(1, max_n + 1):
        value = n * math.log(1000) - math.log(math.factorial(n))
        if value > max_value:
            max_value = value
            best_n = n
    return best_n, max_value

# Установим максимальное значение n для проверки
max_n = 10000
best_n, max_value = maximize_expression(max_n)

print(f"Натуральное число n, при котором выражение 1000^n / n! принимает максимальное значение: {best_n}")
print(f"Максимальное значение выражения: {max_value}")
