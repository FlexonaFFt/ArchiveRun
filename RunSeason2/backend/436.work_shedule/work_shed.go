// Превышает лимит времени 47 тест
package main

import (
	"fmt"
	"sort"
)

type Task struct {
	deadline int
	stress   int
}

func minimizeStress(n int, tasks []Task) int {
	// Сортируем задачи по стрессу в порядке убывания
	sort.Slice(tasks, func(i, j int) bool {
		return tasks[i].stress > tasks[j].stress
	})

	days := make([]bool, 200001) // Массив для отслеживания занятых дней
	totalStress := 0

	for _, task := range tasks {
		deadline := task.deadline
		stress := task.stress

		// Ищем первый свободный день от deadline до 1
		for deadline > 0 && days[deadline] {
			deadline--
		}
		if deadline > 0 {
			days[deadline] = true // Занимаем этот день
		} else {
			totalStress += stress // Если нет доступного дня, добавляем стресс
		}
	}

	return totalStress
}

func main() {
	var n int
	fmt.Scan(&n)

	tasks := make([]Task, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&tasks[i].deadline, &tasks[i].stress)
	}

	result := minimizeStress(n, tasks)
	fmt.Println(result)
}
