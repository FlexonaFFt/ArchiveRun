# Неправильно решает задачу
def find_equation_solve(a, b, c):
    import math
    non_solve, many_solve, solves = 'NO SOLUTION', 'MANY SOLUTIONS', []
    for x in range(-1000, 1000):
        if math.sqrt(a * x + b) == c:
            solves.append(x)
    if len(solves) == 0:
        print(non_solve)
    else:
        for iter in solves:
            print(iter)

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    find_equation_solve(a, b, c)

if __name__ == '__main__':
    main()
