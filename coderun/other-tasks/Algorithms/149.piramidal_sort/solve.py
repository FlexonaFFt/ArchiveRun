def heapify(numbers, n, i):
    largest, left, right = i, 2 * i + 1, 2 * i + 2
    if left < n and numbers[left] > numbers[largest]:
        largest = left
    if right < n and numbers[right] > numbers[largest]:
        largest = right
    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        heapify(numbers, n, largest)

def piramidal(n, numbers):
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)
    return numbers

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(*piramidal(n, numbers))

if __name__ == '__main__':
    main()
