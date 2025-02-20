def find_nearest_stop(stops, x):

    left, right = 0, len(stops) - 1
    while left <= right:
        mid = (left + right) // 2
        if stops[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    left_stop = right

    left, right = 0, len(stops) - 1
    while left <= right:
        mid = (left + right) // 2
        if stops[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1
    right_stop = left

    if stops[left_stop] == x:
        return left_stop + 1
    elif left_stop >= 0 and right_stop < len(stops):
        return max(left_stop + 1, right_stop + 1)
    elif left_stop >= 0:
        return left_stop + 1
    else:
        return right_stop + 1


if __name__ == '__main__':
    n, k = map(int, input().split())
    stops = list(map(int, input().split()))
    coords = list(map(int, input().split()))

    for coord in coords:
        print(find_nearest_stop(stops, coord))
