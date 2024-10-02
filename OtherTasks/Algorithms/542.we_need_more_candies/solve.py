# Не является решением задачи
def min_candies(n, list):
    min_addictions = float('inf')
    unique_values = sorted(set(list))
    if len(unique_values) <= 2:
        return 0

    for i in range(len(unique_values)):
        for j in range(i + 1, len(unique_values)):
            v1 = unique_values[i]
            v2 = unique_values[j]
            addictions = 0
            for candy_count in list:
                if candy_count < v1:
                    addictions += (v1 - candy_count)
                elif candy_count > v2:
                    addictions += (candy_count - v2)
            min_addictions = min(min_addictions, addictions)
    return min_addictions

def main():
    n = int(input())
    listt = list(map(int, input().split()))
    print(min_candies(n, listt))

if __name__ == '__main__':
    main()
