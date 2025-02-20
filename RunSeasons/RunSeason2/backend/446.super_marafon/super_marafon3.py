def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def minutes_to_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02}:{minutes:02}"

def find_meeting_time(andrew_start, boris_start, andrew_time, boris_time):
    andrew_start_minutes = time_to_minutes(andrew_start)
    boris_start_minutes = time_to_minutes(boris_start)
    andrew_time_minutes = time_to_minutes(andrew_time)
    boris_time_minutes = time_to_minutes(boris_time)

    from math import gcd
    def lcm(x, y):
        return x * y // gcd(x, y)

    lap_lcm = lcm(andrew_time_minutes, boris_time_minutes)
    for i in range(0, lap_lcm + 1, andrew_time_minutes):
        andrew_finish_time = andrew_start_minutes + i
        if andrew_finish_time >= 1440:
            andrew_finish_time %= 1440

        if andrew_finish_time >= boris_start_minutes and (andrew_finish_time - boris_start_minutes) % boris_time_minutes == 0:
            day_of_week = (andrew_finish_time // 1440) % 7
            days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            return days[day_of_week], minutes_to_time(andrew_finish_time)

    return "Never"

def main():
    andrew_start = input().strip()
    boris_start = input().strip()
    andrew_time = input().strip()
    boris_time = input().strip()

    result = find_meeting_time(andrew_start, boris_start, andrew_time, boris_time)
    if result == "Never":
        print(result)
    else:
        print(result[0])
        print(result[1])

if __name__ == '__main__':
    main()
