# Не проходит последний тест по времени
def find_raznoobrazie_count(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return len(unique_list)

def main():
    numbers = list(map(int, input().split()))
    print(find_raznoobrazie_count(numbers))

if __name__ == '__main__':
    main()
