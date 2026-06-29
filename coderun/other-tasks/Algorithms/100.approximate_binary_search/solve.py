def find_closest(arr, target):
    import bisect
    pos = bisect.bisect_left(arr, target)
    closest_value = None

    if pos < len(arr):
        closest_value = arr[pos]
    if pos > 0:
        if closest_value is None or abs(arr[pos - 1] - target) < abs(closest_value - target):
            closest_value = arr[pos - 1]
        elif abs(arr[pos - 1] - target) == abs(closest_value - target):
            closest_value = min(closest_value, arr[pos - 1])
    return closest_value

def main():
    n, k = map(int, input().split())
    first_array = list(map(int, input().split()))
    second_array = list(map(int, input().split()))
    results = []
    for number in second_array:
        closest = find_closest(first_array, number)
        results.append(closest)
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    main()
