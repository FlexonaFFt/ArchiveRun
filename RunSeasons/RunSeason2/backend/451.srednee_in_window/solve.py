# Решение не проходит 2 тест
def find_avarage_subarray(string, k):
    n = len(string)
    max_avg= float("-inf")
    current_sum = sum(string[:k])

    max_avg = current_sum / k
    for i in range(k, n):
        current_sum = current_sum - string[i - k] + string[i]
        current_avg = current_sum / k
        max_avg = max(max_avg, current_avg)

    return format(max_avg, '.6f')

def main():
    n, k = map(int, input().split())
    string = list(map(int, input().split()))
    print(find_avarage_subarray(string, k))

if __name__ == '__main__':
    main()
