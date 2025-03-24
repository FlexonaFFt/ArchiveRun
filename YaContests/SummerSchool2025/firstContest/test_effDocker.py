def find_longest_perfect_route(n, zones):
    if n < 2:
        return 0

    max_length = 0

    for i in range(n):
        left = i
        while left > 0 and zones[left - 1] <= zones[left]:
            left -= 1

        right = i
        while right < n - 1 and zones[right + 1] <= zones[right]:
            right += 1

        if left < right:
            is_mirror = True
            for j in range((right - left + 1) // 2):
                if zones[left + j] != zones[right - j]:
                    is_mirror = False
                    break

            if is_mirror:
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length

    return max_length if max_length >= 2 else 0

n = int(input())
zones = list(map(int, input().split()))
result = find_longest_perfect_route(n, zones)
print(result)
