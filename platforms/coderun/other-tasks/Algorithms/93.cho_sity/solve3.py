# Решение превышает лимит времени (id: 38)
def finder(n, r, numbers):
    counter = 0
    left = 0

    # Проходим по всем памятникам с правым указателем
    for right in range(n):
        # Увеличиваем левый указатель, пока разница не станет больше r
        while left < right and numbers[right] - numbers[left] > r:
            left += 1
        # Все индексы от left до right - 1 могут образовать пару с right
        counter += left

    return counter

def main():
    n, r = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(finder(n, r, numbers))

if __name__ == '__main__':
    main()
