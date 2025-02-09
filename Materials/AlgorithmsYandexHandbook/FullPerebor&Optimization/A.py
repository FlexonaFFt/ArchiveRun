def perestanovki(n: int) -> int:
    from math import factorial
    return factorial(n)

def main():
    inp = int(input())
    print(perestanovki(inp))

if __name__ == '__main__':
    main()
