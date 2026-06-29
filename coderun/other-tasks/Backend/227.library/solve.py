def base():
    k, m, d = map(int, input().split())
    days_until_weekend = 7 - d + 1
    books_per_day = k
    total_books = books_per_day * days_until_weekend

    if total_books <= m:
        print(days_until_weekend)
    else:
        remaining_books = m - (total_books - books_per_day)
        days_in_weekend = remaining_books // books_per_day
        print(days_until_weekend + days_in_weekend)

if __name__ == '__main__':
    base()
