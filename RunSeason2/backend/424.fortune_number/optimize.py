def next_happy_number(number):
    n = len(number)
    polovina = len(number) // 2

    while True:
        number = str(int(number[-1]) + 1) + number[:-1]
        if len(number) > polovina * 2:
            number = str("0" * (polovina * 2 - 1) + "1")

        left_sum = 0
        for digit in number[:polovina]:
            left_sum += int(digit)

        right_sum = 0
        for digit in number[polovina:]:
            right_sum += int(digit)

        if left_sum == right_sum and left_sum > 0:
            return number

def main():
    number = str(input())
    print(next_happy_number(number))

if __name__ == '__main__':
    main()
