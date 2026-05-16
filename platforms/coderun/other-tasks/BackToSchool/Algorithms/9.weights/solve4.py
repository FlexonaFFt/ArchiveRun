def function(n, weights):
    possible_weights = {0}

    # Для каждой гири обновляем множество достижимых весов
    for weight in weights:
        new_weights = set()
        for w in possible_weights:
            new_weights.add(w + weight)  # Гиря на одной чаше
            new_weights.add(abs(w - weight))  # Гиря на другой чаше
        possible_weights.update(new_weights)

    # Проверяем, можно ли взвесить все веса от 1 до n
    for i in range(1, n + 1):
        if i not in possible_weights:
            return "No"
    return "Yes"

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    print(function(n, weights=weights))

if __name__ == '__main__':
    main()
