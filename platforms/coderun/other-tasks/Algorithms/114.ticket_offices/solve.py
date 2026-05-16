# Не является решением задачи
# Проходит третий открытый тест
def time_in_minutes(hours, minutes):
    return hours * 60 + minutes

def find_time(n, list):
    start_time, end_time = 0, 24 * 60
    for item in list:
        start_h, start_m, end_h, end_m = item
        start_minutes = time_in_minutes(start_h, start_m)
        end_minutes = time_in_minutes(end_h, end_m)

        if start_minutes <= end_minutes:
            start_time = max(start_time, start_minutes)
            end_time = min(end_time, end_minutes)
        else:
            start_time = max(start_time, start_minutes)
            end_time = min(end_time, end_minutes + 1440)
    return max(0, end_time - start_time)

def main():
    n = int(input())
    list = []
    for _ in range(n):
        iter = tuple(map(int, input().split()))
        list.append(iter)
    print(find_time(n, list))

if __name__ == '__main__':
    main()
