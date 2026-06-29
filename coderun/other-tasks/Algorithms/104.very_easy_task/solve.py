# Решение выдает неправильный ответ, всегда на 1 больше нужного
def can_copy_time(time, n, x, y):
    copies = 0
    copies += time // x
    copies += time // y
    return copies >= n

def find_the_min_time_func(n, time1, time2):
    left = n * min(time1, time2)
    right = n * max(time1, time2)

    while left < right:
        mid = (left + right) // 2
        if can_copy_time(mid, n, time1, time2):
            right = mid
        else:
            left = mid + 1
    return left

def main():
    n, time1, time2 = map(int, input().split())
    print(find_the_min_time_func(n, time1, time2))

if __name__ == '__main__':
    main()
