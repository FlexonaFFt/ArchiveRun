# Не является решением задачи

'''Оптимизированный алгоритм
Используем события: Создаем два списка для хранения событий начала и конца наблюдения.
Сортируем события: Сортируем события по их позициям.
Проходим по событиям: Подсчитываем количество студентов под наблюдением, используя переменную-счетчик.'''

def monitored_func(N, M, ranges):
    events = []
    for b, e in ranges:
        events.append((b, 'start'))
        events.append((e + 1, 'end'))
    events.sort()

    monitored_cnt, current_monitored, last_position = 0, 0, 0
    for position, event_type in events:
        if current_monitored > 0:
            monitored_cnt += position - last_position
        if event_type == 'start':
            current_monitored += 1
        else:
            current_monitored -= 1

    return N - current_monitored

def main():
    N, M = map(int, input().split())
    ranges = [tuple(map(int, input().split())) for _ in range(M)]
    print(monitored_func(N, M, ranges))

if __name__ == '__main__':
    main()
