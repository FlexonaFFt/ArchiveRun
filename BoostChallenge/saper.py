class Answer:
    __slots__ = ('sum', 'field')
    def __init__(self, sum, field):
        self.sum = sum
        self.field = field

def solution(n: int) -> Answer:
    if n == 1:
        return Answer(0, ['x'])

    # точная формула
    if n % 2 == 1:
        total_sum = 4 * (n - 1) * (n - 1)
    else:
        total_sum = 4 * (n - 1) * (n - 2) + 2 * n

    # шахматное поле, мины в клетках i+j чётно
    field = [
        ''.join('x' if (i + j) % 2 == 0 else '-' for j in range(n))
        for i in range(n)
    ]
    return Answer(total_sum, field)

ans = solution(1)
print(ans.sum)      # 0
print(ans.field)    # ['x']

ans = solution(2)
print(ans.sum)      # 4
print(ans.field)    # ['-x', 'x-']

ans = solution(3)
print(ans.sum)
print(ans.field)

ans = solution(4)
print(ans.sum)
print(ans.field)

ans = solution(6)
print(ans.sum)
print(ans.field)
