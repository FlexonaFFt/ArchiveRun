# Решение не проходит 47 тест по времени
def minimize_stress(n, tasks):
    tasks.sort(key=lambda x: -x[1])
    days = [False] * (200001)
    total_stress = 0

    for deadline, stress in tasks:
        for day in range(deadline, 0, -1):
            if not days[day]:
                days[day] = True
                break
        else:
            total_stress += stress

    return total_stress

def main():
    n = int(input())
    tasks = [tuple(map(int, input().split())) for _ in range(n)]
    print(minimize_stress(n, tasks))

if __name__ == '__main__':
    main()
