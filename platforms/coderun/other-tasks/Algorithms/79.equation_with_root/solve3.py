def find_equation_solve(a, b, c):
    non_solve, many_solve, solves = 'NO SOLUTION', 'MANY SOLUTIONS', []
    if c < 0:
        return non_solve
    c_squared = c ** 2
    if a == 0:
        if b == c_squared:
            return many_solve
        else:
            return non_solve
    if a > 0:
        if (c_squared - b) % a == 0:
            x = (c_squared - b) // a
            return x
        else:
            return non_solve
    if a < 0:
        if c_squared < b:
            return non_solve
        else:
            x = (c_squared - b) // a
            return x

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(find_equation_solve(a, b, c))

if __name__ == '__main__':
    main()
