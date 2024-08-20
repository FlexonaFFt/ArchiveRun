# Решение ломается на 12 тесте
def find_closest_number(input_number):
    def sum_of_half_digits(number):
        half = len(number) // 2
        first_half = sum(int(digit) for digit in number[:half])
        second_half = sum(int(digit) for digit in number[half:])
        return first_half, second_half

    def is_sum_equal(number):
        first_half, second_half = sum_of_half_digits(number)
        return first_half == second_half

    number = str(int(input_number) + 1).zfill(len(input_number))
    while True:
        if number != '0' * len(input_number) and is_sum_equal(number):
            return number
        number = str(int(number) + 1).zfill(len(input_number))
        if len(number) > len(input_number):
            number = '0' * len(input_number)

def main():
    number = str(input())
    print(find_closest_number(number))

if __name__ == '__main__':
    main()
