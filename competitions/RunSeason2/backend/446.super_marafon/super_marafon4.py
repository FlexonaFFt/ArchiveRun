# Решение зашло
# Проблема была в отсутствии перехода на следующую неделю
def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def minutes_to_time(minutes):
    hours = (minutes // 60) % 24
    minutes = minutes % 60
    return f'{hours:02}:{minutes:02}'

def find_meeting_time(start1, start2, lap1, lap2):
    time1 = time_to_minutes(start1)
    time2 = time_to_minutes(start2)
    lap1 = time_to_minutes(lap1)
    lap2 = time_to_minutes(lap2)
    max_minutes = 14 * 24 * 60
    for _ in range(max_minutes):
        if time1 == time2:
            days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            day_of_week = days[(time1 // (24 * 60)) % 7]
            return day_of_week, minutes_to_time(time1)

        if time1 < time2:
            time1 += lap1
        else:
            time2 += lap2

    return "Never"

def main():
    start1 = input().strip()
    start2 = input().strip()
    lap1 = input().strip()
    lap2 = input().strip()
    result = find_meeting_time(start1, start2, lap1, lap2)
    if result == "Never":
        print(result)
    else:
        print(result[0])
        print(result[1])

if __name__ == '__main__':
    main()
