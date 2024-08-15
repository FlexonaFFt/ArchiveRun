class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res

def minimize_stress(n, tasks):
    # Сортируем задачи по дедлайнам
    tasks.sort(key=lambda x: x[0])

    # Создаем сегментное дерево
    seg_tree = SegmentTree(200000)
    total_stress = 0

    for deadline, stress in tasks:
        # Проверяем, сколько дней свободно до deadline
        free_days = seg_tree.query(1, deadline)

        # Если есть свободный день, занимаем его
        if free_days > 0:
            seg_tree.update(free_days, 1)
        else:
            total_stress += stress

    return total_stress

def main():
    n = int(input())
    tasks = [tuple(map(int, input().split())) for _ in range(n)]
    print(minimize_stress(n, tasks))

if __name__ == '__main__':
    main()
