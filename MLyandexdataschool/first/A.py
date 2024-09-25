# Решение зачтено
def construct_matrix(massiv1, massiv2):
    import numpy as np
    return np.dstack([massiv1, massiv2])

if __name__ == '__main__':
    mas1 = list(map(int, input().split()))
    mas2 = list(map(int, input().split()))
    print(construct_matrix(mas1, mas2))
