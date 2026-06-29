def function_read(n):
    rezult = n
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            rezult -= rezult // i
        i += 1
    if n > 1:
        rezult -= rezult // n
    return rezult

def main():
    n = int(input())
    rezult = function_read(n)
    print(rezult)

if __name__ == '__main__':
    main()
