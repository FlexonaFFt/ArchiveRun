# Программа неправильно подсчитывает задачи
def min_total_complexy(n, a, b, c):
    prefix_a = [0] * (n + 1)
    prefix_b = [0] * (n + 1)
    prefix_c = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]
        prefix_c[i] = prefix_c[i - 1] + c[i - 1]

    min_complexy = float('inf')
    for i in range(1, n - 1):
        for j in range(i, n):
            total_complexy = prefix_a[i] + prefix_b[j] - prefix_b[i] + prefix_c[n] - prefix_c[j]
            min_complexy = min(min_complexy, total_complexy)
    return min_complexy

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    rezult = min_total_complexy(n, a, b, c)
    print(rezult)

if __name__ == "__main__":
    main()
