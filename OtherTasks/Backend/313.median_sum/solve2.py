import heapq

def find_median_sum(X):
    max_heap = []  # для хранения нижней половины
    min_heap = []  # для хранения верхней половины
    median_sum = 0

    for i in range(len(X)):
        # Добавляем новый элемент в max_heap (как отрицательное число)
        heapq.heappush(max_heap, -X[i])

        # Переносим наибольший элемент из max_heap в min_heap
        if len(max_heap) > 0 and len(min_heap) > 0 and -max_heap[0] > min_heap[0]:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # Если max_heap имеет больше элементов, чем min_heap, перемещаем элемент
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Текущая медиана
        median = -max_heap[0]
        median_sum += median

    return median_sum

# Пример использования:
N = int(input())
X = list(map(int, input().split()))
print(find_median_sum(X))
