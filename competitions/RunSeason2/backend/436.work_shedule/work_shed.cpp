// Неправильный ответ 46 тест
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Task {
    int deadline;
    int stress;
};

int minimizeStress(int n, vector<Task>& tasks) {
    // Сортируем задачи по стрессу в порядке убывания
    sort(tasks.begin(), tasks.end(), [](const Task& a, const Task& b) {
        return a.stress > b.stress;
    });

    vector<bool> days(200001, false); // Массив для отслеживания занятых дней
    int totalStress = 0;

    for (const auto& task : tasks) {
        int deadline = task.deadline;
        int stress = task.stress;

        // Ищем первый свободный день от deadline до 1
        while (deadline > 0 && days[deadline]) {
            deadline--;
        }
        if (deadline > 0) {
            days[deadline] = true; // Занимаем этот день
        } else {
            totalStress += stress; // Если нет доступного дня, добавляем стресс
        }
    }

    return totalStress;
}

int main() {
    int n;
    cin >> n;

    vector<Task> tasks(n);
    for (int i = 0; i < n; i++) {
        cin >> tasks[i].deadline >> tasks[i].stress;
    }

    int result = minimizeStress(n, tasks);
    cout << result << endl;

    return 0;
}
