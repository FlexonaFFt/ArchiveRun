from datetime import datetime, timedelta

def time_to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

def minutes_to_time(minutes):
    h = minutes // 60 % 24
    m = minutes % 60
    return f"{h:02}:{m:02}"

def lcm(a, b):
    from math import gcd
    return abs(a * b) // gcd(a, b)

def find_meeting_time(andrey_start, boris_start, andrey_time, boris_time):
    andrey_start_minutes = time_to_minutes(andrey_start)
    boris_start_minutes = time_to_minutes(boris_start)
    andrey_time_minutes = time_to_minutes(andrey_time)
    boris_time_minutes = time_to_minutes(boris_time)

    # Нахождение НОК времени круга
    period = lcm(andrey_time_minutes, boris_time_minutes)

    # Проверка на совпадение
    for minute in range(0, 7 * 24 * 60):  # Проверяем в течение недели
        andrey_finish = andrey_start_minutes + minute * andrey_time_minutes
        boris_finish = boris_start_minutes + minute * boris_time_minutes

        if (andrey_finish % period == andrey_start_minutes % period) and (boris_finish % period == boris_start_minutes % period):
            total_minutes = min(andrey_finish, boris_finish)
            day_of_week = total_minutes // (24 * 60)
            time_of_day = total_minutes % (24 * 60)

            days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            return f"{days_of_week[day_of_week]}\n{minutes_to_time(time_of_day)}"

    return "Never"

def main():
    andrey_start = input().strip()
    boris_start = input().strip()
    andrey_time = input().strip()
    boris_time = input().strip()

    print(find_meeting_time(andrey_start, boris_start, andrey_time, boris_time))

if __name__ == '__main__':
    main()
