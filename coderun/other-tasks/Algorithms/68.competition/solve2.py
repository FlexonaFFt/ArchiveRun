# Возникает неправильный ответ на закрытом тесте (id: 10)
def find_winner_func(n, array):
    max_position = 0
    for i in range(1, n - 1):
        if array[i] % 10 == 5:
            if max(array[:i]) >= array[i]:
                if array[i] > array[i + 1]:
                    max_position = max(max_position, sum(1 for arr in array if arr > array[i]) + 1)
    return max_position

def main():
    n = int(input())
    array = list(map(int, input().split()))
    print(find_winner_func(n, array))

if __name__ == '__main__':
    main()
