Для решения этой задачи мы можем использовать алгоритм поиска в ширину (BFS), который хорошо подходит для нахождения кратчайшего пути в графах. В нашем случае шахматная доска будет представлять собой граф, где каждая клетка — это узел, а возможные ходы коня — это рёбра между узлами.

## Шаги решения

1. **Преобразование координат**: Преобразуем шахматные координаты (например, `a1`, `h8`) в числовые индексы, чтобы упростить работу с ними.
2. **Определение возможных ходов коня**: Конь может двигаться в 8 различных направлениях.
3. **Поиск с помощью BFS**: Мы будем одновременно перемещать обоих коней, и если они окажутся на одной клетке, мы завершим поиск.

Вот пример кода на Python, который реализует описанный алгоритм:

```python
from collections import deque

def chess_position_to_indices(pos):
    column, row = pos
    return ord(column) - ord('a'), int(row) - 1

def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def knight_moves(position):
    x, y = position
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    return [(x + dx, y + dy) for dx, dy in moves if is_valid(x + dx, y + dy)]

def min_moves_to_meet(start1, start2):
    start1 = chess_position_to_indices(start1)
    start2 = chess_position_to_indices(start2)
    
    queue = deque([(start1[0], start1[1], start2[0], start2[1], 0)])  # (x1, y1, x2, y2, moves)
    visited = set()
    visited.add((start1[0], start1[1], start2[0], start2[1]))

    while queue:
        x1, y1, x2, y2, moves = queue.popleft()

        if (x1, y1) == (x2, y2):
            return moves

        for nx1, ny1 in knight_moves((x1, y1)):
            for nx2, ny2 in knight_moves((x2, y2)):
                if (nx1, ny1, nx2, ny2) not in visited:
                    visited.add((nx1, ny1, nx2, ny2))
                    queue.append((nx1, ny1, nx2, ny2, moves + 1))

    return -1

# Ввод данных
start_pos1, start_pos2 = input().strip().split()
result = min_moves_to_meet(start_pos1, start_pos2)
print(result)
```

## Объяснение кода

1. **Функция `chess_position_to_indices`**: Преобразует шахматные координаты в числовые индексы.
2. **Функция `is_valid`**: Проверяет, находится ли клетка на доске.
3. **Функция `knight_moves`**: Генерирует все возможные ходы коня из текущей позиции.
4. **Функция `min_moves_to_meet`**: Реализует BFS для нахождения минимального количества ходов, необходимых для встречи коней.

## Пример использования

При запуске программы она ожидает ввод координат двух коней, например:
```
a1 a3
```
И выведет:
```
1
```

Этот код должен успешно решать задачу, учитывая все возможные ситуации.
