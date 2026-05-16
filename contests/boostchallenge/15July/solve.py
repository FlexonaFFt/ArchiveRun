import sys
import random

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def calculate_answer(n: int, points: list[Point]) -> tuple[int, int]:
    idx = list(range(n))
    tries = min(200, n * (n - 1) // 2)
    checked = set()
    for _ in range(tries):
        i, j = random.sample(idx, 2)
        if (i, j) in checked or (j, i) in checked:
            continue
        checked.add((i, j))
        ok = True
        for k in range(n):
            if k == i or k == j:
                continue
            d1 = (points[k].x - points[i].x) ** 2 + (points[k].y - points[i].y) ** 2
            d2 = (points[k].x - points[j].x) ** 2 + (points[k].y - points[j].y) ** 2
            if d1 == d2:
                ok = False
                break
        if ok:
            return i + 1, j + 1
    return 0, 0

class FastInput:
    def __init__(self):
        self.stdin = sys.stdin

    def read_line(self):
        return sys.stdin.readline().strip()

    def read_tokens(self):
        return self.read_line().split()

    def read_int(self):
        return int(self.read_line())

    def read_ints(self):
        return map(int, self.read_tokens())

def solution():
    input = FastInput()
    n = input.read_int()
    coords = list(input.read_ints())
    points = [Point(coords[i * 2], coords[i * 2 + 1]) for i in range(n)]
    first, second = calculate_answer(n, points)
    print(first, second)
