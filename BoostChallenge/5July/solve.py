def solution(n: int, a: list[int]) -> int:
    from collections import defaultdict

    left = 0
    freq = defaultdict(int)
    max_len = 0

    for right in range(n):
        freq[a[right]] += 1

        while len(freq) > 2:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1

        if len(freq) == 2:
            max_len = max(max_len, right - left + 1)

    return max_len

