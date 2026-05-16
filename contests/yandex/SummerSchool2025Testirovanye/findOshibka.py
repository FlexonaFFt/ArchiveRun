def find_largest_number(numbers):
    if not numbers: # Обработка пустого списка
        return None

    largest = numbers[0]  # инициализируем первым элементом

    for num in numbers:
        if num > largest:
            largest = num

    return largest

def main():
    import sys
    input_data = sys.stdin.read().strip()

    if not input_data:  # если ввод пустой
        print("")  # или можно вернуть None или другое значение по умолчанию
        return

    numbers = list(map(int, input_data.split()))

    largest = find_largest_number(numbers)
    print(largest)

if __name__ == "__main__":
    main()
