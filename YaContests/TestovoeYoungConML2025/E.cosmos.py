import numpy as np
from scipy.optimize import minimize

n = int(input())
data = []
for _ in range(n):
    x, fx = map(float, input().split())
    data.append((x, fx))

X = np.array([x for x, fx in data])
F = np.array([fx for x, fx in data])

def f(x, coeffs):
    a, b, c, d = coeffs
    return a * np.tan(x) + (b * np.sin(x) + c * np.cos(x))**2 + d * np.sqrt(x)

def loss(coeffs):
    return np.sum((F - f(X, coeffs))**2)

initial_coeffs = [1.0, 1.0, 1.0, 1.0]
result = minimize(loss, initial_coeffs, method='BFGS')
optimal_coeffs = result.x
print("{:.2f} {:.2f} {:.2f} {:.2f}".format(*optimal_coeffs))
