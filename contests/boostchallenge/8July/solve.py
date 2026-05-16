class Answer:
    __slots__ = ['sum', 'field']
    def __init__(self, sum, field):
        self.sum = sum
        self.field = field

def solution(n):
    if n == 1:
        return Answer(0, ['x'])
    if n == 2:
        return Answer(4, ['-x', 'x-'])

    field = []
    total_sum = 0
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 1:
                row.append('-')
                
                cnt = 8
                if i == 0 or i == n-1:
                    cnt -= 3
                if j == 0 or j == n-1:
                    cnt -= 3
                if (i == 0 or i == n-1) and (j == 0 or j == n-1):
                    cnt += 1
                total_sum += cnt
            else:
                row.append('x')
        field.append(''.join(row))
    return Answer(total_sum, field)

