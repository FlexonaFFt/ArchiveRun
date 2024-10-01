def parse_time(time_str):
    hh, mm, ss = map(int, time_str.split(":"))
    return hh * 3600 + mm * 60 + ss

def format_time(seconds):
    hh = (seconds // 3600) % 24
    mm = (seconds % 3600) // 60
    ss = seconds % 60
    return f'{hh:02}:{mm:02}:{ss:02}'

def calculate_correct_time(A, B, C):
    A_seconds = parse_time(A)
    B_seconds = parse_time(B)
    C_seconds = parse_time(C)
    delay = (C_seconds - A_seconds) - (B_seconds - A_seconds)
    correct_time = B_seconds + (delay // 2)
    return format_time(correct_time)

def main():
    A = input().strip()
    B = input().strip()
    C = input().strip()
    print(calculate_correct_time(A, B, C))

if __name__ == '__main__':
    main()
