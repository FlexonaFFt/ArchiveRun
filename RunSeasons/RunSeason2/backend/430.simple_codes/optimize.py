# Решение ломается на 11 тесте (TL)
from collections import defaultdict
def find_simple_codes(n, items):
    digit_mask_count = defaultdict(int)
    total_pairs = 0

    for item in items:
        current_mask = 0
        for digit in str(item):
            current_mask |= 1 << int(digit)

        for mask, count in digit_mask_count.items():
            if mask & current_mask:
                total_pairs += count
        digit_mask_count[current_mask] += 1

    return total_pairs

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(find_simple_codes(n, numbers))

if __name__ == '__main__':
    main()
