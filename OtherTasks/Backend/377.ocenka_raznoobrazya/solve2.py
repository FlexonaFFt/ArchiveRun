def calculate_diversity(n, products, order):
    from collections import defaultdict
    category_positions = defaultdict(list)
    for product_id, category_id in products:
        category_positions[category_id].append(product_id)
    position_map = {product_id: idx for idx, product_id in enumerate(order)}

    min_difference = float("inf")
    for category, product_ids in category_positions.items():
        positions = [position_map[pid] for pid in product_ids]
        positions.sort()

        for i in range(1, len(positions)):
            diff = positions[i] - positions[i - 1]
            min_difference = min(min_difference, diff)

    if min_difference == float('inf'):
        return n
    else:
        return min_difference

def main():
    n = int(input())
    products = [tuple(map(int, input().split())) for _ in range(n)]
    order = list(map(int, input().split()))
    print(calculate_diversity(n, products, order))

if __name__ == '__main__':
    main()
