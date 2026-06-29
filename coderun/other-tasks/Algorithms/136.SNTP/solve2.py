def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def seconds_to_time(seconds):
    seconds %= 86400
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f'{h:02}:{m:02}:{s:02}'

A = input().strip()
B = input().strip()
C = input().strip()

A_seconds = time_to_seconds(A)
B_seconds = time_to_seconds(B)
C_seconds = time_to_seconds(C)

delta_seconds = (C_seconds - A_seconds) // 2
exact_time_seconds = B_seconds + delta_seconds
print(seconds_to_time(exact_time_seconds))
