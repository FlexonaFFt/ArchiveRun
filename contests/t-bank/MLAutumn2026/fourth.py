n, k = map(int, input().split())

left, right = 1, n
answer = []

while left < right and k >= right - left:
    answer.append(right)
    k -= right - left
    right -= 1

# Здесь k < right - left.
# Число left + k образует k инверсий с числами left ... left + k - 1
answer.append(left + k)
answer.extend(range(left, left + k))
answer.extend(range(left + k + 1, right + 1))

print(*answer)
