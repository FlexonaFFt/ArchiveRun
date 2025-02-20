# Решение зашло (Как же это было тяжело...)
def max_average_subarray(n, k, array):
    # Если длина подмассива равна 1, то максимальное среднее - это максимальный элемент массива
    if k == 1:
        return format(max(array), '.6f')

    def can_find_subarray_with_average_greater_than(mid):
        prefix_sum = [0] * (n + 1)
        min_prefix_sum = 0

        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + array[i - 1] - mid
            if i >= k and prefix_sum[i] - min_prefix_sum >= 0:
                return True
            if i >= k:
                min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])

        return False

    left, right = min(array), max(array)
    while right - left > 1e-6:
        mid = (left + right) / 2
        if can_find_subarray_with_average_greater_than(mid):
            left = mid
        else:
            right = mid

    return format(left, '.6f')

def main():
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    print(max_average_subarray(n, k, array))

if __name__ == '__main__':
    main()
