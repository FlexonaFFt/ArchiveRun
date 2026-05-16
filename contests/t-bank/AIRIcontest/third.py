import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]

    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]

    freq = {}Vj
    left = 0
    right = -1
    bad = 0

    while left <= n - 1:
        while right + 1 <= n and freq.get(prefix[right + 1], 0) == 0:
            right += 1
            value = prefix[right]
            freq[value] = freq.get(value, 0) + 1

        bad += right - left

        lv = prefix[left]
        freq[lv] -= 1
        if freq[lv] == 0:
            del freq[lv]
        left += 1

    total = n * (n + 1) // 2
    normal = total - bad
    print(normal)


if __name__ == "__main__":
    main()
