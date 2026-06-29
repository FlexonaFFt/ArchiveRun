def find_median(N, L, numbers):
    result = []
    for i in range(N):
        for j in range(i + 1, N):
            merged = sorted(numbers[i] + numbers[j])
            result.append(merged[L - 1])
    return result

def main():
    N, L = map(int, input().split())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    result = find_median(N, L, numbers)
    for item in result:
        print(item)

if __name__ == '__main__':
    main()
