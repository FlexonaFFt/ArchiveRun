def finder(numbers):
    counter = 0
    for n in range(1, len(numbers) - 1):
        if numbers[n] > numbers[n + 1] and numbers[n] > numbers[n - 1]:
            counter += 1
    return counter

def main():
    numbers = list(map(int, input().split()))
    print(finder(numbers))

if __name__ == '__main__':
    main()
