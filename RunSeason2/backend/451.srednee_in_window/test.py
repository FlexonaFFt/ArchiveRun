from decimal import Decimal, getcontext, ROUND_FLOOR

def max_average_subarray(n, k, array):
    getcontext().prec = 7
    getcontext().rounding = ROUND_FLOOR

    max_average = Decimal('-Infinity')
    current_sum = sum(array[:k])

    # Вычисляем максимальное среднее для подмассивов длины k
    max_average = max(max_average, Decimal(current_sum) / Decimal(k))

    # Вычисляем максимальное среднее для остальных подмассивов
    for i in range(k, n):
        current_sum += array[i] - array[i - k]
        max_average = max(max_average, Decimal(current_sum) / Decimal(k))

    return format(max_average, '.6f')

def main():
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    print(max_average_subarray(n, k, array))

if __name__ == '__main__':
    main()
