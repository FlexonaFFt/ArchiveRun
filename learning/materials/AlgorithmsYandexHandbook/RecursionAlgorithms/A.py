def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f'{source} {target}')
        return 1
    else:
        count = 0
        count += hanoi(n-1, source, auxiliary, target)
        print(f"{source} {target}")
        count += 1
        count += hanoi(n-1, auxiliary, target, source)
        return count

def main():
    n = int(input())
    total_woves = (2 ** n) - 1
    print(total_woves)
    hanoi(n, 1, 3, 2)

if __name__ == '__main__':
    main()
