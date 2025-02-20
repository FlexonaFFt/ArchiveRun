def max_equal_substrings(s):
    n = len(s)
    max_count = 1

    for length in range(1, n + 1):
        if n % length == 0:
            parts = [s[i:i+length] for i in range(0, n, length)]
            if len(set(parts)) == 1:  # Все части должны быть одинаковы
                max_count = n // length

    return max_count

def main():
    string = input()
    print(max_equal_substrings(string))

if __name__ == '__main__':
    main()
