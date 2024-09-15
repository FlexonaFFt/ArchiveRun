def can_cut_segments(lengths, segments, K):
    counter = 0
    for length in lengths:
        counter += length // segments
    return counter >= K

def max_segments_length(lengths, N, K):
    left, right, max_length = 1, max(lengths), 0
    while left <= right:
        mid = (left + right) // 2
        if can_cut_segments(lengths, mid, K):
            max_length = mid
            left = mid + 1
        else:
            right = mid - 1
    return max_length

def main():
    N, K = map(int, input().split())
    lengths = [int(input().strip()) for _ in range(N)]
    print(max_segments_length(lengths, N, K))

if __name__ == '__main__':
    main()
