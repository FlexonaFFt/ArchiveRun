from functools import lru_cache
from collections import defaultdict

n = 11
neighbors = {i: ((i - 3) % n, (i + 3) % n) for i in range(n)}

dp = defaultdict(int)
dp[0] = 1

masks = list(range(1<<n))
masks.sort(key=lambda x: bin(x).count("1"))

for mask in masks:
    ways = dp.get(mask, 0)
    if ways == 0:
        continue

    for i in range(n):
        if not (mask & (1<<i)):
            a, b = neighbors[i]
            if not ((mask & (1<<a)) and (mask & (1<<b))):
                newmask = mask | (1<<i)
                dp[newmask] += ways

answer = sum(ways for mask, ways in dp.items() if bin(mask).count("1") == 10)
print(answer)
