# Решение также ломается на тесте (WA id: 9)
def main():
    input_numbers = list(map(int, input().split()))
    sorted_numbers = sorted(filter(lambda x: x != 0, input_numbers))
    for number in sorted_numbers:
        print(number)

if __name__ == '__main__':
    main()
