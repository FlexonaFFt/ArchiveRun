# Метод скользящего окна

Метод скользящего окна (или скользящего среза) часто используется для обработки последовательностей данных, таких как списки или строки, когда нужно проанализировать все возможные подпоследовательности определенной длины.

## Простой пример 

Рассмотрим простой пример: у нас есть список чисел, и мы хотим найти все подпоследовательности длины 3.

```python
def sliding_window(array, window_size):
    for i in range(len(array) - window_size + 1):
        yield arr[i:i + window_size]

arr = [1, 2, 3, 4, 5]
window = 3
for window in sliding_window(arr, window):
    print(window)
```

## Более сложный пример

Теперь рассмотрим более сложный пример: у нас есть строка, и мы хотим найти все подстроки длины 4.

```python
def sliding_window_string(s, window_size):
    for i in range(len(s) - window_size + 1):
        yield s[i:i + window_size]

s = "abfceg"
window = 4
for window in sliding_window_string(s, window):
    print(window)
```

# Применение метода скользящего окна для решения задачи

Рассмотрим задачу: у нас есть список чисел, и мы хотим найти максимальную сумму всех подпоследовательностей длины 3.

```python
def sliding_window(array, window_size):
    for i in range(len(array) - window_size + 1):
        yield arr[i:i + window_size]

def function(arr, window):
    max_sum = float("-inf")
    for window in sliding_window(arr, window):
        current_sum = sum(window)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

arr = [1, 2, 3, 4, 5]
window_size = 3
print(function(arr, window_size))
```

# Применение метода скользящего окна для поиска подстроки

Рассмотрим задачу: у нас есть строка, и мы хотим найти все подстроки длины 3, которые содержат букву 'a'.

```python
def sliding_window_string(s, window_size):
    for i in range(len(s) - window_size + 1):
        yield s[i:i + window_size]

def function(string, window):
    result = []
    for window in sliding_window_string(s, window):
        if 'a' in window:
            result.append(window)
    return result

s = "abracadabra"
window_size = 3
print(function(s, window_size))
```

## Способ оптимизации метода скользящего окна

Иногда метод скользящего окна можно оптимизировать, чтобы избежать лишних вычислений. Рассмотрим задачу: у нас есть список чисел, и мы хотим найти максимальную сумму всех подпоследовательностей длины 3, но с оптимизацией.

```python
def max_sum_sliding_window_optimized(arr, window_size):
    if len(arr) < window_size:
        return None

    # Вычисляем сумму первого окна
    current_sum = sum(arr[:window_size])
    max_sum = current_sum

    # Перемещаем окно и обновляем сумму
    for i in range(window_size, len(arr)):
        current_sum += arr[i] - arr[i - window_size]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

arr = [1, 2, 3, 4, 5]
window_size = 3
print(max_sum_sliding_window_optimized(arr, window_size))
```

---
