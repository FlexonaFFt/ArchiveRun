# WA на тесте id: 5
import heapq

def find_medians_sum(n, arr):
    lower_half = []
    upper_half = []
    medians_sum = 0

    for i in range(n):
        num = arr[i]
        if len(lower_half) == 0 or num <= -lower_half[0]:
            heapq.heappush(lower_half, -num)
        else:
            heapq.heappush(upper_half, num)

        if len(lower_half) > len(upper_half) + 1:
            heapq.heappush(upper_half, -heapq.heappop(lower_half))

        if len(lower_half) >= len(upper_half):
            medians_sum += -lower_half[0]
        else:
            medians_sum += upper_half[0]

    return medians_sum

def main():
    n = int(input())
    array = list(map(int, input().split()))
    rezult = find_medians_sum(n, array)
    print(rezult)

if __name__ == '__main__':
    main()
