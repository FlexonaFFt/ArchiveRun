def main():
    n = int(input())
    bukvas = []
    for _ in range(n):
        bukvas.append(int(input()))

    # решение
    answer = 0
    for i in range(1, n):
        answer += min(bukvas[i], bukvas[i - 1])
    print(answer)

if __name__ == '__main__':
    main()