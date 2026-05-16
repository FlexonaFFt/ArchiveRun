import sys
import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(n):
            weight = graph[current_vertex][neighbor]
            if weight != -1:  # Если ребро существует
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def count_changed_distances(graph, original_distances):
    n = len(graph)
    max_changed = 0

    for u in range(n):
        for v in range(n):
            if u != v and graph[u][v] != -1:  # Если существует ребро u-v
                # Удаляем ребро u-v
                original_weight = graph[u][v]
                graph[u][v] = -1
                graph[v][u] = -1

                # Пересчитываем расстояния
                new_distances = dijkstra(graph, 0)

                # Считаем количество изменённых расстояний
                changed_count = sum(1 for i in range(n) if new_distances[i] != original_distances[i])

                # Сравниваем с максимальным
                max_changed = max(max_changed, changed_count)

                # Восстанавливаем ребро
                graph[u][v] = original_weight
                graph[v][u] = original_weight

    return max_changed

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    graph = []
    
    for i in range(n):
        row = list(map(int, data[i + 1].split()))
        graph.append(row)

    # Находим начальные расстояния от вершины 1 (индекс 0)
    original_distances = dijkstra(graph, 0)

    # Считаем максимальное количество изменённых расстояний
    result = count_changed_distances(graph, original_distances)

    print(result)

if __name__ == "__main__":
    main()
