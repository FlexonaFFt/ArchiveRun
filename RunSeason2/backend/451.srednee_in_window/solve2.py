# Решение снова не проходит второй тест по округлению
def max_average_subarray(n, k, array):
    max_average = -float('inf')

    for length in range(k, n + 1):
        current_sum = sum(array[:length])
        max_average = max(max_average, current_sum / length)
        for i in range(length, n):
            current_sum += array[i] - array[i - length]
            max_average = max(max_average, current_sum / length)
    return f"{max_average:.6f}"

def main():
    n, k = map(int, input().split())
    string = list(map(int, input().split()))
    print(max_average_subarray(n, k, string))

if __name__ == '__main__':
    main()
