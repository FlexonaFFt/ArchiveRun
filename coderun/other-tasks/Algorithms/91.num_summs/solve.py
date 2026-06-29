# не является решением задачи
def count_segments(n, k, cars):
    count, current_sum, start = 0, 0, 0
    for end in range(n):
        current_sum += cars[end]
        while current_sum > k and start <= end:
            current_sum -= cars[start]
            start += 1
        if current_sum == k:
            count += 1
            temp_start = start
            while temp_start <= end and current_sum == k:
                count += 1
                current_sum -= cars[temp_start]
                temp_start += 1
            current_sum = sum(cars[temp_start:end+1]) if temp_start <= end else 0
    return count

def main():
    n, k = map(int, input().split())
    cars = list(map(int, input().split()))
    print(count_segments(n, k, cars))

if __name__ == '__main__':
    main()
