def solve(dates):
    if not dates:
        return 0, 0, 0

    min_temp = dates[0]
    max_diff, start_day, end_day = 0, 0, 0
    for day in range(1, len(dates)):
        if dates[day] < min_temp:
            min_temp = dates[day]
            start_day = day 
        today_diff = dates[day] - min_temp  
        if today_diff > max_diff:
            max_diff = today_diff 
            end_day = day 

    return max_diff, start_day, end_day

def main():
    dates = list(map(int, input().split())) 
    print(*solve(dates))

if __name__ == '__main__':
    main()
