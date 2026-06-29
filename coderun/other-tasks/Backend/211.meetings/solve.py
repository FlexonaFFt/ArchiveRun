from datetime import datetime, timedelta
meeting_list = {}

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def format_time(time_obj):
    return time_obj.strftime("%H:%M")

def is_overlap(start1, end1, start2, end2):
    return not (end1 <= start2 or start1 >= end2)

def add_meeting(day, time_str, duration, participans):
    global meetings
    start_time = parse_time(time_str)
    end_time = start_time + timedelta(minutes=duration)

    if day not in meeting_list:
        meeting_list[day] = {}
    conflicting_names = []

    for name in participans:
        if name not in meeting_list[day]:
            meeting_list[day][name] = []
        for (s, e, p) in meeting_list[day][name]:
            if is_overlap(start_time, end_time, s, e):
                conflicting_names.append(name)
                break

    if conflicting_names:
        print("FAIL")
        print(" ".join(conflicting_names))
    else:
        print("OK")
        for name in participans:
            meeting_list[day][name].append((start_time, end_time, participans))

def print_meetings(day, name):
    if day in meeting_list and name in meeting_list[day]:
        sorted_meetings = sorted(meeting_list[day][name])
        for (s, e, p) in sorted_meetings:
            print(f"{format_time(s)} {int((e-s).total_seconds() // 60)} {" ".join(p)}")

def main():
    n = int(input().strip())
    for _ in range(n):
        command = input().strip().split()

        if command[0] == "APPOINT":
            day = int(command[1])
            time = command[2]
            duration = int(command[3])
            k = int(command[4])
            participants = command[5:5+k]
            add_meeting(day, time, duration, participants)

        elif command == "PRINT":
            day = int(command[1])
            name = command[2]
            print_meetings(day, name)
    print()

if __name__ == '__main__':
    main()
