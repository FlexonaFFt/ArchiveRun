from bisect import bisect_left

def find_nearest_stop(n, stops, k, queries):
    rezults = []

    for x in queries:
        pos = bisect_left(stops, x)
        if pos < n and stops[pos] == x:
            rezults.append(pos + 1)
        else:
            left_dist = float('inf') if pos == 0 else x - stops[pos - 1]
            right_dist = float('inf') if pos == n else stops[pos] - x

            if left_dist <= right_dist:
                rezults.append(pos)
            else:
                rezults.append(pos + 1)

    return rezults

def main():
    n, k = map(int, input().split())
    stops = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    rezults = find_nearest_stop(n, stops, k, queries)
    for rezult in rezults:
        print(rezult)

if __name__ == '__main__':
    main()
