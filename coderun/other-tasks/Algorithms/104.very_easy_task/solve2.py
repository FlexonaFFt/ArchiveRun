# Решение выдает неправильный ответ, всегда на 1 меньше нужного
import heapq

def find_min_time_func(n, time1, time2):
    heap = []
    heapq.heappush(heap, 0)
    copies, time = 0, 0

    while copies < n:
        time = heapq.heappop(heap)
        copies += 1
        heapq.heappush(heap, time + time1)
        heapq.heappush(heap, time + time2)
    return time

def main():
    n, time1, time2 = map(int, input().split())
    print(find_min_time_func(n, time1, time2))

if __name__ == '__main__':
    main()
