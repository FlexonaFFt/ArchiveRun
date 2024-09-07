# Решение зачтено
def time_in_minutes(hours, minutes):
    return hours * 60 + minutes

def find_time(n, list):
    minutes = [0] * 1440
    for item in list:
        open_hour, open_minute, close_hour, close_minute = item
        open_time = time_in_minutes(open_hour, open_minute)
        close_time = time_in_minutes(close_hour, close_minute)

        if open_time < close_time:
            for minute in range(open_time, close_time):
                minutes[minute] += 1
        else:
            for minute in range(open_time, 1440):
                minutes[minute] += 1
            for minute in range(0, close_time):
                minutes[minute] += 1

    total_minutes = sum(1 for minute in minutes if minute == n)
    return total_minutes

def main():
    n = int(input())
    list = []
    for _ in range(n):
        iter = tuple(map(int, input().split()))
        list.append(iter)
    print(find_time(n, list))

if __name__ == '__main__':
    main()
