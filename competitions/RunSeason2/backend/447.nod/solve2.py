from math import gcd

def get_last_9_digits_of_gcd(n, a_list, m, b_list):
    A = int(''.join(map(str, a_list)))
    B = int(''.join(map(str, b_list)))
    gcd_value = gcd(A, B)
    return str(gcd_value)

def main():
    n = int(input())
    list1 = list(map(int, input().split()))
    k = int(input())
    list2 = list(map(int, input().split()))
    print(get_last_9_digits_of_gcd(n, list1, k, list2))

if __name__ == '__main__':
    main()
