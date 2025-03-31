class Solution:
    def yaGolodny(self, n: int, e: int, s: int) -> float:
        # Граф — путь 1–2–...–N
        graph = {}
        for i in range(1, n + 1):
            graph[i] = []
            if i > 1:
                graph[i].append(i - 1)  # Предыдущая вершина
            if i < n:
                graph[i].append(i + 1)  # Следующая вершина

        # Математическое ожидание P(X)
        P = [0.0] * (n + 1)
        P[e] = 0

        # Итеративный метод
        for _ in range(1000):
            new_P = P.copy()
            for x in range(1, n + 1):
                if x == e:
                    continue
                degree = len(graph[x])
                sum_neighbors = sum(P[y] for y in graph[x])
                new_P[x] = 1 + (1 / degree) * sum_neighbors
            P = new_P

        return round(P[s], 4)


def test():
    solution = Solution()
    print(solution.yaGolodny(3, 2, 1))  # Ожидаемый вывод: 1.5
    print(solution.yaGolodny(4, 1, 3))  # Ожидаемый вывод: 2.6667


def main():
    solution = Solution()
    n, e, s = map(int, input().split())
    print(solution.yaGolodny(n, e, s))


if __name__ == '__main__':
    test()
