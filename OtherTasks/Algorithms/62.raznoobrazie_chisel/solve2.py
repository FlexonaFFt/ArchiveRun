# Решение прошло все тесты
def find_raznoobrazie_count(numbers):
   return len(set(numbers))

def main():
    numbers = list(map(int, input().split()))
    print(find_raznoobrazie_count(numbers))

if __name__ == '__main__':
    main()
