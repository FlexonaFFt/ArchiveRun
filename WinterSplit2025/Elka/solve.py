def solve(number):
    spisok = [] 
    for k in range(1, number + 1):
        numb = 2 ** (k - 1)
        spisok.append(numb)
    answer = sum(spisok)
    return answer

def main():
    number = int(input())
    print(solve(number))

if __name__ == '__main__':
    main()
