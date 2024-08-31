# Я немного не понял как решить эту задачу

def max_days_to_read(k, m, d):
    max_days = 0
    books_needed = 1  # Коля начинает с 1 книги
    current_day = d
    available_books = m

    while True:
        if available_books >= books_needed:
            available_books -= books_needed
            max_days += 1
            books_needed += 1
        else:
            if current_day in range(1, 6):  # Понедельник - Пятница
                available_books += k
                if available_books >= books_needed:
                    available_books -= books_needed
                    max_days += 1
                    books_needed += 1
                else:
                    break
            else:
                break

        current_day = (current_day % 7) + 1  # Переход к следующему дню недели

    return max_days

def main():
    k, m, d = map(int, input().split())
    print(max_days_to_read(k, m, d))

if __name__ == '__main__':
    main()
