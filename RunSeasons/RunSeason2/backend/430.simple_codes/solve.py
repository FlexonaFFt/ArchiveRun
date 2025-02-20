# Решение ломается на 11 тесте (TL)
def find_simple_codes(n, items):

    digit_sets = []
    pair_count = 0

    for i in range(n):
        current_digits = set(str(items[i]))
        for digit_set in digit_sets:
            if current_digits & digit_set:
                pair_count += 1
        digit_sets.append(current_digits)
    return pair_count

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(find_simple_codes(n, numbers))

if __name__ == '__main__':
    main()
