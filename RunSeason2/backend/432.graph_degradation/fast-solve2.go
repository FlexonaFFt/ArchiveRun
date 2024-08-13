package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Item struct {
	vertex   int
	distance int
	index    int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].distance < pq[j].distance
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

func dijkstra(graph [][]int, start int) []int {
	n := len(graph)
	distances := make([]int, n)
	for i := range distances {
		distances[i] = 1<<63 - 1
	}
	distances[start] = 0

	pq := make(PriorityQueue, 0)
	heap.Push(&pq, &Item{vertex: start, distance: 0})

	for pq.Len() > 0 {
		item := heap.Pop(&pq).(*Item)
		currentVertex := item.vertex
		currentDistance := item.distance

		if currentDistance > distances[currentVertex] {
			continue
		}

		for neighbor, weight := range graph[currentVertex] {
			if weight != -1 {
				distance := currentDistance + weight
				if distance < distances[neighbor] {
					distances[neighbor] = distance
					heap.Push(&pq, &Item{vertex: neighbor, distance: distance})
				}
			}
		}
	}

	return distances
}

func countChangedDistances(graph [][]int, originalDistances []int) int {
	n := len(graph)
	maxChanged := 0

	for u := 0; u < n; u++ {
		for v := 0; v < n; v++ {
			if u != v && graph[u][v] != -1 {
				// Проверяем, является ли это ребро частью кратчайшего пути
				if originalDistances[u]+graph[u][v] == originalDistances[v] || originalDistances[v]+graph[u][v] == originalDistances[u] {
					// Удаляем ребро
					originalWeight := graph[u][v]
					graph[u][v] = -1
					graph[v][u] = -1

					// Пересчитываем расстояния
					newDistances := dijkstra(graph, 0)

					// Считаем количество изменённых расстояний
					changedCount := 0
					for i := range newDistances {
						if newDistances[i] != originalDistances[i] {
							changedCount++
						}
					}

					maxChanged = max(maxChanged, changedCount)

					// Восстанавливаем ребро
					graph[u][v] = originalWeight
					graph[v][u] = originalWeight
				}
			}
		}
	}

	return maxChanged
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(line))

	graph := make([][]int, n)
	for i := range graph {
		graph[i] = make([]int, n)
	}

	for i := 0; i < n; i++ {
		line, _ := reader.ReadString('\n')
		parts := strings.Split(strings.TrimSpace(line), " ")
		for j := range parts {
			weight, _ := strconv.Atoi(parts[j])
			graph[i][j] = weight
		}
	}

	originalDistances := dijkstra(graph, 0)
	result := countChangedDistances(graph, originalDistances)

	fmt.Println(result)
}
