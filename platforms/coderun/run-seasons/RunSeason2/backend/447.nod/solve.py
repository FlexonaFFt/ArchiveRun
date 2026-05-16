# Ломается на втором тесте, скорее всего проблема в
# том, что программа перемножает числовые отрезки
from collections import Counter

def factorize(num):
    i = 2
    factors = Counter()
    while i * i <= num:
        while (num % i) == 0:
            factors[i] += 1
            num //= i
        i += 1
    if num > 1:
        factors[num] += 1
    return factors

def last_9_digits_of_gcd_optimized(a_list, b_list):
    factors_A = Counter()
    factors_B = Counter()

    for a in a_list:
        factors_A += factorize(a)

    for b in b_list:
        factors_B += factorize(b)

    common_factors = factors_A & factors_B
    gcd_value = 1
    for prime in common_factors:
        gcd_value *= prime ** common_factors[prime]
        gcd_value %= 10**9

    return str(gcd_value)

def main():
    n = int(input())
    list1 = list(map(int, input().split()))
    k = int(input())
    list2 = list(map(int, input().split()))
    print(last_9_digits_of_gcd_optimized(list1, list2))

if __name__ == '__main__':
    main()
