def sliding_window_string(s, window_size):
    for i in range(len(s) - window_size + 1):
        yield s[i:i + window_size]

def function(string, window):
    result = []
    for window in sliding_window_string(string, window):
        if 'a' in window:
            result.append(window)
    return result

s = "abracadabra"
window_size = 3
print(function(s, window_size))

