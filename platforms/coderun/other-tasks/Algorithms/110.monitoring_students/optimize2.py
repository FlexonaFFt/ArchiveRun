# Проходит все тесты кроме последнего
# Ошибка исполнения на последнем тесте (id: 12)
def monitored_func(N, M, ranges):
    marks = [0] * (N + 1)
    for b, e in ranges:
        marks[b] += 1
        if e + 1 < N:
            marks[e + 1] -= 1

    monitored_cnt, current_monitored = 0, 0
    for i in range(N):
        current_monitored += marks[i]
        if current_monitored > 0:
            monitored_cnt += 1

    return N - monitored_cnt

def main():
    N, M = map(int, input().split())
    ranges = [tuple(map(int, input().split())) for _ in range(M)]
    print(monitored_func(N, M, ranges))

if __name__ == '__main__':
    main()
