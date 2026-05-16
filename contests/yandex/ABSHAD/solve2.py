import numpy as np
pattern = "АБТАБТ"
n = len(pattern)

alphabet = ['А', 'Б', 'Т']
probs = {'А': 16/41, 'Б': 13/41, 'Т': 12/41}

def next_state(i, c):
    s = pattern[:i] + c
    for k in range(min(n, i+1), 0, -1):
        if s[-k:] == pattern[:k]:
            return k
    return 0

A = np.zeros((n+1, n+1))
b = np.zeros(n+1)

A[n][n] = 1
b[n] = 0

for i in range(n):
    A[i][i] = 1
    b[i] = 1  
    for c in alphabet:
        j = next_state(i, c)
        A[i][j] -= probs[c]


E = np.linalg.solve(A, b)
print(f"{E[0]:.10f}")
