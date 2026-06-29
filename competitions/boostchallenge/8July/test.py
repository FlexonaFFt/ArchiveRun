class Answer:
    __slots__ = ('sum', 'field')
    def __init__(self, s, f):
        self.sum, self.field = s, f

def solution(n: int) -> Answer:
    if n == 1:                       
        return Answer(0, ['x'])

    inner_minus = ((n - 2) ** 2) // 2
    edge_minus  = 2 * (n - 2) - ((n - 2) & 1)   
    corner_minus = 2 - (n & 1)
    total = 4 * inner_minus + 3 * edge_minus + 2 * corner_minus

    if n > 100:
        field = []
    else:
        field = [
            ''.join('x' if (i + j) % 2 == 0 else '-' for j in range(n))
            for i in range(n)
        ]

    return Answer(total, field)
