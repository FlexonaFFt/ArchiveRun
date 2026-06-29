# Решение не проходит второй открытый тест
def find_winner_func(n, throws):
    max_position = 0
    for i in range(n):
        if throws[i] % 10 == 5:
            if i > 0 and throws[i - 1] > throws[i]:
                if i < n - 1 and throws[i + 1] < throws[i]:
                    place = sum(1 for throw in throws if throw > throws[i])
                    max_position = max(max_position, place + 1)
    return max_position

def main():
    n = int(input())
    array = list(map(int, input().split()))
    print(find_winner_func(n, array))

if __name__ == '__main__':
    main()
