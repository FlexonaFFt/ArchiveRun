def count_divisors(n):
    divisor_count = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisor_count[j] += 1
    return divisor_count

def find_number_with_max_divisors(n):
    divisor_count = count_divisors(n)
    max_divisors = 0
    number_with_max_divisors = 0
    for i in range(1, n + 1):
        if divisor_count[i] > max_divisors or (divisor_count[i] == max_divisors and i > number_with_max_divisors):
            max_divisors = divisor_count[i]
            number_with_max_divisors = i

    return number_with_max_divisors, max_divisors

def main():
    n = int(input())
    result_number, result_divisors = find_number_with_max_divisors(n)
    print(result_number)
    print(result_divisors)

if __name__ == '__main__':
    main()
