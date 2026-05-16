# Неоптимизированный алгоритм
# Ломается на 6 закрытом тесте (id: 7)
def monitored_func(N, M, ranges):
    monitored = [False] * N
    for b, e in ranges:
        for i in range(b, e + 1):
            monitored[i] = True
    return monitored.count(False)

def main():
    N, M = map(int, input().split())
    ranges = [tuple(map(int, input().split())) for _ in range(M)]
    print(monitored_func(N, M, ranges))

if __name__ == '__main__':
    main()
