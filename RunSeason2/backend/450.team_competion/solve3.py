# Не является решением задачи
def min_complexity(n, complexities):
    from itertools import product
    min_total_complexity = float("inf")

    for distribution in product(range(len(complexities)), repeat=n):
        total_complexity = 0
        for task_index in range(n):
            participant_index = distribution[task_index]
            total_complexity += complexities[participant_index][task_index]
        min_total_complexity = min(min_total_complexity, total_complexity)
    return min_total_complexity

def main():
    n = int(input())
    complexities = [list(map(int, input().split())) for _ in range(3)]
    rezult = min_complexity(n, complexities)
    print(rezult)

if __name__ == '__main__':
    main()
