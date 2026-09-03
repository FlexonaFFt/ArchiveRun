import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, k = data[:2]
a = data[2:]

neg = sorted(-x for x in a if x < 0)  
pos = sorted(x for x in a if x > 0)
zeros = n - len(neg) - len(pos)


def same_sign_pairs_leq(values, x):
    total = 0
    right = len(values) - 1

    for left in range(len(values)):
        while left < right and values[left] * values[right] > x:
            right -= 1

        if right <= left:
            break

        total += right - left

    return total


def count_leq(x):
    if x < 0:
        need = -x
        first_good = len(neg)
        total = 0

        for value in pos:
            while first_good > 0 and value * neg[first_good - 1] >= need:
                first_good -= 1
            total += len(neg) - first_good

        return total

    total = len(neg) * len(pos)
    total += zeros * (n - zeros) + zeros * (zeros - 1) // 2
    total += same_sign_pairs_leq(neg, x)
    total += same_sign_pairs_leq(pos, x)

    return total


a.sort()
candidates = [a[0] * a[1], a[0] * a[-1], a[-2] * a[-1]]
left, right = min(candidates), max(candidates)

while left < right:
    middle = (left + right) // 2

    if count_leq(middle) >= k:
        right = middle
    else:
        left = middle + 1

print(left)
