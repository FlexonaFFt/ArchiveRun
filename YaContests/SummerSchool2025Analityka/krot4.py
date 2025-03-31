import numpy as np

class Solution:
    def yaGolodny(self, n: int, e: int, s: int) -> float:
        # Создаем матрицу A и вектор b
        A = np.zeros((n, n))
        b = np.zeros(n)

        for i in range(n):
            if i == s:
                A[i][i] = 1  # У кладовки время равно 0
                b[i] = 0
            else:
                total_prob = 0
                for j in range(n):
                    distance = min(abs(j - s), n - abs(j - s))  # Расстояние до кладовки
                    prob = (n - distance) / n  # Вероятность перехода
                    A[i][j] -= prob
                    total_prob += prob
                A[i][i] += 1  # Корректируем диагональный элемент
                b[i] = 1  # Каждый шаг добавляет единицу к времени

        # Решаем систему уравнений
        try:
            f = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            raise ValueError("Система уравнений не имеет решения")

        # Возвращаем математическое ожидание для начальной вершины E
        return f[e]

def test():
    solution = Solution()
    print(solution.yaGolodny(3, 2, 1))  # Ожидаемый вывод: 1.5
    print(solution.yaGolodny(4, 1, 3))  # Ожидаемый вывод: 2.66667

def main():
    solution = Solution()
    n, e, s = map(int, input().split())
    print(solution.yaGolodny(n, e, s))

if __name__ == '__main__':
    test()
