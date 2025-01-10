def sliding_window_string(s, window_size):
    for i in range(len(s) - window_size + 1):
        yield s[i:i + window_size]

s = "abfceg"
window = 4
for window in sliding_window_string(s, window):
    print(window)

