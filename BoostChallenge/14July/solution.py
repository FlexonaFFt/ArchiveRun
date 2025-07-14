import sys
import threading
from math import gcd
from collections import Counter

def calculate_answer(n: int, k: int, a: list[int]) -> int:
    b = [x // k for x in a if x % k == 0]
    if len(b) < 2:
        return 0

    max_b = max(b)
    cnt = [0] * (max_b + 2)
    for x in b:
        cnt[x] += 1

    freq = [0] * (max_b + 2)
    for d in range(1, max_b + 1):
        for mult in range(d, max_b + 1, d):
            freq[d] += cnt[mult]

    pairs = [0] * (max_b + 2)
    for d in range(max_b, 0, -1):
        pairs[d] = freq[d] * (freq[d] - 1) // 2
        mult = 2 * d
        while mult <= max_b:
            pairs[d] -= pairs[mult]
            mult += d

    return pairs[1]

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
    t = input.read_int()
    answers = [None] * t
    for test in range(t):
        n, k = input.read_ints()
        a = list(input.read_ints())
        answers[test] = calculate_answer(n, k, a)
    print('\n'.join(map(str, answers)))

if __name__ == "__main__":
    threading.Thread(target=solution).start()

