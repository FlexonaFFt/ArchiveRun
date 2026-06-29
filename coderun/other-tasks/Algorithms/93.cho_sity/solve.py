# Решение ломается на закрытом тесте (id: 3)
def finder(n, r, numbers):
    counter, srt_numbers = 0, set(numbers)
    for num in numbers:
        if (num + r) in srt_numbers:
            counter += 1
        if (num - r) in srt_numbers:
            counter += 1
    return counter

def main():
    n, r = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(finder(n, r, numbers))

if __name__ == '__main__':
    main()
