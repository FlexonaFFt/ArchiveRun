# Возникает ошибка на первом закрытом тесте
def find_the_truth(n, statements):
    truth_count = 0
    for i in range(n):
        a_i, b_i = statements[i]
        if a_i + b_i == n - 1:
            truth_count += 1
    return truth_count

def main():
    n = int(input())
    statements = [tuple(map(int, input().split())) for _ in range(n)]
    print(find_the_truth(n, statements))

if __name__ == '__main__':
    main()
