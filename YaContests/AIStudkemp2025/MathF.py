import math

def calculate(a, b):
    denominator = 8 * math.sqrt(7*a) - 8 * math.sqrt(7*b)
    if denominator == 0:
        return 'Знаменатель не может быть равен нулю'

    numenator = 9 * math.sqrt(7*a) + 9 * math.sqrt(7*b)
    first_part = numenator / denominator
    second_part = (7*a - 3*b) / (28*a + 12*b - 8 * math.sqrt(21*a*b))
    result = first_part - second_part
    formatted_result = f"{result:.4f}"
    return formatted_result

a = 2
b = 3
result = calculate(a, b)
print("Результат:", result)
