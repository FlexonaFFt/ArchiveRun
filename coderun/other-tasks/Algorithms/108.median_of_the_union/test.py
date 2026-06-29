def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        median = sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2
    return median

def find_numb_mid(numbers):
    median = find_median(numbers)
    closest_number = min(numbers, key=lambda x: abs(x - median))
    return closest_number

def main():
    lest = list(map(int, input().split()))
    print(find_numb_mid(lest))

if __name__ == '__main__':
    main()
