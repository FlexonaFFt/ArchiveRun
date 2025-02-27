import numpy as np
from random import random
from matplotlib import pyplot as plt

def f(a, x):
    return a * x

x = np.linspace(0, 10, 100)
y_o = np.array([f(3, t) + 5 * (-0.5 + random()) for t in x])
w, h = random(), 0.01
for i in range(x.shape[0]):
    y = w * x[i]
    dw = -h * (y * y_o) * x[i]
    w = w + dw
