# Решение не проходит лимит времени
def next_happy_number(number):
    n = len(str(number)) // 2

    while True:
        number += 1
        if len(str(number)) > n * 2:
            number = int('1' + '0' * (n * 2))

        left_sum = sum(int(digit) for digit in str(number)[:n])
        right_sum = sum(int(digit) for digit in str(number)[n:])

        if left_sum == right_sum and left_sum > 0:
            return number

def main():
    number = int(input())
    print(next_happy_number(number))

if __name__ == '__main__':
    main()
