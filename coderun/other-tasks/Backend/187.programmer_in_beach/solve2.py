def find_min_xor(tests):
    rezults = []
    for test in tests:
        n, a = test
        a.sort()
        min_xor = float('inf')

        for i in range(n - 1):
            current_xor = a[i] ^ a[i + 1]
            min_xor = min(min_xor, current_xor)
        rezults.append(min_xor)
    return rezults

def main():
    tests = []
    for _ in range(int(input())):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        tests.append((n, a))
    results = find_min_xor(tests)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
