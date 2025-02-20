def funcion(stones, jewels):
    counter = 0
    for element in jewels:
        if element in stones:
            counter += 1
    return counter 

def main():
    stones = str(input())
    jewels = str(input())
    print(funcion(stones=stones, jewels=jewels))

if __name__ == '__main__':
    main()
