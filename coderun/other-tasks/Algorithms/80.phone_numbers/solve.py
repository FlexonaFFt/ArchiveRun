# Не проходит закрытый тест (id: 5)
def normilize_number(number):
    digits = ''.join(filter(str.isdigit, number))
    if digits.startswith('8'):
        return '7' + digits[1:]
    elif digits.startswith('7'):
        return digits
    else:
        return '7495' + digits

def sravnivatel_of_numbers(input_number, all_numbers):
    normilize_input_number, results = normilize_number(input_number), []
    for number in all_numbers:
        normilize_numb = normilize_number(number)
        if normilize_numb == normilize_input_number:
            results.append("YES")
        else:
            results.append("NO")
    return results

def main():
    input_number = input().strip()
    all_numbers = [input().strip() for _ in range(3)]
    results = sravnivatel_of_numbers(input_number, all_numbers)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
