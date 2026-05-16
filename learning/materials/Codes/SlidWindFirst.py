def sliding_window(array, window_size):
    for i in range(len(array) - window_size + 1):
        yield arr[i:i + window_size]

arr = [1, 2, 3, 4, 5]
window = 3
for window in sliding_window(arr, window):
    print(window)

