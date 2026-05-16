import sys
import datetime

weekdays = ['Monday', "Tuesday", 'Wednesday',
            "Thursday", 'Friday', "Saturday",
            'Sunday']

month_to_number = {
    "January": 1, 'February': 2, "March": 3,
    'April': 4, "May": 5, 'June': 6,
    "July": 7, 'August': 8, "September": 9,
    'October': 10, "November": 11, 'December': 12
}

def weekday_searcher():
    input_data = sys.stdin.read().strip().splitlines()
    for line in input_data:
        day, month, year = line.split()
        day = int(day)
        year = int(year)
        month = month_to_number[month]

        date = datetime.date(year, month, day)
        day_of_week = weekdays[date.weekday()]
        print(day_of_week)

if __name__ == '__main__':
    weekday_searcher()
