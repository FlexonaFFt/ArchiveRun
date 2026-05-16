def finder(n, r, numbers):
    from itertools import combinations
    counter, srt_numbers = 0, sorted(numbers, reverse=True)
    for num1, num2 in combinations(srt_numbers, 2):
        if abs(num1 - num2) == r or abs(num2 - num1) == r:
            counter += 1
    return counter

def main():
    n, r = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(finder(n, r, numbers))

if __name__ == '__main__':
    main()
