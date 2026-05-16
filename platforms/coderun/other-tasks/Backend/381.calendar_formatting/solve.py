def print_calendar(n_days, start_weekday):
    weekdays = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
        'Thursday': 3, 'Friday': 4, 'Saturday': 5,
        'Sunday': 6
    }

    start_index = weekdays[start_weekday]
    weeks = []
    current_week = ['..'] * 7
    for day in range(1, n_days + 1):
        if day == 1:
            current_week[start_index] = f'..'
        current_week[(start_index + day - 1) % 7] = f'.{day}' if day < 10 else str(day)

        if (start_index + day) % 7 == 0:
            weeks.append(current_week)
            current_week = ['..'] * 7

    if any(day != '..' for day in current_week):
        weeks.append(current_week)

    if len(weeks) > 0:
        last_week = weeks[-1]
        while last_week[-1] == '..':
            last_week.pop()

    for week in weeks:
        print(' '.join(week))

def main():
    input_data = input().strip().split()
    n_days = int(input_data[0])
    start_weekday = input_data[1]
    print_calendar(n_days, start_weekday)

if __name__ == '__main__':
    main()
