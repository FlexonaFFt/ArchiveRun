# Решение проходит большинство тестов
# Но выходит за лимиты времени
# Довольно непростая задача для меня, самостоятельно решить не смог

import sys
import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(n):
            weight = graph[current_vertex][neighbor]
            if weight != -1:
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
            if u != v and graph[u][v] != -1:
                original_weight = graph[u][v]
                graph[u][v] = -1
                graph[v][u] = -1

                new_distances = dijkstra(graph, 0)
                changed_count = sum(1 for i in range(n) if new_distances[i] != original_distances[i])

                max_changed = max(max_changed, changed_count)
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

    original_distances = dijkstra(graph, 0)
    result = count_changed_distances(graph, original_distances)
    print(result)

if __name__ == "__main__":
    main()
