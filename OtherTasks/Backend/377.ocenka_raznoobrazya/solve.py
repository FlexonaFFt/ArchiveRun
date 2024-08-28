# Программа выдает неправильные ответы на первые два теста
# Ошибка где-то в логике алгоритма
def calculate_diversity(n, products, order):
    from collections import defaultdict

    # Словарь для хранения позиций товаров по категориям
    category_positions = defaultdict(list)

    # Заполняем словарь категориями и позициями
    for index, (product_id, category_id) in enumerate(products):
        category_positions[category_id].append(index)

    # Находим минимальную разницу позиций для каждой категории
    min_diversity = float('inf')
    for positions in category_positions.values():
        if len(positions) > 1:
            min_diversity = min(min_diversity, min(positions[i] - positions[i-1] for i in range(1, len(positions))))

    # Если все товары в разных категориях, возвращаем n
    return min_diversity if min_diversity != float('inf') else n

def main():
    n = int(input())
    products = []
    order = []
    for _ in range(n):
        item = tuple(map(int, input().split()))
        products.append(item)
    order_string = str(input())
    order_string = order_string.replace(' ', '')
    for item in order_string:
        order.append(item)
    print(calculate_diversity(n, products, order))

if __name__ == '__main__':
    main()
