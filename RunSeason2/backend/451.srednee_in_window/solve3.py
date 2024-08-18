# TL: Тест 4 > 1 sec
from decimal import Decimal, getcontext, ROUND_FLOOR

def max_average_subarray(n, k, array):
    getcontext().prec = 7
    getcontext().rounding = ROUND_FLOOR
    max_average = Decimal('-Infinity')

    for length in range(k, n + 1):
        current_sum = sum(array[:length])
        max_average = max(max_average, Decimal(current_sum) / Decimal(length))
        for i in range(length, n):
            current_sum += array[i] - array[i - length]
            max_average = max(max_average, Decimal(current_sum) / Decimal(length))
    return format(max_average, '.6f')

def main():
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    print(max_average_subarray(n, k, array))

if __name__ == '__main__':
    main()
