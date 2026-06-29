# Не является решением задачи
def find_equation_solve(a, b, c):
    from math import sqrt
    non_solve, many_solve = 'NO SOLUTION', 'MANY SOLUTIONS'
    if a == 0:
        if b == c:
            return many_solve
        else:
            return non_solve
    else:
        diff = (c - b)
        if diff % a == 0:
            x_min = (diff // a)
            x_max = (diff // a)
            solutions = []
            while x_min <= x_max:
                solutions.append(str(x_min))
                x_min += 1
            return '\n'.join(solutions)
        else:
            return non_solve

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(find_equation_solve(a, b, c))

if __name__ == '__main__':
    main()
