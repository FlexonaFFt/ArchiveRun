from functools import lru_cache
from collections import Counter

def min_cost(n, prices, X, combo, k, wishlist):
    @lru_cache(None)
    def dfs(remaining):
        # Если ничего не осталось, стоимость - 0
        if all(x == 0 for x in remaining):
            return 0

        # Стоимость без использования комбо
        cost_without_combo = sum(remaining[i] * prices[i] for i in range(n))

        # Стоимость с использованием комбо
        cost_with_combo = float('inf')
        remaining_after_combo = tuple(max(0, remaining[i] - (1 if i+1 in combo else 0)) for i in range(n))

        # Проверяем, имеет ли смысл использовать комбо
        if remaining_after_combo != remaining:
            cost_with_combo = X + dfs(remaining_after_combo)

        # Возвращаем минимум из двух стратегий
        return min(cost_without_combo, cost_with_combo)

    # Начальные оставшиеся товары
    remaining = [0] * n
    for item in wishlist:
        remaining[item - 1] += 1

    return dfs(tuple(remaining))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    b = list(map(int, input().split()))
    k = int(input())
    c = list(map(int, input().split()))
    print(min_cost(n, a, x, b, k, c))
