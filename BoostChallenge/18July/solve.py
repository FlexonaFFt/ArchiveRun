mod = 998244353

def modinv(a):
    return pow(a, mod - 2, mod)

def calculate_answer(n, s):
    total = n * (n - 1) // 2
    attractive = 0
    for l in range(n):
        for r in range(l + 1, n, 2):
            m = r - l + 1
            w = s[l:r+1]
            for i in range(m // 2):
                if w[i] == w[m - i - 1]:
                    attractive += 1
                    break
    if attractive == total:
        return 1
    if attractive == 0:
        return pow(2, total, mod)
    num = (total * pow(2, total, mod)) % mod
    den = attractive
    return (num * modinv(den)) % mod

class FastInput:
    def __init__(self):
        import sys
        self.stdin = sys.stdin

    def read_line(self):
        return self.stdin.readline().strip()

    def read_tokens(self):
        return self.read_line().split()

    def read_int(self):
        return int(self.read_line())

    def read_ints(self):
        return map(int, self.read_tokens())

def solution():
    s = '01'
    s1 = '1001'
    s2 = '110001110111001011'
    n = len(s)
    n1 = len(s1)
    n2 = len(s2)
    answer = calculate_answer(n, s)
    print(answer)
    print(calculate_answer(n1,s1))
    print(calculate_answer(n2,s2))
