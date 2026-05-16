def sliding_window(array, window_size):
    for i in range(len(array) - window_size + 1):
        yield arr[i:i + window_size]

def function(arr, window):
    max_sum = float("-inf")
    for window in sliding_window(arr, window):
        current_sum = sum(window)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

arr = [1, 2, 3, 4, 5]
window_size = 3
print(function(arr, window_size))

