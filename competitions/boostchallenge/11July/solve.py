def solve(n: int, a: list[int]) -> int:
    res = 0
    stack = []
    left = [0] * n
    right = [0] * n
    for i in range(n):
        while stack and a[stack[-1]] < a[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)
    for i in range(n):
        res += (i - left[i]) * (right[i] - i) * a[i]
    stack.clear()
    left_min = [0] * n
    right_min = [0] * n
    for i in range(n):
        while stack and a[stack[-1]] > a[i]:
            stack.pop()
        left_min[i] = stack[-1] if stack else -1
        stack.append(i)
    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        right_min[i] = stack[-1] if stack else n
        stack.append(i)
    for i in range(n):
        res -= (i - left_min[i]) * (right_min[i] - i) * a[i]
    return res

