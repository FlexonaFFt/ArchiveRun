import math

n = int(input())
result = "NO"
max_a = int(math.sqrt(n)) + 1

for a in range(max_a):
    bs = n - a * a
    b = math.isqrt(bs)
    if b * b == bs:
        result = f"{a} {b}"
        break

print(result)
