# Все также не проходит закрытый тест (id: 5)
def normilize_number(number):
    import re
    cleaned = re.sub(r'[^0-9()]', '', number)
    if cleaned.startswith('8'):
        cleaned =  '7' + cleaned[1:]
    elif cleaned.startswith('+7'):
        cleaned = cleaned[2:]
    if cleaned.startswith('7'):
        cleaned = cleaned[1:]

    match = re.match(r'(\d{3})(\d{7})', cleaned)
    if match:
        code = match.group(1)
        number = match.group(2)
    else:
        code = '495'
        number = cleaned[-7:]

    return code, number

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
